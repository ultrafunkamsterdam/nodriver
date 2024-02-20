# Storage

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.storage"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* SerializedStorageKey

### *class* StorageType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of possible storage types.

#### APPCACHE *= 'appcache'*

#### COOKIES *= 'cookies'*

#### FILE_SYSTEMS *= 'file_systems'*

#### INDEXEDDB *= 'indexeddb'*

#### LOCAL_STORAGE *= 'local_storage'*

#### SHADER_CACHE *= 'shader_cache'*

#### WEBSQL *= 'websql'*

#### SERVICE_WORKERS *= 'service_workers'*

#### CACHE_STORAGE *= 'cache_storage'*

#### INTEREST_GROUPS *= 'interest_groups'*

#### SHARED_STORAGE *= 'shared_storage'*

#### STORAGE_BUCKETS *= 'storage_buckets'*

#### ALL_ *= 'all'*

#### OTHER *= 'other'*

### *class* UsageForType(storage_type, usage)

Usage for a storage type.

#### storage_type *: [`StorageType`](#nodriver.cdp.storage.StorageType)*

Name of storage type.

#### usage *: [`float`](https://docs.python.org/3/library/functions.html#float)*

Storage usage (bytes).

### *class* TrustTokens(issuer_origin, count)

Pair of issuer origin and number of available (signed, but not used) Trust
Tokens from that issuer.

#### issuer_origin *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### count *: [`float`](https://docs.python.org/3/library/functions.html#float)*

### *class* InterestGroupAccessType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of interest group access types.

#### JOIN *= 'join'*

#### LEAVE *= 'leave'*

#### UPDATE *= 'update'*

#### LOADED *= 'loaded'*

#### BID *= 'bid'*

#### WIN *= 'win'*

#### ADDITIONAL_BID *= 'additionalBid'*

#### ADDITIONAL_BID_WIN *= 'additionalBidWin'*

#### CLEAR *= 'clear'*

### *class* InterestGroupAd(render_url, metadata=None)

Ad advertising element inside an interest group.

#### render_url *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### metadata *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* InterestGroupDetails(owner_origin, name, expiration_time, joining_origin, trusted_bidding_signals_keys, ads, ad_components, bidding_logic_url=None, bidding_wasm_helper_url=None, update_url=None, trusted_bidding_signals_url=None, user_bidding_signals=None)

The full details of an interest group.

#### owner_origin *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### name *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### expiration_time *: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

#### joining_origin *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### trusted_bidding_signals_keys *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### ads *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`InterestGroupAd`](#nodriver.cdp.storage.InterestGroupAd)]*

#### ad_components *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`InterestGroupAd`](#nodriver.cdp.storage.InterestGroupAd)]*

#### bidding_logic_url *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### bidding_wasm_helper_url *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### update_url *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### trusted_bidding_signals_url *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### user_bidding_signals *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* SharedStorageAccessType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of shared storage access types.

#### DOCUMENT_ADD_MODULE *= 'documentAddModule'*

#### DOCUMENT_SELECT_URL *= 'documentSelectURL'*

#### DOCUMENT_RUN *= 'documentRun'*

#### DOCUMENT_SET *= 'documentSet'*

#### DOCUMENT_APPEND *= 'documentAppend'*

#### DOCUMENT_DELETE *= 'documentDelete'*

#### DOCUMENT_CLEAR *= 'documentClear'*

#### WORKLET_SET *= 'workletSet'*

#### WORKLET_APPEND *= 'workletAppend'*

#### WORKLET_DELETE *= 'workletDelete'*

#### WORKLET_CLEAR *= 'workletClear'*

#### WORKLET_GET *= 'workletGet'*

#### WORKLET_KEYS *= 'workletKeys'*

#### WORKLET_ENTRIES *= 'workletEntries'*

#### WORKLET_LENGTH *= 'workletLength'*

#### WORKLET_REMAINING_BUDGET *= 'workletRemainingBudget'*

### *class* SharedStorageEntry(key, value)

Struct for a single key-value pair in an origin’s shared storage.

#### key *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### value *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* SharedStorageMetadata(creation_time, length, remaining_budget)

Details for an origin’s shared storage.

#### creation_time *: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

#### length *: [`int`](https://docs.python.org/3/library/functions.html#int)*

#### remaining_budget *: [`float`](https://docs.python.org/3/library/functions.html#float)*

### *class* SharedStorageReportingMetadata(event_type, reporting_url)

Pair of reporting metadata details for a candidate URL for `selectURL()`.

#### event_type *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### reporting_url *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* SharedStorageUrlWithMetadata(url, reporting_metadata)

Bundles a candidate URL with its reporting metadata.

#### url *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Spec of candidate URL.

#### reporting_metadata *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SharedStorageReportingMetadata`](#nodriver.cdp.storage.SharedStorageReportingMetadata)]*

Any associated reporting metadata.

### *class* SharedStorageAccessParams(script_source_url=None, operation_name=None, serialized_data=None, urls_with_metadata=None, key=None, value=None, ignore_if_present=None)

Bundles the parameters for shared storage access events whose
presence/absence can vary according to SharedStorageAccessType.

#### script_source_url *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Spec of the module script URL.
Present only for SharedStorageAccessType.documentAddModule.

#### operation_name *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Name of the registered operation to be run.
Present only for SharedStorageAccessType.documentRun and
SharedStorageAccessType.documentSelectURL.

#### serialized_data *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The operation’s serialized data in bytes (converted to a string).
Present only for SharedStorageAccessType.documentRun and
SharedStorageAccessType.documentSelectURL.

#### urls_with_metadata *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SharedStorageUrlWithMetadata`](#nodriver.cdp.storage.SharedStorageUrlWithMetadata)]]* *= None*

Array of candidate URLs’ specs, along with any associated metadata.
Present only for SharedStorageAccessType.documentSelectURL.

#### key *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Key for a specific entry in an origin’s shared storage.
Present only for SharedStorageAccessType.documentSet,
SharedStorageAccessType.documentAppend,
SharedStorageAccessType.documentDelete,
SharedStorageAccessType.workletSet,
SharedStorageAccessType.workletAppend,
SharedStorageAccessType.workletDelete, and
SharedStorageAccessType.workletGet.

#### value *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Value for a specific entry in an origin’s shared storage.
Present only for SharedStorageAccessType.documentSet,
SharedStorageAccessType.documentAppend,
SharedStorageAccessType.workletSet, and
SharedStorageAccessType.workletAppend.

#### ignore_if_present *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether or not to set an entry for a key if that key is already present.
Present only for SharedStorageAccessType.documentSet and
SharedStorageAccessType.workletSet.

### *class* StorageBucketsDurability(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### RELAXED *= 'relaxed'*

#### STRICT *= 'strict'*

### *class* StorageBucket(storage_key, name=None)

#### storage_key *: [`SerializedStorageKey`](#nodriver.cdp.storage.SerializedStorageKey)*

#### name *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

If not specified, it is the default bucket of the storageKey.

### *class* StorageBucketInfo(bucket, id_, expiration, quota, persistent, durability)

#### bucket *: [`StorageBucket`](#nodriver.cdp.storage.StorageBucket)*

#### id_ *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### expiration *: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

#### quota *: [`float`](https://docs.python.org/3/library/functions.html#float)*

Storage quota (bytes).

#### persistent *: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### durability *: [`StorageBucketsDurability`](#nodriver.cdp.storage.StorageBucketsDurability)*

### *class* AttributionReportingSourceType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### NAVIGATION *= 'navigation'*

#### EVENT *= 'event'*

### *class* UnsignedInt64AsBase10

### *class* UnsignedInt128AsBase16

### *class* SignedInt64AsBase10

### *class* AttributionReportingFilterDataEntry(key, values)

#### key *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### values *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

### *class* AttributionReportingFilterConfig(filter_values, lookback_window=None)

#### filter_values *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AttributionReportingFilterDataEntry`](#nodriver.cdp.storage.AttributionReportingFilterDataEntry)]*

#### lookback_window *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

duration in seconds

### *class* AttributionReportingFilterPair(filters, not_filters)

#### filters *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AttributionReportingFilterConfig`](#nodriver.cdp.storage.AttributionReportingFilterConfig)]*

#### not_filters *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AttributionReportingFilterConfig`](#nodriver.cdp.storage.AttributionReportingFilterConfig)]*

### *class* AttributionReportingAggregationKeysEntry(key, value)

#### key *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### value *: [`UnsignedInt128AsBase16`](#nodriver.cdp.storage.UnsignedInt128AsBase16)*

### *class* AttributionReportingEventReportWindows(start, ends)

#### start *: [`int`](https://docs.python.org/3/library/functions.html#int)*

duration in seconds

#### ends *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

duration in seconds

### *class* AttributionReportingTriggerSpec(trigger_data, event_report_windows)

#### trigger_data *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`float`](https://docs.python.org/3/library/functions.html#float)]*

number instead of integer because not all uint32 can be represented by
int

#### event_report_windows *: [`AttributionReportingEventReportWindows`](#nodriver.cdp.storage.AttributionReportingEventReportWindows)*

### *class* AttributionReportingTriggerDataMatching(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### EXACT *= 'exact'*

#### MODULUS *= 'modulus'*

### *class* AttributionReportingSourceRegistration(time, expiry, trigger_specs, aggregatable_report_window, type_, source_origin, reporting_origin, destination_sites, event_id, priority, filter_data, aggregation_keys, trigger_data_matching, debug_key=None)

#### time *: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

#### expiry *: [`int`](https://docs.python.org/3/library/functions.html#int)*

duration in seconds

#### trigger_specs *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AttributionReportingTriggerSpec`](#nodriver.cdp.storage.AttributionReportingTriggerSpec)]*

#### aggregatable_report_window *: [`int`](https://docs.python.org/3/library/functions.html#int)*

duration in seconds

#### type_ *: [`AttributionReportingSourceType`](#nodriver.cdp.storage.AttributionReportingSourceType)*

#### source_origin *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### reporting_origin *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### destination_sites *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### event_id *: [`UnsignedInt64AsBase10`](#nodriver.cdp.storage.UnsignedInt64AsBase10)*

#### priority *: [`SignedInt64AsBase10`](#nodriver.cdp.storage.SignedInt64AsBase10)*

#### filter_data *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AttributionReportingFilterDataEntry`](#nodriver.cdp.storage.AttributionReportingFilterDataEntry)]*

#### aggregation_keys *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AttributionReportingAggregationKeysEntry`](#nodriver.cdp.storage.AttributionReportingAggregationKeysEntry)]*

#### trigger_data_matching *: [`AttributionReportingTriggerDataMatching`](#nodriver.cdp.storage.AttributionReportingTriggerDataMatching)*

#### debug_key *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`UnsignedInt64AsBase10`](#nodriver.cdp.storage.UnsignedInt64AsBase10)]* *= None*

### *class* AttributionReportingSourceRegistrationResult(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### SUCCESS *= 'success'*

#### INTERNAL_ERROR *= 'internalError'*

#### INSUFFICIENT_SOURCE_CAPACITY *= 'insufficientSourceCapacity'*

#### INSUFFICIENT_UNIQUE_DESTINATION_CAPACITY *= 'insufficientUniqueDestinationCapacity'*

#### EXCESSIVE_REPORTING_ORIGINS *= 'excessiveReportingOrigins'*

#### PROHIBITED_BY_BROWSER_POLICY *= 'prohibitedByBrowserPolicy'*

#### SUCCESS_NOISED *= 'successNoised'*

#### DESTINATION_REPORTING_LIMIT_REACHED *= 'destinationReportingLimitReached'*

#### DESTINATION_GLOBAL_LIMIT_REACHED *= 'destinationGlobalLimitReached'*

#### DESTINATION_BOTH_LIMITS_REACHED *= 'destinationBothLimitsReached'*

#### REPORTING_ORIGINS_PER_SITE_LIMIT_REACHED *= 'reportingOriginsPerSiteLimitReached'*

#### EXCEEDS_MAX_CHANNEL_CAPACITY *= 'exceedsMaxChannelCapacity'*

### *class* AttributionReportingSourceRegistrationTimeConfig(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### INCLUDE *= 'include'*

#### EXCLUDE *= 'exclude'*

### *class* AttributionReportingAggregatableValueEntry(key, value)

#### key *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### value *: [`float`](https://docs.python.org/3/library/functions.html#float)*

number instead of integer because not all uint32 can be represented by
int

### *class* AttributionReportingEventTriggerData(data, priority, filters, dedup_key=None)

#### data *: [`UnsignedInt64AsBase10`](#nodriver.cdp.storage.UnsignedInt64AsBase10)*

#### priority *: [`SignedInt64AsBase10`](#nodriver.cdp.storage.SignedInt64AsBase10)*

#### filters *: [`AttributionReportingFilterPair`](#nodriver.cdp.storage.AttributionReportingFilterPair)*

#### dedup_key *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`UnsignedInt64AsBase10`](#nodriver.cdp.storage.UnsignedInt64AsBase10)]* *= None*

### *class* AttributionReportingAggregatableTriggerData(key_piece, source_keys, filters)

#### key_piece *: [`UnsignedInt128AsBase16`](#nodriver.cdp.storage.UnsignedInt128AsBase16)*

#### source_keys *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### filters *: [`AttributionReportingFilterPair`](#nodriver.cdp.storage.AttributionReportingFilterPair)*

### *class* AttributionReportingAggregatableDedupKey(filters, dedup_key=None)

#### filters *: [`AttributionReportingFilterPair`](#nodriver.cdp.storage.AttributionReportingFilterPair)*

#### dedup_key *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`UnsignedInt64AsBase10`](#nodriver.cdp.storage.UnsignedInt64AsBase10)]* *= None*

### *class* AttributionReportingTriggerRegistration(filters, aggregatable_dedup_keys, event_trigger_data, aggregatable_trigger_data, aggregatable_values, debug_reporting, source_registration_time_config, debug_key=None, aggregation_coordinator_origin=None, trigger_context_id=None)

#### filters *: [`AttributionReportingFilterPair`](#nodriver.cdp.storage.AttributionReportingFilterPair)*

#### aggregatable_dedup_keys *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AttributionReportingAggregatableDedupKey`](#nodriver.cdp.storage.AttributionReportingAggregatableDedupKey)]*

#### event_trigger_data *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AttributionReportingEventTriggerData`](#nodriver.cdp.storage.AttributionReportingEventTriggerData)]*

#### aggregatable_trigger_data *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AttributionReportingAggregatableTriggerData`](#nodriver.cdp.storage.AttributionReportingAggregatableTriggerData)]*

#### aggregatable_values *: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AttributionReportingAggregatableValueEntry`](#nodriver.cdp.storage.AttributionReportingAggregatableValueEntry)]*

#### debug_reporting *: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### source_registration_time_config *: [`AttributionReportingSourceRegistrationTimeConfig`](#nodriver.cdp.storage.AttributionReportingSourceRegistrationTimeConfig)*

#### debug_key *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`UnsignedInt64AsBase10`](#nodriver.cdp.storage.UnsignedInt64AsBase10)]* *= None*

#### aggregation_coordinator_origin *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### trigger_context_id *: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* AttributionReportingEventLevelResult(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### SUCCESS *= 'success'*

#### SUCCESS_DROPPED_LOWER_PRIORITY *= 'successDroppedLowerPriority'*

#### INTERNAL_ERROR *= 'internalError'*

#### NO_CAPACITY_FOR_ATTRIBUTION_DESTINATION *= 'noCapacityForAttributionDestination'*

#### NO_MATCHING_SOURCES *= 'noMatchingSources'*

#### DEDUPLICATED *= 'deduplicated'*

#### EXCESSIVE_ATTRIBUTIONS *= 'excessiveAttributions'*

#### PRIORITY_TOO_LOW *= 'priorityTooLow'*

#### NEVER_ATTRIBUTED_SOURCE *= 'neverAttributedSource'*

#### EXCESSIVE_REPORTING_ORIGINS *= 'excessiveReportingOrigins'*

#### NO_MATCHING_SOURCE_FILTER_DATA *= 'noMatchingSourceFilterData'*

#### PROHIBITED_BY_BROWSER_POLICY *= 'prohibitedByBrowserPolicy'*

#### NO_MATCHING_CONFIGURATIONS *= 'noMatchingConfigurations'*

#### EXCESSIVE_REPORTS *= 'excessiveReports'*

#### FALSELY_ATTRIBUTED_SOURCE *= 'falselyAttributedSource'*

#### REPORT_WINDOW_PASSED *= 'reportWindowPassed'*

#### NOT_REGISTERED *= 'notRegistered'*

#### REPORT_WINDOW_NOT_STARTED *= 'reportWindowNotStarted'*

#### NO_MATCHING_TRIGGER_DATA *= 'noMatchingTriggerData'*

### *class* AttributionReportingAggregatableResult(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### SUCCESS *= 'success'*

#### INTERNAL_ERROR *= 'internalError'*

#### NO_CAPACITY_FOR_ATTRIBUTION_DESTINATION *= 'noCapacityForAttributionDestination'*

#### NO_MATCHING_SOURCES *= 'noMatchingSources'*

#### EXCESSIVE_ATTRIBUTIONS *= 'excessiveAttributions'*

#### EXCESSIVE_REPORTING_ORIGINS *= 'excessiveReportingOrigins'*

#### NO_HISTOGRAMS *= 'noHistograms'*

#### INSUFFICIENT_BUDGET *= 'insufficientBudget'*

#### NO_MATCHING_SOURCE_FILTER_DATA *= 'noMatchingSourceFilterData'*

#### NOT_REGISTERED *= 'notRegistered'*

#### PROHIBITED_BY_BROWSER_POLICY *= 'prohibitedByBrowserPolicy'*

#### DEDUPLICATED *= 'deduplicated'*

#### REPORT_WINDOW_PASSED *= 'reportWindowPassed'*

#### EXCESSIVE_REPORTS *= 'excessiveReports'*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../quickstart.md#getting-started-commands).

### clear_cookies(browser_context_id=None)

Clears cookies.

* **Parameters:**
  **browser_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BrowserContextID`](browser.md#nodriver.cdp.browser.BrowserContextID)]) –  *(Optional)* Browser context to use when called on the browser endpoint.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### clear_data_for_origin(origin, storage_types)

Clears storage for origin.

* **Parameters:**
  * **origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Security origin.
  * **storage_types** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Comma separated list of StorageType to clear.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### clear_data_for_storage_key(storage_key, storage_types)

Clears storage for storage key.

* **Parameters:**
  * **storage_key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Storage key.
  * **storage_types** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Comma separated list of StorageType to clear.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### clear_shared_storage_entries(owner_origin)

Clears all entries for a given origin’s shared storage.

**EXPERIMENTAL**

* **Parameters:**
  **owner_origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### clear_trust_tokens(issuer_origin)

Removes all Trust Tokens issued by the provided issuerOrigin.
Leaves other stored data, including the issuer’s Redemption Records, intact.

**EXPERIMENTAL**

* **Parameters:**
  **issuer_origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`bool`](https://docs.python.org/3/library/functions.html#bool)]
* **Returns:**
  True if any tokens were deleted, false otherwise.

### delete_shared_storage_entry(owner_origin, key)

Deletes entry for `key` (if it exists) for a given origin’s shared storage.

**EXPERIMENTAL**

* **Parameters:**
  * **owner_origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### delete_storage_bucket(bucket)

Deletes the Storage Bucket with the given storage key and bucket name.

**EXPERIMENTAL**

* **Parameters:**
  **bucket** ([`StorageBucket`](#nodriver.cdp.storage.StorageBucket)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_cookies(browser_context_id=None)

Returns all browser cookies.

* **Parameters:**
  **browser_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BrowserContextID`](browser.md#nodriver.cdp.browser.BrowserContextID)]) –  *(Optional)* Browser context to use when called on the browser endpoint.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Cookie`](network.md#nodriver.cdp.network.Cookie)]]
* **Returns:**
  Array of cookie objects.

### get_interest_group_details(owner_origin, name)

Gets details for a named interest group.

**EXPERIMENTAL**

* **Parameters:**
  * **owner_origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`InterestGroupDetails`](#nodriver.cdp.storage.InterestGroupDetails)]
* **Returns:**

### get_shared_storage_entries(owner_origin)

Gets the entries in an given origin’s shared storage.

**EXPERIMENTAL**

* **Parameters:**
  **owner_origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SharedStorageEntry`](#nodriver.cdp.storage.SharedStorageEntry)]]
* **Returns:**

### get_shared_storage_metadata(owner_origin)

Gets metadata for an origin’s shared storage.

**EXPERIMENTAL**

* **Parameters:**
  **owner_origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SharedStorageMetadata`](#nodriver.cdp.storage.SharedStorageMetadata)]
* **Returns:**

### get_storage_key_for_frame(frame_id)

Returns a storage key given a frame id.

* **Parameters:**
  **frame_id** ([`FrameId`](page.md#nodriver.cdp.page.FrameId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SerializedStorageKey`](#nodriver.cdp.storage.SerializedStorageKey)]
* **Returns:**

### get_trust_tokens()

Returns the number of stored Trust Tokens per issuer for the
current browsing context.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`TrustTokens`](#nodriver.cdp.storage.TrustTokens)]]
* **Returns:**

### get_usage_and_quota(origin)

Returns usage and quota in bytes.

* **Parameters:**
  **origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Security origin.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`float`](https://docs.python.org/3/library/functions.html#float), [`float`](https://docs.python.org/3/library/functions.html#float), [`bool`](https://docs.python.org/3/library/functions.html#bool), [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`UsageForType`](#nodriver.cdp.storage.UsageForType)]]]
* **Returns:**
  A tuple with the following items:
  1. **usage** - Storage usage (bytes).
  2. **quota** - Storage quota (bytes).
  3. **overrideActive** - Whether or not the origin has an active storage quota override
  4. **usageBreakdown** - Storage usage per type (bytes).

### override_quota_for_origin(origin, quota_size=None)

Override quota for the specified origin

**EXPERIMENTAL**

* **Parameters:**
  * **origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Security origin.
  * **quota_size** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) –  *(Optional)* The quota size (in bytes) to override the original quota with. If this is called multiple times, the overridden quota will be equal to the quotaSize provided in the final call. If this is called without specifying a quotaSize, the quota will be reset to the default value for the specified origin. If this is called multiple times with different origins, the override will be maintained for each origin until it is disabled (called without a quotaSize).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### reset_shared_storage_budget(owner_origin)

Resets the budget for `ownerOrigin` by clearing all budget withdrawals.

**EXPERIMENTAL**

* **Parameters:**
  **owner_origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### run_bounce_tracking_mitigations()

Deletes state for sites identified as potential bounce trackers, immediately.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**

### set_attribution_reporting_local_testing_mode(enabled)

[https://wicg.github.io/attribution-reporting-api/](https://wicg.github.io/attribution-reporting-api/)

**EXPERIMENTAL**

* **Parameters:**
  **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – If enabled, noise is suppressed and reports are sent immediately.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_attribution_reporting_tracking(enable)

Enables/disables issuing of Attribution Reporting events.

**EXPERIMENTAL**

* **Parameters:**
  **enable** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_cookies(cookies, browser_context_id=None)

Sets given cookies.

* **Parameters:**
  * **cookies** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CookieParam`](network.md#nodriver.cdp.network.CookieParam)]) – Cookies to be set.
  * **browser_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BrowserContextID`](browser.md#nodriver.cdp.browser.BrowserContextID)]) –  *(Optional)* Browser context to use when called on the browser endpoint.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_interest_group_tracking(enable)

Enables/Disables issuing of interestGroupAccessed events.

**EXPERIMENTAL**

* **Parameters:**
  **enable** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_shared_storage_entry(owner_origin, key, value, ignore_if_present=None)

Sets entry with `key` and `value` for a given origin’s shared storage.

**EXPERIMENTAL**

* **Parameters:**
  * **owner_origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **value** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **ignore_if_present** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) –  *(Optional)* If ``ignoreIfPresent``` is included and true, then only sets the entry if ```key`` doesn’t already exist.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_shared_storage_tracking(enable)

Enables/disables issuing of sharedStorageAccessed events.

**EXPERIMENTAL**

* **Parameters:**
  **enable** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_storage_bucket_tracking(storage_key, enable)

Set tracking for a storage key’s buckets.

**EXPERIMENTAL**

* **Parameters:**
  * **storage_key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **enable** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### track_cache_storage_for_origin(origin)

Registers origin to be notified when an update occurs to its cache storage list.

* **Parameters:**
  **origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Security origin.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### track_cache_storage_for_storage_key(storage_key)

Registers storage key to be notified when an update occurs to its cache storage list.

* **Parameters:**
  **storage_key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Storage key.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### track_indexed_db_for_origin(origin)

Registers origin to be notified when an update occurs to its IndexedDB.

* **Parameters:**
  **origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Security origin.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### track_indexed_db_for_storage_key(storage_key)

Registers storage key to be notified when an update occurs to its IndexedDB.

* **Parameters:**
  **storage_key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Storage key.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### untrack_cache_storage_for_origin(origin)

Unregisters origin from receiving notifications for cache storage.

* **Parameters:**
  **origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Security origin.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### untrack_cache_storage_for_storage_key(storage_key)

Unregisters storage key from receiving notifications for cache storage.

* **Parameters:**
  **storage_key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Storage key.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### untrack_indexed_db_for_origin(origin)

Unregisters origin from receiving notifications for IndexedDB.

* **Parameters:**
  **origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Security origin.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### untrack_indexed_db_for_storage_key(storage_key)

Unregisters storage key from receiving notifications for IndexedDB.

* **Parameters:**
  **storage_key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Storage key.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* CacheStorageContentUpdated(origin, storage_key, bucket_id, cache_name)

A cache’s contents have been modified.

#### origin *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Origin to update.

#### storage_key *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Storage key to update.

#### bucket_id *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Storage bucket to update.

#### cache_name *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name of cache in origin.

### *class* CacheStorageListUpdated(origin, storage_key, bucket_id)

A cache has been added/deleted.

#### origin *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Origin to update.

#### storage_key *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Storage key to update.

#### bucket_id *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Storage bucket to update.

### *class* IndexedDBContentUpdated(origin, storage_key, bucket_id, database_name, object_store_name)

The origin’s IndexedDB object store has been modified.

#### origin *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Origin to update.

#### storage_key *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Storage key to update.

#### bucket_id *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Storage bucket to update.

#### database_name *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Database to update.

#### object_store_name *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

ObjectStore to update.

### *class* IndexedDBListUpdated(origin, storage_key, bucket_id)

The origin’s IndexedDB database list has been modified.

#### origin *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Origin to update.

#### storage_key *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Storage key to update.

#### bucket_id *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Storage bucket to update.

### *class* InterestGroupAccessed(access_time, type_, owner_origin, name)

One of the interest groups was accessed by the associated page.

#### access_time *: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

#### type_ *: [`InterestGroupAccessType`](#nodriver.cdp.storage.InterestGroupAccessType)*

#### owner_origin *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### name *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* SharedStorageAccessed(access_time, type_, main_frame_id, owner_origin, params)

Shared storage was accessed by the associated page.
The following parameters are included in all events.

#### access_time *: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

Time of the access.

#### type_ *: [`SharedStorageAccessType`](#nodriver.cdp.storage.SharedStorageAccessType)*

Enum value indicating the Shared Storage API method invoked.

#### main_frame_id *: [`FrameId`](page.md#nodriver.cdp.page.FrameId)*

DevTools Frame Token for the primary frame tree’s root.

#### owner_origin *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Serialized origin for the context that invoked the Shared Storage API.

#### params *: [`SharedStorageAccessParams`](#nodriver.cdp.storage.SharedStorageAccessParams)*

The sub-parameters warapped by `params` are all optional and their
presence/absence depends on `type`.

### *class* StorageBucketCreatedOrUpdated(bucket_info)

#### bucket_info *: [`StorageBucketInfo`](#nodriver.cdp.storage.StorageBucketInfo)*

### *class* StorageBucketDeleted(bucket_id)

#### bucket_id *: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* AttributionReportingSourceRegistered(registration, result)

**EXPERIMENTAL**

#### registration *: [`AttributionReportingSourceRegistration`](#nodriver.cdp.storage.AttributionReportingSourceRegistration)*

#### result *: [`AttributionReportingSourceRegistrationResult`](#nodriver.cdp.storage.AttributionReportingSourceRegistrationResult)*

### *class* AttributionReportingTriggerRegistered(registration, event_level, aggregatable)

**EXPERIMENTAL**

#### registration *: [`AttributionReportingTriggerRegistration`](#nodriver.cdp.storage.AttributionReportingTriggerRegistration)*

#### event_level *: [`AttributionReportingEventLevelResult`](#nodriver.cdp.storage.AttributionReportingEventLevelResult)*

#### aggregatable *: [`AttributionReportingAggregatableResult`](#nodriver.cdp.storage.AttributionReportingAggregatableResult)*
