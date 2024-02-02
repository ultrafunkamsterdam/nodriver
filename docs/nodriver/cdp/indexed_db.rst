IndexedDB
=========

*This CDP domain is experimental.*

.. module:: nodriver.cdp.indexed_db

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: DatabaseWithObjectStores
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ObjectStore
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ObjectStoreIndex
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Key
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: KeyRange
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DataEntry
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: KeyPath
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

.. autofunction:: clear_object_store

.. autofunction:: delete_database

.. autofunction:: delete_object_store_entries

.. autofunction:: disable

.. autofunction:: enable

.. autofunction:: get_metadata

.. autofunction:: request_data

.. autofunction:: request_database

.. autofunction:: request_database_names

Events
------

*There are no events in this module.*
