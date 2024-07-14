SystemInfo
==========

The SystemInfo domain defines methods and events for querying low-level system information.

*This CDP domain is experimental.*

.. module:: nodriver.cdp.system_info

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: GPUDevice
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Size
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: VideoDecodeAcceleratorCapability
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: VideoEncodeAcceleratorCapability
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SubsamplingFormat
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ImageType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ImageDecodeAcceleratorCapability
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: GPUInfo
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ProcessInfo
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

.. autofunction:: get_feature_state

.. autofunction:: get_info

.. autofunction:: get_process_info

Events
------

*There are no events in this module.*
