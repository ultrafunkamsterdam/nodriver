Input
=====

.. module:: nodriver.cdp.input_

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: TouchPoint
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: GestureSourceType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: MouseButton
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TimeSinceEpoch
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DragDataItem
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DragData
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

.. autofunction:: cancel_dragging

.. autofunction:: dispatch_drag_event

.. autofunction:: dispatch_key_event

.. autofunction:: dispatch_mouse_event

.. autofunction:: dispatch_touch_event

.. autofunction:: emulate_touch_from_mouse_event

.. autofunction:: ime_set_composition

.. autofunction:: insert_text

.. autofunction:: set_ignore_input_events

.. autofunction:: set_intercept_drags

.. autofunction:: synthesize_pinch_gesture

.. autofunction:: synthesize_scroll_gesture

.. autofunction:: synthesize_tap_gesture

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: DragIntercepted
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
