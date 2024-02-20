<a id="browser"></a>

# Browser class

Some words about the Browser class

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

#### *async classmethod* create(config=None, \*, user_data_dir=None, headless=False, browser_executable_path=None, browser_args=None, sandbox=True, \*\*kwargs)

entry point for creating an instance

* **Return type:**
  [`Browser`](#nodriver.Browser)

#### targets *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)*

current targets (all types

#### *property* main_tab *: [Tab](tab.md#nodriver.Tab)*

returns the target which was launched with the browser

#### *property* tabs *: [List](https://docs.python.org/3/library/typing.html#typing.List)[[Tab](tab.md#nodriver.Tab)]*

returns the current targets which are of type “page”
:return:

#### *async* wait(time=1)

wait for <time> seconds. important to use, especially in between page navigation

* **Parameters:**
  **time** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`float`](https://docs.python.org/3/library/functions.html#float), [`int`](https://docs.python.org/3/library/functions.html#int)]) – 
* **Return type:**
  [`Browser`](#nodriver.Browser)
* **Returns:**

#### *async* sleep(time=1)

alias for wait

* **Return type:**
  [`Browser`](#nodriver.Browser)

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
