
Quickstart guide
=================


Installation
--------------
Since it's a part of undetected-chromedriver, installation goes via

.. code-block::

    # todo. use pip install nodriver instead
    pip install undetected-chromedriver

--------

Or as a seperate package via:

.. code-block::

    pip install nodriver


.. _getting-started-commands:

usage example
===============

The aim of this project (just like undetected-chromedriver, somewhere long ago)
is to keep it short and simple, so you can quickly open an editor or interactive session,
type or paste a few lines and off you go.

.. code-block:: python


    import nodriver as uc

    async def main():
        browser = await uc.start()
        page = await browser.get('https://www.nowsecure.nl')

        await page.save_screenshot()
        await page.get_content()
        await page.scroll_down(150)
        elems = await page.select_all('*[src]')
        for elem in elems:
            await elem.flash()

        page2 = await browser.get('https://twitter.com', new_tab=True)
        page3 = await browser.get('https://github.com/ultrafunkamsterdam/nodriver', new_window=True)

        for p in (page, page2, page3):
           await p.bring_to_front()
           await p.scroll_down(200)
           await p   # wait for events to be processed
           await p.reload()
           if p != page3:
               await p.close()


    if __name__ == '__main__':

        # since asyncio.run never worked (for me)
        uc.loop().run_until_complete(main())



A more concrete example, which can be found in the ./example/ folder,
shows a script to create a twitter account

.. code-block:: python

    import asyncio
    import random
    import string
    import logging

    logging.basicConfig(level=30)

    import nodriver as uc

    months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]


    async def main():
        driver = await uc.start()

        tab = await driver.get("https://twitter.com")

        # wait for text to appear instead of a static number of seconds to wait
        # this does not always work as expected, due to speed.
        print('finding the "create account" button')
        create_account = await tab.find("create account", best_match=True)

        print('"create account" => click')
        await create_account.click()

        print("finding the email input field")
        email = await tab.select("input[type=email]")

        # sometimes, email field is not shown, because phone is being asked instead
        # when this occurs, find the small text which says "use email instead"
        if not email:
            use_mail_instead = await tab.find("use email instead")
            # and click it
            await use_mail_instead.click()

            # now find the email field again
            email = await tab.select("input[type=email]")

        randstr = lambda k: "".join(random.choices(string.ascii_letters, k=k))

        # send keys to email field
        print('filling in the "email" input field')
        await email.send_keys("".join([randstr(8), "@", randstr(8), ".com"]))

        # find the name input field
        print("finding the name input field")
        name = await tab.select("input[type=text]")

        # again, send random text
        print('filling in the "name" input field')
        await name.send_keys(randstr(8))

        # since there are 3 select fields on the tab, we can use unpacking
        # to assign each field
        print('finding the "month" , "day" and "year" fields in 1 go')
        sel_month, sel_day, sel_year = await tab.select_all("select")

        # await sel_month.focus()
        print('filling in the "month" input field')
        await sel_month.send_keys(months[random.randint(0, 11)].title())

        # await sel_day.focus()
        # i don't want to bother with month-lengths and leap years
        print('filling in the "day" input field')
        await sel_day.send_keys(str(random.randint(0, 28)))

        # await sel_year.focus()
        # i don't want to bother with age restrictions
        print('filling in the "year" input field')
        await sel_year.send_keys(str(random.randint(1980, 2005)))

        await tab

        # let's handle the cookie nag as well
        cookie_bar_accept = await tab.find("accept all", best_match=True)
        if cookie_bar_accept:
            await cookie_bar_accept.click()

        await tab.sleep(1)

        next_btn = await tab.find(text="next", best_match=True)
        # for btn in reversed(next_btns):
        await next_btn.mouse_click()

        print("sleeping 2 seconds")
        await tab.sleep(2)  # visually see what part we're actually in

        print('finding "next" button')
        next_btn = await tab.find(text="next", best_match=True)
        print('clicking "next" button')
        await next_btn.mouse_click()

        # just wait for some button, before we continue
        await tab.select("[role=button]")

        print('finding "sign up"  button')
        sign_up_btn = await tab.find("Sign up", best_match=True)
        # we need the second one
        print('clicking "sign up"  button')
        await sign_up_btn.click()

        print('the rest of the "implementation" is out of scope')
        # further implementation outside of scope
        await tab.sleep(10)
        driver.stop()

        # verification code per mail


    if __name__ == "__main__":
        # since asyncio.run never worked (for me)
        # i use
        uc.loop().run_until_complete(main())






