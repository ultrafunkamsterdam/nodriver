Inspector
=========

*This CDP domain is experimental.*

.. module:: nodriver.cdp.inspector

* Types_
* Commands_
* Events_

Types
-----

*There are no types in this module.*

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

.. autoclass:: Detached
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TargetCrashed
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TargetReloadedAfterCrash
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
