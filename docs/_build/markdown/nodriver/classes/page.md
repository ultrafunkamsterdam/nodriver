<a id="page"></a>

# Page class

some words about page connection

### *class* Page(websocket_url, target, browser=None, \*\*kwargs)

* **Parameters:**
  * **websocket_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **target** ([*TargetInfo*](../cdp/target.md#nodriver.cdp.target.TargetInfo)) – 
  * **browser** ([*Browser*](browser.md#nodriver.Browser)) – 

#### *async* activate()

active this target (ie: tab,window,page)

#### *async* aopen(\*\*kw)

* **Parameters:**
  **kw** – 
* **Returns:**

#### *async* back()

history back

#### *async* bring_to_front()

alias to self.activate

#### *async* close()

close the current target (ie: tab,window,page)
:return:
:rtype:

#### *async* download_file(url, filename=None)

downloads file by given url.

* **Parameters:**
  * **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – url of the file
  * **filename** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path), [`None`](https://docs.python.org/3/library/constants.html#None)]) – the name for the file. if not specified the name is composed from the url file name

#### *async* find_element_by_text(text, return_enclosing_element=True)

* **Parameters:**
  * **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **return_enclosing_element** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – 
* **Returns:**
* **Return type:**

#### *async* find_elements_by_text(text, return_enclosing_element=True)

* **Parameters:**
  * **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **return_enclosing_element** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if False, it returns the textual element,
    but usually one needs the element containing the text, like a button. default = True
* **Returns:**
* **Return type:**

#### *async* forward()

history forward

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

* **Return type:**
  [*Bounds*](../cdp/browser.md#nodriver.cdp.browser.Bounds)

#### *async* maximize()

maximize page/tab/window

#### *async* minimize()

minimize page/tab/window

#### *async* query_selector(selector, \_node=None)

find single element based on css selector string

* **Parameters:**
  * **selector** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – css selector(s)
  * **\_node** ([*Node*](../cdp/dom.md#nodriver.cdp.dom.Node) *|* [*Element*](element.md#nodriver.Element) *|* *None*) – 
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

#### *async* wait_for(element, timeout_ms)

wait for element to appear in the dom. could be useful when you expect some element but
not want a hard coded time value to wait

* **Parameters:**
  * **selector** – 
  * **timeout_ms** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`int`](https://docs.python.org/3/library/functions.html#int), [`float`](https://docs.python.org/3/library/functions.html#float)]) – 
* **Returns:**
* **Return type:**
