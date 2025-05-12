# Emulation

This domain emulates different environments for the page.

<a id="module-nodriver.cdp.emulation"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* SafeAreaInsets(top=None, top_max=None, left=None, left_max=None, bottom=None, bottom_max=None, right=None, right_max=None)

#### top*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Overrides safe-area-inset-top.

#### top_max*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Overrides safe-area-max-inset-top.

#### left*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Overrides safe-area-inset-left.

#### left_max*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Overrides safe-area-max-inset-left.

#### bottom*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Overrides safe-area-inset-bottom.

#### bottom_max*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Overrides safe-area-max-inset-bottom.

#### right*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Overrides safe-area-inset-right.

#### right_max*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Overrides safe-area-max-inset-right.

### *class* ScreenOrientation(type_, angle)

Screen orientation.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Orientation type.

#### angle*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Orientation angle.

### *class* DisplayFeature(orientation, offset, mask_length)

#### orientation*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Orientation of a display feature in relation to screen

#### offset*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The offset from the screen origin in either the x (for vertical
orientation) or y (for horizontal orientation) direction.

#### mask_length*: [`int`](https://docs.python.org/3/library/functions.html#int)*

A display feature may mask content such that it is not physically
displayed - this length along with the offset describes this area.
A display feature that only splits content will have a 0 mask_length.

### *class* DevicePosture(type_)

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Current posture of the device

### *class* MediaFeature(name, value)

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* VirtualTimePolicy(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to
allow the next delayed task (if any) to run; pause: The virtual time base may not advance;
pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending
resource fetches.

#### ADVANCE *= 'advance'*

#### PAUSE *= 'pause'*

#### PAUSE_IF_NETWORK_FETCHES_PENDING *= 'pauseIfNetworkFetchesPending'*

### *class* UserAgentBrandVersion(brand, version)

Used to specify User Agent Client Hints to emulate. See [https://wicg.github.io/ua-client-hints](https://wicg.github.io/ua-client-hints)

#### brand*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### version*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* UserAgentMetadata(platform, platform_version, architecture, model, mobile, brands=None, full_version_list=None, full_version=None, bitness=None, wow64=None)

Used to specify User Agent Client Hints to emulate. See [https://wicg.github.io/ua-client-hints](https://wicg.github.io/ua-client-hints)
Missing optional values will be filled in by the target with what it would normally use.

#### platform*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### platform_version*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### architecture*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### model*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### mobile*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### brands*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`UserAgentBrandVersion`](#nodriver.cdp.emulation.UserAgentBrandVersion)]]* *= None*

Brands appearing in Sec-CH-UA.

#### full_version_list*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`UserAgentBrandVersion`](#nodriver.cdp.emulation.UserAgentBrandVersion)]]* *= None*

Brands appearing in Sec-CH-UA-Full-Version-List.

#### full_version*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### bitness*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### wow64*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

### *class* SensorType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Used to specify sensor types to emulate.
See [https://w3c.github.io/sensors/#automation](https://w3c.github.io/sensors/#automation) for more information.

#### ABSOLUTE_ORIENTATION *= 'absolute-orientation'*

#### ACCELEROMETER *= 'accelerometer'*

#### AMBIENT_LIGHT *= 'ambient-light'*

#### GRAVITY *= 'gravity'*

#### GYROSCOPE *= 'gyroscope'*

#### LINEAR_ACCELERATION *= 'linear-acceleration'*

#### MAGNETOMETER *= 'magnetometer'*

#### RELATIVE_ORIENTATION *= 'relative-orientation'*

### *class* SensorMetadata(available=None, minimum_frequency=None, maximum_frequency=None)

#### available*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

#### minimum_frequency*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

#### maximum_frequency*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

### *class* SensorReadingSingle(value)

#### value*: [`float`](https://docs.python.org/3/library/functions.html#float)*

### *class* SensorReadingXYZ(x, y, z)

#### x*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### y*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### z*: [`float`](https://docs.python.org/3/library/functions.html#float)*

### *class* SensorReadingQuaternion(x, y, z, w)

#### x*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### y*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### z*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### w*: [`float`](https://docs.python.org/3/library/functions.html#float)*

### *class* SensorReading(single=None, xyz=None, quaternion=None)

#### single*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SensorReadingSingle`](#nodriver.cdp.emulation.SensorReadingSingle)]* *= None*

#### xyz*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SensorReadingXYZ`](#nodriver.cdp.emulation.SensorReadingXYZ)]* *= None*

#### quaternion*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SensorReadingQuaternion`](#nodriver.cdp.emulation.SensorReadingQuaternion)]* *= None*

### *class* PressureSource(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### CPU *= 'cpu'*

### *class* PressureState(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### NOMINAL *= 'nominal'*

#### FAIR *= 'fair'*

#### SERIOUS *= 'serious'*

#### CRITICAL *= 'critical'*

### *class* PressureMetadata(available=None)

#### available*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

### *class* DisabledImageType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of image types that can be disabled.

#### AVIF *= 'avif'*

#### WEBP *= 'webp'*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### can_emulate()

Tells whether emulation is supported.

#### Deprecated
Deprecated since version 1.3.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`bool`](https://docs.python.org/3/library/functions.html#bool)]
* **Returns:**
  True if emulation is supported.

#### Deprecated
Deprecated since version 1.3.

### clear_device_metrics_override()

Clears the overridden device metrics.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### clear_device_posture_override()

Clears a device posture override set with either setDeviceMetricsOverride()
or setDevicePostureOverride() and starts using posture information from the
platform again.
Does nothing if no override is set.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### clear_display_features_override()

Clears the display features override set with either setDeviceMetricsOverride()
or setDisplayFeaturesOverride() and starts using display features from the
platform again.
Does nothing if no override is set.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### clear_geolocation_override()

Clears the overridden Geolocation Position and Error.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### clear_idle_override()

Clears Idle state overrides.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_overridden_sensor_information(type_)

**EXPERIMENTAL**

* **Parameters:**
  **type** – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`float`](https://docs.python.org/3/library/functions.html#float)]
* **Returns:**

### reset_page_scale_factor()

Requests that page scale factor is reset to initial values.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_auto_dark_mode_override(enabled=None)

Automatically render all web contents using a dark theme.

**EXPERIMENTAL**

* **Parameters:**
  **enabled** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to enable or disable automatic dark mode. If not specified, any existing override will be cleared.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_automation_override(enabled)

Allows overriding the automation flag.

**EXPERIMENTAL**

* **Parameters:**
  **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether the override should be enabled.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_cpu_throttling_rate(rate)

Enables CPU throttling to emulate slow CPUs.

* **Parameters:**
  **rate** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_default_background_color_override(color=None)

Sets or clears an override of the default background color of the frame. This override is used
if the content does not specify one.

* **Parameters:**
  **color** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]) – *(Optional)* RGBA of the default background color. If not specified, any existing override will be cleared.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_device_metrics_override(width, height, device_scale_factor, mobile, scale=None, screen_width=None, screen_height=None, position_x=None, position_y=None, dont_set_visible_size=None, screen_orientation=None, viewport=None, display_feature=None, device_posture=None)

Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
window.innerWidth, window.innerHeight, and “device-width”/”device-height”-related CSS media
query results).

* **Parameters:**
  * **width** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
  * **height** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
  * **device_scale_factor** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Overriding device scale factor value. 0 disables the override.
  * **mobile** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more.
  * **scale** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – **(EXPERIMENTAL)** *(Optional)* Scale to apply to resulting view image.
  * **screen_width** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* Overriding screen width value in pixels (minimum 0, maximum 10000000).
  * **screen_height** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* Overriding screen height value in pixels (minimum 0, maximum 10000000).
  * **position_x** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
  * **position_y** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
  * **dont_set_visible_size** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Do not set visible view size, rely upon explicit setVisibleSize call.
  * **screen_orientation** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ScreenOrientation`](#nodriver.cdp.emulation.ScreenOrientation)]) – *(Optional)* Screen orientation override.
  * **viewport** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Viewport`](page.md#nodriver.cdp.page.Viewport)]) – **(EXPERIMENTAL)** *(Optional)* If set, the visible area of the page will be overridden to this viewport. This viewport change is not observed by the page, e.g. viewport-relative elements do not change positions.
  * **display_feature** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`DisplayFeature`](#nodriver.cdp.emulation.DisplayFeature)]) – **(DEPRECATED)** **(EXPERIMENTAL)** *(Optional)* If set, the display feature of a multi-segment screen. If not set, multi-segment support is turned-off. Deprecated, use Emulation.setDisplayFeaturesOverride.
  * **device_posture** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`DevicePosture`](#nodriver.cdp.emulation.DevicePosture)]) – **(DEPRECATED)** **(EXPERIMENTAL)** *(Optional)* If set, the posture of a foldable device. If not set the posture is set to continuous. Deprecated, use Emulation.setDevicePostureOverride.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_device_posture_override(posture)

Start reporting the given posture value to the Device Posture API.
This override can also be set in setDeviceMetricsOverride().

**EXPERIMENTAL**

* **Parameters:**
  **posture** ([`DevicePosture`](#nodriver.cdp.emulation.DevicePosture)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_disabled_image_types(image_types)

**EXPERIMENTAL**

* **Parameters:**
  **image_types** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`DisabledImageType`](#nodriver.cdp.emulation.DisabledImageType)]) – Image types to disable.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_display_features_override(features)

Start using the given display features to pupulate the Viewport Segments API.
This override can also be set in setDeviceMetricsOverride().

**EXPERIMENTAL**

* **Parameters:**
  **features** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`DisplayFeature`](#nodriver.cdp.emulation.DisplayFeature)]) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_document_cookie_disabled(disabled)

**EXPERIMENTAL**

* **Parameters:**
  **disabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether document.coookie API should be disabled.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_emit_touch_events_for_mouse(enabled, configuration=None)

**EXPERIMENTAL**

* **Parameters:**
  * **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether touch emulation based on mouse input should be enabled.
  * **configuration** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Touch/gesture events configuration. Default: current platform.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_emulated_media(media=None, features=None)

Emulates the given media type or media feature for CSS media queries.

* **Parameters:**
  * **media** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Media type to emulate. Empty string disables the override.
  * **features** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`MediaFeature`](#nodriver.cdp.emulation.MediaFeature)]]) – *(Optional)* Media features to emulate.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_emulated_vision_deficiency(type_)

Emulates the given vision deficiency.

* **Parameters:**
  **type** – Vision deficiency to emulate. Order: best-effort emulations come first, followed by any physiologically accurate emulations for medically recognized color vision deficiencies.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_focus_emulation_enabled(enabled)

Enables or disables simulating a focused and active page.

**EXPERIMENTAL**

* **Parameters:**
  **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to enable to disable focus emulation.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_geolocation_override(latitude=None, longitude=None, accuracy=None)

Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
unavailable.

* **Parameters:**
  * **latitude** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Mock latitude
  * **longitude** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Mock longitude
  * **accuracy** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Mock accuracy
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_hardware_concurrency_override(hardware_concurrency)

**EXPERIMENTAL**

* **Parameters:**
  **hardware_concurrency** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Hardware concurrency to report
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_idle_override(is_user_active, is_screen_unlocked)

Overrides the Idle state.

* **Parameters:**
  * **is_user_active** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Mock isUserActive
  * **is_screen_unlocked** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Mock isScreenUnlocked
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_locale_override(locale=None)

Overrides default host system locale with the specified one.

**EXPERIMENTAL**

* **Parameters:**
  **locale** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* ICU style C locale (e.g. “en_US”). If not specified or empty, disables the override and restores default host system locale.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_navigator_overrides(platform)

Overrides value returned by the javascript navigator object.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  **platform** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – The platform navigator.platform should return.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### set_page_scale_factor(page_scale_factor)

Sets a specified page scale factor.

**EXPERIMENTAL**

* **Parameters:**
  **page_scale_factor** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Page scale factor.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_pressure_source_override_enabled(enabled, source, metadata=None)

Overrides a pressure source of a given type, as used by the Compute
Pressure API, so that updates to PressureObserver.observe() are provided
via setPressureStateOverride instead of being retrieved from
platform-provided telemetry data.

**EXPERIMENTAL**

* **Parameters:**
  * **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
  * **source** ([`PressureSource`](#nodriver.cdp.emulation.PressureSource)) – 
  * **metadata** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`PressureMetadata`](#nodriver.cdp.emulation.PressureMetadata)]) – *(Optional)*
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_pressure_state_override(source, state)

Provides a given pressure state that will be processed and eventually be
delivered to PressureObserver users. `source` must have been previously
overridden by setPressureSourceOverrideEnabled.

**EXPERIMENTAL**

* **Parameters:**
  * **source** ([`PressureSource`](#nodriver.cdp.emulation.PressureSource)) – 
  * **state** ([`PressureState`](#nodriver.cdp.emulation.PressureState)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_safe_area_insets_override(insets)

Overrides the values for env(safe-area-inset-*) and env(safe-area-max-inset-*). Unset values will cause the
respective variables to be undefined, even if previously overridden.

**EXPERIMENTAL**

* **Parameters:**
  **insets** ([`SafeAreaInsets`](#nodriver.cdp.emulation.SafeAreaInsets)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_script_execution_disabled(value)

Switches script execution in the page.

* **Parameters:**
  **value** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether script execution should be disabled in the page.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_scrollbars_hidden(hidden)

**EXPERIMENTAL**

* **Parameters:**
  **hidden** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether scrollbars should be always hidden.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_sensor_override_enabled(enabled, type_, metadata=None)

Overrides a platform sensor of a given type. If `enabled` is true, calls to
Sensor.start() will use a virtual sensor as backend rather than fetching
data from a real hardware sensor. Otherwise, existing virtual
sensor-backend Sensor objects will fire an error event and new calls to
Sensor.start() will attempt to use a real sensor instead.

**EXPERIMENTAL**

* **Parameters:**
  * **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
  * **type** – 
  * **metadata** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SensorMetadata`](#nodriver.cdp.emulation.SensorMetadata)]) – *(Optional)*
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_sensor_override_readings(type_, reading)

Updates the sensor readings reported by a sensor type previously overridden
by setSensorOverrideEnabled.

**EXPERIMENTAL**

* **Parameters:**
  * **type** – 
  * **reading** ([`SensorReading`](#nodriver.cdp.emulation.SensorReading)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_timezone_override(timezone_id)

Overrides default host system timezone with the specified one.

* **Parameters:**
  **timezone_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – The timezone identifier. List of supported timezones: [https://source.chromium.org/chromium/chromium/deps/icu.git/+/faee8bc70570192d82d2978a71e2a615788597d1:source/data/misc/metaZones.txt](https://source.chromium.org/chromium/chromium/deps/icu.git/+/faee8bc70570192d82d2978a71e2a615788597d1:source/data/misc/metaZones.txt) If empty, disables the override and restores default host system timezone.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_touch_emulation_enabled(enabled, max_touch_points=None)

Enables touch on platforms which do not support them.

* **Parameters:**
  * **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether the touch event emulation should be enabled.
  * **max_touch_points** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Maximum touch points supported. Defaults to one.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_user_agent_override(user_agent, accept_language=None, platform=None, user_agent_metadata=None)

Allows overriding user agent with the given string.
`userAgentMetadata` must be set for Client Hint headers to be sent.

* **Parameters:**
  * **user_agent** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – User agent to use.
  * **accept_language** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Browser language to emulate.
  * **platform** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* The platform navigator.platform should return.
  * **user_agent_metadata** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`UserAgentMetadata`](#nodriver.cdp.emulation.UserAgentMetadata)]) – **(EXPERIMENTAL)** *(Optional)* To be sent in Sec-CH-UA-\* headers and returned in navigator.userAgentData
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_virtual_time_policy(policy, budget=None, max_virtual_time_task_starvation_count=None, initial_virtual_time=None)

Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets
the current virtual time policy.  Note this supersedes any previous time budget.

**EXPERIMENTAL**

* **Parameters:**
  * **policy** ([`VirtualTimePolicy`](#nodriver.cdp.emulation.VirtualTimePolicy)) – 
  * **budget** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* If set, after this many virtual milliseconds have elapsed virtual time will be paused and a virtualTimeBudgetExpired event is sent.
  * **max_virtual_time_task_starvation_count** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* If set this specifies the maximum number of tasks that can be run before virtual is forced forwards to prevent deadlock.
  * **initial_virtual_time** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)]) – *(Optional)* If set, base::Time::Now will be overridden to initially return this value.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`float`](https://docs.python.org/3/library/functions.html#float)]
* **Returns:**
  Absolute timestamp at which virtual time was first enabled (up time in milliseconds).

### set_visible_size(width, height)

Resizes the frame/viewport of the page. Note that this does not affect the frame’s container
(e.g. browser window). Can be used to produce screenshots of the specified size. Not supported
on Android.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  * **width** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Frame width (DIP).
  * **height** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Frame height (DIP).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* VirtualTimeBudgetExpired

**EXPERIMENTAL**

Notification sent after the virtual time budget for the current VirtualTimePolicy has run out.
