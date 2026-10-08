import types
import unittest
from unittest.mock import AsyncMock, Mock

from nodriver.core.element import Element
from nodriver.core.tab import Tab


class ElementMouseDragTests(unittest.IsolatedAsyncioTestCase):
    async def test_drag_destinations(self):
        for steps in (1, 4):
            for kind, relative, expected in (
                ("tuple", False, (40, 60)),
                ("tuple", True, (160, 170)),
                ("list", True, (160, 170)),
                ("element", False, (300, 200)),
                ("element", True, (300, 200)),
            ):
                with self.subTest(steps=steps, kind=kind, relative=relative):
                    events = []

                    async def send(command):
                        events.append(next(command)["params"])

                    tab = types.SimpleNamespace(send=send)
                    tab.mouse_drag = types.MethodType(Tab.mouse_drag, tab)
                    source = Mock(spec=Element)
                    source.get_position = AsyncMock(
                        return_value=types.SimpleNamespace(center=(120, 110))
                    )
                    source._tab = tab
                    if kind == "element":
                        destination = Mock(spec=Element)
                        destination.get_position = AsyncMock(
                            return_value=types.SimpleNamespace(center=expected)
                        )
                    else:
                        destination = (40, 60) if kind == "tuple" else [40, 60]

                    await Element.mouse_drag(
                        source, destination, relative=relative, steps=steps
                    )

                    self.assertEqual(events[0]["type"], "mousePressed")
                    self.assertEqual((events[0]["x"], events[0]["y"]), (120, 110))
                    self.assertEqual(events[-1]["type"], "mouseReleased")
                    self.assertEqual((events[-1]["x"], events[-1]["y"]), expected)
                    self.assertEqual((events[-2]["x"], events[-2]["y"]), expected)
