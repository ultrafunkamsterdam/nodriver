Cast
====

A domain for interacting with Cast, Presentation API, and Remote Playback API
functionalities.

*This CDP domain is experimental.*

.. module:: nodriver.cdp.cast

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: Sink
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

.. autofunction:: set_sink_to_use

.. autofunction:: start_desktop_mirroring

.. autofunction:: start_tab_mirroring

.. autofunction:: stop_casting

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: SinksUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: IssueUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
