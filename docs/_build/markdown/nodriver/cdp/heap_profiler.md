# HeapProfiler

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.heap_profiler"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* HeapSnapshotObjectId

Heap snapshot object id.

### *class* SamplingHeapProfileNode(call_frame, self_size, id_, children)

Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes.

#### call_frame*: [`CallFrame`](runtime.md#nodriver.cdp.runtime.CallFrame)*

Function location.

#### self_size*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Allocations size in bytes for the node excluding children.

#### id_*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Node id. Ids are unique across all profiles collected between startSampling and stopSampling.

#### children*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SamplingHeapProfileNode`](#nodriver.cdp.heap_profiler.SamplingHeapProfileNode)]*

Child nodes.

### *class* SamplingHeapProfileSample(size, node_id, ordinal)

A single sample from a sampling profile.

#### size*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Allocation size in bytes attributed to the sample.

#### node_id*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Id of the corresponding profile tree node.

#### ordinal*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Time-ordered sample ordinal number. It is unique across all profiles retrieved
between startSampling and stopSampling.

### *class* SamplingHeapProfile(head, samples)

Sampling profile.

#### head*: [`SamplingHeapProfileNode`](#nodriver.cdp.heap_profiler.SamplingHeapProfileNode)*

#### samples*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SamplingHeapProfileSample`](#nodriver.cdp.heap_profiler.SamplingHeapProfileSample)]*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### add_inspected_heap_object(heap_object_id)

Enables console to refer to the node with given id via $x (see Command Line API for more details
$x functions).

* **Parameters:**
  **heap_object_id** ([`HeapSnapshotObjectId`](#nodriver.cdp.heap_profiler.HeapSnapshotObjectId)) – Heap snapshot object id to be accessible by means of $x command line API.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### collect_garbage()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### disable()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_heap_object_id(object_id)

* **Parameters:**
  **object_id** ([`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)) – Identifier of the object to get heap object id for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`HeapSnapshotObjectId`](#nodriver.cdp.heap_profiler.HeapSnapshotObjectId)]
* **Returns:**
  Id of the heap snapshot object corresponding to the passed remote object id.

### get_object_by_heap_object_id(object_id, object_group=None)

* **Parameters:**
  * **object_id** ([`HeapSnapshotObjectId`](#nodriver.cdp.heap_profiler.HeapSnapshotObjectId)) – 
  * **object_group** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Symbolic group name that can be used to release multiple objects.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`RemoteObject`](runtime.md#nodriver.cdp.runtime.RemoteObject)]
* **Returns:**
  Evaluation result.

### get_sampling_profile()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SamplingHeapProfile`](#nodriver.cdp.heap_profiler.SamplingHeapProfile)]
* **Returns:**
  Return the sampling profile being collected.

### start_sampling(sampling_interval=None, include_objects_collected_by_major_gc=None, include_objects_collected_by_minor_gc=None)

* **Parameters:**
  * **sampling_interval** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Average sample interval in bytes. Poisson distribution is used for the intervals. The default value is 32768 bytes.
  * **include_objects_collected_by_major_gc** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* By default, the sampling heap profiler reports only objects which are still alive when the profile is returned via getSamplingProfile or stopSampling, which is useful for determining what functions contribute the most to steady-state memory usage. This flag instructs the sampling heap profiler to also include information about objects discarded by major GC, which will show which functions cause large temporary memory usage or long GC pauses.
  * **include_objects_collected_by_minor_gc** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* By default, the sampling heap profiler reports only objects which are still alive when the profile is returned via getSamplingProfile or stopSampling, which is useful for determining what functions contribute the most to steady-state memory usage. This flag instructs the sampling heap profiler to also include information about objects discarded by minor GC, which is useful when tuning a latency-sensitive application for minimal GC activity.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### start_tracking_heap_objects(track_allocations=None)

* **Parameters:**
  **track_allocations** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)*
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### stop_sampling()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SamplingHeapProfile`](#nodriver.cdp.heap_profiler.SamplingHeapProfile)]
* **Returns:**
  Recorded sampling heap profile.

### stop_tracking_heap_objects(report_progress=None, treat_global_objects_as_roots=None, capture_numeric_value=None, expose_internals=None)

* **Parameters:**
  * **report_progress** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true ‘reportHeapSnapshotProgress’ events will be generated while snapshot is being taken when the tracking is stopped.
  * **treat_global_objects_as_roots** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(DEPRECATED)** *(Optional)* Deprecated in favor of ``exposeInternals``.
  * **capture_numeric_value** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, numerical values are included in the snapshot
  * **expose_internals** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* If true, exposes internals of the snapshot.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### take_heap_snapshot(report_progress=None, treat_global_objects_as_roots=None, capture_numeric_value=None, expose_internals=None)

* **Parameters:**
  * **report_progress** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true ‘reportHeapSnapshotProgress’ events will be generated while snapshot is being taken.
  * **treat_global_objects_as_roots** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(DEPRECATED)** *(Optional)* If true, a raw snapshot without artificial roots will be generated. Deprecated in favor of ``exposeInternals``.
  * **capture_numeric_value** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, numerical values are included in the snapshot
  * **expose_internals** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* If true, exposes internals of the snapshot.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* AddHeapSnapshotChunk(chunk)

#### chunk*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* HeapStatsUpdate(stats_update)

If heap objects tracking has been started then backend may send update for one or more fragments

#### stats_update*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

An array of triplets. Each triplet describes a fragment. The first integer is the fragment
index, the second integer is a total count of objects for the fragment, the third integer is
a total size of the objects for the fragment.

### *class* LastSeenObjectId(last_seen_object_id, timestamp)

If heap objects tracking has been started then backend regularly sends a current value for last
seen object id and corresponding timestamp. If the were changes in the heap since last event
then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event.

#### last_seen_object_id*: [`int`](https://docs.python.org/3/library/functions.html#int)*

#### timestamp*: [`float`](https://docs.python.org/3/library/functions.html#float)*

### *class* ReportHeapSnapshotProgress(done, total, finished)

#### done*: [`int`](https://docs.python.org/3/library/functions.html#int)*

#### total*: [`int`](https://docs.python.org/3/library/functions.html#int)*

#### finished*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

### *class* ResetProfiles
