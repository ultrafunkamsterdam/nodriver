DeviceOrientation
=================

*This CDP domain is experimental.*

.. module:: nodriver.cdp.device_orientation

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

.. autofunction:: clear_device_orientation_override

.. autofunction:: set_device_orientation_override

Events
------

*There are no events in this module.*
