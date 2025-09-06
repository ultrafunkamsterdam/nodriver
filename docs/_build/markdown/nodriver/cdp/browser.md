# Browser

The Browser domain defines methods and events for browser managing.

<a id="module-nodriver.cdp.browser"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* BrowserContextID

### *class* WindowID

### *class* WindowState(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The state of the browser window.

#### NORMAL *= 'normal'*

#### MINIMIZED *= 'minimized'*

#### MAXIMIZED *= 'maximized'*

#### FULLSCREEN *= 'fullscreen'*

### *class* Bounds(left=None, top=None, width=None, height=None, window_state=None)

Browser window bounds information

#### left*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

The offset from the left edge of the screen to the window in pixels.

#### top*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

The offset from the top edge of the screen to the window in pixels.

#### width*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

The window width in pixels.

#### height*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

The window height in pixels.

#### window_state*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`WindowState`](#nodriver.cdp.browser.WindowState)]* *= None*

The window state. Default to normal.

### *class* PermissionType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### AR *= 'ar'*

#### AUDIO_CAPTURE *= 'audioCapture'*

#### AUTOMATIC_FULLSCREEN *= 'automaticFullscreen'*

#### BACKGROUND_FETCH *= 'backgroundFetch'*

#### BACKGROUND_SYNC *= 'backgroundSync'*

#### CAMERA_PAN_TILT_ZOOM *= 'cameraPanTiltZoom'*

#### CAPTURED_SURFACE_CONTROL *= 'capturedSurfaceControl'*

#### CLIPBOARD_READ_WRITE *= 'clipboardReadWrite'*

#### CLIPBOARD_SANITIZED_WRITE *= 'clipboardSanitizedWrite'*

#### DISPLAY_CAPTURE *= 'displayCapture'*

#### DURABLE_STORAGE *= 'durableStorage'*

#### GEOLOCATION *= 'geolocation'*

#### HAND_TRACKING *= 'handTracking'*

#### IDLE_DETECTION *= 'idleDetection'*

#### KEYBOARD_LOCK *= 'keyboardLock'*

#### LOCAL_FONTS *= 'localFonts'*

#### LOCAL_NETWORK_ACCESS *= 'localNetworkAccess'*

#### MIDI *= 'midi'*

#### MIDI_SYSEX *= 'midiSysex'*

#### NFC *= 'nfc'*

#### NOTIFICATIONS *= 'notifications'*

#### PAYMENT_HANDLER *= 'paymentHandler'*

#### PERIODIC_BACKGROUND_SYNC *= 'periodicBackgroundSync'*

#### POINTER_LOCK *= 'pointerLock'*

#### PROTECTED_MEDIA_IDENTIFIER *= 'protectedMediaIdentifier'*

#### SENSORS *= 'sensors'*

#### SMART_CARD *= 'smartCard'*

#### SPEAKER_SELECTION *= 'speakerSelection'*

#### STORAGE_ACCESS *= 'storageAccess'*

#### TOP_LEVEL_STORAGE_ACCESS *= 'topLevelStorageAccess'*

#### VIDEO_CAPTURE *= 'videoCapture'*

#### VR *= 'vr'*

#### WAKE_LOCK_SCREEN *= 'wakeLockScreen'*

#### WAKE_LOCK_SYSTEM *= 'wakeLockSystem'*

#### WEB_APP_INSTALLATION *= 'webAppInstallation'*

#### WEB_PRINTING *= 'webPrinting'*

#### WINDOW_MANAGEMENT *= 'windowManagement'*

### *class* PermissionSetting(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### GRANTED *= 'granted'*

#### DENIED *= 'denied'*

#### PROMPT *= 'prompt'*

### *class* PermissionDescriptor(name, sysex=None, user_visible_only=None, allow_without_sanitization=None, allow_without_gesture=None, pan_tilt_zoom=None)

Definition of PermissionDescriptor defined in the Permissions API:
[https://w3c.github.io/permissions/#dom-permissiondescriptor](https://w3c.github.io/permissions/#dom-permissiondescriptor).

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name of permission.
See [https://cs.chromium.org/chromium/src/third_party/blink/renderer/modules/permissions/permission_descriptor.idl](https://cs.chromium.org/chromium/src/third_party/blink/renderer/modules/permissions/permission_descriptor.idl) for valid permission names.

#### sysex*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

For “midi” permission, may also specify sysex control.

#### user_visible_only*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

For “push” permission, may specify userVisibleOnly.
Note that userVisibleOnly = true is the only currently supported type.

#### allow_without_sanitization*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

For “clipboard” permission, may specify allowWithoutSanitization.

#### allow_without_gesture*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

true.

* **Type:**
  For “fullscreen” permission, must specify allowWithoutGesture

#### pan_tilt_zoom*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

For “camera” permission, may specify panTiltZoom.

### *class* BrowserCommandId(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Browser command ids used by executeBrowserCommand.

#### OPEN_TAB_SEARCH *= 'openTabSearch'*

#### CLOSE_TAB_SEARCH *= 'closeTabSearch'*

#### OPEN_GLIC *= 'openGlic'*

### *class* Bucket(low, high, count)

Chrome histogram bucket.

#### low*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Minimum value (inclusive).

#### high*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Maximum value (exclusive).

#### count*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Number of samples.

### *class* Histogram(name, sum_, count, buckets)

Chrome histogram.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name.

#### sum_*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Sum of sample values.

#### count*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Total number of samples.

#### buckets*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Bucket`](#nodriver.cdp.browser.Bucket)]*

Buckets.

### *class* PrivacySandboxAPI(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### BIDDING_AND_AUCTION_SERVICES *= 'BiddingAndAuctionServices'*

#### TRUSTED_KEY_VALUE *= 'TrustedKeyValue'*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### add_privacy_sandbox_coordinator_key_config(api, coordinator_origin, key_config, browser_context_id=None)

Configures encryption keys used with a given privacy sandbox API to talk
to a trusted coordinator.  Since this is intended for test automation only,
coordinatorOrigin must be a .test domain. No existing coordinator
configuration for the origin may exist.

* **Parameters:**
  * **api** ([`PrivacySandboxAPI`](#nodriver.cdp.browser.PrivacySandboxAPI)) – 
  * **coordinator_origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **key_config** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **browser_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BrowserContextID`](#nodriver.cdp.browser.BrowserContextID)]) – *(Optional)* BrowserContext to perform the action in. When omitted, default browser context is used.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### add_privacy_sandbox_enrollment_override(url)

Allows a site to use privacy sandbox features that require enrollment
without the site actually being enrolled. Only supported on page targets.

* **Parameters:**
  **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### cancel_download(guid, browser_context_id=None)

Cancel a download if in progress

**EXPERIMENTAL**

* **Parameters:**
  * **guid** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Global unique identifier of the download.
  * **browser_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BrowserContextID`](#nodriver.cdp.browser.BrowserContextID)]) – *(Optional)* BrowserContext to perform the action in. When omitted, default browser context is used.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### close()

Close browser gracefully.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### crash()

Crashes browser on the main thread.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### crash_gpu_process()

Crashes GPU process.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### execute_browser_command(command_id)

Invoke custom browser commands used by telemetry.

**EXPERIMENTAL**

* **Parameters:**
  **command_id** ([`BrowserCommandId`](#nodriver.cdp.browser.BrowserCommandId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_browser_command_line()

Returns the command line switches for the browser process if, and only if
–enable-automation is on the commandline.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**
  Commandline parameters

### get_histogram(name, delta=None)

Get a Chrome histogram by name.

**EXPERIMENTAL**

* **Parameters:**
  * **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Requested histogram name.
  * **delta** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, retrieve delta since last delta call.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Histogram`](#nodriver.cdp.browser.Histogram)]
* **Returns:**
  Histogram.

### get_histograms(query=None, delta=None)

Get Chrome histograms.

**EXPERIMENTAL**

* **Parameters:**
  * **query** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Requested substring in name. Only histograms which have query as a substring in their name are extracted. An empty or absent query returns all histograms.
  * **delta** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, retrieve delta since last delta call.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Histogram`](#nodriver.cdp.browser.Histogram)]]
* **Returns:**
  Histograms.

### get_version()

Returns version information.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**
  A tuple with the following items:
  1. **protocolVersion** - Protocol version.
  2. **product** - Product name.
  3. **revision** - Product revision.
  4. **userAgent** - User-Agent.
  5. **jsVersion** - V8 version.

### get_window_bounds(window_id)

Get position and size of the browser window.

**EXPERIMENTAL**

* **Parameters:**
  **window_id** ([`WindowID`](#nodriver.cdp.browser.WindowID)) – Browser window id.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Bounds`](#nodriver.cdp.browser.Bounds)]
* **Returns:**
  Bounds information of the window. When window state is ‘minimized’, the restored window position and size are returned.

### get_window_for_target(target_id=None)

Get the browser window that contains the devtools target.

**EXPERIMENTAL**

* **Parameters:**
  **target_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TargetID`](target.md#nodriver.cdp.target.TargetID)]) – *(Optional)* Devtools agent host id. If called as a part of the session, associated targetId is used.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`WindowID`](#nodriver.cdp.browser.WindowID), [`Bounds`](#nodriver.cdp.browser.Bounds)]]
* **Returns:**
  A tuple with the following items:
  1. **windowId** - Browser window id.
  2. **bounds** - Bounds information of the window. When window state is ‘minimized’, the restored window position and size are returned.

### grant_permissions(permissions, origin=None, browser_context_id=None)

Grant specific permissions to the given origin and reject all others.

**EXPERIMENTAL**

* **Parameters:**
  * **permissions** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PermissionType`](#nodriver.cdp.browser.PermissionType)]) – 
  * **origin** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Origin the permission applies to, all origins if not specified.
  * **browser_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BrowserContextID`](#nodriver.cdp.browser.BrowserContextID)]) – *(Optional)* BrowserContext to override permissions. When omitted, default browser context is used.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### reset_permissions(browser_context_id=None)

Reset all permission management for all origins.

* **Parameters:**
  **browser_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BrowserContextID`](#nodriver.cdp.browser.BrowserContextID)]) – *(Optional)* BrowserContext to reset permissions. When omitted, default browser context is used.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_contents_size(window_id, width=None, height=None)

Set size of the browser contents resizing browser window as necessary.

**EXPERIMENTAL**

* **Parameters:**
  * **window_id** ([`WindowID`](#nodriver.cdp.browser.WindowID)) – Browser window id.
  * **width** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The window contents width in DIP. Assumes current width if omitted. Must be specified if ‘height’ is omitted.
  * **height** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The window contents height in DIP. Assumes current height if omitted. Must be specified if ‘width’ is omitted.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_dock_tile(badge_label=None, image=None)

Set dock tile details, platform-specific.

**EXPERIMENTAL**

* **Parameters:**
  * **badge_label** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)*
  * **image** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Png encoded image. (Encoded as a base64 string when passed over JSON)
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_download_behavior(behavior, browser_context_id=None, download_path=None, events_enabled=None)

Set the behavior when downloading a file.

**EXPERIMENTAL**

* **Parameters:**
  * **behavior** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Whether to allow all or deny all download requests, or use default Chrome behavior if available (otherwise deny). `allowAndName` allows download and names files according to their download guids.
  * **browser_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BrowserContextID`](#nodriver.cdp.browser.BrowserContextID)]) – *(Optional)* BrowserContext to set download behavior. When omitted, default browser context is used.
  * **download_path** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* The default path to save downloaded files to. This is required if behavior is set to ‘allow’ or ‘allowAndName’.
  * **events_enabled** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to emit download events (defaults to false).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_permission(permission, setting, origin=None, embedding_origin=None, browser_context_id=None)

Set permission settings for given requesting and embedding origins.

**EXPERIMENTAL**

* **Parameters:**
  * **permission** ([`PermissionDescriptor`](#nodriver.cdp.browser.PermissionDescriptor)) – Descriptor of permission to override.
  * **setting** ([`PermissionSetting`](#nodriver.cdp.browser.PermissionSetting)) – Setting of the permission.
  * **origin** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Requesting origin the permission applies to, all origins if not specified.
  * **embedding_origin** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Embedding origin the permission applies to. It is ignored unless the requesting origin is present and valid. If the requesting origin is provided but the embedding origin isn’t, the requesting origin is used as the embedding origin.
  * **browser_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BrowserContextID`](#nodriver.cdp.browser.BrowserContextID)]) – *(Optional)* Context to override. When omitted, default browser context is used.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_window_bounds(window_id, bounds)

Set position and/or size of the browser window.

**EXPERIMENTAL**

* **Parameters:**
  * **window_id** ([`WindowID`](#nodriver.cdp.browser.WindowID)) – Browser window id.
  * **bounds** ([`Bounds`](#nodriver.cdp.browser.Bounds)) – New window bounds. The ‘minimized’, ‘maximized’ and ‘fullscreen’ states cannot be combined with ‘left’, ‘top’, ‘width’ or ‘height’. Leaves unspecified fields unchanged.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* DownloadWillBegin(frame_id, guid, url, suggested_filename)

**EXPERIMENTAL**

Fired when page is about to start a download.

#### frame_id*: [`FrameId`](page.md#nodriver.cdp.page.FrameId)*

Id of the frame that caused the download to begin.

#### guid*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Global unique identifier of the download.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL of the resource being downloaded.

#### suggested_filename*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Suggested file name of the resource (the actual name of the file saved on disk may differ).

### *class* DownloadProgress(guid, total_bytes, received_bytes, state, file_path)

**EXPERIMENTAL**

Fired when download makes progress. Last call has `done` == true.

#### guid*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Global unique identifier of the download.

#### total_bytes*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Total expected bytes to download.

#### received_bytes*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Total bytes received.

#### state*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Download status.

#### file_path*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

If download is “completed”, provides the path of the downloaded file.
Depending on the platform, it is not guaranteed to be set, nor the file
is guaranteed to exist.
