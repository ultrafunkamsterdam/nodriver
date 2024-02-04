# Twitter create account
# demo for undetected_nodriver
# ultrafunkamsterdam


import asyncio
import random
import string
import logging

logging.basicConfig(level=20)
# logging.getLogger("websockets").setLevel(20)


import nodriver as uc

months = [
    "january", "february", "march", "april", "may", "june", "july", "august", "september",
    "october", "november", "december"
]


async def main():
    driver = await uc.start()
    page = await driver.get("https://twitter.com")
    t = uc.loop().create_task(asyncio.sleep(2))

    print('t = ', t, 'loop = ', t.get_loop(), '/', uc.loop())
    # wait for text to appear instead of a static number of seconds to wait
    # this does not always work as expected, due to speed.
    create_account = await page.wait_for_text_content_to_appear(
        "create account", timeout=10
    )
    await create_account.click()

    # get the email input field
    email = await page.wait_for_element_to_appear("input[type=email]")

    # sometimes, email field is not shown, because phone is being asked instead
    # when this occurs, find the small text which says "use email instead"
    if not email:
        use_mail_instead = await page.find_element_by_text_content("use email")

        # and click it
        await use_mail_instead.click()

        # now find the email field again
        email = await page.wait_for_element_to_appear("input[type=email]")

    randstr = lambda k: "".join(random.choices(string.ascii_letters, k=k))

    # send keys to email field
    await email.send_keys("".join([randstr(8), "@", randstr(8), ".com"]))

    # find the name input field
    name = await page.query_selector("input[type=text]")

    # again, send random text
    await name.send_keys(randstr(8))

    # since there are 3 select fields on the page, we can use unpacking
    # to assign each field
    sel_month, sel_day, sel_year = await page.query_selector_all("select")

    await sel_month.focus()
    await sel_month.send_keys(months[random.randint(0, 11)].title())

    await sel_day.focus()
    # i don't want to bother with month-lengths and leap years
    await sel_day.send_keys(str(random.randint(0, 28)))

    await sel_year.focus()
    # i don't want to bother with age restrictions
    await sel_year.send_keys(str(random.randint(1980, 2005)))

    await page.wait()

    # let's handle the cookie nag as well
    cookie_bar_accept = await page.find_element_by_text_content("accept all")
    if cookie_bar_accept:
        await cookie_bar_accept.click()

    await page.wait()

    next_btn = await page.wait_for_text_content_to_appear("next")
    await next_btn.click()
    print("next")

    next_btn = await page.wait_for_text_content_to_appear("next")
    await next_btn.click()
    print("next")


    await page.wait_for_element_to_appear("[role=button]")
    await page.sleep(1)

    sign_up_btns = await page.find_elements_by_text_content(
        "Sign up"
    )
    # all_buttons = await page.find_elements_by_css_selector('button')
    sign_up_btn = sign_up_btns[1]
    await sign_up_btn.click()

    print('awiting 10 seconds')
    # further implementation outside of scope
    await page.sleep(10)
    driver.quit()

    # verification code per mail


if __name__ == "__main__":

    # since asyncio.run never worked (for me)
    # i use
    uc.loop().run_until_complete(main())
