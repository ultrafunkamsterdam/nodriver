import asyncio
from pathlib import Path
from nodriver import *
from undetected_nodriver.core.util import filename_from_url


dl_path = Path('c:\\temp\\downloads3')

async def main():

    urls = set()
    async def on_request_sent_handler(event: cdp.network.RequestWillBeSent):
        the_url = event.request.url
        print('adding', the_url)
        urls.add(the_url)

    browser = await start()
    browser.active_page.add_handler(cdp.network.RequestWillBeSent, on_request_sent_handler)
    await browser.active_page.set_download_path(dl_path)

    page = await browser.get(url)

    for _ in range(5):
        await page.scroll_down(100)
    for _ in range(5):
        await page.scroll_up(100)

    page.remove_handler()

    await page.sleep(0)
    print('got ', len(urls), 'urls!')
    for u in urls:
        fn = filename_from_url(u)
        print('downloading ', u)
        try:
            await page.download_file(u, fn)
            print('got ', fn)
        except:
            print('error getting ', u )

        finally:
            await page.sleep(.5)






if __name__ == '__main__':

    url = "https://trustpilot.com/review/lostempireherbs.com"
    asyncio.run(main())