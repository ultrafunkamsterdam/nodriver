# Runtime

Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror objects.
Evaluation results are returned as mirror object that expose object type, string representation
and unique identifier that can be used for further object reference. Original objects are
maintained in memory unless they are either explicitly released or are released along with the
other objects in their object group.

<a id="module-nodriver.cdp.runtime"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* ScriptId

Unique script identifier.

### *class* SerializationOptions(serialization, max_depth=None, additional_parameters=None)

Represents options for serialization. Overrides `generatePreview` and `returnByValue`.

#### serialization*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### max_depth*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Deep serialization depth. Default is full depth. Respected only in `deep` serialization mode.

#### additional_parameters*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]* *= None*

Embedder-specific parameters. For example if connected to V8 in Chrome these control DOM
serialization via `maxNodeDepth: integer` and `includeShadowTree: "none" `` "open" `` "all"`.
Values can be only of type string or integer.

### *class* DeepSerializedValue(type_, value=None, object_id=None, weak_local_object_reference=None)

Represents deep serialized value.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]* *= None*

#### object_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### weak_local_object_reference*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Set if value reference met more then once during serialization. In such
case, value is provided only to one of the serialized values. Unique
per value in the scope of one CDP call.

### *class* RemoteObjectId

Unique object identifier.

### *class* UnserializableValue

Primitive value which cannot be JSON-stringified. Includes values `-0`, `NaN`, `Infinity`,
`-Infinity`, and bigint literals.

### *class* RemoteObject(type_, subtype=None, class_name=None, value=None, unserializable_value=None, description=None, deep_serialized_value=None, object_id=None, preview=None, custom_preview=None)

Mirror object referencing original JavaScript object.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Object type.

#### subtype*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Object subtype hint. Specified for `object` type values only.
NOTE: If you change anything here, make sure to also update
`subtype` in `ObjectPreview` and `PropertyPreview` below.

#### class_name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Object class (constructor) name. Specified for `object` type values only.

#### value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]* *= None*

Remote object value in case of primitive values or JSON values (if it was requested).

#### unserializable_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`UnserializableValue`](#nodriver.cdp.runtime.UnserializableValue)]* *= None*

Primitive value which can not be JSON-stringified does not have `value`, but gets this
property.

#### description*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

String representation of the object.

#### deep_serialized_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`DeepSerializedValue`](#nodriver.cdp.runtime.DeepSerializedValue)]* *= None*

Deep serialized value.

#### object_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](#nodriver.cdp.runtime.RemoteObjectId)]* *= None*

Unique object identifier (for non-primitive values).

#### preview*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ObjectPreview`](#nodriver.cdp.runtime.ObjectPreview)]* *= None*

Preview containing abbreviated property values. Specified for `object` type values only.

#### custom_preview*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CustomPreview`](#nodriver.cdp.runtime.CustomPreview)]* *= None*

### *class* CustomPreview(header, body_getter_id=None)

#### header*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The JSON-stringified result of formatter.header(object, config) call.
It contains json ML array that represents RemoteObject.

#### body_getter_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](#nodriver.cdp.runtime.RemoteObjectId)]* *= None*

If formatter returns true as a result of formatter.hasBody call then bodyGetterId will
contain RemoteObjectId for the function that returns result of formatter.body(object, config) call.
The result value is json ML array.

### *class* ObjectPreview(type_, overflow, properties, subtype=None, description=None, entries=None)

Object containing abbreviated remote object value.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Object type.

#### overflow*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True iff some of the properties or entries of the original object did not fit.

#### properties*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PropertyPreview`](#nodriver.cdp.runtime.PropertyPreview)]*

List of the properties.

#### subtype*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Object subtype hint. Specified for `object` type values only.

#### description*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

String representation of the object.

#### entries*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`EntryPreview`](#nodriver.cdp.runtime.EntryPreview)]]* *= None*

List of the entries. Specified for `map` and `set` subtype values only.

### *class* PropertyPreview(name, type_, value=None, value_preview=None, subtype=None)

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Property name.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Object type. Accessor means that the property itself is an accessor property.

#### value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

User-friendly property value string.

#### value_preview*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ObjectPreview`](#nodriver.cdp.runtime.ObjectPreview)]* *= None*

Nested value preview.

#### subtype*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Object subtype hint. Specified for `object` type values only.

### *class* EntryPreview(value, key=None)

#### value*: [`ObjectPreview`](#nodriver.cdp.runtime.ObjectPreview)*

Preview of the value.

#### key*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ObjectPreview`](#nodriver.cdp.runtime.ObjectPreview)]* *= None*

Preview of the key. Specified for map-like collection entries.

### *class* PropertyDescriptor(name, configurable, enumerable, value=None, writable=None, get=None, set_=None, was_thrown=None, is_own=None, symbol=None)

Object property descriptor.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Property name or symbol description.

#### configurable*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if the type of this property descriptor may be changed and if the property may be
deleted from the corresponding object.

#### enumerable*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if this property shows up during enumeration of the properties on the corresponding
object.

#### value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject)]* *= None*

The value associated with the property.

#### writable*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if the value associated with the property may be changed (data descriptors only).

#### get*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject)]* *= None*

A function which serves as a getter for the property, or `undefined` if there is no getter
(accessor descriptors only).

#### set_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject)]* *= None*

A function which serves as a setter for the property, or `undefined` if there is no setter
(accessor descriptors only).

#### was_thrown*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if the result was thrown during the evaluation.

#### is_own*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if the property is owned for the object.

#### symbol*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject)]* *= None*

Property symbol object, if the property is of the `symbol` type.

### *class* InternalPropertyDescriptor(name, value=None)

Object internal property descriptor. This property isn’t normally visible in JavaScript code.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Conventional property name.

#### value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject)]* *= None*

The value associated with the property.

### *class* PrivatePropertyDescriptor(name, value=None, get=None, set_=None)

Object private field descriptor.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Private property name.

#### value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject)]* *= None*

The value associated with the private property.

#### get*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject)]* *= None*

A function which serves as a getter for the private property,
or `undefined` if there is no getter (accessor descriptors only).

#### set_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject)]* *= None*

A function which serves as a setter for the private property,
or `undefined` if there is no setter (accessor descriptors only).

### *class* CallArgument(value=None, unserializable_value=None, object_id=None)

Represents function call argument. Either remote object id `objectId`, primitive `value`,
unserializable primitive value or neither of (for undefined) them should be specified.

#### value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]* *= None*

Primitive value or serializable javascript object.

#### unserializable_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`UnserializableValue`](#nodriver.cdp.runtime.UnserializableValue)]* *= None*

Primitive value which can not be JSON-stringified.

#### object_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](#nodriver.cdp.runtime.RemoteObjectId)]* *= None*

Remote object handle.

### *class* ExecutionContextId

Id of an execution context.

### *class* ExecutionContextDescription(id_, origin, name, unique_id, aux_data=None)

Description of an isolated world.

#### id_*: [`ExecutionContextId`](#nodriver.cdp.runtime.ExecutionContextId)*

Unique id of the execution context. It can be used to specify in which execution context
script evaluation should be performed.

#### origin*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Execution context origin.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Human readable name describing given context.

#### unique_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

A system-unique execution context identifier. Unlike the id, this is unique across
multiple processes, so can be reliably used to identify specific context while backend
performs a cross-process navigation.

#### aux_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]* *= None*

‘default’\`\`’isolated’\`\`’worker’, frameId: string}

* **Type:**
  Embedder-specific auxiliary data likely matching {isDefault
* **Type:**
  boolean, [type](https://docs.python.org/3/library/functions.html#type)

### *class* ExceptionDetails(exception_id, text, line_number, column_number, script_id=None, url=None, stack_trace=None, exception=None, execution_context_id=None, exception_meta_data=None)

Detailed information about exception (or error) that was thrown during script compilation or
execution.

#### exception_id*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Exception id.

#### text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Exception text, which should be used together with exception object when available.

#### line_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Line number of the exception location (0-based).

#### column_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Column number of the exception location (0-based).

#### script_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ScriptId`](#nodriver.cdp.runtime.ScriptId)]* *= None*

Script ID of the exception location.

#### url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

URL of the exception location, to be used when the script was not reported.

#### stack_trace*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTrace`](#nodriver.cdp.runtime.StackTrace)]* *= None*

JavaScript stack trace if available.

#### exception*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject)]* *= None*

Exception object if available.

#### execution_context_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExecutionContextId`](#nodriver.cdp.runtime.ExecutionContextId)]* *= None*

Identifier of the context where exception happened.

#### exception_meta_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]* *= None*

Dictionary with entries of meta data that the client associated
with this exception, such as information about associated network
requests, etc.

### *class* Timestamp(x=0, /)

Number of milliseconds since epoch.

### *class* TimeDelta(x=0, /)

Number of milliseconds.

### *class* CallFrame(function_name, script_id, url, line_number, column_number)

Stack entry for runtime errors and assertions.

#### function_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

JavaScript function name.

#### script_id*: [`ScriptId`](#nodriver.cdp.runtime.ScriptId)*

JavaScript script id.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

JavaScript script name or url.

#### line_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

JavaScript script line number (0-based).

#### column_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

JavaScript script column number (0-based).

### *class* StackTrace(call_frames, description=None, parent=None, parent_id=None)

Call frames for assertions or error messages.

#### call_frames*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CallFrame`](#nodriver.cdp.runtime.CallFrame)]*

JavaScript function name.

#### description*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

String label of this stack trace. For async traces this may be a name of the function that
initiated the async call.

#### parent*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTrace`](#nodriver.cdp.runtime.StackTrace)]* *= None*

Asynchronous JavaScript stack trace that preceded this stack, if available.

#### parent_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTraceId`](#nodriver.cdp.runtime.StackTraceId)]* *= None*

Asynchronous JavaScript stack trace that preceded this stack, if available.

### *class* UniqueDebuggerId

Unique identifier of current debugger.

### *class* StackTraceId(id_, debugger_id=None)

If `debuggerId` is set stack trace comes from another debugger and can be resolved there. This
allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages.

#### id_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### debugger_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`UniqueDebuggerId`](#nodriver.cdp.runtime.UniqueDebuggerId)]* *= None*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### add_binding(name, execution_context_id=None, execution_context_name=None)

If executionContextId is empty, adds binding with the given name on the
global objects of all inspected contexts, including those created later,
bindings survive reloads.
Binding function takes exactly one argument, this argument should be string,
in case of any other input, function throws an exception.
Each binding function call produces Runtime.bindingCalled notification.

* **Parameters:**
  * **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **execution_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExecutionContextId`](#nodriver.cdp.runtime.ExecutionContextId)]) – **(DEPRECATED)** **(EXPERIMENTAL)** *(Optional)* If specified, the binding would only be exposed to the specified execution context. If omitted and ``executionContextName``` is not set, the binding is exposed to all execution contexts of the target. This parameter is mutually exclusive with ```executionContextName```. Deprecated in favor of ```executionContextName``` due to an unclear use case and bugs in implementation (crbug.com/1169639). ```executionContextId``` will be removed in the future.
  * **execution_context_name** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If specified, the binding is exposed to the executionContext with matching name, even for contexts created after the binding is added. See also ```ExecutionContext.name``` and ```worldName``` parameter to ```Page.addScriptToEvaluateOnNewDocument```. This parameter is mutually exclusive with ```executionContextId``.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### await_promise(promise_object_id, return_by_value=None, generate_preview=None)

Add handler to promise with given promise object id.

* **Parameters:**
  * **promise_object_id** ([`RemoteObjectId`](#nodriver.cdp.runtime.RemoteObjectId)) – Identifier of the promise.
  * **return_by_value** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether the result is expected to be a JSON object that should be sent by value.
  * **generate_preview** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether preview should be generated for the result.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExceptionDetails`](#nodriver.cdp.runtime.ExceptionDetails)]]]
* **Returns:**
  A tuple with the following items:
  1. **result** - Promise result. Will contain rejected value if promise was rejected.
  2. **exceptionDetails** - *(Optional)* Exception details if stack strace is available.

### call_function_on(function_declaration, object_id=None, arguments=None, silent=None, return_by_value=None, generate_preview=None, user_gesture=None, await_promise=None, execution_context_id=None, object_group=None, throw_on_side_effect=None, unique_context_id=None, serialization_options=None)

Calls function with given declaration on the given object. Object group of the result is
inherited from the target object.

* **Parameters:**
  * **function_declaration** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Declaration of the function to call.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* Identifier of the object to call function on. Either objectId or executionContextId should be specified.
  * **arguments** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CallArgument`](#nodriver.cdp.runtime.CallArgument)]]) – *(Optional)* Call arguments. All call arguments must belong to the same JavaScript world as the target object.
  * **silent** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides ``setPauseOnException``` state.
  * **return_by_value** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether the result is expected to be a JSON object which should be sent by value. Can be overriden by ```serializationOptions```.
  * **generate_preview** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether preview should be generated for the result.
  * **user_gesture** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether execution should be treated as initiated by user in the UI.
  * **await_promise** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether execution should ```await``` for resulting value and return once awaited promise is resolved.
  * **execution_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExecutionContextId`](#nodriver.cdp.runtime.ExecutionContextId)]) – *(Optional)* Specifies execution context which global object will be used to call function on. Either executionContextId or objectId should be specified.
  * **object_group** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Symbolic group name that can be used to release multiple objects. If objectGroup is not specified and objectId is, objectGroup will be inherited from object.
  * **throw_on_side_effect** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether to throw an exception if side effect cannot be ruled out during evaluation.
  * **unique_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* An alternative way to specify the execution context to call function on. Compared to contextId that may be reused across processes, this is guaranteed to be system-unique, so it can be used to prevent accidental function call in context different than intended (e.g. as a result of navigation across process boundaries). This is mutually exclusive with ```executionContextId```.
  * **serialization_options** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SerializationOptions`](#nodriver.cdp.runtime.SerializationOptions)]) – **(EXPERIMENTAL)** *(Optional)* Specifies the result serialization. If provided, overrides ```generatePreview``` and ```returnByValue``.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExceptionDetails`](#nodriver.cdp.runtime.ExceptionDetails)]]]
* **Returns:**
  A tuple with the following items:
  1. **result** - Call result.
  2. **exceptionDetails** - *(Optional)* Exception details.

### compile_script(expression, source_url, persist_script, execution_context_id=None)

Compiles expression.

* **Parameters:**
  * **expression** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Expression to compile.
  * **source_url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Source url to be set for the script.
  * **persist_script** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Specifies whether the compiled script should be persisted.
  * **execution_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExecutionContextId`](#nodriver.cdp.runtime.ExecutionContextId)]) – *(Optional)* Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ScriptId`](#nodriver.cdp.runtime.ScriptId)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExceptionDetails`](#nodriver.cdp.runtime.ExceptionDetails)]]]
* **Returns:**
  A tuple with the following items:
  1. **scriptId** - *(Optional)* Id of the script.
  2. **exceptionDetails** - *(Optional)* Exception details.

### disable()

Disables reporting of execution contexts creation.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### discard_console_entries()

Discards collected exceptions and console API calls.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables reporting of execution contexts creation by means of `executionContextCreated` event.
When the reporting gets enabled the event will be sent immediately for each existing execution
context.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### evaluate(expression, object_group=None, include_command_line_api=None, silent=None, context_id=None, return_by_value=None, generate_preview=None, user_gesture=None, await_promise=None, throw_on_side_effect=None, timeout=None, disable_breaks=None, repl_mode=None, allow_unsafe_eval_blocked_by_csp=None, unique_context_id=None, serialization_options=None)

Evaluates expression on global object.

* **Parameters:**
  * **expression** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Expression to evaluate.
  * **object_group** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Symbolic group name that can be used to release multiple objects.
  * **include_command_line_api** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Determines whether Command Line API should be available during the evaluation.
  * **silent** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides ``setPauseOnException``` state.
  * **context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExecutionContextId`](#nodriver.cdp.runtime.ExecutionContextId)]) – *(Optional)* Specifies in which execution context to perform evaluation. If the parameter is omitted the evaluation will be performed in the context of the inspected page. This is mutually exclusive with ```uniqueContextId```, which offers an alternative way to identify the execution context that is more reliable in a multi-process environment.
  * **return_by_value** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether the result is expected to be a JSON object that should be sent by value.
  * **generate_preview** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether preview should be generated for the result.
  * **user_gesture** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether execution should be treated as initiated by user in the UI.
  * **await_promise** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether execution should ```await``` for resulting value and return once awaited promise is resolved.
  * **throw_on_side_effect** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether to throw an exception if side effect cannot be ruled out during evaluation. This implies ```disableBreaks``` below.
  * **timeout** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeDelta`](#nodriver.cdp.runtime.TimeDelta)]) – **(EXPERIMENTAL)** *(Optional)* Terminate execution after timing out (number of milliseconds).
  * **disable_breaks** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Disable breakpoints during execution.
  * **repl_mode** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Setting this flag to true enables ```let``` re-declaration and top-level ```await```. Note that ```let``` variables can only be re-declared if they originate from ```replMode``` themselves.
  * **allow_unsafe_eval_blocked_by_csp** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* The Content Security Policy (CSP) for the target might block ‘unsafe-eval’ which includes eval(), Function(), setTimeout() and setInterval() when called with non-callable arguments. This flag bypasses CSP for this evaluation and allows unsafe-eval. Defaults to true.
  * **unique_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* An alternative way to specify the execution context to evaluate in. Compared to contextId that may be reused across processes, this is guaranteed to be system-unique, so it can be used to prevent accidental evaluation of the expression in context different than intended (e.g. as a result of navigation across process boundaries). This is mutually exclusive with ```contextId```.
  * **serialization_options** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SerializationOptions`](#nodriver.cdp.runtime.SerializationOptions)]) – **(EXPERIMENTAL)** *(Optional)* Specifies the result serialization. If provided, overrides ```generatePreview``` and ```returnByValue``.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExceptionDetails`](#nodriver.cdp.runtime.ExceptionDetails)]]]
* **Returns:**
  A tuple with the following items:
  1. **result** - Evaluation result.
  2. **exceptionDetails** - *(Optional)* Exception details.

### get_exception_details(error_object_id)

This method tries to lookup and populate exception details for a
JavaScript Error object.
Note that the stackTrace portion of the resulting exceptionDetails will
only be populated if the Runtime domain was enabled at the time when the
Error was thrown.

**EXPERIMENTAL**

* **Parameters:**
  **error_object_id** ([`RemoteObjectId`](#nodriver.cdp.runtime.RemoteObjectId)) – The error object for which to resolve the exception details.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExceptionDetails`](#nodriver.cdp.runtime.ExceptionDetails)]]
* **Returns:**

### get_heap_usage()

Returns the JavaScript heap usage.
It is the total usage of the corresponding isolate not scoped to a particular Runtime.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`float`](https://docs.python.org/3/library/functions.html#float), [`float`](https://docs.python.org/3/library/functions.html#float), [`float`](https://docs.python.org/3/library/functions.html#float), [`float`](https://docs.python.org/3/library/functions.html#float)]]
* **Returns:**
  A tuple with the following items:
  1. **usedSize** - Used JavaScript heap size in bytes.
  2. **totalSize** - Allocated JavaScript heap size in bytes.
  3. **embedderHeapUsedSize** - Used size in bytes in the embedder’s garbage-collected heap.
  4. **backingStorageSize** - Size in bytes of backing storage for array buffers and external strings.

### get_isolate_id()

Returns the isolate id.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**
  The isolate id.

### get_properties(object_id, own_properties=None, accessor_properties_only=None, generate_preview=None, non_indexed_properties_only=None)

Returns properties of a given object. Object group of the result is inherited from the target
object.

* **Parameters:**
  * **object_id** ([`RemoteObjectId`](#nodriver.cdp.runtime.RemoteObjectId)) – Identifier of the object to return properties for.
  * **own_properties** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, returns properties belonging only to the element itself, not to its prototype chain.
  * **accessor_properties_only** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* If true, returns accessor properties (with getter/setter) only; internal properties are not returned either.
  * **generate_preview** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether preview should be generated for the results.
  * **non_indexed_properties_only** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* If true, returns non-indexed properties only.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PropertyDescriptor`](#nodriver.cdp.runtime.PropertyDescriptor)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`InternalPropertyDescriptor`](#nodriver.cdp.runtime.InternalPropertyDescriptor)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PrivatePropertyDescriptor`](#nodriver.cdp.runtime.PrivatePropertyDescriptor)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExceptionDetails`](#nodriver.cdp.runtime.ExceptionDetails)]]]
* **Returns:**
  A tuple with the following items:
  1. **result** - Object properties.
  2. **internalProperties** - *(Optional)* Internal object properties (only of the element itself).
  3. **privateProperties** - *(Optional)* Object private properties.
  4. **exceptionDetails** - *(Optional)* Exception details.

### global_lexical_scope_names(execution_context_id=None)

Returns all let, const and class variables from global scope.

* **Parameters:**
  **execution_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExecutionContextId`](#nodriver.cdp.runtime.ExecutionContextId)]) – *(Optional)* Specifies in which execution context to lookup global scope variables.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**

### query_objects(prototype_object_id, object_group=None)

* **Parameters:**
  * **prototype_object_id** ([`RemoteObjectId`](#nodriver.cdp.runtime.RemoteObjectId)) – Identifier of the prototype to return objects for.
  * **object_group** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Symbolic group name that can be used to release the results.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`RemoteObject`](#nodriver.cdp.runtime.RemoteObject)]
* **Returns:**
  Array with objects.

### release_object(object_id)

Releases remote object with given id.

* **Parameters:**
  **object_id** ([`RemoteObjectId`](#nodriver.cdp.runtime.RemoteObjectId)) – Identifier of the object to release.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### release_object_group(object_group)

Releases all remote objects that belong to a given group.

* **Parameters:**
  **object_group** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Symbolic object group name.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### remove_binding(name)

This method does not remove binding function from global object but
unsubscribes current runtime agent from Runtime.bindingCalled notifications.

* **Parameters:**
  **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### run_if_waiting_for_debugger()

Tells inspected instance to run if it was waiting for debugger to attach.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### run_script(script_id, execution_context_id=None, object_group=None, silent=None, include_command_line_api=None, return_by_value=None, generate_preview=None, await_promise=None)

Runs script with given id in a given context.

* **Parameters:**
  * **script_id** ([`ScriptId`](#nodriver.cdp.runtime.ScriptId)) – Id of the script to run.
  * **execution_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExecutionContextId`](#nodriver.cdp.runtime.ExecutionContextId)]) – *(Optional)* Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
  * **object_group** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Symbolic group name that can be used to release multiple objects.
  * **silent** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides ``setPauseOnException``` state.
  * **include_command_line_api** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Determines whether Command Line API should be available during the evaluation.
  * **return_by_value** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether the result is expected to be a JSON object which should be sent by value.
  * **generate_preview** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether preview should be generated for the result.
  * **await_promise** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether execution should ```await`` for resulting value and return once awaited promise is resolved.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExceptionDetails`](#nodriver.cdp.runtime.ExceptionDetails)]]]
* **Returns:**
  A tuple with the following items:
  1. **result** - Run result.
  2. **exceptionDetails** - *(Optional)* Exception details.

### set_async_call_stack_depth(max_depth)

Enables or disables async call stacks tracking.

* **Parameters:**
  **max_depth** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Maximum depth of async call stacks. Setting to ``0`` will effectively disable collecting async call stacks (default).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_custom_object_formatter_enabled(enabled)

**EXPERIMENTAL**

* **Parameters:**
  **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_max_call_stack_size_to_capture(size)

**EXPERIMENTAL**

* **Parameters:**
  **size** ([`int`](https://docs.python.org/3/library/functions.html#int)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### terminate_execution()

Terminate current or next JavaScript execution.
Will cancel the termination when the outer-most script execution ends.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* BindingCalled(name, payload, execution_context_id)

**EXPERIMENTAL**

Notification is issued every time when binding is called.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### payload*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### execution_context_id*: [`ExecutionContextId`](#nodriver.cdp.runtime.ExecutionContextId)*

Identifier of the context where the call was made.

### *class* ConsoleAPICalled(type_, args, execution_context_id, timestamp, stack_trace, context)

Issued when console API was called.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Type of the call.

#### args*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`RemoteObject`](#nodriver.cdp.runtime.RemoteObject)]*

Call arguments.

#### execution_context_id*: [`ExecutionContextId`](#nodriver.cdp.runtime.ExecutionContextId)*

Identifier of the context where the call was made.

#### timestamp*: [`Timestamp`](#nodriver.cdp.runtime.Timestamp)*

Call timestamp.

#### stack_trace*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTrace`](#nodriver.cdp.runtime.StackTrace)]*

Stack trace captured when the call was made. The async stack chain is automatically reported for
the following call types: `assert`, `error`, `trace`, `warning`. For other types the async call
chain can be retrieved using `Debugger.getStackTrace` and `stackTrace.parentId` field.

#### context*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Console context descriptor for calls on non-default console context (not console.\*):
‘anonymous#unique-logger-id’ for call on unnamed context, ‘name#unique-logger-id’ for call
on named context.

### *class* ExceptionRevoked(reason, exception_id)

Issued when unhandled exception was revoked.

#### reason*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Reason describing why exception was revoked.

#### exception_id*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The id of revoked exception, as reported in `exceptionThrown`.

### *class* ExceptionThrown(timestamp, exception_details)

Issued when exception was thrown and unhandled.

#### timestamp*: [`Timestamp`](#nodriver.cdp.runtime.Timestamp)*

Timestamp of the exception.

#### exception_details*: [`ExceptionDetails`](#nodriver.cdp.runtime.ExceptionDetails)*

### *class* ExecutionContextCreated(context)

Issued when new execution context is created.

#### context*: [`ExecutionContextDescription`](#nodriver.cdp.runtime.ExecutionContextDescription)*

A newly created execution context.

### *class* ExecutionContextDestroyed(execution_context_id, execution_context_unique_id)

Issued when execution context is destroyed.

#### execution_context_id*: [`ExecutionContextId`](#nodriver.cdp.runtime.ExecutionContextId)*

Id of the destroyed context

#### execution_context_unique_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Unique Id of the destroyed context

### *class* ExecutionContextsCleared

Issued when all executionContexts were cleared in browser

### *class* InspectRequested(object_, hints, execution_context_id)

Issued when object should be inspected (for example, as a result of inspect() command line API
call).

#### object_*: [`RemoteObject`](#nodriver.cdp.runtime.RemoteObject)*

#### hints*: [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)*

#### execution_context_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExecutionContextId`](#nodriver.cdp.runtime.ExecutionContextId)]*

Identifier of the context where the call was made.
