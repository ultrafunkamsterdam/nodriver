# Preload

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.preload"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* RuleSetId

Unique id

### *class* RuleSet(id_, loader_id, source_text, backend_node_id=None, url=None, request_id=None, error_type=None, error_message=None)

Corresponds to SpeculationRuleSet

#### id_*: [`RuleSetId`](#nodriver.cdp.preload.RuleSetId)*

#### loader_id*: [`LoaderId`](network.md#nodriver.cdp.network.LoaderId)*

Identifies a document which the rule set is associated with.

#### source_text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Source text of JSON representing the rule set. If it comes from
`<script>` tag, it is the textContent of the node. Note that it is
a JSON for valid case.

See also:
- [https://wicg.github.io/nav-speculation/speculation-rules.html](https://wicg.github.io/nav-speculation/speculation-rules.html)
- [https://github.com/WICG/nav-speculation/blob/main/triggers.md](https://github.com/WICG/nav-speculation/blob/main/triggers.md)

#### backend_node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

A speculation rule set is either added through an inline
`<script>` tag or through an external resource via the
‘Speculation-Rules’ HTTP header. For the first case, we include
the BackendNodeId of the relevant `<script>` tag. For the second
case, we include the external URL where the rule set was loaded
from, and also RequestId if Network domain is enabled.

See also:
- [https://wicg.github.io/nav-speculation/speculation-rules.html#speculation-rules-script](https://wicg.github.io/nav-speculation/speculation-rules.html#speculation-rules-script)
- [https://wicg.github.io/nav-speculation/speculation-rules.html#speculation-rules-header](https://wicg.github.io/nav-speculation/speculation-rules.html#speculation-rules-header)

#### url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### request_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestId`](network.md#nodriver.cdp.network.RequestId)]* *= None*

#### error_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RuleSetErrorType`](#nodriver.cdp.preload.RuleSetErrorType)]* *= None*

Error information
`errorMessage` is null iff `errorType` is null.

#### error_message*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Replace this property with structured error.

* **Type:**
  TODO(https
* **Type:**
  //crbug.com/1425354)

### *class* RuleSetErrorType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### SOURCE_IS_NOT_JSON_OBJECT *= 'SourceIsNotJsonObject'*

#### INVALID_RULES_SKIPPED *= 'InvalidRulesSkipped'*

#### INVALID_RULESET_LEVEL_TAG *= 'InvalidRulesetLevelTag'*

### *class* SpeculationAction(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The type of preloading attempted. It corresponds to
mojom::SpeculationAction (although PrefetchWithSubresources is omitted as it
isn’t being used by clients).

#### PREFETCH *= 'Prefetch'*

#### PRERENDER *= 'Prerender'*

### *class* SpeculationTargetHint(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Corresponds to mojom::SpeculationTargetHint.
See https://github.com/WICG/nav-speculation/blob/main/triggers.md#window-name-targeting-hints

#### BLANK *= 'Blank'*

#### SELF *= 'Self'*

### *class* PreloadingAttemptKey(loader_id, action, url, target_hint=None)

A key that identifies a preloading attempt.

The url used is the url specified by the trigger (i.e. the initial URL), and
not the final url that is navigated to. For example, prerendering allows
same-origin main frame navigations during the attempt, but the attempt is
still keyed with the initial URL.

#### loader_id*: [`LoaderId`](network.md#nodriver.cdp.network.LoaderId)*

#### action*: [`SpeculationAction`](#nodriver.cdp.preload.SpeculationAction)*

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### target_hint*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SpeculationTargetHint`](#nodriver.cdp.preload.SpeculationTargetHint)]* *= None*

### *class* PreloadingAttemptSource(key, rule_set_ids, node_ids)

Lists sources for a preloading attempt, specifically the ids of rule sets
that had a speculation rule that triggered the attempt, and the
BackendNodeIds of <a href> or <area href> elements that triggered the
attempt (in the case of attempts triggered by a document rule). It is
possible for multiple rule sets and links to trigger a single attempt.

#### key*: [`PreloadingAttemptKey`](#nodriver.cdp.preload.PreloadingAttemptKey)*

#### rule_set_ids*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`RuleSetId`](#nodriver.cdp.preload.RuleSetId)]*

#### node_ids*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]*

### *class* PreloadPipelineId

Chrome manages different types of preloads together using a
concept of preloading pipeline. For example, if a site uses a
SpeculationRules for prerender, Chrome first starts a prefetch and
then upgrades it to prerender.

CDP events for them are emitted separately but they share
`PreloadPipelineId`.

### *class* PrerenderFinalStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

List of FinalStatus reasons for Prerender2.

#### ACTIVATED *= 'Activated'*

#### DESTROYED *= 'Destroyed'*

#### LOW_END_DEVICE *= 'LowEndDevice'*

#### INVALID_SCHEME_REDIRECT *= 'InvalidSchemeRedirect'*

#### INVALID_SCHEME_NAVIGATION *= 'InvalidSchemeNavigation'*

#### NAVIGATION_REQUEST_BLOCKED_BY_CSP *= 'NavigationRequestBlockedByCsp'*

#### MOJO_BINDER_POLICY *= 'MojoBinderPolicy'*

#### RENDERER_PROCESS_CRASHED *= 'RendererProcessCrashed'*

#### RENDERER_PROCESS_KILLED *= 'RendererProcessKilled'*

#### DOWNLOAD *= 'Download'*

#### TRIGGER_DESTROYED *= 'TriggerDestroyed'*

#### NAVIGATION_NOT_COMMITTED *= 'NavigationNotCommitted'*

#### NAVIGATION_BAD_HTTP_STATUS *= 'NavigationBadHttpStatus'*

#### CLIENT_CERT_REQUESTED *= 'ClientCertRequested'*

#### NAVIGATION_REQUEST_NETWORK_ERROR *= 'NavigationRequestNetworkError'*

#### CANCEL_ALL_HOSTS_FOR_TESTING *= 'CancelAllHostsForTesting'*

#### DID_FAIL_LOAD *= 'DidFailLoad'*

#### STOP *= 'Stop'*

#### SSL_CERTIFICATE_ERROR *= 'SslCertificateError'*

#### LOGIN_AUTH_REQUESTED *= 'LoginAuthRequested'*

#### UA_CHANGE_REQUIRES_RELOAD *= 'UaChangeRequiresReload'*

#### BLOCKED_BY_CLIENT *= 'BlockedByClient'*

#### AUDIO_OUTPUT_DEVICE_REQUESTED *= 'AudioOutputDeviceRequested'*

#### MIXED_CONTENT *= 'MixedContent'*

#### TRIGGER_BACKGROUNDED *= 'TriggerBackgrounded'*

#### MEMORY_LIMIT_EXCEEDED *= 'MemoryLimitExceeded'*

#### DATA_SAVER_ENABLED *= 'DataSaverEnabled'*

#### TRIGGER_URL_HAS_EFFECTIVE_URL *= 'TriggerUrlHasEffectiveUrl'*

#### ACTIVATED_BEFORE_STARTED *= 'ActivatedBeforeStarted'*

#### INACTIVE_PAGE_RESTRICTION *= 'InactivePageRestriction'*

#### START_FAILED *= 'StartFailed'*

#### TIMEOUT_BACKGROUNDED *= 'TimeoutBackgrounded'*

#### CROSS_SITE_REDIRECT_IN_INITIAL_NAVIGATION *= 'CrossSiteRedirectInInitialNavigation'*

#### CROSS_SITE_NAVIGATION_IN_INITIAL_NAVIGATION *= 'CrossSiteNavigationInInitialNavigation'*

#### SAME_SITE_CROSS_ORIGIN_REDIRECT_NOT_OPT_IN_IN_INITIAL_NAVIGATION *= 'SameSiteCrossOriginRedirectNotOptInInInitialNavigation'*

#### SAME_SITE_CROSS_ORIGIN_NAVIGATION_NOT_OPT_IN_IN_INITIAL_NAVIGATION *= 'SameSiteCrossOriginNavigationNotOptInInInitialNavigation'*

#### ACTIVATION_NAVIGATION_PARAMETER_MISMATCH *= 'ActivationNavigationParameterMismatch'*

#### ACTIVATED_IN_BACKGROUND *= 'ActivatedInBackground'*

#### EMBEDDER_HOST_DISALLOWED *= 'EmbedderHostDisallowed'*

#### ACTIVATION_NAVIGATION_DESTROYED_BEFORE_SUCCESS *= 'ActivationNavigationDestroyedBeforeSuccess'*

#### TAB_CLOSED_BY_USER_GESTURE *= 'TabClosedByUserGesture'*

#### TAB_CLOSED_WITHOUT_USER_GESTURE *= 'TabClosedWithoutUserGesture'*

#### PRIMARY_MAIN_FRAME_RENDERER_PROCESS_CRASHED *= 'PrimaryMainFrameRendererProcessCrashed'*

#### PRIMARY_MAIN_FRAME_RENDERER_PROCESS_KILLED *= 'PrimaryMainFrameRendererProcessKilled'*

#### ACTIVATION_FRAME_POLICY_NOT_COMPATIBLE *= 'ActivationFramePolicyNotCompatible'*

#### PRELOADING_DISABLED *= 'PreloadingDisabled'*

#### BATTERY_SAVER_ENABLED *= 'BatterySaverEnabled'*

#### ACTIVATED_DURING_MAIN_FRAME_NAVIGATION *= 'ActivatedDuringMainFrameNavigation'*

#### PRELOADING_UNSUPPORTED_BY_WEB_CONTENTS *= 'PreloadingUnsupportedByWebContents'*

#### CROSS_SITE_REDIRECT_IN_MAIN_FRAME_NAVIGATION *= 'CrossSiteRedirectInMainFrameNavigation'*

#### CROSS_SITE_NAVIGATION_IN_MAIN_FRAME_NAVIGATION *= 'CrossSiteNavigationInMainFrameNavigation'*

#### SAME_SITE_CROSS_ORIGIN_REDIRECT_NOT_OPT_IN_IN_MAIN_FRAME_NAVIGATION *= 'SameSiteCrossOriginRedirectNotOptInInMainFrameNavigation'*

#### SAME_SITE_CROSS_ORIGIN_NAVIGATION_NOT_OPT_IN_IN_MAIN_FRAME_NAVIGATION *= 'SameSiteCrossOriginNavigationNotOptInInMainFrameNavigation'*

#### MEMORY_PRESSURE_ON_TRIGGER *= 'MemoryPressureOnTrigger'*

#### MEMORY_PRESSURE_AFTER_TRIGGERED *= 'MemoryPressureAfterTriggered'*

#### PRERENDERING_DISABLED_BY_DEV_TOOLS *= 'PrerenderingDisabledByDevTools'*

#### SPECULATION_RULE_REMOVED *= 'SpeculationRuleRemoved'*

#### ACTIVATED_WITH_AUXILIARY_BROWSING_CONTEXTS *= 'ActivatedWithAuxiliaryBrowsingContexts'*

#### MAX_NUM_OF_RUNNING_EAGER_PRERENDERS_EXCEEDED *= 'MaxNumOfRunningEagerPrerendersExceeded'*

#### MAX_NUM_OF_RUNNING_NON_EAGER_PRERENDERS_EXCEEDED *= 'MaxNumOfRunningNonEagerPrerendersExceeded'*

#### MAX_NUM_OF_RUNNING_EMBEDDER_PRERENDERS_EXCEEDED *= 'MaxNumOfRunningEmbedderPrerendersExceeded'*

#### PRERENDERING_URL_HAS_EFFECTIVE_URL *= 'PrerenderingUrlHasEffectiveUrl'*

#### REDIRECTED_PRERENDERING_URL_HAS_EFFECTIVE_URL *= 'RedirectedPrerenderingUrlHasEffectiveUrl'*

#### ACTIVATION_URL_HAS_EFFECTIVE_URL *= 'ActivationUrlHasEffectiveUrl'*

#### JAVA_SCRIPT_INTERFACE_ADDED *= 'JavaScriptInterfaceAdded'*

#### JAVA_SCRIPT_INTERFACE_REMOVED *= 'JavaScriptInterfaceRemoved'*

#### ALL_PRERENDERING_CANCELED *= 'AllPrerenderingCanceled'*

#### WINDOW_CLOSED *= 'WindowClosed'*

#### SLOW_NETWORK *= 'SlowNetwork'*

#### OTHER_PRERENDERED_PAGE_ACTIVATED *= 'OtherPrerenderedPageActivated'*

#### V8_OPTIMIZER_DISABLED *= 'V8OptimizerDisabled'*

#### PRERENDER_FAILED_DURING_PREFETCH *= 'PrerenderFailedDuringPrefetch'*

#### BROWSING_DATA_REMOVED *= 'BrowsingDataRemoved'*

#### PRERENDER_HOST_REUSED *= 'PrerenderHostReused'*

### *class* PreloadingStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Preloading status values, see also PreloadingTriggeringOutcome. This
status is shared by prefetchStatusUpdated and prerenderStatusUpdated.

#### PENDING *= 'Pending'*

#### RUNNING *= 'Running'*

#### READY *= 'Ready'*

#### SUCCESS *= 'Success'*

#### FAILURE *= 'Failure'*

#### NOT_SUPPORTED *= 'NotSupported'*

### *class* PrefetchStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

TODO([https://crbug.com/1384419](https://crbug.com/1384419)): revisit the list of PrefetchStatus and
filter out the ones that aren’t necessary to the developers.

#### PREFETCH_ALLOWED *= 'PrefetchAllowed'*

#### PREFETCH_FAILED_INELIGIBLE_REDIRECT *= 'PrefetchFailedIneligibleRedirect'*

#### PREFETCH_FAILED_INVALID_REDIRECT *= 'PrefetchFailedInvalidRedirect'*

#### PREFETCH_FAILED_MIME_NOT_SUPPORTED *= 'PrefetchFailedMIMENotSupported'*

#### PREFETCH_FAILED_NET_ERROR *= 'PrefetchFailedNetError'*

#### PREFETCH_FAILED_NON2_XX *= 'PrefetchFailedNon2XX'*

#### PREFETCH_EVICTED_AFTER_BROWSING_DATA_REMOVED *= 'PrefetchEvictedAfterBrowsingDataRemoved'*

#### PREFETCH_EVICTED_AFTER_CANDIDATE_REMOVED *= 'PrefetchEvictedAfterCandidateRemoved'*

#### PREFETCH_EVICTED_FOR_NEWER_PREFETCH *= 'PrefetchEvictedForNewerPrefetch'*

#### PREFETCH_HELDBACK *= 'PrefetchHeldback'*

#### PREFETCH_INELIGIBLE_RETRY_AFTER *= 'PrefetchIneligibleRetryAfter'*

#### PREFETCH_IS_PRIVACY_DECOY *= 'PrefetchIsPrivacyDecoy'*

#### PREFETCH_IS_STALE *= 'PrefetchIsStale'*

#### PREFETCH_NOT_ELIGIBLE_BROWSER_CONTEXT_OFF_THE_RECORD *= 'PrefetchNotEligibleBrowserContextOffTheRecord'*

#### PREFETCH_NOT_ELIGIBLE_DATA_SAVER_ENABLED *= 'PrefetchNotEligibleDataSaverEnabled'*

#### PREFETCH_NOT_ELIGIBLE_EXISTING_PROXY *= 'PrefetchNotEligibleExistingProxy'*

#### PREFETCH_NOT_ELIGIBLE_HOST_IS_NON_UNIQUE *= 'PrefetchNotEligibleHostIsNonUnique'*

#### PREFETCH_NOT_ELIGIBLE_NON_DEFAULT_STORAGE_PARTITION *= 'PrefetchNotEligibleNonDefaultStoragePartition'*

#### PREFETCH_NOT_ELIGIBLE_SAME_SITE_CROSS_ORIGIN_PREFETCH_REQUIRED_PROXY *= 'PrefetchNotEligibleSameSiteCrossOriginPrefetchRequiredProxy'*

#### PREFETCH_NOT_ELIGIBLE_SCHEME_IS_NOT_HTTPS *= 'PrefetchNotEligibleSchemeIsNotHttps'*

#### PREFETCH_NOT_ELIGIBLE_USER_HAS_COOKIES *= 'PrefetchNotEligibleUserHasCookies'*

#### PREFETCH_NOT_ELIGIBLE_USER_HAS_SERVICE_WORKER *= 'PrefetchNotEligibleUserHasServiceWorker'*

#### PREFETCH_NOT_ELIGIBLE_USER_HAS_SERVICE_WORKER_NO_FETCH_HANDLER *= 'PrefetchNotEligibleUserHasServiceWorkerNoFetchHandler'*

#### PREFETCH_NOT_ELIGIBLE_REDIRECT_FROM_SERVICE_WORKER *= 'PrefetchNotEligibleRedirectFromServiceWorker'*

#### PREFETCH_NOT_ELIGIBLE_REDIRECT_TO_SERVICE_WORKER *= 'PrefetchNotEligibleRedirectToServiceWorker'*

#### PREFETCH_NOT_ELIGIBLE_BATTERY_SAVER_ENABLED *= 'PrefetchNotEligibleBatterySaverEnabled'*

#### PREFETCH_NOT_ELIGIBLE_PRELOADING_DISABLED *= 'PrefetchNotEligiblePreloadingDisabled'*

#### PREFETCH_NOT_FINISHED_IN_TIME *= 'PrefetchNotFinishedInTime'*

#### PREFETCH_NOT_STARTED *= 'PrefetchNotStarted'*

#### PREFETCH_NOT_USED_COOKIES_CHANGED *= 'PrefetchNotUsedCookiesChanged'*

#### PREFETCH_PROXY_NOT_AVAILABLE *= 'PrefetchProxyNotAvailable'*

#### PREFETCH_RESPONSE_USED *= 'PrefetchResponseUsed'*

#### PREFETCH_SUCCESSFUL_BUT_NOT_USED *= 'PrefetchSuccessfulButNotUsed'*

#### PREFETCH_NOT_USED_PROBE_FAILED *= 'PrefetchNotUsedProbeFailed'*

### *class* PrerenderMismatchedHeaders(header_name, initial_value=None, activation_value=None)

Information of headers to be displayed when the header mismatch occurred.

#### header_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### initial_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### activation_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### disable()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* RuleSetUpdated(rule_set)

Upsert. Currently, it is only emitted when a rule set added.

#### rule_set*: [`RuleSet`](#nodriver.cdp.preload.RuleSet)*

### *class* RuleSetRemoved(id_)

#### id_*: [`RuleSetId`](#nodriver.cdp.preload.RuleSetId)*

### *class* PreloadEnabledStateUpdated(disabled_by_preference, disabled_by_data_saver, disabled_by_battery_saver, disabled_by_holdback_prefetch_speculation_rules, disabled_by_holdback_prerender_speculation_rules)

Fired when a preload enabled state is updated.

#### disabled_by_preference*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### disabled_by_data_saver*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### disabled_by_battery_saver*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### disabled_by_holdback_prefetch_speculation_rules*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### disabled_by_holdback_prerender_speculation_rules*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

### *class* PrefetchStatusUpdated(key, pipeline_id, initiating_frame_id, prefetch_url, status, prefetch_status, request_id)

Fired when a prefetch attempt is updated.

#### key*: [`PreloadingAttemptKey`](#nodriver.cdp.preload.PreloadingAttemptKey)*

#### pipeline_id*: [`PreloadPipelineId`](#nodriver.cdp.preload.PreloadPipelineId)*

#### initiating_frame_id*: [`FrameId`](page.md#nodriver.cdp.page.FrameId)*

The frame id of the frame initiating prefetch.

#### prefetch_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### status*: [`PreloadingStatus`](#nodriver.cdp.preload.PreloadingStatus)*

#### prefetch_status*: [`PrefetchStatus`](#nodriver.cdp.preload.PrefetchStatus)*

#### request_id*: [`RequestId`](network.md#nodriver.cdp.network.RequestId)*

### *class* PrerenderStatusUpdated(key, pipeline_id, status, prerender_status, disallowed_mojo_interface, mismatched_headers)

Fired when a prerender attempt is updated.

#### key*: [`PreloadingAttemptKey`](#nodriver.cdp.preload.PreloadingAttemptKey)*

#### pipeline_id*: [`PreloadPipelineId`](#nodriver.cdp.preload.PreloadPipelineId)*

#### status*: [`PreloadingStatus`](#nodriver.cdp.preload.PreloadingStatus)*

#### prerender_status*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`PrerenderFinalStatus`](#nodriver.cdp.preload.PrerenderFinalStatus)]*

#### disallowed_mojo_interface*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

This is used to give users more information about the name of Mojo interface
that is incompatible with prerender and has caused the cancellation of the attempt.

#### mismatched_headers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PrerenderMismatchedHeaders`](#nodriver.cdp.preload.PrerenderMismatchedHeaders)]]*

### *class* PreloadingAttemptSourcesUpdated(loader_id, preloading_attempt_sources)

Send a list of sources for all preloading attempts in a document.

#### loader_id*: [`LoaderId`](network.md#nodriver.cdp.network.LoaderId)*

#### preloading_attempt_sources*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PreloadingAttemptSource`](#nodriver.cdp.preload.PreloadingAttemptSource)]*
