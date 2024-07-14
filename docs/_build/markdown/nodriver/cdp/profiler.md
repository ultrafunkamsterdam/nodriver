# Profiler

* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* ProfileNode(id_, call_frame, hit_count=None, children=None, deopt_reason=None, position_ticks=None)

Profile node. Holds callsite information, execution statistics and child nodes.

#### id_*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Unique id of the node.

#### call_frame*: [`CallFrame`](runtime.md#nodriver.cdp.runtime.CallFrame)*

Function location.

#### hit_count*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Number of samples where this node was on top of the call stack.

#### children*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]]* *= None*

Child node ids.

#### deopt_reason*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The reason of being not optimized. The function may be deoptimized or marked as don’t
optimize.

#### position_ticks*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PositionTickInfo`](#nodriver.cdp.profiler.PositionTickInfo)]]* *= None*

An array of source position ticks.

### *class* Profile(nodes, start_time, end_time, samples=None, time_deltas=None)

Profile.

#### nodes*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ProfileNode`](#nodriver.cdp.profiler.ProfileNode)]*

The list of profile nodes. First item is the root node.

#### start_time*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Profiling start timestamp in microseconds.

#### end_time*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Profiling end timestamp in microseconds.

#### samples*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]]* *= None*

Ids of samples top nodes.

#### time_deltas*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]]* *= None*

Time intervals between adjacent samples in microseconds. The first delta is relative to the
profile startTime.

### *class* PositionTickInfo(line, ticks)

Specifies a number of samples attributed to a certain source position.

#### line*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Source line number (1-based).

#### ticks*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Number of samples attributed to the source line.

### *class* CoverageRange(start_offset, end_offset, count)

Coverage data for a source range.

#### start_offset*: [`int`](https://docs.python.org/3/library/functions.html#int)*

JavaScript script source offset for the range start.

#### end_offset*: [`int`](https://docs.python.org/3/library/functions.html#int)*

JavaScript script source offset for the range end.

#### count*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Collected execution count of the source range.

### *class* FunctionCoverage(function_name, ranges, is_block_coverage)

Coverage data for a JavaScript function.

#### function_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

JavaScript function name.

#### ranges*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CoverageRange`](#nodriver.cdp.profiler.CoverageRange)]*

Source ranges inside the function with coverage data.

#### is_block_coverage*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether coverage data for this function has block granularity.

### *class* ScriptCoverage(script_id, url, functions)

Coverage data for a JavaScript script.

#### script_id*: [`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)*

JavaScript script id.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

JavaScript script name or url.

#### functions*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`FunctionCoverage`](#nodriver.cdp.profiler.FunctionCoverage)]*

Functions contained in the script that has coverage data.

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### disable()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_best_effort_coverage()

Collect coverage data for the current isolate. The coverage data may be incomplete due to
garbage collection.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ScriptCoverage`](#nodriver.cdp.profiler.ScriptCoverage)]]
* **Returns:**
  Coverage data for the current isolate.

### set_sampling_interval(interval)

Changes CPU profiler sampling interval. Must be called before CPU profiles recording started.

* **Parameters:**
  **interval** ([`int`](https://docs.python.org/3/library/functions.html#int)) – New sampling interval in microseconds.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### start()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### start_precise_coverage(call_count=None, detailed=None, allow_triggered_updates=None)

Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code
coverage may be incomplete. Enabling prevents running optimized code and resets execution
counters.

* **Parameters:**
  * **call_count** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Collect accurate call counts beyond simple ‘covered’ or ‘not covered’.
  * **detailed** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Collect block-based coverage.
  * **allow_triggered_updates** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Allow the backend to send updates on its own initiative
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`float`](https://docs.python.org/3/library/functions.html#float)]
* **Returns:**
  Monotonically increasing time (in seconds) when the coverage update was taken in the backend.

### stop()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Profile`](#nodriver.cdp.profiler.Profile)]
* **Returns:**
  Recorded profile.

### stop_precise_coverage()

Disable precise code coverage. Disabling releases unnecessary execution count records and allows
executing optimized code.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### take_precise_coverage()

Collect coverage data for the current isolate, and resets execution counters. Precise code
coverage needs to have started.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ScriptCoverage`](#nodriver.cdp.profiler.ScriptCoverage)], [`float`](https://docs.python.org/3/library/functions.html#float)]]
* **Returns:**
  A tuple with the following items:
  1. **result** - Coverage data for the current isolate.
  2. **timestamp** - Monotonically increasing time (in seconds) when the coverage update was taken in the backend.

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* ConsoleProfileFinished(id_, location, profile, title)

#### id_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### location*: [`Location`](debugger.md#nodriver.cdp.debugger.Location)*

Location of console.profileEnd().

#### profile*: [`Profile`](#nodriver.cdp.profiler.Profile)*

#### title*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Profile title passed as an argument to console.profile().

### *class* ConsoleProfileStarted(id_, location, title)

Sent when new profile recording is started using console.profile() call.

#### id_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### location*: [`Location`](debugger.md#nodriver.cdp.debugger.Location)*

Location of console.profile().

#### title*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Profile title passed as an argument to console.profile().

### *class* PreciseCoverageDeltaUpdate(timestamp, occasion, result)

**EXPERIMENTAL**

Reports coverage delta since the last poll (either from an event like this, or from
`takePreciseCoverage` for the current isolate. May only be sent if precise code
coverage has been started. This event can be trigged by the embedder to, for example,
trigger collection of coverage data immediately at a certain point in time.

#### timestamp*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Monotonically increasing time (in seconds) when the coverage update was taken in the backend.

#### occasion*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Identifier for distinguishing coverage events.

#### result*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ScriptCoverage`](#nodriver.cdp.profiler.ScriptCoverage)]*

Coverage data for the current isolate.
