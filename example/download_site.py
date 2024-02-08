import asyncio

from nodriver import start, cdp, util
from pathlib import Path
import logging

# logging.basicConfig(level=10)
dl_path = Path("c:\\temp\\downloads3")
import urllib.parse


def get_filename(url):
    u = urllib.parse.urlparse(url)
    split2 = u.path.rsplit("/", 1)
    return split2[-1]


def filename_from_url(url: str):
    import urllib.parse

    p = urllib.parse.urlsplit(url)
    path_split = p.path.rsplit("/")
    if not path_split or len(path_split) <= 1:
        return
    last = path_split[-1]
    return last


async def main(url):
    #
    # events = {}
    #
    # async def on_request_will_be_Sent(event: cdp.network.RequestWillBeSent):
    #     events[event.request.url] = filename_from_url(event.request.url)
    #
    # def unset_on_request_will_be_Sent(event: cdp.network.RequestWillBeSent):
    #     page.off(cdp.network.RequestWillBeSent)
    #

    browser = await start()
    page = await browser.get(url)

    # page.on(cdp.network.RequestWillBeSent, on_request_will_be_Sent)

    # ctxids = await browser.connection.send(cdp.target.get_browser_contexts())
    # print('ctxids', ctxids)
    await page.set_download_path(dl_path)
    # await page.send(cdp.browser.set_download_behavior('allow', None, 'c:\\temp\\Downloads'))

    # await page.set_download_path('c:/temp/Downloads')
    # # pick the current page to bind our listener to
    # # this is an anomality, since we need to bind
    # # the event before the page is loaded
    # page = browser.pages[0]
    # await page.reload()
    # print('waiting')
    for _ in range(10):
        await page.scroll_down(100)
    for _ in range(10):
        await page.scroll_up()

    urls = await page._get_all_urls()
    events = {u: filename_from_url(u) for u in urls}
    # await page.wait()
    # page._handlers.clear()
    # print('done waiting')

    print("events:")
    for ev in events:
        print(ev)

    await page.download_file(page.url, "index.html")

    for ev in events:
        try:
            await page.download_alt(ev, events[ev])
            await page.sleep(0.5)
        except Exception as e:
            print(e)

    allfiles = list(dl_path.glob("*"))
    for ev in events:
        fn = Path(get_filename(ev))
        if fn not in allfiles:
            print("missing ", fn, "from", ev)
            fnfu = Path(filename_from_url(ev))
            if fnfu not in allfiles:
                print("also when using filename_from_url", fnfu)

    await page.sleep(60)


if __name__ == "__main__":
    asyncio.run(main("https://trustpilot.com/review/lostempireherbs.com"))
