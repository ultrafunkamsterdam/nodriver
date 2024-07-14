Profiler
========

.. module:: nodriver.cdp.profiler

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: ProfileNode
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Profile
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PositionTickInfo
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CoverageRange
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FunctionCoverage
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ScriptCoverage
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

.. autofunction:: disable

.. autofunction:: enable

.. autofunction:: get_best_effort_coverage

.. autofunction:: set_sampling_interval

.. autofunction:: start

.. autofunction:: start_precise_coverage

.. autofunction:: stop

.. autofunction:: stop_precise_coverage

.. autofunction:: take_precise_coverage

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: ConsoleProfileFinished
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ConsoleProfileStarted
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PreciseCoverageDeltaUpdate
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
