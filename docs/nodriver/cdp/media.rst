Media
=====

This domain allows detailed inspection of media elements.

*This CDP domain is experimental.*

.. module:: nodriver.cdp.media

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: PlayerId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Timestamp
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PlayerMessage
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PlayerProperty
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PlayerEvent
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PlayerErrorSourceLocation
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PlayerError
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Player
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

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: PlayerPropertiesChanged
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PlayerEventsAdded
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PlayerMessagesLogged
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PlayerErrorsRaised
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PlayerCreated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
