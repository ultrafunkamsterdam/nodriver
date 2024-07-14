DOMDebugger
===========

DOM debugging allows setting breakpoints on particular DOM operations and events. JavaScript
execution will stop on these operations as if there was a regular breakpoint set.

.. module:: nodriver.cdp.dom_debugger

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: DOMBreakpointType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CSPViolationType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: EventListener
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

.. autofunction:: get_event_listeners

.. autofunction:: remove_dom_breakpoint

.. autofunction:: remove_event_listener_breakpoint

.. autofunction:: remove_instrumentation_breakpoint

.. autofunction:: remove_xhr_breakpoint

.. autofunction:: set_break_on_csp_violation

.. autofunction:: set_dom_breakpoint

.. autofunction:: set_event_listener_breakpoint

.. autofunction:: set_instrumentation_breakpoint

.. autofunction:: set_xhr_breakpoint

Events
------

*There are no events in this module.*
