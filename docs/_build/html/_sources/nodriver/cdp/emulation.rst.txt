Emulation
=========

This domain emulates different environments for the page.

.. module:: nodriver.cdp.emulation

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: SafeAreaInsets
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ScreenOrientation
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DisplayFeature
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DevicePosture
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: MediaFeature
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: VirtualTimePolicy
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: UserAgentBrandVersion
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: UserAgentMetadata
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SensorType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SensorMetadata
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SensorReadingSingle
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SensorReadingXYZ
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SensorReadingQuaternion
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SensorReading
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PressureSource
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PressureState
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PressureMetadata
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WorkAreaInsets
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ScreenId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ScreenInfo
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DisabledImageType
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

.. autofunction:: add_screen

.. autofunction:: can_emulate

.. autofunction:: clear_device_metrics_override

.. autofunction:: clear_device_posture_override

.. autofunction:: clear_display_features_override

.. autofunction:: clear_geolocation_override

.. autofunction:: clear_idle_override

.. autofunction:: get_overridden_sensor_information

.. autofunction:: get_screen_infos

.. autofunction:: remove_screen

.. autofunction:: reset_page_scale_factor

.. autofunction:: set_auto_dark_mode_override

.. autofunction:: set_automation_override

.. autofunction:: set_cpu_throttling_rate

.. autofunction:: set_data_saver_override

.. autofunction:: set_default_background_color_override

.. autofunction:: set_device_metrics_override

.. autofunction:: set_device_posture_override

.. autofunction:: set_disabled_image_types

.. autofunction:: set_display_features_override

.. autofunction:: set_document_cookie_disabled

.. autofunction:: set_emit_touch_events_for_mouse

.. autofunction:: set_emulated_media

.. autofunction:: set_emulated_os_text_scale

.. autofunction:: set_emulated_vision_deficiency

.. autofunction:: set_focus_emulation_enabled

.. autofunction:: set_geolocation_override

.. autofunction:: set_hardware_concurrency_override

.. autofunction:: set_idle_override

.. autofunction:: set_locale_override

.. autofunction:: set_navigator_overrides

.. autofunction:: set_page_scale_factor

.. autofunction:: set_pressure_data_override

.. autofunction:: set_pressure_source_override_enabled

.. autofunction:: set_pressure_state_override

.. autofunction:: set_safe_area_insets_override

.. autofunction:: set_script_execution_disabled

.. autofunction:: set_scrollbars_hidden

.. autofunction:: set_sensor_override_enabled

.. autofunction:: set_sensor_override_readings

.. autofunction:: set_small_viewport_height_difference_override

.. autofunction:: set_timezone_override

.. autofunction:: set_touch_emulation_enabled

.. autofunction:: set_user_agent_override

.. autofunction:: set_virtual_time_policy

.. autofunction:: set_visible_size

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: VirtualTimeBudgetExpired
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
