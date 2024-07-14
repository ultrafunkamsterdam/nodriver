HeapProfiler
============

*This CDP domain is experimental.*

.. module:: nodriver.cdp.heap_profiler

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: HeapSnapshotObjectId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SamplingHeapProfileNode
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SamplingHeapProfileSample
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SamplingHeapProfile
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

.. autofunction:: add_inspected_heap_object

.. autofunction:: collect_garbage

.. autofunction:: disable

.. autofunction:: enable

.. autofunction:: get_heap_object_id

.. autofunction:: get_object_by_heap_object_id

.. autofunction:: get_sampling_profile

.. autofunction:: start_sampling

.. autofunction:: start_tracking_heap_objects

.. autofunction:: stop_sampling

.. autofunction:: stop_tracking_heap_objects

.. autofunction:: take_heap_snapshot

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: AddHeapSnapshotChunk
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: HeapStatsUpdate
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: LastSeenObjectId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReportHeapSnapshotProgress
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ResetProfiles
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
