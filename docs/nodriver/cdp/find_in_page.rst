FindInPage
==========

This domain provides commands to trigger the "Find in page" feature.

*This CDP domain is experimental.*

.. module:: nodriver.cdp.find_in_page

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

.. autofunction:: find_first

.. autofunction:: find_next

.. autofunction:: find_prev

.. autofunction:: stop

Events
------

*There are no events in this module.*
