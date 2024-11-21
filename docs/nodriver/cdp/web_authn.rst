WebAuthn
========

This domain allows configuring virtual authenticators to test the WebAuthn
API.

*This CDP domain is experimental.*

.. module:: nodriver.cdp.web_authn

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: AuthenticatorId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AuthenticatorProtocol
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Ctap2Version
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AuthenticatorTransport
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: VirtualAuthenticatorOptions
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Credential
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

.. autofunction:: add_credential

.. autofunction:: add_virtual_authenticator

.. autofunction:: clear_credentials

.. autofunction:: disable

.. autofunction:: enable

.. autofunction:: get_credential

.. autofunction:: get_credentials

.. autofunction:: remove_credential

.. autofunction:: remove_virtual_authenticator

.. autofunction:: set_automatic_presence_simulation

.. autofunction:: set_credential_properties

.. autofunction:: set_response_override_bits

.. autofunction:: set_user_verified

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: CredentialAdded
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CredentialDeleted
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CredentialUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CredentialAsserted
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
