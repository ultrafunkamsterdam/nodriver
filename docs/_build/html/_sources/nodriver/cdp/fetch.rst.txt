Fetch
=====

A domain for letting clients substitute browser's network layer with client code.

.. module:: nodriver.cdp.fetch

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: RequestId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RequestStage
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RequestPattern
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: HeaderEntry
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AuthChallenge
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AuthChallengeResponse
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

.. autofunction:: continue_request

.. autofunction:: continue_response

.. autofunction:: continue_with_auth

.. autofunction:: disable

.. autofunction:: enable

.. autofunction:: fail_request

.. autofunction:: fulfill_request

.. autofunction:: get_response_body

.. autofunction:: take_response_body_as_stream

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: RequestPaused
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AuthRequired
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
