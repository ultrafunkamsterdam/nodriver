WebMCP
======

*This CDP domain is experimental.*

.. module:: nodriver.cdp.web_mcp

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: Annotation
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: InvocationStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Tool
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RemovedTool
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

.. autofunction:: cancel_invocation

.. autofunction:: disable

.. autofunction:: enable

.. autofunction:: invoke_tool

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: ToolsAdded
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ToolsRemoved
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ToolInvoked
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ToolResponded
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
