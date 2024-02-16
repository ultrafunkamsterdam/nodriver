# coding: utf-8


import asyncio
import logging.handlers
import random

import nodriver as uc

logging.basicConfig(level=20)


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
    print('grid')
    print(grid)
    for _ in range(15):
        randbox = lambda: random.choice(grid)
        for i, tab in enumerate(driver.tabs):
            await tab.activate()
            await tab.set_window_size(*randbox())

    await driver


    for i, tab in enumerate(driver):
        await tab.set_window_size(*grid[i])
        await tab.sleep()

    b365pages = [tab for tab in driver.tabs if "bet365" in tab.url]

    for tab in driver:
        if tab not in b365pages:
            await tab.minimize()
        else:
            await tab.medimize()

    await driver.tile_windows(max_columns=12)

    [await tab.sleep() for tab in driver]


    await asyncio.gather(*[flash_spans(tab, i) for (i, tab) in enumerate(b365pages[:4])])

    await driver.tile_windows(max_columns=12)

    await asyncio.gather(*[scroll_task(tab) for tab in driver.tabs])

    for i, tab in enumerate(driver):
        await tab.get('https://www.google.com')
        await tab.activate()
        await driver.tile_windows(i * 2)
        # skip first tab
        if tab == driver.main_tab:
            print('skipping main tab')
            continue
        await tab.close()


    await driver.sleep(2)


    for i, tab in enumerate(driver):
        await driver.tile_windows(i)
        await tab.activate()
        # skip first tab
        if tab == driver.main_tab:
            continue
        await tab.close()
        await driver.sleep(.1)

    driver.stop()


async def scroll_task(tab):
    [await tab.scroll_down(n) or print("tab %s scrolling down : %d" % (tab, n)) for n in range(0, 200, 10)]


async def flash_spans(tab, i):
    logger.info("flashing spans. i=%d , tab=%s, url=%s" % (i, tab, tab.url))
    await tab.fullscreen()

    elems = await tab.query_selector_all("span")
    await tab.medimize()
    await tab.activate()
    for elem in elems:
        await elem.flash(duration=0.25)
        await elem.scroll_into_view()


if __name__ == "__main__":
    import logging

    logger = logging.getLogger("demo")

    uc.loop().run_until_complete(main())

