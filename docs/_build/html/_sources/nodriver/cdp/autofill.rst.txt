Autofill
========

Defines commands and events for Autofill.

*This CDP domain is experimental.*

.. module:: nodriver.cdp.autofill

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: CreditCard
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AddressField
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AddressFields
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Address
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AddressUI
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FillingStrategy
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FilledField
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

.. autofunction:: set_addresses

.. autofunction:: trigger

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: AddressFormFilled
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
