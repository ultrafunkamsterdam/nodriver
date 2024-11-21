# Memory

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.memory"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* PressureLevel(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Memory pressure level.

#### MODERATE *= 'moderate'*

#### CRITICAL *= 'critical'*

### *class* SamplingProfileNode(size, total, stack)

Heap profile sample.

#### size*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Size of the sampled allocation.

#### total*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Total bytes attributed to this sample.

#### stack*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Execution stack at the point of allocation.

### *class* SamplingProfile(samples, modules)

Array of heap profile samples.

#### samples*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SamplingProfileNode`](#nodriver.cdp.memory.SamplingProfileNode)]*

#### modules*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Module`](#nodriver.cdp.memory.Module)]*

### *class* Module(name, uuid, base_address, size)

Executable module information

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name of the module.

#### uuid*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

UUID of the module.

#### base_address*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Base address where the module is loaded into memory. Encoded as a decimal
or hexadecimal (0x prefixed) string.

#### size*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Size of the module in bytes.

### *class* DOMCounter(name, count)

DOM object counter data.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

object names should be presumed volatile and clients should not expect
the returned names to be consistent across runs.

* **Type:**
  Object name. Note

#### count*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Object count.

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### forcibly_purge_java_script_memory()

Simulate OomIntervention by purging V8 memory.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_all_time_sampling_profile()

Retrieve native memory allocations profile
collected since renderer process startup.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SamplingProfile`](#nodriver.cdp.memory.SamplingProfile)]
* **Returns:**

### get_browser_sampling_profile()

Retrieve native memory allocations profile
collected since browser process startup.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SamplingProfile`](#nodriver.cdp.memory.SamplingProfile)]
* **Returns:**

### get_dom_counters()

Retruns current DOM object counters.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`int`](https://docs.python.org/3/library/functions.html#int), [`int`](https://docs.python.org/3/library/functions.html#int), [`int`](https://docs.python.org/3/library/functions.html#int)]]
* **Returns:**
  A tuple with the following items:
  1. **documents** -
  2. **nodes** -
  3. **jsEventListeners** -

### get_dom_counters_for_leak_detection()

Retruns DOM object counters after preparing renderer for leak detection.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`DOMCounter`](#nodriver.cdp.memory.DOMCounter)]]
* **Returns:**
  DOM object counters.

### get_sampling_profile()

Retrieve native memory allocations profile collected since last
`startSampling` call.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SamplingProfile`](#nodriver.cdp.memory.SamplingProfile)]
* **Returns:**

### prepare_for_leak_detection()

Prepares for leak detection by terminating workers, stopping spellcheckers,
dropping non-essential internal caches, running garbage collections, etc.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_pressure_notifications_suppressed(suppressed)

Enable/disable suppressing memory pressure notifications in all processes.

* **Parameters:**
  **suppressed** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – If true, memory pressure notifications will be suppressed.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### simulate_pressure_notification(level)

Simulate a memory pressure notification in all processes.

* **Parameters:**
  **level** ([`PressureLevel`](#nodriver.cdp.memory.PressureLevel)) – Memory pressure level of the notification.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### start_sampling(sampling_interval=None, suppress_randomness=None)

Start collecting native memory profile.

* **Parameters:**
  * **sampling_interval** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Average number of bytes between samples.
  * **suppress_randomness** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Do not randomize intervals between samples.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### stop_sampling()

Stop collecting native memory profile.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

*There are no events in this module.*
