# Page

Actions and events related to the inspected page belong to the page domain.

<a id="module-nodriver.cdp.page"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* FrameId

Unique frame identifier.

### *class* AdFrameType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Indicates whether a frame has been identified as an ad.

#### NONE *= 'none'*

#### CHILD *= 'child'*

#### ROOT *= 'root'*

### *class* AdFrameExplanation(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### PARENT_IS_AD *= 'ParentIsAd'*

#### CREATED_BY_AD_SCRIPT *= 'CreatedByAdScript'*

#### MATCHED_BLOCKING_RULE *= 'MatchedBlockingRule'*

### *class* AdFrameStatus(ad_frame_type, explanations=None)

Indicates whether a frame has been identified as an ad and why.

#### ad_frame_type*: [`AdFrameType`](#nodriver.cdp.page.AdFrameType)*

#### explanations*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AdFrameExplanation`](#nodriver.cdp.page.AdFrameExplanation)]]* *= None*

### *class* AdScriptId(script_id, debugger_id)

Identifies the script which caused a script or frame to be labelled as an
ad.

#### script_id*: [`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)*

Script Id of the script which caused a script or frame to be labelled as
an ad.

#### debugger_id*: [`UniqueDebuggerId`](runtime.md#nodriver.cdp.runtime.UniqueDebuggerId)*

Id of scriptId’s debugger.

### *class* AdScriptAncestry(ancestry_chain, root_script_filterlist_rule=None)

Encapsulates the script ancestry and the root script filterlist rule that
caused the frame to be labelled as an ad. Only created when `ancestryChain`
is not empty.

#### ancestry_chain*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AdScriptId`](#nodriver.cdp.page.AdScriptId)]*

A chain of `AdScriptId`’s representing the ancestry of an ad script that
led to the creation of a frame. The chain is ordered from the script
itself (lower level) up to its root ancestor that was flagged by
filterlist.

#### root_script_filterlist_rule*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The filterlist rule that caused the root (last) script in
`ancestryChain` to be ad-tagged. Only populated if the rule is
available.

### *class* SecureContextType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Indicates whether the frame is a secure context and why it is the case.

#### SECURE *= 'Secure'*

#### SECURE_LOCALHOST *= 'SecureLocalhost'*

#### INSECURE_SCHEME *= 'InsecureScheme'*

#### INSECURE_ANCESTOR *= 'InsecureAncestor'*

### *class* CrossOriginIsolatedContextType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Indicates whether the frame is cross-origin isolated and why it is the case.

#### ISOLATED *= 'Isolated'*

#### NOT_ISOLATED *= 'NotIsolated'*

#### NOT_ISOLATED_FEATURE_DISABLED *= 'NotIsolatedFeatureDisabled'*

### *class* GatedAPIFeatures(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### SHARED_ARRAY_BUFFERS *= 'SharedArrayBuffers'*

#### SHARED_ARRAY_BUFFERS_TRANSFER_ALLOWED *= 'SharedArrayBuffersTransferAllowed'*

#### PERFORMANCE_MEASURE_MEMORY *= 'PerformanceMeasureMemory'*

#### PERFORMANCE_PROFILE *= 'PerformanceProfile'*

### *class* PermissionsPolicyFeature(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

All Permissions Policy features. This enum should match the one defined
in services/network/public/cpp/permissions_policy/permissions_policy_features.json5.
LINT.IfChange(PermissionsPolicyFeature)

#### ACCELEROMETER *= 'accelerometer'*

#### ALL_SCREENS_CAPTURE *= 'all-screens-capture'*

#### AMBIENT_LIGHT_SENSOR *= 'ambient-light-sensor'*

#### ARIA_NOTIFY *= 'aria-notify'*

#### ATTRIBUTION_REPORTING *= 'attribution-reporting'*

#### AUTOPLAY *= 'autoplay'*

#### BLUETOOTH *= 'bluetooth'*

#### BROWSING_TOPICS *= 'browsing-topics'*

#### CAMERA *= 'camera'*

#### CAPTURED_SURFACE_CONTROL *= 'captured-surface-control'*

#### CH_DPR *= 'ch-dpr'*

#### CH_DEVICE_MEMORY *= 'ch-device-memory'*

#### CH_DOWNLINK *= 'ch-downlink'*

#### CH_ECT *= 'ch-ect'*

#### CH_PREFERS_COLOR_SCHEME *= 'ch-prefers-color-scheme'*

#### CH_PREFERS_REDUCED_MOTION *= 'ch-prefers-reduced-motion'*

#### CH_PREFERS_REDUCED_TRANSPARENCY *= 'ch-prefers-reduced-transparency'*

#### CH_RTT *= 'ch-rtt'*

#### CH_SAVE_DATA *= 'ch-save-data'*

#### CH_UA *= 'ch-ua'*

#### CH_UA_ARCH *= 'ch-ua-arch'*

#### CH_UA_BITNESS *= 'ch-ua-bitness'*

#### CH_UA_HIGH_ENTROPY_VALUES *= 'ch-ua-high-entropy-values'*

#### CH_UA_PLATFORM *= 'ch-ua-platform'*

#### CH_UA_MODEL *= 'ch-ua-model'*

#### CH_UA_MOBILE *= 'ch-ua-mobile'*

#### CH_UA_FORM_FACTORS *= 'ch-ua-form-factors'*

#### CH_UA_FULL_VERSION *= 'ch-ua-full-version'*

#### CH_UA_FULL_VERSION_LIST *= 'ch-ua-full-version-list'*

#### CH_UA_PLATFORM_VERSION *= 'ch-ua-platform-version'*

#### CH_UA_WOW64 *= 'ch-ua-wow64'*

#### CH_VIEWPORT_HEIGHT *= 'ch-viewport-height'*

#### CH_VIEWPORT_WIDTH *= 'ch-viewport-width'*

#### CH_WIDTH *= 'ch-width'*

#### CLIPBOARD_READ *= 'clipboard-read'*

#### CLIPBOARD_WRITE *= 'clipboard-write'*

#### COMPUTE_PRESSURE *= 'compute-pressure'*

#### CONTROLLED_FRAME *= 'controlled-frame'*

#### CROSS_ORIGIN_ISOLATED *= 'cross-origin-isolated'*

#### DEFERRED_FETCH *= 'deferred-fetch'*

#### DEFERRED_FETCH_MINIMAL *= 'deferred-fetch-minimal'*

#### DEVICE_ATTRIBUTES *= 'device-attributes'*

#### DIGITAL_CREDENTIALS_CREATE *= 'digital-credentials-create'*

#### DIGITAL_CREDENTIALS_GET *= 'digital-credentials-get'*

#### DIRECT_SOCKETS *= 'direct-sockets'*

#### DIRECT_SOCKETS_MULTICAST *= 'direct-sockets-multicast'*

#### DIRECT_SOCKETS_PRIVATE *= 'direct-sockets-private'*

#### DISPLAY_CAPTURE *= 'display-capture'*

#### DOCUMENT_DOMAIN *= 'document-domain'*

#### ENCRYPTED_MEDIA *= 'encrypted-media'*

#### EXECUTION_WHILE_OUT_OF_VIEWPORT *= 'execution-while-out-of-viewport'*

#### EXECUTION_WHILE_NOT_RENDERED *= 'execution-while-not-rendered'*

#### FENCED_UNPARTITIONED_STORAGE_READ *= 'fenced-unpartitioned-storage-read'*

#### FOCUS_WITHOUT_USER_ACTIVATION *= 'focus-without-user-activation'*

#### FULLSCREEN *= 'fullscreen'*

#### FROBULATE *= 'frobulate'*

#### GAMEPAD *= 'gamepad'*

#### GEOLOCATION *= 'geolocation'*

#### GYROSCOPE *= 'gyroscope'*

#### HID *= 'hid'*

#### IDENTITY_CREDENTIALS_GET *= 'identity-credentials-get'*

#### IDLE_DETECTION *= 'idle-detection'*

#### INTEREST_COHORT *= 'interest-cohort'*

#### JOIN_AD_INTEREST_GROUP *= 'join-ad-interest-group'*

#### KEYBOARD_MAP *= 'keyboard-map'*

#### LANGUAGE_DETECTOR *= 'language-detector'*

#### LANGUAGE_MODEL *= 'language-model'*

#### LOCAL_FONTS *= 'local-fonts'*

#### LOCAL_NETWORK_ACCESS *= 'local-network-access'*

#### MAGNETOMETER *= 'magnetometer'*

#### MEDIA_PLAYBACK_WHILE_NOT_VISIBLE *= 'media-playback-while-not-visible'*

#### MICROPHONE *= 'microphone'*

#### MIDI *= 'midi'*

#### ON_DEVICE_SPEECH_RECOGNITION *= 'on-device-speech-recognition'*

#### OTP_CREDENTIALS *= 'otp-credentials'*

#### PAYMENT *= 'payment'*

#### PICTURE_IN_PICTURE *= 'picture-in-picture'*

#### POPINS *= 'popins'*

#### PRIVATE_AGGREGATION *= 'private-aggregation'*

#### PRIVATE_STATE_TOKEN_ISSUANCE *= 'private-state-token-issuance'*

#### PRIVATE_STATE_TOKEN_REDEMPTION *= 'private-state-token-redemption'*

#### PUBLICKEY_CREDENTIALS_CREATE *= 'publickey-credentials-create'*

#### PUBLICKEY_CREDENTIALS_GET *= 'publickey-credentials-get'*

#### RECORD_AD_AUCTION_EVENTS *= 'record-ad-auction-events'*

#### REWRITER *= 'rewriter'*

#### RUN_AD_AUCTION *= 'run-ad-auction'*

#### SCREEN_WAKE_LOCK *= 'screen-wake-lock'*

#### SERIAL *= 'serial'*

#### SHARED_AUTOFILL *= 'shared-autofill'*

#### SHARED_STORAGE *= 'shared-storage'*

#### SHARED_STORAGE_SELECT_URL *= 'shared-storage-select-url'*

#### SMART_CARD *= 'smart-card'*

#### SPEAKER_SELECTION *= 'speaker-selection'*

#### STORAGE_ACCESS *= 'storage-access'*

#### SUB_APPS *= 'sub-apps'*

#### SUMMARIZER *= 'summarizer'*

#### SYNC_XHR *= 'sync-xhr'*

#### TRANSLATOR *= 'translator'*

#### UNLOAD *= 'unload'*

#### USB *= 'usb'*

#### USB_UNRESTRICTED *= 'usb-unrestricted'*

#### VERTICAL_SCROLL *= 'vertical-scroll'*

#### WEB_APP_INSTALLATION *= 'web-app-installation'*

#### WEB_PRINTING *= 'web-printing'*

#### WEB_SHARE *= 'web-share'*

#### WINDOW_MANAGEMENT *= 'window-management'*

#### WRITER *= 'writer'*

#### XR_SPATIAL_TRACKING *= 'xr-spatial-tracking'*

### *class* PermissionsPolicyBlockReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Reason for a permissions policy feature to be disabled.

#### HEADER *= 'Header'*

#### IFRAME_ATTRIBUTE *= 'IframeAttribute'*

#### IN_FENCED_FRAME_TREE *= 'InFencedFrameTree'*

#### IN_ISOLATED_APP *= 'InIsolatedApp'*

### *class* PermissionsPolicyBlockLocator(frame_id, block_reason)

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

#### block_reason*: [`PermissionsPolicyBlockReason`](#nodriver.cdp.page.PermissionsPolicyBlockReason)*

### *class* PermissionsPolicyFeatureState(feature, allowed, locator=None)

#### feature*: [`PermissionsPolicyFeature`](#nodriver.cdp.page.PermissionsPolicyFeature)*

#### allowed*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### locator*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`PermissionsPolicyBlockLocator`](#nodriver.cdp.page.PermissionsPolicyBlockLocator)]* *= None*

### *class* OriginTrialTokenStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Origin Trial([https://www.chromium.org/blink/origin-trials](https://www.chromium.org/blink/origin-trials)) support.
Status for an Origin Trial token.

#### SUCCESS *= 'Success'*

#### NOT_SUPPORTED *= 'NotSupported'*

#### INSECURE *= 'Insecure'*

#### EXPIRED *= 'Expired'*

#### WRONG_ORIGIN *= 'WrongOrigin'*

#### INVALID_SIGNATURE *= 'InvalidSignature'*

#### MALFORMED *= 'Malformed'*

#### WRONG_VERSION *= 'WrongVersion'*

#### FEATURE_DISABLED *= 'FeatureDisabled'*

#### TOKEN_DISABLED *= 'TokenDisabled'*

#### FEATURE_DISABLED_FOR_USER *= 'FeatureDisabledForUser'*

#### UNKNOWN_TRIAL *= 'UnknownTrial'*

### *class* OriginTrialStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Status for an Origin Trial.

#### ENABLED *= 'Enabled'*

#### VALID_TOKEN_NOT_PROVIDED *= 'ValidTokenNotProvided'*

#### OS_NOT_SUPPORTED *= 'OSNotSupported'*

#### TRIAL_NOT_ALLOWED *= 'TrialNotAllowed'*

### *class* OriginTrialUsageRestriction(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### NONE *= 'None'*

#### SUBSET *= 'Subset'*

### *class* OriginTrialToken(origin, match_sub_domains, trial_name, expiry_time, is_third_party, usage_restriction)

#### origin*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### match_sub_domains*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### trial_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### expiry_time*: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

#### is_third_party*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### usage_restriction*: [`OriginTrialUsageRestriction`](#nodriver.cdp.page.OriginTrialUsageRestriction)*

### *class* OriginTrialTokenWithStatus(raw_token_text, status, parsed_token=None)

#### raw_token_text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### status*: [`OriginTrialTokenStatus`](#nodriver.cdp.page.OriginTrialTokenStatus)*

#### parsed_token*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`OriginTrialToken`](#nodriver.cdp.page.OriginTrialToken)]* *= None*

`parsedToken` is present only when the token is extractable and
parsable.

### *class* OriginTrial(trial_name, status, tokens_with_status)

#### trial_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### status*: [`OriginTrialStatus`](#nodriver.cdp.page.OriginTrialStatus)*

#### tokens_with_status*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`OriginTrialTokenWithStatus`](#nodriver.cdp.page.OriginTrialTokenWithStatus)]*

### *class* SecurityOriginDetails(is_localhost)

Additional information about the frame document’s security origin.

#### is_localhost*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Indicates whether the frame document’s security origin is one
of the local hostnames (e.g. “localhost”) or IP addresses (IPv4
127.0.0.0/8 or IPv6 ::1).

### *class* Frame(id_, loader_id, url, domain_and_registry, security_origin, mime_type, secure_context_type, cross_origin_isolated_context_type, gated_api_features, parent_id=None, name=None, url_fragment=None, security_origin_details=None, unreachable_url=None, ad_frame_status=None)

Information about the Frame on the page.

#### id_*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Frame unique identifier.

#### loader_id*: [`LoaderId`](network.md#nodriver.cdp.network.LoaderId)*

Identifier of the loader associated with this frame.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Frame document’s URL without fragment.

#### domain_and_registry*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Frame document’s registered domain, taking the public suffixes list into account.
Extracted from the Frame’s url.
Example URLs: [http://www.google.com/file.html](http://www.google.com/file.html) -> “google.com”

> [http://a.b.co.uk/file.html](http://a.b.co.uk/file.html)      -> “b.co.uk”

#### security_origin*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Frame document’s security origin.

#### mime_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Frame document’s mimeType as determined by the browser.

#### secure_context_type*: [`SecureContextType`](#nodriver.cdp.page.SecureContextType)*

Indicates whether the main document is a secure context and explains why that is the case.

#### cross_origin_isolated_context_type*: [`CrossOriginIsolatedContextType`](#nodriver.cdp.page.CrossOriginIsolatedContextType)*

Indicates whether this is a cross origin isolated context.

#### gated_api_features*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`GatedAPIFeatures`](#nodriver.cdp.page.GatedAPIFeatures)]*

Indicated which gated APIs / features are available.

#### parent_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](#nodriver.cdp.page.FrameId)]* *= None*

Parent frame identifier.

#### name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Frame’s name as specified in the tag.

#### url_fragment*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Frame document’s URL fragment including the ‘#’.

#### security_origin_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SecurityOriginDetails`](#nodriver.cdp.page.SecurityOriginDetails)]* *= None*

Additional details about the frame document’s security origin.

#### unreachable_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

If the frame failed to load, this contains the URL that could not be loaded. Note that unlike url above, this URL may contain a fragment.

#### ad_frame_status*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AdFrameStatus`](#nodriver.cdp.page.AdFrameStatus)]* *= None*

Indicates whether this frame was tagged as an ad and why.

### *class* FrameResource(url, type_, mime_type, last_modified=None, content_size=None, failed=None, canceled=None)

Information about the Resource on the page.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Resource URL.

#### type_*: [`ResourceType`](network.md#nodriver.cdp.network.ResourceType)*

Type of this resource.

#### mime_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Resource mimeType as determined by the browser.

#### last_modified*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)]* *= None*

last-modified timestamp as reported by server.

#### content_size*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Resource content size.

#### failed*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if the resource failed to load.

#### canceled*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if the resource was canceled during loading.

### *class* FrameResourceTree(frame, resources, child_frames=None)

Information about the Frame hierarchy along with their cached resources.

#### frame*: [`Frame`](#nodriver.cdp.page.Frame)*

Frame information for this tree item.

#### resources*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`FrameResource`](#nodriver.cdp.page.FrameResource)]*

Information about frame resources.

#### child_frames*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`FrameResourceTree`](#nodriver.cdp.page.FrameResourceTree)]]* *= None*

Child frames.

### *class* FrameTree(frame, child_frames=None)

Information about the Frame hierarchy.

#### frame*: [`Frame`](#nodriver.cdp.page.Frame)*

Frame information for this tree item.

#### child_frames*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`FrameTree`](#nodriver.cdp.page.FrameTree)]]* *= None*

Child frames.

### *class* ScriptIdentifier

Unique script identifier.

### *class* TransitionType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Transition type.

#### LINK *= 'link'*

#### TYPED *= 'typed'*

#### ADDRESS_BAR *= 'address_bar'*

#### AUTO_BOOKMARK *= 'auto_bookmark'*

#### AUTO_SUBFRAME *= 'auto_subframe'*

#### MANUAL_SUBFRAME *= 'manual_subframe'*

#### GENERATED *= 'generated'*

#### AUTO_TOPLEVEL *= 'auto_toplevel'*

#### FORM_SUBMIT *= 'form_submit'*

#### RELOAD *= 'reload'*

#### KEYWORD *= 'keyword'*

#### KEYWORD_GENERATED *= 'keyword_generated'*

#### OTHER *= 'other'*

### *class* NavigationEntry(id_, url, user_typed_url, title, transition_type)

Navigation history entry.

#### id_*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Unique id of the navigation history entry.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL of the navigation history entry.

#### user_typed_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL that the user typed in the url bar.

#### title*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Title of the navigation history entry.

#### transition_type*: [`TransitionType`](#nodriver.cdp.page.TransitionType)*

Transition type.

### *class* ScreencastFrameMetadata(offset_top, page_scale_factor, device_width, device_height, scroll_offset_x, scroll_offset_y, timestamp=None)

Screencast frame metadata.

#### offset_top*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Top offset in DIP.

#### page_scale_factor*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Page scale factor.

#### device_width*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Device screen width in DIP.

#### device_height*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Device screen height in DIP.

#### scroll_offset_x*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Position of horizontal scroll in CSS pixels.

#### scroll_offset_y*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Position of vertical scroll in CSS pixels.

#### timestamp*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)]* *= None*

Frame swap timestamp.

### *class* DialogType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Javascript dialog type.

#### ALERT *= 'alert'*

#### CONFIRM *= 'confirm'*

#### PROMPT *= 'prompt'*

#### BEFOREUNLOAD *= 'beforeunload'*

### *class* AppManifestError(message, critical, line, column)

Error while paring app manifest.

#### message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Error message.

#### critical*: [`int`](https://docs.python.org/3/library/functions.html#int)*

If critical, this is a non-recoverable parse error.

#### line*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Error line.

#### column*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Error column.

### *class* AppManifestParsedProperties(scope)

Parsed app manifest properties.

#### scope*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Computed scope value

### *class* LayoutViewport(page_x, page_y, client_width, client_height)

Layout viewport position and dimensions.

#### page_x*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Horizontal offset relative to the document (CSS pixels).

#### page_y*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Vertical offset relative to the document (CSS pixels).

#### client_width*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Width (CSS pixels), excludes scrollbar if present.

#### client_height*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Height (CSS pixels), excludes scrollbar if present.

### *class* VisualViewport(offset_x, offset_y, page_x, page_y, client_width, client_height, scale, zoom=None)

Visual viewport position, dimensions, and scale.

#### offset_x*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Horizontal offset relative to the layout viewport (CSS pixels).

#### offset_y*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Vertical offset relative to the layout viewport (CSS pixels).

#### page_x*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Horizontal offset relative to the document (CSS pixels).

#### page_y*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Vertical offset relative to the document (CSS pixels).

#### client_width*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Width (CSS pixels), excludes scrollbar if present.

#### client_height*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Height (CSS pixels), excludes scrollbar if present.

#### scale*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Scale relative to the ideal viewport (size at width=device-width).

#### zoom*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Page zoom factor (CSS to device independent pixels ratio).

### *class* Viewport(x, y, width, height, scale)

Viewport for capturing screenshot.

#### x*: [`float`](https://docs.python.org/3/library/functions.html#float)*

X offset in device independent pixels (dip).

#### y*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Y offset in device independent pixels (dip).

#### width*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Rectangle width in device independent pixels (dip).

#### height*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Rectangle height in device independent pixels (dip).

#### scale*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Page scale factor.

### *class* FontFamilies(standard=None, fixed=None, serif=None, sans_serif=None, cursive=None, fantasy=None, math=None)

Generic font families collection.

#### standard*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The standard font-family.

#### fixed*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The fixed font-family.

#### serif*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The serif font-family.

#### sans_serif*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The sansSerif font-family.

#### cursive*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The cursive font-family.

#### fantasy*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The fantasy font-family.

#### math*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The math font-family.

### *class* ScriptFontFamilies(script, font_families)

Font families collection for a script.

#### script*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name of the script which these font families are defined for.

#### font_families*: [`FontFamilies`](#nodriver.cdp.page.FontFamilies)*

Generic font families collection for the script.

### *class* FontSizes(standard=None, fixed=None)

Default font sizes.

#### standard*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Default standard font size.

#### fixed*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Default fixed font size.

### *class* ClientNavigationReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### ANCHOR_CLICK *= 'anchorClick'*

#### FORM_SUBMISSION_GET *= 'formSubmissionGet'*

#### FORM_SUBMISSION_POST *= 'formSubmissionPost'*

#### HTTP_HEADER_REFRESH *= 'httpHeaderRefresh'*

#### INITIAL_FRAME_NAVIGATION *= 'initialFrameNavigation'*

#### META_TAG_REFRESH *= 'metaTagRefresh'*

#### OTHER *= 'other'*

#### PAGE_BLOCK_INTERSTITIAL *= 'pageBlockInterstitial'*

#### RELOAD *= 'reload'*

#### SCRIPT_INITIATED *= 'scriptInitiated'*

### *class* ClientNavigationDisposition(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### CURRENT_TAB *= 'currentTab'*

#### NEW_TAB *= 'newTab'*

#### NEW_WINDOW *= 'newWindow'*

#### DOWNLOAD *= 'download'*

### *class* InstallabilityErrorArgument(name, value)

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

‘minimum-icon-size-in-pixels’).

* **Type:**
  Argument name (e.g. name

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

‘64’).

* **Type:**
  Argument value (e.g. value

### *class* InstallabilityError(error_id, error_arguments)

The installability error

#### error_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The error id (e.g. ‘manifest-missing-suitable-icon’).

#### error_arguments*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`InstallabilityErrorArgument`](#nodriver.cdp.page.InstallabilityErrorArgument)]*

‘64’}).

* **Type:**
  The list of error arguments (e.g. {name
* **Type:**
  ‘minimum-icon-size-in-pixels’, value

### *class* ReferrerPolicy(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The referring-policy used for the navigation.

#### NO_REFERRER *= 'noReferrer'*

#### NO_REFERRER_WHEN_DOWNGRADE *= 'noReferrerWhenDowngrade'*

#### ORIGIN *= 'origin'*

#### ORIGIN_WHEN_CROSS_ORIGIN *= 'originWhenCrossOrigin'*

#### SAME_ORIGIN *= 'sameOrigin'*

#### STRICT_ORIGIN *= 'strictOrigin'*

#### STRICT_ORIGIN_WHEN_CROSS_ORIGIN *= 'strictOriginWhenCrossOrigin'*

#### UNSAFE_URL *= 'unsafeUrl'*

### *class* CompilationCacheParams(url, eager=None)

Per-script compilation cache parameters for `Page.produceCompilationCache`

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The URL of the script to produce a compilation cache entry for.

#### eager*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

A hint to the backend whether eager compilation is recommended.
(the actual compilation mode used is upon backend discretion).

### *class* FileFilter(name=None, accepts=None)

#### name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### accepts*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

### *class* FileHandler(action, name, launch_type, icons=None, accepts=None)

#### action*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### launch_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Won’t repeat the enums, using string for easy comparison. Same as the
other enums below.

#### icons*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ImageResource`](#nodriver.cdp.page.ImageResource)]]* *= None*

#### accepts*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`FileFilter`](#nodriver.cdp.page.FileFilter)]]* *= None*

Mimic a map, name is the key, accepts is the value.

### *class* ImageResource(url, sizes=None, type_=None)

The image definition used in both icon and screenshot.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The src field in the definition, but changing to url in favor of
consistency.

#### sizes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### type_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* LaunchHandler(client_mode)

#### client_mode*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* ProtocolHandler(protocol, url)

#### protocol*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* RelatedApplication(url, id_=None)

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### id_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* ScopeExtension(origin, has_origin_wildcard)

#### origin*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Instead of using tuple, this field always returns the serialized string
for easy understanding and comparison.

#### has_origin_wildcard*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

### *class* Screenshot(image, form_factor, label=None)

#### image*: [`ImageResource`](#nodriver.cdp.page.ImageResource)*

#### form_factor*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### label*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* ShareTarget(action, method, enctype, title=None, text=None, url=None, files=None)

#### action*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### method*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### enctype*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### title*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Embed the ShareTargetParams

#### text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### files*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`FileFilter`](#nodriver.cdp.page.FileFilter)]]* *= None*

### *class* Shortcut(name, url)

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* WebAppManifest(background_color=None, description=None, dir_=None, display=None, display_overrides=None, file_handlers=None, icons=None, id_=None, lang=None, launch_handler=None, name=None, orientation=None, prefer_related_applications=None, protocol_handlers=None, related_applications=None, scope=None, scope_extensions=None, screenshots=None, share_target=None, short_name=None, shortcuts=None, start_url=None, theme_color=None)

#### background_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### description*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The extra description provided by the manifest.

#### dir_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### display*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### display_overrides*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

The overrided display mode controlled by the user.

#### file_handlers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`FileHandler`](#nodriver.cdp.page.FileHandler)]]* *= None*

The handlers to open files.

#### icons*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ImageResource`](#nodriver.cdp.page.ImageResource)]]* *= None*

#### id_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### lang*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### launch_handler*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LaunchHandler`](#nodriver.cdp.page.LaunchHandler)]* *= None*

This field is non-standard and part of a Chrome
experiment. See:
[https://github.com/WICG/web-app-launch/blob/main/launch_handler.md](https://github.com/WICG/web-app-launch/blob/main/launch_handler.md)

* **Type:**
  TODO(crbug.com/1231886)

#### name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### orientation*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### prefer_related_applications*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

#### protocol_handlers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ProtocolHandler`](#nodriver.cdp.page.ProtocolHandler)]]* *= None*

The handlers to open protocols.

#### related_applications*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`RelatedApplication`](#nodriver.cdp.page.RelatedApplication)]]* *= None*

#### scope*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### scope_extensions*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ScopeExtension`](#nodriver.cdp.page.ScopeExtension)]]* *= None*

Non-standard, see
[https://github.com/WICG/manifest-incubations/blob/gh-pages/scope_extensions-explainer.md](https://github.com/WICG/manifest-incubations/blob/gh-pages/scope_extensions-explainer.md)

#### screenshots*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Screenshot`](#nodriver.cdp.page.Screenshot)]]* *= None*

The screenshots used by chromium.

#### share_target*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ShareTarget`](#nodriver.cdp.page.ShareTarget)]* *= None*

#### short_name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### shortcuts*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Shortcut`](#nodriver.cdp.page.Shortcut)]]* *= None*

#### start_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### theme_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* NavigationType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The type of a frameNavigated event.

#### NAVIGATION *= 'Navigation'*

#### BACK_FORWARD_CACHE_RESTORE *= 'BackForwardCacheRestore'*

### *class* BackForwardCacheNotRestoredReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

List of not restored reasons for back-forward cache.

#### NOT_PRIMARY_MAIN_FRAME *= 'NotPrimaryMainFrame'*

#### BACK_FORWARD_CACHE_DISABLED *= 'BackForwardCacheDisabled'*

#### RELATED_ACTIVE_CONTENTS_EXIST *= 'RelatedActiveContentsExist'*

#### HTTP_STATUS_NOT_OK *= 'HTTPStatusNotOK'*

#### SCHEME_NOT_HTTP_OR_HTTPS *= 'SchemeNotHTTPOrHTTPS'*

#### LOADING *= 'Loading'*

#### WAS_GRANTED_MEDIA_ACCESS *= 'WasGrantedMediaAccess'*

#### DISABLE_FOR_RENDER_FRAME_HOST_CALLED *= 'DisableForRenderFrameHostCalled'*

#### DOMAIN_NOT_ALLOWED *= 'DomainNotAllowed'*

#### HTTP_METHOD_NOT_GET *= 'HTTPMethodNotGET'*

#### SUBFRAME_IS_NAVIGATING *= 'SubframeIsNavigating'*

#### TIMEOUT *= 'Timeout'*

#### CACHE_LIMIT *= 'CacheLimit'*

#### JAVA_SCRIPT_EXECUTION *= 'JavaScriptExecution'*

#### RENDERER_PROCESS_KILLED *= 'RendererProcessKilled'*

#### RENDERER_PROCESS_CRASHED *= 'RendererProcessCrashed'*

#### SCHEDULER_TRACKED_FEATURE_USED *= 'SchedulerTrackedFeatureUsed'*

#### CONFLICTING_BROWSING_INSTANCE *= 'ConflictingBrowsingInstance'*

#### CACHE_FLUSHED *= 'CacheFlushed'*

#### SERVICE_WORKER_VERSION_ACTIVATION *= 'ServiceWorkerVersionActivation'*

#### SESSION_RESTORED *= 'SessionRestored'*

#### SERVICE_WORKER_POST_MESSAGE *= 'ServiceWorkerPostMessage'*

#### ENTERED_BACK_FORWARD_CACHE_BEFORE_SERVICE_WORKER_HOST_ADDED *= 'EnteredBackForwardCacheBeforeServiceWorkerHostAdded'*

#### RENDER_FRAME_HOST_REUSED_SAME_SITE *= 'RenderFrameHostReused_SameSite'*

#### RENDER_FRAME_HOST_REUSED_CROSS_SITE *= 'RenderFrameHostReused_CrossSite'*

#### SERVICE_WORKER_CLAIM *= 'ServiceWorkerClaim'*

#### IGNORE_EVENT_AND_EVICT *= 'IgnoreEventAndEvict'*

#### HAVE_INNER_CONTENTS *= 'HaveInnerContents'*

#### TIMEOUT_PUTTING_IN_CACHE *= 'TimeoutPuttingInCache'*

#### BACK_FORWARD_CACHE_DISABLED_BY_LOW_MEMORY *= 'BackForwardCacheDisabledByLowMemory'*

#### BACK_FORWARD_CACHE_DISABLED_BY_COMMAND_LINE *= 'BackForwardCacheDisabledByCommandLine'*

#### NETWORK_REQUEST_DATAPIPE_DRAINED_AS_BYTES_CONSUMER *= 'NetworkRequestDatapipeDrainedAsBytesConsumer'*

#### NETWORK_REQUEST_REDIRECTED *= 'NetworkRequestRedirected'*

#### NETWORK_REQUEST_TIMEOUT *= 'NetworkRequestTimeout'*

#### NETWORK_EXCEEDS_BUFFER_LIMIT *= 'NetworkExceedsBufferLimit'*

#### NAVIGATION_CANCELLED_WHILE_RESTORING *= 'NavigationCancelledWhileRestoring'*

#### NOT_MOST_RECENT_NAVIGATION_ENTRY *= 'NotMostRecentNavigationEntry'*

#### BACK_FORWARD_CACHE_DISABLED_FOR_PRERENDER *= 'BackForwardCacheDisabledForPrerender'*

#### USER_AGENT_OVERRIDE_DIFFERS *= 'UserAgentOverrideDiffers'*

#### FOREGROUND_CACHE_LIMIT *= 'ForegroundCacheLimit'*

#### BROWSING_INSTANCE_NOT_SWAPPED *= 'BrowsingInstanceNotSwapped'*

#### BACK_FORWARD_CACHE_DISABLED_FOR_DELEGATE *= 'BackForwardCacheDisabledForDelegate'*

#### UNLOAD_HANDLER_EXISTS_IN_MAIN_FRAME *= 'UnloadHandlerExistsInMainFrame'*

#### UNLOAD_HANDLER_EXISTS_IN_SUB_FRAME *= 'UnloadHandlerExistsInSubFrame'*

#### SERVICE_WORKER_UNREGISTRATION *= 'ServiceWorkerUnregistration'*

#### CACHE_CONTROL_NO_STORE *= 'CacheControlNoStore'*

#### CACHE_CONTROL_NO_STORE_COOKIE_MODIFIED *= 'CacheControlNoStoreCookieModified'*

#### CACHE_CONTROL_NO_STORE_HTTP_ONLY_COOKIE_MODIFIED *= 'CacheControlNoStoreHTTPOnlyCookieModified'*

#### NO_RESPONSE_HEAD *= 'NoResponseHead'*

#### UNKNOWN *= 'Unknown'*

#### ACTIVATION_NAVIGATIONS_DISALLOWED_FOR_BUG1234857 *= 'ActivationNavigationsDisallowedForBug1234857'*

#### ERROR_DOCUMENT *= 'ErrorDocument'*

#### FENCED_FRAMES_EMBEDDER *= 'FencedFramesEmbedder'*

#### COOKIE_DISABLED *= 'CookieDisabled'*

#### HTTP_AUTH_REQUIRED *= 'HTTPAuthRequired'*

#### COOKIE_FLUSHED *= 'CookieFlushed'*

#### BROADCAST_CHANNEL_ON_MESSAGE *= 'BroadcastChannelOnMessage'*

#### WEB_VIEW_SETTINGS_CHANGED *= 'WebViewSettingsChanged'*

#### WEB_VIEW_JAVA_SCRIPT_OBJECT_CHANGED *= 'WebViewJavaScriptObjectChanged'*

#### WEB_VIEW_MESSAGE_LISTENER_INJECTED *= 'WebViewMessageListenerInjected'*

#### WEB_VIEW_SAFE_BROWSING_ALLOWLIST_CHANGED *= 'WebViewSafeBrowsingAllowlistChanged'*

#### WEB_VIEW_DOCUMENT_START_JAVASCRIPT_CHANGED *= 'WebViewDocumentStartJavascriptChanged'*

#### WEB_SOCKET *= 'WebSocket'*

#### WEB_TRANSPORT *= 'WebTransport'*

#### WEB_RTC *= 'WebRTC'*

#### MAIN_RESOURCE_HAS_CACHE_CONTROL_NO_STORE *= 'MainResourceHasCacheControlNoStore'*

#### MAIN_RESOURCE_HAS_CACHE_CONTROL_NO_CACHE *= 'MainResourceHasCacheControlNoCache'*

#### SUBRESOURCE_HAS_CACHE_CONTROL_NO_STORE *= 'SubresourceHasCacheControlNoStore'*

#### SUBRESOURCE_HAS_CACHE_CONTROL_NO_CACHE *= 'SubresourceHasCacheControlNoCache'*

#### CONTAINS_PLUGINS *= 'ContainsPlugins'*

#### DOCUMENT_LOADED *= 'DocumentLoaded'*

#### OUTSTANDING_NETWORK_REQUEST_OTHERS *= 'OutstandingNetworkRequestOthers'*

#### REQUESTED_MIDI_PERMISSION *= 'RequestedMIDIPermission'*

#### REQUESTED_AUDIO_CAPTURE_PERMISSION *= 'RequestedAudioCapturePermission'*

#### REQUESTED_VIDEO_CAPTURE_PERMISSION *= 'RequestedVideoCapturePermission'*

#### REQUESTED_BACK_FORWARD_CACHE_BLOCKED_SENSORS *= 'RequestedBackForwardCacheBlockedSensors'*

#### REQUESTED_BACKGROUND_WORK_PERMISSION *= 'RequestedBackgroundWorkPermission'*

#### BROADCAST_CHANNEL *= 'BroadcastChannel'*

#### WEB_XR *= 'WebXR'*

#### SHARED_WORKER *= 'SharedWorker'*

#### SHARED_WORKER_MESSAGE *= 'SharedWorkerMessage'*

#### WEB_LOCKS *= 'WebLocks'*

#### WEB_HID *= 'WebHID'*

#### WEB_SHARE *= 'WebShare'*

#### REQUESTED_STORAGE_ACCESS_GRANT *= 'RequestedStorageAccessGrant'*

#### WEB_NFC *= 'WebNfc'*

#### OUTSTANDING_NETWORK_REQUEST_FETCH *= 'OutstandingNetworkRequestFetch'*

#### OUTSTANDING_NETWORK_REQUEST_XHR *= 'OutstandingNetworkRequestXHR'*

#### APP_BANNER *= 'AppBanner'*

#### PRINTING *= 'Printing'*

#### WEB_DATABASE *= 'WebDatabase'*

#### PICTURE_IN_PICTURE *= 'PictureInPicture'*

#### SPEECH_RECOGNIZER *= 'SpeechRecognizer'*

#### IDLE_MANAGER *= 'IdleManager'*

#### PAYMENT_MANAGER *= 'PaymentManager'*

#### SPEECH_SYNTHESIS *= 'SpeechSynthesis'*

#### KEYBOARD_LOCK *= 'KeyboardLock'*

#### WEB_OTP_SERVICE *= 'WebOTPService'*

#### OUTSTANDING_NETWORK_REQUEST_DIRECT_SOCKET *= 'OutstandingNetworkRequestDirectSocket'*

#### INJECTED_JAVASCRIPT *= 'InjectedJavascript'*

#### INJECTED_STYLE_SHEET *= 'InjectedStyleSheet'*

#### KEEPALIVE_REQUEST *= 'KeepaliveRequest'*

#### INDEXED_DB_EVENT *= 'IndexedDBEvent'*

#### DUMMY *= 'Dummy'*

#### JS_NETWORK_REQUEST_RECEIVED_CACHE_CONTROL_NO_STORE_RESOURCE *= 'JsNetworkRequestReceivedCacheControlNoStoreResource'*

#### WEB_RTC_USED_WITH_CCNS *= 'WebRTCUsedWithCCNS'*

#### WEB_TRANSPORT_USED_WITH_CCNS *= 'WebTransportUsedWithCCNS'*

#### WEB_SOCKET_USED_WITH_CCNS *= 'WebSocketUsedWithCCNS'*

#### SMART_CARD *= 'SmartCard'*

#### LIVE_MEDIA_STREAM_TRACK *= 'LiveMediaStreamTrack'*

#### UNLOAD_HANDLER *= 'UnloadHandler'*

#### PARSER_ABORTED *= 'ParserAborted'*

#### CONTENT_SECURITY_HANDLER *= 'ContentSecurityHandler'*

#### CONTENT_WEB_AUTHENTICATION_API *= 'ContentWebAuthenticationAPI'*

#### CONTENT_FILE_CHOOSER *= 'ContentFileChooser'*

#### CONTENT_SERIAL *= 'ContentSerial'*

#### CONTENT_FILE_SYSTEM_ACCESS *= 'ContentFileSystemAccess'*

#### CONTENT_MEDIA_DEVICES_DISPATCHER_HOST *= 'ContentMediaDevicesDispatcherHost'*

#### CONTENT_WEB_BLUETOOTH *= 'ContentWebBluetooth'*

#### CONTENT_WEB_USB *= 'ContentWebUSB'*

#### CONTENT_MEDIA_SESSION_SERVICE *= 'ContentMediaSessionService'*

#### CONTENT_SCREEN_READER *= 'ContentScreenReader'*

#### CONTENT_DISCARDED *= 'ContentDiscarded'*

#### EMBEDDER_POPUP_BLOCKER_TAB_HELPER *= 'EmbedderPopupBlockerTabHelper'*

#### EMBEDDER_SAFE_BROWSING_TRIGGERED_POPUP_BLOCKER *= 'EmbedderSafeBrowsingTriggeredPopupBlocker'*

#### EMBEDDER_SAFE_BROWSING_THREAT_DETAILS *= 'EmbedderSafeBrowsingThreatDetails'*

#### EMBEDDER_APP_BANNER_MANAGER *= 'EmbedderAppBannerManager'*

#### EMBEDDER_DOM_DISTILLER_VIEWER_SOURCE *= 'EmbedderDomDistillerViewerSource'*

#### EMBEDDER_DOM_DISTILLER_SELF_DELETING_REQUEST_DELEGATE *= 'EmbedderDomDistillerSelfDeletingRequestDelegate'*

#### EMBEDDER_OOM_INTERVENTION_TAB_HELPER *= 'EmbedderOomInterventionTabHelper'*

#### EMBEDDER_OFFLINE_PAGE *= 'EmbedderOfflinePage'*

#### EMBEDDER_CHROME_PASSWORD_MANAGER_CLIENT_BIND_CREDENTIAL_MANAGER *= 'EmbedderChromePasswordManagerClientBindCredentialManager'*

#### EMBEDDER_PERMISSION_REQUEST_MANAGER *= 'EmbedderPermissionRequestManager'*

#### EMBEDDER_MODAL_DIALOG *= 'EmbedderModalDialog'*

#### EMBEDDER_EXTENSIONS *= 'EmbedderExtensions'*

#### EMBEDDER_EXTENSION_MESSAGING *= 'EmbedderExtensionMessaging'*

#### EMBEDDER_EXTENSION_MESSAGING_FOR_OPEN_PORT *= 'EmbedderExtensionMessagingForOpenPort'*

#### EMBEDDER_EXTENSION_SENT_MESSAGE_TO_CACHED_FRAME *= 'EmbedderExtensionSentMessageToCachedFrame'*

#### REQUESTED_BY_WEB_VIEW_CLIENT *= 'RequestedByWebViewClient'*

#### POST_MESSAGE_BY_WEB_VIEW_CLIENT *= 'PostMessageByWebViewClient'*

#### CACHE_CONTROL_NO_STORE_DEVICE_BOUND_SESSION_TERMINATED *= 'CacheControlNoStoreDeviceBoundSessionTerminated'*

#### CACHE_LIMIT_PRUNED_ON_MODERATE_MEMORY_PRESSURE *= 'CacheLimitPrunedOnModerateMemoryPressure'*

#### CACHE_LIMIT_PRUNED_ON_CRITICAL_MEMORY_PRESSURE *= 'CacheLimitPrunedOnCriticalMemoryPressure'*

### *class* BackForwardCacheNotRestoredReasonType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Types of not restored reasons for back-forward cache.

#### SUPPORT_PENDING *= 'SupportPending'*

#### PAGE_SUPPORT_NEEDED *= 'PageSupportNeeded'*

#### CIRCUMSTANTIAL *= 'Circumstantial'*

### *class* BackForwardCacheBlockingDetails(line_number, column_number, url=None, function=None)

#### line_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Line number in the script (0-based).

#### column_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Column number in the script (0-based).

#### url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Url of the file where blockage happened. Optional because of tests.

#### function*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Function name where blockage happened. Optional because of anonymous functions and tests.

### *class* BackForwardCacheNotRestoredExplanation(type_, reason, context=None, details=None)

#### type_*: [`BackForwardCacheNotRestoredReasonType`](#nodriver.cdp.page.BackForwardCacheNotRestoredReasonType)*

Type of the reason

#### reason*: [`BackForwardCacheNotRestoredReason`](#nodriver.cdp.page.BackForwardCacheNotRestoredReason)*

Not restored reason

#### context*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Context associated with the reason. The meaning of this context is
dependent on the reason:
- EmbedderExtensionSentMessageToCachedFrame: the extension ID.

#### details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BackForwardCacheBlockingDetails`](#nodriver.cdp.page.BackForwardCacheBlockingDetails)]]* *= None*

### *class* BackForwardCacheNotRestoredExplanationTree(url, explanations, children)

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL of each frame

#### explanations*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BackForwardCacheNotRestoredExplanation`](#nodriver.cdp.page.BackForwardCacheNotRestoredExplanation)]*

Not restored reasons of each frame

#### children*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BackForwardCacheNotRestoredExplanationTree`](#nodriver.cdp.page.BackForwardCacheNotRestoredExplanationTree)]*

Array of children frame

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### add_compilation_cache(url, data)

Seeds compilation cache for given url. Compilation cache does not survive
cross-process navigation.

**EXPERIMENTAL**

* **Parameters:**
  * **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **data** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Base64-encoded data (Encoded as a base64 string when passed over JSON)
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### add_script_to_evaluate_on_load(script_source)

Deprecated, please use addScriptToEvaluateOnNewDocument instead.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  **script_source** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`ScriptIdentifier`](#nodriver.cdp.page.ScriptIdentifier)]
* **Returns:**
  Identifier of the added script.

#### Deprecated
Deprecated since version 1.3.

### add_script_to_evaluate_on_new_document(source, world_name=None, include_command_line_api=None, run_immediately=None)

Evaluates given script in every frame upon creation (before loading frame’s scripts).

* **Parameters:**
  * **source** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **world_name** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* If specified, creates an isolated world with the given name and evaluates given script in it. This world name will be used as the ExecutionContextDescription::name when the corresponding event is emitted.
  * **include_command_line_api** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Specifies whether command line API should be available to the script, defaults to false.
  * **run_immediately** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* If true, runs the script immediately on existing execution contexts or worlds. Default: false.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`ScriptIdentifier`](#nodriver.cdp.page.ScriptIdentifier)]
* **Returns:**
  Identifier of the added script.

### bring_to_front()

Brings page to front (activates tab).

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### capture_screenshot(format_=None, quality=None, clip=None, from_surface=None, capture_beyond_viewport=None, optimize_for_speed=None)

Capture page screenshot.

* **Parameters:**
  * **format** – *(Optional)* Image compression format (defaults to png).
  * **quality** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Compression quality from range [0..100] (jpeg only).
  * **clip** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Viewport`](#nodriver.cdp.page.Viewport)]) – *(Optional)* Capture the screenshot of a given region only.
  * **from_surface** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Capture the screenshot from the surface, rather than the view. Defaults to true.
  * **capture_beyond_viewport** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Capture the screenshot beyond the viewport. Defaults to false.
  * **optimize_for_speed** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Optimize image encoding for speed, not for resulting size (defaults to false)
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**
  Base64-encoded image data. (Encoded as a base64 string when passed over JSON)

### capture_snapshot(format_=None)

Returns a snapshot of the page as a string. For MHTML format, the serialization includes
iframes, shadow DOM, external resources, and element-inline styles.

**EXPERIMENTAL**

* **Parameters:**
  **format** – *(Optional)* Format (defaults to mhtml).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**
  Serialized page data.

### clear_compilation_cache()

Clears seeded compilation cache.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### clear_device_metrics_override()

Clears the overridden device metrics.
:rtype: [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

#### Deprecated
Deprecated since version 1.3.

### clear_device_orientation_override()

Clears the overridden Device Orientation.
:rtype: [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

#### Deprecated
Deprecated since version 1.3.

### clear_geolocation_override()

Clears the overridden Geolocation Position and Error.
:rtype: [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

#### Deprecated
Deprecated since version 1.3.

### close()

Tries to close page, running its beforeunload hooks, if any.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### crash()

Crashes renderer on the IO thread, generates minidumps.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### create_isolated_world(frame_id, world_name=None, grant_univeral_access=None)

Creates an isolated world for the given frame.

* **Parameters:**
  * **frame_id** ([`FrameId`](#nodriver.cdp.page.FrameId)) – Id of the frame in which the isolated world should be created.
  * **world_name** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* An optional name which is reported in the Execution Context.
  * **grant_univeral_access** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether or not universal access should be granted to the isolated world. This is a powerful option, use with caution.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`ExecutionContextId`](runtime.md#nodriver.cdp.runtime.ExecutionContextId)]
* **Returns:**
  Execution context of the isolated world.

### delete_cookie(cookie_name, url)

Deletes browser cookie with given name, domain and path.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  * **cookie_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Name of the cookie to remove.
  * **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – URL to match cooke domain and path.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### disable()

Disables page domain notifications.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable(enable_file_chooser_opened_event=None)

Enables page domain notifications.

* **Parameters:**
  **enable_file_chooser_opened_event** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* If true, the ``Page.fileChooserOpened``` event will be emitted regardless of the state set by ```Page.setInterceptFileChooserDialog`` command (default: false).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### generate_test_report(message, group=None)

Generates a report for testing.

**EXPERIMENTAL**

* **Parameters:**
  * **message** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Message to be displayed in the report.
  * **group** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Specifies the endpoint group to deliver the report to.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_ad_script_ancestry(frame_id)

**EXPERIMENTAL**

* **Parameters:**
  **frame_id** ([`FrameId`](#nodriver.cdp.page.FrameId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AdScriptAncestry`](#nodriver.cdp.page.AdScriptAncestry)]]
* **Returns:**
  *(Optional)* The ancestry chain of ad script identifiers leading to this frame’s creation, along with the root script’s filterlist rule. The ancestry chain is ordered from the most immediate script (in the frame creation stack) to more distant ancestors (that created the immediately preceding script). Only sent if frame is labelled as an ad and ids are available.

### get_app_id()

Returns the unique (PWA) app id.
Only returns values if the feature flag ‘WebAppEnableManifestId’ is enabled

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]]
* **Returns:**
  A tuple with the following items:
  1. **appId** - *(Optional)* App id, either from manifest’s id attribute or computed from start_url
  2. **recommendedId** - *(Optional)* Recommendation for manifest’s id attribute to match current id computed from start_url

### get_app_manifest(manifest_id=None)

Gets the processed manifest for this current document.
: This API always waits for the manifest to be loaded.
  If manifestId is provided, and it does not match the manifest of the
  <br/>
  > current document, this API errors out.
  <br/>
  If there is not a loaded page, this API errors out immediately.

* **Parameters:**
  **manifest_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)*
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AppManifestError`](#nodriver.cdp.page.AppManifestError)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AppManifestParsedProperties`](#nodriver.cdp.page.AppManifestParsedProperties)], [`WebAppManifest`](#nodriver.cdp.page.WebAppManifest)]]
* **Returns:**
  A tuple with the following items:
  1. **url** - Manifest location.
  2. **errors** -
  3. **data** - *(Optional)* Manifest content.
  4. **parsed** - *(Optional)* Parsed manifest properties. Deprecated, use manifest instead.
  5. **manifest** -

### get_frame_tree()

Returns present frame tree structure.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`FrameTree`](#nodriver.cdp.page.FrameTree)]
* **Returns:**
  Present frame tree structure.

### get_installability_errors()

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`InstallabilityError`](#nodriver.cdp.page.InstallabilityError)]]
* **Returns:**

### get_layout_metrics()

Returns metrics relating to the layouting of the page, such as viewport bounds/scale.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`LayoutViewport`](#nodriver.cdp.page.LayoutViewport), [`VisualViewport`](#nodriver.cdp.page.VisualViewport), [`Rect`](dom.md#nodriver.cdp.dom.Rect), [`LayoutViewport`](#nodriver.cdp.page.LayoutViewport), [`VisualViewport`](#nodriver.cdp.page.VisualViewport), [`Rect`](dom.md#nodriver.cdp.dom.Rect)]]
* **Returns:**
  A tuple with the following items:
  1. **layoutViewport** - Deprecated metrics relating to the layout viewport. Is in device pixels. Use `cssLayoutViewport` instead.
  2. **visualViewport** - Deprecated metrics relating to the visual viewport. Is in device pixels. Use `cssVisualViewport` instead.
  3. **contentSize** - Deprecated size of scrollable area. Is in DP. Use `cssContentSize` instead.
  4. **cssLayoutViewport** - Metrics relating to the layout viewport in CSS pixels.
  5. **cssVisualViewport** - Metrics relating to the visual viewport in CSS pixels.
  6. **cssContentSize** - Size of scrollable area in CSS pixels.

### get_manifest_icons()

Deprecated because it’s not guaranteed that the returned icon is in fact the one used for PWA installation.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**

#### Deprecated
Deprecated since version 1.3.

### get_navigation_history()

Returns navigation history for the current page.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`int`](https://docs.python.org/3/library/functions.html#int), [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NavigationEntry`](#nodriver.cdp.page.NavigationEntry)]]]
* **Returns:**
  A tuple with the following items:
  1. **currentIndex** - Index of the current navigation history entry.
  2. **entries** - Array of navigation history entries.

### get_origin_trials(frame_id)

Get Origin Trials on given frame.

**EXPERIMENTAL**

* **Parameters:**
  **frame_id** ([`FrameId`](#nodriver.cdp.page.FrameId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`OriginTrial`](#nodriver.cdp.page.OriginTrial)]]
* **Returns:**

### get_permissions_policy_state(frame_id)

Get Permissions Policy state on given frame.

**EXPERIMENTAL**

* **Parameters:**
  **frame_id** ([`FrameId`](#nodriver.cdp.page.FrameId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PermissionsPolicyFeatureState`](#nodriver.cdp.page.PermissionsPolicyFeatureState)]]
* **Returns:**

### get_resource_content(frame_id, url)

Returns content of the given resource.

**EXPERIMENTAL**

* **Parameters:**
  * **frame_id** ([`FrameId`](#nodriver.cdp.page.FrameId)) – Frame id to get resource for.
  * **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – URL of the resource to get content for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`bool`](https://docs.python.org/3/library/functions.html#bool)]]
* **Returns:**
  A tuple with the following items:
  1. **content** - Resource content.
  2. **base64Encoded** - True, if content was served as base64.

### get_resource_tree()

Returns present frame / resource tree structure.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`FrameResourceTree`](#nodriver.cdp.page.FrameResourceTree)]
* **Returns:**
  Present frame / resource tree structure.

### handle_java_script_dialog(accept, prompt_text=None)

Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload).

* **Parameters:**
  * **accept** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to accept or dismiss the dialog.
  * **prompt_text** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* The text to enter into the dialog prompt before accepting. Used only if this is a prompt dialog.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### navigate(url, referrer=None, transition_type=None, frame_id=None, referrer_policy=None)

Navigates current page to the given URL.

* **Parameters:**
  * **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – URL to navigate the page to.
  * **referrer** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Referrer URL.
  * **transition_type** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TransitionType`](#nodriver.cdp.page.TransitionType)]) – *(Optional)* Intended transition type.
  * **frame_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](#nodriver.cdp.page.FrameId)]) – *(Optional)* Frame id to navigate, if not specified navigates the top frame.
  * **referrer_policy** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ReferrerPolicy`](#nodriver.cdp.page.ReferrerPolicy)]) – **(EXPERIMENTAL)** *(Optional)* Referrer-policy used for the navigation.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`FrameId`](#nodriver.cdp.page.FrameId), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LoaderId`](network.md#nodriver.cdp.network.LoaderId)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]]]
* **Returns:**
  A tuple with the following items:
  1. **frameId** - Frame id that has navigated (or failed to navigate)
  2. **loaderId** - *(Optional)* Loader identifier. This is omitted in case of same-document navigation, as the previously committed loaderId would not change.
  3. **errorText** - *(Optional)* User friendly error message, present if and only if navigation has failed.
  4. **isDownload** - *(Optional)* Whether the navigation resulted in a download.

### navigate_to_history_entry(entry_id)

Navigates current page to the given history entry.

* **Parameters:**
  **entry_id** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Unique id of the entry to navigate to.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### print_to_pdf(landscape=None, display_header_footer=None, print_background=None, scale=None, paper_width=None, paper_height=None, margin_top=None, margin_bottom=None, margin_left=None, margin_right=None, page_ranges=None, header_template=None, footer_template=None, prefer_css_page_size=None, transfer_mode=None, generate_tagged_pdf=None, generate_document_outline=None)

Print page as PDF.

* **Parameters:**
  * **landscape** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Paper orientation. Defaults to false.
  * **display_header_footer** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Display header and footer. Defaults to false.
  * **print_background** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Print background graphics. Defaults to false.
  * **scale** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Scale of the webpage rendering. Defaults to 1.
  * **paper_width** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Paper width in inches. Defaults to 8.5 inches.
  * **paper_height** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Paper height in inches. Defaults to 11 inches.
  * **margin_top** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Top margin in inches. Defaults to 1cm (~0.4 inches).
  * **margin_bottom** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Bottom margin in inches. Defaults to 1cm (~0.4 inches).
  * **margin_left** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Left margin in inches. Defaults to 1cm (~0.4 inches).
  * **margin_right** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Right margin in inches. Defaults to 1cm (~0.4 inches).
  * **page_ranges** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Paper ranges to print, one based, e.g., ‘1-5, 8, 11-13’. Pages are printed in the document order, not in the order specified, and no more than once. Defaults to empty string, which implies the entire document is printed. The page numbers are quietly capped to actual page count of the document, and ranges beyond the end of the document are ignored. If this results in no pages to print, an error is reported. It is an error to specify a range with start greater than end.
  * **header_template** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values into them: - ``date```: formatted print date - ```title```: document title - ```url```: document location - ```pageNumber```: current page number - ```totalPages```: total pages in the document  For example, ```<span class=title></span>``` would generate span containing the title.
  * **footer_template** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* HTML template for the print footer. Should use the same format as the ```headerTemplate```.
  * **prefer_css_page_size** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether or not to prefer page size as defined by css. Defaults to false, in which case the content will be scaled to fit the paper size.
  * **transfer_mode** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* return as stream
  * **generate_tagged_pdf** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether or not to generate tagged (accessible) PDF. Defaults to embedder choice.
  * **generate_document_outline** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether or not to embed the document outline into the PDF.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StreamHandle`](io.md#nodriver.cdp.io.StreamHandle)]]]
* **Returns:**
  A tuple with the following items:
  1. **data** - Base64-encoded pdf data. Empty if \`\` returnAsStream\` is specified. (Encoded as a base64 string when passed over JSON)
  2. **stream** - *(Optional)* A handle of the stream that holds resulting PDF data.

### produce_compilation_cache(scripts)

Requests backend to produce compilation cache for the specified scripts.
`scripts` are appended to the list of scripts for which the cache
would be produced. The list may be reset during page navigation.
When script with a matching URL is encountered, the cache is optionally
produced upon backend discretion, based on internal heuristics.
See also: `Page.compilationCacheProduced`.

**EXPERIMENTAL**

* **Parameters:**
  **scripts** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CompilationCacheParams`](#nodriver.cdp.page.CompilationCacheParams)]) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### reload(ignore_cache=None, script_to_evaluate_on_load=None, loader_id=None)

Reloads given page optionally ignoring the cache.

* **Parameters:**
  * **ignore_cache** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, browser cache is ignored (as if the user pressed Shift+refresh).
  * **script_to_evaluate_on_load** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If set, the script will be injected into all frames of the inspected page after reload. Argument will be ignored if reloading dataURL origin.
  * **loader_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LoaderId`](network.md#nodriver.cdp.network.LoaderId)]) – **(EXPERIMENTAL)** *(Optional)* If set, an error will be thrown if the target page’s main frame’s loader id does not match the provided id. This prevents accidentally reloading an unintended target in case there’s a racing navigation.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### remove_script_to_evaluate_on_load(identifier)

Deprecated, please use removeScriptToEvaluateOnNewDocument instead.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  **identifier** ([`ScriptIdentifier`](#nodriver.cdp.page.ScriptIdentifier)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### remove_script_to_evaluate_on_new_document(identifier)

Removes given script from the list.

* **Parameters:**
  **identifier** ([`ScriptIdentifier`](#nodriver.cdp.page.ScriptIdentifier)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### reset_navigation_history()

Resets navigation history for the current page.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### screencast_frame_ack(session_id)

Acknowledges that a screencast frame has been received by the frontend.

**EXPERIMENTAL**

* **Parameters:**
  **session_id** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Frame number.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### search_in_resource(frame_id, url, query, case_sensitive=None, is_regex=None)

Searches for given string in resource content.

**EXPERIMENTAL**

* **Parameters:**
  * **frame_id** ([`FrameId`](#nodriver.cdp.page.FrameId)) – Frame id for resource to search in.
  * **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – URL of the resource to search in.
  * **query** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – String to search for.
  * **case_sensitive** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, search is case sensitive.
  * **is_regex** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, treats string parameter as regex.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SearchMatch`](debugger.md#nodriver.cdp.debugger.SearchMatch)]]
* **Returns:**
  List of search matches.

### set_ad_blocking_enabled(enabled)

Enable Chrome’s experimental ad filter on all sites.

**EXPERIMENTAL**

* **Parameters:**
  **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to block ads.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_bypass_csp(enabled)

Enable page Content Security Policy by-passing.

* **Parameters:**
  **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to bypass page CSP.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_device_metrics_override(width, height, device_scale_factor, mobile, scale=None, screen_width=None, screen_height=None, position_x=None, position_y=None, dont_set_visible_size=None, screen_orientation=None, viewport=None)

Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
window.innerWidth, window.innerHeight, and “device-width”/”device-height”-related CSS media
query results).

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  * **width** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
  * **height** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
  * **device_scale_factor** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Overriding device scale factor value. 0 disables the override.
  * **mobile** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more.
  * **scale** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Scale to apply to resulting view image.
  * **screen_width** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Overriding screen width value in pixels (minimum 0, maximum 10000000).
  * **screen_height** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Overriding screen height value in pixels (minimum 0, maximum 10000000).
  * **position_x** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
  * **position_y** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
  * **dont_set_visible_size** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Do not set visible view size, rely upon explicit setVisibleSize call.
  * **screen_orientation** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ScreenOrientation`](emulation.md#nodriver.cdp.emulation.ScreenOrientation)]) – *(Optional)* Screen orientation override.
  * **viewport** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Viewport`](#nodriver.cdp.page.Viewport)]) – *(Optional)* The viewport dimensions and scale. If not set, the override is cleared.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### set_device_orientation_override(alpha, beta, gamma)

Overrides the Device Orientation.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  * **alpha** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Mock alpha
  * **beta** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Mock beta
  * **gamma** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Mock gamma
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### set_document_content(frame_id, html)

Sets given markup as the document’s HTML.

* **Parameters:**
  * **frame_id** ([`FrameId`](#nodriver.cdp.page.FrameId)) – Frame id to set HTML for.
  * **html** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – HTML content to set.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_download_behavior(behavior, download_path=None)

Set the behavior when downloading a file.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  * **behavior** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Whether to allow all or deny all download requests, or use default Chrome behavior if available (otherwise deny).
  * **download_path** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* The default path to save downloaded files to. This is required if behavior is set to ‘allow’
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### set_font_families(font_families, for_scripts=None)

Set generic font families.

**EXPERIMENTAL**

* **Parameters:**
  * **font_families** ([`FontFamilies`](#nodriver.cdp.page.FontFamilies)) – Specifies font families to set. If a font family is not specified, it won’t be changed.
  * **for_scripts** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ScriptFontFamilies`](#nodriver.cdp.page.ScriptFontFamilies)]]) – *(Optional)* Specifies font families to set for individual scripts.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_font_sizes(font_sizes)

Set default font sizes.

**EXPERIMENTAL**

* **Parameters:**
  **font_sizes** ([`FontSizes`](#nodriver.cdp.page.FontSizes)) – Specifies font sizes to set. If a font size is not specified, it won’t be changed.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_geolocation_override(latitude=None, longitude=None, accuracy=None)

Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
unavailable.

#### Deprecated
Deprecated since version 1.3.

* **Parameters:**
  * **latitude** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Mock latitude
  * **longitude** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Mock longitude
  * **accuracy** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* Mock accuracy
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### set_intercept_file_chooser_dialog(enabled, cancel=None)

Intercept file chooser requests and transfer control to protocol clients.
When file chooser interception is enabled, native file chooser dialog is not shown.
Instead, a protocol event `Page.fileChooserOpened` is emitted.

* **Parameters:**
  * **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
  * **cancel** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* If true, cancels the dialog by emitting relevant events (if any) in addition to not showing it if the interception is enabled (default: false).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_lifecycle_events_enabled(enabled)

Controls whether page will emit lifecycle events.

* **Parameters:**
  **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – If true, starts emitting lifecycle events.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_prerendering_allowed(is_allowed)

Enable/disable prerendering manually.

This command is a short-term solution for [https://crbug.com/1440085](https://crbug.com/1440085).
See [https://docs.google.com/document/d/12HVmFxYj5Jc-eJr5OmWsa2bqTJsbgGLKI6ZIyx0_wpA](https://docs.google.com/document/d/12HVmFxYj5Jc-eJr5OmWsa2bqTJsbgGLKI6ZIyx0_wpA)
for more details.

TODO([https://crbug.com/1440085](https://crbug.com/1440085)): Remove this once Puppeteer supports tab targets.

**EXPERIMENTAL**

* **Parameters:**
  **is_allowed** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_rph_registration_mode(mode)

Extensions for Custom Handlers API:
[https://html.spec.whatwg.org/multipage/system-state.html#rph-automation](https://html.spec.whatwg.org/multipage/system-state.html#rph-automation)

**EXPERIMENTAL**

* **Parameters:**
  **mode** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_spc_transaction_mode(mode)

Sets the Secure Payment Confirmation transaction mode.
[https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode](https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode)

**EXPERIMENTAL**

* **Parameters:**
  **mode** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_touch_emulation_enabled(enabled, configuration=None)

Toggles mouse event-based touch event emulation.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  * **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether the touch event emulation should be enabled.
  * **configuration** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Touch/gesture events configuration. Default: current platform.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### set_web_lifecycle_state(state)

Tries to update the web lifecycle state of the page.
It will transition the page to the given state according to:
[https://github.com/WICG/web-lifecycle/](https://github.com/WICG/web-lifecycle/)

**EXPERIMENTAL**

* **Parameters:**
  **state** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Target lifecycle state
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### start_screencast(format_=None, quality=None, max_width=None, max_height=None, every_nth_frame=None)

Starts sending each frame using the `screencastFrame` event.

**EXPERIMENTAL**

* **Parameters:**
  * **format** – *(Optional)* Image compression format.
  * **quality** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Compression quality from range [0..100].
  * **max_width** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Maximum screenshot width.
  * **max_height** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Maximum screenshot height.
  * **every_nth_frame** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Send every n-th frame.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### stop_loading()

Force the page stop all navigations and pending resource fetches.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### stop_screencast()

Stops sending each frame in the `screencastFrame`.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### wait_for_debugger()

Pauses page execution. Can be resumed using generic Runtime.runIfWaitingForDebugger.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* DomContentEventFired(timestamp)

#### timestamp*: [`MonotonicTime`](network.md#nodriver.cdp.network.MonotonicTime)*

### *class* FileChooserOpened(frame_id, mode, backend_node_id)

Emitted only when `page.interceptFileChooser` is enabled.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Id of the frame containing input node.

#### mode*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Input mode.

#### backend_node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]*

Input node id. Only present for file choosers opened via an `<input type="file">` element.

### *class* FrameAttached(frame_id, parent_frame_id, stack)

Fired when frame has been attached to its parent.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Id of the frame that has been attached.

#### parent_frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Parent frame identifier.

#### stack*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTrace`](runtime.md#nodriver.cdp.runtime.StackTrace)]*

JavaScript stack trace of when frame was attached, only set if frame initiated from script.

### *class* FrameClearedScheduledNavigation(frame_id)

Fired when frame no longer has a scheduled navigation.

#### Deprecated
Deprecated since version 1.3.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Id of the frame that has cleared its scheduled navigation.

### *class* FrameDetached(frame_id, reason)

Fired when frame has been detached from its parent.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Id of the frame that has been detached.

#### reason*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* FrameSubtreeWillBeDetached(frame_id)

**EXPERIMENTAL**

Fired before frame subtree is detached. Emitted before any frame of the
subtree is actually detached.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Id of the frame that is the root of the subtree that will be detached.

### *class* FrameNavigated(frame, type_)

Fired once navigation of the frame has completed. Frame is now associated with the new loader.

#### frame*: [`Frame`](#nodriver.cdp.page.Frame)*

Frame object.

#### type_*: [`NavigationType`](#nodriver.cdp.page.NavigationType)*

### *class* DocumentOpened(frame)

**EXPERIMENTAL**

Fired when opening document to write to.

#### frame*: [`Frame`](#nodriver.cdp.page.Frame)*

Frame object.

### *class* FrameResized

**EXPERIMENTAL**

### *class* FrameStartedNavigating(frame_id, url, loader_id, navigation_type)

**EXPERIMENTAL**

Fired when a navigation starts. This event is fired for both
renderer-initiated and browser-initiated navigations. For renderer-initiated
navigations, the event is fired after `frameRequestedNavigation`.
Navigation may still be cancelled after the event is issued. Multiple events
can be fired for a single navigation, for example, when a same-document
navigation becomes a cross-document navigation (such as in the case of a
frameset).

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

ID of the frame that is being navigated.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The URL the navigation started with. The final URL can be different.

#### loader_id*: [`LoaderId`](network.md#nodriver.cdp.network.LoaderId)*

Loader identifier. Even though it is present in case of same-document
navigation, the previously committed loaderId would not change unless
the navigation changes from a same-document to a cross-document
navigation.

#### navigation_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* FrameRequestedNavigation(frame_id, reason, url, disposition)

**EXPERIMENTAL**

Fired when a renderer-initiated navigation is requested.
Navigation may still be cancelled after the event is issued.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Id of the frame that is being navigated.

#### reason*: [`ClientNavigationReason`](#nodriver.cdp.page.ClientNavigationReason)*

The reason for the navigation.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The destination URL for the requested navigation.

#### disposition*: [`ClientNavigationDisposition`](#nodriver.cdp.page.ClientNavigationDisposition)*

The disposition for the navigation.

### *class* FrameScheduledNavigation(frame_id, delay, reason, url)

Fired when frame schedules a potential navigation.

#### Deprecated
Deprecated since version 1.3.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Id of the frame that has scheduled a navigation.

#### delay*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Delay (in seconds) until the navigation is scheduled to begin. The navigation is not
guaranteed to start.

#### reason*: [`ClientNavigationReason`](#nodriver.cdp.page.ClientNavigationReason)*

The reason for the navigation.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The destination URL for the scheduled navigation.

### *class* FrameStartedLoading(frame_id)

**EXPERIMENTAL**

Fired when frame has started loading.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Id of the frame that has started loading.

### *class* FrameStoppedLoading(frame_id)

**EXPERIMENTAL**

Fired when frame has stopped loading.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Id of the frame that has stopped loading.

### *class* DownloadWillBegin(frame_id, guid, url, suggested_filename)

**EXPERIMENTAL**

Fired when page is about to start a download.
Deprecated. Use Browser.downloadWillBegin instead.

#### Deprecated
Deprecated since version 1.3.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Id of the frame that caused download to begin.

#### guid*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Global unique identifier of the download.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL of the resource being downloaded.

#### suggested_filename*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Suggested file name of the resource (the actual name of the file saved on disk may differ).

### *class* DownloadProgress(guid, total_bytes, received_bytes, state)

**EXPERIMENTAL**

Fired when download makes progress. Last call has `done` == true.
Deprecated. Use Browser.downloadProgress instead.

#### Deprecated
Deprecated since version 1.3.

#### guid*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Global unique identifier of the download.

#### total_bytes*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Total expected bytes to download.

#### received_bytes*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Total bytes received.

#### state*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Download status.

### *class* InterstitialHidden

Fired when interstitial page was hidden

### *class* InterstitialShown

Fired when interstitial page was shown

### *class* JavascriptDialogClosed(frame_id, result, user_input)

Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been
closed.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Frame id.

#### result*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether dialog was confirmed.

#### user_input*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

User input in case of prompt.

### *class* JavascriptDialogOpening(url, frame_id, message, type_, has_browser_handler, default_prompt)

Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to
open.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Frame url.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Frame id.

#### message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Message that will be displayed by the dialog.

#### type_*: [`DialogType`](#nodriver.cdp.page.DialogType)*

Dialog type.

#### has_browser_handler*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True iff browser is capable showing or acting on the given dialog. When browser has no
dialog handler for given target, calling alert while Page domain is engaged will stall
the page execution. Execution can be resumed via calling Page.handleJavaScriptDialog.

#### default_prompt*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Default dialog prompt.

### *class* LifecycleEvent(frame_id, loader_id, name, timestamp)

Fired for lifecycle events (navigation, load, paint, etc) in the current
target (including local frames).

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Id of the frame.

#### loader_id*: [`LoaderId`](network.md#nodriver.cdp.network.LoaderId)*

Loader identifier. Empty string if the request is fetched from worker.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### timestamp*: [`MonotonicTime`](network.md#nodriver.cdp.network.MonotonicTime)*

### *class* BackForwardCacheNotUsed(loader_id, frame_id, not_restored_explanations, not_restored_explanations_tree)

**EXPERIMENTAL**

Fired for failed bfcache history navigations if BackForwardCache feature is enabled. Do
not assume any ordering with the Page.frameNavigated event. This event is fired only for
main-frame history navigation where the document changes (non-same-document navigations),
when bfcache navigation fails.

#### loader_id*: [`LoaderId`](network.md#nodriver.cdp.network.LoaderId)*

The loader id for the associated navigation.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

The frame id of the associated frame.

#### not_restored_explanations*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BackForwardCacheNotRestoredExplanation`](#nodriver.cdp.page.BackForwardCacheNotRestoredExplanation)]*

Array of reasons why the page could not be cached. This must not be empty.

#### not_restored_explanations_tree*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackForwardCacheNotRestoredExplanationTree`](#nodriver.cdp.page.BackForwardCacheNotRestoredExplanationTree)]*

Tree structure of reasons why the page could not be cached for each frame.

### *class* LoadEventFired(timestamp)

#### timestamp*: [`MonotonicTime`](network.md#nodriver.cdp.network.MonotonicTime)*

### *class* NavigatedWithinDocument(frame_id, url, navigation_type)

**EXPERIMENTAL**

Fired when same-document navigation happens, e.g. due to history API usage or anchor navigation.

#### frame_id*: [`FrameId`](#nodriver.cdp.page.FrameId)*

Id of the frame.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Frame’s new url.

#### navigation_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Navigation type

### *class* ScreencastFrame(data, metadata, session_id)

**EXPERIMENTAL**

Compressed image data requested by the `startScreencast`.

#### data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Base64-encoded compressed image. (Encoded as a base64 string when passed over JSON)

#### metadata*: [`ScreencastFrameMetadata`](#nodriver.cdp.page.ScreencastFrameMetadata)*

Screencast frame metadata.

#### session_id*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Frame number.

### *class* ScreencastVisibilityChanged(visible)

**EXPERIMENTAL**

Fired when the page with currently enabled screencast was shown or hidden .

#### visible*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if the page is visible.

### *class* WindowOpen(url, window_name, window_features, user_gesture)

Fired when a new window is going to be opened, via window.open(), link click, form submission,
etc.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The URL for the new window.

#### window_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Window name.

#### window_features*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

An array of enabled window features.

#### user_gesture*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether or not it was triggered by user gesture.

### *class* CompilationCacheProduced(url, data)

**EXPERIMENTAL**

Issued for every compilation cache generated.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Base64-encoded data (Encoded as a base64 string when passed over JSON)
