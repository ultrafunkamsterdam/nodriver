import unittest
from unittest.mock import AsyncMock, MagicMock

from nodriver import cdp
from nodriver.core.connection import Connection
from nodriver.core.tab import Tab


class SessionAndDialogTests(unittest.IsolatedAsyncioTestCase):
    async def test_attach_idempotent_on_same_target(self):
        conn = Connection(target="target-123")
        conn.session_id = "session-abc"
        mock_socket = MagicMock()
        mock_socket.close_code = None
        conn.socket = mock_socket

        send_mock = AsyncMock()
        conn.send = send_mock

        # Calling attach on already-attached target should be a no-op
        await conn.attach("target-123")
        send_mock.assert_not_called()

        # Calling attach without argument should also be a no-op
        await conn.attach()
        send_mock.assert_not_called()

    async def test_process_event_filters_different_session(self):
        conn = Connection(target="target-123")
        conn.session_id = "session-tab"

        callback_called = False

        def on_event(event):
            nonlocal callback_called
            callback_called = True

        conn.handlers[cdp.page.JavascriptDialogOpening] = [on_event]

        # Event from a different session
        message_other_session = {
            "method": "Page.javascriptDialogOpening",
            "params": {
                "url": "https://example.com",
                "frameId": "frame-1",
                "message": "Hello",
                "type": "confirm",
                "hasBrowserHandler": True,
            },
            "sessionId": "session-other",
        }

        await conn.process_event(message_other_session)
        self.assertFalse(callback_called)

        # Event from the same session
        message_same_session = {
            "method": "Page.javascriptDialogOpening",
            "params": {
                "url": "https://example.com",
                "frameId": "frame-1",
                "message": "Hello",
                "type": "confirm",
                "hasBrowserHandler": True,
            },
            "sessionId": "session-tab",
        }

        await conn.process_event(message_same_session)
        self.assertTrue(callback_called)

    async def test_process_event_routes_to_child_target(self):
        parent = Connection(target="target-parent")
        parent.session_id = "session-parent"

        child = Connection(target="target-child", parent=parent)
        child.session_id = "session-child"
        parent._targets.append(child)

        child_callback_called = False

        def on_child_event(event):
            nonlocal child_callback_called
            child_callback_called = True

        child.handlers[cdp.page.JavascriptDialogOpening] = [on_child_event]

        message = {
            "method": "Page.javascriptDialogOpening",
            "params": {
                "url": "https://example.com",
                "frameId": "frame-child",
                "message": "Iframe alert",
                "type": "alert",
                "hasBrowserHandler": True,
            },
            "sessionId": "session-child",
        }

        await parent.process_event(message)
        self.assertTrue(child_callback_called)

    async def test_handle_dialog_command(self):
        tab = Tab(target="target-123")
        tab.session_id = "session-123"
        sent_commands = []

        async def fake_send(cdp_obj, **kwargs):
            payload = next(cdp_obj)
            sent_commands.append(payload)

        tab.send = fake_send

        await tab.handle_dialog(accept=True, prompt_text="User input")
        self.assertEqual(len(sent_commands), 1)
        self.assertEqual(
            sent_commands[0]["method"], "Page.handleJavaScriptDialog"
        )
        self.assertEqual(
            sent_commands[0]["params"],
            {"accept": True, "promptText": "User input"},
        )


if __name__ == "__main__":
    unittest.main()
