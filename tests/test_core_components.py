import asyncio
import unittest
import warnings
from unittest.mock import AsyncMock, MagicMock

from nodriver import cdp
from nodriver.core.browser import Browser
from nodriver.core.connection import Connection, Transaction
from nodriver.core.element import Element
from nodriver.core.tab import Tab


class TestCoreComponents(unittest.TestCase):
    def test_transaction_params_dict_fallback(self):
        # send() fallback sets params to dict if absent or non-dict
        tx_dict = Transaction({"id": 1, "method": "Target.getTargets", "params": {"key": "val"}})
        self.assertEqual(tx_dict.request["params"], {"key": "val"})

    def test_cookie_resilient_deserialization(self):
        cookie_json = {
            "name": "session_id",
            "value": "xyz123",
            "domain": ".example.com",
            "path": "/",
            "expires": 1893456000.0,
            "size": 16,
            "httpOnly": True,
            "secure": True,
            "session": False,
            "priority": "Medium",
            "sourceScheme": "Secure",
            "sourcePort": 443,
        }
        cookie = cdp.network.Cookie.from_json(cookie_json)
        self.assertEqual(cookie.name, "session_id")
        self.assertEqual(cookie.value, "xyz123")
        self.assertEqual(cookie.source_port, 443)

    def test_connection_and_tab_closed_properties(self):
        conn = Connection()
        self.assertTrue(conn.closed)
        self.assertTrue(conn.is_closed)

        mock_socket = MagicMock()
        mock_socket.close_code = None
        mock_socket.closed = False
        conn.socket = mock_socket
        self.assertFalse(conn.closed)
        self.assertFalse(conn.is_closed)

        mock_socket.close_code = 1000
        self.assertTrue(conn.closed)

        tab = Tab()
        self.assertTrue(tab.closed)
        self.assertTrue(tab.is_closed)

        tab.socket = mock_socket
        mock_socket.close_code = None
        self.assertFalse(tab.closed)
        tab._closed = True
        self.assertTrue(tab.closed)
        self.assertTrue(tab.is_closed)

    def test_browser_stop_idempotent(self):
        b = Browser.__new__(Browser)
        b.socket = None
        b._process = None
        b._process_pid = None
        b.stop()
        self.assertIsNone(b._process)
        self.assertIsNone(b._process_pid)

    def test_mouse_drag_coordinate_offset(self):
        tab = Tab()
        tab.mouse_drag = AsyncMock()
        elem = Element.__new__(Element)
        elem._attrs = {}
        elem._tab = tab
        object.__setattr__(elem, "get_position", AsyncMock(return_value=MagicMock(center=[100.0, 100.0])))

        asyncio.run(elem.mouse_drag([50.0, 20.0], relative=True))
        tab.mouse_drag.assert_called_once_with(
            [100.0, 100.0],
            (150.0, 120.0),
            relative=False,
            steps=1,
        )

    def test_flash_point_coordinate_validation(self):
        tab = Tab()
        tab.evaluate = AsyncMock()
        asyncio.run(tab.flash_point(None, 50.0))
        tab.evaluate.assert_not_called()

        asyncio.run(tab.flash_point(10.0, None))
        tab.evaluate.assert_not_called()

    def test_scroll_bottom_reached_boolean_result(self):
        tab = Tab()
        tab.evaluate = AsyncMock(return_value=True)
        res = asyncio.run(tab.scroll_bottom_reached())
        self.assertTrue(res)

        tab.evaluate = AsyncMock(return_value=False)
        res = asyncio.run(tab.scroll_bottom_reached())
        self.assertFalse(res)

    def test_process_event_session_isolation(self):
        conn = Connection()
        conn.session_id = "target-session-1"
        handled = []
        conn.handlers[cdp.page.JavascriptDialogOpening] = [lambda ev: handled.append(ev)]

        # Event for a different session should be discarded
        foreign_event = {
            "method": "Page.javascriptDialogOpening",
            "params": {
                "url": "https://example.com",
                "frameId": "frame-1",
                "message": "Confirm?",
                "type": "confirm",
                "hasBrowserHandler": False,
                "defaultPrompt": "",
            },
            "sessionId": "target-session-2",
        }
        asyncio.run(conn.process_event(foreign_event))
        self.assertEqual(len(handled), 0)

        # Event for matching session should be processed
        matching_event = {
            "method": "Page.javascriptDialogOpening",
            "params": {
                "url": "https://example.com",
                "frameId": "frame-1",
                "message": "Confirm?",
                "type": "confirm",
                "hasBrowserHandler": False,
                "defaultPrompt": "",
            },
            "sessionId": "target-session-1",
        }
        asyncio.run(conn.process_event(matching_event))
        self.assertEqual(len(handled), 1)

    def test_grant_all_permissions_safe_enum_filtering(self):
        b = Browser.__new__(Browser)
        b.send = AsyncMock()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            asyncio.run(b.grant_all_permissions())
        b.send.assert_called_once()
        sent_call = b.send.call_args[0][0]
        method_dict = next(sent_call)
        self.assertEqual(method_dict["method"], "Browser.grantPermissions")
        perms = method_dict["params"]["permissions"]
        self.assertNotIn("flash", perms)


if __name__ == "__main__":
    unittest.main()
