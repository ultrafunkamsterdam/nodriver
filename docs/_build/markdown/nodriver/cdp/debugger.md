# Debugger

Debugger domain exposes JavaScript debugging capabilities. It allows setting and removing
breakpoints, stepping through execution, exploring stack traces, etc.

<a id="module-nodriver.cdp.debugger"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* BreakpointId

Breakpoint identifier.

### *class* CallFrameId

Call frame identifier.

### *class* Location(script_id, line_number, column_number=None)

Location in the source code.

#### script_id*: [`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)*

Script identifier as reported in the `Debugger.scriptParsed`.

#### line_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Line number in the script (0-based).

#### column_number*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Column number in the script (0-based).

### *class* ScriptPosition(line_number, column_number)

Location in the source code.

#### line_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

#### column_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

### *class* LocationRange(script_id, start, end)

Location range within one script.

#### script_id*: [`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)*

#### start*: [`ScriptPosition`](#nodriver.cdp.debugger.ScriptPosition)*

#### end*: [`ScriptPosition`](#nodriver.cdp.debugger.ScriptPosition)*

### *class* CallFrame(call_frame_id, function_name, location, url, scope_chain, this, function_location=None, return_value=None, can_be_restarted=None)

JavaScript call frame. Array of call frames form the call stack.

#### call_frame_id*: [`CallFrameId`](#nodriver.cdp.debugger.CallFrameId)*

Call frame identifier. This identifier is only valid while the virtual machine is paused.

#### function_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name of the JavaScript function called on this call frame.

#### location*: [`Location`](#nodriver.cdp.debugger.Location)*

Location in the source code.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

JavaScript script name or url.
Deprecated in favor of using the `location.scriptId` to resolve the URL via a previously
sent `Debugger.scriptParsed` event.

#### scope_chain*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Scope`](#nodriver.cdp.debugger.Scope)]*

Scope chain for this call frame.

#### this*: [`RemoteObject`](runtime.md#nodriver.cdp.runtime.RemoteObject)*

`this` object for this call frame.

#### function_location*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Location`](#nodriver.cdp.debugger.Location)]* *= None*

Location in the source code.

#### return_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObject`](runtime.md#nodriver.cdp.runtime.RemoteObject)]* *= None*

The value being returned, if the function is at return point.

#### can_be_restarted*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Valid only while the VM is paused and indicates whether this frame
can be restarted or not. Note that a `true` value here does not
guarantee that Debugger#restartFrame with this CallFrameId will be
successful, but it is very likely.

### *class* Scope(type_, object_, name=None, start_location=None, end_location=None)

Scope description.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Scope type.

#### object_*: [`RemoteObject`](runtime.md#nodriver.cdp.runtime.RemoteObject)*

Object representing the scope. For `global` and `with` scopes it represents the actual
object; for the rest of the scopes, it is artificial transient object enumerating scope
variables as its properties.

#### name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### start_location*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Location`](#nodriver.cdp.debugger.Location)]* *= None*

Location in the source code where scope starts

#### end_location*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Location`](#nodriver.cdp.debugger.Location)]* *= None*

Location in the source code where scope ends

### *class* SearchMatch(line_number, line_content)

Search match for resource.

#### line_number*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Line number in resource content.

#### line_content*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Line with match content.

### *class* BreakLocation(script_id, line_number, column_number=None, type_=None)

#### script_id*: [`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)*

Script identifier as reported in the `Debugger.scriptParsed`.

#### line_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Line number in the script (0-based).

#### column_number*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Column number in the script (0-based).

#### type_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* WasmDisassemblyChunk(lines, bytecode_offsets)

#### lines*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

The next chunk of disassembled lines.

#### bytecode_offsets*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

The bytecode offsets describing the start of each line.

### *class* ScriptLanguage(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of possible script languages.

#### JAVA_SCRIPT *= 'JavaScript'*

#### WEB_ASSEMBLY *= 'WebAssembly'*

### *class* DebugSymbols(type_, external_url=None)

Debug symbols available for a wasm script.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Type of the debug symbols.

#### external_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

URL of the external symbol source.

### *class* ResolvedBreakpoint(breakpoint_id, location)

#### breakpoint_id*: [`BreakpointId`](#nodriver.cdp.debugger.BreakpointId)*

Breakpoint unique identifier.

#### location*: [`Location`](#nodriver.cdp.debugger.Location)*

Actual breakpoint location.

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### continue_to_location(location, target_call_frames=None)

Continues execution until specific location is reached.

* **Parameters:**
  * **location** ([`Location`](#nodriver.cdp.debugger.Location)) – Location to continue to.
  * **target_call_frames** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)*
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### disable()

Disables debugger for given page.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### disassemble_wasm_module(script_id)

**EXPERIMENTAL**

* **Parameters:**
  **script_id** ([`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)) – Id of the script to disassemble
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)], [`int`](https://docs.python.org/3/library/functions.html#int), [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)], [`WasmDisassemblyChunk`](#nodriver.cdp.debugger.WasmDisassemblyChunk)]]
* **Returns:**
  A tuple with the following items:
  1. **streamId** - *(Optional)* For large modules, return a stream from which additional chunks of disassembly can be read successively.
  2. **totalNumberOfLines** - The total number of lines in the disassembly text.
  3. **functionBodyOffsets** - The offsets of all function bodies, in the format [start1, end1, start2, end2, …] where all ends are exclusive.
  4. **chunk** - The first chunk of disassembly.

### enable(max_scripts_cache_size=None)

Enables debugger for the given page. Clients should not assume that the debugging has been
enabled until the result for this command is received.

* **Parameters:**
  **max_scripts_cache_size** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – **(EXPERIMENTAL)** *(Optional)* The maximum size in bytes of collected scripts (not referenced by other heap objects) the debugger can hold. Puts no limit if parameter is omitted.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`UniqueDebuggerId`](runtime.md#nodriver.cdp.runtime.UniqueDebuggerId)]
* **Returns:**
  Unique identifier of the debugger.

### evaluate_on_call_frame(call_frame_id, expression, object_group=None, include_command_line_api=None, silent=None, return_by_value=None, generate_preview=None, throw_on_side_effect=None, timeout=None)

Evaluates expression on a given call frame.

* **Parameters:**
  * **call_frame_id** ([`CallFrameId`](#nodriver.cdp.debugger.CallFrameId)) – Call frame identifier to evaluate on.
  * **expression** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Expression to evaluate.
  * **object_group** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* String object group name to put result into (allows rapid releasing resulting object handles using ``releaseObjectGroup```).
  * **include_command_line_api** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Specifies whether command line API should be available to the evaluated expression, defaults to false.
  * **silent** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides ```setPauseOnException`` state.
  * **return_by_value** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether the result is expected to be a JSON object that should be sent by value.
  * **generate_preview** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether preview should be generated for the result.
  * **throw_on_side_effect** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to throw an exception if side effect cannot be ruled out during evaluation.
  * **timeout** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeDelta`](runtime.md#nodriver.cdp.runtime.TimeDelta)]) – **(EXPERIMENTAL)** *(Optional)* Terminate execution after timing out (number of milliseconds).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`RemoteObject`](runtime.md#nodriver.cdp.runtime.RemoteObject), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExceptionDetails`](runtime.md#nodriver.cdp.runtime.ExceptionDetails)]]]
* **Returns:**
  A tuple with the following items:
  1. **result** - Object wrapper for the evaluation result.
  2. **exceptionDetails** - *(Optional)* Exception details.

### get_possible_breakpoints(start, end=None, restrict_to_function=None)

Returns possible locations for breakpoint. scriptId in start and end range locations should be
the same.

* **Parameters:**
  * **start** ([`Location`](#nodriver.cdp.debugger.Location)) – Start of range to search possible breakpoint locations in.
  * **end** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Location`](#nodriver.cdp.debugger.Location)]) – *(Optional)* End of range to search possible breakpoint locations in (excluding). When not specified, end of scripts is used as end of range.
  * **restrict_to_function** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Only consider locations which are in the same (non-nested) function as start.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BreakLocation`](#nodriver.cdp.debugger.BreakLocation)]]
* **Returns:**
  List of the possible breakpoint locations.

### get_script_source(script_id)

Returns source for the script with given id.

* **Parameters:**
  **script_id** ([`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)) – Id of the script to get source for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]]
* **Returns:**
  A tuple with the following items:
  1. **scriptSource** - Script source (empty in case of Wasm bytecode).
  2. **bytecode** - *(Optional)* Wasm bytecode. (Encoded as a base64 string when passed over JSON)

### get_stack_trace(stack_trace_id)

Returns stack trace with given `stackTraceId`.

**EXPERIMENTAL**

* **Parameters:**
  **stack_trace_id** ([`StackTraceId`](runtime.md#nodriver.cdp.runtime.StackTraceId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`StackTrace`](runtime.md#nodriver.cdp.runtime.StackTrace)]
* **Returns:**

### get_wasm_bytecode(script_id)

This command is deprecated. Use getScriptSource instead.

#### Deprecated
Deprecated since version 1.3.

* **Parameters:**
  **script_id** ([`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)) – Id of the Wasm script to get source for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**
  Script source. (Encoded as a base64 string when passed over JSON)

#### Deprecated
Deprecated since version 1.3.

### next_wasm_disassembly_chunk(stream_id)

Disassemble the next chunk of lines for the module corresponding to the
stream. If disassembly is complete, this API will invalidate the streamId
and return an empty chunk. Any subsequent calls for the now invalid stream
will return errors.

**EXPERIMENTAL**

* **Parameters:**
  **stream_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`WasmDisassemblyChunk`](#nodriver.cdp.debugger.WasmDisassemblyChunk)]
* **Returns:**
  The next chunk of disassembly.

### pause()

Stops on the next JavaScript statement.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### pause_on_async_call(parent_stack_trace_id)

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  **parent_stack_trace_id** ([`StackTraceId`](runtime.md#nodriver.cdp.runtime.StackTraceId)) – Debugger will pause when async call with given stack trace is started.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### remove_breakpoint(breakpoint_id)

Removes JavaScript breakpoint.

* **Parameters:**
  **breakpoint_id** ([`BreakpointId`](#nodriver.cdp.debugger.BreakpointId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### restart_frame(call_frame_id, mode=None)

Restarts particular call frame from the beginning. The old, deprecated
behavior of `restartFrame` is to stay paused and allow further CDP commands
after a restart was scheduled. This can cause problems with restarting, so
we now continue execution immediatly after it has been scheduled until we
reach the beginning of the restarted frame.

To stay back-wards compatible, `restartFrame` now expects a `mode`
parameter to be present. If the `mode` parameter is missing, `restartFrame`
errors out.

The various return values are deprecated and `callFrames` is always empty.
Use the call frames from the `Debugger#paused` events instead, that fires
once V8 pauses at the beginning of the restarted function.

* **Parameters:**
  * **call_frame_id** ([`CallFrameId`](#nodriver.cdp.debugger.CallFrameId)) – Call frame identifier to evaluate on.
  * **mode** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* The ``mode``` parameter must be present and set to ‘StepInto’, otherwise ```restartFrame`` will error out.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CallFrame`](#nodriver.cdp.debugger.CallFrame)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTrace`](runtime.md#nodriver.cdp.runtime.StackTrace)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTraceId`](runtime.md#nodriver.cdp.runtime.StackTraceId)]]]
* **Returns:**
  A tuple with the following items:
  1. **callFrames** - New stack trace.
  2. **asyncStackTrace** - *(Optional)* Async stack trace, if any.
  3. **asyncStackTraceId** - *(Optional)* Async stack trace, if any.

### resume(terminate_on_resume=None)

Resumes JavaScript execution.

* **Parameters:**
  **terminate_on_resume** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Set to true to terminate execution upon resuming execution. In contrast to Runtime.terminateExecution, this will allows to execute further JavaScript (i.e. via evaluation) until execution of the paused code is actually resumed, at which point termination is triggered. If execution is currently not paused, this parameter has no effect.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### search_in_content(script_id, query, case_sensitive=None, is_regex=None)

Searches for given string in script content.

* **Parameters:**
  * **script_id** ([`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)) – Id of the script to search in.
  * **query** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – String to search for.
  * **case_sensitive** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, search is case sensitive.
  * **is_regex** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, treats string parameter as regex.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SearchMatch`](#nodriver.cdp.debugger.SearchMatch)]]
* **Returns:**
  List of search matches.

### set_async_call_stack_depth(max_depth)

Enables or disables async call stacks tracking.

* **Parameters:**
  **max_depth** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Maximum depth of async call stacks. Setting to ``0`` will effectively disable collecting async call stacks (default).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_blackbox_execution_contexts(unique_ids)

Replace previous blackbox execution contexts with passed ones. Forces backend to skip
stepping/pausing in scripts in these execution contexts. VM will try to leave blackboxed script by
performing ‘step in’ several times, finally resorting to ‘step out’ if unsuccessful.

**EXPERIMENTAL**

* **Parameters:**
  **unique_ids** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – Array of execution context unique ids for the debugger to ignore.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_blackbox_patterns(patterns, skip_anonymous=None)

Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in
scripts with url matching one of the patterns. VM will try to leave blackboxed script by
performing ‘step in’ several times, finally resorting to ‘step out’ if unsuccessful.

**EXPERIMENTAL**

* **Parameters:**
  * **patterns** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – Array of regexps that will be used to check script url for blackbox state.
  * **skip_anonymous** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, also ignore scripts with no source url.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_blackboxed_ranges(script_id, positions)

Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted
scripts by performing ‘step in’ several times, finally resorting to ‘step out’ if unsuccessful.
Positions array contains positions where blackbox state is changed. First interval isn’t
blackboxed. Array should be sorted.

**EXPERIMENTAL**

* **Parameters:**
  * **script_id** ([`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)) – Id of the script.
  * **positions** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ScriptPosition`](#nodriver.cdp.debugger.ScriptPosition)]) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_breakpoint(location, condition=None)

Sets JavaScript breakpoint at a given location.

* **Parameters:**
  * **location** ([`Location`](#nodriver.cdp.debugger.Location)) – Location to set breakpoint in.
  * **condition** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`BreakpointId`](#nodriver.cdp.debugger.BreakpointId), [`Location`](#nodriver.cdp.debugger.Location)]]
* **Returns:**
  A tuple with the following items:
  1. **breakpointId** - Id of the created breakpoint for further reference.
  2. **actualLocation** - Location this breakpoint resolved into.

### set_breakpoint_by_url(line_number, url=None, url_regex=None, script_hash=None, column_number=None, condition=None)

Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this
command is issued, all existing parsed scripts will have breakpoints resolved and returned in
`locations` property. Further matching script parsing will result in subsequent
`breakpointResolved` events issued. This logical breakpoint will survive page reloads.

* **Parameters:**
  * **line_number** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Line number to set breakpoint at.
  * **url** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* URL of the resources to set breakpoint on.
  * **url_regex** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Regex pattern for the URLs of the resources to set breakpoints on. Either ``url``` or ```urlRegex`` must be specified.
  * **script_hash** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Script hash of the resources to set breakpoint on.
  * **column_number** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Offset in the line to set breakpoint at.
  * **condition** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`BreakpointId`](#nodriver.cdp.debugger.BreakpointId), [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Location`](#nodriver.cdp.debugger.Location)]]]
* **Returns:**
  A tuple with the following items:
  1. **breakpointId** - Id of the created breakpoint for further reference.
  2. **locations** - List of the locations this breakpoint resolved into upon addition.

### set_breakpoint_on_function_call(object_id, condition=None)

Sets JavaScript breakpoint before each call to the given function.
If another function was created from the same source as a given one,
calling it will also trigger the breakpoint.

**EXPERIMENTAL**

* **Parameters:**
  * **object_id** ([`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)) – Function object id.
  * **condition** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Expression to use as a breakpoint condition. When specified, debugger will stop on the breakpoint if this expression evaluates to true.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`BreakpointId`](#nodriver.cdp.debugger.BreakpointId)]
* **Returns:**
  Id of the created breakpoint for further reference.

### set_breakpoints_active(active)

Activates / deactivates all breakpoints on the page.

* **Parameters:**
  **active** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – New value for breakpoints active state.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_instrumentation_breakpoint(instrumentation)

Sets instrumentation breakpoint.

* **Parameters:**
  **instrumentation** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Instrumentation name.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`BreakpointId`](#nodriver.cdp.debugger.BreakpointId)]
* **Returns:**
  Id of the created breakpoint for further reference.

### set_pause_on_exceptions(state)

Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions,
or caught exceptions, no exceptions. Initial pause on exceptions state is `none`.

* **Parameters:**
  **state** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Pause on exceptions mode.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_return_value(new_value)

Changes return value in top frame. Available only at return break position.

**EXPERIMENTAL**

* **Parameters:**
  **new_value** ([`CallArgument`](runtime.md#nodriver.cdp.runtime.CallArgument)) – New return value.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_script_source(script_id, script_source, dry_run=None, allow_top_frame_editing=None)

Edits JavaScript source live.

In general, functions that are currently on the stack can not be edited with
a single exception: If the edited function is the top-most stack frame and
that is the only activation of that function on the stack. In this case
the live edit will be successful and a `Debugger.restartFrame` for the
top-most function is automatically triggered.

* **Parameters:**
  * **script_id** ([`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)) – Id of the script to edit.
  * **script_source** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – New content of the script.
  * **dry_run** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true the change will not actually be applied. Dry run may be used to get result description without actually modifying the code.
  * **allow_top_frame_editing** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* If true, then ``scriptSource``` is allowed to change the function on top of the stack as long as the top-most stack frame is the only activation of that function.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CallFrame`](#nodriver.cdp.debugger.CallFrame)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTrace`](runtime.md#nodriver.cdp.runtime.StackTrace)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTraceId`](runtime.md#nodriver.cdp.runtime.StackTraceId)], [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExceptionDetails`](runtime.md#nodriver.cdp.runtime.ExceptionDetails)]]]
* **Returns:**
  A tuple with the following items:
  1. **callFrames** - *(Optional)* New stack trace in case editing has happened while VM was stopped.
  2. **stackChanged** - *(Optional)* Whether current call stack  was modified after applying the changes.
  3. **asyncStackTrace** - *(Optional)* Async stack trace, if any.
  4. **asyncStackTraceId** - *(Optional)* Async stack trace, if any.
  5. **status** - Whether the operation was successful or not. Only \`\` Ok\`\` denotes a successful live edit while the other enum variants denote why the live edit failed.
  6. **exceptionDetails** - *(Optional)* Exception details if any. Only present when \`\` status\`\` is \`\` CompileError\`.

### set_skip_all_pauses(skip)

Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc).

* **Parameters:**
  **skip** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – New value for skip pauses state.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_variable_value(scope_number, variable_name, new_value, call_frame_id)

Changes value of variable in a callframe. Object-based scopes are not supported and must be
mutated manually.

* **Parameters:**
  * **scope_number** ([`int`](https://docs.python.org/3/library/functions.html#int)) – 0-based number of scope as was listed in scope chain. Only ‘local’, ‘closure’ and ‘catch’ scope types are allowed. Other scopes could be manipulated manually.
  * **variable_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Variable name.
  * **new_value** ([`CallArgument`](runtime.md#nodriver.cdp.runtime.CallArgument)) – New variable value.
  * **call_frame_id** ([`CallFrameId`](#nodriver.cdp.debugger.CallFrameId)) – Id of callframe that holds variable.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### step_into(break_on_async_call=None, skip_list=None)

Steps into the function call.

* **Parameters:**
  * **break_on_async_call** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Debugger will pause on the execution of the first async task which was scheduled before next pause.
  * **skip_list** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`LocationRange`](#nodriver.cdp.debugger.LocationRange)]]) – **(EXPERIMENTAL)** *(Optional)* The skipList specifies location ranges that should be skipped on step into.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### step_out()

Steps out of the function call.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### step_over(skip_list=None)

Steps over the statement.

* **Parameters:**
  **skip_list** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`LocationRange`](#nodriver.cdp.debugger.LocationRange)]]) – **(EXPERIMENTAL)** *(Optional)* The skipList specifies location ranges that should be skipped on step over.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* BreakpointResolved(breakpoint_id, location)

Fired when breakpoint is resolved to an actual script and location.
Deprecated in favor of `resolvedBreakpoints` in the `scriptParsed` event.

#### Deprecated
Deprecated since version 1.3.

#### breakpoint_id*: [`BreakpointId`](#nodriver.cdp.debugger.BreakpointId)*

Breakpoint unique identifier.

#### location*: [`Location`](#nodriver.cdp.debugger.Location)*

Actual breakpoint location.

### *class* Paused(call_frames, reason, data, hit_breakpoints, async_stack_trace, async_stack_trace_id, async_call_stack_trace_id)

Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria.

#### call_frames*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CallFrame`](#nodriver.cdp.debugger.CallFrame)]*

Call stack the virtual machine stopped on.

#### reason*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Pause reason.

#### data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]*

Object containing break-specific auxiliary properties.

#### hit_breakpoints*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]*

Hit breakpoints IDs

#### async_stack_trace*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTrace`](runtime.md#nodriver.cdp.runtime.StackTrace)]*

Async stack trace, if any.

#### async_stack_trace_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTraceId`](runtime.md#nodriver.cdp.runtime.StackTraceId)]*

Async stack trace, if any.

#### async_call_stack_trace_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTraceId`](runtime.md#nodriver.cdp.runtime.StackTraceId)]*

Never present, will be removed.

### *class* Resumed

Fired when the virtual machine resumed execution.

### *class* ScriptFailedToParse(script_id, url, start_line, start_column, end_line, end_column, execution_context_id, hash_, build_id, execution_context_aux_data, source_map_url, has_source_url, is_module, length, stack_trace, code_offset, script_language, embedder_name)

Fired when virtual machine fails to parse the script.

#### script_id*: [`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)*

Identifier of the script parsed.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL or name of the script parsed (if any).

#### start_line*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Line offset of the script within the resource with given URL (for script tags).

#### start_column*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Column offset of the script within the resource with given URL.

#### end_line*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Last line of the script.

#### end_column*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Length of the last line of the script.

#### execution_context_id*: [`ExecutionContextId`](runtime.md#nodriver.cdp.runtime.ExecutionContextId)*

Specifies script creation context.

#### hash_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Content hash of the script, SHA-256.

#### build_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

For Wasm modules, the content of the `build_id` custom section. For JavaScript the `debugId` magic comment.

#### execution_context_aux_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]*

‘default’\`\`’isolated’\`\`’worker’, frameId: string}

* **Type:**
  Embedder-specific auxiliary data likely matching {isDefault
* **Type:**
  boolean, [type](https://docs.python.org/3/library/functions.html#type)

#### source_map_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

URL of source map associated with script (if any).

#### has_source_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

True, if this script has sourceURL.

#### is_module*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

True, if this script is ES6 module.

#### length*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

This script length.

#### stack_trace*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTrace`](runtime.md#nodriver.cdp.runtime.StackTrace)]*

JavaScript top stack frame of where the script parsed event was triggered if available.

#### code_offset*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

If the scriptLanguage is WebAssembly, the code section offset in the module.

#### script_language*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ScriptLanguage`](#nodriver.cdp.debugger.ScriptLanguage)]*

The language of the script.

#### embedder_name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

The name the embedder supplied for this script.

### *class* ScriptParsed(script_id, url, start_line, start_column, end_line, end_column, execution_context_id, hash_, build_id, execution_context_aux_data, is_live_edit, source_map_url, has_source_url, is_module, length, stack_trace, code_offset, script_language, debug_symbols, embedder_name, resolved_breakpoints)

Fired when virtual machine parses script. This event is also fired for all known and uncollected
scripts upon enabling debugger.

#### script_id*: [`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)*

Identifier of the script parsed.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL or name of the script parsed (if any).

#### start_line*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Line offset of the script within the resource with given URL (for script tags).

#### start_column*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Column offset of the script within the resource with given URL.

#### end_line*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Last line of the script.

#### end_column*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Length of the last line of the script.

#### execution_context_id*: [`ExecutionContextId`](runtime.md#nodriver.cdp.runtime.ExecutionContextId)*

Specifies script creation context.

#### hash_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Content hash of the script, SHA-256.

#### build_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

For Wasm modules, the content of the `build_id` custom section. For JavaScript the `debugId` magic comment.

#### execution_context_aux_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]*

‘default’\`\`’isolated’\`\`’worker’, frameId: string}

* **Type:**
  Embedder-specific auxiliary data likely matching {isDefault
* **Type:**
  boolean, [type](https://docs.python.org/3/library/functions.html#type)

#### is_live_edit*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

True, if this script is generated as a result of the live edit operation.

#### source_map_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

URL of source map associated with script (if any).

#### has_source_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

True, if this script has sourceURL.

#### is_module*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

True, if this script is ES6 module.

#### length*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

This script length.

#### stack_trace*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTrace`](runtime.md#nodriver.cdp.runtime.StackTrace)]*

JavaScript top stack frame of where the script parsed event was triggered if available.

#### code_offset*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

If the scriptLanguage is WebAssembly, the code section offset in the module.

#### script_language*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ScriptLanguage`](#nodriver.cdp.debugger.ScriptLanguage)]*

The language of the script.

#### debug_symbols*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`DebugSymbols`](#nodriver.cdp.debugger.DebugSymbols)]]*

If the scriptLanguage is WebAssembly, the source of debug symbols for the module.

#### embedder_name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

The name the embedder supplied for this script.

#### resolved_breakpoints*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ResolvedBreakpoint`](#nodriver.cdp.debugger.ResolvedBreakpoint)]]*

The list of set breakpoints in this script if calls to `setBreakpointByUrl`
matches this script’s URL or hash. Clients that use this list can ignore the
`breakpointResolved` event. They are equivalent.
