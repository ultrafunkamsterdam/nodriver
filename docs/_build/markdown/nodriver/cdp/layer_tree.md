# LayerTree

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.layer_tree"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* LayerId

Unique Layer identifier.

### *class* SnapshotId

Unique snapshot identifier.

### *class* ScrollRect(rect, type_)

Rectangle where scrolling happens on the main thread.

#### rect*: [`Rect`](dom.md#nodriver.cdp.dom.Rect)*

Rectangle itself.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Reason for rectangle to force scrolling on the main thread

### *class* StickyPositionConstraint(sticky_box_rect, containing_block_rect, nearest_layer_shifting_sticky_box=None, nearest_layer_shifting_containing_block=None)

Sticky position constraints.

#### sticky_box_rect*: [`Rect`](dom.md#nodriver.cdp.dom.Rect)*

Layout rectangle of the sticky element before being shifted

#### containing_block_rect*: [`Rect`](dom.md#nodriver.cdp.dom.Rect)*

Layout rectangle of the containing block of the sticky element

#### nearest_layer_shifting_sticky_box*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LayerId`](#nodriver.cdp.layer_tree.LayerId)]* *= None*

The nearest sticky layer that shifts the sticky box

#### nearest_layer_shifting_containing_block*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LayerId`](#nodriver.cdp.layer_tree.LayerId)]* *= None*

The nearest sticky layer that shifts the containing block

### *class* PictureTile(x, y, picture)

Serialized fragment of layer picture along with its offset within the layer.

#### x*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Offset from owning layer left boundary

#### y*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Offset from owning layer top boundary

#### picture*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Base64-encoded snapshot data. (Encoded as a base64 string when passed over JSON)

### *class* Layer(layer_id, offset_x, offset_y, width, height, paint_count, draws_content, parent_layer_id=None, backend_node_id=None, transform=None, anchor_x=None, anchor_y=None, anchor_z=None, invisible=None, scroll_rects=None, sticky_position_constraint=None)

Information about a compositing layer.

#### layer_id*: [`LayerId`](#nodriver.cdp.layer_tree.LayerId)*

The unique id for this layer.

#### offset_x*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Offset from parent layer, X coordinate.

#### offset_y*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Offset from parent layer, Y coordinate.

#### width*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Layer width.

#### height*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Layer height.

#### paint_count*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Indicates how many time this layer has painted.

#### draws_content*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Indicates whether this layer hosts any content, rather than being used for
transform/scrolling purposes only.

#### parent_layer_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LayerId`](#nodriver.cdp.layer_tree.LayerId)]* *= None*

The id of parent (not present for root).

#### backend_node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

The backend id for the node associated with this layer.

#### transform*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`float`](https://docs.python.org/3/library/functions.html#float)]]* *= None*

Transformation matrix for layer, default is identity matrix

#### anchor_x*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Transform anchor point X, absent if no transform specified

#### anchor_y*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Transform anchor point Y, absent if no transform specified

#### anchor_z*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Transform anchor point Z, absent if no transform specified

#### invisible*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Set if layer is not visible.

#### scroll_rects*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ScrollRect`](#nodriver.cdp.layer_tree.ScrollRect)]]* *= None*

Rectangles scrolling on main thread only.

#### sticky_position_constraint*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StickyPositionConstraint`](#nodriver.cdp.layer_tree.StickyPositionConstraint)]* *= None*

Sticky position constraint information

### *class* PaintProfile(iterable=(), /)

Array of timings, one per paint step.

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### compositing_reasons(layer_id)

Provides the reasons why the given layer was composited.

* **Parameters:**
  **layer_id** ([`LayerId`](#nodriver.cdp.layer_tree.LayerId)) – The id of the layer for which we want to get the reasons it was composited.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]]
* **Returns:**
  A tuple with the following items:
  1. **compositingReasons** - A list of strings specifying reasons for the given layer to become composited.
  2. **compositingReasonIds** - A list of strings specifying reason IDs for the given layer to become composited.

### disable()

Disables compositing tree inspection.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables compositing tree inspection.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### load_snapshot(tiles)

Returns the snapshot identifier.

* **Parameters:**
  **tiles** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PictureTile`](#nodriver.cdp.layer_tree.PictureTile)]) – An array of tiles composing the snapshot.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SnapshotId`](#nodriver.cdp.layer_tree.SnapshotId)]
* **Returns:**
  The id of the snapshot.

### make_snapshot(layer_id)

Returns the layer snapshot identifier.

* **Parameters:**
  **layer_id** ([`LayerId`](#nodriver.cdp.layer_tree.LayerId)) – The id of the layer.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SnapshotId`](#nodriver.cdp.layer_tree.SnapshotId)]
* **Returns:**
  The id of the layer snapshot.

### profile_snapshot(snapshot_id, min_repeat_count=None, min_duration=None, clip_rect=None)

* **Parameters:**
  * **snapshot_id** ([`SnapshotId`](#nodriver.cdp.layer_tree.SnapshotId)) – The id of the layer snapshot.
  * **min_repeat_count** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The maximum number of times to replay the snapshot (1, if not specified).
  * **min_duration** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* The minimum duration (in seconds) to replay the snapshot.
  * **clip_rect** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Rect`](dom.md#nodriver.cdp.dom.Rect)]) – *(Optional)* The clip rectangle to apply when replaying the snapshot.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PaintProfile`](#nodriver.cdp.layer_tree.PaintProfile)]]
* **Returns:**
  The array of paint profiles, one per run.

### release_snapshot(snapshot_id)

Releases layer snapshot captured by the back-end.

* **Parameters:**
  **snapshot_id** ([`SnapshotId`](#nodriver.cdp.layer_tree.SnapshotId)) – The id of the layer snapshot.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### replay_snapshot(snapshot_id, from_step=None, to_step=None, scale=None)

Replays the layer snapshot and returns the resulting bitmap.

* **Parameters:**
  * **snapshot_id** ([`SnapshotId`](#nodriver.cdp.layer_tree.SnapshotId)) – The id of the layer snapshot.
  * **from_step** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The first step to replay from (replay from the very start if not specified).
  * **to_step** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The last step to replay to (replay till the end if not specified).
  * **scale** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* The scale to apply while replaying (defaults to 1).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**
  A data: URL for resulting image.

### snapshot_command_log(snapshot_id)

Replays the layer snapshot and returns canvas log.

* **Parameters:**
  **snapshot_id** ([`SnapshotId`](#nodriver.cdp.layer_tree.SnapshotId)) – The id of the layer snapshot.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]]
* **Returns:**
  The array of canvas function calls.

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* LayerPainted(layer_id, clip)

#### layer_id*: [`LayerId`](#nodriver.cdp.layer_tree.LayerId)*

The id of the painted layer.

#### clip*: [`Rect`](dom.md#nodriver.cdp.dom.Rect)*

Clip rectangle.

### *class* LayerTreeDidChange(layers)

#### layers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Layer`](#nodriver.cdp.layer_tree.Layer)]]*

Layer tree, absent if not in the compositing mode.
