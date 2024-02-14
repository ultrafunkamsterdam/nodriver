<a id="tab"></a>

### *class* Tab(websocket_url, target, browser=None, \*\*kwargs)

tab is the controlling mechanism/connection to a ‘target’,
for most of us ‘target’ can be read as ‘tab’. however it could also
be an iframe, serviceworker or background script for example,
although there isn’t much to control for those.

if you open a new window by using `browser.get(..., new_window=True)()`
your url will open a new window. this window is a ‘tab’.
When you browse to another page, the tab will be the same (it is an browser view).

So it’s important to keep some reference to tab objects, in case you’re
done interacting with elements and want to operate on the page level again.

Tab object provide many useful and often-used methods. It is also
possible to utilize the included cdp classes to to something totally custom.

the cdp package is a set of so-called “domains” with each having methods, events and types.
to send a cdp method, for example [`cdp.page.navigate`](../cdp/page.md#nodriver.cdp.page.navigate), you’ll have to check
whether the method accepts any parameters and whether they are required or not.

you can use

``python
await tab.send(cdp.page.navigate(url='https://yoururlhere'))
``

so tab.send() accepts a generator object, which is created by calling a cdp method.
this way you can build very detailed and customized commands.
(note: finding correct command combo’s can be a time consuming task, luckily i added a whole bunch
of useful methods, preferably having the same api’s or lookalikes, as in selenium)

# some useful, often needed and simply required methods

## [`query_selector_all()`](#nodriver.Tab.query_selector_all)

this is just like javascripts’ document.querySelectorAll, which you can use
to quickly select elements based a css selector.

tip: you can also use `await page('.your-css-selector')`

## [`find_element_by_text()`](#nodriver.Tab.find_element_by_text)

this is almost like query_selector all, but performs a text search and returns
any elements that matches. This is case insensitive.

tip: you can also use `await page(text='sign up')`

## await `Page`

calling `await page` will do a lot of stuff under the hood, and ensures all references
are up to date. also it allows for the script to “breathe”, as it is oftentime faster than your browser or
webpage. So whenever you get stuck and things crashes or element could not be found, you should probably let
it “breathe”  by calling `await page`  and/or `await page.sleep()`

also, it’s ensuring `url` will be updated to the most recent one, which is quite important in some
other methods.

## [`send()`](#nodriver.Tab.send)

this is probably THE most important method, although you won’t ever call it, unless you want to
go really custom. the send method accepts a `cdp` command. Each of which can be found in the
cdp section.

when you import \* from this package, cdp will be in your namespace, and contains all domains/actions/events
you can act upon.

#### *async* aclose()

#### *async* activate()

active this target (ie: tab,window,page)

#### add_handler(event_type_or_domain, handler)

add a handler for given event

if event_type_or_domain is a module instead of a type, it will find all available events and add
the handler.

if you want to receive event updates (network traffic are also ‘events’) you can add handlers for those events.
handlers can be regular callback functions or async coroutine functions (and also just lamba’s).
for example, you want to check the network traffic:

```default
page.add_handler(cdp.network.RequestWillBeSent, lambda event: print('network event => %s' % event.request))
```

the next time you make network traffic you will see your console print like crazy.

* **Parameters:**
  * **event_type_or_domain** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`type`](https://docs.python.org/3/library/functions.html#type), [`ModuleType`](https://docs.python.org/3/library/types.html#types.ModuleType)]) – 
  * **handler** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable), [`Awaitable`](https://docs.python.org/3/library/typing.html#typing.Awaitable)]) – 
* **Returns:**
* **Return type:**

#### *async* aopen(\*\*kw)

* **Parameters:**
  **kw** – 
* **Returns:**

#### attached*: bool* *= None*

#### *async* back()

history back

#### *async* bring_to_front()

alias to self.activate

#### browser*: [`Browser`](browser.md#nodriver.Browser)*

#### *async* close()

close the current target (ie: tab,window,page)
:return:
:rtype:

#### *async* download_file(url, filename=None)

downloads file by given url.

* **Parameters:**
  * **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – url of the file
  * **filename** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path), [`None`](https://docs.python.org/3/library/constants.html#None)]) – the name for the file. if not specified the name is composed from the url file name

#### *async* find(text='', selector='', timeout=5)

#### *async* find_all(text='', selector='', timeout=5)

#### *async* find_element_by_text(text, return_enclosing_element=True)

* **Parameters:**
  * **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **return_enclosing_element** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – 
* **Returns:**
* **Return type:**

#### *async* find_elements_by_text(text, tag_hint=None, return_enclosing_element=True)

* **Parameters:**
  * **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **return_enclosing_element** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if False, it returns the textual element,
    but usually one needs the element containing the text, like a button. default = True
* **Returns:**
* **Return type:**

#### *async* forward()

history forward

#### *async* fullscreen()

minimize page/tab/window

#### *async* get(url='chrome://welcome', new_tab=False, new_window=False)

top level get. utilizes the first tab to retrieve given url.

convenience function known from selenium.
this function handles waits/sleeps and detects when DOM events fired, so it’s the safest
way of navigating.

* **Parameters:**
  * **url** – the url to navigate to
  * **new_tab** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – open new tab
  * **new_window** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – open new window
* **Returns:**
  Page

#### *async* get_all_cookies(requests_cookie_format=False)

get all cookies

* **Parameters:**
  **requests_cookie_format** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – when True, returns python http.cookiejar.Cookie objects, compatible  with requests library and many others.
* **Returns:**
* **Return type:**

#### *async* get_all_linked_sources()

get all elements of tag: link, a, img, scripts meta, video, audio

* **Return type:**
  [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Element`](element.md#nodriver.Element)]
* **Returns:**

#### *async* get_all_urls(absolute=True)

convenience function, which returns all links (a,link,img,script,meta)

* **Parameters:**
  **absolute** – try to build all the links in absolute form instead of “as is”, often relative
* **Return type:**
  [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**
  list of urls

#### *async* get_content()

gets the current page source content (html)
:return:
:rtype:

#### *async* get_window()

get the window Bounds
:return:
:rtype:

#### *async* maximize()

maximize page/tab/window

#### *async* medimize()

#### *async* minimize()

minimize page/tab/window

#### *async* query_selector(selector, \_node=None)

find single element based on css selector string

* **Parameters:**
  **selector** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – css selector(s)
* **Returns:**
* **Return type:**

#### *async* query_selector_all(selector, \_node=None)

equivalent of javascripts document.querySelectorAll.
this is considered one of the main methods to use in this package.

it returns all matching [`nodriver.Element`](element.md#nodriver.Element) objects.

* **Parameters:**
  * **selector** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – css selector. (first time? => [https://www.w3schools.com/cssref/css_selectors.php](https://www.w3schools.com/cssref/css_selectors.php) )
  * **\_node** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`Node`](../cdp/dom.md#nodriver.cdp.dom.Node), [`Element`](element.md#nodriver.Element), [`None`](https://docs.python.org/3/library/constants.html#None)]) – internal use
* **Returns:**
* **Return type:**

#### *async* reload(ignore_cache=True, script_to_evaluate_on_load=None)

Reloads the page

* **Parameters:**
  * **ignore_cache** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – when set to True (default), it ignores cache, and re-downloads the items
  * **script_to_evaluate_on_load** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – script to run on load. I actually haven’t experimented with this one, so no guarantees.
* **Returns:**
* **Return type:**

#### *async* save_screenshot(filename='auto', format='jpeg', full_page=False)

Saves a screenshot of the page.
This is not the same as [`Element.save_screenshot`](element.md#nodriver.Element.save_screenshot), which saves a screenshot of a single element only

* **Parameters:**
  * **filename** (*PathLike*) – uses this as the save path
  * **format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – jpeg or png (defaults to jpeg)
  * **full_page** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – when False (default) it captures the current viewport. when True, it captures the entire page
* **Returns:**
  the path/filename of saved screenshot
* **Return type:**
  [str](https://docs.python.org/3/library/stdtypes.html#str)

#### *async* scroll_down(amount=25)

scrolls down maybe

* **Parameters:**
  **amount** ([*int*](https://docs.python.org/3/library/functions.html#int)) – number in percentage. 25 is a quarter of page, 50 half, and 1000 is 10x the page
* **Returns:**
* **Return type:**

#### *async* scroll_up(amount=25)

scrolls up maybe

* **Parameters:**
  **amount** ([*int*](https://docs.python.org/3/library/functions.html#int)) – number in percentage. 25 is a quarter of page, 50 half, and 1000 is 10x the page
* **Returns:**
* **Return type:**

#### *async* send(cdp_obj, \_is_update=False)

send a protocol command

* **Return type:**
  [object](https://docs.python.org/3/library/functions.html#object)
* **Parameters:**
  * **cdp_obj** ([`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]) – 
  * **\_is_update** – 
* **Returns:**

#### *async* set_all_cookies(cookies)

set cookies

* **Parameters:**
  **cookies** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CookieParam`](../cdp/network.md#nodriver.cdp.network.CookieParam)]) – list of cookies
* **Returns:**
* **Return type:**

#### *async* set_download_path(path)

sets the download path and allows downloads
this is required for any download function to work (well not entirely, since when unset we set a default folder)

* **Parameters:**
  **path** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path)]) – 
* **Returns:**
* **Return type:**

#### *async* set_window_size(left=0, top=0, width=1280, height=1024)

set window size and position

* **Parameters:**
  * **left** – pixels from the left of the screen to the window top-left corner
  * **top** – pixels from the top of the screen to the window top-left corner
  * **width** – width of the window in pixels
  * **height** – height of the window in pixels
* **Returns:**
* **Return type:**

#### *async* set_window_state(left=0, top=0, width=1280, height=720, state='normal')

sets the window size and state.
in case state is set other than “normal”, the left, top, width, and height are ignored.

* **Parameters:**
  * **left** ([*int*](https://docs.python.org/3/library/functions.html#int)) – desired offset from left, in pixels
  * **top** ([*int*](https://docs.python.org/3/library/functions.html#int)) – desired offset from the top, in pixels
  * **width** ([*int*](https://docs.python.org/3/library/functions.html#int)) – desired width in pixels
  * **height** ([*int*](https://docs.python.org/3/library/functions.html#int)) – desired height in pixels
  * **state** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – can be one of the following strings:
    : - normal
      - fullscreen
      - maximized
      - minimized

#### *async* sleep(t=0.25)

#### *property* target*: [TargetInfo](../cdp/target.md#nodriver.cdp.target.TargetInfo)*

#### *async* update_target()

#### *async* wait(t=None)

#### *async* wait_for(text='', selector='', timeout=5)

variant on query_selector_all and find_elements_by_text
this variant takes either selector or text, and will block until
the requested element(s) are found.

it will block for a maximum of <timeout> seconds, after which
an TimeoutError will be raised

* **Parameters:**
  * **selector** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – css selector
  * **text** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – text
  * **timeout** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`int`](https://docs.python.org/3/library/functions.html#int), [`float`](https://docs.python.org/3/library/functions.html#float), [`None`](https://docs.python.org/3/library/constants.html#None)]) – 
* **Returns:**
* **Return type:**
  [Element](element.md#nodriver.Element)
* **Raises:**
  asyncio.TimeoutError

#### websocket*: websockets.WebSocketClientProtocol*
