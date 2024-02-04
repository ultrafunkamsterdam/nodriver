from nodriver import *

# interesting, this is a typical site which runs completely on javascript, and that causes
# this script to be faster than the js can present the elements, so we have to build in quite some
# sleep/pauses

async def main():


    browser = await start()
    page = await browser.get('https://imgur.com')

    print('waiting for')
    x = await page.wait_for(selector='body', timeout_ms=1000)
    print('done waiting for', x )
    # accept goddamn cookies
    # they have too many text having words like 'consent' so find by text takes
    # very long

    # so i'm getting the buttons and read their text.

    buttons = await page.query_selector_all('button')

    await page.wait_for('button[text')
    for button in buttons:
        print(button.text)
        # 100s of other buttons
        # help_outline
        # Accept all
        # Confirm choices
        # Close
    print('''so the second to last looks "the one" ''')
    await page.wait_for
    await buttons[-2].click()

    page.add_handler(cdp.dom, lambda e: print(e ))
    # shortcut
    await (await page.find_element_by_text('new post')).click()
    await page.listener.busy.wait()

    file_input = await page.query_selector('input[type=file]')

    while not file_input:
        await page.sleep(1)
        file_input = await page.query_selector('input[type=file]')


    await file_input.send_file(
        'c://users/leon/Downloads/(m=eafTGgaaaa)(mh=_hxkIK3ynk-Y5sXw)16 (1).jpg',
        'c://users/leon/downloads/(m=eafTGgaaaa)(mh=kNSEJA02jkztvUH9)2.jpg'
    )
    # since file upload takes a while , the next buttons are not available yet
    await page.sleep(3)


    title_field = await page.find_element_by_text('unique title')
    await title_field.send_keys('unique title')
    await page.sleep(1)


    grab_link = await page.find_element_by_text('grab link')
    await grab_link.click()

    # now they have the annoying input-like field where your link is
    # i could not find inputs and other obvious element types so i did it differently,
    # by taking a nearby element and walking up some parents
    here_is_your_link = await page.find_element_by_text("here's your link")

    # walk 2 parent up the tree, and perform a query_selector there.
    input_thing = await here_is_your_link.parent.parent.query_selector('input')
    my_link = input_thing.attrs.value

    print(my_link)




if __name__ == '__main__':
    loop = create_loop()
    loop.run_until_complete(main())