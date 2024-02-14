

##################
NODRIVER
##################


**This package provides next level webscraping and browser automation
using a relatively simple interface.**

* **This is the official successor of the** `Undetected-Chromedriver <https://github.com/ultrafunkamsterdam/undetected-chromedriver/>`_ **python package.**
* **No more webdriver, no more selenium**

Direct communication provides even better resistance against web applicatinon firewalls (WAF's), while
performance gets a massive boost.
This module is, contrary to undetected-chromedriver, fully asynchronous.

What makes this package different from other known packages,
is the optimization to stay undetected for most anti-bot solutions.

Another focus point is usability and quick prototyping, so expect a lot to work `-as is-` ,
with most method parameters having `best practice` defaults.
Using 1 or 2 lines, this is up and running, providing best practice config
by default.

While usability and convenience is important. It's also easy
to fully customizable everything using the entire array of
`CDP <https://chromedevtools.github.io/devtools-protocol />`_ domains, methods and events available.


Some features
^^^^^^^^^^^^^^^^^^^^^^

* A blazing fast undetected chrome (-ish) automation library

* No chromedriver binary or Selenium dependency

* This equals bizarre performance increase and less detections!

* Up and running in 1 line of code*

* uses fresh profile on each run, cleans up on exit

* save and load cookies to file to not repeat tedious login steps

* fast element lookup, by selector or text. also searches embedded iframes.

* descriptive __repr__ for elements, which represent the element as html

* packed with helpers and utility methods for most used and important operations

..
   * ```elem.text```
   * ```elem.text_all```

   * ```elem.parent.parent.parent.attrs```
   * ```anchor_elem.href and anchor_elem['href']```
   * ```anchor_elem.href = 'someotherthing'; await anchor_elem.save()```
   * ```elem.children[-1].children[0].children[4]```

   * ```await html5video_element.record_video()```
   * ```await html5video_element('method')```
   * ```await html5video_element.apply('''(el) => el.currentTime = 0''')```
   * ```tab = await browser.get(url, new_tab=True)```
   * ```tab_win = await browser.get(url, new_window=True)```
   * ```first = await tab.find('search text')```
   * ```all_results = await tab.find_all('search text')```
   * ```first_submit_button = await tab.find(selector='button[type=submit]')```
   * ```inputs_in_form = await tab.find_all('form input')```



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




.. toctree::
    :caption: getting started
    :titlesonly:

    nodriver/quickstart


.. toctree::
    :caption: nodriver object reference
    :titlesonly:
    :glob:

    nodriver/classes/*


.. toctree::
    :caption: nodriver cdp reference
    :glob:
    :maxdepth: 1

    nodriver/cdp/*





