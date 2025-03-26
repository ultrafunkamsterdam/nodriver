from typing import Any, Generator

from .. import cdp
from .element import create
from .tab import Tab


class JSInterface:

    def __init__(self, tab: Tab):
        self._tab = tab
        self._ser = cdp.runtime.SerializationOptions(
            serialization="deep",
            max_depth=10,
            additional_parameters={"maxNodeDepth": 10, "includeShadowTree": "all"},
        )

    async def send(
        self, cdp_object: Generator[dict[str, Any], dict[str, Any], Any]
    ) -> Any:
        return await self._tab.send(cdp_object)

    async def querySelector(self, query: str):
        raw: tuple[cdp.runtime.RemoteObject, Any] = await self.send(
            cdp.runtime.evaluate(
                'document.querySelector("%s")' % query,
                await_promise=True,
                return_by_value=False,
                user_gesture=True,
                serialization_options=self._ser,
            )
        )
        js_node = await JSNode.create(raw[0].deep_serialized_value.value, self._tab)
        return await create(js_node, self._tab, js_node)

    async def querySelectorAll(self, query: str):
        raw: tuple[cdp.runtime.RemoteObject, Any] = await self.send(
            cdp.runtime.evaluate(
                'document.querySelectorAll("%s")' % query,
                await_promise=True,
                return_by_value=False,
                user_gesture=True,
                serialization_options=self._ser,
            )
        )
        js_nodes = [
            await JSNode.create(el, self._tab)
            for el in raw[0].deep_serialized_value.value
        ]
        return [await create(el, self._tab) for el in js_nodes]

    async def queryXPath(self, path: str):
        """

        :param path:
        :type path:
        :return:
        :rtype:
        """
        js_impl = """
              function xPath(path){
                var result = [];
                var nodesSnapshot = document.evaluate(path, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null );
                for ( var i=0 ; i < nodesSnapshot.snapshotLength; i++ ){
                  result.push( nodesSnapshot.snapshotItem(i) );
                }
                return result;
              };
              xPath(`%s`)
              """
        raw = await self._tab.send(
            cdp.runtime.evaluate(
                js_impl % path,
                await_promise=True,
                return_by_value=False,
                user_gesture=True,
                serialization_options=self._ser,
            )
        )

        js_nodes = [
            await JSNode.create(el, self._tab)
            for el in raw[0].deep_serialized_value.value
        ]

        return [await create(el, self._tab) for el in js_nodes]


class JSNode(cdp.dom.Node):
    _required = [
        "node_id",
        "backend_node_id",
        "node_type",
        "node_name",
        "local_name",
        "node_value",
    ]

    def __init__(self, obj: dict):
        super().__init__(**obj)

    @classmethod
    async def create(cls, obj: dict, tab: Tab):
        if not isinstance(obj, dict):
            obj = obj.__dict__
        if "value" in obj:
            obj = obj["value"]
        d = {}
        obj = recursive_camel_to_snake(obj)
        for k, v in obj.items():
            if k not in cls._required:
                continue
            d[k] = v

        d["node_name"] = obj.get("local_name")
        d["local_name"] = d["node_name"]
        d["node_id"] = None
        # await tab.send(cdp.dom.get_document(-1, True))
        # js_obj: cdp.runtime.RemoteObject = await tab.send(
        #     cdp.dom.resolve_node(backend_node_id=cdp.dom.BackendNodeId(d['backend_node_id'])))
        # d['node_id'] = await tab.send(cdp.dom.request_node(object_id=js_obj.object_id))
        d["node_value"] = None
        if "children" in obj:
            d["children"] = []
            for chobj in obj["children"]:
                d["children"].append(await cls.create(chobj, tab))
        instance = cls(d)
        return instance


def recursive_camel_to_snake(obj):
    new = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            new[camel_to_snake(k)] = recursive_camel_to_snake(v)
        return new
    elif isinstance(obj, list):
        return [recursive_camel_to_snake(item) for item in obj]
    else:
        return obj


import re

RE_CAMEL_TO_SNAKE = re.compile("((?!^)(?<!_)[A-Z][a-z]+|(?<=[a-z0-9])[A-Z])")
RE_SNAKE_TO_CAMEL = re.compile("(.*?)_([a-zA-Z])")


def camel_to_snake(s):
    """
    Converts CamelCase/camelCase to snake_case
    :param str s: string to be converted
    :return: (str) snake_case version of s
    """
    return RE_CAMEL_TO_SNAKE.sub(r"_\1", s).lower()


def snake_to_camel(s):
    """
    Converts snake_case_string to camelCaseString
    :param str s: string to be converted
    :return: (str) camelCase version of s
    """
    return RE_SNAKE_TO_CAMEL.sub(lambda m: m.group(1) + m.group(2).upper(), s, 0)


#
class JSHTMLElement:

    def __init__(self, obj: dict):
        # node_type = None,
        # child_node_count = None,
        # backend_node_id = None,
        # loader_id = None,
        # frame_id = None ,
        # shadow_root = None,
        # local_name = None,
        # namespace_uri = None,
        # attributes = None,
        # **kwargs,
        obj = recursive_camel_to_snake(obj)
        if obj.get("children", None):
            children = obj.pop("children")
            obj["children"] = [JSHTMLElement(o) for o in children]
        self.__dict__.update(obj)

    def __repr__(self):
        s = (
            "<{0.__class__.__name__}(\n".format(self)
            + (
                "\n".join(
                    f"{k}={v}" for k, v in self.__dict__.items() if k != "children"
                )
            )
            + "\n)"
        )
        return s


def translate_serialized(obj: cdp.runtime.DeepSerializedValue | dict):
    raw_obj = {}
    if isinstance(obj, cdp.runtime.DeepSerializedValue):
        raw_obj = obj.__dict__
        try:
            obj_type = raw_obj["type_"]
        except KeyError:
            obj_type = raw_obj["type"]
    else:
        raw_obj = obj
        try:
            obj_type = raw_obj["type_"]
        except KeyError:
            obj_type = raw_obj["type"]

    if obj_type == "array":
        arr = raw_obj["value"]
        return [translate_serialized(item) for item in arr]
        # return arr
    elif obj_type == "node":
        node = raw_obj["value"]
        return JSHTMLNode(**node)


class JSHTMLNode:
    def __init__(
        self,
        nodeType=None,
        childNodeCount=None,
        backendNodeId=None,
        loaderId=None,
        shadowRoot=None,
        localName=None,
        namespaceURI=None,
        attributes=None,
        children=None,
        nodeValue=None,
        **kwargs,
    ):

        self.node_type: int = nodeType
        self.node_type_name: nodeType = (
            nodeType == 1 and "node" or nodeType == 11 and "shadow-root" or "text"
        )
        self.child_node_count: int = childNodeCount
        self.backend_node_id = (
            cdp.dom.BackendNodeId(backendNodeId) if backendNodeId else None
        )
        self.loader_id: str = loaderId

        self.local_name: str = localName or "shadow-root" if nodeType == 11 else None
        self.node_name: str = self.local_name.upper() if self.local_name else ""
        self.namespace_uri: str = namespaceURI
        self.attributes: dict = attributes or {}
        if shadowRoot:

            self.shadow_roots = JSHTMLNode(**shadowRoot["value"])
        else:
            self.shadow_roots = []
        if children:
            self.children = [JSHTMLNode(**child["value"]) for child in children]
        else:
            self.children = []
        self.node_value = nodeValue

    def __repr__(self):
        tag_name = self.node_name.lower()
        content = ""
        # collect all text from this leaf
        if self.child_node_count:
            if self.child_node_count == 1:
                if self.children:
                    content += str(self.children[0])

            elif self.child_node_count > 1:
                if self.children:
                    for child in self.children:
                        content += str(child)

        if self.node_type == 3:  # we could be a text node ourselves
            content += self.node_value

            # return text only, no tag names
            # this makes it look most natural, and compatible with other hml libs
            return content

        attrs = " ".join(
            [
                f'{k if k != "class_" else "class"}="{v}"'
                for k, v in self.attributes.items()
            ]
        )
        s = f"<{tag_name} {attrs}>{content}</{tag_name}>"
        return s
