# Input

* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* TouchPoint(x, y, radius_x=None, radius_y=None, rotation_angle=None, force=None, tangential_pressure=None, tilt_x=None, tilt_y=None, twist=None, id_=None)

#### x*: [`float`](https://docs.python.org/3/library/functions.html#float)*

X coordinate of the event relative to the main frame’s viewport in CSS pixels.

#### y*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Y coordinate of the event relative to the main frame’s viewport in CSS pixels. 0 refers to
the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.

#### radius_x*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

1.0).

* **Type:**
  X radius of the touch area (default

#### radius_y*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

1.0).

* **Type:**
  Y radius of the touch area (default

#### rotation_angle*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

0.0).

* **Type:**
  Rotation angle (default

#### force*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

1.0).

* **Type:**
  Force (default

#### tangential_pressure*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

0).

* **Type:**
  The normalized tangential pressure, which has a range of [-1,1] (default

#### tilt_x*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

* **Type:**
  The plane angle between the Y-Z plane and the plane containing both the stylus axis and the Y axis, in degrees of the range [-90,90], a positive tiltX is to the right (default

#### tilt_y*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

0).

* **Type:**
  The plane angle between the X-Z plane and the plane containing both the stylus axis and the X axis, in degrees of the range [-90,90], a positive tiltY is towards the user (default

#### twist*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

0).

* **Type:**
  The clockwise rotation of a pen stylus around its own major axis, in degrees in the range [0,359] (default

#### id_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Identifier used to track touch sources between events, must be unique within an event.

### *class* GestureSourceType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### DEFAULT *= 'default'*

#### TOUCH *= 'touch'*

#### MOUSE *= 'mouse'*

### *class* MouseButton(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### NONE *= 'none'*

#### LEFT *= 'left'*

#### MIDDLE *= 'middle'*

#### RIGHT *= 'right'*

#### BACK *= 'back'*

#### FORWARD *= 'forward'*

### *class* TimeSinceEpoch(x=0, /)

UTC time in seconds, counted from January 1, 1970.

### *class* DragDataItem(mime_type, data, title=None, base_url=None)

#### mime_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Mime type of the dragged data.

#### data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Depending of the value of `mimeType`, it contains the dragged link,
text, HTML markup or any other data.

#### title*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Title associated with a link. Only valid when `mimeType` == “text/uri-list”.

#### base_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Stores the base URL for the contained markup. Only valid when `mimeType`
== “text/html”.

### *class* DragData(items, drag_operations_mask, files=None)

#### items*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`DragDataItem`](#nodriver.cdp.input_.DragDataItem)]*

#### drag_operations_mask*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Bit field representing allowed drag operations. Copy = 1, Link = 2, Move = 16

#### files*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

List of filenames that should be included when dropping

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### cancel_dragging()

Cancels any active dragging in the page.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### dispatch_drag_event(type_, x, y, data, modifiers=None)

Dispatches a drag event into the page.

**EXPERIMENTAL**

* **Parameters:**
  * **type** – Type of the drag event.
  * **x** ([`float`](https://docs.python.org/3/library/functions.html#float)) – X coordinate of the event relative to the main frame’s viewport in CSS pixels.
  * **y** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Y coordinate of the event relative to the main frame’s viewport in CSS pixels. 0 refers to the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.
  * **data** ([`DragData`](#nodriver.cdp.input_.DragData)) – 
  * **modifiers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### dispatch_key_event(type_, modifiers=None, timestamp=None, text=None, unmodified_text=None, key_identifier=None, code=None, key=None, windows_virtual_key_code=None, native_virtual_key_code=None, auto_repeat=None, is_keypad=None, is_system_key=None, location=None, commands=None)

Dispatches a key event to the page.

* **Parameters:**
  * **type** – Type of the key event.
  * **modifiers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
  * **timestamp** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeSinceEpoch`](#nodriver.cdp.input_.TimeSinceEpoch)]) – *(Optional)* Time at which the event occurred.
  * **text** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Text as generated by processing a virtual key code with a keyboard layout. Not needed for for ``keyUp``` and ```rawKeyDown``` events (default: “”)
  * **unmodified_text** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Text that would have been generated by the keyboard if no modifiers were pressed (except for shift). Useful for shortcut (accelerator) key handling (default: “”).
  * **key_identifier** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Unique key identifier (e.g., ‘U+0041’) (default: “”).
  * **code** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Unique DOM defined string value for each physical key (e.g., ‘KeyA’) (default: “”).
  * **key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Unique DOM defined string value describing the meaning of the key in the context of active modifiers, keyboard layout, etc (e.g., ‘AltGr’) (default: “”).
  * **windows_virtual_key_code** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Windows virtual key code (default: 0).
  * **native_virtual_key_code** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Native virtual key code (default: 0).
  * **auto_repeat** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether the event was generated from auto repeat (default: false).
  * **is_keypad** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether the event was generated from the keypad (default: false).
  * **is_system_key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether the event was a system key event (default: false).
  * **location** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Whether the event was from the left or right side of the keyboard. 1=Left, 2=Right (default: 0).
  * **commands** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]) – **(EXPERIMENTAL)** *(Optional)* Editing commands to send with the key event (e.g., ‘selectAll’) (default: []). These are related to but not equal the command names used in ```document.execCommand`` and NSStandardKeyBindingResponding. See [https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/editing/commands/editor_command_names.h](https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/editing/commands/editor_command_names.h) for valid command names.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### dispatch_mouse_event(type_, x, y, modifiers=None, timestamp=None, button=None, buttons=None, click_count=None, force=None, tangential_pressure=None, tilt_x=None, tilt_y=None, twist=None, delta_x=None, delta_y=None, pointer_type=None)

Dispatches a mouse event to the page.

* **Parameters:**
  * **type** – Type of the mouse event.
  * **x** ([`float`](https://docs.python.org/3/library/functions.html#float)) – X coordinate of the event relative to the main frame’s viewport in CSS pixels.
  * **y** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Y coordinate of the event relative to the main frame’s viewport in CSS pixels. 0 refers to the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.
  * **modifiers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
  * **timestamp** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeSinceEpoch`](#nodriver.cdp.input_.TimeSinceEpoch)]) – *(Optional)* Time at which the event occurred.
  * **button** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`MouseButton`](#nodriver.cdp.input_.MouseButton)]) – *(Optional)* Mouse button (default: “none”).
  * **buttons** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* A number indicating which buttons are pressed on the mouse when a mouse event is triggered. Left=1, Right=2, Middle=4, Back=8, Forward=16, None=0.
  * **click_count** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Number of times the mouse button was clicked (default: 0).
  * **force** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – **(EXPERIMENTAL)** *(Optional)* The normalized pressure, which has a range of [0,1] (default: 0).
  * **tangential_pressure** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – **(EXPERIMENTAL)** *(Optional)* The normalized tangential pressure, which has a range of [-1,1] (default: 0).
  * **tilt_x** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* The plane angle between the Y-Z plane and the plane containing both the stylus axis and the Y axis, in degrees of the range [-90,90], a positive tiltX is to the right (default: 0).
  * **tilt_y** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* The plane angle between the X-Z plane and the plane containing both the stylus axis and the X axis, in degrees of the range [-90,90], a positive tiltY is towards the user (default: 0).
  * **twist** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* The clockwise rotation of a pen stylus around its own major axis, in degrees in the range [0,359] (default: 0).
  * **delta_x** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* X delta in CSS pixels for mouse wheel event (default: 0).
  * **delta_y** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Y delta in CSS pixels for mouse wheel event (default: 0).
  * **pointer_type** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Pointer type (default: “mouse”).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### dispatch_touch_event(type_, touch_points, modifiers=None, timestamp=None)

Dispatches a touch event to the page.

* **Parameters:**
  * **type** – Type of the touch event. TouchEnd and TouchCancel must not contain any touch points, while TouchStart and TouchMove must contains at least one.
  * **touch_points** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`TouchPoint`](#nodriver.cdp.input_.TouchPoint)]) – Active touch points on the touch device. One event per any changed point (compared to previous touch event in a sequence) is generated, emulating pressing/moving/releasing points one by one.
  * **modifiers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
  * **timestamp** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeSinceEpoch`](#nodriver.cdp.input_.TimeSinceEpoch)]) – *(Optional)* Time at which the event occurred.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### emulate_touch_from_mouse_event(type_, x, y, button, timestamp=None, delta_x=None, delta_y=None, modifiers=None, click_count=None)

Emulates touch event from the mouse event parameters.

**EXPERIMENTAL**

* **Parameters:**
  * **type** – Type of the mouse event.
  * **x** ([`int`](https://docs.python.org/3/library/functions.html#int)) – X coordinate of the mouse pointer in DIP.
  * **y** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Y coordinate of the mouse pointer in DIP.
  * **button** ([`MouseButton`](#nodriver.cdp.input_.MouseButton)) – Mouse button. Only “none”, “left”, “right” are supported.
  * **timestamp** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeSinceEpoch`](#nodriver.cdp.input_.TimeSinceEpoch)]) – *(Optional)* Time at which the event occurred (default: current time).
  * **delta_x** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* X delta in DIP for mouse wheel event (default: 0).
  * **delta_y** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Y delta in DIP for mouse wheel event (default: 0).
  * **modifiers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
  * **click_count** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Number of times the mouse button was clicked (default: 0).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### ime_set_composition(text, selection_start, selection_end, replacement_start=None, replacement_end=None)

This method sets the current candidate text for IME.
Use imeCommitComposition to commit the final text.
Use imeSetComposition with empty string as text to cancel composition.

**EXPERIMENTAL**

* **Parameters:**
  * **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – The text to insert
  * **selection_start** ([`int`](https://docs.python.org/3/library/functions.html#int)) – selection start
  * **selection_end** ([`int`](https://docs.python.org/3/library/functions.html#int)) – selection end
  * **replacement_start** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* replacement start
  * **replacement_end** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* replacement end
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### insert_text(text)

This method emulates inserting text that doesn’t come from a key press,
for example an emoji keyboard or an IME.

**EXPERIMENTAL**

* **Parameters:**
  **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – The text to insert.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_ignore_input_events(ignore)

Ignores input events (useful while auditing page).

* **Parameters:**
  **ignore** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Ignores input events processing when set to true.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_intercept_drags(enabled)

Prevents default drag and drop behavior and instead emits `Input.dragIntercepted` events.
Drag and drop behavior can be directly controlled via `Input.dispatchDragEvent`.

**EXPERIMENTAL**

* **Parameters:**
  **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### synthesize_pinch_gesture(x, y, scale_factor, relative_speed=None, gesture_source_type=None)

Synthesizes a pinch gesture over a time period by issuing appropriate touch events.

**EXPERIMENTAL**

* **Parameters:**
  * **x** ([`float`](https://docs.python.org/3/library/functions.html#float)) – X coordinate of the start of the gesture in CSS pixels.
  * **y** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Y coordinate of the start of the gesture in CSS pixels.
  * **scale_factor** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Relative scale factor after zooming (>1.0 zooms in, <1.0 zooms out).
  * **relative_speed** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Relative pointer speed in pixels per second (default: 800).
  * **gesture_source_type** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`GestureSourceType`](#nodriver.cdp.input_.GestureSourceType)]) – *(Optional)* Which type of input events to be generated (default: ‘default’, which queries the platform for the preferred input type).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### synthesize_scroll_gesture(x, y, x_distance=None, y_distance=None, x_overscroll=None, y_overscroll=None, prevent_fling=None, speed=None, gesture_source_type=None, repeat_count=None, repeat_delay_ms=None, interaction_marker_name=None)

Synthesizes a scroll gesture over a time period by issuing appropriate touch events.

**EXPERIMENTAL**

* **Parameters:**
  * **x** ([`float`](https://docs.python.org/3/library/functions.html#float)) – X coordinate of the start of the gesture in CSS pixels.
  * **y** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Y coordinate of the start of the gesture in CSS pixels.
  * **x_distance** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* The distance to scroll along the X axis (positive to scroll left).
  * **y_distance** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* The distance to scroll along the Y axis (positive to scroll up).
  * **x_overscroll** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* The number of additional pixels to scroll back along the X axis, in addition to the given distance.
  * **y_overscroll** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* The number of additional pixels to scroll back along the Y axis, in addition to the given distance.
  * **prevent_fling** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Prevent fling (default: true).
  * **speed** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Swipe speed in pixels per second (default: 800).
  * **gesture_source_type** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`GestureSourceType`](#nodriver.cdp.input_.GestureSourceType)]) – *(Optional)* Which type of input events to be generated (default: ‘default’, which queries the platform for the preferred input type).
  * **repeat_count** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The number of times to repeat the gesture (default: 0).
  * **repeat_delay_ms** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The number of milliseconds delay between each repeat. (default: 250).
  * **interaction_marker_name** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* The name of the interaction markers to generate, if not empty (default: “”).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### synthesize_tap_gesture(x, y, duration=None, tap_count=None, gesture_source_type=None)

Synthesizes a tap gesture over a time period by issuing appropriate touch events.

**EXPERIMENTAL**

* **Parameters:**
  * **x** ([`float`](https://docs.python.org/3/library/functions.html#float)) – X coordinate of the start of the gesture in CSS pixels.
  * **y** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Y coordinate of the start of the gesture in CSS pixels.
  * **duration** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Duration between touchdown and touchup events in ms (default: 50).
  * **tap_count** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Number of times to perform the tap (e.g. 2 for double tap, default: 1).
  * **gesture_source_type** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`GestureSourceType`](#nodriver.cdp.input_.GestureSourceType)]) – *(Optional)* Which type of input events to be generated (default: ‘default’, which queries the platform for the preferred input type).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* DragIntercepted(data)

**EXPERIMENTAL**

Emitted only when `Input.setInterceptDrags` is enabled. Use this data with `Input.dispatchDragEvent` to
restore normal drag and drop behavior.

#### data*: [`DragData`](#nodriver.cdp.input_.DragData)*
