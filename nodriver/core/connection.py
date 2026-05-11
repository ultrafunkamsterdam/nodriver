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
import re
import types
from asyncio import iscoroutine, iscoroutinefunction
from typing import Any, Awaitable, Callable, Generator, List, TypeVar, Union

import websockets.asyncio.client
from websockets import InvalidStatus

from .. import cdp
from . import browser as _browser
from . import util

T = TypeVar("T")

GLOBAL_DELAY = 0.005
MAX_SIZE: int = 2**28
PING_TIMEOUT: int = 900  # 15 minutes

TargetType = Union[cdp.target.TargetInfo, cdp.target.TargetID, str]

logger = logging.getLogger(__name__)


class ProtocolException(Exception):
    def __init__(self, *args, **kwargs):  # real signature unknown

        self.message = None
        self.code = None
        self.args = args
        self.extra = kwargs

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

        self.message += "\n".join(f"{k}:{v}" for k, v in self.extra.items())

    def __str__(self):
        return (
            f"{self.message} [code: {self.code}]"
            if self.code
            else f"{self.message}" + f"\n{self.extra}"
        )


class Transaction:
    request: dict = None
    events: list | None = None
    id: int | None = None

    def __init__(self, request: dict):
        self.id = request["id"]
        self.request = request
        self.result = None
        self.events = []

    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"[\n"
            f"request: {self._truncate(self.request)}\n"
            f"events:{len(self.events)}\n"
            f"result: {self._truncate(self.result)}\n"
            f"]"
        )

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def _truncate(item: Any, max_length: int = 256, ellipsis: bool = True) -> str:
        string = str(item)
        if len(string) > max_length:
            return f"{string[:max_length]} {'...' if ellipsis else ''}"
        return string

    # class MapperEntry(asyncio.Future):


#
#     def __init__(self,  cdp_obj: Generator, id: int, session_id: str = None):
#
#         super().__init__()
#         self._cdp_obj = cdp_obj
#
#         method, *params = next(self._cdp_obj).values()
#         if params:
#             params = params.pop()
#
#         request = {"method": method, "params": params, "id": id}
#         if session_id:
#             request["sessionId"] = session_id
#
#         self.request = request
#         self.response = None
#         self.events = []
#
#     def set_session_id(self, session_id: str):
#         self.request['sessionId'] = session_id
#
#     def __call__(self, response: dict):
#         self.response = response
#         if "error" in response:
#             # set exception and bail out
#             return self.set_exception(ProtocolException(response["error"], request=self.request))
#         try:
#             # try to parse the result according to the py cdp docs.
#             self._cdp_obj.send(response["result"])
#         except StopIteration as e:
#             # exception value holds the parsed response
#             self.set_result(e.value)


class Connection:
    socket: websockets.asyncio.client.ClientConnection | None
    websocket_url: str = None

    @property
    def attached(self):
        return bool(self.session_id and self.target)

    @property
    def transactions(self):
        """
        simple array that holds recent transactions.
        each transaction consist of a response, request, result, events fields
        the latest transaction is the last element in the list.
        """
        return self._transactions

    @property
    def last_transaction(self):
        """
        simple alias to get the last transaction to inspect.
        """
        return self.transactions[-1]

    def __init__(
        self,
        target: TargetType = None,
        parent: Connection = None,
        auto_attach: bool = False,
        **kwargs,
    ) -> None:

        self.session_id = None
        self.websocket_url = parent.websocket_url if parent else None
        self.handlers = collections.defaultdict(list)
        self.lock = asyncio.Lock()
        self.socket = None
        self.target = target
        self.parent = parent
        self.__count__ = itertools.count(0)
        self._auto_attach = auto_attach
        self._transactions: List[Transaction] = []
        self._targets: List[Connection] = []

    #
    # @classmethod
    # async def from_parent(
    #     cls,
    #     target: cdp.target.TargetID | cdp.target.TargetInfo,
    #     parent: Connection,
    #     auto_attach: bool = False,
    # ) -> Connection:
    #     target_id = None
    #     if isinstance(target, cdp.target.TargetInfo):
    #         target_id = target.target_id
    #     elif isinstance(target, (cdp.target.TargetID, str)):
    #         target_id = target
    #     instance = cls(target=target_id, parent=parent, auto_attach=auto_attach)
    #     await instance.attach()
    #     return instance

    async def aopen(self):
        """ """
        if not self.websocket_url:
            raise RuntimeError("having no parent and no websocket url")

        if not self.socket or bool(self.socket.close_code):
            self.socket = await websockets.connect(
                self.websocket_url,
                ping_timeout=PING_TIMEOUT,
                max_size=MAX_SIZE,
            )

    async def aclose(self):
        """ """
        if self.socket:
            await self.socket.close()
            await self.socket.wait_closed()
        self.socket = None

    async def attach(self, target: TargetType = None):
        """ " """
        await self.aopen()
        target = target or self.target

        if not target:
            # is possibly browser target

            self.handlers[cdp.target.AttachedToTarget] = [
                lambda event: setattr(self, "target", event.target_info)
            ]
            self.session_id = await self.send(
                cdp.target.attach_to_browser_target(), _attach=True
            )
            self.handlers[cdp.target.AttachedToTarget] = []
            self.handlers.clear()
            if self._auto_attach:
                self.handlers[cdp.target.AttachedToTarget].append(self._attach_handler)
                self.handlers[cdp.target.DetachedFromTarget].append(
                    self._attach_handler
                )
                await self.send(
                    cdp.target.auto_attach_related(self.target.target_id, False)
                )

        else:
            target_id = None
            if isinstance(target, cdp.target.TargetInfo):
                target_id = target.target_id
            elif isinstance(target, (cdp.target.TargetID, str)):
                target_id = target
            self.session_id = await self.send(
                cdp.target.attach_to_target(target_id=target_id, flatten=True),
                _attach=True,
            )

            self.target = await self.send(cdp.target.get_target_info(target_id))
            if self._auto_attach:
                self.handlers.clear()
                self.handlers[cdp.target.AttachedToTarget].append(self._attach_handler)
                self.handlers[cdp.target.DetachedFromTarget].append(
                    self._attach_handler
                )
                self.handlers[cdp.target.TargetInfoChanged].append(self._attach_handler)
                self.handlers[cdp.target.TargetCrashed].append(self._attach_handler)
                await self.send(
                    cdp.target.set_auto_attach(
                        True, wait_for_debugger_on_start=False, flatten=True
                    )
                )
            # self.target = await self.send(cdp.target.get_target_info(target_id))

    async def detach(self):

        for child in self._targets:
            await child.detach()
        await self.send(
            cdp.target.detach_from_target(
                session_id=self.session_id, target_id=self.target.target_id
            ),
            _attach=True,
        )
        self.session_id = None
        self.target = None
        self.handlers.clear()
        self._targets.clear()

    async def _attach_handler(
        self,
        event: (
            cdp.target.AttachedToTarget
            | cdp.target.DetachedFromTarget
            | cdp.target.TargetInfoChanged
            | cdp.target.TargetDestroyed
        ),
    ):
        if isinstance(event, cdp.target.AttachedToTarget):
            if event.target_info.target_id == self.target.target_id:
                self.session_id = event.session_id
                self.target = event.target_info
            else:
                if event.target_info.type_ == "browser":
                    return
                elif event.target_info.type_ == "page":
                    from nodriver.core.tab import Tab

                    new_child = Tab(target=event.target_info, parent=self)
                    self._targets.append(new_child)
                elif event.target_info.type_ == "iframe":
                    from nodriver.core.tab import IFrame

                    new_child = IFrame(target=event.target_info, parent=self)
                    self._targets.append(new_child)
                else:
                    new_child = Connection(target=event.target_info, parent=self)
                    self._targets.append(new_child)

        elif isinstance(event, cdp.target.DetachedFromTarget):
            if event.target_id == self.target.target_id:
                self.session_id = None
            removed = [
                child for child in self._targets if child.session_id == event.session_id
            ]
            for child in removed:
                self._targets.remove(child)

        elif isinstance(event, cdp.target.TargetInfoChanged):
            if event.target_info.target_id == self.target.target_id:
                self.target = event.target_info
            else:
                for child in self._targets:
                    if (
                        child.target
                        and child.target.target_id == event.target_info.target_id
                    ):
                        child.target = event.target_info

        elif isinstance(event, cdp.target.TargetDestroyed):
            if event.target_id == self.target.target_id:
                self.target = None
            else:
                for child in self._targets.copy():
                    if child.target.target_id == event.target_id:
                        self._targets.remove(child)

    async def send(
        self,
        cdp_obj: Generator[dict[str, Any], dict[str, Any], Any],
        _attach: bool = False,
        **kwargs,
    ) -> Any:

        # if self.parent and self.session_id:
        #     return await self.parent.send(cdp_obj, **kwargs)

        if not _attach:
            if not self.attached or not self.socket:
                await self.attach()

        method, *params = next(cdp_obj).values()
        if params:
            params = params.pop()
        _id = next(self.__count__)
        message = {"method": method, "params": params, "id": _id}
        if not _attach:
            message["sessionId"] = self.session_id
        message.update(kwargs)

        self.transactions.append(Transaction(message))

        while len(self.transactions) > 25:
            # clears the oldest request/response pair from transactions
            self.transactions.pop(0)

        async with self.lock:
            await self.socket.send(json.dumps(message))
            while True:
                raw = await self.socket.recv()
                response_message = json.loads(raw)
                if not response_message:
                    raise RuntimeError("no message from stream: %s" % raw)
                if "result" not in response_message:
                    if "error" in response_message:
                        # set the exception visible in transactions
                        self.transactions[-1].result = ProtocolException(
                            response_message["error"]
                        )
                        raise self.transactions[-1].result

                    if "method" in response_message:
                        # event
                        try:
                            await self.process_event(response_message, _id)
                        except (Exception,):
                            raise RuntimeError(
                                "error processing event: %s which occurred during processing of event: %s"
                                % (response_message, message)
                            )
                else:
                    try:
                        cdp_obj.send(response_message["result"])
                    except StopIteration as e:
                        # exception value holds the parsed response
                        self.transactions[-1].result = e.value
                        return e.value
                    except (Exception,) as e:
                        self.transactions[-1].result = e
                        raise
                    finally:
                        await asyncio.sleep(0)

    async def process_event(self, message: dict, id: int) -> None:
        """ """
        event = None

        try:
            event = cdp.util.parse_json_event(message)
            self.transactions[-1].events.append(event)
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
                if iscoroutinefunction(callback) or iscoroutine(callback):
                    try:
                        # handler is defined with the second param being the tab instance
                        asyncio.create_task(callback(event, self))
                    except TypeError as e:
                        # handler is defined without the tab parameter
                        asyncio.create_task(callback(event))
                        # if this causes an exception it is handled by the outer handler
                else:
                    try:
                        # handler is defined with the second param being the tab instance
                        callback(event, self)
                    except TypeError:
                        # handler is defined without the tab parameter
                        callback(event)
                        # if this causes an exception it is handled by the outer handler

            except Exception as e:
                logger.warning(
                    "exception in callback %s for event %s => %s",
                    callback,
                    event.__class__.__name__,
                    e,
                    exc_info=True,
                )

    def __str__(self):
        name = self.__class__.__name__
        if self.target and self.target.type_:
            name = self.target.type_.title()
        name = util.to_camel(name)
        return (
            f"<{name}\n"
            f"\turl: {self.target.url if type(self.target) is cdp.target.TargetInfo else ''}\n"
            f"\tattached: {self.attached}>\n"
        )

    def __repr__(self):
        return self.__str__()
