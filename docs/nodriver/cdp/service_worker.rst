ServiceWorker
=============

*This CDP domain is experimental.*

.. module:: nodriver.cdp.service_worker

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: RegistrationID
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ServiceWorkerRegistration
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ServiceWorkerVersionRunningStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ServiceWorkerVersionStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ServiceWorkerVersion
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ServiceWorkerErrorMessage
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

.. autofunction:: deliver_push_message

.. autofunction:: disable

.. autofunction:: dispatch_periodic_sync_event

.. autofunction:: dispatch_sync_event

.. autofunction:: enable

.. autofunction:: set_force_update_on_page_load

.. autofunction:: skip_waiting

.. autofunction:: start_worker

.. autofunction:: stop_all_workers

.. autofunction:: stop_worker

.. autofunction:: unregister

.. autofunction:: update_registration

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: WorkerErrorReported
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WorkerRegistrationUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WorkerVersionUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
