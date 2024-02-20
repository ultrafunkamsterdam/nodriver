from __future__ import annotations

import asyncio
import logging
import shutil
import types
import typing
from typing import Optional, List, Set, Union, Callable

import typing_extensions

from .element import Element

if typing_extensions.TYPE_CHECKING:
    from .browser import Browser, PathLike
from .config import Config
from .. import cdp

__registered__instances__: Set[Browser] = set()

logger = logging.getLogger(__name__)
T = typing.TypeVar("T")


async def start(
    config: Optional[Config] = None,
    *,
    user_data_dir: Optional[PathLike] = None,
    headless: Optional[bool] = False,
    browser_executable_path: Optional[PathLike] = None,
    browser_args: Optional[List[str]] = None,
    sandbox: Optional[bool] = True,
    lang: Optional[str] = None,
    **kwargs: Optional[dict],
) -> Browser:
    """
    helper function to launch a browser. it accepts several keyword parameters.
    conveniently, you can just call it bare (no parameters) to quickly launch an instance
    with best practice defaults.
    note: this should be called ```await start()```

    :param user_data_dir:
    :type user_data_dir: PathLike

    :param headless:
    :type headless: bool

    :param browser_executable_path:
    :type browser_executable_path: PathLike

    :param browser_args: ["--some-chromeparam=somevalue", "some-other-param=someval"]
    :type browser_args: List[str]

    :param sandbox: default True, but when set to False it adds --no-sandbox to the params, also
    when using linux under a root user, it adds False automatically (else chrome won't start
    :type sandbox: bool

    :param lang: language string
    :type lang: str
    :return:
    """
    if not config:
        config = Config(
            user_data_dir,
            headless,
            browser_executable_path,
            browser_args,
            sandbox,
            lang,
            **kwargs,
        )
    from .browser import Browser

    return await Browser.create(config)


async def create_from_undetected_chromedriver(
    driver: "undetected_chromedriver.Chrome",
) -> Browser:
    """
    create a nodriver.Browser instance from a running undetected_chromedriver.Chrome instance.
    """
    from .config import Config

    conf = Config()

    host, port = driver.options.debugger_address.split(":")
    conf.host, conf.port = host, int(port)

    # create nodriver Browser instance
    browser = await start(conf)

    browser._process_pid = driver.browser_pid
    # stop chromedriver binary
    driver.service.stop()
    driver.browser_pid = -1
    driver.user_data_dir = None
    return browser


def get_registered_instances():
    return __registered__instances__


def free_port() -> int:
    """
    Determines a free port using sockets.
    """
    import socket

    free_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    free_socket.bind(("127.0.0.1", 0))
    free_socket.listen(5)
    port: int = free_socket.getsockname()[1]
    free_socket.close()
    return port


def deconstruct_browser():
    import time

    for _ in __registered__instances__:
        if not _.stopped:
            _.stop()
        for attempt in range(5):
            try:
                if _.config and not _.config.custom_data_dir:
                    shutil.rmtree(_.config.user_data_dir, ignore_errors=False)
            except FileNotFoundError as e:
                break
            except (PermissionError, OSError) as e:
                if attempt == 4:
                    logger.debug(
                        "problem removing data dir %s\nConsider checking whether it's there and remove it by hand\nerror: %s",
                        _.config.user_data_dir,
                        e,
                    )
                    break
                time.sleep(0.15)
                continue
        print("successfully removed temp profile %s", _.config.user_data_dir)


def filter_recurse_all(
    doc: T, predicate: Callable[[cdp.dom.Node, Element], bool]
) -> List[T]:
    """
    test each child using predicate(child), and return all children for which predicate(child) == True

    :param doc: the cdp.dom.Node object or :py:class:`nodriver.Element`
    :param predicate: a function which takes a node as first parameter and returns a boolean, where True means include
    :return:
    :rtype:
    """
    if not hasattr(doc, "children"):
        raise TypeError("object should have a .children attribute")
    out = []
    if doc and doc.children:
        for child in doc.children:
            if predicate(child):
                # if predicate is True
                out.append(child)
            out.extend(filter_recurse_all(child, predicate))
            # if result:
            #     out.append(result)
    return out


def filter_recurse(doc: T, predicate: Callable[[cdp.dom.Node, Element], bool]) -> T:
    """
    test each child using predicate(child), and return the first child of which predicate(child) == True

    :param doc: the cdp.dom.Node object or :py:class:`nodriver.Element`
    :param predicate: a function which takes a node as first parameter and returns a boolean, where True means include

    """
    if not hasattr(doc, "children"):
        raise TypeError("object should have a .children attribute")

    if doc and doc.children:
        for child in doc.children:
            if predicate(child):
                # if predicate is True
                return child
            result = filter_recurse(child, predicate)
            if result:
                return result


def remove_from_tree(tree: cdp.dom.Node, node: cdp.dom.Node) -> cdp.dom.Node:
    if not hasattr(tree, "children"):
        raise TypeError("object should have a .children attribute")

    if tree and tree.children:
        for child in tree.children:
            if child.backend_node_id == node.backend_node_id:
                tree.children.remove(child)
            remove_from_tree(child, node)
    return tree


async def html_from_tree(tree: Union[cdp.dom.Node, Element], target: "nodriver.Tab"):
    if not hasattr(tree, "children"):
        raise TypeError("object should have a .children attribute")
    out = ""
    if tree and tree.children:
        for child in tree.children:
            if isinstance(child, Element):
                out += await child.get_html()
            else:
                out += await target.send(
                    cdp.dom.get_outer_html(backend_node_id=child.backend_node_id)
                )
            out += await html_from_tree(child, target)
    return out


def loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop


def cdp_get_module(domain: Union[str, types.ModuleType]):
    """
    get cdp module by given string

    :param domain:
    :type domain:
    :return:
    :rtype:
    """
    import importlib

    if isinstance(domain, types.ModuleType):
        # you get what you ask for
        domain_mod = domain
    else:
        try:
            if domain in ("input",):
                domain = "input_"

            #  fallback if someone passes a str
            domain_mod = getattr(cdp, domain)
            if not domain_mod:
                raise AttributeError
        except AttributeError:
            try:
                domain_mod = importlib.import_module(domain)
            except ModuleNotFoundError:
                raise ModuleNotFoundError(
                    "could not find cdp module from input '%s'" % domain
                )
    return domain_mod


class js_helpers:
    @staticmethod
    def dumps(obj: str, indent: int = 4):
        return """
        (
           (value, space) => {
               var cache = [];
               var output = JSON.stringify(value, function(key, value) {
                   if (key && key.length > 0 && (key.charAt(0) == "$" || key.charAt(0) == "_")) {
                       return;
                   }
                   if (typeof value === 'object' && value !== null) {
                       if (cache.indexOf(value) !== -1) {
                           // Circular reference found, discard key
                           return;
                       }
                       // Store value in our collection
                       cache.push(value);
                   }
                   return value;
               }, space)
               cache = null; // Enable garbage collection
               return output;
           }
    )(%s, %d)
    """ % (
            obj,
            indent,
        )
