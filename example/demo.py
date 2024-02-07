# coding: utf-8
# coding: utf-8

import asyncio

import time
import logging
import logging.handlers


logging.basicConfig(level=20)

# logger = logging.getLogger()


import random





async def main():

    # asyncio.create_task(perf_watcher())
    driver = await uc.start()

    URL1 = "https://www.bet365.com"
    URL2 = "https://www.nowsecure.nl"

    for _ in range(10):
        if _ % 2 == 0:
            await driver.get(URL1, new_window=True)
        else:
            await driver.get(URL2, new_window=True)
    await driver.wait(2)
    # for p in driver.pages:
    #     await p.wait(.5)


    grid = await driver.tile_windows(8)

    # for _ in grid:
    #     # print(_)
    #     # _[0] = 1024
    #     # _[1] = 768
    #     print(_)

    randbox = lambda: random.choice(grid)
    for _ in range(15):
        for i, tab in enumerate(driver.tabs):
            await tab.activate()
            # if _ // 4 == i:
            #     await tab.get(URL2)
            #     await tab.wait(5)
            await tab.set_window_size(*randbox())
            await tab.sleep(random.uniform(.005, .03))
            # await tab.sleep(1 / (_ + 10))
    await driver

    for i, tab in enumerate(driver.tabs):
        await tab.set_window_size(*grid[i])
        await tab

    async def flash_spans(tab, i):
        logger.info('flashing spans. i=%d , tab=%s, url=%s' % (i, tab, tab.url))

        await tab.set_window_size(height=1280, top=0, left=i * 640, width=1024)
        await tab.fullscreen()
        # await tab.minimize()
        # await tab.medimize()

        await tab.activate()
        elems = await tab.query_selector_all("span")

        await tab.medimize()
        for elem in elems:
            await elem.flash(duration=3)
            await elem.scroll_into_view()


    b365pages = [tab for tab in driver.tabs if "bet365" in tab.url]

    await driver.tile_windows(max_columns=15)

    [await tab for tab in driver]
    await asyncio.gather(
        *[flash_spans(tab, i) for (i, tab) in enumerate(b365pages[:4])]
    )

    async def scroll_task(tab):
        await tab.scroll_down(100)
        await tab.scroll_up(100)
        
    await driver.tile_windows(max_columns=8)
    await asyncio.gather(*[scroll_task(tab) for tab in driver.tabs])
    await driver

    driver.stop()


import threading
from collections import Counter


async def perf_watcher():

    start_time = time.perf_counter()

    def sort_coros(tasks):
        _coros = [t.get_coro() for t in tasks]
        _coros_list = [c.cr_code.co_qualname for c in _coros]
        counter = Counter(_coros_list)
        for _ in counter.most_common(10):
            logger.warning(f'{_}')
        return _coros

    while True:
        all_tasks = asyncio.all_tasks()
        len_all = len(all_tasks)
        len_done = len([t for t in all_tasks if t.done()])
        logger.debug(f'[ {time.perf_counter() - start_time} ]   coroutines: {len(all_tasks)} (of which: {len_done} done) / (threads: {threading.active_count()}')
        sort_coros(all_tasks)
        await asyncio.sleep(1)


if __name__ == "__main__":
    import logging

    logger = logging.getLogger('demo')
    import nodriver as uc
    uc.loop().run_until_complete(main())

    #
    # print('starting up undetectd_nodriver')
    #
    # handler = logging.FileHandler('log_0.txt', encoding='utf8')
    # handler.setLevel(10)
    #
    # logger = logging.getLogger('root')
    # logger.addHandler(handler)
    # logger.setLevel(10)
    #
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    #
    # import nodriver as uc
    #
    # tasks = asyncio.gather(main())
    # try:
    #     loop.run_until_complete(tasks)
    # except:
    #     tasks.cancel()
    #     loop.run_until_complete(asyncio.sleep(1))
    #     raise
    # print('done!')
    #
    #
    #
    # logger.removeHandler(handler)
    #
    # print('starting up undetectd_nodriver1')
    # handler = logging.FileHandler('log_1.txt', encoding='utf8')
    # handler.setLevel(10)
    # logger.addHandler(handler)
    #
    # import nodriver as uc
    #
    # tasks = asyncio.gather(main())
    #
    # try:
    #     loop.run_until_complete(tasks)
    #
    # except:
    #     tasks.cancel()
    #     loop.run_until_complete(asyncio.sleep(1))
    #




    exit()