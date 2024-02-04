from __future__ import annotations

import asyncio
import collections
import functools
import importlib
import inspect
import itertools
import json
import logging
import types
import typing
from asyncio import iscoroutine, iscoroutinefunction
from typing import (
    Generator,
    Union,
    Dict,
    Awaitable,
    Callable,
    Any,
    TypeVar,
)

import websockets
from .. import cdp
from . import util

T = TypeVar("T")

GLOBAL_DELAY = 0.005
MAX_SIZE: int = 2**28
PING_TIMEOUT: int = 900  # 15 minutes

TargetType = Union[cdp.target.TargetInfo, cdp.target.TargetID]

logger = logging.getLogger("uc.connection")
tx_logger = logging.getLogger("uc.transaction")


class ProtocolException(ValueError):
    def __init__(self, *args, **kwargs):  # real signature unknown
        self.message = None
        self.code = None
        self.args = args
        if isinstance(args[0], dict):
            self.message = args[0].get("message", None)  # noqa
            self.code = args[0].get("code", None)

    def __str__(self):
        return f"{self.message} " f"[code: {self.code}]" if self.code else ""


class SettingClassVarNotAllowedException(PermissionError):
    pass


class Transaction(asyncio.Future):
    __counter__ = itertools.count(0)
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
        self.id = next(self.__counter__)
        self.method, *params = next(self.__cdp_obj__).values()
        if params:
            params = params.pop()
        self.params = params

    @property
    def message(self):
        return json.dumps({"method": self.method, "params": self.params, "id": self.id})

    # @property
    # def result(self):
    #     # just make it an attribute instead of having to call it
    #     return super().result()
    #
    # @property
    # def exception(self):
    #     # just make it an attribute instead of having to call it
    #     return super().exception()

    def __call__(self, **response: dict):
        """
        parsed the response message and marks the future
        complete

        :param response:
        :return:
        """

        # s = ""
        # for k,v in self.raw_request['params'].items():
        #     s += f"{k} = {v}"
        # print(s)
        # tx_logger.info(s)
        # tx_logger.debug(
        #     "\n[%d]\n"
        #     "-----------------\n"
        #     ">>> %s \n"
        #     "<<< %s \n"
        #     "-----------------\n",
        #     self.message_id,
        #     self.cdp_method,
        #     self.raw_response,
        # )

        if "error" in response:
            # set exception and bail out
            return self.set_exception(ProtocolException(response["error"]))
        try:
            # try to parse the result according to the py cdp docs.
            self.__cdp_obj__.send(response["result"])
        except StopIteration as e:
            # exception value holds the parsed response
            return self.set_result(e.value)
        raise ProtocolException("could not parse the cdp response:\n%s" % response)

    def __repr__(self):
        success = False if (self.done() and self.exception()) else True
        if self.done():
            status = "finished"
        else:
            status = "pending"
        fmt = (
            f"<{self.__class__.__name__} [message id: {self.id}] method: {self.method}\n\t"
            f"status: {status}\n\t"
            f"success: {success}>"
        )
        return fmt


class EventTransaction(Transaction):
    def __init__(self, message):
        try:
            super().__init__(None)
        except:
            pass
        self.response = message

    def __repr__(self):
        status = "finished"
        success = False if self.exception else True

        fmt = f"<{self.__class__.__name__}\n\t" f"event: {self.response.__class__}"
        return fmt


def update_targets(fn: types.MethodType):
    # instance = fn.__self__
    print("fn = ", fn)
    globals()["fn"] = fn

    @functools.wraps(fn)
    async def wrapped(*args, **kwargs):
        self = args[0]
        res = await fn(*args, **kwargs)
        targets = await fn(self.send(cdp.target.get_targets()))
        print("targets = ", targets)
        return res

    return wrapped


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
    websocket: websockets.WebSocketClientProtocol
    _target: cdp.target.TargetInfo

    def __init__(
        self,
        websocket_url: str,
        target: cdp.target.TargetInfo = None,
        _owner: "Browser" = None,
        **kwargs,
    ):
        super().__init__()
        self._target = target
        self.__count__ = itertools.count(0)
        # self._owner = _owner

        self.websocket_url: str = websocket_url
        self.websocket = None
        self.mapper = {}
        self.handlers = collections.defaultdict(list)
        self.recv_task = None
        self.enabled_domains = []
        self._last_result = []
        self.listener: Listener = None
        # self.listener_task  = None
        # self.target = target
        # self.type: str = ""

        # self._targets = []

        # if target and target.type_:
        #     self.type = target.__dict__.pop('type_')
        # self._retrieve_task = None
        self.__dict__.update(**kwargs)

    @property
    def target(self) -> cdp.target.TargetInfo:
        return self._target

    @target.setter
    def target(self, target: cdp.target.TargetInfo):
        if not isinstance(target, cdp.target.TargetInfo):
            raise TypeError(
                "target must be set to a '%s' but got '%s"
                % (cdp.target.TargetInfo.__name__, type(target).__name__)
            )
        self._target = target
        # try:
        #     self.__dict__.update(target.__dict__)
        # except AttributeError:
        #     pass

    def add_handler(
        self,
        event_type_or_domain: Union[type, types.ModuleType],
        handler: Union[Callable, Awaitable],
    ):
        """
        add a handler for an event type or entire domain (=all events for that domain)

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
        if isinstance(event_type_or_domain, types.ModuleType):
            for name, obj in inspect.getmembers_static(cdp.network):
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
        self.handlers[event_type_or_domain].append(handler)

    @classmethod
    async def create(cls, websocket_url: str, **kwargs):
        instance = cls(websocket_url, **kwargs)
        # await instance.open()
        return instance
        # instance.recv_task = asyncio.create_task(instance.recv_loop())
        # return instance

    async def aopen(self, **kw):
        """
        :param kw:
        :return:
        """
        if not self.websocket or self.websocket.closed:
            self.websocket = await websockets.connect(
                self.websocket_url,
                ping_timeout=PING_TIMEOUT,
                max_size=MAX_SIZE,
            )
            self.listener = Listener(self)
        if not self.listener or not self.listener.running:
            self.listener = Listener(self)

            # if self.websocket and not self._retrieve_task or self._retrieve_task.done():
            #     self._retrieve_task = asyncio.ensure_future(self._retrieve_loop())
            logger.debug("\n✅  opened websocket connection to %s", self.websocket_url)
            # self.recv_task = asyncio.create_task(self.recv_loop())

    async def aclose(self):
        if self.websocket and not self.websocket.closed:
            if self.listener and self.listener.running:
                self.listener.cancel()

            await self.websocket.close()
            logger.debug("\n❌ closed websocket connection to %s", self.websocket_url)

    async def sleep(self, t: Union[int, float] = 0.25):
        await asyncio.sleep(t)

    async def wait(self):
        await self
        await self.listener.busy.wait()

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
        await self.aclose()
        if exc_type and exc_val:
            raise exc_type(exc_val)

    def __await__(self):
        return self.update_target().__await__()

    async def update_target(self):
        target_info: cdp.target.TargetInfo = await self.send(
            cdp.target.get_target_info(self.target_id), _is_update=True
        )
        self.target.__dict__.update(target_info.__dict__)

    async def send(
        self, cdp_obj: Generator[dict[str, Any], dict[str, Any], Any], _is_update=False
    ) -> Any:
        """
        send a protocol command

        :rtype: object
        :param cdp_obj:
        :param _is_update:
        :return:
        """
        await self.aopen()
        if not self.listener or not self.listener.running:
            self.listener = Listener(self)

        tx = Transaction(cdp_obj)
        tx.connection = self
        self.mapper.update({tx.id: tx})

        if not _is_update:
            # pass
            await self._register_handlers()

        # send out
        await self.websocket.send(tx.message)

        # try:
        return await tx
        # finally:
        # await asyncio.sleep(GLOBAL_DELAY)

    # async def listener(self):
    #
    #     if not self.websocket:
    #         await self.open()
    #     while True:
    #         try:
    #             msg = await asyncio.wait_for(self.websocket.recv(), 1)
    #         except asyncio.TimeoutError:
    #             self.recv_task_busy.clear()
    #             await self.sleep(.5)
    #             continue
    #         # async for msg in self.websocket:
    #         self.recv_task.busy.set()
    #         message = json.loads(msg)
    #         if "id" in message:
    #             # response to our command
    #             if message["id"] in self.mapper:
    #                 tx = self.mapper[message["id"]]
    #                 tx(**message)
    #         else:
    #             # probably an event
    #             try:
    #                 event = cdp.util.parse_json_event(message)
    #
    #             except Exception as e:
    #                 logger.info(
    #                     "%s: %s  during parsing of json from event : %s"
    #                     % (type(e).__name__, e.args, message),
    #                     exc_info=True,
    #                 )
    #
    #                 continue
    #             except KeyError as e:
    #                 logger.info("some lousy KeyError %s" % e, exc_info=True)
    #
    #                 continue
    #
    #             try:
    #                 # logger.warning('%s in handlers? %s' % (type(event), type(event) in self.handlers))
    #                 if type(event) in self.handlers:
    #                     callbacks = self.handlers[type(event)]
    #                 else:

    #                     module = cdp_get_module(type(event).__module__)
    #                     event_type = getattr(module, type(event).__qualname__, None)
    #                     if not event_type:
    #                         continue
    #                     callbacks = self.handlers[event_type]
    #                 # logger.warning('callbacks? %s' % callbacks)
    #                 if not len(callbacks):
    #                     continue
    #                 # if not isinstance(callbacks, typing.Sequence):
    #                 #     if isinstance(callbacks, types.FunctionType):
    #                 #         self.handlers[type(event)] = [callbacks]
    #
    #                 for handler in self.handlers[type(event)]:
    #                     try:
    #                         if iscoroutinefunction(handler) or iscoroutine(handler):
    #                             await handler(event)
    #                         else:
    #                             handler(event)
    #
    #                     except Exception as e:
    #                         logger.warning(
    #                             "exception in handler %s for event %s => %s",
    #                             handler,
    #                             event.__class__.__name__,
    #                             e,
    #                             exc_info=True,
    #                         )
    #                         raise
    #             except Exception:
    #                 raise
    #
    #             continue

    async def _register_handlers(self):
        """
        ensure that for current (event) handlers, the corresponding
        domain is enabled in the protocol.

        """
        seen = []
        for event_type in self.handlers.copy():
            domain_mod = None
            if len(self.handlers[event_type]) == 0:
                self.handlers.pop(event_type)
                continue
            if isinstance(event_type, type):
                domain_mod = util.cdp_get_module(event_type.__module__)
            # if isinstance(event_type, types.ModuleType):
            #     domain_mod = event_type
            if domain_mod in self.enabled_domains:
                continue
            elif domain_mod not in self.enabled_domains:
                if domain_mod in (cdp.target, cdp.storage):
                    # by default enabled
                    continue
                try:
                    # we add this before sending the request, because it will
                    # loop indefinite
                    # self.enabled_domains.append(domain_mod)
                    self.enabled_domains.append(domain_mod)
                    # logger.debug("added %s to enabled domains" % domain_mod)
                    await self.send(domain_mod.enable(), _is_update=True)

                except:  # noqa - as broad as possible, we don't want an error before the "actual" request is sent
                    logger.info("", exc_info=True)
                    try:
                        self.enabled_domains.remove(domain_mod)
                    except:  # noqa
                        logger.debug("NOT GOOD", exc_info=True)
                        continue
                finally:
                    continue


class Listener:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.task: asyncio.Future = None
        self.busy = asyncio.Event()
        self.run()

    # def busy_monitor(self):
    #     print('recv_task busy ? ', self.busy.is_set())
    #     asyncio.get_running_loop().call_later(.5, self.busy_monitor)

    def run(self):
        self.task = asyncio.create_task(self.listener_loop())

    def cancel(self):
        self.task.cancel()

    @property
    def running(self):
        if not self.task:
            return False
        if self.task.done():
            return False
        return True

    async def listener_loop(self):
        if not self.connection.websocket:
            await self.connection.aopen()
        while True:
            try:
                msg = await asyncio.wait_for(self.connection.websocket.recv(), 1)
            except asyncio.TimeoutError:
                self.busy.clear()
                await asyncio.sleep(0.1)
                continue
            except Exception:
                break
            # async for msg in self.connection.websocket:
            if not self.running:
                print("not running")
                break
            self.busy.set()
            message = json.loads(msg)
            if "id" in message:
                # response to our command
                if message["id"] in self.connection.mapper:
                    tx = self.connection.mapper[message["id"]]
                    tx(**message)
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
                    if type(event) in self.connection.handlers:
                        callbacks = self.connection.handlers[type(event)]
                    else:
                        continue

                    if not len(callbacks):
                        continue

                    for handler in self.connection.handlers[type(event)]:
                        try:
                            if iscoroutinefunction(handler) or iscoroutine(handler):
                                await handler(event)
                            else:
                                handler(event)

                        except Exception as e:
                            logger.warning(
                                "exception in handler %s for event %s => %s",
                                handler,
                                event.__class__.__name__,
                                e,
                                exc_info=True,
                            )
                            raise
                except Exception:
                    raise

                continue
