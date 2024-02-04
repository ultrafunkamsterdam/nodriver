from __future__ import annotations

import urllib.request
import urllib.parse
import asyncio
import atexit
import json
import logging
import operator
import os
import pathlib
import shutil
import warnings
import weakref
from typing import List, Optional, Union, Tuple

from .. import cdp
from .config import PathLike, Config, is_posix
from .connection import Connection
from ._contradict import ContraDict
from . import util

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

        self._process = None
        self._process_pid = None
        self.info = None
        self._target = None
        self._keep_user_data_dir = None
        self.connection: Connection = None
        self._is_updating = asyncio.Event()
        logger.debug("Session object initialized: %s" % vars(self))

    @property
    def websocket_url(self):
        return self.info.webSocketDebuggerUrl

    @property
    def active_page(self):
        """returns the target which was launched with the browser"""
        return sorted(self.targets, key=lambda x: x.type_ == "page", reverse=True)[0]

    @property
    def pages(self) -> List:
        """returns the current targets which are of type "page"
        :return:
        """
        pages = filter(lambda item: item.type_ == "page", self.targets)
        return list(pages)

    @property
    def stopped(self):
        if self._process and self._process.returncode is None:
            return False
        return True
        # return (self._process and self._process.returncode) or False

    async def wait(self, time: Union[float, int] = 1) -> Browser:
        """wait for <time> seconds. important to use, especially in between page navigation

        :param time:
        :return:
        """
        return await asyncio.sleep(time, result=self)

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

            current_page = next(
                filter(
                    lambda item: item.target_id == target_info.target_id, self.targets
                )
            )
            current_target = current_page.target
            logger.debug(
                "target for #%d to target changed from %s to: %s"
                % (
                    self.targets.index(current_page),
                    current_target.target_id,
                    target_info.target_id,
                )
            )
            self.target = target_info

        elif isinstance(event, cdp.target.TargetCreated):
            target_info: cdp.target.TargetInfo = event.target_info
            from .page import Page

            new_target = Page(
                (
                    f"ws://{self.config.host}:{self.config.port}"
                    f"/devtools/{target_info.type_.lower()}"
                    f"/{target_info.target_id}"
                ),
                target=target_info,
                browser=self,
            )

            self.targets.append(new_target)
            logger.warning("target #%d created => %s", len(self.targets), new_target)

        elif isinstance(event, cdp.target.TargetDestroyed):
            current_target = next(
                filter(lambda item: item.target_id == event.target_id, self.targets)
            )
            logger.debug(
                "target removed. id # %d => %s"
                % (self.targets.index(current_target), current_target)
            )
            self.targets.remove(current_target)

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

        if new_window and not new_tab:
            new_tab = True
        # get first tab
        tab = next(filter(lambda item: item.type_ == "page", self.targets))
        if new_tab:
            target_id = await self.connection.send(
                cdp.target.create_target(
                    url, new_window=new_window, enable_begin_frame_control=True
                )
            )
            tab = next(
                filter(
                    lambda item: item.type_ == "page" and item.target_id == target_id,
                    self.targets,
                )
            )
            while not tab:
                await self.wait()
                tab = next(
                    filter(
                        lambda item: item.type_ == "page"
                        and item.target_id == target_id,
                        self.targets,
                    )
                )
            return tab

        else:
            frame_id, loader_id, *_ = await tab.send(cdp.page.navigate(url))
            tab.frame_id = frame_id
            await self.wait()
            return tab

    # async def get(
    #         self, url="chrome://welcome", new_tab: bool = False, new_window: bool = False
    # ):
    #     """top level get. utilizes the first tab to retrieve given url.
    #
    #     convenience function known from selenium.
    #     this function handles waits/sleeps and detects when DOM events fired, so it's the safest
    #     way of navigating.
    #
    #     :param url: the url to navigate to
    #     :param new_tab: open new tab
    #     :param new_window:  open new window
    #     :return: Page
    #     """
    #     from .target import Target
    #     if new_window and not new_tab:
    #         new_tab = True
    #
    #     # get first tab
    #     try:
    #         tab = next(filter(lambda item: item.type_ == 'page', self.targets))
    #     except StopIteration:
    #         print(' stopiteration')
    #
    #         targets_http = await self._http.get('list')
    #         pages = [t for t in targets_http if t['type'] == 'page']
    #         _t = pages[0]  # dict
    #         # remap keys
    #         target_info = cdp.target.TargetInfo(**{
    #             'target_id': cdp.target.TargetID(_t.pop('id')),
    #             'type_': _t.pop('type'),
    #             'url': _t.pop('url'),
    #             'title': _t.pop('title'),
    #             'attached': True,
    #             'can_access_opener': True
    #         })
    #         tab = Target((
    #             f"ws://{self.config.host}:{self.config.port}"
    #             f"/devtools/{target_info.type_.lower()}"
    #             f"/{target_info.target_id}")
    #             , target=target_info)
    #         await tab.open()
    #         self.targets.append(tab)
    #         return await self.get(url, new_tab=new_tab, new_window=new_window)
    #     if new_tab:
    #         if not self.config.autodiscover_targets:
    #             _t = await self._http._request(method='put', endpoint=f'new/?{url}')
    #             target_info = cdp.target.TargetInfo(**{
    #                 'target_id': cdp.target.TargetID(_t.pop('id')),
    #                 'type_': _t.pop('type'),
    #                 'url': _t.pop('url'),
    #                 'title': _t.pop('title'),
    #                 'attached': False,
    #                 'can_access_opener': False
    #             })
    #             tab = Target((
    #                 f"ws://{self.config.host}:{self.config.port}"
    #                 f"/devtools/{target_info.type_.lower()}"
    #                 f"/{target_info.target_id}")
    #                 , target=target_info)
    #
    #             self.targets.append(tab)
    #         else:
    #
    #             target_id = await self.connection.send(
    #                 cdp.target.create_target(
    #                     url, new_window=new_window,
    #                     enable_begin_frame_control=True
    #                 )
    #             )
    #             if not self.config.autodiscover_targets:
    #                 target_info = cdp.target.TargetInfo(**{
    #                     'target_id': target_id,
    #                     'type_': 'page',
    #                     'url': url,
    #                     'title': None,
    #                     'attached': False,
    #                     'can_access_opener': False
    #                 })
    #                 tab = Target((
    #                     f"ws://{self.config.host}:{self.config.port}"
    #                     f"/devtools/{target_info.type_.lower()}"
    #                     f"/{target_info.target_id}")
    #                     , target=target_info)
    #             else:
    #                 tab = next(filter(lambda item: item.type_ == 'page' and item.target_id == target_id, self.targets))
    #             while not tab:
    #                 await self.wait()
    #                 tab = next(filter(lambda item: item.type_ == 'page' and item.target_id == target_id, self.targets))
    #         return tab
    #
    #     else:
    #         frame_id, loader_id, *_ = await tab.send(cdp.page.navigate(url))
    #         tab.frame_id = frame_id
    #         await self.wait()
    #         return tab

    #     """top level get. utilizes the first tab to retrieve given url.
    #
    #     convenience function known from selenium.
    #     this function handles waits/sleeps and detects when DOM events fired, so it's the safest
    #     way of navigating.
    #
    #     :param url: the url to navigate to
    #     :param new_tab: open new tab
    #     :param new_window:  open new window
    #     :return: Page
    #     """
    #
    #     if new_window and not new_tab:
    #         new_tab = True
    #     # get first tab
    #     try:
    #         tab = next(filter(lambda item: item.type_ == 'page', self.targets))
    #     except StopIteration:
    #         from .target import Target
    #         targets_http = await self._http.get('list')
    #         pages = [t for t in targets_http if t['type'] == 'page']
    #         _t = pages[0] # dict
    #         # remap keys
    #         target_info = cdp.target.TargetInfo(**{
    #             'target_id': cdp.target.TargetID(_t.pop('id')),
    #             'type_': _t.pop('type'),
    #             'url': _t.pop('url'),
    #             'title': _t.pop('title'),
    #             'attached': None,
    #             'can_access_opener': None
    #         })
    #
    #         tab = Target((
    #             f"ws://{self.config.host}:{self.config.port}"
    #             f"/devtools/{target_info.type_.lower()}"
    #             f"/{target_info.target_id}")
    #             , target=target_info)
    #         await tab.open()
    #
    #         self.targets.append(tab)
    #
    #     if new_tab:
    #         target_id = await self.connection.send(
    #             cdp.target.create_target(
    #                 url, new_window=new_window,
    #                 enable_begin_frame_control=True
    #             )
    #         )
    #         if not tab:
    #             tab = next(filter(lambda item: item.type_ == 'page' and item.target_id == target_id, self.targets))
    #
    #         while not tab:
    #             await self.wait()
    #             tab = next(filter(lambda item: item.type_ == 'page' and item.target_id == target_id, self.targets))
    #
    #         return tab
    #     else:
    #         if not tab:
    #             print(' creating tab')
    #             await self.update_targets()
    #             tab = next(filter(lambda item: item.type_ == 'page', self.targets))
    #             #
    #             # target_id = await self.connection.send(
    #             #     cdp.target.create_target(
    #             #         url,
    #             #         new_window=False,
    #             #         enable_begin_frame_control=True
    #             #     )
    #             # )
    #             # target_info = await self.connection.send(
    #             #     cdp.target.get_target_info(target_id)
    #             # )
    #             # tab = SimpleConnection((
    #             #     f"ws://{self.config.host}:{self.config.port}"
    #             #     f"/devtools/{target_info.type_.lower()}"
    #             #     f"/{target_info.target_id}"))
    #         if isinstance(tab, list):
    #             print(' tab is a list', tab)
    #             tab = tab[-1]
    #         frame_id, loader_id, *_ = await tab.send(cdp.page.navigate(url))
    #         tab.frame_id = frame_id
    #         await self.wait()
    #         return tab

    async def start(self=None):
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

        self.config.host = self.config.host or "127.0.0.1"
        self.config.port = self.config.port or util.free_port()

        logger.debug("BROWSER EXECUTABLE PATH: %s", self.config.browser_executable_path)
        if not pathlib.Path(self.config.browser_executable_path).exists():
            raise FileNotFoundError(
                "\n---------------------\n"
                "Could not determine browser executable."
                "\n---------------------\n"
                "Make sure your browser is installed in the default location (path).\n"
                "If you are sure about the browser executable, you can specify it using\n"
                "the `browser_executable_path='{}` parameter.\n\n".format(
                    "/path/to/browser/executable"
                    if is_posix
                    else "c:/path/to/your/browser.exe"
                )
            )

        exe = self.config.browser_executable_path
        params = self.config()
        logger.info(
            "starting\n\texecutable :%s\n\narguments:\n%s", exe, "\n\t".join(params)
        )
        self._process: asyncio.subprocess.Process = await asyncio.create_subprocess_exec(
            # self.config.browser_executable_path,
            # *cmdparams,
            exe,
            *params,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            close_fds=is_posix,
        )

        self._process_pid = self._process.pid
        logger.info("created process with pid %d " % self._process_pid)
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
                "\n---------------------\n"
                "Failed to connect to browser"
                "\n---------------------\n"
                "One of the causes could be when you are running as root.\n"
                "In that case you need to pass no_sandbox=True.\n\n"
            )

        self.connection = await Connection.create(
            self.info.webSocketDebuggerUrl, _owner=self
        )

        self.connection.handlers[cdp.inspector.Detached] = [self.stop]

        if self.config.autodiscover_targets:
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
            logger.info("enabling autodiscover targets")
            await self.connection.send(cdp.target.set_discover_targets(True))
        # await self

    async def tile_windows(self, rows=2, columns=2):
        import mss
        import math

        m = mss.mss()

        if m.monitors and len(m.monitors) >= 1:
            screen = m.monitors[0]
            width = screen["width"]
            height = screen["height"]
        await self

        ntabs = len(self.pages)  # number of actual browser windows
        print(ntabs)
        cols = math.floor(ntabs / rows)
        while (cols * rows) < ntabs:
            cols += 1
        _rows = math.floor(ntabs / columns)
        while (cols * _rows) < ntabs:
            _rows += 1

        return _rows, cols, screen

    async def _get_targets(self) -> List[cdp.target.TargetInfo]:
        info = await self.connection.send(cdp.target.get_targets(), _is_update=True)
        return info

    async def update_targets(self):
        targets: List[cdp.target.TargetInfo]
        targets = await self._get_targets()
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
                            f"/devtools/{t.type_.lower()}"
                            f"/{t.target_id}"
                        ),
                        target=t,
                    )
                )

        await asyncio.sleep(0)
        # asyncio.get_running_loop().call_later(
        #     2,
        #     lambda: asyncio.create_task(self._update_targets())
        # )

    async def __aenter__(self):
        print("x")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type and exc_val:
            raise exc_type(exc_val)

    def __iter__(self):
        self._i = self.pages.index(self.active_page)
        return self

    def __next__(self):
        try:
            return self.pages[self._i]
        except IndexError:
            del self._i
            raise StopIteration
        except AttributeError:
            del self._i
            raise StopIteration
        finally:
            if hasattr(self, "_i"):
                if self._i != len(self.pages):
                    self._i += 1
                else:
                    del self._i

    def stop(self):
        try:
            # asyncio.get_running_loop().create_task(self.connection.send(cdp.browser.close()))

            asyncio.get_event_loop().create_task(self.connection.aclose())
            logger.debug("closed the connection using get_event_loop().create_task()")
        except:
            if self.connection:
                try:
                    # asyncio.run(self.connection.send(cdp.browser.close()))
                    asyncio.run(self.connection.aclose())
                    logger.debug("closed the connection using asyncio.run()")
                except Exception:
                    logger.exception("exccc while closing", exc_info=True)
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

        # Close connection when this object is destroyed
        #
        # try:
        #     loop = asyncio.get_running_loop()
        #     logger.debug('%s __del__ => scheduling websocket cleanup to existing running loop',
        #                  self.__class__.__name__)
        #     loop.create_task(self.connection.send(cdp.browser.close()))
        #
        #     # if loop.is_running():
        #     #
        #     #     loop.create_task(self.connection.send(cdp.browser.close()))

        # except RuntimeError:
        #     logger.debug('%s __del__ => scheduling websocket cleanup to new loop',
        #                  self.__class__.__name__)
        #     asyncio.run(self.connection.send(cdp.browser.close()))
        # except Exception:  # noqa
        #     raise

    # def __del__(self):
    #     try:
    #         loop = asyncio.get_running_loop()
    #     except RuntimeError:
    #         return
    #     coro = self.connection.send(cdp.browser.close())
    #     if loop.is_running():
    #         loop.create_task(coro)
    #     else:
    #         loop.run_until_complete(coro)


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
        url = urllib.parse.urljoin(self.api, "/".join(["json", endpoint]))
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
            None, urllib.request.urlopen, request
        )
        return json.loads(response.read())


atexit.register(util.deconstruct_browser)
