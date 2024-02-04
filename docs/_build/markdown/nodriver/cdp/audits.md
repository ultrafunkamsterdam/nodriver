# Audits

Audits domain allows investigation of page violations and possible improvements.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.audits"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* AffectedCookie(name, path, domain)

Information about a cookie that is affected by an inspector issue.

* **Parameters:**
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **domain** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### domain*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The following three properties uniquely identify a cookie

#### path*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* AffectedRequest(request_id, url=None)

Information about a request that is affected by an inspector issue.

* **Parameters:**
  * **request_id** ([*RequestId*](network.md#nodriver.cdp.network.RequestId)) – 
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### request_id*: [`RequestId`](network.md#nodriver.cdp.network.RequestId)*

The unique request id.

#### url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* AffectedFrame(frame_id)

Information about the frame affected by an inspector issue.

* **Parameters:**
  **frame_id** ([*FrameId*](page.md#nodriver.cdp.page.FrameId)) – 

#### frame_id*: [`FrameId`](page.md#nodriver.cdp.page.FrameId)*

### *class* CookieExclusionReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### EXCLUDE_DOMAIN_NON_ASCII *= 'ExcludeDomainNonASCII'*

#### EXCLUDE_INVALID_SAME_PARTY *= 'ExcludeInvalidSameParty'*

#### EXCLUDE_SAME_PARTY_CROSS_PARTY_CONTEXT *= 'ExcludeSamePartyCrossPartyContext'*

#### EXCLUDE_SAME_SITE_LAX *= 'ExcludeSameSiteLax'*

#### EXCLUDE_SAME_SITE_NONE_INSECURE *= 'ExcludeSameSiteNoneInsecure'*

#### EXCLUDE_SAME_SITE_STRICT *= 'ExcludeSameSiteStrict'*

#### EXCLUDE_SAME_SITE_UNSPECIFIED_TREATED_AS_LAX *= 'ExcludeSameSiteUnspecifiedTreatedAsLax'*

#### EXCLUDE_THIRD_PARTY_COOKIE_BLOCKED_IN_FIRST_PARTY_SET *= 'ExcludeThirdPartyCookieBlockedInFirstPartySet'*

#### EXCLUDE_THIRD_PARTY_PHASEOUT *= 'ExcludeThirdPartyPhaseout'*

### *class* CookieWarningReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### WARN_ATTRIBUTE_VALUE_EXCEEDS_MAX_SIZE *= 'WarnAttributeValueExceedsMaxSize'*

#### WARN_CROSS_SITE_REDIRECT_DOWNGRADE_CHANGES_INCLUSION *= 'WarnCrossSiteRedirectDowngradeChangesInclusion'*

#### WARN_DOMAIN_NON_ASCII *= 'WarnDomainNonASCII'*

#### WARN_SAME_SITE_LAX_CROSS_DOWNGRADE_LAX *= 'WarnSameSiteLaxCrossDowngradeLax'*

#### WARN_SAME_SITE_LAX_CROSS_DOWNGRADE_STRICT *= 'WarnSameSiteLaxCrossDowngradeStrict'*

#### WARN_SAME_SITE_NONE_INSECURE *= 'WarnSameSiteNoneInsecure'*

#### WARN_SAME_SITE_STRICT_CROSS_DOWNGRADE_LAX *= 'WarnSameSiteStrictCrossDowngradeLax'*

#### WARN_SAME_SITE_STRICT_CROSS_DOWNGRADE_STRICT *= 'WarnSameSiteStrictCrossDowngradeStrict'*

#### WARN_SAME_SITE_STRICT_LAX_DOWNGRADE_STRICT *= 'WarnSameSiteStrictLaxDowngradeStrict'*

#### WARN_SAME_SITE_UNSPECIFIED_CROSS_SITE_CONTEXT *= 'WarnSameSiteUnspecifiedCrossSiteContext'*

#### WARN_SAME_SITE_UNSPECIFIED_LAX_ALLOW_UNSAFE *= 'WarnSameSiteUnspecifiedLaxAllowUnsafe'*

#### WARN_THIRD_PARTY_PHASEOUT *= 'WarnThirdPartyPhaseout'*

### *class* CookieOperation(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### READ_COOKIE *= 'ReadCookie'*

#### SET_COOKIE *= 'SetCookie'*

### *class* CookieIssueDetails(cookie_warning_reasons, cookie_exclusion_reasons, operation, cookie=None, raw_cookie_line=None, site_for_cookies=None, cookie_url=None, request=None)

This information is currently necessary, as the front-end has a difficult
time finding a specific cookie. With this, we can convey specific error
information without the cookie.

* **Parameters:**
  * **cookie_warning_reasons** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*CookieWarningReason*](#nodriver.cdp.audits.CookieWarningReason)*]*) – 
  * **cookie_exclusion_reasons** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*CookieExclusionReason*](#nodriver.cdp.audits.CookieExclusionReason)*]*) – 
  * **operation** ([*CookieOperation*](#nodriver.cdp.audits.CookieOperation)) – 
  * **cookie** ([*AffectedCookie*](#nodriver.cdp.audits.AffectedCookie) *|* *None*) – 
  * **raw_cookie_line** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **site_for_cookies** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **cookie_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **request** ([*AffectedRequest*](#nodriver.cdp.audits.AffectedRequest) *|* *None*) – 

#### cookie*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AffectedCookie`](#nodriver.cdp.audits.AffectedCookie)]* *= None*

If AffectedCookie is not set then rawCookieLine contains the raw
Set-Cookie header string. This hints at a problem where the
cookie line is syntactically or semantically malformed in a way
that no valid cookie could be created.

#### cookie_exclusion_reasons*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CookieExclusionReason`](#nodriver.cdp.audits.CookieExclusionReason)]*

#### cookie_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### cookie_warning_reasons*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CookieWarningReason`](#nodriver.cdp.audits.CookieWarningReason)]*

#### operation*: [`CookieOperation`](#nodriver.cdp.audits.CookieOperation)*

Optionally identifies the site-for-cookies and the cookie url, which
may be used by the front-end as additional context.

#### raw_cookie_line*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### request*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AffectedRequest`](#nodriver.cdp.audits.AffectedRequest)]* *= None*

#### site_for_cookies*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* MixedContentResolutionStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### MIXED_CONTENT_AUTOMATICALLY_UPGRADED *= 'MixedContentAutomaticallyUpgraded'*

#### MIXED_CONTENT_BLOCKED *= 'MixedContentBlocked'*

#### MIXED_CONTENT_WARNING *= 'MixedContentWarning'*

### *class* MixedContentResourceType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### ATTRIBUTION_SRC *= 'AttributionSrc'*

#### AUDIO *= 'Audio'*

#### BEACON *= 'Beacon'*

#### CSP_REPORT *= 'CSPReport'*

#### DOWNLOAD *= 'Download'*

#### EVENT_SOURCE *= 'EventSource'*

#### FAVICON *= 'Favicon'*

#### FONT *= 'Font'*

#### FORM *= 'Form'*

#### FRAME *= 'Frame'*

#### IMAGE *= 'Image'*

#### IMPORT *= 'Import'*

#### MANIFEST *= 'Manifest'*

#### PING *= 'Ping'*

#### PLUGIN_DATA *= 'PluginData'*

#### PLUGIN_RESOURCE *= 'PluginResource'*

#### PREFETCH *= 'Prefetch'*

#### RESOURCE *= 'Resource'*

#### SCRIPT *= 'Script'*

#### SERVICE_WORKER *= 'ServiceWorker'*

#### SHARED_WORKER *= 'SharedWorker'*

#### SPECULATION_RULES *= 'SpeculationRules'*

#### STYLESHEET *= 'Stylesheet'*

#### TRACK *= 'Track'*

#### VIDEO *= 'Video'*

#### WORKER *= 'Worker'*

#### XML_HTTP_REQUEST *= 'XMLHttpRequest'*

#### XSLT *= 'XSLT'*

### *class* MixedContentIssueDetails(resolution_status, insecure_url, main_resource_url, resource_type=None, request=None, frame=None)

* **Parameters:**
  * **resolution_status** ([*MixedContentResolutionStatus*](#nodriver.cdp.audits.MixedContentResolutionStatus)) – 
  * **insecure_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **main_resource_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **resource_type** ([*MixedContentResourceType*](#nodriver.cdp.audits.MixedContentResourceType) *|* *None*) – 
  * **request** ([*AffectedRequest*](#nodriver.cdp.audits.AffectedRequest) *|* *None*) – 
  * **frame** ([*AffectedFrame*](#nodriver.cdp.audits.AffectedFrame) *|* *None*) – 

#### frame*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AffectedFrame`](#nodriver.cdp.audits.AffectedFrame)]* *= None*

Optional because not every mixed content issue is necessarily linked to a frame.

#### insecure_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The unsafe http url causing the mixed content issue.

#### main_resource_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The url responsible for the call to an unsafe url.

#### request*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AffectedRequest`](#nodriver.cdp.audits.AffectedRequest)]* *= None*

The mixed content request.
Does not always exist (e.g. for unsafe form submission urls).

#### resolution_status*: [`MixedContentResolutionStatus`](#nodriver.cdp.audits.MixedContentResolutionStatus)*

The way the mixed content issue is being resolved.

#### resource_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`MixedContentResourceType`](#nodriver.cdp.audits.MixedContentResourceType)]* *= None*

The type of resource causing the mixed content issue (css, js, iframe,
form,…). Marked as optional because it is mapped to from
blink::mojom::RequestContextType, which will be replaced
by network::mojom::RequestDestination

### *class* BlockedByResponseReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum indicating the reason a response has been blocked. These reasons are
refinements of the net error BLOCKED_BY_RESPONSE.

#### COEP_FRAME_RESOURCE_NEEDS_COEP_HEADER *= 'CoepFrameResourceNeedsCoepHeader'*

#### COOP_SANDBOXED_I_FRAME_CANNOT_NAVIGATE_TO_COOP_PAGE *= 'CoopSandboxedIFrameCannotNavigateToCoopPage'*

#### CORP_NOT_SAME_ORIGIN *= 'CorpNotSameOrigin'*

#### CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP *= 'CorpNotSameOriginAfterDefaultedToSameOriginByCoep'*

#### CORP_NOT_SAME_SITE *= 'CorpNotSameSite'*

### *class* BlockedByResponseIssueDetails(request, reason, parent_frame=None, blocked_frame=None)

Details for a request that has been blocked with the BLOCKED_BY_RESPONSE
code. Currently only used for COEP/COOP, but may be extended to include
some CSP errors in the future.

* **Parameters:**
  * **request** ([*AffectedRequest*](#nodriver.cdp.audits.AffectedRequest)) – 
  * **reason** ([*BlockedByResponseReason*](#nodriver.cdp.audits.BlockedByResponseReason)) – 
  * **parent_frame** ([*AffectedFrame*](#nodriver.cdp.audits.AffectedFrame) *|* *None*) – 
  * **blocked_frame** ([*AffectedFrame*](#nodriver.cdp.audits.AffectedFrame) *|* *None*) – 

#### blocked_frame*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AffectedFrame`](#nodriver.cdp.audits.AffectedFrame)]* *= None*

#### parent_frame*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AffectedFrame`](#nodriver.cdp.audits.AffectedFrame)]* *= None*

#### reason*: [`BlockedByResponseReason`](#nodriver.cdp.audits.BlockedByResponseReason)*

#### request*: [`AffectedRequest`](#nodriver.cdp.audits.AffectedRequest)*

### *class* HeavyAdResolutionStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### HEAVY_AD_BLOCKED *= 'HeavyAdBlocked'*

#### HEAVY_AD_WARNING *= 'HeavyAdWarning'*

### *class* HeavyAdReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### CPU_PEAK_LIMIT *= 'CpuPeakLimit'*

#### CPU_TOTAL_LIMIT *= 'CpuTotalLimit'*

#### NETWORK_TOTAL_LIMIT *= 'NetworkTotalLimit'*

### *class* HeavyAdIssueDetails(resolution, reason, frame)

* **Parameters:**
  * **resolution** ([*HeavyAdResolutionStatus*](#nodriver.cdp.audits.HeavyAdResolutionStatus)) – 
  * **reason** ([*HeavyAdReason*](#nodriver.cdp.audits.HeavyAdReason)) – 
  * **frame** ([*AffectedFrame*](#nodriver.cdp.audits.AffectedFrame)) – 

#### frame*: [`AffectedFrame`](#nodriver.cdp.audits.AffectedFrame)*

The frame that was blocked.

#### reason*: [`HeavyAdReason`](#nodriver.cdp.audits.HeavyAdReason)*

The reason the ad was blocked, total network or cpu or peak cpu.

#### resolution*: [`HeavyAdResolutionStatus`](#nodriver.cdp.audits.HeavyAdResolutionStatus)*

The resolution status, either blocking the content or warning.

### *class* ContentSecurityPolicyViolationType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### K_EVAL_VIOLATION *= 'kEvalViolation'*

#### K_INLINE_VIOLATION *= 'kInlineViolation'*

#### K_TRUSTED_TYPES_POLICY_VIOLATION *= 'kTrustedTypesPolicyViolation'*

#### K_TRUSTED_TYPES_SINK_VIOLATION *= 'kTrustedTypesSinkViolation'*

#### K_URL_VIOLATION *= 'kURLViolation'*

#### K_WASM_EVAL_VIOLATION *= 'kWasmEvalViolation'*

### *class* SourceCodeLocation(url, line_number, column_number, script_id=None)

* **Parameters:**
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **line_number** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **column_number** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **script_id** ([*ScriptId*](runtime.md#nodriver.cdp.runtime.ScriptId) *|* *None*) – 

#### column_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

#### line_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

#### script_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ScriptId`](runtime.md#nodriver.cdp.runtime.ScriptId)]* *= None*

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* ContentSecurityPolicyIssueDetails(violated_directive, is_report_only, content_security_policy_violation_type, blocked_url=None, frame_ancestor=None, source_code_location=None, violating_node_id=None)

* **Parameters:**
  * **violated_directive** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **is_report_only** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **content_security_policy_violation_type** ([*ContentSecurityPolicyViolationType*](#nodriver.cdp.audits.ContentSecurityPolicyViolationType)) – 
  * **blocked_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **frame_ancestor** ([*AffectedFrame*](#nodriver.cdp.audits.AffectedFrame) *|* *None*) – 
  * **source_code_location** ([*SourceCodeLocation*](#nodriver.cdp.audits.SourceCodeLocation) *|* *None*) – 
  * **violating_node_id** ([*BackendNodeId*](dom.md#nodriver.cdp.dom.BackendNodeId) *|* *None*) – 

#### blocked_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The url not included in allowed sources.

#### content_security_policy_violation_type*: [`ContentSecurityPolicyViolationType`](#nodriver.cdp.audits.ContentSecurityPolicyViolationType)*

#### frame_ancestor*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AffectedFrame`](#nodriver.cdp.audits.AffectedFrame)]* *= None*

#### is_report_only*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### source_code_location*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceCodeLocation`](#nodriver.cdp.audits.SourceCodeLocation)]* *= None*

#### violated_directive*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Specific directive that is violated, causing the CSP issue.

#### violating_node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

### *class* SharedArrayBufferIssueType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### CREATION_ISSUE *= 'CreationIssue'*

#### TRANSFER_ISSUE *= 'TransferIssue'*

### *class* SharedArrayBufferIssueDetails(source_code_location, is_warning, type_)

Details for a issue arising from an SAB being instantiated in, or
transferred to a context that is not cross-origin isolated.

* **Parameters:**
  * **source_code_location** ([*SourceCodeLocation*](#nodriver.cdp.audits.SourceCodeLocation)) – 
  * **is_warning** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **type_** ([*SharedArrayBufferIssueType*](#nodriver.cdp.audits.SharedArrayBufferIssueType)) – 

#### is_warning*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### source_code_location*: [`SourceCodeLocation`](#nodriver.cdp.audits.SourceCodeLocation)*

#### type_*: [`SharedArrayBufferIssueType`](#nodriver.cdp.audits.SharedArrayBufferIssueType)*

### *class* LowTextContrastIssueDetails(violating_node_id, violating_node_selector, contrast_ratio, threshold_aa, threshold_aaa, font_size, font_weight)

* **Parameters:**
  * **violating_node_id** ([*BackendNodeId*](dom.md#nodriver.cdp.dom.BackendNodeId)) – 
  * **violating_node_selector** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **contrast_ratio** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **threshold_aa** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **threshold_aaa** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **font_size** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **font_weight** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### contrast_ratio*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### font_size*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### font_weight*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### threshold_aa*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### threshold_aaa*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### violating_node_id*: [`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)*

#### violating_node_selector*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* CorsIssueDetails(cors_error_status, is_warning, request, location=None, initiator_origin=None, resource_ip_address_space=None, client_security_state=None)

Details for a CORS related issue, e.g. a warning or error related to
CORS RFC1918 enforcement.

* **Parameters:**
  * **cors_error_status** ([*CorsErrorStatus*](network.md#nodriver.cdp.network.CorsErrorStatus)) – 
  * **is_warning** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **request** ([*AffectedRequest*](#nodriver.cdp.audits.AffectedRequest)) – 
  * **location** ([*SourceCodeLocation*](#nodriver.cdp.audits.SourceCodeLocation) *|* *None*) – 
  * **initiator_origin** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **resource_ip_address_space** ([*IPAddressSpace*](network.md#nodriver.cdp.network.IPAddressSpace) *|* *None*) – 
  * **client_security_state** ([*ClientSecurityState*](network.md#nodriver.cdp.network.ClientSecurityState) *|* *None*) – 

#### client_security_state*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ClientSecurityState`](network.md#nodriver.cdp.network.ClientSecurityState)]* *= None*

#### cors_error_status*: [`CorsErrorStatus`](network.md#nodriver.cdp.network.CorsErrorStatus)*

#### initiator_origin*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### is_warning*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### location*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceCodeLocation`](#nodriver.cdp.audits.SourceCodeLocation)]* *= None*

#### request*: [`AffectedRequest`](#nodriver.cdp.audits.AffectedRequest)*

#### resource_ip_address_space*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`IPAddressSpace`](network.md#nodriver.cdp.network.IPAddressSpace)]* *= None*

### *class* AttributionReportingIssueType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### INSECURE_CONTEXT *= 'InsecureContext'*

#### INVALID_HEADER *= 'InvalidHeader'*

#### INVALID_REGISTER_OS_SOURCE_HEADER *= 'InvalidRegisterOsSourceHeader'*

#### INVALID_REGISTER_OS_TRIGGER_HEADER *= 'InvalidRegisterOsTriggerHeader'*

#### INVALID_REGISTER_TRIGGER_HEADER *= 'InvalidRegisterTriggerHeader'*

#### NAVIGATION_REGISTRATION_WITHOUT_TRANSIENT_USER_ACTIVATION *= 'NavigationRegistrationWithoutTransientUserActivation'*

#### NO_WEB_OR_OS_SUPPORT *= 'NoWebOrOsSupport'*

#### OS_SOURCE_IGNORED *= 'OsSourceIgnored'*

#### OS_TRIGGER_IGNORED *= 'OsTriggerIgnored'*

#### PERMISSION_POLICY_DISABLED *= 'PermissionPolicyDisabled'*

#### SOURCE_AND_TRIGGER_HEADERS *= 'SourceAndTriggerHeaders'*

#### SOURCE_IGNORED *= 'SourceIgnored'*

#### TRIGGER_IGNORED *= 'TriggerIgnored'*

#### UNTRUSTWORTHY_REPORTING_ORIGIN *= 'UntrustworthyReportingOrigin'*

#### WEB_AND_OS_HEADERS *= 'WebAndOsHeaders'*

### *class* AttributionReportingIssueDetails(violation_type, request=None, violating_node_id=None, invalid_parameter=None)

Details for issues around “Attribution Reporting API” usage.
Explainer: [https://github.com/WICG/attribution-reporting-api](https://github.com/WICG/attribution-reporting-api)

* **Parameters:**
  * **violation_type** ([*AttributionReportingIssueType*](#nodriver.cdp.audits.AttributionReportingIssueType)) – 
  * **request** ([*AffectedRequest*](#nodriver.cdp.audits.AffectedRequest) *|* *None*) – 
  * **violating_node_id** ([*BackendNodeId*](dom.md#nodriver.cdp.dom.BackendNodeId) *|* *None*) – 
  * **invalid_parameter** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### invalid_parameter*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### request*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AffectedRequest`](#nodriver.cdp.audits.AffectedRequest)]* *= None*

#### violating_node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

#### violation_type*: [`AttributionReportingIssueType`](#nodriver.cdp.audits.AttributionReportingIssueType)*

### *class* QuirksModeIssueDetails(is_limited_quirks_mode, document_node_id, url, frame_id, loader_id)

Details for issues about documents in Quirks Mode
or Limited Quirks Mode that affects page layouting.

* **Parameters:**
  * **is_limited_quirks_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **document_node_id** ([*BackendNodeId*](dom.md#nodriver.cdp.dom.BackendNodeId)) – 
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **frame_id** ([*FrameId*](page.md#nodriver.cdp.page.FrameId)) – 
  * **loader_id** ([*LoaderId*](network.md#nodriver.cdp.network.LoaderId)) – 

#### document_node_id*: [`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)*

#### frame_id*: [`FrameId`](page.md#nodriver.cdp.page.FrameId)*

#### is_limited_quirks_mode*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

If false, it means the document’s mode is “quirks”
instead of “limited-quirks”.

#### loader_id*: [`LoaderId`](network.md#nodriver.cdp.network.LoaderId)*

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* NavigatorUserAgentIssueDetails(url, location=None)

* **Parameters:**
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **location** ([*SourceCodeLocation*](#nodriver.cdp.audits.SourceCodeLocation) *|* *None*) – 

#### location*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceCodeLocation`](#nodriver.cdp.audits.SourceCodeLocation)]* *= None*

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* GenericIssueErrorType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### CROSS_ORIGIN_PORTAL_POST_MESSAGE_ERROR *= 'CrossOriginPortalPostMessageError'*

#### FORM_ARIA_LABELLED_BY_TO_NON_EXISTING_ID *= 'FormAriaLabelledByToNonExistingId'*

#### FORM_AUTOCOMPLETE_ATTRIBUTE_EMPTY_ERROR *= 'FormAutocompleteAttributeEmptyError'*

#### FORM_DUPLICATE_ID_FOR_INPUT_ERROR *= 'FormDuplicateIdForInputError'*

#### FORM_EMPTY_ID_AND_NAME_ATTRIBUTES_FOR_INPUT_ERROR *= 'FormEmptyIdAndNameAttributesForInputError'*

#### FORM_INPUT_ASSIGNED_AUTOCOMPLETE_VALUE_TO_ID_OR_NAME_ATTRIBUTE_ERROR *= 'FormInputAssignedAutocompleteValueToIdOrNameAttributeError'*

#### FORM_INPUT_HAS_WRONG_BUT_WELL_INTENDED_AUTOCOMPLETE_VALUE_ERROR *= 'FormInputHasWrongButWellIntendedAutocompleteValueError'*

#### FORM_INPUT_WITH_NO_LABEL_ERROR *= 'FormInputWithNoLabelError'*

#### FORM_LABEL_FOR_MATCHES_NON_EXISTING_ID_ERROR *= 'FormLabelForMatchesNonExistingIdError'*

#### FORM_LABEL_FOR_NAME_ERROR *= 'FormLabelForNameError'*

#### FORM_LABEL_HAS_NEITHER_FOR_NOR_NESTED_INPUT *= 'FormLabelHasNeitherForNorNestedInput'*

#### RESPONSE_WAS_BLOCKED_BY_ORB *= 'ResponseWasBlockedByORB'*

### *class* GenericIssueDetails(error_type, frame_id=None, violating_node_id=None, violating_node_attribute=None, request=None)

Depending on the concrete errorType, different properties are set.

* **Parameters:**
  * **error_type** ([*GenericIssueErrorType*](#nodriver.cdp.audits.GenericIssueErrorType)) – 
  * **frame_id** ([*FrameId*](page.md#nodriver.cdp.page.FrameId) *|* *None*) – 
  * **violating_node_id** ([*BackendNodeId*](dom.md#nodriver.cdp.dom.BackendNodeId) *|* *None*) – 
  * **violating_node_attribute** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **request** ([*AffectedRequest*](#nodriver.cdp.audits.AffectedRequest) *|* *None*) – 

#### error_type*: [`GenericIssueErrorType`](#nodriver.cdp.audits.GenericIssueErrorType)*

Issues with the same errorType are aggregated in the frontend.

#### frame_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]* *= None*

#### request*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AffectedRequest`](#nodriver.cdp.audits.AffectedRequest)]* *= None*

#### violating_node_attribute*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### violating_node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

### *class* DeprecationIssueDetails(source_code_location, type_, affected_frame=None)

This issue tracks information needed to print a deprecation message.
[https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md](https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md)

* **Parameters:**
  * **source_code_location** ([*SourceCodeLocation*](#nodriver.cdp.audits.SourceCodeLocation)) – 
  * **type_** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **affected_frame** ([*AffectedFrame*](#nodriver.cdp.audits.AffectedFrame) *|* *None*) – 

#### affected_frame*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AffectedFrame`](#nodriver.cdp.audits.AffectedFrame)]* *= None*

#### source_code_location*: [`SourceCodeLocation`](#nodriver.cdp.audits.SourceCodeLocation)*

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

One of the deprecation names from third_party/blink/renderer/core/frame/deprecation/deprecation.json5

### *class* BounceTrackingIssueDetails(tracking_sites)

This issue warns about sites in the redirect chain of a finished navigation
that may be flagged as trackers and have their state cleared if they don’t
receive a user interaction. Note that in this context ‘site’ means eTLD+1.
For example, if the URL `https://example.test:80/bounce` was in the
redirect chain, the site reported would be `example.test`.

* **Parameters:**
  **tracking_sites** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 

#### tracking_sites*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

### *class* CookieDeprecationMetadataIssueDetails(allowed_sites)

This issue warns about third-party sites that are accessing cookies on the
current page, and have been permitted due to having a global metadata grant.
Note that in this context ‘site’ means eTLD+1. For example, if the URL
`https://example.test:80/web_page` was accessing cookies, the site reported
would be `example.test`.

* **Parameters:**
  **allowed_sites** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 

#### allowed_sites*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

### *class* ClientHintIssueReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### META_TAG_ALLOW_LIST_INVALID_ORIGIN *= 'MetaTagAllowListInvalidOrigin'*

#### META_TAG_MODIFIED_HTML *= 'MetaTagModifiedHTML'*

### *class* FederatedAuthRequestIssueDetails(federated_auth_request_issue_reason)

* **Parameters:**
  **federated_auth_request_issue_reason** ([*FederatedAuthRequestIssueReason*](#nodriver.cdp.audits.FederatedAuthRequestIssueReason)) – 

#### federated_auth_request_issue_reason*: [`FederatedAuthRequestIssueReason`](#nodriver.cdp.audits.FederatedAuthRequestIssueReason)*

### *class* FederatedAuthRequestIssueReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Represents the failure reason when a federated authentication reason fails.
Should be updated alongside RequestIdTokenStatus in
third_party/blink/public/mojom/devtools/inspector_issue.mojom to include
all cases except for success.

#### ACCOUNTS_HTTP_NOT_FOUND *= 'AccountsHttpNotFound'*

#### ACCOUNTS_INVALID_CONTENT_TYPE *= 'AccountsInvalidContentType'*

#### ACCOUNTS_INVALID_RESPONSE *= 'AccountsInvalidResponse'*

#### ACCOUNTS_LIST_EMPTY *= 'AccountsListEmpty'*

#### ACCOUNTS_NO_RESPONSE *= 'AccountsNoResponse'*

#### CANCELED *= 'Canceled'*

#### CLIENT_METADATA_HTTP_NOT_FOUND *= 'ClientMetadataHttpNotFound'*

#### CLIENT_METADATA_INVALID_CONTENT_TYPE *= 'ClientMetadataInvalidContentType'*

#### CLIENT_METADATA_INVALID_RESPONSE *= 'ClientMetadataInvalidResponse'*

#### CLIENT_METADATA_NO_RESPONSE *= 'ClientMetadataNoResponse'*

#### CONFIG_HTTP_NOT_FOUND *= 'ConfigHttpNotFound'*

#### CONFIG_INVALID_CONTENT_TYPE *= 'ConfigInvalidContentType'*

#### CONFIG_INVALID_RESPONSE *= 'ConfigInvalidResponse'*

#### CONFIG_NOT_IN_WELL_KNOWN *= 'ConfigNotInWellKnown'*

#### CONFIG_NO_RESPONSE *= 'ConfigNoResponse'*

#### DISABLED_IN_SETTINGS *= 'DisabledInSettings'*

#### ERROR_FETCHING_SIGNIN *= 'ErrorFetchingSignin'*

#### ERROR_ID_TOKEN *= 'ErrorIdToken'*

#### ID_TOKEN_CROSS_SITE_IDP_ERROR_RESPONSE *= 'IdTokenCrossSiteIdpErrorResponse'*

#### ID_TOKEN_HTTP_NOT_FOUND *= 'IdTokenHttpNotFound'*

#### ID_TOKEN_IDP_ERROR_RESPONSE *= 'IdTokenIdpErrorResponse'*

#### ID_TOKEN_INVALID_CONTENT_TYPE *= 'IdTokenInvalidContentType'*

#### ID_TOKEN_INVALID_REQUEST *= 'IdTokenInvalidRequest'*

#### ID_TOKEN_INVALID_RESPONSE *= 'IdTokenInvalidResponse'*

#### ID_TOKEN_NO_RESPONSE *= 'IdTokenNoResponse'*

#### INVALID_SIGNIN_RESPONSE *= 'InvalidSigninResponse'*

#### NOT_SIGNED_IN_WITH_IDP *= 'NotSignedInWithIdp'*

#### RP_PAGE_NOT_VISIBLE *= 'RpPageNotVisible'*

#### SHOULD_EMBARGO *= 'ShouldEmbargo'*

#### SILENT_MEDIATION_FAILURE *= 'SilentMediationFailure'*

#### THIRD_PARTY_COOKIES_BLOCKED *= 'ThirdPartyCookiesBlocked'*

#### TOO_MANY_REQUESTS *= 'TooManyRequests'*

#### WELL_KNOWN_HTTP_NOT_FOUND *= 'WellKnownHttpNotFound'*

#### WELL_KNOWN_INVALID_CONTENT_TYPE *= 'WellKnownInvalidContentType'*

#### WELL_KNOWN_INVALID_RESPONSE *= 'WellKnownInvalidResponse'*

#### WELL_KNOWN_LIST_EMPTY *= 'WellKnownListEmpty'*

#### WELL_KNOWN_NO_RESPONSE *= 'WellKnownNoResponse'*

#### WELL_KNOWN_TOO_BIG *= 'WellKnownTooBig'*

### *class* FederatedAuthUserInfoRequestIssueDetails(federated_auth_user_info_request_issue_reason)

* **Parameters:**
  **federated_auth_user_info_request_issue_reason** ([*FederatedAuthUserInfoRequestIssueReason*](#nodriver.cdp.audits.FederatedAuthUserInfoRequestIssueReason)) – 

#### federated_auth_user_info_request_issue_reason*: [`FederatedAuthUserInfoRequestIssueReason`](#nodriver.cdp.audits.FederatedAuthUserInfoRequestIssueReason)*

### *class* FederatedAuthUserInfoRequestIssueReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Represents the failure reason when a getUserInfo() call fails.
Should be updated alongside FederatedAuthUserInfoRequestResult in
third_party/blink/public/mojom/devtools/inspector_issue.mojom.

#### INVALID_ACCOUNTS_RESPONSE *= 'InvalidAccountsResponse'*

#### INVALID_CONFIG_OR_WELL_KNOWN *= 'InvalidConfigOrWellKnown'*

#### NOT_IFRAME *= 'NotIframe'*

#### NOT_POTENTIALLY_TRUSTWORTHY *= 'NotPotentiallyTrustworthy'*

#### NOT_SAME_ORIGIN *= 'NotSameOrigin'*

#### NOT_SIGNED_IN_WITH_IDP *= 'NotSignedInWithIdp'*

#### NO_ACCOUNT_SHARING_PERMISSION *= 'NoAccountSharingPermission'*

#### NO_API_PERMISSION *= 'NoApiPermission'*

#### NO_RETURNING_USER_FROM_FETCHED_ACCOUNTS *= 'NoReturningUserFromFetchedAccounts'*

### *class* ClientHintIssueDetails(source_code_location, client_hint_issue_reason)

This issue tracks client hints related issues. It’s used to deprecate old
features, encourage the use of new ones, and provide general guidance.

* **Parameters:**
  * **source_code_location** ([*SourceCodeLocation*](#nodriver.cdp.audits.SourceCodeLocation)) – 
  * **client_hint_issue_reason** ([*ClientHintIssueReason*](#nodriver.cdp.audits.ClientHintIssueReason)) – 

#### client_hint_issue_reason*: [`ClientHintIssueReason`](#nodriver.cdp.audits.ClientHintIssueReason)*

#### source_code_location*: [`SourceCodeLocation`](#nodriver.cdp.audits.SourceCodeLocation)*

### *class* FailedRequestInfo(url, failure_message, request_id=None)

* **Parameters:**
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **failure_message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **request_id** ([*RequestId*](network.md#nodriver.cdp.network.RequestId) *|* *None*) – 

#### failure_message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The failure message for the failed request.

#### request_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestId`](network.md#nodriver.cdp.network.RequestId)]* *= None*

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The URL that failed to load.

### *class* StyleSheetLoadingIssueReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### LATE_IMPORT_RULE *= 'LateImportRule'*

#### REQUEST_FAILED *= 'RequestFailed'*

### *class* StylesheetLoadingIssueDetails(source_code_location, style_sheet_loading_issue_reason, failed_request_info=None)

This issue warns when a referenced stylesheet couldn’t be loaded.

* **Parameters:**
  * **source_code_location** ([*SourceCodeLocation*](#nodriver.cdp.audits.SourceCodeLocation)) – 
  * **style_sheet_loading_issue_reason** ([*StyleSheetLoadingIssueReason*](#nodriver.cdp.audits.StyleSheetLoadingIssueReason)) – 
  * **failed_request_info** ([*FailedRequestInfo*](#nodriver.cdp.audits.FailedRequestInfo) *|* *None*) – 

#### failed_request_info*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FailedRequestInfo`](#nodriver.cdp.audits.FailedRequestInfo)]* *= None*

Contains additional info when the failure was due to a request.

#### source_code_location*: [`SourceCodeLocation`](#nodriver.cdp.audits.SourceCodeLocation)*

Source code position that referenced the failing stylesheet.

#### style_sheet_loading_issue_reason*: [`StyleSheetLoadingIssueReason`](#nodriver.cdp.audits.StyleSheetLoadingIssueReason)*

Reason why the stylesheet couldn’t be loaded.

### *class* PropertyRuleIssueReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### INVALID_INHERITS *= 'InvalidInherits'*

#### INVALID_INITIAL_VALUE *= 'InvalidInitialValue'*

#### INVALID_NAME *= 'InvalidName'*

#### INVALID_SYNTAX *= 'InvalidSyntax'*

### *class* PropertyRuleIssueDetails(source_code_location, property_rule_issue_reason, property_value=None)

This issue warns about errors in property rules that lead to property
registrations being ignored.

* **Parameters:**
  * **source_code_location** ([*SourceCodeLocation*](#nodriver.cdp.audits.SourceCodeLocation)) – 
  * **property_rule_issue_reason** ([*PropertyRuleIssueReason*](#nodriver.cdp.audits.PropertyRuleIssueReason)) – 
  * **property_value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### property_rule_issue_reason*: [`PropertyRuleIssueReason`](#nodriver.cdp.audits.PropertyRuleIssueReason)*

Reason why the property rule was discarded.

#### property_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The value of the property rule property that failed to parse

#### source_code_location*: [`SourceCodeLocation`](#nodriver.cdp.audits.SourceCodeLocation)*

Source code position of the property rule.

### *class* InspectorIssueCode(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

A unique identifier for the type of issue. Each type may use one of the
optional fields in InspectorIssueDetails to convey more specific
information about the kind of issue.

#### ATTRIBUTION_REPORTING_ISSUE *= 'AttributionReportingIssue'*

#### BLOCKED_BY_RESPONSE_ISSUE *= 'BlockedByResponseIssue'*

#### BOUNCE_TRACKING_ISSUE *= 'BounceTrackingIssue'*

#### CLIENT_HINT_ISSUE *= 'ClientHintIssue'*

#### CONTENT_SECURITY_POLICY_ISSUE *= 'ContentSecurityPolicyIssue'*

#### COOKIE_DEPRECATION_METADATA_ISSUE *= 'CookieDeprecationMetadataIssue'*

#### COOKIE_ISSUE *= 'CookieIssue'*

#### CORS_ISSUE *= 'CorsIssue'*

#### DEPRECATION_ISSUE *= 'DeprecationIssue'*

#### FEDERATED_AUTH_REQUEST_ISSUE *= 'FederatedAuthRequestIssue'*

#### FEDERATED_AUTH_USER_INFO_REQUEST_ISSUE *= 'FederatedAuthUserInfoRequestIssue'*

#### GENERIC_ISSUE *= 'GenericIssue'*

#### HEAVY_AD_ISSUE *= 'HeavyAdIssue'*

#### LOW_TEXT_CONTRAST_ISSUE *= 'LowTextContrastIssue'*

#### MIXED_CONTENT_ISSUE *= 'MixedContentIssue'*

#### NAVIGATOR_USER_AGENT_ISSUE *= 'NavigatorUserAgentIssue'*

#### PROPERTY_RULE_ISSUE *= 'PropertyRuleIssue'*

#### QUIRKS_MODE_ISSUE *= 'QuirksModeIssue'*

#### SHARED_ARRAY_BUFFER_ISSUE *= 'SharedArrayBufferIssue'*

#### STYLESHEET_LOADING_ISSUE *= 'StylesheetLoadingIssue'*

### *class* InspectorIssueDetails(cookie_issue_details=None, mixed_content_issue_details=None, blocked_by_response_issue_details=None, heavy_ad_issue_details=None, content_security_policy_issue_details=None, shared_array_buffer_issue_details=None, low_text_contrast_issue_details=None, cors_issue_details=None, attribution_reporting_issue_details=None, quirks_mode_issue_details=None, navigator_user_agent_issue_details=None, generic_issue_details=None, deprecation_issue_details=None, client_hint_issue_details=None, federated_auth_request_issue_details=None, bounce_tracking_issue_details=None, cookie_deprecation_metadata_issue_details=None, stylesheet_loading_issue_details=None, property_rule_issue_details=None, federated_auth_user_info_request_issue_details=None)

This struct holds a list of optional fields with additional information
specific to the kind of issue. When adding a new issue code, please also
add a new optional field to this type.

* **Parameters:**
  * **cookie_issue_details** ([*CookieIssueDetails*](#nodriver.cdp.audits.CookieIssueDetails) *|* *None*) – 
  * **mixed_content_issue_details** ([*MixedContentIssueDetails*](#nodriver.cdp.audits.MixedContentIssueDetails) *|* *None*) – 
  * **blocked_by_response_issue_details** ([*BlockedByResponseIssueDetails*](#nodriver.cdp.audits.BlockedByResponseIssueDetails) *|* *None*) – 
  * **heavy_ad_issue_details** ([*HeavyAdIssueDetails*](#nodriver.cdp.audits.HeavyAdIssueDetails) *|* *None*) – 
  * **content_security_policy_issue_details** ([*ContentSecurityPolicyIssueDetails*](#nodriver.cdp.audits.ContentSecurityPolicyIssueDetails) *|* *None*) – 
  * **shared_array_buffer_issue_details** ([*SharedArrayBufferIssueDetails*](#nodriver.cdp.audits.SharedArrayBufferIssueDetails) *|* *None*) – 
  * **low_text_contrast_issue_details** ([*LowTextContrastIssueDetails*](#nodriver.cdp.audits.LowTextContrastIssueDetails) *|* *None*) – 
  * **cors_issue_details** ([*CorsIssueDetails*](#nodriver.cdp.audits.CorsIssueDetails) *|* *None*) – 
  * **attribution_reporting_issue_details** ([*AttributionReportingIssueDetails*](#nodriver.cdp.audits.AttributionReportingIssueDetails) *|* *None*) – 
  * **quirks_mode_issue_details** ([*QuirksModeIssueDetails*](#nodriver.cdp.audits.QuirksModeIssueDetails) *|* *None*) – 
  * **navigator_user_agent_issue_details** ([*NavigatorUserAgentIssueDetails*](#nodriver.cdp.audits.NavigatorUserAgentIssueDetails) *|* *None*) – 
  * **generic_issue_details** ([*GenericIssueDetails*](#nodriver.cdp.audits.GenericIssueDetails) *|* *None*) – 
  * **deprecation_issue_details** ([*DeprecationIssueDetails*](#nodriver.cdp.audits.DeprecationIssueDetails) *|* *None*) – 
  * **client_hint_issue_details** ([*ClientHintIssueDetails*](#nodriver.cdp.audits.ClientHintIssueDetails) *|* *None*) – 
  * **federated_auth_request_issue_details** ([*FederatedAuthRequestIssueDetails*](#nodriver.cdp.audits.FederatedAuthRequestIssueDetails) *|* *None*) – 
  * **bounce_tracking_issue_details** ([*BounceTrackingIssueDetails*](#nodriver.cdp.audits.BounceTrackingIssueDetails) *|* *None*) – 
  * **cookie_deprecation_metadata_issue_details** ([*CookieDeprecationMetadataIssueDetails*](#nodriver.cdp.audits.CookieDeprecationMetadataIssueDetails) *|* *None*) – 
  * **stylesheet_loading_issue_details** ([*StylesheetLoadingIssueDetails*](#nodriver.cdp.audits.StylesheetLoadingIssueDetails) *|* *None*) – 
  * **property_rule_issue_details** ([*PropertyRuleIssueDetails*](#nodriver.cdp.audits.PropertyRuleIssueDetails) *|* *None*) – 
  * **federated_auth_user_info_request_issue_details** ([*FederatedAuthUserInfoRequestIssueDetails*](#nodriver.cdp.audits.FederatedAuthUserInfoRequestIssueDetails) *|* *None*) – 

#### attribution_reporting_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AttributionReportingIssueDetails`](#nodriver.cdp.audits.AttributionReportingIssueDetails)]* *= None*

#### blocked_by_response_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BlockedByResponseIssueDetails`](#nodriver.cdp.audits.BlockedByResponseIssueDetails)]* *= None*

#### bounce_tracking_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BounceTrackingIssueDetails`](#nodriver.cdp.audits.BounceTrackingIssueDetails)]* *= None*

#### client_hint_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ClientHintIssueDetails`](#nodriver.cdp.audits.ClientHintIssueDetails)]* *= None*

#### content_security_policy_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ContentSecurityPolicyIssueDetails`](#nodriver.cdp.audits.ContentSecurityPolicyIssueDetails)]* *= None*

#### cookie_deprecation_metadata_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookieDeprecationMetadataIssueDetails`](#nodriver.cdp.audits.CookieDeprecationMetadataIssueDetails)]* *= None*

#### cookie_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookieIssueDetails`](#nodriver.cdp.audits.CookieIssueDetails)]* *= None*

#### cors_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CorsIssueDetails`](#nodriver.cdp.audits.CorsIssueDetails)]* *= None*

#### deprecation_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`DeprecationIssueDetails`](#nodriver.cdp.audits.DeprecationIssueDetails)]* *= None*

#### federated_auth_request_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FederatedAuthRequestIssueDetails`](#nodriver.cdp.audits.FederatedAuthRequestIssueDetails)]* *= None*

#### federated_auth_user_info_request_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FederatedAuthUserInfoRequestIssueDetails`](#nodriver.cdp.audits.FederatedAuthUserInfoRequestIssueDetails)]* *= None*

#### generic_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`GenericIssueDetails`](#nodriver.cdp.audits.GenericIssueDetails)]* *= None*

#### heavy_ad_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`HeavyAdIssueDetails`](#nodriver.cdp.audits.HeavyAdIssueDetails)]* *= None*

#### low_text_contrast_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LowTextContrastIssueDetails`](#nodriver.cdp.audits.LowTextContrastIssueDetails)]* *= None*

#### mixed_content_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`MixedContentIssueDetails`](#nodriver.cdp.audits.MixedContentIssueDetails)]* *= None*

#### navigator_user_agent_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NavigatorUserAgentIssueDetails`](#nodriver.cdp.audits.NavigatorUserAgentIssueDetails)]* *= None*

#### property_rule_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`PropertyRuleIssueDetails`](#nodriver.cdp.audits.PropertyRuleIssueDetails)]* *= None*

#### quirks_mode_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`QuirksModeIssueDetails`](#nodriver.cdp.audits.QuirksModeIssueDetails)]* *= None*

#### shared_array_buffer_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SharedArrayBufferIssueDetails`](#nodriver.cdp.audits.SharedArrayBufferIssueDetails)]* *= None*

#### stylesheet_loading_issue_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StylesheetLoadingIssueDetails`](#nodriver.cdp.audits.StylesheetLoadingIssueDetails)]* *= None*

### *class* IssueId

A unique id for a DevTools inspector issue. Allows other entities (e.g.
exceptions, CDP message, console messages, etc.) to reference an issue.

### *class* InspectorIssue(code, details, issue_id=None)

An inspector issue reported from the back-end.

* **Parameters:**
  * **code** ([*InspectorIssueCode*](#nodriver.cdp.audits.InspectorIssueCode)) – 
  * **details** ([*InspectorIssueDetails*](#nodriver.cdp.audits.InspectorIssueDetails)) – 
  * **issue_id** ([*IssueId*](#nodriver.cdp.audits.IssueId) *|* *None*) – 

#### code*: [`InspectorIssueCode`](#nodriver.cdp.audits.InspectorIssueCode)*

#### details*: [`InspectorIssueDetails`](#nodriver.cdp.audits.InspectorIssueDetails)*

#### issue_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`IssueId`](#nodriver.cdp.audits.IssueId)]* *= None*

A unique id for this issue. May be omitted if no other entity (e.g.
exception, CDP message, etc.) is referencing this issue.

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../quickstart.md#getting-started-commands).

### check_contrast(report_aaa=None)

Runs the contrast check for the target page. Found issues are reported
using Audits.issueAdded event.

* **Parameters:**
  **report_aaa** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to report WCAG AAA level issues. Default is false.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### check_forms_issues()

Runs the form issues check for the target page. Found issues are reported
using Audits.issueAdded event.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`GenericIssueDetails`](#nodriver.cdp.audits.GenericIssueDetails)]]
* **Returns:**

### disable()

Disables issues domain, prevents further issues from being reported to the client.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables issues domain, sends the issues collected so far to the client by means of the
`issueAdded` event.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_encoded_response(request_id, encoding, quality=None, size_only=None)

Returns the response body and size if it were re-encoded with the specified settings. Only
applies to images.

* **Parameters:**
  * **request_id** ([`RequestId`](network.md#nodriver.cdp.network.RequestId)) – Identifier of the network request to get content for.
  * **encoding** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – The encoding to use.
  * **quality** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – *(Optional)* The quality of the encoding (0-1). (defaults to 1)
  * **size_only** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to only return the size information (defaults to false).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)], [`int`](https://docs.python.org/3/library/functions.html#int), [`int`](https://docs.python.org/3/library/functions.html#int)]]
* **Returns:**
  A tuple with the following items:
  1. **body** - *(Optional)* The encoded body as a base64 string. Omitted if sizeOnly is true. (Encoded as a base64 string when passed over JSON)
  2. **originalSize** - Size before re-encoding.
  3. **encodedSize** - Size after re-encoding.

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* IssueAdded(issue)

* **Parameters:**
  **issue** ([*InspectorIssue*](#nodriver.cdp.audits.InspectorIssue)) – 

#### issue*: [`InspectorIssue`](#nodriver.cdp.audits.InspectorIssue)*
