from nodriver import *

# interesting, this is a typical site which runs completely on javascript, and that causes
# this script to be faster than the js can present the elements, so we have to build in quite some
# sleep/pauses


async def main():
    browser = await start()

    tab = await browser.get("https://imgur.com")
    x = await tab.wait_for(selector="body")

    # accept goddamn cookies
    # they have too many text having words like 'consent' so find by text takes
    # very long, so alternatively, fetch all buttons, and match text.

    buttons = await tab.query_selector_all("button")

    # # ensure it's done
    # await tab.wait_for(selector='button')

    # the second last button is our target
    await buttons[-2].click()

    # shortcut
    await (await tab(text="new post")).click()

    # await tab.listener.busy.wait()

    file_input = await tab(selector="input[type=file]")

    # while not file_input:
    #     await tab.sleep(1)
    #     file_input = await tab.query_selector('input[type=file]')

    await file_input.send_file(
        "c://users/leon/Downloads/(m=eafTGgaaaa)(mh=_hxkIK3ynk-Y5sXw)16 (1).jpg",
        "c://users/leon/downloads/(m=eafTGgaaaa)(mh=kNSEJA02jkztvUH9)2.jpg",
    )
    # since file upload takes a while , the next buttons are not available yet
    await tab.sleep(3)

    title_field = await tab(text="unique title")
    await title_field.send_keys("undetected nodriver")

    await tab.sleep(1)

    grab_link = await tab(text="grab link")
    await grab_link.click()

    # now they have the annoying input-like field where your link is
    # i could not find inputs and other obvious element types so i did it differently,
    # by taking a nearby element and walking up some parents
    here_is_your_link = await tab.find_element_by_text("here's your link")

    # walk 2 parent up the tree, and perform a query_selector there.
    input_thing = await here_is_your_link.parent.parent.query_selector("input")
    my_link = input_thing.attrs.value

    print(my_link)
    await tab.sleep(5)


if __name__ == "__main__":
    loop = loop()
    loop.run_until_complete(main())
