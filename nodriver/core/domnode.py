from __future__ import annotations

from typing import List

from . import util
from ._contradict import ContraDict
from .. import cdp


class DomNode:
    attrs: ContraDict

    def __init__(self, node: cdp.dom.Node, target: "nodriver.Page"):
        self._target = target
        self._attrs = ContraDict()
        self._node = node

    def __getattr__(self, item):
        print("getattr", item)
        x = self.attrs.get(item, None)
        if x:
            return x
        x = getattr(self._node, item, None)
        if x:
            return x

        raise AttributeError(f'{self.__class__.__name__} has no attribute "%s"' % item)

    def __getitem__(self, item):
        print(" getitem ", item)
        x = self.attrs.get(item, None)
        if x:
            return x
        x = getattr(self._node, item, None)
        if x:
            return x

    @property
    def node(self):
        return self._node

    @property
    def parent(self):
        return self._node.parent_id

    @property
    def children(self) -> List[DomNode]:
        return self.node.children

    @property
    def attrs(self) -> ContraDict:
        """
        holds the elments' attributes
        :return:
        :rtype:
        """
        sav = None
        for i, a in enumerate(self.node.attributes):  # noqa
            if i == 0 or i % 2 == 0:
                if a == "class":
                    a = "class_"
                sav = a
            else:
                if sav:
                    self._attrs[sav] = a
        for k, v in self.__dict__.items():
            if k[0] != "_":
                self._attrs.update({k: v})

        return self._attrs

    def _attrs_string(self):
        attrs = " ".join(
            [f'{k if k != "class_" else "class"}="{v}"' for k, v in self.attrs.items()]
        )
        return attrs

    async def save(self):
        doc = await self._target.send(cdp.dom.get_document(-1, True))
        updated_self = util.filter_recurse(
            doc, lambda n: n.backend_node_id == self.node.backend_node_id
        )
        # util.filter_recurse(self.node)
        self._node = updated_self
        await self._target.send(cdp.dom.set_outer_html(self.node.node_id, str(self)))
        await self.update()

    def __repr__(self):
        close_tag = " />"
        content = ""

        if self.children:  # optimize speed
            text_node = util.filter_recurse(
                self, lambda n: n.node_type == 3
            )  # 3 = textnode
            if text_node:
                # close_tag = f"</{self.node_name.lower()}>"
                content += text_node.node_value

        if self.node.node_type == 3:  # we could be an text node already
            content = self.node.node_value
            # < / {self.node_name.lower()} >
            # close_tag = f"</{self.node_name.lower()}>"
            content += f"{self.node.node_value}"

        if content:
            close_tag = f"</{self.node_name.lower()}>"
            content = f">{content}"

        attrs = self._attrs_string()
        s = f"<{self.node_name.lower()} {attrs}{content}{close_tag}"
        return s
