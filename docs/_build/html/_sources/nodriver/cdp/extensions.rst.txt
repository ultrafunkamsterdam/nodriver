Extensions
==========

Defines commands and events for browser extensions.

*This CDP domain is experimental.*

.. module:: nodriver.cdp.extensions

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: StorageArea
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

.. autofunction:: clear_storage_items

.. autofunction:: get_storage_items

.. autofunction:: load_unpacked

.. autofunction:: remove_storage_items

.. autofunction:: set_storage_items

.. autofunction:: uninstall

Events
------

*There are no events in this module.*
