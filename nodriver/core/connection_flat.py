# Copyright 2024 by UltrafunkAmsterdam (https://github.com/UltrafunkAmsterdam)
# All rights reserved.
# This file is part of the nodriver package.
# and is released under the "GNU AFFERO GENERAL PUBLIC LICENSE".
# Please see the LICENSE.txt file that should have been included as part of this package.

from __future__ import annotations

import asyncio
import collections
import inspect
import itertools
import json
import logging
import types
import re
from asyncio import iscoroutine, iscoroutinefunction
from typing import Any, Awaitable, Callable, Generator, List, TypeVar, Union

import websockets.asyncio.client
from websockets import InvalidStatus

from .. import cdp
from . import browser as _browser
from . import util

T = TypeVar("T")

GLOBAL_DELAY = 0.005
MAX_SIZE: int = 2 ** 28
PING_TIMEOUT: int = 900  # 15 minutes

TargetType = Union[cdp.target.TargetInfo, cdp.target.TargetID]

logger = logging.getLogger(__name__)


class ProtocolException(Exception):
    def __init__(self, *args, **kwargs):  # real signature unknown

        self.message = None
        self.code = None
        self.args = args
        if isinstance(args[0], dict):

            self.message = args[0].get("message", None)  # noqa
            self.code = args[0].get("code", None)

        elif hasattr(args[0], "to_json"):

            def serialize(obj, _d=0):
                res = "\n"
                for k, v in obj.items():
                    space = "\t" * _d
                    if isinstance(v, dict):
                        res += f"{space}{k}: {serialize(v, _d + 1)}\n"
                    else:
                        res += f"{space}{k}: {v}\n"

                return res

            self.message = serialize(args[0].to_json())

        else:
            self.message = "| ".join(str(x) for x in args)

    def __str__(self):
        return f"{self.message} [code: {self.code}]" if self.code else f"{self.message}"

# async def _update_targets(self):
#     targets = await self.send(cdp.target.get_targets())
#
#     new_attached = list(filter(lambda t: t.attached, targets))
#     self.other_targets = [t for t in targets if t not in new_attached]
#     currently_attached = self.targets.copy()
#
#     final_attached = set()
#
#     for new_target in new_attached:
#         for cur_target in currently_attached:
#             if cur_target.target_id == new_target.target_id:
#                 final_attached.add(cur_target.target_id)
#                 break
#         else:
#             final_attached.add(new_target.target_id)
#
#     else:
#         all_targets = []
#         for x in new_attached + currently_attached:
#             if x not in all_targets:
#                 all_targets.append(x)
#         self.targets = [x for x in all_targets if x.target_id in final_attached]



class Connection:
    """

    """
    _websocket: websockets.asyncio.client.ClientConnection | None
    _session_id: cdp.target.SessionID | None

    targets: List[cdp.target.TargetInfo]  = []
    current_target: cdp.target.TargetInfo
    other_targets: List[cdp.target.TargetInfo] = []

    def __init__(
            self,
            browser = None,
            **kwargs,
    ):
        self.target = None
        self.attached = False
        self.auto_attach = False 
        self.websocket_url = kwargs.get("websocket_url", getattr(browser, "websocket_url", None))
        
        self.mapper = {}
        self.handlers = collections.defaultdict(list)
        self.enabled_domains = []
        self.browser = browser
        self._session_id = None
        self._websocket = None
        self._event = asyncio.Event()
        self._lock = asyncio.Lock()
        self._connected = False
        self._listener_task = None
        self.__count__ = itertools.count(0)
        self.__dict__.update(**kwargs)


    # @classmethod
    # async def as_brow(cls, browser = None, **kwargs):
    #     instance = cls(browser=browser, **kwargs)
    #     instance.attached = True
    #     sid = await instance.send(cdp.target.attach_to_browser_target())
    #     instance._session_id = sid
    #     await instance._update_targets()
    #     instance.target = "BROWSER"
    #     return instance


    @classmethod
    async def from_target(cls, target: cdp.target.TargetID | cdp.target.TargetInfo | str, browser: _browser.Browser = None,
                              **kwargs):

        target_id = None
        host = None
        port = None
        if isinstance(target, cdp.target.TargetInfo):
            target_id = target.target_id

        elif isinstance(target, cdp.target.TargetID):
            target_id = target

        elif isinstance(target, str):
            match = re.match((
                r"^(?P<proto>wss?)://"
                r"(?P<host>\S+?):?(?P<port>\d+?)"
                r"/devtools/(?P<type>\S+)/(?P<id>\S+)"),
                target)
            if match:
                d = match.groupdict()
                host = d.get('host')
                port = d.get('port')
                typ = d.get('type', 'page')
                target_id = d.get('id')
                ws_url = match[0]
            else:
                target_id = target
            target_id = cdp.target.TargetID(target)

        instance = cls(browser, **kwargs)
        await instance.attach(target_id)
        # for t in instance.targets:
        #     if t.attached:
        #         instance.attached = True
        #         instance.target = t
        #         return instance
        # else:
        #     await instance.attach(target_id)
        return instance


    async def attach(self, target: cdp.target.TargetInfo | cdp.target.TargetID | str = None):
        target = target or self.target
        target_id = None
        if isinstance(target, cdp.target.TargetInfo):
            target_id = target.target_id
        elif isinstance(target, cdp.target.TargetID):
            target_id = target
        elif isinstance(target, str):
            target_id = cdp.target.TargetID(target)
        if not target_id:
            raise ValueError("could not extract a valid target from '%s'. make sure the format looks as , for example 3B49E08AD54DBE41F7B4ECD6B6CCA742")
        if 'auto_attach' in vars(self):
            sid = await self.send(cdp.target.set_auto_attach(auto_attach=True, wait_for_debugger_on_start=True, flatten=True))
        sid = await self.send(cdp.target.attach_to_target(target_id, True))
        if sid:
            self._session_id = sid
            # await self._update_targets()
            tinfo = await self.send(cdp.target.get_target_info(target_id))
            self.target = tinfo
            # self.target = next(filter(lambda x:x.target_id == target_id, self.targets))
            self.attached = True
        return self


    async def detach(self,  target: cdp.target.TargetInfo | cdp.target.TargetID | str):
        target_id = None
        if isinstance(target, cdp.target.TargetInfo):
            target_id = target.target_id
        elif isinstance(target, cdp.target.TargetID):
            target_id = target
        elif isinstance(target, str):
            target_id = cdp.target.TargetID(target)
        if not target_id:
            raise ValueError(
                "could not extract a valid target from '%s'. make sure the format looks as , for example 3B49E08AD54DBE41F7B4ECD6B6CCA742")
        return await self.send(cdp.target.detach_from_target(target_id=target_id))


    # def __getitem__(self, item: int|str):
    #     if isinstance(item, int):
    #         return self.targets[item]
    #     elif isinstance(item, str):
    #         return next(filter(lambda x: item.lower() in (x.url.lower() + x.title.lower()), self.targets))
    #
    #
    # def __iter__(self):
    #     self._idx = self.targets.index(self.target)
    #     print('iter', self._idx)
    #     return self
    #
    # def __next__(self):
    #
    #     if self._idx == -1:
    #         raise StopIteration
    #
    #     idx = self._idx
    #     retval = self.targets[idx]
    #
    #     if idx == len(self.targets) - 1:
    #         self._idx = 0
    #
    #     elif idx == self.targets.index(self.target) - 1:
    #         self._idx = -1
    #
    #     return retval
    #


            # all_target_ids = set(map(lambda x: x.target_id, all_targets))

            # self._targets.append(new_target)
                # final_attached(new_target.target_id)

                # breakpoint()

        # breakpoint()
        # all_targets = new_attached + currently_attached
        # breakpoint()
        # self._targets = [ item for item in filter(lambda t: t.target_id in final_attached, all_targets) if item not in self._targets ]


    async def open(self):
        if not self._connected:
            try:
                self._websocket = await websockets.connect(
                    self.websocket_url,
                    ping_timeout=PING_TIMEOUT,
                    max_size=MAX_SIZE,
                )
                self._connected = True
            except (InvalidStatus,):
                raise

    async def close(self):
        try:
            try:
                await self._websocket.close()
                await self._websocket.wait_closed()
            except (Exception,):
                raise
        finally:
            self._connected = False
            self._websocket = None

    def add_handler(
        self,
        event_type_or_domain: Union[type, types.ModuleType, List[type]],
        handler: Union[Callable, Awaitable],
    ):
        """
        add a handler for given event

        if event_type_or_domain is a module instead of a type, it will find all available events and add
        the handler.

        if you want to receive event updates (network traffic are also 'events') you can add handlers for those events.
        handlers can be regular callback functions or async coroutine functions (and also just lamba's).
        for example, you want to check the network traffic:

        .. code-block::

            page.add_handler(cdp.network.RequestWillBeSent, lambda event: print('network event => %s' % event.request))

        the next time you make network traffic you will see your console print like crazy.

        :param event_type_or_domain:
        :type event_type_or_domain:
        :param handler:
        :type handler:

        :return:
        :rtype:
        """

        if not isinstance(event_type_or_domain, list):
            event_type_or_domain = [event_type_or_domain]

        for evt_dom in event_type_or_domain:
            if isinstance(evt_dom, types.ModuleType):
                for name, obj in inspect.getmembers_static(evt_dom):
                    if name.isupper():
                        continue
                    if not name[0].isupper():
                        continue
                    if type(obj) != type:
                        continue
                    if inspect.isbuiltin(obj):
                        continue
                    self.handlers[obj].append(handler)
                return
            else:
                self.handlers[evt_dom].append(handler)

    def remove_handler(
        self,
        event_type_or_domain: Union[type, types.ModuleType, List[type]],
        handler: Union[Callable, Awaitable] = None,
    ):
        """
        remove a handler for given event
        :param event_type_or_domain:
        :type event_type_or_domain:
        :param handler:
        :type handler:
        """
        if handler:
            for event, callbacks in self.handlers.items():
                for cb in callbacks:
                    if cb == self:
                        self.handlers[event].remove(handler)

        if not isinstance(event_type_or_domain, list):
            event_type_or_domain = [event_type_or_domain]

        for evt_dom in event_type_or_domain:
            if isinstance(evt_dom, types.ModuleType):
                for name, obj in inspect.getmembers_static(evt_dom):
                    if name.isupper():
                        continue
                    if not name[0].isupper():
                        continue
                    if type(obj) is type:
                        continue
                    if inspect.isbuiltin(obj):
                        continue
                    try:
                        del self.handlers[obj]
                    except KeyError:
                        # missing key is not that important here
                        pass
                return
            else:
                del self.handlers[evt_dom]

    async def send(self, cdp_obj: Generator[dict[str, Any], dict[str, Any], Any], _update=None):

        method, *params = next(cdp_obj).values()
        if params:
            params = params.pop()
        _id = next(self.__count__)
        message = {"method": method, "params": params, "id": _id}
        if self._session_id:
            message['sessionId'] = self._session_id
        await self.open()
        await self._websocket.send(json.dumps(message))

        while True:
            try:
                raw = await asyncio.wait_for(self._websocket.recv(), 5)
                raw_json = json.loads(raw)
                if not raw_json:
                    return raw_json
                if "result" not in raw_json:
                    if "method" in raw_json:
                        await self.process_event(raw_json)
                else:
                    try:
                        cdp_obj.send(raw_json["result"])
                    except KeyError as e:
                        raise KeyError(f"key '{e.args}' not found in message: {raw_json}")
                    except StopIteration as e:
                        # exception value holds the parsed response
                        return e.value
            except (Exception,):
                raise

    async def process_event(self, raw_json: dict):
        event = None
        try:
            event = cdp.util.parse_json_event(raw_json)
            print('EVENT', event, vars(event))
        except KeyError as e:
            logger.exception(e)
            return

        if type(event) in self.handlers:
            callbacks = self.handlers[type(event)]
        else:
            return
        if not callbacks:
            return
        for callback in callbacks:
            try:
                if iscoroutinefunction(callback) or iscoroutine(
                        callback
                ):
                    try:
                        asyncio.create_task(callback(event, self))
                    except TypeError as e:
                        asyncio.create_task(callback(event))
                else:
                    try:
                        callback(event, self)
                    except TypeError:
                        callback(event)

            except Exception as e:
                logger.warning(
                    "exception in callback %s for event %s => %s",
                    callback,
                    event.__class__.__name__,
                    e,
                    exc_info=True,
                )
                # since it's handlers, don't raise and screw our program



class ConnectionManager:
    master: Connection = None

    def __init__(self, browser: "nodriver.browser.Browser", **kwargs):
        self.browser = browser
        self.master = None
        self.tabs = []
        self.targets = []

    async def update_targets(self):
        new_targets = await self.master.send(cdp.target.get_targets())
        self.targets = new_targets
        for i, t in enumerate(self.targets.copy()):
            if isinstance(t, cdp.target.TargetInfo):
                if t.type_ == "page":
                    if t.target_id not in [x.target.target_id for x in self.tabs]:
                        self.tabs.append(await Connection.from_target(t, self.browser))
                for tab in self.tabs.copy():
                    if tab.target not in new_targets:
                        self.tabs.remove(tab)


    @classmethod
    async def create(cls, browser: "nodriver.browser.Browser", **kwargs):
        instance = cls(browser)
        c = Connection(browser, auto_attach=True)
        await c.open()
        c.attached = True
        c.sid = await c.send(cdp.target.attach_to_browser_target())
        instance.master = c
        await instance.update_targets()

        return instance

    async def get_frame_connections_for_tab(self, tab: Connection):
        await self.update_targets()
        frame_ids = [x.id_ for x in util.flatten_frame_tree(await tab.send(cdp.page.get_frame_tree()))]
        frame_targets = [
            x for x in self.targets
            if str(x.parent_frame_id) in map(str, frame_ids)
        ]
        return [
            await Connection.from_target(t, self.browser)
            for t in frame_targets
        ]

        # async def on_attached(event: cdp.target.AttachedToTarget):
        #     print('ON ATTACHED', event.target_info.target_id)
        #     if event.target_info.type_ == "browser":
        #         c.target = event.target_info
        #         instance.targets.extend(
        #             await c.send(cdp.target.get_targets()))
        #
        #     else:
        #         instance.targets.append(await Connection.from_target(event.target_info, browser))
        #     # c.remove_handler(cdp.target.AttachedToTarget)
        # #
        # async def on_detached(event: cdp.target.DetachedFromTarget):
        #     print('ON DETACHED', event.target_id)
        #     try:
        #         target = next(filter( lambda x : x.target.target_id == event.target_id, instance.targets))
        #         instance.targets.remove(target)
        #     except:
        #         raise
        #
        # async def on_destroyed(event: cdp.target.TargetDestroyed):
        #     print('TARGET DESTOYED', event.target_id)
        #     try:
        #         target = next(filter(lambda x: x.target.target_id == event.target_id, instance.targets))
        #         instance.targets.remove(target)
        #     except:
        #         raise
        #
        # async def target_changed(event: cdp.target.TargetInfoChanged):
        #     print('TARGET CHANGED', event.target_info.target_id)
        #     try:
        #         tab = next(filter(lambda x: x.target.target_id == event.target_info.target_id, instance.targets))
        #         tab.target = event.target_info
        #     except:
        #         raise
        #
        # c.add_handler(cdp.target.AttachedToTarget, on_attached)
        # c.add_handler(cdp.target.DetachedFromTarget, on_detached)
        # c.add_handler(cdp.target.DetachedFromTarget, on_destroyed)
        # c.add_handler(cdp.target.TargetInfoChanged, target_changed)
        # c.add_handler(cdp.target.DetachedFromTarget, on_detached)

