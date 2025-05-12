Browser
=======

The Browser domain defines methods and events for browser managing.

.. module:: nodriver.cdp.browser

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: BrowserContextID
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WindowID
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WindowState
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Bounds
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PermissionType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PermissionSetting
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PermissionDescriptor
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BrowserCommandId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Bucket
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Histogram
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PrivacySandboxAPI
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

.. autofunction:: add_privacy_sandbox_coordinator_key_config

.. autofunction:: add_privacy_sandbox_enrollment_override

.. autofunction:: cancel_download

.. autofunction:: close

.. autofunction:: crash

.. autofunction:: crash_gpu_process

.. autofunction:: execute_browser_command

.. autofunction:: get_browser_command_line

.. autofunction:: get_histogram

.. autofunction:: get_histograms

.. autofunction:: get_version

.. autofunction:: get_window_bounds

.. autofunction:: get_window_for_target

.. autofunction:: grant_permissions

.. autofunction:: reset_permissions

.. autofunction:: set_dock_tile

.. autofunction:: set_download_behavior

.. autofunction:: set_permission

.. autofunction:: set_window_bounds

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: DownloadWillBegin
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DownloadProgress
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
