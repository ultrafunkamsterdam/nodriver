SmartCardEmulation
==================

*This CDP domain is experimental.*

.. module:: nodriver.cdp.smart_card_emulation

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: ResultCode
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ShareMode
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Disposition
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ConnectionState
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReaderStateFlags
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ProtocolSet
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Protocol
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReaderStateIn
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReaderStateOut
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

.. autofunction:: report_begin_transaction_result

.. autofunction:: report_connect_result

.. autofunction:: report_data_result

.. autofunction:: report_error

.. autofunction:: report_establish_context_result

.. autofunction:: report_get_status_change_result

.. autofunction:: report_list_readers_result

.. autofunction:: report_plain_result

.. autofunction:: report_release_context_result

.. autofunction:: report_status_result

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: EstablishContextRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReleaseContextRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ListReadersRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: GetStatusChangeRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CancelRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ConnectRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DisconnectRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TransmitRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ControlRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: GetAttribRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SetAttribRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: StatusRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BeginTransactionRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: EndTransactionRequested
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
