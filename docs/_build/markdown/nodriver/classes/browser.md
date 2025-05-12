<a id="browser"></a>

# Browser class

## cookies

You can load and save all cookies from the browser.

```default
# save. when no filepath is given, it is saved in '.session.dat'
await browser.cookies.save()
```

```default
# load. when no filepath is given, it is loaded from '.session.dat'
await browser.cookies.load()
```

```default
# export for requests or other library
requests_style_cookies = await browser.cookies.get_all(requests_cookie_format=True)

# use in requests:
session = requests.Session()
for cookie in requests_style_cookies:
    session.cookies.set_cookie(cookie)
```

## Browser class

### *class* Browser(config, \*\*kwargs)

The Browser object is the “root” of the hierarchy and contains a reference
to the browser parent process.
there should usually be only 1 instance of this.

All opened tabs, extra browser screens and resources will not cause a new Browser process,
but rather create additional [`nodriver.Tab`](tab.md#nodriver.Tab) objects.

So, besides starting your instance and first/additional tabs, you don’t actively use it a lot under normal conditions.

Tab objects will represent and control
: - tabs (as you know them)
  - browser windows (new window)
  - iframe
  - background processes

note:
the Browser object is not instantiated by \_\_init_\_ but using the asynchronous [`nodriver.Browser.create()`](#nodriver.Browser.create) method.

note:
in Chromium based browsers, there is a parent process which keeps running all the time, even if
there are no visible browser windows. sometimes it’s stubborn to close it, so make sure after using
this library, the browser is correctly and fully closed/exited/killed.

#### *async classmethod* create(config=None, \*, user_data_dir=None, headless=False, browser_executable_path=None, browser_args=None, sandbox=True, host=None, port=None, \*\*kwargs)

entry point for creating an instance

* **Return type:**
  [`Browser`](#nodriver.Browser)

#### config*: [`Config`](others_and_helpers.md#nodriver.Config)*

#### targets*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)*

current targets (all types

#### connection*: `Connection`*

#### *property* websocket_url

#### *property* main_tab*: [Tab](tab.md#nodriver.Tab)*

returns the target which was launched with the browser

#### *property* tabs*: [List](https://docs.python.org/3/library/typing.html#typing.List)[[Tab](tab.md#nodriver.Tab)]*

returns the current targets which are of type “page”
:return:

#### *property* cookies*: CookieJar*

#### *property* stopped

#### *async* wait(time=0.1)

wait for <time> seconds. important to use, especially in between page navigation

* **Parameters:**
  **time** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`float`](https://docs.python.org/3/library/functions.html#float), [`int`](https://docs.python.org/3/library/functions.html#int)]) – 
* **Returns:**

#### *async* sleep(time=0.1)

alias for wait

#### *async* get(url='chrome://welcome', new_tab=False, new_window=False)

top level get. utilizes the first tab to retrieve given url.

convenience function known from selenium.
this function handles waits/sleeps and detects when DOM events fired, so it’s the safest
way of navigating.

* **Parameters:**
  * **url** – the url to navigate to
  * **new_tab** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – open new tab
  * **new_window** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – open new window
* **Return type:**
  [`Tab`](tab.md#nodriver.Tab)
* **Returns:**
  Page

#### *async* create_context(url='chrome://welcome', new_tab=False, new_window=True, dispose_on_detach=True, proxy_server=None, proxy_bypass_list=None, origins_with_universal_network_access=None)

creates a new browser context - mostly useful if you want to use proxies for different browser instances
since chrome usually can only use 1 proxy per browser.
socks5 with authentication is supported by using a forwarder proxy, the
correct string to use socks proxy with username/password auth is socks://USERNAME:PASSWORD@SERVER:PORT

dispose_on_detach – (EXPERIMENTAL) (Optional) If specified, disposes this context when debugging session disconnects.
proxy_server – (EXPERIMENTAL) (Optional) Proxy server, similar to the one passed to –proxy-server
proxy_bypass_list – (EXPERIMENTAL) (Optional) Proxy bypass list, similar to the one passed to –proxy-bypass-list
origins_with_universal_network_access – (EXPERIMENTAL) (Optional) An optional list of origins to grant unlimited cross-origin access to. Parts of the URL other than those constituting origin are ignored.

* **Parameters:**
  * **new_window** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
  * **new_tab** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
  * **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **dispose_on_detach** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
  * **proxy_server** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **proxy_bypass_list** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – 
  * **origins_with_universal_network_access** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – 
* **Returns:**
* **Return type:**

#### *async* start()

launches the actual browser

* **Return type:**
  [`Browser`](#nodriver.Browser)

#### *async* grant_all_permissions()

grant permissions for:
: accessibilityEvents
  audioCapture
  backgroundSync
  backgroundFetch
  clipboardReadWrite
  clipboardSanitizedWrite
  displayCapture
  durableStorage
  geolocation
  idleDetection
  localFonts
  midi
  midiSysex
  nfc
  notifications
  paymentHandler
  periodicBackgroundSync
  protectedMediaIdentifier
  sensors
  storageAccess
  topLevelStorageAccess
  videoCapture
  videoCapturePanTiltZoom
  wakeLockScreen
  wakeLockSystem
  windowManagement

#### *async* tile_windows(windows=None, max_columns=0)

#### *async* update_targets()

#### stop()
