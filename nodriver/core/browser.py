# Copyright 2024 by UltrafunkAmsterdam (https://github.com/UltrafunkAmsterdam)
# All rights reserved.
# This file is part of the nodriver package.
# and is released under the "GNU AFFERO GENERAL PUBLIC LICENSE".
# Please see the LICENSE.txt file that should have been included as part of this package.

from __future__ import annotations

import asyncio
import atexit
import json
import logging
import os
import pathlib
import pickle
import urllib.parse
import urllib.request
import warnings
from collections import defaultdict
from typing import List, Tuple, Union

from .. import cdp
from . import tab, util
from ._contradict import ContraDict
from .config import Config, PathLike, is_posix
from .connection import Connection

logger = logging.getLogger(__name__)


class Browser:
    """
    The Browser object is the "root" of the hierarchy and contains a reference
    to the browser parent process.
    there should usually be only 1 instance of this.

    All opened tabs, extra browser screens and resources will not cause a new Browser process,
    but rather create additional :class:`nodriver.Tab` objects.

    So, besides starting your instance and first/additional tabs, you don't actively use it a lot under normal conditions.

    Tab objects will represent and control
     - tabs (as you know them)
     - browser windows (new window)
     - iframe
     - background processes

    note:
    the Browser object is not instantiated by __init__ but using the asynchronous :meth:`nodriver.Browser.create` method.

    note:
    in Chromium based browsers, there is a parent process which keeps running all the time, even if
    there are no visible browser windows. sometimes it's stubborn to close it, so make sure after using
    this library, the browser is correctly and fully closed/exited/killed.

    """

    _process: asyncio.subprocess.Process
    _process_pid: int
    _http: HTTPApi = None
    _cookies: CookieJar = None

    config: Config
    connection: Connection

    @classmethod
    async def create(
        cls,
        config: Config = None,
        *,
        user_data_dir: PathLike = None,
        headless: bool = False,
        browser_executable_path: PathLike = None,
        browser_args: List[str] = None,
        sandbox: bool = True,
        host: str = None,
        port: int = None,
        **kwargs,
    ) -> Browser:
        """
        entry point for creating an instance
        """
        if not config:
            config = Config(
                user_data_dir=user_data_dir,
                headless=headless,
                browser_executable_path=browser_executable_path,
                browser_args=browser_args or [],
                sandbox=sandbox,
                host=host,
                port=port,
                **kwargs,
            )
        instance = cls(config)
        await instance.start()
        return instance

    def __init__(self, config: Config, **kwargs):
        """
        constructor. to create a instance, use :py:meth:`Browser.create(...)`

        :param config:
        """

        try:
            asyncio.get_running_loop()
        except RuntimeError:
            raise RuntimeError(
                "{0} objects of this class are created using await {0}.create()".format(
                    self.__class__.__name__
                )
            )
        # weakref.finalize(self, self._quit, self)
        self.config = config

        self.targets: List = []
        """current targets (all types"""
        self.info = None
        self._target = None
        self._process = None
        self._process_pid = None
        self._keep_user_data_dir = None
        self._is_updating = asyncio.Event()
        self.connection: Connection = None
        logger.debug("Session object initialized: %s" % vars(self))

    @property
    def websocket_url(self):
        return self.info.webSocketDebuggerUrl

    @property
    def main_tab(self) -> tab.Tab:
        """returns the target which was launched with the browser"""
        return sorted(self.targets, key=lambda x: x.type_ == "page", reverse=True)[0]

    @property
    def tabs(self) -> List[tab.Tab]:
        """returns the current targets which are of type "page"
        :return:
        """
        tabs = filter(lambda item: item.type_ == "page", self.targets)
        return list(tabs)

    @property
    def cookies(self) -> CookieJar:
        if not self._cookies:
            self._cookies = CookieJar(self)
        return self._cookies

    @property
    def stopped(self):
        if self._process and self._process.returncode is None:
            return False
        return True
        # return (self._process and self._process.returncode) or False

    async def wait(self, time: Union[float, int] = 0.1):
        """wait for <time> seconds. important to use, especially in between page navigation

        :param time:
        :return:
        """
        try:
            await asyncio.sleep(time)
        except asyncio.TimeoutError:
            pass

    sleep = wait
    """alias for wait"""

    def _handle_target_update(
        self,
        event: Union[
            cdp.target.TargetInfoChanged,
            cdp.target.TargetDestroyed,
            cdp.target.TargetCreated,
            cdp.target.TargetCrashed,
        ],
    ):
        """this is an internal handler which updates the targets when chrome emits the corresponding event"""

        if isinstance(event, cdp.target.TargetInfoChanged):
            target_info = event.target_info

            current_tab = next(
                filter(
                    lambda item: item.target_id == target_info.target_id, self.targets
                )
            )
            current_target = current_tab.target

            if logger.getEffectiveLevel() <= 10:
                changes = util.compare_target_info(current_target, target_info)
                changes_string = ""
                for change in changes:
                    key, old, new = change
                    changes_string += f"\n{key}: {old} => {new}\n"
                logger.debug(
                    "target #%d has changed: %s"
                    % (self.targets.index(current_tab), changes_string)
                )

                current_tab._target = target_info

        elif isinstance(event, cdp.target.TargetCreated):
            target_info: cdp.target.TargetInfo = event.target_info
            from .tab import Tab

            new_target = Tab(
                (
                    f"ws://{self.config.host}:{self.config.port}"
                    f"/devtools/{target_info.type_ or 'page'}"  # all types are 'page' internally in chrome apparently
                    f"/{target_info.target_id}"
                ),
                target=target_info,
                browser=self,
            )

            self.targets.append(new_target)

            logger.debug("target #%d created => %s", len(self.targets), new_target)

        elif isinstance(event, cdp.target.TargetDestroyed):
            current_tab = next(
                filter(lambda item: item.target_id == event.target_id, self.targets)
            )
            logger.debug(
                "target removed. id # %d => %s"
                % (self.targets.index(current_tab), current_tab)
            )
            self.targets.remove(current_tab)

        asyncio.create_task(self.update_targets())

    async def get(
        self, url="chrome://welcome", new_tab: bool = False, new_window: bool = False
    ) -> tab.Tab:
        """top level get. utilizes the first tab to retrieve given url.

        convenience function known from selenium.
        this function handles waits/sleeps and detects when DOM events fired, so it's the safest
        way of navigating.

        :param url: the url to navigate to
        :param new_tab: open new tab
        :param new_window:  open new window
        :return: Page
        """
        if new_tab or new_window:
            # creat new target using the browser session
            target_id = await self.connection.send(
                cdp.target.create_target(
                    url, new_window=new_window, enable_begin_frame_control=True
                )
            )
            # get the connection matching the new target_id from our inventory
            connection: tab.Tab = next(
                filter(
                    lambda item: item.type_ == "page" and item.target_id == target_id,
                    self.targets,
                )
            )
            connection._browser = self

        else:
            # first tab from browser.tabs
            connection: tab.Tab = next(
                filter(lambda item: item.type_ == "page", self.targets)
            )
            # use the tab to navigate to new url
            frame_id, loader_id, *_ = await connection.send(cdp.page.navigate(url))
            # update the frame_id on the tab
            connection.frame_id = frame_id
            connection._browser = self

        await self
        return connection

    async def create_context(
        self,
        url: str = "chrome://welcome",
        new_tab: bool = False,
        new_window: bool = True,
        dispose_on_detach: bool = True,
        proxy_server: str = None,
        proxy_bypass_list: List[str] = None,
        origins_with_universal_network_access: List[str] = None,
    ) -> tab.Tab:
        """
        creates a new browser context - mostly useful if you want to use proxies for different browser instances
        since chrome usually can only use 1 proxy per browser.
        socks5 with authentication is supported by using a forwarder proxy, the
        correct string to use socks proxy with username/password auth is socks://USERNAME:PASSWORD@SERVER:PORT

        dispose_on_detach – (EXPERIMENTAL) (Optional) If specified, disposes this context when debugging session disconnects.
        proxy_server – (EXPERIMENTAL) (Optional) Proxy server, similar to the one passed to –proxy-server
        proxy_bypass_list – (EXPERIMENTAL) (Optional) Proxy bypass list, similar to the one passed to –proxy-bypass-list
        origins_with_universal_network_access – (EXPERIMENTAL) (Optional) An optional list of origins to grant unlimited cross-origin access to. Parts of the URL other than those constituting origin are ignored.

        :param new_window:
        :type new_window:
        :param new_tab:
        :type new_tab:
        :param url:
        :type url:
        :param dispose_on_detach:
        :type dispose_on_detach:
        :param proxy_server:
        :type proxy_server:
        :param proxy_bypass_list:
        :type proxy_bypass_list:
        :param origins_with_universal_network_access:
        :type origins_with_universal_network_access:
        :return:
        :rtype:
        """
        if proxy_server:
            fw = util.ProxyForwarder(proxy_server=proxy_server)
            proxy_server = fw.proxy_server

        ctx: cdp.browser.BrowserContextID = await self.connection.send(
            cdp.target.create_browser_context(
                dispose_on_detach=dispose_on_detach,
                proxy_server=proxy_server,
                proxy_bypass_list=proxy_bypass_list,
                origins_with_universal_network_access=origins_with_universal_network_access,
            )
        )
        target_id: cdp.target.TargetID = await self.connection.send(
            cdp.target.create_target(
                url, browser_context_id=ctx, new_window=new_window, for_tab=new_tab
            )
        )
        await self.sleep(0.5)
        connection: tab.Tab = next(
            filter(
                lambda item: item.type_ == "page" and item.target_id == target_id,
                self.targets,
            )
        )
        return connection

    async def start(self=None) -> Browser:
        """launches the actual browser"""
        if not self:
            warnings.warn("use ``await Browser.create()`` to create a new instance")
            return

        if self._process or self._process_pid:
            if self._process.returncode is not None:
                return await self.create(config=self.config)
            warnings.warn("ignored! this call has no effect when already running.")
            return

        # self.config.update(kwargs)
        connect_existing = False
        if self.config.host is not None and self.config.port is not None:
            connect_existing = True
        else:
            self.config.host = "127.0.0.1"
            self.config.port = util.free_port()

        if not connect_existing:
            logger.debug(
                "BROWSER EXECUTABLE PATH: %s", self.config.browser_executable_path
            )
            if not pathlib.Path(self.config.browser_executable_path).exists():
                raise FileNotFoundError(
                    (
                        """
                    ---------------------
                    Could not determine browser executable.
                    ---------------------
                    Make sure your browser is installed in the default location (path).
                    If you are sure about the browser executable, you can specify it using
                    the `browser_executable_path='{}` parameter."""
                    ).format(
                        "/path/to/browser/executable"
                        if is_posix
                        else "c:/path/to/your/browser.exe"
                    )
                )

        if getattr(self.config, "_extensions", None):  # noqa
            self.config.add_argument(
                "--load-extension=%s"
                % ",".join(str(_) for _ in self.config._extensions)
            )  # noqa

        exe = self.config.browser_executable_path
        params = self.config()

        logger.info(
            "starting\n\texecutable :%s\n\narguments:\n%s", exe, "\n\t".join(params)
        )
        if not connect_existing:
            self._process: asyncio.subprocess.Process = (
                await asyncio.create_subprocess_exec(
                    # self.config.browser_executable_path,
                    # *cmdparams,
                    exe,
                    *params,
                    stdin=asyncio.subprocess.PIPE,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                    close_fds=is_posix,
                )
            )
            self._process_pid = self._process.pid

        self._http = HTTPApi((self.config.host, self.config.port))
        util.get_registered_instances().add(self)
        await asyncio.sleep(0.25)
        for _ in range(5):
            try:
                self.info = ContraDict(await self._http.get("version"), silent=True)
            except (Exception,):
                if _ == 4:
                    logger.debug("could not start", exc_info=True)
                await self.sleep(0.5)
            else:
                break

        if not self.info:
            raise Exception(
                (
                    """
                ---------------------
                Failed to connect to browser
                ---------------------
                One of the causes could be when you are running as root.
                In that case you need to pass no_sandbox=True 
                """
                )
            )

        self.connection = Connection(self.info.webSocketDebuggerUrl, browser=self)

        if self.config.autodiscover_targets:
            logger.info("enabling autodiscover targets")

            self.connection.handlers[cdp.target.TargetInfoChanged] = [
                self._handle_target_update
            ]
            self.connection.handlers[cdp.target.TargetCreated] = [
                self._handle_target_update
            ]
            self.connection.handlers[cdp.target.TargetDestroyed] = [
                self._handle_target_update
            ]
            self.connection.handlers[cdp.target.TargetCrashed] = [
                self._handle_target_update
            ]
            await self.connection.send(cdp.target.set_discover_targets(discover=True))

        await self.update_targets()

        # await self

        # self.connection.handlers[cdp.inspector.Detached] = [self.stop]
        # return self

    async def grant_all_permissions(self):
        """
        grant permissions for:
            accessibilityEvents
            audioCapture
            backgroundSync
            backgroundFetch
            clipboardReadWrite
            clipboardSanitizedWrite
            displayCapture
            durableStorage
            geolocation
            idleDetection
            localFonts
            midi
            midiSysex
            nfc
            notifications
            paymentHandler
            periodicBackgroundSync
            protectedMediaIdentifier
            sensors
            storageAccess
            topLevelStorageAccess
            videoCapture
            videoCapturePanTiltZoom
            wakeLockScreen
            wakeLockSystem
            windowManagement
        """
        permissions = list(cdp.browser.PermissionType)
        permissions.remove(cdp.browser.PermissionType.FLASH)
        permissions.remove(cdp.browser.PermissionType.CAPTURED_SURFACE_CONTROL)
        await self.connection.send(cdp.browser.grant_permissions(permissions))

    async def tile_windows(self, windows=None, max_columns: int = 0):
        import math

        import mss

        m = mss.mss()
        screen, screen_width, screen_height = 3 * (None,)
        if m.monitors and len(m.monitors) >= 1:
            screen = m.monitors[0]
            screen_width = screen["width"]
            screen_height = screen["height"]
        if not screen or not screen_width or not screen_height:
            warnings.warn("no monitors detected")
            return
        await self
        distinct_windows = defaultdict(list)

        if windows:
            tabs = windows
        else:
            tabs = self.tabs
        for tab in tabs:
            window_id, bounds = await tab.get_window()
            distinct_windows[window_id].append(tab)

        num_windows = len(distinct_windows)
        req_cols = max_columns or int(num_windows * (19 / 6))
        req_rows = int(num_windows / req_cols)

        while req_cols * req_rows < num_windows:
            req_rows += 1

        box_w = math.floor((screen_width / req_cols) - 1)
        box_h = math.floor(screen_height / req_rows)

        distinct_windows_iter = iter(distinct_windows.values())
        grid = []
        for x in range(req_cols):
            for y in range(req_rows):
                num = x + y
                try:
                    tabs = next(distinct_windows_iter)
                except StopIteration:
                    continue
                if not tabs:
                    continue
                tab = tabs[0]

                try:
                    pos = [x * box_w, y * box_h, box_w, box_h]
                    grid.append(pos)
                    await tab.set_window_size(*pos)
                except Exception:
                    logger.info(
                        "could not set window size. exception => ", exc_info=True
                    )
                    continue
        return grid

    async def _get_targets(self) -> List[cdp.target.TargetInfo]:
        info = await self.connection.send(cdp.target.get_targets(), _is_update=True)
        return info

    async def update_targets(self):

        targets: List[cdp.target.TargetInfo]
        targets = await self._get_targets()
        target_ids = [t.target_id for t in targets]
        existing_target_ids = [t.target_id for t in self.targets]
        for t in targets:
            for existing_tab in self.targets:
                existing_target = existing_tab.target
                if existing_target.target_id == t.target_id:
                    existing_tab.target.__dict__.update(t.__dict__)
                    break
            else:
                self.targets.append(
                    Connection(
                        (
                            f"ws://{self.config.host}:{self.config.port}"
                            f"/devtools/page"  # all types are 'page' somehow
                            f"/{t.target_id}"
                        ),
                        target=t,
                        browser=self,
                    )
                )

        await asyncio.sleep(0)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type and exc_val:
            raise exc_type(exc_val)

    def __iter__(self):
        self._i = self.tabs.index(self.main_tab)
        return self

    def __getitem__(
        self, item: Union[str, int, slice]
    ) -> Union[tab.Tab, List[tab.Tab]]:
        """
        allows to get py:obj:`tab.Tab` instances by using browser[0], browser[1], etc.
        a string is also allowed. it will then return the first tab where the py:obj:`cdp.target.TargetInfo` object
        (as json string) contains the given key, or the first tab in case no matches are found. eg:
        `browser["google"]` gives the first tab which has "google" in it's serialized target object.

        :param item:
        :type item:
        :return:
        :rtype: tab.Tab
        """
        if isinstance(item, int):
            return self.tabs[item]
        elif isinstance(item, slice):
            tabs: List[tab.Tab] = []
            sta, sto, ste = item.start, item.stop, item.step
            if not ste:
                ste = 1
            if not sto:
                sto = len(self.tabs) - 1
            if not sta:
                sta = 0
            for x in range(sta, sto, ste):
                try:
                    tabs.append(self.tabs[x])
                except IndexError:
                    pass
            return tabs
        elif isinstance(item, tuple):
            r = range(*item)
            tabs: List[tab.Tab] = []
            for i in r:
                try:
                    tabs.append(self.tabs[i])
                except IndexError:
                    pass
            return tabs
        elif isinstance(item, str):
            for t in self.tabs:
                if item.lower() in str(t.target.to_json()).lower():
                    return t
            else:
                return self.tabs[0]

    def __reversed__(self):
        return reversed(list(self.tabs))

    def __next__(self):
        try:
            return self.tabs[self._i]
        except IndexError:
            del self._i
            raise StopIteration
        except AttributeError:
            del self._i
            raise StopIteration
        finally:
            if hasattr(self, "_i"):
                if self._i != len(self.tabs):
                    self._i += 1
                else:
                    del self._i

    def stop(self):
        try:
            # asyncio.get_running_loop().create_task(self.connection.send(cdp.browser.close()))

            asyncio.get_event_loop().create_task(self.connection.disconnect())
            logger.debug("closed the connection using get_event_loop().create_task()")
        except RuntimeError:
            if self.connection:
                try:
                    # asyncio.run(self.connection.send(cdp.browser.close()))
                    asyncio.run(self.connection.disconnect())
                    logger.debug("closed the connection using asyncio.run()")
                except Exception:
                    pass

        for _ in range(3):
            try:
                self._process.terminate()
                logger.info(
                    "terminated browser with pid %d successfully" % self._process.pid
                )
                break
            except (Exception,):
                try:
                    self._process.kill()
                    logger.info(
                        "killed browser with pid %d successfully" % self._process.pid
                    )
                    break
                except (Exception,):
                    try:
                        if hasattr(self, "browser_process_pid"):
                            os.kill(self._process_pid, 15)
                            logger.info(
                                "killed browser with pid %d using signal 15 successfully"
                                % self._process.pid
                            )
                            break
                    except (TypeError,):
                        logger.info("typerror", exc_info=True)
                        pass
                    except (PermissionError,):
                        logger.info(
                            "browser already stopped, or no permission to kill. skip"
                        )
                        pass
                    except (ProcessLookupError,):
                        logger.info("process lookup failure")
                        pass
                    except (Exception,):
                        raise
            self._process = None
            self._process_pid = None

    def __await__(self):
        # return ( asyncio.sleep(0)).__await__()
        return self.update_targets().__await__()

    def __del__(self):
        pass


class CookieJar:
    def __init__(self, browser: Browser):
        self._browser = browser
        # self._connection = connection

    async def get_all(
        self, requests_cookie_format: bool = False
    ) -> List[Union[cdp.network.Cookie, "http.cookiejar.Cookie"]]:
        """
        get all cookies

        :param requests_cookie_format: when True, returns python http.cookiejar.Cookie objects, compatible  with requests library and many others.
        :type requests_cookie_format: bool
        :return:
        :rtype:

        """
        connection = None
        for tab in self._browser.tabs:
            if tab.closed:
                continue
            connection = tab
            break
        else:
            connection = self._browser.connection
        cookies = await connection.send(cdp.storage.get_cookies())
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

    async def set_all(self, cookies: List[cdp.network.CookieParam]):
        """
        set cookies

        :param cookies: list of cookies
        :type cookies:
        :return:
        :rtype:
        """
        connection = None
        for tab in self._browser.tabs:
            if tab.closed:
                continue
            connection = tab
            break
        else:
            connection = self._browser.connection
        cookies = await connection.send(cdp.storage.get_cookies())
        await connection.send(cdp.storage.set_cookies(cookies))

    async def save(self, file: PathLike = ".session.dat", pattern: str = ".*"):
        """
        save all cookies (or a subset, controlled by `pattern`) to a file to be restored later

        :param file:
        :type file:
        :param pattern: regex style pattern string.
               any cookie that has a  domain, key or value field which matches the pattern will be included.
               default = ".*"  (all)

               eg: the pattern "(cf|.com|nowsecure)" will include those cookies which:
                    - have a string "cf" (cloudflare)
                    - have ".com" in them, in either domain, key or value field.
                    - contain "nowsecure"
        :type pattern: str
        :return:
        :rtype:
        """
        import re

        pattern = re.compile(pattern)
        save_path = pathlib.Path(file).resolve()
        connection = None
        for tab in self._browser.tabs:
            if tab.closed:
                continue
            connection = tab
            break
        else:
            connection = self._browser.connection

        cookies = await self.get_all(requests_cookie_format=False)
        included_cookies = []
        for cookie in cookies:
            for match in pattern.finditer(str(cookie.__dict__)):
                logger.debug(
                    "saved cookie for matching pattern '%s' => (%s: %s)",
                    pattern.pattern,
                    cookie.name,
                    cookie.value,
                )
                included_cookies.append(cookie)
                break
        pickle.dump(cookies, save_path.open("w+b"))

    async def load(self, file: PathLike = ".session.dat", pattern: str = ".*"):
        """
        load all cookies (or a subset, controlled by `pattern`) from a file created by :py:meth:`~save_cookies`.

        :param file:
        :type file:
        :param pattern: regex style pattern string.
               any cookie that has a  domain, key or value field which matches the pattern will be included.
               default = ".*"  (all)

               eg: the pattern "(cf|.com|nowsecure)" will include those cookies which:
                    - have a string "cf" (cloudflare)
                    - have ".com" in them, in either domain, key or value field.
                    - contain "nowsecure"
        :type pattern: str
        :return:
        :rtype:
        """
        import re

        pattern = re.compile(pattern)
        save_path = pathlib.Path(file).resolve()
        cookies = pickle.load(save_path.open("r+b"))
        included_cookies = []
        connection = None
        for tab in self._browser.tabs:
            if tab.closed:
                continue
            connection = tab
            break
        else:
            connection = self._browser.connection
        for cookie in cookies:
            for match in pattern.finditer(str(cookie.__dict__)):
                included_cookies.append(cookie)
                logger.debug(
                    "loaded cookie for matching pattern '%s' => (%s: %s)",
                    pattern.pattern,
                    cookie.name,
                    cookie.value,
                )
                break
        await connection.send(cdp.storage.set_cookies(included_cookies))

    async def clear(self):
        """
        clear current cookies

        note: this includes all open tabs/windows for this browser

        :return:
        :rtype:
        """
        connection = None
        for tab in self._browser.tabs:
            if tab.closed:
                continue
            connection = tab
            break
        else:
            connection = self._browser.connection

        await connection.send(cdp.storage.clear_cookies())


class HTTPApi:
    def __init__(self, addr: Tuple[str, int]):
        self.host, self.port = addr
        self.api = "http://%s:%d" % (self.host, self.port)

    @classmethod
    def from_target(cls, target: "Target"):
        ws_url = urllib.parse.urlparse(target.websocket_url)
        inst = cls((ws_url.hostname, ws_url.port))
        return inst

    async def get(self, endpoint: str):
        return await self._request(endpoint)

    async def post(self, endpoint, data):
        return await self._request(endpoint, data)

    async def _request(self, endpoint, method: str = "get", data: dict = None):
        url = urllib.parse.urljoin(
            self.api, f"json/{endpoint}" if endpoint else "/json"
        )
        if data and method.lower() == "get":
            raise ValueError("get requests cannot contain data")
        if not url:
            url = self.api + endpoint
        request = urllib.request.Request(url)
        request.method = method
        request.data = None
        if data:
            request.data = json.dumps(data).encode("utf-8")

        response = await asyncio.get_running_loop().run_in_executor(
            None, lambda: urllib.request.urlopen(request, timeout=10)
        )
        return json.loads(response.read())


atexit.register(util.deconstruct_browser)
