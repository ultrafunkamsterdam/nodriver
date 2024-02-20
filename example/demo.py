# coding: utf-8


import asyncio
import logging.handlers
import random

import nodriver as uc

logging.basicConfig(level=10)


async def main():
    driver = await uc.start()

    URL1 = "https://www.bet365.com"
    URL2 = "https://www.nowsecure.nl"

    await driver.get(URL2)

    for _ in range(10):
        if _ % 2 == 0:
            await driver.get(URL1, new_window=True)
        else:
            await driver.get(URL2, new_window=True)

    await driver

    grid = await driver.tile_windows(5)

    for _ in range(15):
        randbox = lambda: random.choice(grid)
        for i, tab in enumerate(driver.tabs):
            await tab.activate()
            await tab.set_window_size(*randbox())
    await driver

    for i, tab in enumerate(driver):
        if i >= len(grid):
            i = len(grid) - i
        await tab.set_window_size(*grid[i])
        await tab.sleep()

    b365pages = [tab for tab in driver.tabs if "bet365" in tab.url]

    await driver.tile_windows(12)

    await asyncio.gather(*[flash_spans(tab, i) for (i, tab) in enumerate(b365pages)])

    await asyncio.gather(*[scroll_task(tab) for tab in b365pages])

    for i, tab in enumerate(driver):
        try:
            await tab.get("https://www.google.com")
            await tab.activate()
            # skip first tab
            if tab == driver.main_tab:
                print("skipping main tab")
                continue
        except:
            pass
        await tab.close()

    for i, tab in enumerate(driver):
        try:
            if i == 0:
                continue
            # await driver.tile_windows(i)
            await tab.activate()
            # skip first tab
            await tab.close()

        except:
            pass

    driver.stop()


async def scroll_task(tab):
    await tab.scroll_up(200)
    spans = await tab.select_all("span")
    [await s.scroll_into_view() or await s.flash(duration=1) for s in reversed(spans)]
    [
        (await tab.scroll_up(n // 2) or await tab.scroll_down(n))
        or print("tab %s scrolling down : %d" % (tab, n))
        for n in range(0, 75, 15)
    ]


async def flash_spans(tab, i):
    logger.info("flashing spans. i=%d , tab=%s, url=%s" % (i, tab, tab.url))
    # await tab.fullscreen()
    elems = await tab.select_all("span")
    # await tab.medimize()
    await tab.activate()
    for elem in elems:
        await elem.flash(duration=0.25)
        await elem.scroll_into_view()


if __name__ == "__main__":
    import logging

    logger = logging.getLogger("demo")

    uc.loop().run_until_complete(main())
