import types
import unittest
from unittest.mock import Mock

from nodriver import cdp
from nodriver.core.browser import Browser


class BrowserPermissionsTests(unittest.IsolatedAsyncioTestCase):
    async def test_grant_all_permissions_without_error(self):
        sent_commands = []

        async def send(command):
            # cdp command generators yield a dict on first next()
            sent_commands.append(next(command))

        browser = Mock(spec=Browser)
        browser.send = send
        browser.grant_all_permissions = types.MethodType(
            Browser.grant_all_permissions, browser
        )

        await browser.grant_all_permissions()

        self.assertEqual(len(sent_commands), 1)
        cmd = sent_commands[0]
        self.assertEqual(cmd["method"], "Browser.grantPermissions")
        perms = cmd["params"]["permissions"]

        # Ensure excluded / deprecated permissions are not present
        self.assertNotIn("flash", perms)
        self.assertNotIn("FLASH", perms)
        self.assertNotIn("capturedSurfaceControl", perms)

        # Ensure standard permissions are included
        self.assertIn("geolocation", perms)
        self.assertIn("notifications", perms)
        self.assertIn("audioCapture", perms)
        self.assertIn("videoCapture", perms)
        self.assertIn("clipboardReadWrite", perms)

    async def test_grant_all_permissions_with_origin_and_context(self):
        sent_commands = []

        async def send(command):
            sent_commands.append(next(command))

        browser = Mock(spec=Browser)
        browser.send = send
        browser.grant_all_permissions = types.MethodType(
            Browser.grant_all_permissions, browser
        )

        context_id = cdp.browser.BrowserContextID("test-context-123")
        await browser.grant_all_permissions(
            origin="https://example.com",
            browser_context_id=context_id,
        )

        self.assertEqual(len(sent_commands), 1)
        cmd = sent_commands[0]
        self.assertEqual(cmd["params"].get("origin"), "https://example.com")
        self.assertEqual(cmd["params"].get("browserContextId"), "test-context-123")


if __name__ == "__main__":
    unittest.main()
