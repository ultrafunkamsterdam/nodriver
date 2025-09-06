# PWA

This domain allows interacting with the browser to control PWAs.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.pwa"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* FileHandlerAccept(media_type, file_extensions)

The following types are the replica of
[https://crsrc.org/c/chrome/browser/web_applications/proto/web_app_os_integration_state.proto;drc=9910d3be894c8f142c977ba1023f30a656bc13fc;l=67](https://crsrc.org/c/chrome/browser/web_applications/proto/web_app_os_integration_state.proto;drc=9910d3be894c8f142c977ba1023f30a656bc13fc;l=67)

#### media_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

New name of the mimetype according to
[https://www.iana.org/assignments/media-types/media-types.xhtml](https://www.iana.org/assignments/media-types/media-types.xhtml)

#### file_extensions*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

### *class* FileHandler(action, accepts, display_name)

#### action*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### accepts*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`FileHandlerAccept`](#nodriver.cdp.pwa.FileHandlerAccept)]*

#### display_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* DisplayMode(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

If user prefers opening the app in browser or an app window.

#### STANDALONE *= 'standalone'*

#### BROWSER *= 'browser'*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### change_app_user_settings(manifest_id, link_capturing=None, display_mode=None)

Changes user settings of the web app identified by its manifestId. If the
app was not installed, this command returns an error. Unset parameters will
be ignored; unrecognized values will cause an error.

Unlike the ones defined in the manifest files of the web apps, these
settings are provided by the browser and controlled by the users, they
impact the way the browser handling the web apps.

See the comment of each parameter.

* **Parameters:**
  * **manifest_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **link_capturing** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If user allows the links clicked on by the user in the app’s scope, or extended scope if the manifest has scope extensions and the flags ``DesktopPWAsLinkCapturingWithScopeExtensions``` and ```WebAppEnableScopeExtensions`` are enabled.  Note, the API does not support resetting the linkCapturing to the initial value, uninstalling and installing the web app again will reset it.  TODO(crbug.com/339453269): Setting this value on ChromeOS is not supported yet.
  * **display_mode** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`DisplayMode`](#nodriver.cdp.pwa.DisplayMode)]) – *(Optional)*
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_os_app_state(manifest_id)

Returns the following OS state for the given manifest id.

* **Parameters:**
  **manifest_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – The id from the webapp’s manifest file, commonly it’s the url of the site installing the webapp. See [https://web.dev/learn/pwa/web-app-manifest](https://web.dev/learn/pwa/web-app-manifest).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`int`](https://docs.python.org/3/library/functions.html#int), [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`FileHandler`](#nodriver.cdp.pwa.FileHandler)]]]
* **Returns:**
  A tuple with the following items:
  1. **badgeCount** -
  2. **fileHandlers** -

### install(manifest_id, install_url_or_bundle_url=None)

Installs the given manifest identity, optionally using the given installUrlOrBundleUrl

IWA-specific install description:
manifestId corresponds to isolated-app:// + web_package::SignedWebBundleId

File installation mode:
The installUrlOrBundleUrl can be either [file://](file://) or http(s):// pointing
to a signed web bundle (.swbn). In this case SignedWebBundleId must correspond to
The .swbn file’s signing key.

Dev proxy installation mode:
installUrlOrBundleUrl must be http(s):// that serves dev mode IWA.
web_package::SignedWebBundleId must be of type dev proxy.

The advantage of dev proxy mode is that all changes to IWA
automatically will be reflected in the running app without
reinstallation.

To generate bundle id for proxy mode:
1. Generate 32 random bytes.
2. Add a specific suffix at the end following the documentation

> [https://github.com/WICG/isolated-web-apps/blob/main/Scheme.md#suffix](https://github.com/WICG/isolated-web-apps/blob/main/Scheme.md#suffix)
1. Encode the entire sequence using Base32 without padding.

If Chrome is not in IWA dev
mode, the installation will fail, regardless of the state of the allowlist.

* **Parameters:**
  * **manifest_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **install_url_or_bundle_url** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* The location of the app or bundle overriding the one derived from the manifestId.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### launch(manifest_id, url=None)

Launches the installed web app, or an url in the same web app instead of the
default start url if it is provided. Returns a page Target.TargetID which
can be used to attach to via Target.attachToTarget or similar APIs.

* **Parameters:**
  * **manifest_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **url** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)*
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`TargetID`](target.md#nodriver.cdp.target.TargetID)]
* **Returns:**
  ID of the tab target created as a result.

### launch_files_in_app(manifest_id, files)

Opens one or more local files from an installed web app identified by its
manifestId. The web app needs to have file handlers registered to process
the files. The API returns one or more page Target.TargetIDs which can be
used to attach to via Target.attachToTarget or similar APIs.
If some files in the parameters cannot be handled by the web app, they will
be ignored. If none of the files can be handled, this API returns an error.
If no files are provided as the parameter, this API also returns an error.

According to the definition of the file handlers in the manifest file, one
Target.TargetID may represent a page handling one or more files. The order
of the returned Target.TargetIDs is not guaranteed.

TODO(crbug.com/339454034): Check the existences of the input files.

* **Parameters:**
  * **manifest_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **files** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`TargetID`](target.md#nodriver.cdp.target.TargetID)]]
* **Returns:**
  IDs of the tab targets created as the result.

### open_current_page_in_app(manifest_id)

Opens the current page in its web app identified by the manifest id, needs
to be called on a page target. This function returns immediately without
waiting for the app to finish loading.

* **Parameters:**
  **manifest_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### uninstall(manifest_id)

Uninstalls the given manifest_id and closes any opened app windows.

* **Parameters:**
  **manifest_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

*There are no events in this module.*
