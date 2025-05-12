Target
======

Supports additional targets discovery and allows to attach to them.

.. module:: nodriver.cdp.target

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: TargetID
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SessionID
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TargetInfo
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FilterEntry
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TargetFilter
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RemoteLocation
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WindowState
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

.. autofunction:: activate_target

.. autofunction:: attach_to_browser_target

.. autofunction:: attach_to_target

.. autofunction:: auto_attach_related

.. autofunction:: close_target

.. autofunction:: create_browser_context

.. autofunction:: create_target

.. autofunction:: detach_from_target

.. autofunction:: dispose_browser_context

.. autofunction:: expose_dev_tools_protocol

.. autofunction:: get_browser_contexts

.. autofunction:: get_target_info

.. autofunction:: get_targets

.. autofunction:: send_message_to_target

.. autofunction:: set_auto_attach

.. autofunction:: set_discover_targets

.. autofunction:: set_remote_locations

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: AttachedToTarget
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DetachedFromTarget
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReceivedMessageFromTarget
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TargetCreated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TargetDestroyed
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TargetCrashed
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TargetInfoChanged
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
