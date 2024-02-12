import asyncio
import http.cookiejar
import logging
import pathlib
import types
import typing
import warnings
from typing import List, Union, Optional, Tuple

import nodriver.core.browser
from . import element
from . import util
from .config import PathLike
from .connection import Connection, ProtocolException
from .. import cdp

logger = logging.getLogger(__name__)


class Tab(Connection):
    """
    :ref:`tab` is the controlling mechanism/connection to a 'target',
    for most of us 'target' can be read as 'tab'. however it could also
    be an iframe, serviceworker or background script for example,
    although there isn't much to control for those.

    if you open a new window by using :py:meth:`browser.get(..., new_window=True)`
    your url will open a new window. this window is a 'tab'.
    When you browse to another page, the tab will be the same (it is an browser view).

    So it's important to keep some reference to tab objects, in case you're
    done interacting with elements and want to operate on the page level again.

    Tab object provide many useful and often-used methods. It is also
    possible to utilize the included cdp classes to to something totally custom.

    the cdp package is a set of so-called "domains" with each having methods, events and types.
    to send a cdp method, for example :py:obj:`cdp.page.navigate`, you'll have to check
    whether the method accepts any parameters and whether they are required or not.

    you can use

    ```python
    await tab.send(cdp.page.navigate(url='https://yoururlhere'))
    ```

    so tab.send() accepts a generator object, which is created by calling a cdp method.
    this way you can build very detailed and customized commands.
    (note: finding correct command combo's can be a time consuming task, luckily i added a whole bunch
    of useful methods, preferably having the same api's or lookalikes, as in selenium)


    some useful, often needed and simply required methods
    ===================================================================

    :py:meth:`~query_selector_all`
    ----------------------------------------
    this is just like javascripts' document.querySelectorAll, which you can use
    to quickly select elements based a css selector.

    tip: you can also use `await page('.your-css-selector')`


    :py:meth:`~find_element_by_text`
    -----------------------------------------
    this is almost like query_selector all, but performs a text search and returns
    any elements that matches. This is case insensitive.

    tip: you can also use `await page(text='sign up')`

    await :py:obj:`Page`
    ---------------------------
    calling `await page` will do a lot of stuff under the hood, and ensures all references
    are up to date. also it allows for the script to "breathe", as it is oftentime faster than your browser or
    webpage. So whenever you get stuck and things crashes or element could not be found, you should probably let
    it "breathe"  by calling `await page`  and/or `await page.sleep()`

    also, it's ensuring :py:obj:`~url` will be updated to the most recent one, which is quite important in some
    other methods.


    :py:meth:`~send`
    ---------------------------
    this is probably THE most important method, although you won't ever call it, unless you want to
    go really custom. the send method accepts a :py:obj:`cdp` command. Each of which can be found in the
    cdp section.

    when you import * from this package, cdp will be in your namespace, and contains all domains/actions/events
    you can act upon.


    """

    browser: nodriver.core.browser.Browser
    _download_behavior: List[str] = None

    def __init__(
        self,
        websocket_url: str,
        target: cdp.target.TargetInfo,
        browser: Optional["nodriver.Browser"] = None,
        **kwargs,
    ):
        super().__init__(websocket_url, target, **kwargs)
        self.browser = browser
        self._dom = None
        self._window_id = None

    def __getattr__(self, item):
        try:
            return getattr(self._target, item)
        except AttributeError:
            raise AttributeError(
                f'"{self.__class__.__name__}" has no attribute "%s"' % item
            )

    async def find(
        self,
        text: Optional[str] = "",
        selector: Optional[str] = "",
        timeout: Union[int, float] = 5,
    ):
        loop = asyncio.get_running_loop()
        now = loop.time()
        if selector:
            item = await self.query_selector(selector)
            while not item:
                await self
                item = await self.query_selector(selector)
                if loop.time() - now > timeout:
                    raise asyncio.TimeoutError(
                        "time ran out while waiting for %s" % selector
                    )
                await self.sleep(0.5)
            return item
        if text:
            item = await self.find_element_by_text(text)
            while not item:
                await self
                item = await self.find_element_by_text(text)
                if loop.time() - now > timeout:
                    raise asyncio.TimeoutError(
                        "time ran out while waiting for text: %s" % text
                    )
                await self.sleep(0.5)
            return item

    async def find_all(
        self,
        text: Optional[str] = "",
        selector: Optional[str] = "",
        timeout: Union[int, float] = 5,
    ):
        loop = asyncio.get_running_loop()
        now = loop.time()
        results = []
        if selector:
            items = await self.query_selector_all(selector)
            while not items:
                await self
                items = await self.query_selector_all(selector)
                if loop.time() - now > timeout:
                    raise asyncio.TimeoutError(
                        "time ran out while waiting for %s" % selector
                    )
                await self.sleep(0.5)
            results.extend(items)
        if text:
            items = await self.find_elements_by_text(text)
            while not items:
                await self
                items = await self.find_elements_by_text(text)
                if loop.time() - now > timeout:
                    raise asyncio.TimeoutError(
                        "time ran out while waiting for text: %s" % text
                    )
                await self.sleep(0.5)
            results.extend(items)
        return results

    def __call__(
        self,
        text: Optional[str] = "",
        selector: Optional[str] = "",
        timeout: Optional[Union[int, float]] = 5,
    ):
        """
        alias to query_selector_all or find_elements_by_text, depending
        on whether text= is set or selector= is set

        :param selector: css selector string
        :type selector: str
        :return:
        :rtype:
        """
        return self.wait_for(text, selector, timeout)

    def __repr__(self):
        s = f"<{type(self).__name__} [{self.target_id}] [{self.type_}]>"
        return s

    async def get(
        self, url="chrome://welcome", new_tab: bool = False, new_window: bool = False
    ):
        """top level get. utilizes the first tab to retrieve given url.

        convenience function known from selenium.
        this function handles waits/sleeps and detects when DOM events fired, so it's the safest
        way of navigating.

        :param url: the url to navigate to
        :param new_tab: open new tab
        :param new_window:  open new window
        :return: Page
        """

        if not self.browser:
            await AttributeError(
                "this page/tab has no browser attribute, so you can't use get()"
            )

        if new_window and not new_tab:
            new_tab = True

        # get first tab
        tab = next(filter(lambda item: item.type_ == "page", self.browser.targets))

        if new_tab:
            target_id = await self.browser.connection.send(
                cdp.target.create_target(
                    url, new_window=new_window, enable_begin_frame_control=True
                )
            )
            tab = next(
                filter(
                    lambda item: item.type_ == "page" and item.target_id == target_id,
                    self.browser.targets,
                )
            )
            while not tab:
                await self.browser.wait()
                tab = next(
                    filter(
                        lambda item: item.type_ == "page"
                        and item.target_id == target_id,
                        self.browser.targets,
                    )
                )
            return tab

        else:
            frame_id, loader_id, *_ = await tab.send(cdp.page.navigate(url))
            tab.frame_id = frame_id
            await self.wait()
            return tab

    async def query_selector_all(
        self,
        selector: str,
        _node: Optional[Union[cdp.dom.Node, "element.Element"]] = None,
    ):
        """
        equivalent of javascripts document.querySelectorAll.
        this is considered one of the main methods to use in this package.

        it returns all matching :py:obj:`nodriver.Element` objects.

        :param selector: css selector. (first time? => https://www.w3schools.com/cssref/css_selectors.php )
        :type selector: str
        :param _node: internal use
        :type _node:
        :return:
        :rtype:
        """

        if not _node:
            doc: cdp.dom.Node = await self.send(cdp.dom.get_document(-1, True))
        else:
            doc = _node
            if _node.node_name == "IFRAME":
                doc = _node.content_document
        try:
            node_ids = await self.send(
                cdp.dom.query_selector_all(doc.node_id, selector)
            )
        except ProtocolException as e:
            if _node is not None:
                if "could not find node" in e.message.lower():
                    if getattr(_node, "__last", None):
                        del _node.__last
                        return []
                    # if supplied node is not found, the dom has changed since acquiring the element
                    # therefore we need to update our passed node and try again
                    await _node.update()
                    _node.__last = (
                        True  # make sure this isn't turned into infinite loop
                    )
                    return await self.query_selector_all(selector, _node)
        if not node_ids:
            return []
        results = []

        for nid in node_ids:
            node = util.filter_recurse(doc, lambda n: n.node_id == nid)
            # we pass along the retrieved document tree,
            # to improve performance
            if not node:
                continue
            elem = element.create(node, self, doc)
            results.append(elem)

        return results

    async def query_selector(
        self,
        selector: str,
        _node: Optional[Union[cdp.dom.Node, element.Element]] = None,
    ):
        """
        find single element based on css selector string

        :param selector: css selector(s)
        :type selector: str
        :return:
        :rtype:
        """
        if _node:
            doc = _node
            if _node.node_name == "IFRAME":
                doc = _node.content_document
        else:
            doc = await self.send(cdp.dom.get_document(-1, True))

        node_id = await self.send(cdp.dom.query_selector(doc.node_id, selector))
        if not node_id:
            return
        node = util.filter_recurse(doc, lambda n: n.node_id == node_id)
        if not node:
            return
        return element.create(node, self, doc)

    async def find_elements_by_text(
        self,
        text: str,
        tag_hint: Optional[str] = None,
        return_enclosing_element: Optional[bool] = True,
    ) -> List[element.Element]:
        """

        :param text:
        :type text:
        :param return_enclosing_element: if False, it returns the textual element,
                but usually one needs the element containing the text, like a button. default = True
        :type return_enclosing_element: bool
        :return:
        :rtype:
        """

        doc = await self.send(cdp.dom.get_document(-1, True))
        search_id, nresult = await self.send(cdp.dom.perform_search(text, True))
        if nresult == 0:
            return []
        node_ids = await self.send(cdp.dom.get_search_results(search_id, 0, nresult))

        results = []
        for nid in node_ids:
            node = util.filter_recurse(doc, lambda n: n.node_id == nid)
            if node:
                try:
                    elem = element.create(node, self, doc)
                    if tag_hint:
                        if elem.node_name.lower() != tag_hint.lower():
                            continue
                except:
                    continue
                if return_enclosing_element:
                    if not elem.parent:
                        await elem.update()
                    elem = elem.parent

                results.append(elem)
        iframes = util.filter_recurse_all(doc, lambda n: n.node_name == "IFRAME")
        if iframes:
            iframes = [element.create(iframe, self, doc) for iframe in iframes]
            for iframe in iframes:
                iframe_text_elems = util.filter_recurse_all(
                    iframe,
                    lambda n: n.node_type == 3 and text.lower() in n.node_value.lower(),
                )
                if return_enclosing_element:
                    if not iframe.parent:
                        await iframe.update()
                    results.extend(elem.parent for elem in iframe_text_elems)
                else:
                    results.extend(iframe_text_elems)
        return results

    async def find_element_by_text(
        self, text: str, return_enclosing_element: Optional[bool] = True
    ) -> element.Element:
        """

        :param text:
        :type text:
        :param return_enclosing_element:
        :type return_enclosing_element:
        :return:
        :rtype:
        """
        doc = await self.send(cdp.dom.get_document(-1, True))
        search_id, nresult = await self.send(cdp.dom.perform_search(text, True))
        if nresult == 0:
            return
        node_ids = await self.send(
            cdp.dom.get_search_results(search_id, nresult - 1, nresult)
        )
        if not node_ids:
            return
        node_id = node_ids[0]
        node = util.filter_recurse(doc, lambda n: n.node_id == node_id)
        if not node:
            return
        elem = element.create(node, self, doc)
        if return_enclosing_element:
            if elem.node_type == 3:  # apply only if is text node
                if not elem.parent:
                    await elem.update()
                elem = elem.parent
                return elem
        await self.send(cdp.dom.discard_search_results(search_id))
        await self.send(cdp.dom.disable())
        for event_type in self.handlers.copy():
            if isinstance(event_type, types.ModuleType):
                if "cdp.dom" in event_type.__name__:
                    if event_type in self.handlers:
                        self.handlers.pop(event_type)
            else:
                if event_type in self.handlers:
                    self.handlers.pop(event_type)
        return elem

    async def back(self):
        """
        history back
        """
        await self.send(cdp.runtime.evaluate("window.history.back()"))

    async def forward(self):
        """
        history forward
        """
        await self.send(cdp.runtime.evaluate("window.history.forward()"))

    async def reload(
        self,
        ignore_cache: Optional[bool] = True,
        script_to_evaluate_on_load: Optional[str] = None,
    ):
        """
        Reloads the page

        :param ignore_cache: when set to True (default), it ignores cache, and re-downloads the items
        :type ignore_cache:
        :param script_to_evaluate_on_load: script to run on load. I actually haven't experimented with this one, so no guarantees.
        :type script_to_evaluate_on_load:
        :return:
        :rtype:
        """
        await self.send(
            cdp.page.reload(
                ignore_cache=ignore_cache,
                script_to_evaluate_on_load=script_to_evaluate_on_load,
            ),
        )

    async def close(self):
        """
        close the current target (ie: tab,window,page)
        :return:
        :rtype:
        """
        if self.target and self.target.target_id:
            await self.send(cdp.target.close_target(target_id=self.target.target_id))

    async def get_window(self) -> Tuple[cdp.browser.WindowID, cdp.browser.Bounds]:
        """
        get the window Bounds
        :return:
        :rtype:
        """
        window_id, bounds = await self.send(
            cdp.browser.get_window_for_target(self.target_id)
        )
        return window_id, bounds

    async def get_all_cookies(
        self, requests_cookie_format: bool = False
    ) -> List[Union[cdp.network.Cookie, "http.cookiejar.Cookie"]]:
        """
        get all cookies

        :param requests_cookie_format: when True, returns python http.cookiejar.Cookie objects, compatible  with requests library and many others.
        :type requests_cookie_format: bool
        :return:
        :rtype:

        """

        cookies = await self.send(cdp.storage.get_cookies())
        if requests_cookie_format:
            import requests.cookies

            return [
                requests.cookies.create_cookie(
                    name=c.name,
                    value=c.value,
                    domain=c.domain,
                    path=c.path,
                    expires=c.expires,
                    secure=c.secure,
                )
                for c in cookies
            ]
        return cookies

    async def get_content(self):
        """
        gets the current page source content (html)
        :return:
        :rtype:
        """
        doc: cdp.dom.Node = await self.send(cdp.dom.get_document(-1, True))
        return await self.send(
            cdp.dom.get_outer_html(backend_node_id=doc.backend_node_id)
        )

    async def set_all_cookies(self, cookies: List[cdp.network.CookieParam]):
        """
        set cookies

        :param cookies: list of cookies
        :type cookies:
        :return:
        :rtype:
        """
        await self.send(cdp.storage.set_cookies(cookies))

    async def maximize(self):
        """
        maximize page/tab/window
        """
        return await self.set_window_state(state="maximize")

    async def minimize(self):
        """
        minimize page/tab/window
        """
        return await self.set_window_state(state="minimize")

    async def fullscreen(self):
        """
        minimize page/tab/window
        """
        return await self.set_window_state(state="fullscreen")

    async def medimize(self):
        return await self.set_window_state(state="normal")

    async def set_window_size(self, left=0, top=0, width=1280, height=1024):
        """
        set window size and position

        :param left: pixels from the left of the screen to the window top-left corner
        :type left:
        :param top: pixels from the top of the screen to the window top-left corner
        :type top:
        :param width: width of the window in pixels
        :type width:
        :param height: height of the window in pixels
        :type height:
        :return:
        :rtype:
        """
        return await self.set_window_state(left, top, width, height)

    async def activate(self):
        """
        active this target (ie: tab,window,page)
        """
        await self.send(cdp.target.activate_target(self.target.target_id))

    async def bring_to_front(self):
        """
        alias to self.activate
        """
        await self.activate()

    async def set_window_state(
        self, left=0, top=0, width=1280, height=720, state="normal"
    ):
        """
        sets the window size and state.
        in case state is set other than "normal", the left, top, width, and height are ignored.

        :param left:
            desired offset from left, in pixels
        :type left: int

        :param top:
            desired offset from the top, in pixels
        :type top: int

        :param width:
            desired width in pixels
        :type width: int

        :param height:
            desired height in pixels
        :type height: int

        :param state:
            can be one of the following strings:
                - normal
                - fullscreen
                - maximized
                - minimized

        :type state: str

        """
        available_states = ["minimized", "maximized", "fullscreen", "normal"]
        window_id: cdp.browser.WindowID
        bounds: cdp.browser.Bounds
        (window_id, bounds) = await self.get_window()

        for state_name in available_states:
            if all(x in state_name for x in state.lower()):
                break
        else:
            raise NameError(
                "could not determine any of %s from input '%s'"
                % (",".join(available_states), state)
            )
        window_state = getattr(
            cdp.browser.WindowState, state_name.upper(), cdp.browser.WindowState.NORMAL
        )
        if window_state == cdp.browser.WindowState.NORMAL:
            bounds = cdp.browser.Bounds(left, top, width, height, window_state)
        else:
            window_id, current_bounds = await self.get_window()
            if current_bounds.window_state != cdp.browser.WindowState.NORMAL:
                # min, max, full can only be used when current state == NORMAL
                # therefore we first switch to NORMAL
                await self.set_window_state(state="normal")
            bounds = cdp.browser.Bounds(window_state=window_state)

        await self.send(cdp.browser.set_window_bounds(window_id, bounds=bounds))

    async def scroll_down(self, amount=25):
        """
        scrolls down maybe

        :param amount: number in percentage. 25 is a quarter of page, 50 half, and 1000 is 10x the page
        :type amount: int
        :return:
        :rtype:
        """
        window_id: cdp.browser.WindowID
        bounds: cdp.browser.Bounds
        (window_id, bounds) = await self.get_window()

        await self.send(
            cdp.input_.synthesize_scroll_gesture(
                x=0,
                y=0,
                y_distance=-(bounds.height * (amount / 100)),
                y_overscroll=0,
                x_overscroll=0,
                prevent_fling=True,
                repeat_delay_ms=0,
                speed=7777,
            )
        )

    async def scroll_up(self, amount=25):
        """
        scrolls up maybe

        :param amount: number in percentage. 25 is a quarter of page, 50 half, and 1000 is 10x the page
        :type amount: int

        :return:
        :rtype:
        """
        window_id: cdp.browser.WindowID
        bounds: cdp.browser.Bounds
        (window_id, bounds) = await self.get_window()

        await self.send(
            cdp.input_.synthesize_scroll_gesture(
                x=0,
                y=0,
                y_distance=(bounds.height * (amount / 100)),
                x_overscroll=0,
                prevent_fling=True,
                repeat_delay_ms=0,
                speed=7777,
            )
        )

    async def wait_for(
        self,
        text: Optional[str] = "",
        selector: Optional[str] = "",
        timeout: Optional[Union[int, float]] = 5,
    ) -> element.Element:
        """
        variant on query_selector_all and find_elements_by_text
        this variant takes either selector or text, and will block until
        the requested element(s) are found.

        it will block for a maximum of <timeout> seconds, after which
        an TimeoutError will be raised

        :param selector: css selector
        :type selector:
        :param text: text
        :type text:
        :param timeout:
        :type timeout:
        :return:
        :rtype: Element
        :raises: asyncio.TimeoutError
        """
        loop = asyncio.get_running_loop()
        now = loop.time()
        if selector:
            item = await self.query_selector(selector)
            while not item:
                await self
                item = await self.query_selector(selector)
                if loop.time() - now > timeout:
                    raise asyncio.TimeoutError(
                        "time ran out while waiting for %s" % selector
                    )
                await self.sleep(0.5)
            return item
        if text:
            item = await self.find_element_by_text(text)
            while not item:
                await self
                item = await self.find_element_by_text(text)
                if loop.time() - now > timeout:
                    raise asyncio.TimeoutError(
                        "time ran out while waiting for text: %s" % text
                    )
                await self.sleep(0.5)
            return item

    async def download_file(self, url: str, filename: Optional[PathLike] = None):
        """
        downloads file by given url.

        :param url: url of the file
        :param filename: the name for the file. if not specified the name is composed from the url file name
        """
        if not self._download_behavior:
            directory_path = pathlib.Path.cwd() / "downloads"
            directory_path.mkdir(exist_ok=True)
            await self.set_download_path(directory_path)

            warnings.warn(
                f"no download path set, so creating and using a default of"
                f"{directory_path}"
            )
        if not filename:
            filename = url.rsplit("/")[-1]
            filename = filename.split("?")[0]

        code = """
         (elem) => {
            async function _downloadFile(
              imageSrc,
              nameOfDownload,
            ) {
              const response = await fetch(imageSrc);
              const blobImage = await response.blob();
              const href = URL.createObjectURL(blobImage);

              const anchorElement = document.createElement('a');
              anchorElement.href = href;
              anchorElement.download = nameOfDownload;

              document.body.appendChild(anchorElement);
              anchorElement.click();

              setTimeout(() => {
                document.body.removeChild(anchorElement);
                window.URL.revokeObjectURL(href);
                }, 500);
            }
            _downloadFile('%s', '%s')
            }
            """ % (
            url,
            filename,
        )

        body = (await self.query_selector_all("body"))[0]
        await body.update()
        await self.send(
            cdp.runtime.call_function_on(
                code,
                object_id=body.object_id,
                arguments=[cdp.runtime.CallArgument(object_id=body.object_id)],
            )
        )

    async def save_screenshot(
        self,
        filename: Optional[PathLike] = "auto",
        format: Optional[str] = "jpeg",
        full_page: Optional[bool] = False,
    ) -> str:
        """
        Saves a screenshot of the page.
        This is not the same as :py:obj:`Element.save_screenshot`, which saves a screenshot of a single element only

        :param filename: uses this as the save path
        :type filename: PathLike
        :param format: jpeg or png (defaults to jpeg)
        :type format: str
        :param full_page: when False (default) it captures the current viewport. when True, it captures the entire page
        :type full_page: bool
        :return: the path/filename of saved screenshot
        :rtype: str
        """
        # noqa
        import urllib.parse
        import datetime

        await self  # update the target's url
        path = None

        if not filename or filename == "auto":
            parsed = urllib.parse.urlparse(self.target.url)
            parts = parsed.path.split("/")
            last_part = parts[-1]
            last_part = last_part.rsplit("?", 1)[0]
            dt_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            candidate = f"{parsed.hostname}__{last_part}_{dt_str}"

            if format.lower() in ["jpg", "jpeg"]:
                ext = ".jpg"
                format = "jpeg"

            elif format.lower() in ["png"]:
                ext = ".png"
                format = "png"
            path = pathlib.Path(candidate + ext)
        else:
            path = pathlib.Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        data = await self.send(
            cdp.page.capture_screenshot(format_=format, capture_beyond_viewport=True)
        )
        import base64

        data_bytes = base64.b64decode(data)
        if not path:
            raise RuntimeError("invalid filename or path: '%s'" % filename)
        path.write_bytes(data_bytes)
        return str(path)

    async def set_download_path(self, path: PathLike):
        """
        sets the download path and allows downloads
        this is required for any download function to work (well not entirely, since when unset we set a default folder)

        :param path:
        :type path:
        :return:
        :rtype:
        """
        await self.send(
            cdp.browser.set_download_behavior(
                behavior="allow", download_path=str(path.resolve())
            )
        )
        self._download_behavior = ["allow", str(path.resolve())]

    async def get_all_linked_sources(self) -> List["nodriver.Element"]:
        """
        get all elements of tag: link, a, img, scripts meta, video, audio

        :return:
        """
        all_assets = await self.query_selector_all(selector="a,link,img,script,meta")
        return [element.create(asset, self) for asset in all_assets]

    async def get_all_urls(self, absolute=True) -> List[str]:
        """
        convenience function, which returns all links (a,link,img,script,meta)

        :param absolute: try to build all the links in absolute form instead of "as is", often relative
        :return: list of urls
        """

        import urllib.parse

        res = []
        all_assets = await self.query_selector_all(selector="a,link,img,script,meta")
        for asset in all_assets:
            if not absolute:
                res.append(asset.src or asset.href)
            else:
                for k, v in asset.attrs.items():
                    if k in ("src", "href"):
                        if "#" in v:
                            continue
                        if not any([_ in v for _ in ("http", "//", "/")]):
                            continue
                        abs_url = urllib.parse.urljoin(
                            "/".join(self.url.rsplit("/")[:3]), v
                        )
                        if not abs_url.startswith(("http", "//", "ws")):
                            continue
                        res.append(abs_url)
        return res


class WaitFor:
    def __init__(self, page: Tab):
        self.page = page

    async def __call__(self, text: str = None, selector: str = None, timeout: int = 5):
        loop = asyncio.get_running_loop()
        now = loop.time()
        if selector:
            item = await self.page.query_selector_all(selector)
            while not item:
                await self.page
                item = await self.page.query_selector_all(selector)
                if loop.time() - now > timeout:
                    raise asyncio.TimeoutError(
                        "time ran out while waiting for %s" % selector
                    )
                await self.page.sleep(0.5)
            return item
        if text:
            item = await self.page.find_elements_by_text(text)
            while not item:
                await self.page
                item = await self.page.find_elements_by_text(text)
                if loop.time() - now > timeout:
                    raise asyncio.TimeoutError(
                        "time ran out while waiting for text: %s" % text
                    )
                await self.page.sleep(0.5)
            return item
