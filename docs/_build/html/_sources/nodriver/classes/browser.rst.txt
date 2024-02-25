.. _browser:

Browser class
---------------------

cookies
^^^^^^^^^^^^^^^^^^^^^^^

You can load and save all cookies from the browser.


.. code-block::

    # save. when no filepath is given, it is saved in '.session.dat'
    await browser.cookies.save()


.. code-block::

    # load. when no filepath is given, it is loaded from '.session.dat'
    await browser.cookies.load()


.. code-block::

    # export for requests or other library
    requests_style_cookies = await browser.cookies.get_all(requests_cookie_format=True)

    # use in requests:
    session = requests.Session()
    for cookie in requests_style_cookies:
        session.cookies.set_cookie(cookie)


Browser class
^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass::  nodriver.Browser
    :members:
    :undoc-members:
    :inherited-members:


