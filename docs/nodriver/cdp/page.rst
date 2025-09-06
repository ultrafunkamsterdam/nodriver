Page
====

Actions and events related to the inspected page belong to the page domain.

.. module:: nodriver.cdp.page

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: FrameId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AdFrameType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AdFrameExplanation
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AdFrameStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AdScriptId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AdScriptAncestry
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SecureContextType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CrossOriginIsolatedContextType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: GatedAPIFeatures
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PermissionsPolicyFeature
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PermissionsPolicyBlockReason
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PermissionsPolicyBlockLocator
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PermissionsPolicyFeatureState
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: OriginTrialTokenStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: OriginTrialStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: OriginTrialUsageRestriction
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: OriginTrialToken
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: OriginTrialTokenWithStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: OriginTrial
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SecurityOriginDetails
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Frame
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameResource
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameResourceTree
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameTree
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ScriptIdentifier
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TransitionType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: NavigationEntry
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ScreencastFrameMetadata
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DialogType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AppManifestError
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AppManifestParsedProperties
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: LayoutViewport
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: VisualViewport
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Viewport
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FontFamilies
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ScriptFontFamilies
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FontSizes
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ClientNavigationReason
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ClientNavigationDisposition
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: InstallabilityErrorArgument
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: InstallabilityError
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReferrerPolicy
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CompilationCacheParams
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FileFilter
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FileHandler
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ImageResource
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: LaunchHandler
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ProtocolHandler
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RelatedApplication
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ScopeExtension
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Screenshot
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ShareTarget
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Shortcut
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebAppManifest
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: NavigationType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BackForwardCacheNotRestoredReason
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BackForwardCacheNotRestoredReasonType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BackForwardCacheBlockingDetails
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BackForwardCacheNotRestoredExplanation
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BackForwardCacheNotRestoredExplanationTree
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

.. autofunction:: add_compilation_cache

.. autofunction:: add_script_to_evaluate_on_load

.. autofunction:: add_script_to_evaluate_on_new_document

.. autofunction:: bring_to_front

.. autofunction:: capture_screenshot

.. autofunction:: capture_snapshot

.. autofunction:: clear_compilation_cache

.. autofunction:: clear_device_metrics_override

.. autofunction:: clear_device_orientation_override

.. autofunction:: clear_geolocation_override

.. autofunction:: close

.. autofunction:: crash

.. autofunction:: create_isolated_world

.. autofunction:: delete_cookie

.. autofunction:: disable

.. autofunction:: enable

.. autofunction:: generate_test_report

.. autofunction:: get_ad_script_ancestry

.. autofunction:: get_app_id

.. autofunction:: get_app_manifest

.. autofunction:: get_frame_tree

.. autofunction:: get_installability_errors

.. autofunction:: get_layout_metrics

.. autofunction:: get_manifest_icons

.. autofunction:: get_navigation_history

.. autofunction:: get_origin_trials

.. autofunction:: get_permissions_policy_state

.. autofunction:: get_resource_content

.. autofunction:: get_resource_tree

.. autofunction:: handle_java_script_dialog

.. autofunction:: navigate

.. autofunction:: navigate_to_history_entry

.. autofunction:: print_to_pdf

.. autofunction:: produce_compilation_cache

.. autofunction:: reload

.. autofunction:: remove_script_to_evaluate_on_load

.. autofunction:: remove_script_to_evaluate_on_new_document

.. autofunction:: reset_navigation_history

.. autofunction:: screencast_frame_ack

.. autofunction:: search_in_resource

.. autofunction:: set_ad_blocking_enabled

.. autofunction:: set_bypass_csp

.. autofunction:: set_device_metrics_override

.. autofunction:: set_device_orientation_override

.. autofunction:: set_document_content

.. autofunction:: set_download_behavior

.. autofunction:: set_font_families

.. autofunction:: set_font_sizes

.. autofunction:: set_geolocation_override

.. autofunction:: set_intercept_file_chooser_dialog

.. autofunction:: set_lifecycle_events_enabled

.. autofunction:: set_prerendering_allowed

.. autofunction:: set_rph_registration_mode

.. autofunction:: set_spc_transaction_mode

.. autofunction:: set_touch_emulation_enabled

.. autofunction:: set_web_lifecycle_state

.. autofunction:: start_screencast

.. autofunction:: stop_loading

.. autofunction:: stop_screencast

.. autofunction:: wait_for_debugger

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: DomContentEventFired
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FileChooserOpened
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameAttached
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameClearedScheduledNavigation
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameDetached
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameSubtreeWillBeDetached
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameNavigated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DocumentOpened
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameResized
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameStartedNavigating
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameRequestedNavigation
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameScheduledNavigation
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameStartedLoading
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FrameStoppedLoading
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DownloadWillBegin
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DownloadProgress
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: InterstitialHidden
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: InterstitialShown
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: JavascriptDialogClosed
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: JavascriptDialogOpening
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: LifecycleEvent
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BackForwardCacheNotUsed
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: LoadEventFired
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: NavigatedWithinDocument
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ScreencastFrame
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ScreencastVisibilityChanged
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WindowOpen
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CompilationCacheProduced
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
