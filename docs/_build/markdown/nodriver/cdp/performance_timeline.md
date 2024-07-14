# PerformanceTimeline

Reporting of performance timeline events, as specified in
[https://w3c.github.io/performance-timeline/#dom-performanceobserver](https://w3c.github.io/performance-timeline/#dom-performanceobserver).

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.performance_timeline"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* LargestContentfulPaint(render_time, load_time, size, element_id=None, url=None, node_id=None)

See [https://github.com/WICG/LargestContentfulPaint](https://github.com/WICG/LargestContentfulPaint) and largest_contentful_paint.idl

#### render_time*: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

#### load_time*: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

#### size*: [`float`](https://docs.python.org/3/library/functions.html#float)*

The number of pixels being painted.

#### element_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The id attribute of the element, if available.

#### url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The URL of the image (may be trimmed).

#### node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

### *class* LayoutShiftAttribution(previous_rect, current_rect, node_id=None)

#### previous_rect*: [`Rect`](dom.md#nodriver.cdp.dom.Rect)*

#### current_rect*: [`Rect`](dom.md#nodriver.cdp.dom.Rect)*

#### node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

### *class* LayoutShift(value, had_recent_input, last_input_time, sources)

See [https://wicg.github.io/layout-instability/#sec-layout-shift](https://wicg.github.io/layout-instability/#sec-layout-shift) and layout_shift.idl

#### value*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Score increment produced by this event.

#### had_recent_input*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### last_input_time*: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

#### sources*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`LayoutShiftAttribution`](#nodriver.cdp.performance_timeline.LayoutShiftAttribution)]*

### *class* TimelineEvent(frame_id, type_, name, time, duration=None, lcp_details=None, layout_shift_details=None)

#### frame_id*: [`FrameId`](page.md#nodriver.cdp.page.FrameId)*

Identifies the frame that this event is related to. Empty for non-frame targets.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

//w3c.github.io/performance-timeline/#dom-performanceentry-entrytype
This determines which of the optional “details” fields is present.

* **Type:**
  The event type, as specified in https

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name may be empty depending on the type.

#### time*: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

Time in seconds since Epoch, monotonically increasing within document lifetime.

#### duration*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Event duration, if applicable.

#### lcp_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LargestContentfulPaint`](#nodriver.cdp.performance_timeline.LargestContentfulPaint)]* *= None*

#### layout_shift_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LayoutShift`](#nodriver.cdp.performance_timeline.LayoutShift)]* *= None*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### enable(event_types)

Previously buffered events would be reported before method returns.
See also: timelineEventAdded

* **Parameters:**
  **event_types** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – The types of event to report, as specified in [https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype](https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype) The specified filter overrides any previous filters, passing empty filter disables recording. Note that not all types exposed to the web platform are currently supported.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* TimelineEventAdded(event)

Sent when a performance timeline event is added. See reportPerformanceTimeline method.

#### event*: [`TimelineEvent`](#nodriver.cdp.performance_timeline.TimelineEvent)*
