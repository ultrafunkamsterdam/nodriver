import asyncio
import unittest
from unittest import mock

from nodriver.core import connection
from nodriver.core.connection import Connection


class AopenConcurrencyTests(unittest.IsolatedAsyncioTestCase):
    async def test_concurrent_aopen_opens_one_socket_and_one_listener(self):
        sockets = []
        listeners = []

        async def fake_connect(*args, **kwargs):
            await asyncio.sleep(0)  # the real handshake yields here
            socket = mock.Mock(close_code=None)
            sockets.append(socket)
            return socket

        async def fake_listener(self):
            listeners.append(self.socket)

        conn = Connection()
        conn.websocket_url = "ws://127.0.0.1:9222/devtools/page/test"
        patch_connect = mock.patch.object(
            connection.websockets, "connect", fake_connect
        )
        patch_listener = mock.patch.object(Connection, "_listener", fake_listener)
        with patch_connect, patch_listener:
            await asyncio.gather(*(conn.aopen() for _ in range(5)))
            await asyncio.sleep(0)

        self.assertEqual(len(sockets), 1)
        self.assertEqual(listeners, [conn.socket])


if __name__ == "__main__":
    unittest.main()
