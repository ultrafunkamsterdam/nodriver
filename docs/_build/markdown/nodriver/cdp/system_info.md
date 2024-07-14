# SystemInfo

The SystemInfo domain defines methods and events for querying low-level system information.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.system_info"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* GPUDevice(vendor_id, device_id, vendor_string, device_string, driver_vendor, driver_version, sub_sys_id=None, revision=None)

Describes a single graphics processor (GPU).

#### vendor_id*: [`float`](https://docs.python.org/3/library/functions.html#float)*

PCI ID of the GPU vendor, if available; 0 otherwise.

#### device_id*: [`float`](https://docs.python.org/3/library/functions.html#float)*

PCI ID of the GPU device, if available; 0 otherwise.

#### vendor_string*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

String description of the GPU vendor, if the PCI ID is not available.

#### device_string*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

String description of the GPU device, if the PCI ID is not available.

#### driver_vendor*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

String description of the GPU driver vendor.

#### driver_version*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

String description of the GPU driver version.

#### sub_sys_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Sub sys ID of the GPU, only available on Windows.

#### revision*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Revision of the GPU, only available on Windows.

### *class* Size(width, height)

Describes the width and height dimensions of an entity.

#### width*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Width in pixels.

#### height*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Height in pixels.

### *class* VideoDecodeAcceleratorCapability(profile, max_resolution, min_resolution)

Describes a supported video decoding profile with its associated minimum and
maximum resolutions.

#### profile*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Video codec profile that is supported, e.g. VP9 Profile 2.

#### max_resolution*: [`Size`](#nodriver.cdp.system_info.Size)*

Maximum video dimensions in pixels supported for this `profile`.

#### min_resolution*: [`Size`](#nodriver.cdp.system_info.Size)*

Minimum video dimensions in pixels supported for this `profile`.

### *class* VideoEncodeAcceleratorCapability(profile, max_resolution, max_framerate_numerator, max_framerate_denominator)

Describes a supported video encoding profile with its associated maximum
resolution and maximum framerate.

#### profile*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Video codec profile that is supported, e.g H264 Main.

#### max_resolution*: [`Size`](#nodriver.cdp.system_info.Size)*

Maximum video dimensions in pixels supported for this `profile`.

#### max_framerate_numerator*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Maximum encoding framerate in frames per second supported for this
`profile`, as fraction’s numerator and denominator, e.g. 24/1 fps,
24000/1001 fps, etc.

#### max_framerate_denominator*: [`int`](https://docs.python.org/3/library/functions.html#int)*

### *class* SubsamplingFormat(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

YUV subsampling type of the pixels of a given image.

#### YUV420 *= 'yuv420'*

#### YUV422 *= 'yuv422'*

#### YUV444 *= 'yuv444'*

### *class* ImageType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Image format of a given image.

#### JPEG *= 'jpeg'*

#### WEBP *= 'webp'*

#### UNKNOWN *= 'unknown'*

### *class* ImageDecodeAcceleratorCapability(image_type, max_dimensions, min_dimensions, subsamplings)

Describes a supported image decoding profile with its associated minimum and
maximum resolutions and subsampling.

#### image_type*: [`ImageType`](#nodriver.cdp.system_info.ImageType)*

Image coded, e.g. Jpeg.

#### max_dimensions*: [`Size`](#nodriver.cdp.system_info.Size)*

Maximum supported dimensions of the image in pixels.

#### min_dimensions*: [`Size`](#nodriver.cdp.system_info.Size)*

Minimum supported dimensions of the image in pixels.

#### subsamplings*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SubsamplingFormat`](#nodriver.cdp.system_info.SubsamplingFormat)]*

0, if known.

* **Type:**
  Optional array of supported subsampling formats, e.g. 4
* **Type:**
  2

### *class* GPUInfo(devices, driver_bug_workarounds, video_decoding, video_encoding, image_decoding, aux_attributes=None, feature_status=None)

Provides information about the GPU(s) on the system.

#### devices*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`GPUDevice`](#nodriver.cdp.system_info.GPUDevice)]*

The graphics devices on the system. Element 0 is the primary GPU.

#### driver_bug_workarounds*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

An optional array of GPU driver bug workarounds.

#### video_decoding*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`VideoDecodeAcceleratorCapability`](#nodriver.cdp.system_info.VideoDecodeAcceleratorCapability)]*

Supported accelerated video decoding capabilities.

#### video_encoding*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`VideoEncodeAcceleratorCapability`](#nodriver.cdp.system_info.VideoEncodeAcceleratorCapability)]*

Supported accelerated video encoding capabilities.

#### image_decoding*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ImageDecodeAcceleratorCapability`](#nodriver.cdp.system_info.ImageDecodeAcceleratorCapability)]*

Supported accelerated image decoding capabilities.

#### aux_attributes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]* *= None*

An optional dictionary of additional GPU related attributes.

#### feature_status*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]* *= None*

An optional dictionary of graphics features and their status.

### *class* ProcessInfo(type_, id_, cpu_time)

Represents process info.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Specifies process type.

#### id_*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Specifies process id.

#### cpu_time*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Specifies cumulative CPU usage in seconds across all threads of the
process since the process start.

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### get_feature_state(feature_state)

Returns information about the feature state.

* **Parameters:**
  **feature_state** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`bool`](https://docs.python.org/3/library/functions.html#bool)]
* **Returns:**

### get_info()

Returns information about the system.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`GPUInfo`](#nodriver.cdp.system_info.GPUInfo), [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**
  A tuple with the following items:
  1. **gpu** - Information about the GPUs on the system.
  2. **modelName** - A platform-dependent description of the model of the machine. On Mac OS, this is, for example, ‘MacBookPro’. Will be the empty string if not supported.
  3. **modelVersion** - A platform-dependent description of the version of the machine. On Mac OS, this is, for example, ‘10.1’. Will be the empty string if not supported.
  4. **commandLine** - The command line string used to launch the browser. Will be the empty string if not supported.

### get_process_info()

Returns information about all running processes.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ProcessInfo`](#nodriver.cdp.system_info.ProcessInfo)]]
* **Returns:**
  An array of process info blocks.

## Events

*There are no events in this module.*
