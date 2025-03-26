Preload
=======

*This CDP domain is experimental.*

.. module:: nodriver.cdp.preload

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: RuleSetId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RuleSet
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RuleSetErrorType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SpeculationAction
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SpeculationTargetHint
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PreloadingAttemptKey
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PreloadingAttemptSource
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PreloadPipelineId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PrerenderFinalStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PreloadingStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PrefetchStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PrerenderMismatchedHeaders
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

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: RuleSetUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RuleSetRemoved
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PreloadEnabledStateUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PrefetchStatusUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PrerenderStatusUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PreloadingAttemptSourcesUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
