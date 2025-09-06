# Network

Network domain allows tracking network activities of the page. It exposes information about http,
file, data and other requests and responses, their headers, bodies, timing, etc.

<a id="module-nodriver.cdp.network"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* ResourceType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Resource type as it was perceived by the rendering engine.

#### DOCUMENT *= 'Document'*

#### STYLESHEET *= 'Stylesheet'*

#### IMAGE *= 'Image'*

#### MEDIA *= 'Media'*

#### FONT *= 'Font'*

#### SCRIPT *= 'Script'*

#### TEXT_TRACK *= 'TextTrack'*

#### XHR *= 'XHR'*

#### FETCH *= 'Fetch'*

#### PREFETCH *= 'Prefetch'*

#### EVENT_SOURCE *= 'EventSource'*

#### WEB_SOCKET *= 'WebSocket'*

#### MANIFEST *= 'Manifest'*

#### SIGNED_EXCHANGE *= 'SignedExchange'*

#### PING *= 'Ping'*

#### CSP_VIOLATION_REPORT *= 'CSPViolationReport'*

#### PREFLIGHT *= 'Preflight'*

#### FED_CM *= 'FedCM'*

#### OTHER *= 'Other'*

### *class* LoaderId

Unique loader identifier.

### *class* RequestId

Unique network request identifier.
Note that this does not identify individual HTTP requests that are part of
a network request.

### *class* InterceptionId

Unique intercepted request identifier.

### *class* ErrorReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Network level fetch failure reason.

#### FAILED *= 'Failed'*

#### ABORTED *= 'Aborted'*

#### TIMED_OUT *= 'TimedOut'*

#### ACCESS_DENIED *= 'AccessDenied'*

#### CONNECTION_CLOSED *= 'ConnectionClosed'*

#### CONNECTION_RESET *= 'ConnectionReset'*

#### CONNECTION_REFUSED *= 'ConnectionRefused'*

#### CONNECTION_ABORTED *= 'ConnectionAborted'*

#### CONNECTION_FAILED *= 'ConnectionFailed'*

#### NAME_NOT_RESOLVED *= 'NameNotResolved'*

#### INTERNET_DISCONNECTED *= 'InternetDisconnected'*

#### ADDRESS_UNREACHABLE *= 'AddressUnreachable'*

#### BLOCKED_BY_CLIENT *= 'BlockedByClient'*

#### BLOCKED_BY_RESPONSE *= 'BlockedByResponse'*

### *class* TimeSinceEpoch(x=0, /)

UTC time in seconds, counted from January 1, 1970.

### *class* MonotonicTime(x=0, /)

Monotonically increasing time in seconds since an arbitrary point in the past.

### *class* Headers

Request / response headers as keys / values of JSON object.

### *class* ConnectionType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The underlying connection technology that the browser is supposedly using.

#### NONE *= 'none'*

#### CELLULAR2G *= 'cellular2g'*

#### CELLULAR3G *= 'cellular3g'*

#### CELLULAR4G *= 'cellular4g'*

#### BLUETOOTH *= 'bluetooth'*

#### ETHERNET *= 'ethernet'*

#### WIFI *= 'wifi'*

#### WIMAX *= 'wimax'*

#### OTHER *= 'other'*

### *class* CookieSameSite(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Represents the cookie’s ‘SameSite’ status:
[https://tools.ietf.org/html/draft-west-first-party-cookies](https://tools.ietf.org/html/draft-west-first-party-cookies)

#### STRICT *= 'Strict'*

#### LAX *= 'Lax'*

#### NONE *= 'None'*

### *class* CookiePriority(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Represents the cookie’s ‘Priority’ status:
[https://tools.ietf.org/html/draft-west-cookie-priority-00](https://tools.ietf.org/html/draft-west-cookie-priority-00)

#### LOW *= 'Low'*

#### MEDIUM *= 'Medium'*

#### HIGH *= 'High'*

### *class* CookieSourceScheme(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Represents the source scheme of the origin that originally set the cookie.
A value of “Unset” allows protocol clients to emulate legacy cookie scope for the scheme.
This is a temporary ability and it will be removed in the future.

#### UNSET *= 'Unset'*

#### NON_SECURE *= 'NonSecure'*

#### SECURE *= 'Secure'*

### *class* ResourceTiming(request_time, proxy_start, proxy_end, dns_start, dns_end, connect_start, connect_end, ssl_start, ssl_end, worker_start, worker_ready, worker_fetch_start, worker_respond_with_settled, send_start, send_end, push_start, push_end, receive_headers_start, receive_headers_end, worker_router_evaluation_start=None, worker_cache_lookup_start=None)

Timing information for the request.

#### request_time*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Timing’s requestTime is a baseline in seconds, while the other numbers are ticks in
milliseconds relatively to this requestTime.

#### proxy_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started resolving proxy.

#### proxy_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Finished resolving proxy.

#### dns_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started DNS address resolve.

#### dns_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Finished DNS address resolve.

#### connect_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started connecting to the remote host.

#### connect_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Connected to the remote host.

#### ssl_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started SSL handshake.

#### ssl_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Finished SSL handshake.

#### worker_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started running ServiceWorker.

#### worker_ready*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Finished Starting ServiceWorker.

#### worker_fetch_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started fetch event.

#### worker_respond_with_settled*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Settled fetch event respondWith promise.

#### send_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started sending request.

#### send_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Finished sending request.

#### push_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Time the server started pushing request.

#### push_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Time the server finished pushing request.

#### receive_headers_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started receiving response headers.

#### receive_headers_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Finished receiving response headers.

#### worker_router_evaluation_start*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Started ServiceWorker static routing source evaluation.

#### worker_cache_lookup_start*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Started cache lookup when the source was evaluated to `cache`.

### *class* ResourcePriority(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Loading priority of a resource request.

#### VERY_LOW *= 'VeryLow'*

#### LOW *= 'Low'*

#### MEDIUM *= 'Medium'*

#### HIGH *= 'High'*

#### VERY_HIGH *= 'VeryHigh'*

### *class* PostDataEntry(bytes_=None)

Post data entry for HTTP request

#### bytes_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* Request(url, method, headers, initial_priority, referrer_policy, url_fragment=None, post_data=None, has_post_data=None, post_data_entries=None, mixed_content_type=None, is_link_preload=None, trust_token_params=None, is_same_site=None)

HTTP request data.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Request URL (without fragment).

#### method*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

HTTP request method.

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

HTTP request headers.

#### initial_priority*: [`ResourcePriority`](#nodriver.cdp.network.ResourcePriority)*

Priority of the resource request at the time request is sent.

#### referrer_policy*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

//www.w3.org/TR/referrer-policy/

* **Type:**
  The referrer policy of the request, as defined in https

#### url_fragment*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Fragment of the requested URL starting with hash, if present.

#### post_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

HTTP POST request data.
Use postDataEntries instead.

#### has_post_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True when the request has POST data. Note that postData might still be omitted when this flag is true when the data is too long.

#### post_data_entries*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PostDataEntry`](#nodriver.cdp.network.PostDataEntry)]]* *= None*

Request body elements (post data broken into individual entries).

#### mixed_content_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`MixedContentType`](security.md#nodriver.cdp.security.MixedContentType)]* *= None*

The mixed content type of the request.

#### is_link_preload*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether is loaded via link preload.

#### trust_token_params*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TrustTokenParams`](#nodriver.cdp.network.TrustTokenParams)]* *= None*

Set for requests when the TrustToken API is used. Contains the parameters
passed by the developer (e.g. via “fetch”) as understood by the backend.

#### is_same_site*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if this resource request is considered to be the ‘same site’ as the
request corresponding to the main frame.

### *class* SignedCertificateTimestamp(status, origin, log_description, log_id, timestamp, hash_algorithm, signature_algorithm, signature_data)

Details of a signed certificate timestamp (SCT).

#### status*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Validation status.

#### origin*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Origin.

#### log_description*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Log name / description.

#### log_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Log ID.

#### timestamp*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Issuance date. Unlike TimeSinceEpoch, this contains the number of
milliseconds since January 1, 1970, UTC, not the number of seconds.

#### hash_algorithm*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Hash algorithm.

#### signature_algorithm*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signature algorithm.

#### signature_data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signature data.

### *class* SecurityDetails(protocol, key_exchange, cipher, certificate_id, subject_name, san_list, issuer, valid_from, valid_to, signed_certificate_timestamp_list, certificate_transparency_compliance, encrypted_client_hello, key_exchange_group=None, mac=None, server_signature_algorithm=None)

Security details about a request.

#### protocol*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Protocol name (e.g. “TLS 1.2” or “QUIC”).

#### key_exchange*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Key Exchange used by the connection, or the empty string if not applicable.

#### cipher*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cipher name.

#### certificate_id*: [`CertificateId`](security.md#nodriver.cdp.security.CertificateId)*

Certificate ID value.

#### subject_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Certificate subject name.

#### san_list*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Subject Alternative Name (SAN) DNS names and IP addresses.

#### issuer*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name of the issuing CA.

#### valid_from*: [`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)*

Certificate valid from date.

#### valid_to*: [`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)*

Certificate valid to (expiration) date

#### signed_certificate_timestamp_list*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SignedCertificateTimestamp`](#nodriver.cdp.network.SignedCertificateTimestamp)]*

List of signed certificate timestamps (SCTs).

#### certificate_transparency_compliance*: [`CertificateTransparencyCompliance`](#nodriver.cdp.network.CertificateTransparencyCompliance)*

Whether the request complied with Certificate Transparency policy

#### encrypted_client_hello*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether the connection used Encrypted ClientHello

#### key_exchange_group*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

(EC)DH group used by the connection, if applicable.

#### mac*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

TLS MAC. Note that AEAD ciphers do not have separate MACs.

#### server_signature_algorithm*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

The signature algorithm used by the server in the TLS server signature,
represented as a TLS SignatureScheme code point. Omitted if not
applicable or not known.

### *class* CertificateTransparencyCompliance(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Whether the request complied with Certificate Transparency policy.

#### UNKNOWN *= 'unknown'*

#### NOT_COMPLIANT *= 'not-compliant'*

#### COMPLIANT *= 'compliant'*

### *class* BlockedReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The reason why request was blocked.

#### OTHER *= 'other'*

#### CSP *= 'csp'*

#### MIXED_CONTENT *= 'mixed-content'*

#### ORIGIN *= 'origin'*

#### INSPECTOR *= 'inspector'*

#### INTEGRITY *= 'integrity'*

#### SUBRESOURCE_FILTER *= 'subresource-filter'*

#### CONTENT_TYPE *= 'content-type'*

#### COEP_FRAME_RESOURCE_NEEDS_COEP_HEADER *= 'coep-frame-resource-needs-coep-header'*

#### COOP_SANDBOXED_IFRAME_CANNOT_NAVIGATE_TO_COOP_PAGE *= 'coop-sandboxed-iframe-cannot-navigate-to-coop-page'*

#### CORP_NOT_SAME_ORIGIN *= 'corp-not-same-origin'*

#### CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP *= 'corp-not-same-origin-after-defaulted-to-same-origin-by-coep'*

#### CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_DIP *= 'corp-not-same-origin-after-defaulted-to-same-origin-by-dip'*

#### CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP_AND_DIP *= 'corp-not-same-origin-after-defaulted-to-same-origin-by-coep-and-dip'*

#### CORP_NOT_SAME_SITE *= 'corp-not-same-site'*

#### SRI_MESSAGE_SIGNATURE_MISMATCH *= 'sri-message-signature-mismatch'*

### *class* IpProxyStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Sets Controls for IP Proxy of requests.
Page reload is required before the new behavior will be observed.

#### AVAILABLE *= 'Available'*

#### FEATURE_NOT_ENABLED *= 'FeatureNotEnabled'*

#### MASKED_DOMAIN_LIST_NOT_ENABLED *= 'MaskedDomainListNotEnabled'*

#### MASKED_DOMAIN_LIST_NOT_POPULATED *= 'MaskedDomainListNotPopulated'*

#### AUTH_TOKENS_UNAVAILABLE *= 'AuthTokensUnavailable'*

#### UNAVAILABLE *= 'Unavailable'*

#### BYPASSED_BY_DEV_TOOLS *= 'BypassedByDevTools'*

### *class* CorsError(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The reason why request was blocked.

#### DISALLOWED_BY_MODE *= 'DisallowedByMode'*

#### INVALID_RESPONSE *= 'InvalidResponse'*

#### WILDCARD_ORIGIN_NOT_ALLOWED *= 'WildcardOriginNotAllowed'*

#### MISSING_ALLOW_ORIGIN_HEADER *= 'MissingAllowOriginHeader'*

#### MULTIPLE_ALLOW_ORIGIN_VALUES *= 'MultipleAllowOriginValues'*

#### INVALID_ALLOW_ORIGIN_VALUE *= 'InvalidAllowOriginValue'*

#### ALLOW_ORIGIN_MISMATCH *= 'AllowOriginMismatch'*

#### INVALID_ALLOW_CREDENTIALS *= 'InvalidAllowCredentials'*

#### CORS_DISABLED_SCHEME *= 'CorsDisabledScheme'*

#### PREFLIGHT_INVALID_STATUS *= 'PreflightInvalidStatus'*

#### PREFLIGHT_DISALLOWED_REDIRECT *= 'PreflightDisallowedRedirect'*

#### PREFLIGHT_WILDCARD_ORIGIN_NOT_ALLOWED *= 'PreflightWildcardOriginNotAllowed'*

#### PREFLIGHT_MISSING_ALLOW_ORIGIN_HEADER *= 'PreflightMissingAllowOriginHeader'*

#### PREFLIGHT_MULTIPLE_ALLOW_ORIGIN_VALUES *= 'PreflightMultipleAllowOriginValues'*

#### PREFLIGHT_INVALID_ALLOW_ORIGIN_VALUE *= 'PreflightInvalidAllowOriginValue'*

#### PREFLIGHT_ALLOW_ORIGIN_MISMATCH *= 'PreflightAllowOriginMismatch'*

#### PREFLIGHT_INVALID_ALLOW_CREDENTIALS *= 'PreflightInvalidAllowCredentials'*

#### PREFLIGHT_MISSING_ALLOW_EXTERNAL *= 'PreflightMissingAllowExternal'*

#### PREFLIGHT_INVALID_ALLOW_EXTERNAL *= 'PreflightInvalidAllowExternal'*

#### PREFLIGHT_MISSING_ALLOW_PRIVATE_NETWORK *= 'PreflightMissingAllowPrivateNetwork'*

#### PREFLIGHT_INVALID_ALLOW_PRIVATE_NETWORK *= 'PreflightInvalidAllowPrivateNetwork'*

#### INVALID_ALLOW_METHODS_PREFLIGHT_RESPONSE *= 'InvalidAllowMethodsPreflightResponse'*

#### INVALID_ALLOW_HEADERS_PREFLIGHT_RESPONSE *= 'InvalidAllowHeadersPreflightResponse'*

#### METHOD_DISALLOWED_BY_PREFLIGHT_RESPONSE *= 'MethodDisallowedByPreflightResponse'*

#### HEADER_DISALLOWED_BY_PREFLIGHT_RESPONSE *= 'HeaderDisallowedByPreflightResponse'*

#### REDIRECT_CONTAINS_CREDENTIALS *= 'RedirectContainsCredentials'*

#### INSECURE_PRIVATE_NETWORK *= 'InsecurePrivateNetwork'*

#### INVALID_PRIVATE_NETWORK_ACCESS *= 'InvalidPrivateNetworkAccess'*

#### UNEXPECTED_PRIVATE_NETWORK_ACCESS *= 'UnexpectedPrivateNetworkAccess'*

#### NO_CORS_REDIRECT_MODE_NOT_FOLLOW *= 'NoCorsRedirectModeNotFollow'*

#### PREFLIGHT_MISSING_PRIVATE_NETWORK_ACCESS_ID *= 'PreflightMissingPrivateNetworkAccessId'*

#### PREFLIGHT_MISSING_PRIVATE_NETWORK_ACCESS_NAME *= 'PreflightMissingPrivateNetworkAccessName'*

#### PRIVATE_NETWORK_ACCESS_PERMISSION_UNAVAILABLE *= 'PrivateNetworkAccessPermissionUnavailable'*

#### PRIVATE_NETWORK_ACCESS_PERMISSION_DENIED *= 'PrivateNetworkAccessPermissionDenied'*

#### LOCAL_NETWORK_ACCESS_PERMISSION_DENIED *= 'LocalNetworkAccessPermissionDenied'*

### *class* CorsErrorStatus(cors_error, failed_parameter)

#### cors_error*: [`CorsError`](#nodriver.cdp.network.CorsError)*

#### failed_parameter*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* ServiceWorkerResponseSource(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Source of serviceworker response.

#### CACHE_STORAGE *= 'cache-storage'*

#### HTTP_CACHE *= 'http-cache'*

#### FALLBACK_CODE *= 'fallback-code'*

#### NETWORK *= 'network'*

### *class* TrustTokenParams(operation, refresh_policy, issuers=None)

Determines what type of Trust Token operation is executed and
depending on the type, some additional parameters. The values
are specified in third_party/blink/renderer/core/fetch/trust_token.idl.

#### operation*: [`TrustTokenOperationType`](#nodriver.cdp.network.TrustTokenOperationType)*

#### refresh_policy*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Only set for “token-redemption” operation and determine whether
to request a fresh SRR or use a still valid cached SRR.

#### issuers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

Origins of issuers from whom to request tokens or redemption
records.

### *class* TrustTokenOperationType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### ISSUANCE *= 'Issuance'*

#### REDEMPTION *= 'Redemption'*

#### SIGNING *= 'Signing'*

### *class* AlternateProtocolUsage(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The reason why Chrome uses a specific transport protocol for HTTP semantics.

#### ALTERNATIVE_JOB_WON_WITHOUT_RACE *= 'alternativeJobWonWithoutRace'*

#### ALTERNATIVE_JOB_WON_RACE *= 'alternativeJobWonRace'*

#### MAIN_JOB_WON_RACE *= 'mainJobWonRace'*

#### MAPPING_MISSING *= 'mappingMissing'*

#### BROKEN *= 'broken'*

#### DNS_ALPN_H3_JOB_WON_WITHOUT_RACE *= 'dnsAlpnH3JobWonWithoutRace'*

#### DNS_ALPN_H3_JOB_WON_RACE *= 'dnsAlpnH3JobWonRace'*

#### UNSPECIFIED_REASON *= 'unspecifiedReason'*

### *class* ServiceWorkerRouterSource(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Source of service worker router.

#### NETWORK *= 'network'*

#### CACHE *= 'cache'*

#### FETCH_EVENT *= 'fetch-event'*

#### RACE_NETWORK_AND_FETCH_HANDLER *= 'race-network-and-fetch-handler'*

#### RACE_NETWORK_AND_CACHE *= 'race-network-and-cache'*

### *class* ServiceWorkerRouterInfo(rule_id_matched=None, matched_source_type=None, actual_source_type=None)

#### rule_id_matched*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

ID of the rule matched. If there is a matched rule, this field will
be set, otherwiser no value will be set.

#### matched_source_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ServiceWorkerRouterSource`](#nodriver.cdp.network.ServiceWorkerRouterSource)]* *= None*

The router source of the matched rule. If there is a matched rule, this
field will be set, otherwise no value will be set.

#### actual_source_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ServiceWorkerRouterSource`](#nodriver.cdp.network.ServiceWorkerRouterSource)]* *= None*

The actual router source used.

### *class* Response(url, status, status_text, headers, mime_type, charset, connection_reused, connection_id, encoded_data_length, security_state, headers_text=None, request_headers=None, request_headers_text=None, remote_ip_address=None, remote_port=None, from_disk_cache=None, from_service_worker=None, from_prefetch_cache=None, from_early_hints=None, service_worker_router_info=None, timing=None, service_worker_response_source=None, response_time=None, cache_storage_cache_name=None, protocol=None, alternate_protocol_usage=None, security_details=None, is_ip_protection_used=None)

HTTP response data.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Response URL. This URL can be different from CachedResource.url in case of redirect.

#### status*: [`int`](https://docs.python.org/3/library/functions.html#int)*

HTTP response status code.

#### status_text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

HTTP response status text.

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

HTTP response headers.

#### mime_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Resource mimeType as determined by the browser.

#### charset*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Resource charset as determined by the browser (if applicable).

#### connection_reused*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Specifies whether physical connection was actually reused for this request.

#### connection_id*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Physical connection id that was actually used for this request.

#### encoded_data_length*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Total number of bytes received for this request so far.

#### security_state*: [`SecurityState`](security.md#nodriver.cdp.security.SecurityState)*

Security state of the request resource.

#### headers_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

HTTP response headers text. This has been replaced by the headers in Network.responseReceivedExtraInfo.

#### request_headers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Headers`](#nodriver.cdp.network.Headers)]* *= None*

Refined HTTP request headers that were actually transmitted over the network.

#### request_headers_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

HTTP request headers text. This has been replaced by the headers in Network.requestWillBeSentExtraInfo.

#### remote_ip_address*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Remote IP address.

#### remote_port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Remote port.

#### from_disk_cache*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Specifies that the request was served from the disk cache.

#### from_service_worker*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Specifies that the request was served from the ServiceWorker.

#### from_prefetch_cache*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Specifies that the request was served from the prefetch cache.

#### from_early_hints*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Specifies that the request was served from the prefetch cache.

#### service_worker_router_info*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ServiceWorkerRouterInfo`](#nodriver.cdp.network.ServiceWorkerRouterInfo)]* *= None*

Information about how ServiceWorker Static Router API was used. If this
field is set with `matchedSourceType` field, a matching rule is found.
If this field is set without `matchedSource`, no matching rule is found.
Otherwise, the API is not used.

#### timing*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ResourceTiming`](#nodriver.cdp.network.ResourceTiming)]* *= None*

Timing information for the given request.

#### service_worker_response_source*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ServiceWorkerResponseSource`](#nodriver.cdp.network.ServiceWorkerResponseSource)]* *= None*

Response source of response from ServiceWorker.

#### response_time*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)]* *= None*

The time at which the returned response was generated.

#### cache_storage_cache_name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Cache Storage Cache Name.

#### protocol*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Protocol used to fetch this request.

#### alternate_protocol_usage*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AlternateProtocolUsage`](#nodriver.cdp.network.AlternateProtocolUsage)]* *= None*

The reason why Chrome uses a specific transport protocol for HTTP semantics.

#### security_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SecurityDetails`](#nodriver.cdp.network.SecurityDetails)]* *= None*

Security details for the request.

#### is_ip_protection_used*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Indicates whether the request was sent through IP Protection proxies. If
set to true, the request used the IP Protection privacy feature.

### *class* WebSocketRequest(headers)

WebSocket request data.

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

HTTP request headers.

### *class* WebSocketResponse(status, status_text, headers, headers_text=None, request_headers=None, request_headers_text=None)

WebSocket response data.

#### status*: [`int`](https://docs.python.org/3/library/functions.html#int)*

HTTP response status code.

#### status_text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

HTTP response status text.

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

HTTP response headers.

#### headers_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

HTTP response headers text.

#### request_headers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Headers`](#nodriver.cdp.network.Headers)]* *= None*

HTTP request headers.

#### request_headers_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

HTTP request headers text.

### *class* WebSocketFrame(opcode, mask, payload_data)

WebSocket message data. This represents an entire WebSocket message, not just a fragmented frame as the name suggests.

#### opcode*: [`float`](https://docs.python.org/3/library/functions.html#float)*

WebSocket message opcode.

#### mask*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

WebSocket message mask.

#### payload_data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

WebSocket message payload data.
If the opcode is 1, this is a text message and payloadData is a UTF-8 string.
If the opcode isn’t 1, then payloadData is a base64 encoded string representing binary data.

### *class* CachedResource(url, type_, body_size, response=None)

Information about the cached resource.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Resource URL. This is the url of the original network request.

#### type_*: [`ResourceType`](#nodriver.cdp.network.ResourceType)*

Type of this resource.

#### body_size*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Cached response body size.

#### response*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Response`](#nodriver.cdp.network.Response)]* *= None*

Cached response data.

### *class* Initiator(type_, stack=None, url=None, line_number=None, column_number=None, request_id=None)

Information about the request initiator.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Type of this initiator.

#### stack*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTrace`](runtime.md#nodriver.cdp.runtime.StackTrace)]* *= None*

Initiator JavaScript stack trace, set for Script only.
Requires the Debugger domain to be enabled.

#### url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Initiator URL, set for Parser type or for Script type (when script is importing module) or for SignedExchange type.

#### line_number*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Initiator line number, set for Parser type or for Script type (when script is importing
module) (0-based).

#### column_number*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Initiator column number, set for Parser type or for Script type (when script is importing
module) (0-based).

#### request_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestId`](#nodriver.cdp.network.RequestId)]* *= None*

Set if another request triggered this request (e.g. preflight).

### *class* CookiePartitionKey(top_level_site, has_cross_site_ancestor)

cookiePartitionKey object
The representation of the components of the key that are created by the cookiePartitionKey class contained in net/cookies/cookie_partition_key.h.

#### top_level_site*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The site of the top-level URL the browser was visiting at the start
of the request to the endpoint that set the cookie.

#### has_cross_site_ancestor*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Indicates if the cookie has any ancestors that are cross-site to the topLevelSite.

### *class* Cookie(name, value, domain, path, size, http_only, secure, session, priority, same_party, source_scheme, source_port, expires=None, same_site=None, partition_key=None, partition_key_opaque=None)

Cookie object

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cookie name.

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cookie value.

#### domain*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cookie domain.

#### path*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cookie path.

#### size*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Cookie size.

#### http_only*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if cookie is http-only.

#### secure*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if cookie is secure.

#### session*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True in case of session cookie.

#### priority*: [`CookiePriority`](#nodriver.cdp.network.CookiePriority)*

Cookie Priority

#### same_party*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if cookie is SameParty.

#### source_scheme*: [`CookieSourceScheme`](#nodriver.cdp.network.CookieSourceScheme)*

Cookie source scheme type.

#### source_port*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port.
An unspecified port value allows protocol clients to emulate legacy cookie scope for the port.
This is a temporary ability and it will be removed in the future.

#### expires*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Cookie expiration date as the number of seconds since the UNIX epoch.

#### same_site*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookieSameSite`](#nodriver.cdp.network.CookieSameSite)]* *= None*

Cookie SameSite type.

#### partition_key*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookiePartitionKey`](#nodriver.cdp.network.CookiePartitionKey)]* *= None*

Cookie partition key.

#### partition_key_opaque*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if cookie partition key is opaque.

### *class* SetCookieBlockedReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Types of reasons why a cookie may not be stored from a response.

#### SECURE_ONLY *= 'SecureOnly'*

#### SAME_SITE_STRICT *= 'SameSiteStrict'*

#### SAME_SITE_LAX *= 'SameSiteLax'*

#### SAME_SITE_UNSPECIFIED_TREATED_AS_LAX *= 'SameSiteUnspecifiedTreatedAsLax'*

#### SAME_SITE_NONE_INSECURE *= 'SameSiteNoneInsecure'*

#### USER_PREFERENCES *= 'UserPreferences'*

#### THIRD_PARTY_PHASEOUT *= 'ThirdPartyPhaseout'*

#### THIRD_PARTY_BLOCKED_IN_FIRST_PARTY_SET *= 'ThirdPartyBlockedInFirstPartySet'*

#### SYNTAX_ERROR *= 'SyntaxError'*

#### SCHEME_NOT_SUPPORTED *= 'SchemeNotSupported'*

#### OVERWRITE_SECURE *= 'OverwriteSecure'*

#### INVALID_DOMAIN *= 'InvalidDomain'*

#### INVALID_PREFIX *= 'InvalidPrefix'*

#### UNKNOWN_ERROR *= 'UnknownError'*

#### SCHEMEFUL_SAME_SITE_STRICT *= 'SchemefulSameSiteStrict'*

#### SCHEMEFUL_SAME_SITE_LAX *= 'SchemefulSameSiteLax'*

#### SCHEMEFUL_SAME_SITE_UNSPECIFIED_TREATED_AS_LAX *= 'SchemefulSameSiteUnspecifiedTreatedAsLax'*

#### SAME_PARTY_FROM_CROSS_PARTY_CONTEXT *= 'SamePartyFromCrossPartyContext'*

#### SAME_PARTY_CONFLICTS_WITH_OTHER_ATTRIBUTES *= 'SamePartyConflictsWithOtherAttributes'*

#### NAME_VALUE_PAIR_EXCEEDS_MAX_SIZE *= 'NameValuePairExceedsMaxSize'*

#### DISALLOWED_CHARACTER *= 'DisallowedCharacter'*

#### NO_COOKIE_CONTENT *= 'NoCookieContent'*

### *class* CookieBlockedReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Types of reasons why a cookie may not be sent with a request.

#### SECURE_ONLY *= 'SecureOnly'*

#### NOT_ON_PATH *= 'NotOnPath'*

#### DOMAIN_MISMATCH *= 'DomainMismatch'*

#### SAME_SITE_STRICT *= 'SameSiteStrict'*

#### SAME_SITE_LAX *= 'SameSiteLax'*

#### SAME_SITE_UNSPECIFIED_TREATED_AS_LAX *= 'SameSiteUnspecifiedTreatedAsLax'*

#### SAME_SITE_NONE_INSECURE *= 'SameSiteNoneInsecure'*

#### USER_PREFERENCES *= 'UserPreferences'*

#### THIRD_PARTY_PHASEOUT *= 'ThirdPartyPhaseout'*

#### THIRD_PARTY_BLOCKED_IN_FIRST_PARTY_SET *= 'ThirdPartyBlockedInFirstPartySet'*

#### UNKNOWN_ERROR *= 'UnknownError'*

#### SCHEMEFUL_SAME_SITE_STRICT *= 'SchemefulSameSiteStrict'*

#### SCHEMEFUL_SAME_SITE_LAX *= 'SchemefulSameSiteLax'*

#### SCHEMEFUL_SAME_SITE_UNSPECIFIED_TREATED_AS_LAX *= 'SchemefulSameSiteUnspecifiedTreatedAsLax'*

#### SAME_PARTY_FROM_CROSS_PARTY_CONTEXT *= 'SamePartyFromCrossPartyContext'*

#### NAME_VALUE_PAIR_EXCEEDS_MAX_SIZE *= 'NameValuePairExceedsMaxSize'*

#### PORT_MISMATCH *= 'PortMismatch'*

#### SCHEME_MISMATCH *= 'SchemeMismatch'*

#### ANONYMOUS_CONTEXT *= 'AnonymousContext'*

### *class* CookieExemptionReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Types of reasons why a cookie should have been blocked by 3PCD but is exempted for the request.

#### NONE *= 'None'*

#### USER_SETTING *= 'UserSetting'*

#### TPCD_METADATA *= 'TPCDMetadata'*

#### TPCD_DEPRECATION_TRIAL *= 'TPCDDeprecationTrial'*

#### TOP_LEVEL_TPCD_DEPRECATION_TRIAL *= 'TopLevelTPCDDeprecationTrial'*

#### TPCD_HEURISTICS *= 'TPCDHeuristics'*

#### ENTERPRISE_POLICY *= 'EnterprisePolicy'*

#### STORAGE_ACCESS *= 'StorageAccess'*

#### TOP_LEVEL_STORAGE_ACCESS *= 'TopLevelStorageAccess'*

#### SCHEME *= 'Scheme'*

#### SAME_SITE_NONE_COOKIES_IN_SANDBOX *= 'SameSiteNoneCookiesInSandbox'*

### *class* BlockedSetCookieWithReason(blocked_reasons, cookie_line, cookie=None)

A cookie which was not stored from a response with the corresponding reason.

#### blocked_reasons*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SetCookieBlockedReason`](#nodriver.cdp.network.SetCookieBlockedReason)]*

The reason(s) this cookie was blocked.

#### cookie_line*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The string representing this individual cookie as it would appear in the header.
This is not the entire “cookie” or “set-cookie” header which could have multiple cookies.

#### cookie*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Cookie`](#nodriver.cdp.network.Cookie)]* *= None*

The cookie object which represents the cookie which was not stored. It is optional because
sometimes complete cookie information is not available, such as in the case of parsing
errors.

### *class* ExemptedSetCookieWithReason(exemption_reason, cookie_line, cookie)

A cookie should have been blocked by 3PCD but is exempted and stored from a response with the
corresponding reason. A cookie could only have at most one exemption reason.

#### exemption_reason*: [`CookieExemptionReason`](#nodriver.cdp.network.CookieExemptionReason)*

The reason the cookie was exempted.

#### cookie_line*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The string representing this individual cookie as it would appear in the header.

#### cookie*: [`Cookie`](#nodriver.cdp.network.Cookie)*

The cookie object representing the cookie.

### *class* AssociatedCookie(cookie, blocked_reasons, exemption_reason=None)

A cookie associated with the request which may or may not be sent with it.
Includes the cookies itself and reasons for blocking or exemption.

#### cookie*: [`Cookie`](#nodriver.cdp.network.Cookie)*

The cookie object representing the cookie which was not sent.

#### blocked_reasons*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CookieBlockedReason`](#nodriver.cdp.network.CookieBlockedReason)]*

The reason(s) the cookie was blocked. If empty means the cookie is included.

#### exemption_reason*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookieExemptionReason`](#nodriver.cdp.network.CookieExemptionReason)]* *= None*

The reason the cookie should have been blocked by 3PCD but is exempted. A cookie could
only have at most one exemption reason.

### *class* CookieParam(name, value, url=None, domain=None, path=None, secure=None, http_only=None, same_site=None, expires=None, priority=None, same_party=None, source_scheme=None, source_port=None, partition_key=None)

Cookie parameter object

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cookie name.

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cookie value.

#### url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The request-URI to associate with the setting of the cookie. This value can affect the
default domain, path, source port, and source scheme values of the created cookie.

#### domain*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Cookie domain.

#### path*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Cookie path.

#### secure*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if cookie is secure.

#### http_only*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if cookie is http-only.

#### same_site*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookieSameSite`](#nodriver.cdp.network.CookieSameSite)]* *= None*

Cookie SameSite type.

#### expires*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)]* *= None*

Cookie expiration date, session cookie if not set

#### priority*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookiePriority`](#nodriver.cdp.network.CookiePriority)]* *= None*

Cookie Priority.

#### same_party*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if cookie is SameParty.

#### source_scheme*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookieSourceScheme`](#nodriver.cdp.network.CookieSourceScheme)]* *= None*

Cookie source scheme type.

#### source_port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port.
An unspecified port value allows protocol clients to emulate legacy cookie scope for the port.
This is a temporary ability and it will be removed in the future.

#### partition_key*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookiePartitionKey`](#nodriver.cdp.network.CookiePartitionKey)]* *= None*

Cookie partition key. If not set, the cookie will be set as not partitioned.

### *class* AuthChallenge(origin, scheme, realm, source=None)

Authorization challenge for HTTP status code 401 or 407.

#### origin*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Origin of the challenger.

#### scheme*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The authentication scheme used, such as basic or digest

#### realm*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The realm of the challenge. May be empty.

#### source*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Source of the authentication challenge.

### *class* AuthChallengeResponse(response, username=None, password=None)

Response to an AuthChallenge.

#### response*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The decision on what to do in response to the authorization challenge.  Default means
deferring to the default behavior of the net stack, which will likely either the Cancel
authentication or display a popup dialog box.

#### username*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The username to provide, possibly empty. Should only be set if response is
ProvideCredentials.

#### password*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The password to provide, possibly empty. Should only be set if response is
ProvideCredentials.

### *class* InterceptionStage(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Stages of the interception to begin intercepting. Request will intercept before the request is
sent. Response will intercept after the response is received.

#### REQUEST *= 'Request'*

#### HEADERS_RECEIVED *= 'HeadersReceived'*

### *class* RequestPattern(url_pattern=None, resource_type=None, interception_stage=None)

Request pattern for interception.

#### url_pattern*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Wildcards (`'*'` -> zero or more, `'?'` -> exactly one) are allowed. Escape character is
backslash. Omitting is equivalent to `"*"`.

#### resource_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ResourceType`](#nodriver.cdp.network.ResourceType)]* *= None*

If set, only requests for matching resource types will be intercepted.

#### interception_stage*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`InterceptionStage`](#nodriver.cdp.network.InterceptionStage)]* *= None*

Stage at which to begin intercepting requests. Default is Request.

### *class* SignedExchangeSignature(label, signature, integrity, validity_url, date, expires, cert_url=None, cert_sha256=None, certificates=None)

Information about a signed exchange signature.
[https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1](https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1)

#### label*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signed exchange signature label.

#### signature*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The hex string of signed exchange signature.

#### integrity*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signed exchange signature integrity.

#### validity_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signed exchange signature validity Url.

#### date*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Signed exchange signature date.

#### expires*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Signed exchange signature expires.

#### cert_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Signed exchange signature cert Url.

#### cert_sha256*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The hex string of signed exchange signature cert sha256.

#### certificates*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

The encoded certificates.

### *class* SignedExchangeHeader(request_url, response_code, response_headers, signatures, header_integrity)

Information about a signed exchange header.
[https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation](https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation)

#### request_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signed exchange request URL.

#### response_code*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Signed exchange response code.

#### response_headers*: [`Headers`](#nodriver.cdp.network.Headers)*

Signed exchange response headers.

#### signatures*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SignedExchangeSignature`](#nodriver.cdp.network.SignedExchangeSignature)]*

Signed exchange response signature.

#### header_integrity*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signed exchange header integrity hash in the form of `sha256-<base64-hash-value>`.

### *class* SignedExchangeErrorField(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Field type for a signed exchange related error.

#### SIGNATURE_SIG *= 'signatureSig'*

#### SIGNATURE_INTEGRITY *= 'signatureIntegrity'*

#### SIGNATURE_CERT_URL *= 'signatureCertUrl'*

#### SIGNATURE_CERT_SHA256 *= 'signatureCertSha256'*

#### SIGNATURE_VALIDITY_URL *= 'signatureValidityUrl'*

#### SIGNATURE_TIMESTAMPS *= 'signatureTimestamps'*

### *class* SignedExchangeError(message, signature_index=None, error_field=None)

Information about a signed exchange response.

#### message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Error message.

#### signature_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

The index of the signature which caused the error.

#### error_field*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SignedExchangeErrorField`](#nodriver.cdp.network.SignedExchangeErrorField)]* *= None*

The field which caused the error.

### *class* SignedExchangeInfo(outer_response, has_extra_info, header=None, security_details=None, errors=None)

Information about a signed exchange response.

#### outer_response*: [`Response`](#nodriver.cdp.network.Response)*

The outer response of signed HTTP exchange which was received from network.

#### has_extra_info*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether network response for the signed exchange was accompanied by
extra headers.

#### header*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SignedExchangeHeader`](#nodriver.cdp.network.SignedExchangeHeader)]* *= None*

Information about the signed exchange header.

#### security_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SecurityDetails`](#nodriver.cdp.network.SecurityDetails)]* *= None*

Security details for the signed exchange header.

#### errors*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SignedExchangeError`](#nodriver.cdp.network.SignedExchangeError)]]* *= None*

Errors occurred while handling the signed exchange.

### *class* ContentEncoding(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

List of content encodings supported by the backend.

#### DEFLATE *= 'deflate'*

#### GZIP *= 'gzip'*

#### BR *= 'br'*

#### ZSTD *= 'zstd'*

### *class* DirectSocketDnsQueryType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### IPV4 *= 'ipv4'*

#### IPV6 *= 'ipv6'*

### *class* DirectTCPSocketOptions(no_delay, keep_alive_delay=None, send_buffer_size=None, receive_buffer_size=None, dns_query_type=None)

#### no_delay*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

TCP_NODELAY option

#### keep_alive_delay*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Expected to be unsigned integer.

#### send_buffer_size*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Expected to be unsigned integer.

#### receive_buffer_size*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Expected to be unsigned integer.

#### dns_query_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`DirectSocketDnsQueryType`](#nodriver.cdp.network.DirectSocketDnsQueryType)]* *= None*

### *class* DirectUDPSocketOptions(remote_addr=None, remote_port=None, local_addr=None, local_port=None, dns_query_type=None, send_buffer_size=None, receive_buffer_size=None)

#### remote_addr*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### remote_port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Unsigned int 16.

#### local_addr*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### local_port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Unsigned int 16.

#### dns_query_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`DirectSocketDnsQueryType`](#nodriver.cdp.network.DirectSocketDnsQueryType)]* *= None*

#### send_buffer_size*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Expected to be unsigned integer.

#### receive_buffer_size*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Expected to be unsigned integer.

### *class* DirectUDPMessage(data, remote_addr=None, remote_port=None)

#### data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### remote_addr*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Null for connected mode.

#### remote_port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Null for connected mode.
Expected to be unsigned integer.

### *class* PrivateNetworkRequestPolicy(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### ALLOW *= 'Allow'*

#### BLOCK_FROM_INSECURE_TO_MORE_PRIVATE *= 'BlockFromInsecureToMorePrivate'*

#### WARN_FROM_INSECURE_TO_MORE_PRIVATE *= 'WarnFromInsecureToMorePrivate'*

#### PREFLIGHT_BLOCK *= 'PreflightBlock'*

#### PREFLIGHT_WARN *= 'PreflightWarn'*

#### PERMISSION_BLOCK *= 'PermissionBlock'*

#### PERMISSION_WARN *= 'PermissionWarn'*

### *class* IPAddressSpace(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### LOOPBACK *= 'Loopback'*

#### LOCAL *= 'Local'*

#### PUBLIC *= 'Public'*

#### UNKNOWN *= 'Unknown'*

### *class* ConnectTiming(request_time)

#### request_time*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Timing’s requestTime is a baseline in seconds, while the other numbers are ticks in
milliseconds relatively to this requestTime. Matches ResourceTiming’s requestTime for
the same request (but not for redirected requests).

### *class* ClientSecurityState(initiator_is_secure_context, initiator_ip_address_space, private_network_request_policy)

#### initiator_is_secure_context*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### initiator_ip_address_space*: [`IPAddressSpace`](#nodriver.cdp.network.IPAddressSpace)*

#### private_network_request_policy*: [`PrivateNetworkRequestPolicy`](#nodriver.cdp.network.PrivateNetworkRequestPolicy)*

### *class* CrossOriginOpenerPolicyValue(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### SAME_ORIGIN *= 'SameOrigin'*

#### SAME_ORIGIN_ALLOW_POPUPS *= 'SameOriginAllowPopups'*

#### RESTRICT_PROPERTIES *= 'RestrictProperties'*

#### UNSAFE_NONE *= 'UnsafeNone'*

#### SAME_ORIGIN_PLUS_COEP *= 'SameOriginPlusCoep'*

#### RESTRICT_PROPERTIES_PLUS_COEP *= 'RestrictPropertiesPlusCoep'*

#### NOOPENER_ALLOW_POPUPS *= 'NoopenerAllowPopups'*

### *class* CrossOriginOpenerPolicyStatus(value, report_only_value, reporting_endpoint=None, report_only_reporting_endpoint=None)

#### value*: [`CrossOriginOpenerPolicyValue`](#nodriver.cdp.network.CrossOriginOpenerPolicyValue)*

#### report_only_value*: [`CrossOriginOpenerPolicyValue`](#nodriver.cdp.network.CrossOriginOpenerPolicyValue)*

#### reporting_endpoint*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### report_only_reporting_endpoint*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* CrossOriginEmbedderPolicyValue(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### NONE *= 'None'*

#### CREDENTIALLESS *= 'Credentialless'*

#### REQUIRE_CORP *= 'RequireCorp'*

### *class* CrossOriginEmbedderPolicyStatus(value, report_only_value, reporting_endpoint=None, report_only_reporting_endpoint=None)

#### value*: [`CrossOriginEmbedderPolicyValue`](#nodriver.cdp.network.CrossOriginEmbedderPolicyValue)*

#### report_only_value*: [`CrossOriginEmbedderPolicyValue`](#nodriver.cdp.network.CrossOriginEmbedderPolicyValue)*

#### reporting_endpoint*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### report_only_reporting_endpoint*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* ContentSecurityPolicySource(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### HTTP *= 'HTTP'*

#### META *= 'Meta'*

### *class* ContentSecurityPolicyStatus(effective_directives, is_enforced, source)

#### effective_directives*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### is_enforced*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### source*: [`ContentSecurityPolicySource`](#nodriver.cdp.network.ContentSecurityPolicySource)*

### *class* SecurityIsolationStatus(coop=None, coep=None, csp=None)

#### coop*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CrossOriginOpenerPolicyStatus`](#nodriver.cdp.network.CrossOriginOpenerPolicyStatus)]* *= None*

#### coep*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CrossOriginEmbedderPolicyStatus`](#nodriver.cdp.network.CrossOriginEmbedderPolicyStatus)]* *= None*

#### csp*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ContentSecurityPolicyStatus`](#nodriver.cdp.network.ContentSecurityPolicyStatus)]]* *= None*

### *class* ReportStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The status of a Reporting API report.

#### QUEUED *= 'Queued'*

#### PENDING *= 'Pending'*

#### MARKED_FOR_REMOVAL *= 'MarkedForRemoval'*

#### SUCCESS *= 'Success'*

### *class* ReportId

### *class* ReportingApiReport(id_, initiator_url, destination, type_, timestamp, depth, completed_attempts, body, status)

An object representing a report generated by the Reporting API.

#### id_*: [`ReportId`](#nodriver.cdp.network.ReportId)*

#### initiator_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The URL of the document that triggered the report.

#### destination*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The name of the endpoint group that should be used to deliver the report.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The type of the report (specifies the set of data that is contained in the report body).

#### timestamp*: [`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)*

When the report was generated.

#### depth*: [`int`](https://docs.python.org/3/library/functions.html#int)*

How many uploads deep the related request was.

#### completed_attempts*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The number of delivery attempts made so far, not including an active attempt.

#### body*: [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)*

#### status*: [`ReportStatus`](#nodriver.cdp.network.ReportStatus)*

### *class* ReportingApiEndpoint(url, group_name)

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The URL of the endpoint to which reports may be delivered.

#### group_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name of the endpoint group.

### *class* LoadNetworkResourcePageResult(success, net_error=None, net_error_name=None, http_status_code=None, stream=None, headers=None)

An object providing the result of a network resource load.

#### success*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### net_error*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Optional values used for error reporting.

#### net_error_name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### http_status_code*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

#### stream*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StreamHandle`](io.md#nodriver.cdp.io.StreamHandle)]* *= None*

If successful, one of the following two fields holds the result.

#### headers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Headers`](#nodriver.cdp.network.Headers)]* *= None*

Response headers.

### *class* LoadNetworkResourceOptions(disable_cache, include_credentials)

An options object that may be extended later to better support CORS,
CORB and streaming.

#### disable_cache*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### include_credentials*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### can_clear_browser_cache()

Tells whether clearing browser cache is supported.

#### Deprecated
Deprecated since version 1.3.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`bool`](https://docs.python.org/3/library/functions.html#bool)]
* **Returns:**
  True if browser cache can be cleared.

#### Deprecated
Deprecated since version 1.3.

### can_clear_browser_cookies()

Tells whether clearing browser cookies is supported.

#### Deprecated
Deprecated since version 1.3.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`bool`](https://docs.python.org/3/library/functions.html#bool)]
* **Returns:**
  True if browser cookies can be cleared.

#### Deprecated
Deprecated since version 1.3.

### can_emulate_network_conditions()

Tells whether emulation of network conditions is supported.

#### Deprecated
Deprecated since version 1.3.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`bool`](https://docs.python.org/3/library/functions.html#bool)]
* **Returns:**
  True if emulation of network conditions is supported.

#### Deprecated
Deprecated since version 1.3.

### clear_accepted_encodings_override()

Clears accepted encodings set by setAcceptedEncodings

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### clear_browser_cache()

Clears browser cache.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### clear_browser_cookies()

Clears browser cookies.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### continue_intercepted_request(interception_id, error_reason=None, raw_response=None, url=None, method=None, post_data=None, headers=None, auth_challenge_response=None)

Response to Network.requestIntercepted which either modifies the request to continue with any
modifications, or blocks it, or completes it with the provided response bytes. If a network
fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted
event will be sent with the same InterceptionId.
Deprecated, use Fetch.continueRequest, Fetch.fulfillRequest and Fetch.failRequest instead.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  * **interception_id** ([`InterceptionId`](#nodriver.cdp.network.InterceptionId)) – 
  * **error_reason** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ErrorReason`](#nodriver.cdp.network.ErrorReason)]) – *(Optional)* If set this causes the request to fail with the given reason. Passing ``Aborted``` for requests marked with ```isNavigationRequest`` also cancels the navigation. Must not be set in response to an authChallenge.
  * **raw_response** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If set the requests completes using with the provided base64 encoded raw response, including HTTP status line and headers etc… Must not be set in response to an authChallenge. (Encoded as a base64 string when passed over JSON)
  * **url** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If set the request url will be modified in a way that’s not observable by page. Must not be set in response to an authChallenge.
  * **method** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If set this allows the request method to be overridden. Must not be set in response to an authChallenge.
  * **post_data** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If set this allows postData to be set. Must not be set in response to an authChallenge.
  * **headers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Headers`](#nodriver.cdp.network.Headers)]) – *(Optional)* If set this allows the request headers to be changed. Must not be set in response to an authChallenge.
  * **auth_challenge_response** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AuthChallengeResponse`](#nodriver.cdp.network.AuthChallengeResponse)]) – *(Optional)* Response to a requestIntercepted with an authChallenge. Must not be set otherwise.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### delete_cookies(name, url=None, domain=None, path=None, partition_key=None)

Deletes browser cookies with matching name and url or domain/path/partitionKey pair.

* **Parameters:**
  * **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Name of the cookies to remove.
  * **url** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If specified, deletes all the cookies with the given name where domain and path match provided URL.
  * **domain** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If specified, deletes only cookies with the exact domain.
  * **path** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If specified, deletes only cookies with the exact path.
  * **partition_key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookiePartitionKey`](#nodriver.cdp.network.CookiePartitionKey)]) – **(EXPERIMENTAL)** *(Optional)* If specified, deletes only cookies with the the given name and partitionKey where all partition key attributes match the cookie partition key attribute.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### disable()

Disables network tracking, prevents network events from being sent to the client.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### emulate_network_conditions(offline, latency, download_throughput, upload_throughput, connection_type=None, packet_loss=None, packet_queue_length=None, packet_reordering=None)

Activates emulation of network conditions.

* **Parameters:**
  * **offline** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – True to emulate internet disconnection.
  * **latency** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Minimum latency from request sent to response headers received (ms).
  * **download_throughput** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
  * **upload_throughput** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
  * **connection_type** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ConnectionType`](#nodriver.cdp.network.ConnectionType)]) – *(Optional)* Connection type if known.
  * **packet_loss** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]) – **(EXPERIMENTAL)** *(Optional)* WebRTC packet loss (percent, 0-100). 0 disables packet loss emulation, 100 drops all the packets.
  * **packet_queue_length** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* WebRTC packet queue length (packet). 0 removes any queue length limitations.
  * **packet_reordering** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* WebRTC packetReordering feature.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable(max_total_buffer_size=None, max_resource_buffer_size=None, max_post_data_size=None, report_direct_socket_traffic=None, enable_durable_messages=None)

Enables network tracking, network events will now be delivered to the client.

* **Parameters:**
  * **max_total_buffer_size** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* Buffer size in bytes to use when preserving network payloads (XHRs, etc).
  * **max_resource_buffer_size** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
  * **max_post_data_size** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Longest post body size (in bytes) that would be included in requestWillBeSent notification
  * **report_direct_socket_traffic** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether DirectSocket chunk send/receive events should be reported.
  * **enable_durable_messages** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Enable storing response bodies outside of renderer, so that these survive a cross-process navigation. Requires maxTotalBufferSize to be set. Currently defaults to false.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable_reporting_api(enable)

Enables tracking for the Reporting API, events generated by the Reporting API will now be delivered to the client.
Enabling triggers ‘reportingApiReportAdded’ for all existing reports.

**EXPERIMENTAL**

* **Parameters:**
  **enable** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to enable or disable events for the Reporting API
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_all_cookies()

Returns all browser cookies. Depending on the backend support, will return detailed cookie
information in the `cookies` field.
Deprecated. Use Storage.getCookies instead.

#### Deprecated
Deprecated since version 1.3.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Cookie`](#nodriver.cdp.network.Cookie)]]
* **Returns:**
  Array of cookie objects.

#### Deprecated
Deprecated since version 1.3.

### get_certificate(origin)

Returns the DER-encoded certificate.

**EXPERIMENTAL**

* **Parameters:**
  **origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Origin to get certificate for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**

### get_cookies(urls=None)

Returns all browser cookies for the current URL. Depending on the backend support, will return
detailed cookie information in the `cookies` field.

* **Parameters:**
  **urls** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]) – *(Optional)* The list of URLs for which applicable cookies will be fetched. If not specified, it’s assumed to be set to the list containing the URLs of the page and all of its subframes.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Cookie`](#nodriver.cdp.network.Cookie)]]
* **Returns:**
  Array of cookie objects.

### get_ip_protection_proxy_status()

Returns enum representing if IP Proxy of requests is available
or reason it is not active.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`IpProxyStatus`](#nodriver.cdp.network.IpProxyStatus)]
* **Returns:**
  Whether IP proxy is available

### get_request_post_data(request_id)

Returns post data sent with the request. Returns an error when no data was sent with the request.

* **Parameters:**
  **request_id** ([`RequestId`](#nodriver.cdp.network.RequestId)) – Identifier of the network request to get content for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**
  Request body string, omitting files from multipart requests

### get_response_body(request_id)

Returns content served for the given request.

* **Parameters:**
  **request_id** ([`RequestId`](#nodriver.cdp.network.RequestId)) – Identifier of the network request to get content for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`bool`](https://docs.python.org/3/library/functions.html#bool)]]
* **Returns:**
  A tuple with the following items:
  1. **body** - Response body.
  2. **base64Encoded** - True, if content was sent as base64.

### get_response_body_for_interception(interception_id)

Returns content served for the given currently intercepted request.

**EXPERIMENTAL**

* **Parameters:**
  **interception_id** ([`InterceptionId`](#nodriver.cdp.network.InterceptionId)) – Identifier for the intercepted request to get body for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`bool`](https://docs.python.org/3/library/functions.html#bool)]]
* **Returns:**
  A tuple with the following items:
  1. **body** - Response body.
  2. **base64Encoded** - True, if content was sent as base64.

### get_security_isolation_status(frame_id=None)

Returns information about the COEP/COOP isolation status.

**EXPERIMENTAL**

* **Parameters:**
  **frame_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]) – *(Optional)* If no frameId is provided, the status of the target is provided.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SecurityIsolationStatus`](#nodriver.cdp.network.SecurityIsolationStatus)]
* **Returns:**

### load_network_resource(url, options, frame_id=None)

Fetches the resource and returns the content.

**EXPERIMENTAL**

* **Parameters:**
  * **frame_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]) – *(Optional)* Frame id to get the resource for. Mandatory for frame targets, and should be omitted for worker targets.
  * **url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – URL of the resource to get content for.
  * **options** ([`LoadNetworkResourceOptions`](#nodriver.cdp.network.LoadNetworkResourceOptions)) – Options for the request.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`LoadNetworkResourcePageResult`](#nodriver.cdp.network.LoadNetworkResourcePageResult)]
* **Returns:**

### replay_xhr(request_id)

This method sends a new XMLHttpRequest which is identical to the original one. The following
parameters should be identical: method, url, async, request body, extra headers, withCredentials
attribute, user, password.

**EXPERIMENTAL**

* **Parameters:**
  **request_id** ([`RequestId`](#nodriver.cdp.network.RequestId)) – Identifier of XHR to replay.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### search_in_response_body(request_id, query, case_sensitive=None, is_regex=None)

Searches for given string in response content.

**EXPERIMENTAL**

* **Parameters:**
  * **request_id** ([`RequestId`](#nodriver.cdp.network.RequestId)) – Identifier of the network response to search.
  * **query** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – String to search for.
  * **case_sensitive** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, search is case sensitive.
  * **is_regex** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, treats string parameter as regex.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SearchMatch`](debugger.md#nodriver.cdp.debugger.SearchMatch)]]
* **Returns:**
  List of search matches.

### set_accepted_encodings(encodings)

Sets a list of content encodings that will be accepted. Empty list means no encoding is accepted.

**EXPERIMENTAL**

* **Parameters:**
  **encodings** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ContentEncoding`](#nodriver.cdp.network.ContentEncoding)]) – List of accepted content encodings.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_attach_debug_stack(enabled)

Specifies whether to attach a page script stack id in requests

**EXPERIMENTAL**

* **Parameters:**
  **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to attach a page script stack for debugging purpose.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_blocked_ur_ls(urls)

Blocks URLs from loading.

**EXPERIMENTAL**

* **Parameters:**
  **urls** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – URL patterns to block. Wildcards (‘\*’) are allowed.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_bypass_service_worker(bypass)

Toggles ignoring of service worker for each request.

* **Parameters:**
  **bypass** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Bypass service worker and load from network.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_cache_disabled(cache_disabled)

Toggles ignoring cache for each request. If `true`, cache will not be used.

* **Parameters:**
  **cache_disabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Cache disabled state.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_cookie(name, value, url=None, domain=None, path=None, secure=None, http_only=None, same_site=None, expires=None, priority=None, same_party=None, source_scheme=None, source_port=None, partition_key=None)

Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.

* **Parameters:**
  * **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Cookie name.
  * **value** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Cookie value.
  * **url** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* The request-URI to associate with the setting of the cookie. This value can affect the default domain, path, source port, and source scheme values of the created cookie.
  * **domain** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Cookie domain.
  * **path** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Cookie path.
  * **secure** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* True if cookie is secure.
  * **http_only** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* True if cookie is http-only.
  * **same_site** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookieSameSite`](#nodriver.cdp.network.CookieSameSite)]) – *(Optional)* Cookie SameSite type.
  * **expires** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)]) – *(Optional)* Cookie expiration date, session cookie if not set
  * **priority** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookiePriority`](#nodriver.cdp.network.CookiePriority)]) – **(EXPERIMENTAL)** *(Optional)* Cookie Priority type.
  * **same_party** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* True if cookie is SameParty.
  * **source_scheme** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookieSourceScheme`](#nodriver.cdp.network.CookieSourceScheme)]) – **(EXPERIMENTAL)** *(Optional)* Cookie source scheme type.
  * **source_port** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port. An unspecified port value allows protocol clients to emulate legacy cookie scope for the port. This is a temporary ability and it will be removed in the future.
  * **partition_key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookiePartitionKey`](#nodriver.cdp.network.CookiePartitionKey)]) – **(EXPERIMENTAL)** *(Optional)* Cookie partition key. If not set, the cookie will be set as not partitioned.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`bool`](https://docs.python.org/3/library/functions.html#bool)]
* **Returns:**
  Always set to true. If an error occurs, the response indicates protocol error.

### set_cookie_controls(enable_third_party_cookie_restriction, disable_third_party_cookie_metadata, disable_third_party_cookie_heuristics)

Sets Controls for third-party cookie access
Page reload is required before the new cookie behavior will be observed

**EXPERIMENTAL**

* **Parameters:**
  * **enable_third_party_cookie_restriction** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether 3pc restriction is enabled.
  * **disable_third_party_cookie_metadata** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether 3pc grace period exception should be enabled; false by default.
  * **disable_third_party_cookie_heuristics** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether 3pc heuristics exceptions should be enabled; false by default.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_cookies(cookies)

Sets given cookies.

* **Parameters:**
  **cookies** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CookieParam`](#nodriver.cdp.network.CookieParam)]) – Cookies to be set.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_extra_http_headers(headers)

Specifies whether to always send extra HTTP headers with the requests from this page.

* **Parameters:**
  **headers** ([`Headers`](#nodriver.cdp.network.Headers)) – Map with extra HTTP headers.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_ip_protection_proxy_bypass_enabled(enabled)

Sets bypass IP Protection Proxy boolean.

**EXPERIMENTAL**

* **Parameters:**
  **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether IP Proxy is being bypassed by devtools; false by default.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_request_interception(patterns)

Sets the requests to intercept that match the provided patterns and optionally resource types.
Deprecated, please use Fetch.enable instead.

#### Deprecated
Deprecated since version 1.3.

**EXPERIMENTAL**

* **Parameters:**
  **patterns** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`RequestPattern`](#nodriver.cdp.network.RequestPattern)]) – Requests matching any of these patterns will be forwarded and wait for the corresponding continueInterceptedRequest call.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### set_user_agent_override(user_agent, accept_language=None, platform=None, user_agent_metadata=None)

Allows overriding user agent with the given string.

* **Parameters:**
  * **user_agent** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – User agent to use.
  * **accept_language** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Browser language to emulate.
  * **platform** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* The platform navigator.platform should return.
  * **user_agent_metadata** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`UserAgentMetadata`](emulation.md#nodriver.cdp.emulation.UserAgentMetadata)]) – **(EXPERIMENTAL)** *(Optional)* To be sent in Sec-CH-UA-\* headers and returned in navigator.userAgentData
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### stream_resource_content(request_id)

Enables streaming of the response for the given requestId.
If enabled, the dataReceived event contains the data that was received during streaming.

**EXPERIMENTAL**

* **Parameters:**
  **request_id** ([`RequestId`](#nodriver.cdp.network.RequestId)) – Identifier of the request to stream.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**
  Data that has been buffered until streaming is enabled. (Encoded as a base64 string when passed over JSON)

### take_response_body_for_interception_as_stream(interception_id)

Returns a handle to the stream representing the response body. Note that after this command,
the intercepted request can’t be continued as is – you either need to cancel it or to provide
the response body. The stream only supports sequential read, IO.read will fail if the position
is specified.

**EXPERIMENTAL**

* **Parameters:**
  **interception_id** ([`InterceptionId`](#nodriver.cdp.network.InterceptionId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`StreamHandle`](io.md#nodriver.cdp.io.StreamHandle)]
* **Returns:**

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* DataReceived(request_id, timestamp, data_length, encoded_data_length, data)

Fired when data chunk was received over the network.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### data_length*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Data chunk length.

#### encoded_data_length*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Actual bytes received (might be less than dataLength for compressed encodings).

#### data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Data that was received. (Encoded as a base64 string when passed over JSON)

### *class* EventSourceMessageReceived(request_id, timestamp, event_name, event_id, data)

Fired when EventSource message is received.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### event_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Message type.

#### event_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Message identifier.

#### data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Message content.

### *class* LoadingFailed(request_id, timestamp, type_, error_text, canceled, blocked_reason, cors_error_status)

Fired when HTTP request has failed to load.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### type_*: [`ResourceType`](#nodriver.cdp.network.ResourceType)*

Resource type.

#### error_text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

//cs.chromium.org/chromium/src/net/base/net_error_list.h

* **Type:**
  Error message. List of network errors
* **Type:**
  https

#### canceled*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

True if loading was canceled.

#### blocked_reason*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BlockedReason`](#nodriver.cdp.network.BlockedReason)]*

The reason why loading was blocked, if any.

#### cors_error_status*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CorsErrorStatus`](#nodriver.cdp.network.CorsErrorStatus)]*

The reason why loading was blocked by CORS, if any.

### *class* LoadingFinished(request_id, timestamp, encoded_data_length)

Fired when HTTP request has finished loading.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### encoded_data_length*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Total number of bytes received for this request.

### *class* RequestIntercepted(interception_id, request, frame_id, resource_type, is_navigation_request, is_download, redirect_url, auth_challenge, response_error_reason, response_status_code, response_headers, request_id)

**EXPERIMENTAL**

Details of an intercepted HTTP request, which must be either allowed, blocked, modified or
mocked.
Deprecated, use Fetch.requestPaused instead.

#### Deprecated
Deprecated since version 1.3.

#### interception_id*: [`InterceptionId`](#nodriver.cdp.network.InterceptionId)*

Each request the page makes will have a unique id, however if any redirects are encountered
while processing that fetch, they will be reported with the same id as the original fetch.
Likewise if HTTP authentication is needed then the same fetch id will be used.

#### request*: [`Request`](#nodriver.cdp.network.Request)*

#### frame_id*: [`FrameId`](page.md#nodriver.cdp.page.FrameId)*

The id of the frame that initiated the request.

#### resource_type*: [`ResourceType`](#nodriver.cdp.network.ResourceType)*

How the requested resource will be used.

#### is_navigation_request*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether this is a navigation request, which can abort the navigation completely.

#### is_download*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

Set if the request is a navigation that will result in a download.
Only present after response is received from the server (i.e. HeadersReceived stage).

#### redirect_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Redirect location, only sent if a redirect was intercepted.

#### auth_challenge*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AuthChallenge`](#nodriver.cdp.network.AuthChallenge)]*

Details of the Authorization Challenge encountered. If this is set then
continueInterceptedRequest must contain an authChallengeResponse.

#### response_error_reason*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ErrorReason`](#nodriver.cdp.network.ErrorReason)]*

Response error if intercepted at response stage or if redirect occurred while intercepting
request.

#### response_status_code*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

Response code if intercepted at response stage or if redirect occurred while intercepting
request or auth retry occurred.

#### response_headers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Headers`](#nodriver.cdp.network.Headers)]*

Response headers if intercepted at the response stage or if redirect occurred while
intercepting request or auth retry occurred.

#### request_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestId`](#nodriver.cdp.network.RequestId)]*

If the intercepted request had a corresponding requestWillBeSent event fired for it, then
this requestId will be the same as the requestId present in the requestWillBeSent event.

### *class* RequestServedFromCache(request_id)

Fired if request ended up loading from cache.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

### *class* RequestWillBeSent(request_id, loader_id, document_url, request, timestamp, wall_time, initiator, redirect_has_extra_info, redirect_response, type_, frame_id, has_user_gesture)

Fired when page is about to send HTTP request.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### loader_id*: [`LoaderId`](#nodriver.cdp.network.LoaderId)*

Loader identifier. Empty string if the request is fetched from worker.

#### document_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL of the document this request is loaded for.

#### request*: [`Request`](#nodriver.cdp.network.Request)*

Request data.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### wall_time*: [`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)*

Timestamp.

#### initiator*: [`Initiator`](#nodriver.cdp.network.Initiator)*

Request initiator.

#### redirect_has_extra_info*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

In the case that redirectResponse is populated, this flag indicates whether
requestWillBeSentExtraInfo and responseReceivedExtraInfo events will be or were emitted
for the request which was just redirected.

#### redirect_response*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Response`](#nodriver.cdp.network.Response)]*

Redirect response data.

#### type_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ResourceType`](#nodriver.cdp.network.ResourceType)]*

Type of this resource.

#### frame_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]*

Frame identifier.

#### has_user_gesture*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

Whether the request is initiated by a user gesture. Defaults to false.

### *class* ResourceChangedPriority(request_id, new_priority, timestamp)

**EXPERIMENTAL**

Fired when resource loading priority is changed

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### new_priority*: [`ResourcePriority`](#nodriver.cdp.network.ResourcePriority)*

New priority

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* SignedExchangeReceived(request_id, info)

**EXPERIMENTAL**

Fired when a signed exchange was received over the network

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### info*: [`SignedExchangeInfo`](#nodriver.cdp.network.SignedExchangeInfo)*

Information about the signed exchange response.

### *class* ResponseReceived(request_id, loader_id, timestamp, type_, response, has_extra_info, frame_id)

Fired when HTTP response is available.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### loader_id*: [`LoaderId`](#nodriver.cdp.network.LoaderId)*

Loader identifier. Empty string if the request is fetched from worker.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### type_*: [`ResourceType`](#nodriver.cdp.network.ResourceType)*

Resource type.

#### response*: [`Response`](#nodriver.cdp.network.Response)*

Response data.

#### has_extra_info*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Indicates whether requestWillBeSentExtraInfo and responseReceivedExtraInfo events will be
or were emitted for this request.

#### frame_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]*

Frame identifier.

### *class* WebSocketClosed(request_id, timestamp)

Fired when WebSocket is closed.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* WebSocketCreated(request_id, url, initiator)

Fired upon WebSocket creation.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

WebSocket request URL.

#### initiator*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Initiator`](#nodriver.cdp.network.Initiator)]*

Request initiator.

### *class* WebSocketFrameError(request_id, timestamp, error_message)

Fired when WebSocket message error occurs.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### error_message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

WebSocket error message.

### *class* WebSocketFrameReceived(request_id, timestamp, response)

Fired when WebSocket message is received.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### response*: [`WebSocketFrame`](#nodriver.cdp.network.WebSocketFrame)*

WebSocket response data.

### *class* WebSocketFrameSent(request_id, timestamp, response)

Fired when WebSocket message is sent.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### response*: [`WebSocketFrame`](#nodriver.cdp.network.WebSocketFrame)*

WebSocket response data.

### *class* WebSocketHandshakeResponseReceived(request_id, timestamp, response)

Fired when WebSocket handshake response becomes available.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### response*: [`WebSocketResponse`](#nodriver.cdp.network.WebSocketResponse)*

WebSocket response data.

### *class* WebSocketWillSendHandshakeRequest(request_id, timestamp, wall_time, request)

Fired when WebSocket is about to initiate handshake.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### wall_time*: [`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)*

UTC Timestamp.

#### request*: [`WebSocketRequest`](#nodriver.cdp.network.WebSocketRequest)*

WebSocket request data.

### *class* WebTransportCreated(transport_id, url, timestamp, initiator)

Fired upon WebTransport creation.

#### transport_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

WebTransport identifier.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

WebTransport request URL.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### initiator*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Initiator`](#nodriver.cdp.network.Initiator)]*

Request initiator.

### *class* WebTransportConnectionEstablished(transport_id, timestamp)

Fired when WebTransport handshake is finished.

#### transport_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

WebTransport identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* WebTransportClosed(transport_id, timestamp)

Fired when WebTransport is disposed.

#### transport_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

WebTransport identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* DirectTCPSocketCreated(identifier, remote_addr, remote_port, options, timestamp, initiator)

**EXPERIMENTAL**

Fired upon direct_socket.TCPSocket creation.

#### identifier*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### remote_addr*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### remote_port*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Unsigned int 16.

#### options*: [`DirectTCPSocketOptions`](#nodriver.cdp.network.DirectTCPSocketOptions)*

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

#### initiator*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Initiator`](#nodriver.cdp.network.Initiator)]*

### *class* DirectTCPSocketOpened(identifier, remote_addr, remote_port, timestamp, local_addr, local_port)

**EXPERIMENTAL**

Fired when direct_socket.TCPSocket connection is opened.

#### identifier*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### remote_addr*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### remote_port*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Expected to be unsigned integer.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

#### local_addr*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### local_port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

Expected to be unsigned integer.

### *class* DirectTCPSocketAborted(identifier, error_message, timestamp)

**EXPERIMENTAL**

Fired when direct_socket.TCPSocket is aborted.

#### identifier*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### error_message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

### *class* DirectTCPSocketClosed(identifier, timestamp)

**EXPERIMENTAL**

Fired when direct_socket.TCPSocket is closed.

#### identifier*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

### *class* DirectTCPSocketChunkSent(identifier, data, timestamp)

**EXPERIMENTAL**

Fired when data is sent to tcp direct socket stream.

#### identifier*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

### *class* DirectTCPSocketChunkReceived(identifier, data, timestamp)

**EXPERIMENTAL**

Fired when data is received from tcp direct socket stream.

#### identifier*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

### *class* DirectUDPSocketCreated(identifier, options, timestamp, initiator)

**EXPERIMENTAL**

Fired upon direct_socket.UDPSocket creation.

#### identifier*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### options*: [`DirectUDPSocketOptions`](#nodriver.cdp.network.DirectUDPSocketOptions)*

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

#### initiator*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Initiator`](#nodriver.cdp.network.Initiator)]*

### *class* DirectUDPSocketOpened(identifier, local_addr, local_port, timestamp, remote_addr, remote_port)

**EXPERIMENTAL**

Fired when direct_socket.UDPSocket connection is opened.

#### identifier*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### local_addr*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### local_port*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Expected to be unsigned integer.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

#### remote_addr*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### remote_port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

Expected to be unsigned integer.

### *class* DirectUDPSocketAborted(identifier, error_message, timestamp)

**EXPERIMENTAL**

Fired when direct_socket.UDPSocket is aborted.

#### identifier*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### error_message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

### *class* DirectUDPSocketClosed(identifier, timestamp)

**EXPERIMENTAL**

Fired when direct_socket.UDPSocket is closed.

#### identifier*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

### *class* DirectUDPSocketChunkSent(identifier, message, timestamp)

**EXPERIMENTAL**

Fired when message is sent to udp direct socket stream.

#### identifier*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### message*: [`DirectUDPMessage`](#nodriver.cdp.network.DirectUDPMessage)*

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

### *class* DirectUDPSocketChunkReceived(identifier, message, timestamp)

**EXPERIMENTAL**

Fired when message is received from udp direct socket stream.

#### identifier*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### message*: [`DirectUDPMessage`](#nodriver.cdp.network.DirectUDPMessage)*

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

### *class* RequestWillBeSentExtraInfo(request_id, associated_cookies, headers, connect_timing, client_security_state, site_has_cookie_in_other_partition)

**EXPERIMENTAL**

Fired when additional information about a requestWillBeSent event is available from the
network stack. Not every requestWillBeSent event will have an additional
requestWillBeSentExtraInfo fired for it, and there is no guarantee whether requestWillBeSent
or requestWillBeSentExtraInfo will be fired first for the same request.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier. Used to match this information to an existing requestWillBeSent event.

#### associated_cookies*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AssociatedCookie`](#nodriver.cdp.network.AssociatedCookie)]*

A list of cookies potentially associated to the requested URL. This includes both cookies sent with
the request and the ones not sent; the latter are distinguished by having blockedReasons field set.

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

Raw request headers as they will be sent over the wire.

#### connect_timing*: [`ConnectTiming`](#nodriver.cdp.network.ConnectTiming)*

Connection timing information for the request.

#### client_security_state*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ClientSecurityState`](#nodriver.cdp.network.ClientSecurityState)]*

The client security state set for the request.

#### site_has_cookie_in_other_partition*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

Whether the site has partitioned cookies stored in a partition different than the current one.

### *class* ResponseReceivedExtraInfo(request_id, blocked_cookies, headers, resource_ip_address_space, status_code, headers_text, cookie_partition_key, cookie_partition_key_opaque, exempted_cookies)

**EXPERIMENTAL**

Fired when additional information about a responseReceived event is available from the network
stack. Not every responseReceived event will have an additional responseReceivedExtraInfo for
it, and responseReceivedExtraInfo may be fired before or after responseReceived.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier. Used to match this information to another responseReceived event.

#### blocked_cookies*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BlockedSetCookieWithReason`](#nodriver.cdp.network.BlockedSetCookieWithReason)]*

A list of cookies which were not stored from the response along with the corresponding
reasons for blocking. The cookies here may not be valid due to syntax errors, which
are represented by the invalid cookie line string instead of a proper cookie.

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

Raw response headers as they were received over the wire.
Duplicate headers in the response are represented as a single key with their values
concatentated using `\n` as the separator.
See also `headersText` that contains verbatim text for HTTP/1.\*.

#### resource_ip_address_space*: [`IPAddressSpace`](#nodriver.cdp.network.IPAddressSpace)*

The IP address space of the resource. The address space can only be determined once the transport
established the connection, so we can’t send it in `requestWillBeSentExtraInfo`.

#### status_code*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The status code of the response. This is useful in cases the request failed and no responseReceived
event is triggered, which is the case for, e.g., CORS errors. This is also the correct status code
for cached requests, where the status in responseReceived is a 200 and this will be 304.

#### headers_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Raw response header text as it was received over the wire. The raw text may not always be
available, such as in the case of HTTP/2 or QUIC.

#### cookie_partition_key*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookiePartitionKey`](#nodriver.cdp.network.CookiePartitionKey)]*

The cookie partition key that will be used to store partitioned cookies set in this response.
Only sent when partitioned cookies are enabled.

#### cookie_partition_key_opaque*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

True if partitioned cookies are enabled, but the partition key is not serializable to string.

#### exempted_cookies*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ExemptedSetCookieWithReason`](#nodriver.cdp.network.ExemptedSetCookieWithReason)]]*

A list of cookies which should have been blocked by 3PCD but are exempted and stored from
the response with the corresponding reason.

### *class* ResponseReceivedEarlyHints(request_id, headers)

**EXPERIMENTAL**

Fired when 103 Early Hints headers is received in addition to the common response.
Not every responseReceived event will have an responseReceivedEarlyHints fired.
Only one responseReceivedEarlyHints may be fired for eached responseReceived event.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier. Used to match this information to another responseReceived event.

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

Raw response headers as they were received over the wire.
Duplicate headers in the response are represented as a single key with their values
concatentated using `\n` as the separator.
See also `headersText` that contains verbatim text for HTTP/1.\*.

### *class* TrustTokenOperationDone(status, type_, request_id, top_level_origin, issuer_origin, issued_token_count)

**EXPERIMENTAL**

Fired exactly once for each Trust Token operation. Depending on
the type of the operation and whether the operation succeeded or
failed, the event is fired before the corresponding request was sent
or after the response was received.

#### status*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Detailed success or error status of the operation.
‘AlreadyExists’ also signifies a successful operation, as the result
of the operation already exists und thus, the operation was abort
preemptively (e.g. a cache hit).

#### type_*: [`TrustTokenOperationType`](#nodriver.cdp.network.TrustTokenOperationType)*

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### top_level_origin*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Top level origin. The context in which the operation was attempted.

#### issuer_origin*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Origin of the issuer in case of a “Issuance” or “Redemption” operation.

#### issued_token_count*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

The number of obtained Trust Tokens on a successful “Issuance” operation.

### *class* PolicyUpdated

**EXPERIMENTAL**

Fired once security policy has been updated.

### *class* SubresourceWebBundleMetadataReceived(request_id, urls)

**EXPERIMENTAL**

Fired once when parsing the .wbn file has succeeded.
The event contains the information about the web bundle contents.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier. Used to match this information to another event.

#### urls*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

A list of URLs of resources in the subresource Web Bundle.

### *class* SubresourceWebBundleMetadataError(request_id, error_message)

**EXPERIMENTAL**

Fired once when parsing the .wbn file has failed.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier. Used to match this information to another event.

#### error_message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Error message

### *class* SubresourceWebBundleInnerResponseParsed(inner_request_id, inner_request_url, bundle_request_id)

**EXPERIMENTAL**

Fired when handling requests for resources within a .wbn file.
Note: this will only be fired for resources that are requested by the webpage.

#### inner_request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier of the subresource request

#### inner_request_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL of the subresource resource.

#### bundle_request_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestId`](#nodriver.cdp.network.RequestId)]*

Bundle request identifier. Used to match this information to another event.
This made be absent in case when the instrumentation was enabled only
after webbundle was parsed.

### *class* SubresourceWebBundleInnerResponseError(inner_request_id, inner_request_url, error_message, bundle_request_id)

**EXPERIMENTAL**

Fired when request for resources within a .wbn file failed.

#### inner_request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier of the subresource request

#### inner_request_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL of the subresource resource.

#### error_message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Error message

#### bundle_request_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestId`](#nodriver.cdp.network.RequestId)]*

Bundle request identifier. Used to match this information to another event.
This made be absent in case when the instrumentation was enabled only
after webbundle was parsed.

### *class* ReportingApiReportAdded(report)

**EXPERIMENTAL**

Is sent whenever a new report is added.
And after ‘enableReportingApi’ for all existing reports.

#### report*: [`ReportingApiReport`](#nodriver.cdp.network.ReportingApiReport)*

### *class* ReportingApiReportUpdated(report)

**EXPERIMENTAL**

#### report*: [`ReportingApiReport`](#nodriver.cdp.network.ReportingApiReport)*

### *class* ReportingApiEndpointsChangedForOrigin(origin, endpoints)

**EXPERIMENTAL**

#### origin*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Origin of the document(s) which configured the endpoints.

#### endpoints*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ReportingApiEndpoint`](#nodriver.cdp.network.ReportingApiEndpoint)]*
