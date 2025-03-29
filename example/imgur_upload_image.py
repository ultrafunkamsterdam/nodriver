try:
    from nodriver import *
except (ModuleNotFoundError, ImportError):
    import os
    import sys

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from nodriver import *

from pathlib import Path

# interesting, this is a typical site which runs completely on javascript, and that causes
# this script to be faster than the js can present the elements. This may be one of the downsides
# of this fast beast. You have to carefully consider timing.

DELAY = 2


try:
    from nodriver import *
except (ModuleNotFoundError, ImportError):
    import os
    import sys

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from nodriver import *


async def main():

    browser = await start()
    tab = await browser.get("https://imgur.com")

    # now we first need an image to upload, lets make a screenshot of the project page
    save_path = Path("screenshot.jpg").resolve()
    # create new tab with the project page
    temp_tab = await browser.get(
        "https://github.com/ultrafunkamsterdam/undetected-chromedriver", new_tab=True
    )

    # wait page to load
    await temp_tab
    # save the screenshot to the previously declared path of screenshot.jpg (which is just current directory)
    await temp_tab.save_screenshot(save_path)
    # done, discard the temp_tab
    await temp_tab.close()

    # accept goddamn cookies
    # the best_match flag will filter the best match from
    # matching elements containing "consent" and takes the
    # one having most similar text length
    consent = await tab.find("Consent", best_match=True)
    await consent.click()

    # shortcut
    await (await tab.find("new post", best_match=True)).click()

    file_input = await tab.select("input[type=file]")
    await file_input.send_file(save_path)
    # since file upload takes a while , the next buttons are not available yet

    await tab.wait(DELAY)

    # wait until the grab link becomes clickable, by waiting for the toast message
    await tab.select(".Toast-message--check")

    # this one is tricky. we are trying to find a element by text content
    # usually. the text node itself is not needed, but it's enclosing element.
    # in this case however, the text is NOT a text node, but an "placeholder" attribute of a span element.
    # so for this one, we use the flag return_enclosing_element and set it to False
    title_field = await tab.find("give your post a unique title", best_match=True)
    print(title_field)
    await title_field.send_keys("undetected nodriver")

    grab_link = await tab.find("grab a link", best_match=True)
    await grab_link.click()

    # there is a delay for the link sharing popup.
    # let's pause for a sec
    await tab.wait(DELAY)

    # get inputs of which the value starts with http
    input_thing = await tab.select("input[value^=https]")

    my_link = input_thing.attrs.value

    print(my_link)
    await tab


if __name__ == "__main__":
    loop = loop()
    loop.run_until_complete(main())
