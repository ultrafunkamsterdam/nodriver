Animation
=========

*This CDP domain is experimental.*

.. module:: nodriver.cdp.animation

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: Animation
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ViewOrScrollTimeline
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AnimationEffect
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: KeyframesRule
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: KeyframeStyle
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

.. autofunction:: disable

.. autofunction:: enable

.. autofunction:: get_current_time

.. autofunction:: get_playback_rate

.. autofunction:: release_animations

.. autofunction:: resolve_animation

.. autofunction:: seek_animations

.. autofunction:: set_paused

.. autofunction:: set_playback_rate

.. autofunction:: set_timing

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: AnimationCanceled
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AnimationCreated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AnimationStarted
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AnimationUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
