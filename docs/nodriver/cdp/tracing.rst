Tracing
=======

.. module:: nodriver.cdp.tracing

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: MemoryDumpConfig
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TraceConfig
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: StreamFormat
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: StreamCompression
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: MemoryDumpLevelOfDetail
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TracingBackend
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

.. autofunction:: end

.. autofunction:: get_categories

.. autofunction:: record_clock_sync_marker

.. autofunction:: request_memory_dump

.. autofunction:: start

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: BufferUsage
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DataCollected
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TracingComplete
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
