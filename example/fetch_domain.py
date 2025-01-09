try:
    from nodriver import *
except (ModuleNotFoundError, ImportError):
    import os
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from nodriver import *

import logging

logging.basicConfig(level=logging.INFO)


async def request_handler(ev: cdp.fetch.RequestPaused, tab: Tab):
    print('\nRequestPaused handler\n', ev, type(ev))
    print('TAB = ', tab)
    tab.feed_cdp(cdp.fetch.continue_request(request_id=ev.request_id))


async def main():

    browser = await start()

    [await browser.get(
        'https://www.google.com',
        new_window=True)
     for _ in range(10)]

    for tab in browser:
        print(tab)
        tab.add_handler(cdp.fetch.RequestPaused, request_handler)
        await tab.send(cdp.fetch.enable())

    for tab in browser:
        await tab

    for tab in browser:
        await tab.activate()

    for tab in reversed(browser):
        await tab.activate()
        await tab.close()

    browser.stop()


browser = loop().run_until_complete(main())
