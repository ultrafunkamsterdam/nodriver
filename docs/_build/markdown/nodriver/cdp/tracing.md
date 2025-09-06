# Tracing

* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* MemoryDumpConfig

Configuration for memory dump. Used only when “memory-infra” category is enabled.

### *class* TraceConfig(record_mode=None, trace_buffer_size_in_kb=None, enable_sampling=None, enable_systrace=None, enable_argument_filter=None, included_categories=None, excluded_categories=None, synthetic_delays=None, memory_dump_config=None)

#### record_mode*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Controls how the trace buffer stores data. The default is `recordUntilFull`.

#### trace_buffer_size_in_kb*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Size of the trace buffer in kilobytes. If not specified or zero is passed, a default value
of 200 MB would be used.

#### enable_sampling*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Turns on JavaScript stack sampling.

#### enable_systrace*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Turns on system tracing.

#### enable_argument_filter*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Turns on argument filter.

#### included_categories*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

Included category filters.

#### excluded_categories*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

Excluded category filters.

#### synthetic_delays*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

Configuration to synthesize the delays in tracing.

#### memory_dump_config*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`MemoryDumpConfig`](#nodriver.cdp.tracing.MemoryDumpConfig)]* *= None*

Configuration for memory dump triggers. Used only when “memory-infra” category is enabled.

### *class* StreamFormat(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Data format of a trace. Can be either the legacy JSON format or the
protocol buffer format. Note that the JSON format will be deprecated soon.

#### JSON *= 'json'*

#### PROTO *= 'proto'*

### *class* StreamCompression(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Compression type to use for traces returned via streams.

#### NONE *= 'none'*

#### GZIP *= 'gzip'*

### *class* MemoryDumpLevelOfDetail(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Details exposed when memory request explicitly declared.
Keep consistent with memory_dump_request_args.h and
memory_instrumentation.mojom

#### BACKGROUND *= 'background'*

#### LIGHT *= 'light'*

#### DETAILED *= 'detailed'*

### *class* TracingBackend(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Backend type to use for tracing. `chrome` uses the Chrome-integrated
tracing service and is supported on all platforms. `system` is only
supported on Chrome OS and uses the Perfetto system tracing service.
`auto` chooses `system` when the perfettoConfig provided to Tracing.start
specifies at least one non-Chrome data source; otherwise uses `chrome`.

#### AUTO *= 'auto'*

#### CHROME *= 'chrome'*

#### SYSTEM *= 'system'*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### end()

Stop trace events collection.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_categories()

Gets supported tracing categories.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**
  A list of supported tracing categories.

### record_clock_sync_marker(sync_id)

Record a clock sync marker in the trace.

**EXPERIMENTAL**

* **Parameters:**
  **sync_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – The ID of this clock sync marker
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### request_memory_dump(deterministic=None, level_of_detail=None)

Request a global memory dump.

**EXPERIMENTAL**

* **Parameters:**
  * **deterministic** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Enables more deterministic results by forcing garbage collection
  * **level_of_detail** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`MemoryDumpLevelOfDetail`](#nodriver.cdp.tracing.MemoryDumpLevelOfDetail)]) – *(Optional)* Specifies level of details in memory dump. Defaults to “detailed”.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`bool`](https://docs.python.org/3/library/functions.html#bool)]]
* **Returns:**
  A tuple with the following items:
  1. **dumpGuid** - GUID of the resulting global memory dump.
  2. **success** - True iff the global memory dump succeeded.

### start(categories=None, options=None, buffer_usage_reporting_interval=None, transfer_mode=None, stream_format=None, stream_compression=None, trace_config=None, perfetto_config=None, tracing_backend=None)

Start trace events collection.

* **Parameters:**
  * **categories** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(DEPRECATED)** **(EXPERIMENTAL)** *(Optional)* Category/tag filter
  * **options** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(DEPRECATED)** **(EXPERIMENTAL)** *(Optional)* Tracing options
  * **buffer_usage_reporting_interval** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – **(EXPERIMENTAL)** *(Optional)* If set, the agent will issue bufferUsage events at this interval, specified in milliseconds
  * **transfer_mode** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Whether to report trace events as series of dataCollected events or to save trace to a stream (defaults to ``ReportEvents```).
  * **stream_format** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StreamFormat`](#nodriver.cdp.tracing.StreamFormat)]) – *(Optional)* Trace data format to use. This only applies when using ```ReturnAsStream``` transfer mode (defaults to ```json```).
  * **stream_compression** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StreamCompression`](#nodriver.cdp.tracing.StreamCompression)]) – **(EXPERIMENTAL)** *(Optional)* Compression format to use. This only applies when using ```ReturnAsStream``` transfer mode (defaults to ```none```)
  * **trace_config** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TraceConfig`](#nodriver.cdp.tracing.TraceConfig)]) – *(Optional)*
  * **perfetto_config** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* Base64-encoded serialized perfetto.protos.TraceConfig protobuf message When specified, the parameters ```categories```, ```options```, ```traceConfig``` are ignored. (Encoded as a base64 string when passed over JSON)
  * **tracing_backend** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TracingBackend`](#nodriver.cdp.tracing.TracingBackend)]) – **(EXPERIMENTAL)** *(Optional)* Backend type (defaults to ```auto``)
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* BufferUsage(percent_full, event_count, value)

**EXPERIMENTAL**

#### percent_full*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]*

A number in range [0..1] that indicates the used size of event buffer as a fraction of its
total size.

#### event_count*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]*

An approximate number of events in the trace log.

#### value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]*

A number in range [0..1] that indicates the used size of event buffer as a fraction of its
total size.

### *class* DataCollected(value)

**EXPERIMENTAL**

Contains a bucket of collected trace events. When tracing is stopped collected events will be
sent as a sequence of dataCollected events followed by tracingComplete event.

#### value*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]*

### *class* TracingComplete(data_loss_occurred, stream, trace_format, stream_compression)

Signals that tracing is stopped and there is no trace buffers pending flush, all data were
delivered via dataCollected events.

#### data_loss_occurred*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Indicates whether some trace data is known to have been lost, e.g. because the trace ring
buffer wrapped around.

#### stream*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StreamHandle`](io.md#nodriver.cdp.io.StreamHandle)]*

A handle of the stream that holds resulting trace data.

#### trace_format*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StreamFormat`](#nodriver.cdp.tracing.StreamFormat)]*

Trace data format of returned stream.

#### stream_compression*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StreamCompression`](#nodriver.cdp.tracing.StreamCompression)]*

Compression format of returned stream.
