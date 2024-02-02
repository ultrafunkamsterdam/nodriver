


Installation
=============
Since it's a part of undetected-chromedriver, installation goes via

.. code-block::

    pip install undetected-chromedriver

--------


.. _getting-started-commands:

usage example
===============

The aim of this project (just like undetected-chromedriver, somewhere long ago)
is to keep it short and simple, so you can quickly open an editor or interactive session,
type or paste a few lines and off you go.

.. code-block:: python

    import asyncio
    import nodriver as uc

    async def main():
        browser = await uc.start()
        page = await browser.get('https://www.nowsecure.nl')

        await page.save_screenshot()
        await page.get_content()
        await page.scroll_down(150)
        elems = await page.query_selector_all('*[src]')
        for elem in elems:
            await elem.highlight_position()

        page2 = await browser.get('https://twitter.com', new_tab=True)
        page3 = await browser.get('https://pornhub.com', new_window=True)

        for p in (page, page2, page3):
           await p.bring_to_front()
           await p.scroll_down(200)
           await p.sleep(1)
           await p.reload()
           if p != page3:
               await p.close()


    if __name__ == '__main__':

        # since asyncio.run never worked (for me)
        uc.loop().run_until_complete(main())





Components and interaction
============================

There are a couple of layers. But the package
will keep it as easy as possible (compared to plain cdp)


Browser
---------------------------------
:ref:`browser` object holds your entire session and should be
seen as "root"


Page
---------------------------------
:ref:`page` is the connection to each 'target',
for most of us this would read 'tab' but could also be
an iframe for example.

the page object will stay the same for each tab and window and
will not close when you navigate to another url.
So it's important to keep some reference to page, in case you're
done interacting with elements and want to operate on the page level again.


Element
---------------------------------
:ref:`element`\s are (html) elements (nodes) on a page.
like page object, you can interact with elements.
since element does have a reference to page,
you can interact with elements directly. They offer
different set of methods compared :ref:`page`.







