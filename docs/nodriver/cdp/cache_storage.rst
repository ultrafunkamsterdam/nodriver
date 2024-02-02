CacheStorage
============

*This CDP domain is experimental.*

.. module:: nodriver.cdp.cache_storage

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: CacheId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CachedResponseType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DataEntry
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Cache
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Header
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CachedResponse
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

.. autofunction:: delete_cache

.. autofunction:: delete_entry

.. autofunction:: request_cache_names

.. autofunction:: request_cached_response

.. autofunction:: request_entries

Events
------

*There are no events in this module.*
