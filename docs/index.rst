

========================
NODRIVER
========================


Features
-------------

.. hlist::
    :columns: 3

    * A blazing fast undetected chrome (-ish) automation tool (without the use of an webdriver binary)
    * No chromedriver binary or Selenium dependency
    * this equals bizarre performance increase and less detections!

.. important::

    those who landed here who never used undetected-chromedriver (or whatever webdriver)
    might be confused by the use of "driver" all around here while there is no driver.

    Don't worry. The term driver can be replaced with "browser", but since most users
    are accustomed to "driver" and the abbreviation "uc" for undetected-chromedriver, it's convenient to
    keep using it, although to prevent confusion, i'll use nd as abbr for nodriver.



Welcome
-----------------------------------

**this package provides next level webscraping and browser automation
using a relatively simple interface.**


This is the official follow up on the `Undetected-Chromedriver <https://github.com/ultrafunkamsterdam/undetected-chromedriver />`_ python package.

It stepped away from selenium/webdriver, which have had their best
time by now in terms of webscraping and browser automation.
Direct communication provides even better resistance against web applicatinon firewalls (WAF's), while
performance gets a massive boost.
This module is, contrary to undetected-chromedriver, fully asynchronous.

What makes this package different from other known packages,
is the optimization to stay undetected for most anti-bot solutions.

another focus point is usability and quick prototyping, so expect batteries included.
Using 1 or 2 lines, this is up and running, providing best practice config
by default.


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





