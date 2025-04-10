import asyncio

try:
    from nodriver import *
except (ModuleNotFoundError, ImportError):
    import os
    import sys

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from nodriver import *


async def response_received_handler(ev: cdp.network.ResponseReceived, tab=None):
    try:
        body, base64encoded = await tab.send(cdp.network.get_response_body(
            ev.request_id))
        if base64encoded:
            import base64
            body = base64.b64decode(body)
        print(ev.response.url, '\n', 'body[:100]:', '\n', body[:100])
    except TypeError:
        pass
    except ProtocolException:
        return



async def main():
    global browser
    browser = await start()
    browser[0].add_handler(cdp.network.ResponseReceived, handler=response_received_handler)
    while True:
        tab = await browser[0].get('https://google.com')
        await asyncio.sleep(5)



if __name__ == '__main__':

    loop().run_until_complete(main())
