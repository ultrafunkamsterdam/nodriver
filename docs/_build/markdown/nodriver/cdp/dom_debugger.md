# DOMDebugger

DOM debugging allows setting breakpoints on particular DOM operations and events. JavaScript
execution will stop on these operations as if there was a regular breakpoint set.

<a id="module-nodriver.cdp.dom_debugger"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* DOMBreakpointType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

DOM breakpoint type.

#### SUBTREE_MODIFIED *= 'subtree-modified'*

#### ATTRIBUTE_MODIFIED *= 'attribute-modified'*

#### NODE_REMOVED *= 'node-removed'*

### *class* CSPViolationType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

CSP Violation type.

#### TRUSTEDTYPE_SINK_VIOLATION *= 'trustedtype-sink-violation'*

#### TRUSTEDTYPE_POLICY_VIOLATION *= 'trustedtype-policy-violation'*

### *class* EventListener(type_, use_capture, passive, once, script_id, line_number, column_number, handler=None, original_handler=None, backend_node_id=None)

Object event listener.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`EventListener`’s type.

#### use_capture*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

`EventListener`’s useCapture.

#### passive*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

`EventListener`’s passive flag.

#### once*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

`EventListener`’s once flag.

#### script_id*: [`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)*

Script id of the handler code.

#### line_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Line number in the script (0-based).

#### column_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Column number in the script (0-based).

#### handler*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObject`](runtime.md#nodriver.cdp.runtime.RemoteObject)]* *= None*

Event handler function value.

#### original_handler*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObject`](runtime.md#nodriver.cdp.runtime.RemoteObject)]* *= None*

Event original handler function value.

#### backend_node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

Node the listener is added to (if any).

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### get_event_listeners(object_id, depth=None, pierce=None)

Returns event listeners of the given object.

* **Parameters:**
  * **object_id** ([`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)) – Identifier of the object to return listeners for.
  * **depth** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
  * **pierce** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false). Reports listeners for all contexts if pierce is enabled.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`EventListener`](#nodriver.cdp.dom_debugger.EventListener)]]
* **Returns:**
  Array of relevant listeners.

### remove_dom_breakpoint(node_id, type_)

Removes DOM breakpoint that was set using `setDOMBreakpoint`.

* **Parameters:**
  * **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – Identifier of the node to remove breakpoint from.
  * **type** – Type of the breakpoint to remove.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### remove_event_listener_breakpoint(event_name, target_name=None)

Removes breakpoint on particular DOM event.

* **Parameters:**
  * **event_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Event name.
  * **target_name** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* EventTarget interface name.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### remove_instrumentation_breakpoint(event_name)

Removes breakpoint on particular native event.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  **event_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Instrumentation name to stop on.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### remove_xhr_breakpoint(url)

Removes breakpoint from XMLHttpRequest.

* **Parameters:**
  **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Resource URL substring.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_break_on_csp_violation(violation_types)

Sets breakpoint on particular CSP violations.

**EXPERIMENTAL**

* **Parameters:**
  **violation_types** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSPViolationType`](#nodriver.cdp.dom_debugger.CSPViolationType)]) – CSP Violations to stop upon.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_dom_breakpoint(node_id, type_)

Sets breakpoint on particular operation with DOM.

* **Parameters:**
  * **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – Identifier of the node to set breakpoint on.
  * **type** – Type of the operation to stop upon.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_event_listener_breakpoint(event_name, target_name=None)

Sets breakpoint on particular DOM event.

* **Parameters:**
  * **event_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – DOM Event name to stop on (any DOM event will do).
  * **target_name** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* EventTarget interface name to stop on. If equal to ``"*"`` or not provided, will stop on any EventTarget.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_instrumentation_breakpoint(event_name)

Sets breakpoint on particular native event.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  **event_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Instrumentation name to stop on.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### set_xhr_breakpoint(url)

Sets breakpoint on XMLHttpRequest.

* **Parameters:**
  **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Resource URL substring. All XHRs having this substring in the URL will get stopped upon.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

*There are no events in this module.*
