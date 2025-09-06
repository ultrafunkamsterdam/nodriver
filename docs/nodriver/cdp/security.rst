Security
========

.. module:: nodriver.cdp.security

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: CertificateId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: MixedContentType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SecurityState
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CertificateSecurityState
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SafetyTipStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SafetyTipInfo
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: VisibleSecurityState
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SecurityStateExplanation
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: InsecureContentStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CertificateErrorAction
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

.. autofunction:: handle_certificate_error

.. autofunction:: set_ignore_certificate_errors

.. autofunction:: set_override_certificate_errors

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: CertificateError
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: VisibleSecurityStateChanged
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SecurityStateChanged
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
