try:
    from nodriver import *
except (ModuleNotFoundError, ImportError):
    import os
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from nodriver import *


async def main():
    browser = await start()
    await demo_drag_to_target(browser)
    await demo_drag_to_target_in_steps(browser)
    await demo_drag_to_absolute_position(browser)
    await demo_drag_to_absolute_position_in_steps(browser)
    await demo_drag_to_relative_position(browser)
    await demo_drag_to_relative_position_in_steps(browser)


async def demo_drag_to_target(browser):
    tab = await browser.get("https://nowsecure.nl/mouse.html?boxes=50")
    boxes = await tab.select_all(".box")
    area = await tab.select(".area-a")
    for box in boxes:
        await box.mouse_drag(area)


async def demo_drag_to_target_in_steps(browser):

    tab = await browser.get("https://nowsecure.nl/mouse.html")
    boxes = await tab.select_all(".box")
    area = await tab.select(".area-a")

    for box in boxes:
        await box.mouse_drag(area, steps=100)


async def demo_drag_to_absolute_position(browser):
    tab = await browser.get("https://nowsecure.nl/mouse.html?boxes=50")
    boxes = await tab.select_all(".box")
    area = await tab.select(".area-a")

    for box in boxes:
        await box.mouse_drag((500, 500))


async def demo_drag_to_absolute_position_in_steps(browser):
    tab = await browser.get("https://nowsecure.nl/mouse.html")
    boxes = await tab.select_all(".box")
    area = await tab.select(".area-a")

    for box in boxes:
        await box.mouse_drag((500, 500), steps=50)


async def demo_drag_to_relative_position(browser):
    tab = await browser.get("https://nowsecure.nl/mouse.html?boxes=50")
    boxes = await tab.select_all(".box")

    for box in boxes:
        await box.mouse_drag((500, 500), relative=True)


async def demo_drag_to_relative_position_in_steps(browser):
    tab = await browser.get("https://nowsecure.nl/mouse.html")
    boxes = await tab.select_all(".box")

    for box in boxes:
        await box.mouse_drag((500, 500), relative=True, steps=50)


if __name__ == "__main__":
    loop().run_until_complete(main())
