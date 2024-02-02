import asyncio
import pathlib
import warnings
from typing import Generator, Any, Dict, List, Union, Optional
import logging
import nodriver.core.browser
import mss
from .connection import SimpleConnection, ProtocolException
from .. import cdp
from . import element
from . import util

logger = logging.getLogger(__name__)


class Target(SimpleConnection):
    browser: nodriver.core.browser.Browser

    def __init__(self, websocket_url: str, target: cdp.target.TargetInfo, **kwargs):
        super().__init__(websocket_url, target, **kwargs)
        self._dom = None
        self._window_id = None

    def __getattr__(self, item):
        try:
            return getattr(self._target, item)
        except AttributeError:
            raise AttributeError(
                f'"{self.__class__.__name__}" has no attribute "%s"' % item
            )

    def __repr__(self):
        s = f"<{type(self).__name__} [{self.target_id}] [{self.type_}]>"
        return s

    async def query_selector_all(
        self,
        selector: str,
        _node: Optional[Union[cdp.dom.Node, "nodriver.Element"]] = None,
    ):
        if not _node:
            doc: cdp.dom.Node = await self.send(cdp.dom.get_document(-1, True))
        else:
            doc = _node
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
            elem = element.create(node, self, doc)
            results.append(elem)
        try:
            await self.send(cdp.dom.disable())
            for handler in self.handlers.copy():
                if "cdp.dom" in handler.__module__:
                    try:
                        self.handlers.pop(handler)
                    except:
                        pass
        except:
            raise

        return results

    async def query_selector(self, selector: str):
        """
        find single element based on css selector string

        :param selector: css selector(s)
        :type selector: str
        :return:
        :rtype:
        """
        doc = await self.send(cdp.dom.get_document(-1, True))
        node_id = await self.send(cdp.dom.query_selector(doc.node_id, selector))
        if not node_id:
            return
        node = util.filter_recurse(doc, lambda n: n.node_id == node_id)
        return await element.create(node, self, doc)


    async def find_elements_by_text(
        self, text: str, return_enclosing_element: bool = True
    ):
        """

        :param text:
        :type text:
        :param return_enclosing_element: if False, it returns the textual element,
                but usually one needs the element containing the text, like a button. default = True
        :type return_enclosing_element: bool
        :return:
        :rtype:
        """
        # if cdp.dom not in self.enabled_domains:
        #     await self.send(cdp.dom.enable())
        #     self.enabled_domains.append(cdp.dom)
        doc = await self.send(cdp.dom.get_document(-1, True))
        search_id, nresult = await self.send(cdp.dom.perform_search(text, True))
        if nresult == 0:
            return []
        node_ids = await self.send(cdp.dom.get_search_results(search_id, 0, nresult))
        #
        # doc: cdp.dom.Node = await self.send(cdp.dom.get_document(-1, True))
        # node_ids = await self.send(cdp.dom.query_selector_all(doc.node_id, '*'))
        # if not node_ids:
        #     return []
        results = []
        for nid in node_ids:
            node = util.filter_recurse(doc, lambda n: n.node_id == nid)
            if node:
                try:
                    elem = element.create(node, self, doc)
                except:
                    continue
                if return_enclosing_element:
                    await elem.update()
                    elem = elem.parent
                results.append(elem)
        try:
            await self.send(cdp.dom.discard_search_results(search_id))
            await self.send(cdp.dom.disable())
            for event_type in self.handlers.copy():
                if "cdp.dom" in event_type.__module__:
                    if event_type in self.handlers:
                        self.handlers.pop(event_type)
        except:
            logger.debug("", exc_info=True)
        return results

    async def find_element_by_text(self, text: str, return_enclosing_element=True):
        doc = await self.send(cdp.dom.get_document(-1, True))
        search_id, nresult = await self.send(cdp.dom.perform_search(text, True))
        if nresult == 0:
            return
        node_ids = await self.send(cdp.dom.get_search_results(search_id, nresult-1, nresult))
        if not node_ids:
            return
        node_id = node_ids[0]
        node = util.filter_recurse(doc, lambda n: n.node_id == node_id)
        if not node:
            return
        elem = element.create(node, self, doc)
        if return_enclosing_element:
            if elem.node_type == 3:  # apply only if is text node
                await elem.update()
                elem = elem.parent
                return elem
        await self.send(cdp.dom.discard_search_results(search_id))
        await self.send(cdp.dom.disable())
        for event_type in self.handlers.copy():
            if "cdp.dom" in event_type.__module__:
                if event_type in self.handlers:
                    self.handlers.pop(event_type)
        return elem



    async def back(self):
        await self.send(cdp.runtime.evaluate("window.history.back()"))

    async def forward(self):
        await self.send(cdp.runtime.evaluate("window.history.forward()"))

    async def close_target(self):
        if self.target and self.target.target_id:
            await self.send(cdp.target.close_target(target_id=self.target.target_id))

    async def get_window(self) -> cdp.browser.Bounds:
        self._window_id, bounds = await self.send(
            cdp.browser.get_window_for_target(self.target_id)
        )
        return bounds

    async def maximize(self):
        return await self.set_window_state(state_name="maximize")

    async def minimize(self):
        return await self.set_window_state(state_name="minimize")

    async def set_window_size(self, left=0, top=0, width=1280, height=1024):
        return await self.set_window_state(left, top, width, height)

    async def activate_target(self):
        await self.send(cdp.target.activate_target(self.target.target_id))

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
        if not self._window_id:
            await self.get_window()

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
            current_bounds = await self.get_window()
            if current_bounds.window_state != cdp.browser.WindowState.NORMAL:
                # min, max, full can only be used when current state == NORMAL
                # therefore we first switch to NORMAL
                await self.set_window_size(state="normal")
            bounds = cdp.browser.Bounds(window_state=window_state)

        await self.send(cdp.browser.set_window_bounds(self._window_id, bounds=bounds))

    async def download_file(self, url=None, filename=None):
        """downloads file by given url (or current page if not provided)

        :param url: url of the file. if not specified: current url
        :param filename: the name for the file. if not specified the name is composed from the url file name
        """
        directory_path = pathlib.Path.cwd() / "downloads"
        directory_path.mkdir(exist_ok=True)

        warnings.warn(
            f"filename or download path is not a folder,"
            f"so it's location is automatically set to {directory_path}"
        )
        await self.send(
            cdp.browser.set_download_behavior(
                "allow", download_path=str(directory_path)
            )
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

        # await .close()

    async def get_all_linked_sources(self) -> List["nodriver.Element"]:
        """get all elements of tag: link, a, img, scripts meta, video, audio
        :return:
        """
        all_assets = await self.query_selector_all(selector="a,link,img,script,meta")
        return all_assets or []

    async def get_all_urls(self, absolute=True):
        """extract all the src and href properties from link, a, img, scripts and meta tags
        rebuilds urls to
        :return:
        """

        import urllib.parse

        res = []
        all_assets = await self.query_selector_all(selector="a,link,img,script,meta")
        for asset in all_assets:
            if not absolute:
                res.append(asset.src or asset.href)
            else:
                for k, v in asset.attrs.items():
                    print("k v ", k, v)
                    if k in ("src", "href"):
                        print(k, "in src,href")
                        if "#" in v:
                            print("# found")
                            continue
                        if not any([_ in v for _ in ("http", "//", "/")]):
                            print('not any any([_ in v for _ in ("http", "//", "/")])')
                            continue
                        abs_url = urllib.parse.urljoin(
                            "/".join(self.url.rsplit("/")[:3]), v
                        )
                        if not abs_url.startswith(("http", "//", "ws")):
                            continue
                        res.append(abs_url)
        return res
