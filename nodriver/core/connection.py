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
from asyncio import iscoroutine, iscoroutinefunction
from typing import Any, Awaitable, Callable, Generator, List, TypeVar, Union

import websockets.asyncio.client

from .. import cdp
from . import browser as _browser
from . import util

T = TypeVar("T")

GLOBAL_DELAY = 0.005
MAX_SIZE: int = 2**28
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


class SettingClassVarNotAllowedException(PermissionError):
    pass


class Transaction(asyncio.Future):
    __cdp_obj__: Generator = None

    method: str = None
    params: dict = None

    id: int = None

    def __init__(self, cdp_obj: Generator):
        """
        :param cdp_obj:
        """
        super().__init__()
        self.__cdp_obj__ = cdp_obj
        self.connection = None

        self.method, *params = next(self.__cdp_obj__).values()
        if params:
            params = params.pop()
        self.params = params

    @property
    def message(self):
        return json.dumps({"method": self.method, "params": self.params, "id": self.id})

    @property
    def has_exception(self):
        try:
            if self.exception():
                return True
        except asyncio.InvalidStateError as e:  # noqa
            if "not set" in e.args:
                return False
        except:
            return True
        return False

    def __call__(self, **response: dict):
        """
        parsed the response message and marks the future
        complete

        :param response:
        :return:
        """
        if "error" in response:
            # set exception and bail out
            return self.set_exception(ProtocolException(response["error"]))
        try:
            # try to parse the result according to the py cdp docs.
            self.__cdp_obj__.send(response["result"])
        except KeyError as e:
            raise KeyError(f"key '{e.args}' not found in message: {response['result']}")
        except StopIteration as e:
            # exception value holds the parsed response
            self.set_result(e.value)

    def __repr__(self):
        success = False if (self.done() and self.has_exception) else True
        if self.done():
            status = "finished"
        else:
            status = "pending"
        fmt = (
            f"<{self.__class__.__name__}\n\t"
            f"method: {self.method}\n\t"
            f"status: {status}\n\t"
            f"success: {success}>"
        )
        return fmt


class EventTransaction(Transaction):
    event = None
    value = None

    def __init__(self, event_object):
        try:
            super().__init__(None)
        except:
            pass
        self.set_result(event_object)
        self.event = self.value = self.result()

    def __repr__(self):
        status = "finished"
        success = False if self.exception() else True
        event_object = self.result()
        fmt = (
            f"{self.__class__.__name__}\n\t"
            f"event: {event_object.__class__.__module__}.{event_object.__class__.__name__}\n\t"
            f"status: {status}\n\t"
            f"success: {success}>"
        )
        return fmt


class CantTouchThis(type):
    def __setattr__(cls, attr, value):
        """
        :meta private:
        """
        if attr == "__annotations__":
            # fix autodoc
            return super().__setattr__(attr, value)
        raise SettingClassVarNotAllowedException(
            "\n".join(
                (
                    "don't set '%s' on the %s class directly, as those are shared with other objects.",
                    "use `my_object.%s = %s`  instead",
                )
            )
            % (attr, cls.__name__, attr, value)
        )


class Connection(metaclass=CantTouchThis):
    attached: bool = None

    @property
    def browser(self) -> _browser.Browser:
        return self._browser

    @property
    def websocket(self) -> websockets.asyncio.client.ClientConnection:
        return self._websocket

    @property
    def target(self) -> cdp.target.TargetInfo:
        return self._target

    def __init__(
        self,
        websocket_url: str,
        target: cdp.target.TargetInfo = None,
        browser: _browser.Browser = None,
        **kwargs,
    ):
        super().__init__()
        self.websocket_url: str = websocket_url
        self.mapper = {}
        self.handlers = collections.defaultdict(list)
        self.enabled_domains = []
        self._target = target
        self._browser = browser
        self._websocket = None
        self._listener_task = None
        self._event = asyncio.Event()
        self._lock = asyncio.Lock()
        self.__count__ = itertools.count(0)
        self.__dict__.update(**kwargs)

    @property
    def closed(self):
        if not self.websocket:
            return True
        return bool(self.websocket.close_code)

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
                    if type(obj) != type:
                        continue
                    if inspect.isbuiltin(obj):
                        continue
                    del self.handlers[obj]
                return
            else:
                del self.handlers[evt_dom]

    async def connect(self, **kw):
        """
        opens the websocket connection. should not be called manually by users
        :param kw:
        :return:
        """
        if not self.websocket or bool(self.websocket.close_code):
            try:
                self._websocket = await websockets.connect(
                    self.websocket_url,
                    ping_timeout=PING_TIMEOUT,
                    max_size=MAX_SIZE,
                )
                self._listener_task = asyncio.ensure_future(self._listener())

            except (Exception,) as e:
                logger.debug("exception during opening of websocket : %s", e)
                raise

            await self._register_handlers()

    async def disconnect(self):
        """
        closes the websocket connection. should not be called manually by users.
        """
        if self._listener_task:
            self._listener_task.cancel()
        if self.websocket:
            self.enabled_domains.clear()
            await self.websocket.close()
            logger.debug("\n❌ closed websocket connection to %s", self.websocket_url)

    def __getattr__(self, item):
        """:meta private:"""
        try:
            return getattr(self.target, item)
        except AttributeError:
            raise

    async def __aenter__(self):
        """:meta private:"""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """:meta private:"""
        await self.close()

    async def _register_handlers(self):
        """
        ensure that for current (event) handlers, the corresponding
        domain is enabled in the protocol.

        """
        seen = []
        # save a copy of current enabled domains in a variable
        # domains will be removed from this variable
        # if it is still needed according to the set handlers
        # so at the end this variable will hold the domains that
        # are not represented by handlers, and can be removed
        enabled_domains = self.enabled_domains.copy()
        for event_type in self.handlers.copy():
            domain_mod = None
            if len(self.handlers[event_type]) == 0:
                self.handlers.pop(event_type)
                continue
            if isinstance(event_type, type):
                domain_mod = util.cdp_get_module(event_type.__module__)
            if domain_mod in self.enabled_domains:
                # at this point, the domain is being used by a handler
                # so remove that domain from temp variable 'enabled_domains' if present
                if domain_mod in enabled_domains:
                    enabled_domains.remove(domain_mod)
                continue
            elif domain_mod not in self.enabled_domains:
                if domain_mod in (cdp.target, cdp.storage):
                    # by default enabled
                    continue
                try:
                    # we add this before sending the request, because it will
                    # loop indefinite
                    logger.debug("registered %s", domain_mod)
                    self.enabled_domains.append(domain_mod)

                    await self.send(domain_mod.enable(), _is_update=True)

                except:  # noqa - as broad as possible, we don't want an error before the "actual" request is sent
                    logger.debug("", exc_info=True)
                    try:
                        self.enabled_domains.remove(domain_mod)
                    except:  # noqa
                        logger.debug("NOT GOOD", exc_info=True)
                        continue
                finally:
                    continue
        for ed in enabled_domains:
            # we started with a copy of self.enabled_domains and removed a domain from this
            # temp variable when we registered it or saw handlers for it.
            # items still present at this point are unused and need removal
            self.enabled_domains.remove(ed)

    async def _listener(self):
        seen_one = False
        while True:
            try:
                async with self._lock:
                    raw = await asyncio.wait_for(self.websocket.recv(), 0.05)
            except ProtocolException:
                break
            except websockets.exceptions.ConnectionClosedOK:
                await self.disconnect()
                break
            except websockets.exceptions.ConnectionClosed:
                await self.disconnect()
                break
            except asyncio.TimeoutError as e:
                await asyncio.sleep(0.05)
                continue
            except (Exception,) as e:
                logger.info(
                    "error when receiving websocket response: %s" % e, exc_info=True
                )
                raise
            else:
                message = json.loads(raw)
                seen_one = True
                if "id" in message:
                    tx: Transaction = self.mapper.pop(message["id"])
                    tx(**message)
                    logger.debug("got answer for (message_id:%d) => %s", tx.id, message)
                else:
                    # probably an event
                    try:
                        event = cdp.util.parse_json_event(message)
                    except Exception as e:
                        logger.info(
                            "%s: %s  during parsing of json from event : %s"
                            % (type(e).__name__, e.args, message),
                            exc_info=True,
                        )
                        continue
                    except KeyError as e:
                        logger.info("some lousy KeyError %s" % e, exc_info=True)
                        continue
                    try:
                        if type(event) in self.handlers:
                            callbacks = self.handlers[type(event)]
                        else:
                            continue
                        if not len(callbacks):
                            continue
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

                    except (Exception,) as e:
                        raise

    async def send(
        self, cdp_obj: Generator[dict[str, Any], dict[str, Any], Any], _is_update=False
    ) -> Any:
        """
        send a protocol command. the commands are made using any of the cdp.<domain>.<method>()'s
        and is used to send custom cdp commands as well.

        :param cdp_obj: the generator object created by a cdp method

        :param _is_update: internal flag
            prevents infinite loop by skipping the registeration of handlers
            when multiple calls to connection.send() are made
        :return:
        """
        if self.closed:
            await self.connect()
        if not _is_update:
            await self._register_handlers()
        tx = Transaction(cdp_obj)
        the_id = next(self.__count__)
        tx.id = the_id
        self.mapper[the_id] = tx
        asyncio.create_task(self.websocket.send(tx.message))
        return await tx

    async def _send_oneshot(self, cdp_obj):
        """fire and forget , eg: send command without waiting for any response"""
        return await self.send(cdp_obj, _is_update=True)
