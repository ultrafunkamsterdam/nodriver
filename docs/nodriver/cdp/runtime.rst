Runtime
=======

Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror objects.
Evaluation results are returned as mirror object that expose object type, string representation
and unique identifier that can be used for further object reference. Original objects are
maintained in memory unless they are either explicitly released or are released along with the
other objects in their object group.

.. module:: nodriver.cdp.runtime

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: ScriptId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SerializationOptions
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DeepSerializedValue
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RemoteObjectId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: UnserializableValue
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RemoteObject
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CustomPreview
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ObjectPreview
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PropertyPreview
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: EntryPreview
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PropertyDescriptor
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: InternalPropertyDescriptor
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PrivatePropertyDescriptor
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CallArgument
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ExecutionContextId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ExecutionContextDescription
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ExceptionDetails
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Timestamp
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TimeDelta
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CallFrame
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: StackTrace
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: UniqueDebuggerId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: StackTraceId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

Commands
--------

Each command is a generator function. The return
type ``Generator[x, y, z]`` indicates that the generator
*yields* arguments of type ``x``, it must be resumed with
an argument of type ``y``, and it returns type ``z``. In
this library, types ``x`` and ``y`` are the same for all
commands, and ``z`` is the return type you should pay attention
to. For more information, see
:ref:`Getting Started: Commands <getting-started-commands>`.

.. autofunction:: add_binding

.. autofunction:: await_promise

.. autofunction:: call_function_on

.. autofunction:: compile_script

.. autofunction:: disable

.. autofunction:: discard_console_entries

.. autofunction:: enable

.. autofunction:: evaluate

.. autofunction:: get_exception_details

.. autofunction:: get_heap_usage

.. autofunction:: get_isolate_id

.. autofunction:: get_properties

.. autofunction:: global_lexical_scope_names

.. autofunction:: query_objects

.. autofunction:: release_object

.. autofunction:: release_object_group

.. autofunction:: remove_binding

.. autofunction:: run_if_waiting_for_debugger

.. autofunction:: run_script

.. autofunction:: set_async_call_stack_depth

.. autofunction:: set_custom_object_formatter_enabled

.. autofunction:: set_max_call_stack_size_to_capture

.. autofunction:: terminate_execution

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: BindingCalled
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ConsoleAPICalled
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ExceptionRevoked
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ExceptionThrown
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ExecutionContextCreated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ExecutionContextDestroyed
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ExecutionContextsCleared
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: InspectRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
