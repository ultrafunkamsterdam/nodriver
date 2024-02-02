DOMStorage
==========

Query and modify DOM storage.

*This CDP domain is experimental.*

.. module:: nodriver.cdp.dom_storage

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: SerializedStorageKey
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: StorageId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Item
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

.. autofunction:: clear

.. autofunction:: disable

.. autofunction:: enable

.. autofunction:: get_dom_storage_items

.. autofunction:: remove_dom_storage_item

.. autofunction:: set_dom_storage_item

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: DomStorageItemAdded
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DomStorageItemRemoved
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DomStorageItemUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DomStorageItemsCleared
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
