# Target

Supports additional targets discovery and allows to attach to them.

<a id="module-nodriver.cdp.target"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* TargetID

### *class* SessionID

Unique identifier of attached debugging session.

### *class* TargetInfo(target_id, type_, title, url, attached, can_access_opener, opener_id=None, opener_frame_id=None, browser_context_id=None, subtype=None)

#### target_id*: [`TargetID`](#nodriver.cdp.target.TargetID)*

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

//source.chromium.org/chromium/chromium/src/+/main:content/browser/devtools/devtools_agent_host_impl.cc?ss=chromium&q=f:devtools%20-f:out%20%22::kTypeTab%5B%5D%22

* **Type:**
  List of types
* **Type:**
  https

#### title*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### attached*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether the target has an attached client.

#### can_access_opener*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether the target has access to the originating window.

#### opener_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TargetID`](#nodriver.cdp.target.TargetID)]* *= None*

Opener target Id

#### opener_frame_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]* *= None*

Frame id of originating window (is only set if target has an opener).

#### browser_context_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BrowserContextID`](browser.md#nodriver.cdp.browser.BrowserContextID)]* *= None*

#### subtype*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Provides additional details for specific target types. For example, for
the type of “page”, this may be set to “prerender”.

### *class* FilterEntry(exclude=None, type_=None)

A filter used by target query/discovery/auto-attach operations.

#### exclude*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

If set, causes exclusion of matching targets from the list.

#### type_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

If not present, matches any type.

### *class* TargetFilter(iterable=(), /)

The entries in TargetFilter are matched sequentially against targets and
the first entry that matches determines if the target is included or not,
depending on the value of `exclude` field in the entry.
If filter is not specified, the one assumed is
[{type: “browser”, exclude: true}, {type: “tab”, exclude: true}, {}]
(i.e. include everything but `browser` and `tab`).

### *class* RemoteLocation(host, port)

#### host*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### port*: [`int`](https://docs.python.org/3/library/functions.html#int)*

### *class* WindowState(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The state of the target window.

#### NORMAL *= 'normal'*

#### MINIMIZED *= 'minimized'*

#### MAXIMIZED *= 'maximized'*

#### FULLSCREEN *= 'fullscreen'*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### activate_target(target_id)

Activates (focuses) the target.

* **Parameters:**
  **target_id** ([`TargetID`](#nodriver.cdp.target.TargetID)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### attach_to_browser_target()

Attaches to the browser target, only uses flat sessionId mode.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SessionID`](#nodriver.cdp.target.SessionID)]
* **Returns:**
  Id assigned to the session.

### attach_to_target(target_id, flatten=None)

Attaches to the target with given id.

* **Parameters:**
  * **target_id** ([`TargetID`](#nodriver.cdp.target.TargetID)) – 
  * **flatten** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Enables “flat” access to the session via specifying sessionId attribute in the commands. We plan to make this the default, deprecate non-flattened mode, and eventually retire it. See crbug.com/991325.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SessionID`](#nodriver.cdp.target.SessionID)]
* **Returns:**
  Id assigned to the session.

### auto_attach_related(target_id, wait_for_debugger_on_start, filter_=None)

Adds the specified target to the list of targets that will be monitored for any related target
creation (such as child frames, child workers and new versions of service worker) and reported
through `attachedToTarget`. The specified target is also auto-attached.
This cancels the effect of any previous `setAutoAttach` and is also cancelled by subsequent
`setAutoAttach`. Only available at the Browser target.

**EXPERIMENTAL**

* **Parameters:**
  * **target_id** ([`TargetID`](#nodriver.cdp.target.TargetID)) – 
  * **wait_for_debugger_on_start** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to pause new targets when attaching to them. Use ``Runtime.runIfWaitingForDebugger`` to run paused targets.
  * **filter** – **(EXPERIMENTAL)** *(Optional)* Only targets matching filter will be attached.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### close_target(target_id)

Closes the target. If the target is a page that gets closed too.

* **Parameters:**
  **target_id** ([`TargetID`](#nodriver.cdp.target.TargetID)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`bool`](https://docs.python.org/3/library/functions.html#bool)]
* **Returns:**
  Always set to true. If an error occurs, the response indicates protocol error.

### create_browser_context(dispose_on_detach=None, proxy_server=None, proxy_bypass_list=None, origins_with_universal_network_access=None)

Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than
one.

* **Parameters:**
  * **dispose_on_detach** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* If specified, disposes this context when debugging session disconnects.
  * **proxy_server** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* Proxy server, similar to the one passed to –proxy-server
  * **proxy_bypass_list** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* Proxy bypass list, similar to the one passed to –proxy-bypass-list
  * **origins_with_universal_network_access** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]) – **(EXPERIMENTAL)** *(Optional)* An optional list of origins to grant unlimited cross-origin access to. Parts of the URL other than those constituting origin are ignored.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`BrowserContextID`](browser.md#nodriver.cdp.browser.BrowserContextID)]
* **Returns:**
  The id of the context created.

### create_target(url, left=None, top=None, width=None, height=None, window_state=None, browser_context_id=None, enable_begin_frame_control=None, new_window=None, background=None, for_tab=None)

Creates a new page.

* **Parameters:**
  * **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – The initial URL the page will be navigated to. An empty string indicates [about:blank](about:blank).
  * **left** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* Frame left origin in DIP (requires newWindow to be true or headless shell).
  * **top** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* Frame top origin in DIP (requires newWindow to be true or headless shell).
  * **width** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Frame width in DIP (requires newWindow to be true or headless shell).
  * **height** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Frame height in DIP (requires newWindow to be true or headless shell).
  * **window_state** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`WindowState`](#nodriver.cdp.target.WindowState)]) – *(Optional)* Frame window state (requires newWindow to be true or headless shell). Default is normal.
  * **browser_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BrowserContextID`](browser.md#nodriver.cdp.browser.BrowserContextID)]) – **(EXPERIMENTAL)** *(Optional)* The browser context to create the page in.
  * **enable_begin_frame_control** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether BeginFrames for this target will be controlled via DevTools (headless shell only, not supported on MacOS yet, false by default).
  * **new_window** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to create a new Window or Tab (false by default, not supported by headless shell).
  * **background** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to create the target in background or foreground (false by default, not supported by headless shell).
  * **for_tab** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether to create the target of type “tab”.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`TargetID`](#nodriver.cdp.target.TargetID)]
* **Returns:**
  The id of the page opened.

### detach_from_target(session_id=None, target_id=None)

Detaches session with given id.

* **Parameters:**
  * **session_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SessionID`](#nodriver.cdp.target.SessionID)]) – *(Optional)* Session to detach.
  * **target_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TargetID`](#nodriver.cdp.target.TargetID)]) – **(DEPRECATED)** *(Optional)* Deprecated.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### dispose_browser_context(browser_context_id)

Deletes a BrowserContext. All the belonging pages will be closed without calling their
beforeunload hooks.

* **Parameters:**
  **browser_context_id** ([`BrowserContextID`](browser.md#nodriver.cdp.browser.BrowserContextID)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### expose_dev_tools_protocol(target_id, binding_name=None, inherit_permissions=None)

Inject object to the target’s main frame that provides a communication
channel with browser target.

Injected object will be available as `window[bindingName]`.

The object has the following API:
- `binding.send(json)` - a method to send messages over the remote debugging protocol
- `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses.

**EXPERIMENTAL**

* **Parameters:**
  * **target_id** ([`TargetID`](#nodriver.cdp.target.TargetID)) – 
  * **binding_name** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Binding name, ‘cdp’ if not specified.
  * **inherit_permissions** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, inherits the current root session’s permissions (default: false).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_browser_contexts()

Returns all browser contexts created with `Target.createBrowserContext` method.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BrowserContextID`](browser.md#nodriver.cdp.browser.BrowserContextID)]]
* **Returns:**
  An array of browser context ids.

### get_target_info(target_id=None)

Returns information about a target.

**EXPERIMENTAL**

* **Parameters:**
  **target_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TargetID`](#nodriver.cdp.target.TargetID)]) – *(Optional)*
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`TargetInfo`](#nodriver.cdp.target.TargetInfo)]
* **Returns:**

### get_targets(filter_=None)

Retrieves a list of available targets.

* **Parameters:**
  **filter** – **(EXPERIMENTAL)** *(Optional)* Only targets matching filter will be reported. If filter is not specified and target discovery is currently enabled, a filter used for target discovery is used for consistency.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`TargetInfo`](#nodriver.cdp.target.TargetInfo)]]
* **Returns:**
  The list of targets.

### send_message_to_target(message, session_id=None, target_id=None)

Sends protocol message over session with given id.
Consider using flat mode instead; see commands attachToTarget, setAutoAttach,
and crbug.com/991325.

#### Deprecated
Deprecated since version 1.3.

* **Parameters:**
  * **message** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **session_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SessionID`](#nodriver.cdp.target.SessionID)]) – *(Optional)* Identifier of the session.
  * **target_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TargetID`](#nodriver.cdp.target.TargetID)]) – **(DEPRECATED)** *(Optional)* Deprecated.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### set_auto_attach(auto_attach, wait_for_debugger_on_start, flatten=None, filter_=None)

Controls whether to automatically attach to new targets which are considered to be related to
this one. When turned on, attaches to all existing related targets as well. When turned off,
automatically detaches from all currently attached targets.
This also clears all targets added by `autoAttachRelated` from the list of targets to watch
for creation of related targets.

* **Parameters:**
  * **auto_attach** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to auto-attach to related targets.
  * **wait_for_debugger_on_start** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to pause new targets when attaching to them. Use ``Runtime.runIfWaitingForDebugger`` to run paused targets.
  * **flatten** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Enables “flat” access to the session via specifying sessionId attribute in the commands. We plan to make this the default, deprecate non-flattened mode, and eventually retire it. See crbug.com/991325.
  * **filter** – **(EXPERIMENTAL)** *(Optional)* Only targets matching filter will be attached.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_discover_targets(discover, filter_=None)

Controls whether to discover available targets and notify via
`targetCreated/targetInfoChanged/targetDestroyed` events.

* **Parameters:**
  * **discover** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to discover available targets.
  * **filter** – **(EXPERIMENTAL)** *(Optional)* Only targets matching filter will be attached. If ``discover``` is false, ```filter`` must be omitted or empty.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_remote_locations(locations)

Enables target discovery for the specified locations, when `setDiscoverTargets` was set to
`true`.

**EXPERIMENTAL**

* **Parameters:**
  **locations** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`RemoteLocation`](#nodriver.cdp.target.RemoteLocation)]) – List of remote locations.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* AttachedToTarget(session_id, target_info, waiting_for_debugger)

**EXPERIMENTAL**

Issued when attached to target because of auto-attach or `attachToTarget` command.

#### session_id*: [`SessionID`](#nodriver.cdp.target.SessionID)*

Identifier assigned to the session used to send/receive messages.

#### target_info*: [`TargetInfo`](#nodriver.cdp.target.TargetInfo)*

#### waiting_for_debugger*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

### *class* DetachedFromTarget(session_id, target_id)

**EXPERIMENTAL**

Issued when detached from target for any reason (including `detachFromTarget` command). Can be
issued multiple times per target if multiple sessions have been attached to it.

#### session_id*: [`SessionID`](#nodriver.cdp.target.SessionID)*

Detached session identifier.

#### target_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TargetID`](#nodriver.cdp.target.TargetID)]*

Deprecated.

### *class* ReceivedMessageFromTarget(session_id, message, target_id)

Notifies about a new protocol message received from the session (as reported in
`attachedToTarget` event).

#### session_id*: [`SessionID`](#nodriver.cdp.target.SessionID)*

Identifier of a session which sends a message.

#### message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### target_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TargetID`](#nodriver.cdp.target.TargetID)]*

Deprecated.

### *class* TargetCreated(target_info)

Issued when a possible inspection target is created.

#### target_info*: [`TargetInfo`](#nodriver.cdp.target.TargetInfo)*

### *class* TargetDestroyed(target_id)

Issued when a target is destroyed.

#### target_id*: [`TargetID`](#nodriver.cdp.target.TargetID)*

### *class* TargetCrashed(target_id, status, error_code)

Issued when a target has crashed.

#### target_id*: [`TargetID`](#nodriver.cdp.target.TargetID)*

#### status*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Termination status type.

#### error_code*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Termination error code.

### *class* TargetInfoChanged(target_info)

Issued when some information about a target has changed. This only happens between
`targetCreated` and `targetDestroyed`.

#### target_info*: [`TargetInfo`](#nodriver.cdp.target.TargetInfo)*
