# coding: utf-8


import asyncio
import logging
import logging.handlers
import random

import mss

logger = logging.getLogger("demo")
logging.basicConfig(level=10)


try:
    import nodriver as uc
except (ModuleNotFoundError, ImportError):
    import os
    import sys

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    import nodriver as uc

import time

_monitor = mss.mss().monitors[0]
SCREEN_WIDTH = _monitor["width"]
NUM_WINS = SCREEN_WIDTH // 325  # as to not fill up the screen to much


class Timing:

    def __init__(self):
        self.start = None
        self.stop = None
        self.taken = None

    def __enter__(self):
        self.start = time.monotonic()
        return self

    def __exit__(self, *args, **kwargs):
        self.stop = time.monotonic()
        self.taken = self.stop - self.start
        print("taken:", self.taken, "seconds")


async def main():

    driver = await uc.start()

    URL1 = "https://www.bet365.com"
    URL2 = "https://www.nowsecure.nl"

    print(
        "the startup speed of the windows depend on the line speed and availability/load on the servers"
    )
    await driver.get(URL2)

    for _ in range(NUM_WINS):
        if _ % 2 == 0:
            await driver.get(URL1, new_window=True)
        else:
            await driver.get(URL2, new_window=True)

    await driver

    grid = await driver.tile_windows(max_columns=NUM_WINS)
    await driver.sleep(5)
    for tab in driver.tabs:
        await tab.maximize()

    for _ in range(15):
        randbox = lambda: random.choice(grid)
        for i, tab in enumerate(driver.tabs):
            await tab.activate()
            await tab.set_window_size(*randbox())
    await driver

    for i, tab in enumerate(driver):
        tab: tab.Tab
        if i >= len(grid):
            i = len(grid) - i
        await tab.set_window_size(*grid[i])
        await tab

    await asyncio.gather(
        *[move_circle(tab, i % 2) for (i, tab) in enumerate(driver.tabs)]
    )

    nowsecure_pages = [tab for tab in driver.tabs if "nowsecure" in tab.url]

    await asyncio.gather(
        *[tab.get("https://nowsecure.nl/mouse.html") for tab in nowsecure_pages]
    )
    await driver.tile_windows(max_columns=NUM_WINS)
    await asyncio.gather(*[mouse_move(tab) for tab in nowsecure_pages])

    b365pages = [tab for tab in driver.tabs if "bet365" in tab.url]
    # await driver.tile_windows()
    await driver.sleep(1)

    positions = await driver.tile_windows(b365pages)
    # await asyncio.gather(*[tab.set_window_size(*pos) for (tab, pos) in zip(b365pages, positions)])
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
    [
        await s.scroll_into_view()
        # since scroll_into_view does not return a value
        # we can abuse 'or' to run 2 functions in a list comprehension
        or await s.flash()
        for s in reversed(spans)
    ]
    [
        (await tab.scroll_up(n // 2) or await tab.scroll_down(n))
        # since the above does not return a value
        # we can abuse 'or' to run even more while doing a list comprehension
        or print("tab %s scrolling down : %d" % (tab, n))
        for n in range(0, 75, 15)
    ]


async def mouse_move(tab):
    await tab.activate()
    boxes = await tab.select_all(".box")
    for box in boxes:
        await box.mouse_move()

    for box in boxes:
        await box.mouse_drag([250, 250],relative=True)


async def move_circle(tab, x=0):

    window_id, bounds = await tab.get_window()

    old_left, old_top = bounds.left, bounds.top
    old_width, old_height = bounds.width, bounds.height

    center = int(old_left), int(old_top)

    for coord in uc.util.circle(*center, radius=100, num=1050, dir=x):
        new_left, new_top = int(coord[0]), int(coord[1])
        await tab.set_window_size(new_left, new_top)

    for coord in uc.util.circle(*center, radius=250, num=500, dir=x):
        new_left, new_top = int(coord[0] / 2), int(coord[1] / 2)
        # await tab.set_window_size(old_left, old_top)
        await tab.set_window_size(new_left, new_top)

    await tab.set_window_size(old_left, old_top, old_width, old_height)


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
    with Timing() as t:
        uc.loop().run_until_complete(main())
