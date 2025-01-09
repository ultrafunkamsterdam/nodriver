try:
    from nodriver import cdp, loop, start
except (ModuleNotFoundError, ImportError):
    import os
    import sys

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from nodriver import cdp, loop, start


async def main():
    browser = await start()

    tab = browser.main_tab
    tab.add_handler(cdp.network.RequestWillBeSent, send_handler)
    tab.add_handler(cdp.network.ResponseReceived, receive_handler)

    tab = await browser.get("https://www.google.com/?hl=en")

    reject_btn = await tab.find("reject all", best_match=True)
    await reject_btn.click()

    search_inp = await tab.select("textarea")
    await search_inp.send_keys("undetected nodriver")

    search_btn = await tab.find("google search", True)
    await search_btn.click()

    for _ in range(10):
        await tab.scroll_down(50)

    await tab
    await tab.back()

    search_inp = await tab.select("textarea")

    for letter in "undetected nodriver":
        await search_inp.clear_input()
        await search_inp.send_keys(
            "undetected nodriver".replace(letter, letter.upper())
        )
        await tab.wait(0.1)

    all_urls = await tab.get_all_urls()
    for u in all_urls:
        print("downloading %s" % u)
        await tab.download_file(u)

    await tab.sleep(10)


async def receive_handler(event: cdp.network.ResponseReceived):
    print(event.response)


async def send_handler(event: cdp.network.RequestWillBeSent):
    r = event.request
    s = f"{r.method} {r.url}"
    for k, v in r.headers.items():
        s += f"\n\t{k} : {v}"
    print(s)


if __name__ == "__main__":
    loop().run_until_complete(main())
