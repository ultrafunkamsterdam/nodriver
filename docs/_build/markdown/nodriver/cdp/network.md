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

#### CSP_VIOLATION_REPORT *= 'CSPViolationReport'*

#### DOCUMENT *= 'Document'*

#### EVENT_SOURCE *= 'EventSource'*

#### FETCH *= 'Fetch'*

#### FONT *= 'Font'*

#### IMAGE *= 'Image'*

#### MANIFEST *= 'Manifest'*

#### MEDIA *= 'Media'*

#### OTHER *= 'Other'*

#### PING *= 'Ping'*

#### PREFETCH *= 'Prefetch'*

#### PREFLIGHT *= 'Preflight'*

#### SCRIPT *= 'Script'*

#### SIGNED_EXCHANGE *= 'SignedExchange'*

#### STYLESHEET *= 'Stylesheet'*

#### TEXT_TRACK *= 'TextTrack'*

#### WEB_SOCKET *= 'WebSocket'*

#### XHR *= 'XHR'*

### *class* LoaderId

Unique loader identifier.

### *class* RequestId

Unique request identifier.

### *class* InterceptionId

Unique intercepted request identifier.

### *class* ErrorReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Network level fetch failure reason.

#### ABORTED *= 'Aborted'*

#### ACCESS_DENIED *= 'AccessDenied'*

#### ADDRESS_UNREACHABLE *= 'AddressUnreachable'*

#### BLOCKED_BY_CLIENT *= 'BlockedByClient'*

#### BLOCKED_BY_RESPONSE *= 'BlockedByResponse'*

#### CONNECTION_ABORTED *= 'ConnectionAborted'*

#### CONNECTION_CLOSED *= 'ConnectionClosed'*

#### CONNECTION_FAILED *= 'ConnectionFailed'*

#### CONNECTION_REFUSED *= 'ConnectionRefused'*

#### CONNECTION_RESET *= 'ConnectionReset'*

#### FAILED *= 'Failed'*

#### INTERNET_DISCONNECTED *= 'InternetDisconnected'*

#### NAME_NOT_RESOLVED *= 'NameNotResolved'*

#### TIMED_OUT *= 'TimedOut'*

### *class* TimeSinceEpoch(x=0, /)

UTC time in seconds, counted from January 1, 1970.

### *class* MonotonicTime(x=0, /)

Monotonically increasing time in seconds since an arbitrary point in the past.

### *class* Headers

Request / response headers as keys / values of JSON object.

### *class* ConnectionType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The underlying connection technology that the browser is supposedly using.

#### BLUETOOTH *= 'bluetooth'*

#### CELLULAR2G *= 'cellular2g'*

#### CELLULAR3G *= 'cellular3g'*

#### CELLULAR4G *= 'cellular4g'*

#### ETHERNET *= 'ethernet'*

#### NONE *= 'none'*

#### OTHER *= 'other'*

#### WIFI *= 'wifi'*

#### WIMAX *= 'wimax'*

### *class* CookieSameSite(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Represents the cookie’s ‘SameSite’ status:
[https://tools.ietf.org/html/draft-west-first-party-cookies](https://tools.ietf.org/html/draft-west-first-party-cookies)

#### LAX *= 'Lax'*

#### NONE *= 'None'*

#### STRICT *= 'Strict'*

### *class* CookiePriority(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Represents the cookie’s ‘Priority’ status:
[https://tools.ietf.org/html/draft-west-cookie-priority-00](https://tools.ietf.org/html/draft-west-cookie-priority-00)

#### HIGH *= 'High'*

#### LOW *= 'Low'*

#### MEDIUM *= 'Medium'*

### *class* CookieSourceScheme(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Represents the source scheme of the origin that originally set the cookie.
A value of “Unset” allows protocol clients to emulate legacy cookie scope for the scheme.
This is a temporary ability and it will be removed in the future.

#### NON_SECURE *= 'NonSecure'*

#### SECURE *= 'Secure'*

#### UNSET *= 'Unset'*

### *class* ResourceTiming(request_time, proxy_start, proxy_end, dns_start, dns_end, connect_start, connect_end, ssl_start, ssl_end, worker_start, worker_ready, worker_fetch_start, worker_respond_with_settled, send_start, send_end, push_start, push_end, receive_headers_start, receive_headers_end)

Timing information for the request.

* **Parameters:**
  * **request_time** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **proxy_start** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **proxy_end** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **dns_start** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **dns_end** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **connect_start** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **connect_end** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **ssl_start** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **ssl_end** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **worker_start** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **worker_ready** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **worker_fetch_start** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **worker_respond_with_settled** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **send_start** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **send_end** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **push_start** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **push_end** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **receive_headers_start** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **receive_headers_end** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 

#### connect_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Connected to the remote host.

#### connect_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started connecting to the remote host.

#### dns_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Finished DNS address resolve.

#### dns_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started DNS address resolve.

#### proxy_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Finished resolving proxy.

#### proxy_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started resolving proxy.

#### push_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Time the server finished pushing request.

#### push_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Time the server started pushing request.

#### receive_headers_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Finished receiving response headers.

#### receive_headers_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started receiving response headers.

#### request_time*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Timing’s requestTime is a baseline in seconds, while the other numbers are ticks in
milliseconds relatively to this requestTime.

#### send_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Finished sending request.

#### send_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started sending request.

#### ssl_end*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Finished SSL handshake.

#### ssl_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started SSL handshake.

#### worker_fetch_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started fetch event.

#### worker_ready*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Finished Starting ServiceWorker.

#### worker_respond_with_settled*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Settled fetch event respondWith promise.

#### worker_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Started running ServiceWorker.

### *class* ResourcePriority(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Loading priority of a resource request.

#### HIGH *= 'High'*

#### LOW *= 'Low'*

#### MEDIUM *= 'Medium'*

#### VERY_HIGH *= 'VeryHigh'*

#### VERY_LOW *= 'VeryLow'*

### *class* PostDataEntry(bytes_=None)

Post data entry for HTTP request

* **Parameters:**
  **bytes_** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### bytes_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* Request(url, method, headers, initial_priority, referrer_policy, url_fragment=None, post_data=None, has_post_data=None, post_data_entries=None, mixed_content_type=None, is_link_preload=None, trust_token_params=None, is_same_site=None)

HTTP request data.

* **Parameters:**
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **method** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **headers** ([*Headers*](#nodriver.cdp.network.Headers)) – 
  * **initial_priority** ([*ResourcePriority*](#nodriver.cdp.network.ResourcePriority)) – 
  * **referrer_policy** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **url_fragment** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **post_data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **has_post_data** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **post_data_entries** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*PostDataEntry*](#nodriver.cdp.network.PostDataEntry)*]* *|* *None*) – 
  * **mixed_content_type** ([*MixedContentType*](security.md#nodriver.cdp.security.MixedContentType) *|* *None*) – 
  * **is_link_preload** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **trust_token_params** ([*TrustTokenParams*](#nodriver.cdp.network.TrustTokenParams) *|* *None*) – 
  * **is_same_site** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 

#### has_post_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True when the request has POST data. Note that postData might still be omitted when this flag is true when the data is too long.

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

HTTP request headers.

#### initial_priority*: [`ResourcePriority`](#nodriver.cdp.network.ResourcePriority)*

Priority of the resource request at the time request is sent.

#### is_link_preload*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether is loaded via link preload.

#### is_same_site*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if this resource request is considered to be the ‘same site’ as the
request correspondinfg to the main frame.

#### method*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

HTTP request method.

#### mixed_content_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`MixedContentType`](security.md#nodriver.cdp.security.MixedContentType)]* *= None*

The mixed content type of the request.

#### post_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

HTTP POST request data.

#### post_data_entries*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PostDataEntry`](#nodriver.cdp.network.PostDataEntry)]]* *= None*

Request body elements. This will be converted from base64 to binary

#### referrer_policy*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

//www.w3.org/TR/referrer-policy/

* **Type:**
  The referrer policy of the request, as defined in https

#### trust_token_params*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TrustTokenParams`](#nodriver.cdp.network.TrustTokenParams)]* *= None*

Set for requests when the TrustToken API is used. Contains the parameters
passed by the developer (e.g. via “fetch”) as understood by the backend.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Request URL (without fragment).

#### url_fragment*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Fragment of the requested URL starting with hash, if present.

### *class* SignedCertificateTimestamp(status, origin, log_description, log_id, timestamp, hash_algorithm, signature_algorithm, signature_data)

Details of a signed certificate timestamp (SCT).

* **Parameters:**
  * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **origin** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **log_description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **log_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **timestamp** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **hash_algorithm** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **signature_algorithm** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **signature_data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### hash_algorithm*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Hash algorithm.

#### log_description*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Log name / description.

#### log_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Log ID.

#### origin*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Origin.

#### signature_algorithm*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signature algorithm.

#### signature_data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signature data.

#### status*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Validation status.

#### timestamp*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Issuance date. Unlike TimeSinceEpoch, this contains the number of
milliseconds since January 1, 1970, UTC, not the number of seconds.

### *class* SecurityDetails(protocol, key_exchange, cipher, certificate_id, subject_name, san_list, issuer, valid_from, valid_to, signed_certificate_timestamp_list, certificate_transparency_compliance, encrypted_client_hello, key_exchange_group=None, mac=None, server_signature_algorithm=None)

Security details about a request.

* **Parameters:**
  * **protocol** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **key_exchange** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **cipher** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **certificate_id** ([*CertificateId*](security.md#nodriver.cdp.security.CertificateId)) – 
  * **subject_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **san_list** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **issuer** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **valid_from** ([*TimeSinceEpoch*](#nodriver.cdp.network.TimeSinceEpoch)) – 
  * **valid_to** ([*TimeSinceEpoch*](#nodriver.cdp.network.TimeSinceEpoch)) – 
  * **signed_certificate_timestamp_list** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*SignedCertificateTimestamp*](#nodriver.cdp.network.SignedCertificateTimestamp)*]*) – 
  * **certificate_transparency_compliance** ([*CertificateTransparencyCompliance*](#nodriver.cdp.network.CertificateTransparencyCompliance)) – 
  * **encrypted_client_hello** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **key_exchange_group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **mac** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **server_signature_algorithm** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 

#### certificate_id*: [`CertificateId`](security.md#nodriver.cdp.security.CertificateId)*

Certificate ID value.

#### certificate_transparency_compliance*: [`CertificateTransparencyCompliance`](#nodriver.cdp.network.CertificateTransparencyCompliance)*

Whether the request complied with Certificate Transparency policy

#### cipher*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cipher name.

#### encrypted_client_hello*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether the connection used Encrypted ClientHello

#### issuer*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name of the issuing CA.

#### key_exchange*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Key Exchange used by the connection, or the empty string if not applicable.

#### key_exchange_group*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

(EC)DH group used by the connection, if applicable.

#### mac*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

TLS MAC. Note that AEAD ciphers do not have separate MACs.

#### protocol*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Protocol name (e.g. “TLS 1.2” or “QUIC”).

#### san_list*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Subject Alternative Name (SAN) DNS names and IP addresses.

#### server_signature_algorithm*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

The signature algorithm used by the server in the TLS server signature,
represented as a TLS SignatureScheme code point. Omitted if not
applicable or not known.

#### signed_certificate_timestamp_list*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SignedCertificateTimestamp`](#nodriver.cdp.network.SignedCertificateTimestamp)]*

List of signed certificate timestamps (SCTs).

#### subject_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Certificate subject name.

#### valid_from*: [`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)*

Certificate valid from date.

#### valid_to*: [`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)*

Certificate valid to (expiration) date

### *class* CertificateTransparencyCompliance(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Whether the request complied with Certificate Transparency policy.

#### COMPLIANT *= 'compliant'*

#### NOT_COMPLIANT *= 'not-compliant'*

#### UNKNOWN *= 'unknown'*

### *class* BlockedReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The reason why request was blocked.

#### COEP_FRAME_RESOURCE_NEEDS_COEP_HEADER *= 'coep-frame-resource-needs-coep-header'*

#### CONTENT_TYPE *= 'content-type'*

#### COOP_SANDBOXED_IFRAME_CANNOT_NAVIGATE_TO_COOP_PAGE *= 'coop-sandboxed-iframe-cannot-navigate-to-coop-page'*

#### CORP_NOT_SAME_ORIGIN *= 'corp-not-same-origin'*

#### CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP *= 'corp-not-same-origin-after-defaulted-to-same-origin-by-coep'*

#### CORP_NOT_SAME_SITE *= 'corp-not-same-site'*

#### CSP *= 'csp'*

#### INSPECTOR *= 'inspector'*

#### MIXED_CONTENT *= 'mixed-content'*

#### ORIGIN *= 'origin'*

#### OTHER *= 'other'*

#### SUBRESOURCE_FILTER *= 'subresource-filter'*

### *class* CorsError(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The reason why request was blocked.

#### ALLOW_ORIGIN_MISMATCH *= 'AllowOriginMismatch'*

#### CORS_DISABLED_SCHEME *= 'CorsDisabledScheme'*

#### DISALLOWED_BY_MODE *= 'DisallowedByMode'*

#### HEADER_DISALLOWED_BY_PREFLIGHT_RESPONSE *= 'HeaderDisallowedByPreflightResponse'*

#### INSECURE_PRIVATE_NETWORK *= 'InsecurePrivateNetwork'*

#### INVALID_ALLOW_CREDENTIALS *= 'InvalidAllowCredentials'*

#### INVALID_ALLOW_HEADERS_PREFLIGHT_RESPONSE *= 'InvalidAllowHeadersPreflightResponse'*

#### INVALID_ALLOW_METHODS_PREFLIGHT_RESPONSE *= 'InvalidAllowMethodsPreflightResponse'*

#### INVALID_ALLOW_ORIGIN_VALUE *= 'InvalidAllowOriginValue'*

#### INVALID_PRIVATE_NETWORK_ACCESS *= 'InvalidPrivateNetworkAccess'*

#### INVALID_RESPONSE *= 'InvalidResponse'*

#### METHOD_DISALLOWED_BY_PREFLIGHT_RESPONSE *= 'MethodDisallowedByPreflightResponse'*

#### MISSING_ALLOW_ORIGIN_HEADER *= 'MissingAllowOriginHeader'*

#### MULTIPLE_ALLOW_ORIGIN_VALUES *= 'MultipleAllowOriginValues'*

#### NO_CORS_REDIRECT_MODE_NOT_FOLLOW *= 'NoCorsRedirectModeNotFollow'*

#### PREFLIGHT_ALLOW_ORIGIN_MISMATCH *= 'PreflightAllowOriginMismatch'*

#### PREFLIGHT_DISALLOWED_REDIRECT *= 'PreflightDisallowedRedirect'*

#### PREFLIGHT_INVALID_ALLOW_CREDENTIALS *= 'PreflightInvalidAllowCredentials'*

#### PREFLIGHT_INVALID_ALLOW_EXTERNAL *= 'PreflightInvalidAllowExternal'*

#### PREFLIGHT_INVALID_ALLOW_ORIGIN_VALUE *= 'PreflightInvalidAllowOriginValue'*

#### PREFLIGHT_INVALID_ALLOW_PRIVATE_NETWORK *= 'PreflightInvalidAllowPrivateNetwork'*

#### PREFLIGHT_INVALID_STATUS *= 'PreflightInvalidStatus'*

#### PREFLIGHT_MISSING_ALLOW_EXTERNAL *= 'PreflightMissingAllowExternal'*

#### PREFLIGHT_MISSING_ALLOW_ORIGIN_HEADER *= 'PreflightMissingAllowOriginHeader'*

#### PREFLIGHT_MISSING_ALLOW_PRIVATE_NETWORK *= 'PreflightMissingAllowPrivateNetwork'*

#### PREFLIGHT_MISSING_PRIVATE_NETWORK_ACCESS_ID *= 'PreflightMissingPrivateNetworkAccessId'*

#### PREFLIGHT_MISSING_PRIVATE_NETWORK_ACCESS_NAME *= 'PreflightMissingPrivateNetworkAccessName'*

#### PREFLIGHT_MULTIPLE_ALLOW_ORIGIN_VALUES *= 'PreflightMultipleAllowOriginValues'*

#### PREFLIGHT_WILDCARD_ORIGIN_NOT_ALLOWED *= 'PreflightWildcardOriginNotAllowed'*

#### PRIVATE_NETWORK_ACCESS_PERMISSION_DENIED *= 'PrivateNetworkAccessPermissionDenied'*

#### PRIVATE_NETWORK_ACCESS_PERMISSION_UNAVAILABLE *= 'PrivateNetworkAccessPermissionUnavailable'*

#### REDIRECT_CONTAINS_CREDENTIALS *= 'RedirectContainsCredentials'*

#### UNEXPECTED_PRIVATE_NETWORK_ACCESS *= 'UnexpectedPrivateNetworkAccess'*

#### WILDCARD_ORIGIN_NOT_ALLOWED *= 'WildcardOriginNotAllowed'*

### *class* CorsErrorStatus(cors_error, failed_parameter)

* **Parameters:**
  * **cors_error** ([*CorsError*](#nodriver.cdp.network.CorsError)) – 
  * **failed_parameter** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### cors_error*: [`CorsError`](#nodriver.cdp.network.CorsError)*

#### failed_parameter*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* ServiceWorkerResponseSource(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Source of serviceworker response.

#### CACHE_STORAGE *= 'cache-storage'*

#### FALLBACK_CODE *= 'fallback-code'*

#### HTTP_CACHE *= 'http-cache'*

#### NETWORK *= 'network'*

### *class* TrustTokenParams(operation, refresh_policy, issuers=None)

Determines what type of Trust Token operation is executed and
depending on the type, some additional parameters. The values
are specified in third_party/blink/renderer/core/fetch/trust_token.idl.

* **Parameters:**
  * **operation** ([*TrustTokenOperationType*](#nodriver.cdp.network.TrustTokenOperationType)) – 
  * **refresh_policy** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **issuers** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]* *|* *None*) – 

#### issuers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

Origins of issuers from whom to request tokens or redemption
records.

#### operation*: [`TrustTokenOperationType`](#nodriver.cdp.network.TrustTokenOperationType)*

#### refresh_policy*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Only set for “token-redemption” operation and determine whether
to request a fresh SRR or use a still valid cached SRR.

### *class* TrustTokenOperationType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### ISSUANCE *= 'Issuance'*

#### REDEMPTION *= 'Redemption'*

#### SIGNING *= 'Signing'*

### *class* AlternateProtocolUsage(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The reason why Chrome uses a specific transport protocol for HTTP semantics.

#### ALTERNATIVE_JOB_WON_RACE *= 'alternativeJobWonRace'*

#### ALTERNATIVE_JOB_WON_WITHOUT_RACE *= 'alternativeJobWonWithoutRace'*

#### BROKEN *= 'broken'*

#### DNS_ALPN_H3_JOB_WON_RACE *= 'dnsAlpnH3JobWonRace'*

#### DNS_ALPN_H3_JOB_WON_WITHOUT_RACE *= 'dnsAlpnH3JobWonWithoutRace'*

#### MAIN_JOB_WON_RACE *= 'mainJobWonRace'*

#### MAPPING_MISSING *= 'mappingMissing'*

#### UNSPECIFIED_REASON *= 'unspecifiedReason'*

### *class* ServiceWorkerRouterInfo(rule_id_matched)

* **Parameters:**
  **rule_id_matched** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 

#### rule_id_matched*: [`int`](https://docs.python.org/3/library/functions.html#int)*

### *class* Response(url, status, status_text, headers, mime_type, charset, connection_reused, connection_id, encoded_data_length, security_state, headers_text=None, request_headers=None, request_headers_text=None, remote_ip_address=None, remote_port=None, from_disk_cache=None, from_service_worker=None, from_prefetch_cache=None, service_worker_router_info=None, timing=None, service_worker_response_source=None, response_time=None, cache_storage_cache_name=None, protocol=None, alternate_protocol_usage=None, security_details=None)

HTTP response data.

* **Parameters:**
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **status** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **status_text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **headers** ([*Headers*](#nodriver.cdp.network.Headers)) – 
  * **mime_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **charset** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **connection_reused** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **connection_id** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **encoded_data_length** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **security_state** ([*SecurityState*](security.md#nodriver.cdp.security.SecurityState)) – 
  * **headers_text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **request_headers** ([*Headers*](#nodriver.cdp.network.Headers) *|* *None*) – 
  * **request_headers_text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **remote_ip_address** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **remote_port** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **from_disk_cache** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **from_service_worker** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **from_prefetch_cache** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **service_worker_router_info** ([*ServiceWorkerRouterInfo*](#nodriver.cdp.network.ServiceWorkerRouterInfo) *|* *None*) – 
  * **timing** ([*ResourceTiming*](#nodriver.cdp.network.ResourceTiming) *|* *None*) – 
  * **service_worker_response_source** ([*ServiceWorkerResponseSource*](#nodriver.cdp.network.ServiceWorkerResponseSource) *|* *None*) – 
  * **response_time** ([*TimeSinceEpoch*](#nodriver.cdp.network.TimeSinceEpoch) *|* *None*) – 
  * **cache_storage_cache_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **protocol** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **alternate_protocol_usage** ([*AlternateProtocolUsage*](#nodriver.cdp.network.AlternateProtocolUsage) *|* *None*) – 
  * **security_details** ([*SecurityDetails*](#nodriver.cdp.network.SecurityDetails) *|* *None*) – 

#### alternate_protocol_usage*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AlternateProtocolUsage`](#nodriver.cdp.network.AlternateProtocolUsage)]* *= None*

The reason why Chrome uses a specific transport protocol for HTTP semantics.

#### cache_storage_cache_name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Cache Storage Cache Name.

#### charset*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Resource charset as determined by the browser (if applicable).

#### connection_id*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Physical connection id that was actually used for this request.

#### connection_reused*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Specifies whether physical connection was actually reused for this request.

#### encoded_data_length*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Total number of bytes received for this request so far.

#### from_disk_cache*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Specifies that the request was served from the disk cache.

#### from_prefetch_cache*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Specifies that the request was served from the prefetch cache.

#### from_service_worker*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Specifies that the request was served from the ServiceWorker.

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

HTTP response headers.

#### headers_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

HTTP response headers text. This has been replaced by the headers in Network.responseReceivedExtraInfo.

#### mime_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Resource mimeType as determined by the browser.

#### protocol*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Protocol used to fetch this request.

#### remote_ip_address*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Remote IP address.

#### remote_port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Remote port.

#### request_headers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Headers`](#nodriver.cdp.network.Headers)]* *= None*

Refined HTTP request headers that were actually transmitted over the network.

#### request_headers_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

HTTP request headers text. This has been replaced by the headers in Network.requestWillBeSentExtraInfo.

#### response_time*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)]* *= None*

The time at which the returned response was generated.

#### security_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SecurityDetails`](#nodriver.cdp.network.SecurityDetails)]* *= None*

Security details for the request.

#### security_state*: [`SecurityState`](security.md#nodriver.cdp.security.SecurityState)*

Security state of the request resource.

#### service_worker_response_source*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ServiceWorkerResponseSource`](#nodriver.cdp.network.ServiceWorkerResponseSource)]* *= None*

Response source of response from ServiceWorker.

#### service_worker_router_info*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ServiceWorkerRouterInfo`](#nodriver.cdp.network.ServiceWorkerRouterInfo)]* *= None*

Infomation about how Service Worker Static Router was used.

#### status*: [`int`](https://docs.python.org/3/library/functions.html#int)*

HTTP response status code.

#### status_text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

HTTP response status text.

#### timing*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ResourceTiming`](#nodriver.cdp.network.ResourceTiming)]* *= None*

Timing information for the given request.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Response URL. This URL can be different from CachedResource.url in case of redirect.

### *class* WebSocketRequest(headers)

WebSocket request data.

* **Parameters:**
  **headers** ([*Headers*](#nodriver.cdp.network.Headers)) – 

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

HTTP request headers.

### *class* WebSocketResponse(status, status_text, headers, headers_text=None, request_headers=None, request_headers_text=None)

WebSocket response data.

* **Parameters:**
  * **status** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **status_text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **headers** ([*Headers*](#nodriver.cdp.network.Headers)) – 
  * **headers_text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **request_headers** ([*Headers*](#nodriver.cdp.network.Headers) *|* *None*) – 
  * **request_headers_text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

HTTP response headers.

#### headers_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

HTTP response headers text.

#### request_headers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Headers`](#nodriver.cdp.network.Headers)]* *= None*

HTTP request headers.

#### request_headers_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

HTTP request headers text.

#### status*: [`int`](https://docs.python.org/3/library/functions.html#int)*

HTTP response status code.

#### status_text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

HTTP response status text.

### *class* WebSocketFrame(opcode, mask, payload_data)

WebSocket message data. This represents an entire WebSocket message, not just a fragmented frame as the name suggests.

* **Parameters:**
  * **opcode** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **mask** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **payload_data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### mask*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

WebSocket message mask.

#### opcode*: [`float`](https://docs.python.org/3/library/functions.html#float)*

WebSocket message opcode.

#### payload_data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

WebSocket message payload data.
If the opcode is 1, this is a text message and payloadData is a UTF-8 string.
If the opcode isn’t 1, then payloadData is a base64 encoded string representing binary data.

### *class* CachedResource(url, type_, body_size, response=None)

Information about the cached resource.

* **Parameters:**
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **type_** ([*ResourceType*](#nodriver.cdp.network.ResourceType)) – 
  * **body_size** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 
  * **response** ([*Response*](#nodriver.cdp.network.Response) *|* *None*) – 

#### body_size*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Cached response body size.

#### response*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Response`](#nodriver.cdp.network.Response)]* *= None*

Cached response data.

#### type_*: [`ResourceType`](#nodriver.cdp.network.ResourceType)*

Type of this resource.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Resource URL. This is the url of the original network request.

### *class* Initiator(type_, stack=None, url=None, line_number=None, column_number=None, request_id=None)

Information about the request initiator.

* **Parameters:**
  * **type_** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **stack** ([*StackTrace*](runtime.md#nodriver.cdp.runtime.StackTrace) *|* *None*) – 
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **line_number** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **column_number** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId) *|* *None*) – 

#### column_number*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Initiator column number, set for Parser type or for Script type (when script is importing
module) (0-based).

#### line_number*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Initiator line number, set for Parser type or for Script type (when script is importing
module) (0-based).

#### request_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestId`](#nodriver.cdp.network.RequestId)]* *= None*

Set if another request triggered this request (e.g. preflight).

#### stack*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTrace`](runtime.md#nodriver.cdp.runtime.StackTrace)]* *= None*

Initiator JavaScript stack trace, set for Script only.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Type of this initiator.

#### url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Initiator URL, set for Parser type or for Script type (when script is importing module) or for SignedExchange type.

### *class* Cookie(name, value, domain, path, size, http_only, secure, session, priority, same_party, source_scheme, source_port, expires=None, same_site=None, partition_key=None, partition_key_opaque=None)

Cookie object

* **Parameters:**
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **domain** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **size** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **http_only** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **secure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **session** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **priority** ([*CookiePriority*](#nodriver.cdp.network.CookiePriority)) – 
  * **same_party** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **source_scheme** ([*CookieSourceScheme*](#nodriver.cdp.network.CookieSourceScheme)) – 
  * **source_port** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **expires** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **same_site** ([*CookieSameSite*](#nodriver.cdp.network.CookieSameSite) *|* *None*) – 
  * **partition_key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **partition_key_opaque** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 

#### domain*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cookie domain.

#### expires*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Cookie expiration date as the number of seconds since the UNIX epoch.

#### http_only*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if cookie is http-only.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cookie name.

#### partition_key*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Cookie partition key. The site of the top-level URL the browser was visiting at the start
of the request to the endpoint that set the cookie.

#### partition_key_opaque*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if cookie partition key is opaque.

#### path*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cookie path.

#### priority*: [`CookiePriority`](#nodriver.cdp.network.CookiePriority)*

Cookie Priority

#### same_party*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if cookie is SameParty.

#### same_site*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookieSameSite`](#nodriver.cdp.network.CookieSameSite)]* *= None*

Cookie SameSite type.

#### secure*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if cookie is secure.

#### session*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True in case of session cookie.

#### size*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Cookie size.

#### source_port*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port.
An unspecified port value allows protocol clients to emulate legacy cookie scope for the port.
This is a temporary ability and it will be removed in the future.

#### source_scheme*: [`CookieSourceScheme`](#nodriver.cdp.network.CookieSourceScheme)*

Cookie source scheme type.

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cookie value.

### *class* SetCookieBlockedReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Types of reasons why a cookie may not be stored from a response.

#### DISALLOWED_CHARACTER *= 'DisallowedCharacter'*

#### INVALID_DOMAIN *= 'InvalidDomain'*

#### INVALID_PREFIX *= 'InvalidPrefix'*

#### NAME_VALUE_PAIR_EXCEEDS_MAX_SIZE *= 'NameValuePairExceedsMaxSize'*

#### NO_COOKIE_CONTENT *= 'NoCookieContent'*

#### OVERWRITE_SECURE *= 'OverwriteSecure'*

#### SAME_PARTY_CONFLICTS_WITH_OTHER_ATTRIBUTES *= 'SamePartyConflictsWithOtherAttributes'*

#### SAME_PARTY_FROM_CROSS_PARTY_CONTEXT *= 'SamePartyFromCrossPartyContext'*

#### SAME_SITE_LAX *= 'SameSiteLax'*

#### SAME_SITE_NONE_INSECURE *= 'SameSiteNoneInsecure'*

#### SAME_SITE_STRICT *= 'SameSiteStrict'*

#### SAME_SITE_UNSPECIFIED_TREATED_AS_LAX *= 'SameSiteUnspecifiedTreatedAsLax'*

#### SCHEMEFUL_SAME_SITE_LAX *= 'SchemefulSameSiteLax'*

#### SCHEMEFUL_SAME_SITE_STRICT *= 'SchemefulSameSiteStrict'*

#### SCHEMEFUL_SAME_SITE_UNSPECIFIED_TREATED_AS_LAX *= 'SchemefulSameSiteUnspecifiedTreatedAsLax'*

#### SCHEME_NOT_SUPPORTED *= 'SchemeNotSupported'*

#### SECURE_ONLY *= 'SecureOnly'*

#### SYNTAX_ERROR *= 'SyntaxError'*

#### THIRD_PARTY_BLOCKED_IN_FIRST_PARTY_SET *= 'ThirdPartyBlockedInFirstPartySet'*

#### THIRD_PARTY_PHASEOUT *= 'ThirdPartyPhaseout'*

#### UNKNOWN_ERROR *= 'UnknownError'*

#### USER_PREFERENCES *= 'UserPreferences'*

### *class* CookieBlockedReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Types of reasons why a cookie may not be sent with a request.

#### DOMAIN_MISMATCH *= 'DomainMismatch'*

#### NAME_VALUE_PAIR_EXCEEDS_MAX_SIZE *= 'NameValuePairExceedsMaxSize'*

#### NOT_ON_PATH *= 'NotOnPath'*

#### SAME_PARTY_FROM_CROSS_PARTY_CONTEXT *= 'SamePartyFromCrossPartyContext'*

#### SAME_SITE_LAX *= 'SameSiteLax'*

#### SAME_SITE_NONE_INSECURE *= 'SameSiteNoneInsecure'*

#### SAME_SITE_STRICT *= 'SameSiteStrict'*

#### SAME_SITE_UNSPECIFIED_TREATED_AS_LAX *= 'SameSiteUnspecifiedTreatedAsLax'*

#### SCHEMEFUL_SAME_SITE_LAX *= 'SchemefulSameSiteLax'*

#### SCHEMEFUL_SAME_SITE_STRICT *= 'SchemefulSameSiteStrict'*

#### SCHEMEFUL_SAME_SITE_UNSPECIFIED_TREATED_AS_LAX *= 'SchemefulSameSiteUnspecifiedTreatedAsLax'*

#### SECURE_ONLY *= 'SecureOnly'*

#### THIRD_PARTY_BLOCKED_IN_FIRST_PARTY_SET *= 'ThirdPartyBlockedInFirstPartySet'*

#### THIRD_PARTY_PHASEOUT *= 'ThirdPartyPhaseout'*

#### UNKNOWN_ERROR *= 'UnknownError'*

#### USER_PREFERENCES *= 'UserPreferences'*

### *class* BlockedSetCookieWithReason(blocked_reasons, cookie_line, cookie=None)

A cookie which was not stored from a response with the corresponding reason.

* **Parameters:**
  * **blocked_reasons** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*SetCookieBlockedReason*](#nodriver.cdp.network.SetCookieBlockedReason)*]*) – 
  * **cookie_line** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **cookie** ([*Cookie*](#nodriver.cdp.network.Cookie) *|* *None*) – 

#### blocked_reasons*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SetCookieBlockedReason`](#nodriver.cdp.network.SetCookieBlockedReason)]*

The reason(s) this cookie was blocked.

#### cookie*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Cookie`](#nodriver.cdp.network.Cookie)]* *= None*

The cookie object which represents the cookie which was not stored. It is optional because
sometimes complete cookie information is not available, such as in the case of parsing
errors.

#### cookie_line*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The string representing this individual cookie as it would appear in the header.
This is not the entire “cookie” or “set-cookie” header which could have multiple cookies.

### *class* BlockedCookieWithReason(blocked_reasons, cookie)

A cookie with was not sent with a request with the corresponding reason.

* **Parameters:**
  * **blocked_reasons** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*CookieBlockedReason*](#nodriver.cdp.network.CookieBlockedReason)*]*) – 
  * **cookie** ([*Cookie*](#nodriver.cdp.network.Cookie)) – 

#### blocked_reasons*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CookieBlockedReason`](#nodriver.cdp.network.CookieBlockedReason)]*

The reason(s) the cookie was blocked.

#### cookie*: [`Cookie`](#nodriver.cdp.network.Cookie)*

The cookie object representing the cookie which was not sent.

### *class* CookieParam(name, value, url=None, domain=None, path=None, secure=None, http_only=None, same_site=None, expires=None, priority=None, same_party=None, source_scheme=None, source_port=None, partition_key=None)

Cookie parameter object

* **Parameters:**
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **domain** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **secure** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **http_only** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **same_site** ([*CookieSameSite*](#nodriver.cdp.network.CookieSameSite) *|* *None*) – 
  * **expires** ([*TimeSinceEpoch*](#nodriver.cdp.network.TimeSinceEpoch) *|* *None*) – 
  * **priority** ([*CookiePriority*](#nodriver.cdp.network.CookiePriority) *|* *None*) – 
  * **same_party** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **source_scheme** ([*CookieSourceScheme*](#nodriver.cdp.network.CookieSourceScheme) *|* *None*) – 
  * **source_port** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **partition_key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### domain*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Cookie domain.

#### expires*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)]* *= None*

Cookie expiration date, session cookie if not set

#### http_only*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if cookie is http-only.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cookie name.

#### partition_key*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Cookie partition key. The site of the top-level URL the browser was visiting at the start
of the request to the endpoint that set the cookie.
If not set, the cookie will be set as not partitioned.

#### path*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Cookie path.

#### priority*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookiePriority`](#nodriver.cdp.network.CookiePriority)]* *= None*

Cookie Priority.

#### same_party*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if cookie is SameParty.

#### same_site*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookieSameSite`](#nodriver.cdp.network.CookieSameSite)]* *= None*

Cookie SameSite type.

#### secure*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

True if cookie is secure.

#### source_port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port.
An unspecified port value allows protocol clients to emulate legacy cookie scope for the port.
This is a temporary ability and it will be removed in the future.

#### source_scheme*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CookieSourceScheme`](#nodriver.cdp.network.CookieSourceScheme)]* *= None*

Cookie source scheme type.

#### url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The request-URI to associate with the setting of the cookie. This value can affect the
default domain, path, source port, and source scheme values of the created cookie.

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cookie value.

### *class* AuthChallenge(origin, scheme, realm, source=None)

Authorization challenge for HTTP status code 401 or 407.

* **Parameters:**
  * **origin** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **scheme** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **realm** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### origin*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Origin of the challenger.

#### realm*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The realm of the challenge. May be empty.

#### scheme*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The authentication scheme used, such as basic or digest

#### source*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Source of the authentication challenge.

### *class* AuthChallengeResponse(response, username=None, password=None)

Response to an AuthChallenge.

* **Parameters:**
  * **response** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **username** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **password** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### password*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The password to provide, possibly empty. Should only be set if response is
ProvideCredentials.

#### response*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The decision on what to do in response to the authorization challenge.  Default means
deferring to the default behavior of the net stack, which will likely either the Cancel
authentication or display a popup dialog box.

#### username*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The username to provide, possibly empty. Should only be set if response is
ProvideCredentials.

### *class* InterceptionStage(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Stages of the interception to begin intercepting. Request will intercept before the request is
sent. Response will intercept after the response is received.

#### HEADERS_RECEIVED *= 'HeadersReceived'*

#### REQUEST *= 'Request'*

### *class* RequestPattern(url_pattern=None, resource_type=None, interception_stage=None)

Request pattern for interception.

* **Parameters:**
  * **url_pattern** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **resource_type** ([*ResourceType*](#nodriver.cdp.network.ResourceType) *|* *None*) – 
  * **interception_stage** ([*InterceptionStage*](#nodriver.cdp.network.InterceptionStage) *|* *None*) – 

#### interception_stage*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`InterceptionStage`](#nodriver.cdp.network.InterceptionStage)]* *= None*

Stage at which to begin intercepting requests. Default is Request.

#### resource_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ResourceType`](#nodriver.cdp.network.ResourceType)]* *= None*

If set, only requests for matching resource types will be intercepted.

#### url_pattern*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Wildcards (`'*'` -> zero or more, `'?'` -> exactly one) are allowed. Escape character is
backslash. Omitting is equivalent to `"*"`.

### *class* SignedExchangeSignature(label, signature, integrity, validity_url, date, expires, cert_url=None, cert_sha256=None, certificates=None)

Information about a signed exchange signature.
[https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1](https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1)

* **Parameters:**
  * **label** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **signature** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **integrity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **validity_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **date** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **expires** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **cert_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **cert_sha256** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **certificates** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]* *|* *None*) – 

#### cert_sha256*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The hex string of signed exchange signature cert sha256.

#### cert_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Signed exchange signature cert Url.

#### certificates*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

The encoded certificates.

#### date*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Signed exchange signature date.

#### expires*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Signed exchange signature expires.

#### integrity*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signed exchange signature integrity.

#### label*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signed exchange signature label.

#### signature*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The hex string of signed exchange signature.

#### validity_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signed exchange signature validity Url.

### *class* SignedExchangeHeader(request_url, response_code, response_headers, signatures, header_integrity)

Information about a signed exchange header.
[https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation](https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation)

* **Parameters:**
  * **request_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **response_code** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **response_headers** ([*Headers*](#nodriver.cdp.network.Headers)) – 
  * **signatures** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*SignedExchangeSignature*](#nodriver.cdp.network.SignedExchangeSignature)*]*) – 
  * **header_integrity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### header_integrity*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signed exchange header integrity hash in the form of `sha256-<base64-hash-value>`.

#### request_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Signed exchange request URL.

#### response_code*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Signed exchange response code.

#### response_headers*: [`Headers`](#nodriver.cdp.network.Headers)*

Signed exchange response headers.

#### signatures*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SignedExchangeSignature`](#nodriver.cdp.network.SignedExchangeSignature)]*

Signed exchange response signature.

### *class* SignedExchangeErrorField(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Field type for a signed exchange related error.

#### SIGNATURE_CERT_SHA256 *= 'signatureCertSha256'*

#### SIGNATURE_CERT_URL *= 'signatureCertUrl'*

#### SIGNATURE_INTEGRITY *= 'signatureIntegrity'*

#### SIGNATURE_SIG *= 'signatureSig'*

#### SIGNATURE_TIMESTAMPS *= 'signatureTimestamps'*

#### SIGNATURE_VALIDITY_URL *= 'signatureValidityUrl'*

### *class* SignedExchangeError(message, signature_index=None, error_field=None)

Information about a signed exchange response.

* **Parameters:**
  * **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **signature_index** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **error_field** ([*SignedExchangeErrorField*](#nodriver.cdp.network.SignedExchangeErrorField) *|* *None*) – 

#### error_field*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SignedExchangeErrorField`](#nodriver.cdp.network.SignedExchangeErrorField)]* *= None*

The field which caused the error.

#### message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Error message.

#### signature_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

The index of the signature which caused the error.

### *class* SignedExchangeInfo(outer_response, header=None, security_details=None, errors=None)

Information about a signed exchange response.

* **Parameters:**
  * **outer_response** ([*Response*](#nodriver.cdp.network.Response)) – 
  * **header** ([*SignedExchangeHeader*](#nodriver.cdp.network.SignedExchangeHeader) *|* *None*) – 
  * **security_details** ([*SecurityDetails*](#nodriver.cdp.network.SecurityDetails) *|* *None*) – 
  * **errors** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*SignedExchangeError*](#nodriver.cdp.network.SignedExchangeError)*]* *|* *None*) – 

#### errors*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SignedExchangeError`](#nodriver.cdp.network.SignedExchangeError)]]* *= None*

Errors occurred while handling the signed exchagne.

#### header*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SignedExchangeHeader`](#nodriver.cdp.network.SignedExchangeHeader)]* *= None*

Information about the signed exchange header.

#### outer_response*: [`Response`](#nodriver.cdp.network.Response)*

The outer response of signed HTTP exchange which was received from network.

#### security_details*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SecurityDetails`](#nodriver.cdp.network.SecurityDetails)]* *= None*

Security details for the signed exchange header.

### *class* ContentEncoding(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

List of content encodings supported by the backend.

#### BR *= 'br'*

#### DEFLATE *= 'deflate'*

#### GZIP *= 'gzip'*

#### ZSTD *= 'zstd'*

### *class* PrivateNetworkRequestPolicy(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### ALLOW *= 'Allow'*

#### BLOCK_FROM_INSECURE_TO_MORE_PRIVATE *= 'BlockFromInsecureToMorePrivate'*

#### PREFLIGHT_BLOCK *= 'PreflightBlock'*

#### PREFLIGHT_WARN *= 'PreflightWarn'*

#### WARN_FROM_INSECURE_TO_MORE_PRIVATE *= 'WarnFromInsecureToMorePrivate'*

### *class* IPAddressSpace(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### LOCAL *= 'Local'*

#### PRIVATE *= 'Private'*

#### PUBLIC *= 'Public'*

#### UNKNOWN *= 'Unknown'*

### *class* ConnectTiming(request_time)

* **Parameters:**
  **request_time** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 

#### request_time*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Timing’s requestTime is a baseline in seconds, while the other numbers are ticks in
milliseconds relatively to this requestTime. Matches ResourceTiming’s requestTime for
the same request (but not for redirected requests).

### *class* ClientSecurityState(initiator_is_secure_context, initiator_ip_address_space, private_network_request_policy)

* **Parameters:**
  * **initiator_is_secure_context** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **initiator_ip_address_space** ([*IPAddressSpace*](#nodriver.cdp.network.IPAddressSpace)) – 
  * **private_network_request_policy** ([*PrivateNetworkRequestPolicy*](#nodriver.cdp.network.PrivateNetworkRequestPolicy)) – 

#### initiator_ip_address_space*: [`IPAddressSpace`](#nodriver.cdp.network.IPAddressSpace)*

#### initiator_is_secure_context*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### private_network_request_policy*: [`PrivateNetworkRequestPolicy`](#nodriver.cdp.network.PrivateNetworkRequestPolicy)*

### *class* CrossOriginOpenerPolicyValue(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### RESTRICT_PROPERTIES *= 'RestrictProperties'*

#### RESTRICT_PROPERTIES_PLUS_COEP *= 'RestrictPropertiesPlusCoep'*

#### SAME_ORIGIN *= 'SameOrigin'*

#### SAME_ORIGIN_ALLOW_POPUPS *= 'SameOriginAllowPopups'*

#### SAME_ORIGIN_PLUS_COEP *= 'SameOriginPlusCoep'*

#### UNSAFE_NONE *= 'UnsafeNone'*

### *class* CrossOriginOpenerPolicyStatus(value, report_only_value, reporting_endpoint=None, report_only_reporting_endpoint=None)

* **Parameters:**
  * **value** ([*CrossOriginOpenerPolicyValue*](#nodriver.cdp.network.CrossOriginOpenerPolicyValue)) – 
  * **report_only_value** ([*CrossOriginOpenerPolicyValue*](#nodriver.cdp.network.CrossOriginOpenerPolicyValue)) – 
  * **reporting_endpoint** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **report_only_reporting_endpoint** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### report_only_reporting_endpoint*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### report_only_value*: [`CrossOriginOpenerPolicyValue`](#nodriver.cdp.network.CrossOriginOpenerPolicyValue)*

#### reporting_endpoint*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### value*: [`CrossOriginOpenerPolicyValue`](#nodriver.cdp.network.CrossOriginOpenerPolicyValue)*

### *class* CrossOriginEmbedderPolicyValue(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### CREDENTIALLESS *= 'Credentialless'*

#### NONE *= 'None'*

#### REQUIRE_CORP *= 'RequireCorp'*

### *class* CrossOriginEmbedderPolicyStatus(value, report_only_value, reporting_endpoint=None, report_only_reporting_endpoint=None)

* **Parameters:**
  * **value** ([*CrossOriginEmbedderPolicyValue*](#nodriver.cdp.network.CrossOriginEmbedderPolicyValue)) – 
  * **report_only_value** ([*CrossOriginEmbedderPolicyValue*](#nodriver.cdp.network.CrossOriginEmbedderPolicyValue)) – 
  * **reporting_endpoint** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **report_only_reporting_endpoint** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### report_only_reporting_endpoint*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### report_only_value*: [`CrossOriginEmbedderPolicyValue`](#nodriver.cdp.network.CrossOriginEmbedderPolicyValue)*

#### reporting_endpoint*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### value*: [`CrossOriginEmbedderPolicyValue`](#nodriver.cdp.network.CrossOriginEmbedderPolicyValue)*

### *class* ContentSecurityPolicySource(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### HTTP *= 'HTTP'*

#### META *= 'Meta'*

### *class* ContentSecurityPolicyStatus(effective_directives, is_enforced, source)

* **Parameters:**
  * **effective_directives** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **is_enforced** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **source** ([*ContentSecurityPolicySource*](#nodriver.cdp.network.ContentSecurityPolicySource)) – 

#### effective_directives*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### is_enforced*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### source*: [`ContentSecurityPolicySource`](#nodriver.cdp.network.ContentSecurityPolicySource)*

### *class* SecurityIsolationStatus(coop=None, coep=None, csp=None)

* **Parameters:**
  * **coop** ([*CrossOriginOpenerPolicyStatus*](#nodriver.cdp.network.CrossOriginOpenerPolicyStatus) *|* *None*) – 
  * **coep** ([*CrossOriginEmbedderPolicyStatus*](#nodriver.cdp.network.CrossOriginEmbedderPolicyStatus) *|* *None*) – 
  * **csp** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*ContentSecurityPolicyStatus*](#nodriver.cdp.network.ContentSecurityPolicyStatus)*]* *|* *None*) – 

#### coep*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CrossOriginEmbedderPolicyStatus`](#nodriver.cdp.network.CrossOriginEmbedderPolicyStatus)]* *= None*

#### coop*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CrossOriginOpenerPolicyStatus`](#nodriver.cdp.network.CrossOriginOpenerPolicyStatus)]* *= None*

#### csp*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ContentSecurityPolicyStatus`](#nodriver.cdp.network.ContentSecurityPolicyStatus)]]* *= None*

### *class* ReportStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The status of a Reporting API report.

#### MARKED_FOR_REMOVAL *= 'MarkedForRemoval'*

#### PENDING *= 'Pending'*

#### QUEUED *= 'Queued'*

#### SUCCESS *= 'Success'*

### *class* ReportId

### *class* ReportingApiReport(id_, initiator_url, destination, type_, timestamp, depth, completed_attempts, body, status)

An object representing a report generated by the Reporting API.

* **Parameters:**
  * **id_** ([*ReportId*](#nodriver.cdp.network.ReportId)) – 
  * **initiator_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **destination** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **type_** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **timestamp** ([*TimeSinceEpoch*](#nodriver.cdp.network.TimeSinceEpoch)) – 
  * **depth** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **completed_attempts** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **body** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – 
  * **status** ([*ReportStatus*](#nodriver.cdp.network.ReportStatus)) – 

#### body*: [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)*

#### completed_attempts*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The number of delivery attempts made so far, not including an active attempt.

#### depth*: [`int`](https://docs.python.org/3/library/functions.html#int)*

How many uploads deep the related request was.

#### destination*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The name of the endpoint group that should be used to deliver the report.

#### id_*: [`ReportId`](#nodriver.cdp.network.ReportId)*

#### initiator_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The URL of the document that triggered the report.

#### status*: [`ReportStatus`](#nodriver.cdp.network.ReportStatus)*

#### timestamp*: [`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)*

When the report was generated.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The type of the report (specifies the set of data that is contained in the report body).

### *class* ReportingApiEndpoint(url, group_name)

* **Parameters:**
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **group_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### group_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name of the endpoint group.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The URL of the endpoint to which reports may be delivered.

### *class* LoadNetworkResourcePageResult(success, net_error=None, net_error_name=None, http_status_code=None, stream=None, headers=None)

An object providing the result of a network resource load.

* **Parameters:**
  * **success** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **net_error** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **net_error_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **http_status_code** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **stream** ([*StreamHandle*](io.md#nodriver.cdp.io.StreamHandle) *|* *None*) – 
  * **headers** ([*Headers*](#nodriver.cdp.network.Headers) *|* *None*) – 

#### headers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Headers`](#nodriver.cdp.network.Headers)]* *= None*

Response headers.

#### http_status_code*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

#### net_error*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Optional values used for error reporting.

#### net_error_name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### stream*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StreamHandle`](io.md#nodriver.cdp.io.StreamHandle)]* *= None*

If successful, one of the following two fields holds the result.

#### success*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

### *class* LoadNetworkResourceOptions(disable_cache, include_credentials)

An options object that may be extended later to better support CORS,
CORB and streaming.

* **Parameters:**
  * **disable_cache** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **include_credentials** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 

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
[Getting Started: Commands](../quickstart.md#getting-started-commands).

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

### delete_cookies(name, url=None, domain=None, path=None)

Deletes browser cookies with matching name and url or domain/path pair.

* **Parameters:**
  * **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Name of the cookies to remove.
  * **url** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If specified, deletes all the cookies with the given name where domain and path match provided URL.
  * **domain** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If specified, deletes only cookies with the exact domain.
  * **path** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If specified, deletes only cookies with the exact path.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### disable()

Disables network tracking, prevents network events from being sent to the client.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### emulate_network_conditions(offline, latency, download_throughput, upload_throughput, connection_type=None)

Activates emulation of network conditions.

* **Parameters:**
  * **offline** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – True to emulate internet disconnection.
  * **latency** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Minimum latency from request sent to response headers received (ms).
  * **download_throughput** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
  * **upload_throughput** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
  * **connection_type** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ConnectionType`](#nodriver.cdp.network.ConnectionType)]) – *(Optional)* Connection type if known.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable(max_total_buffer_size=None, max_resource_buffer_size=None, max_post_data_size=None)

Enables network tracking, network events will now be delivered to the client.

* **Parameters:**
  * **max_total_buffer_size** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* Buffer size in bytes to use when preserving network payloads (XHRs, etc).
  * **max_resource_buffer_size** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – **(EXPERIMENTAL)** *(Optional)* Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
  * **max_post_data_size** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Longest post body size (in bytes) that would be included in requestWillBeSent notification
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
  * **partition_key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* Cookie partition key. The site of the top-level URL the browser was visiting at the start of the request to the endpoint that set the cookie. If not set, the cookie will be set as not partitioned.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`bool`](https://docs.python.org/3/library/functions.html#bool)]
* **Returns:**
  Always set to true. If an error occurs, the response indicates protocol error.

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

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 
  * **data_length** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **encoded_data_length** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Data that was received. (Encoded as a base64 string when passed over JSON)

#### data_length*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Data chunk length.

#### encoded_data_length*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Actual bytes received (might be less than dataLength for compressed encodings).

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* EventSourceMessageReceived(request_id, timestamp, event_name, event_id, data)

Fired when EventSource message is received.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 
  * **event_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **event_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Message content.

#### event_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Message identifier.

#### event_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Message type.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* LoadingFailed(request_id, timestamp, type_, error_text, canceled, blocked_reason, cors_error_status)

Fired when HTTP request has failed to load.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 
  * **type_** ([*ResourceType*](#nodriver.cdp.network.ResourceType)) – 
  * **error_text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **canceled** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **blocked_reason** ([*BlockedReason*](#nodriver.cdp.network.BlockedReason) *|* *None*) – 
  * **cors_error_status** ([*CorsErrorStatus*](#nodriver.cdp.network.CorsErrorStatus) *|* *None*) – 

#### blocked_reason*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BlockedReason`](#nodriver.cdp.network.BlockedReason)]*

The reason why loading was blocked, if any.

#### canceled*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

True if loading was canceled.

#### cors_error_status*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CorsErrorStatus`](#nodriver.cdp.network.CorsErrorStatus)]*

The reason why loading was blocked by CORS, if any.

#### error_text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

User friendly error message.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### type_*: [`ResourceType`](#nodriver.cdp.network.ResourceType)*

Resource type.

### *class* LoadingFinished(request_id, timestamp, encoded_data_length)

Fired when HTTP request has finished loading.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 
  * **encoded_data_length** ([*float*](https://docs.python.org/3/library/functions.html#float)) – 

#### encoded_data_length*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Total number of bytes received for this request.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* RequestIntercepted(interception_id, request, frame_id, resource_type, is_navigation_request, is_download, redirect_url, auth_challenge, response_error_reason, response_status_code, response_headers, request_id)

**EXPERIMENTAL**

Details of an intercepted HTTP request, which must be either allowed, blocked, modified or
mocked.
Deprecated, use Fetch.requestPaused instead.

#### Deprecated
Deprecated since version 1.3.

#### auth_challenge*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AuthChallenge`](#nodriver.cdp.network.AuthChallenge)]*

Details of the Authorization Challenge encountered. If this is set then
continueInterceptedRequest must contain an authChallengeResponse.

#### frame_id*: [`FrameId`](page.md#nodriver.cdp.page.FrameId)*

The id of the frame that initiated the request.

#### interception_id*: [`InterceptionId`](#nodriver.cdp.network.InterceptionId)*

Each request the page makes will have a unique id, however if any redirects are encountered
while processing that fetch, they will be reported with the same id as the original fetch.
Likewise if HTTP authentication is needed then the same fetch id will be used.

#### is_download*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

Set if the request is a navigation that will result in a download.
Only present after response is received from the server (i.e. HeadersReceived stage).

#### is_navigation_request*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether this is a navigation request, which can abort the navigation completely.

#### redirect_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Redirect location, only sent if a redirect was intercepted.

#### request*: [`Request`](#nodriver.cdp.network.Request)*

#### request_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestId`](#nodriver.cdp.network.RequestId)]*

If the intercepted request had a corresponding requestWillBeSent event fired for it, then
this requestId will be the same as the requestId present in the requestWillBeSent event.

#### resource_type*: [`ResourceType`](#nodriver.cdp.network.ResourceType)*

How the requested resource will be used.

#### response_error_reason*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ErrorReason`](#nodriver.cdp.network.ErrorReason)]*

Response error if intercepted at response stage or if redirect occurred while intercepting
request.

#### response_headers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Headers`](#nodriver.cdp.network.Headers)]*

Response headers if intercepted at the response stage or if redirect occurred while
intercepting request or auth retry occurred.

#### response_status_code*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

Response code if intercepted at response stage or if redirect occurred while intercepting
request or auth retry occurred.

### *class* RequestServedFromCache(request_id)

Fired if request ended up loading from cache.

* **Parameters:**
  **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

### *class* RequestWillBeSent(request_id, loader_id, document_url, request, timestamp, wall_time, initiator, redirect_has_extra_info, redirect_response, type_, frame_id, has_user_gesture)

Fired when page is about to send HTTP request.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **loader_id** ([*LoaderId*](#nodriver.cdp.network.LoaderId)) – 
  * **document_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **request** ([*Request*](#nodriver.cdp.network.Request)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 
  * **wall_time** ([*TimeSinceEpoch*](#nodriver.cdp.network.TimeSinceEpoch)) – 
  * **initiator** ([*Initiator*](#nodriver.cdp.network.Initiator)) – 
  * **redirect_has_extra_info** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **redirect_response** ([*Response*](#nodriver.cdp.network.Response) *|* *None*) – 
  * **type_** ([*ResourceType*](#nodriver.cdp.network.ResourceType) *|* *None*) – 
  * **frame_id** ([*FrameId*](page.md#nodriver.cdp.page.FrameId) *|* *None*) – 
  * **has_user_gesture** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 

#### document_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL of the document this request is loaded for.

#### frame_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]*

Frame identifier.

#### has_user_gesture*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

Whether the request is initiated by a user gesture. Defaults to false.

#### initiator*: [`Initiator`](#nodriver.cdp.network.Initiator)*

Request initiator.

#### loader_id*: [`LoaderId`](#nodriver.cdp.network.LoaderId)*

Loader identifier. Empty string if the request is fetched from worker.

#### redirect_has_extra_info*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

In the case that redirectResponse is populated, this flag indicates whether
requestWillBeSentExtraInfo and responseReceivedExtraInfo events will be or were emitted
for the request which was just redirected.

#### redirect_response*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Response`](#nodriver.cdp.network.Response)]*

Redirect response data.

#### request*: [`Request`](#nodriver.cdp.network.Request)*

Request data.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### type_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ResourceType`](#nodriver.cdp.network.ResourceType)]*

Type of this resource.

#### wall_time*: [`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)*

Timestamp.

### *class* ResourceChangedPriority(request_id, new_priority, timestamp)

**EXPERIMENTAL**

Fired when resource loading priority is changed

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **new_priority** ([*ResourcePriority*](#nodriver.cdp.network.ResourcePriority)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 

#### new_priority*: [`ResourcePriority`](#nodriver.cdp.network.ResourcePriority)*

New priority

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* SignedExchangeReceived(request_id, info)

**EXPERIMENTAL**

Fired when a signed exchange was received over the network

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **info** ([*SignedExchangeInfo*](#nodriver.cdp.network.SignedExchangeInfo)) – 

#### info*: [`SignedExchangeInfo`](#nodriver.cdp.network.SignedExchangeInfo)*

Information about the signed exchange response.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

### *class* ResponseReceived(request_id, loader_id, timestamp, type_, response, has_extra_info, frame_id)

Fired when HTTP response is available.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **loader_id** ([*LoaderId*](#nodriver.cdp.network.LoaderId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 
  * **type_** ([*ResourceType*](#nodriver.cdp.network.ResourceType)) – 
  * **response** ([*Response*](#nodriver.cdp.network.Response)) – 
  * **has_extra_info** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **frame_id** ([*FrameId*](page.md#nodriver.cdp.page.FrameId) *|* *None*) – 

#### frame_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]*

Frame identifier.

#### has_extra_info*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Indicates whether requestWillBeSentExtraInfo and responseReceivedExtraInfo events will be
or were emitted for this request.

#### loader_id*: [`LoaderId`](#nodriver.cdp.network.LoaderId)*

Loader identifier. Empty string if the request is fetched from worker.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### response*: [`Response`](#nodriver.cdp.network.Response)*

Response data.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### type_*: [`ResourceType`](#nodriver.cdp.network.ResourceType)*

Resource type.

### *class* WebSocketClosed(request_id, timestamp)

Fired when WebSocket is closed.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* WebSocketCreated(request_id, url, initiator)

Fired upon WebSocket creation.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **initiator** ([*Initiator*](#nodriver.cdp.network.Initiator) *|* *None*) – 

#### initiator*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Initiator`](#nodriver.cdp.network.Initiator)]*

Request initiator.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

WebSocket request URL.

### *class* WebSocketFrameError(request_id, timestamp, error_message)

Fired when WebSocket message error occurs.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 
  * **error_message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### error_message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

WebSocket error message.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* WebSocketFrameReceived(request_id, timestamp, response)

Fired when WebSocket message is received.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 
  * **response** ([*WebSocketFrame*](#nodriver.cdp.network.WebSocketFrame)) – 

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### response*: [`WebSocketFrame`](#nodriver.cdp.network.WebSocketFrame)*

WebSocket response data.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* WebSocketFrameSent(request_id, timestamp, response)

Fired when WebSocket message is sent.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 
  * **response** ([*WebSocketFrame*](#nodriver.cdp.network.WebSocketFrame)) – 

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### response*: [`WebSocketFrame`](#nodriver.cdp.network.WebSocketFrame)*

WebSocket response data.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* WebSocketHandshakeResponseReceived(request_id, timestamp, response)

Fired when WebSocket handshake response becomes available.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 
  * **response** ([*WebSocketResponse*](#nodriver.cdp.network.WebSocketResponse)) – 

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### response*: [`WebSocketResponse`](#nodriver.cdp.network.WebSocketResponse)*

WebSocket response data.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

### *class* WebSocketWillSendHandshakeRequest(request_id, timestamp, wall_time, request)

Fired when WebSocket is about to initiate handshake.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 
  * **wall_time** ([*TimeSinceEpoch*](#nodriver.cdp.network.TimeSinceEpoch)) – 
  * **request** ([*WebSocketRequest*](#nodriver.cdp.network.WebSocketRequest)) – 

#### request*: [`WebSocketRequest`](#nodriver.cdp.network.WebSocketRequest)*

WebSocket request data.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### wall_time*: [`TimeSinceEpoch`](#nodriver.cdp.network.TimeSinceEpoch)*

UTC Timestamp.

### *class* WebTransportCreated(transport_id, url, timestamp, initiator)

Fired upon WebTransport creation.

* **Parameters:**
  * **transport_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 
  * **initiator** ([*Initiator*](#nodriver.cdp.network.Initiator) *|* *None*) – 

#### initiator*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Initiator`](#nodriver.cdp.network.Initiator)]*

Request initiator.

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### transport_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

WebTransport identifier.

#### url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

WebTransport request URL.

### *class* WebTransportConnectionEstablished(transport_id, timestamp)

Fired when WebTransport handshake is finished.

* **Parameters:**
  * **transport_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### transport_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

WebTransport identifier.

### *class* WebTransportClosed(transport_id, timestamp)

Fired when WebTransport is disposed.

* **Parameters:**
  * **transport_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **timestamp** ([*MonotonicTime*](#nodriver.cdp.network.MonotonicTime)) – 

#### timestamp*: [`MonotonicTime`](#nodriver.cdp.network.MonotonicTime)*

Timestamp.

#### transport_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

WebTransport identifier.

### *class* RequestWillBeSentExtraInfo(request_id, associated_cookies, headers, connect_timing, client_security_state, site_has_cookie_in_other_partition)

**EXPERIMENTAL**

Fired when additional information about a requestWillBeSent event is available from the
network stack. Not every requestWillBeSent event will have an additional
requestWillBeSentExtraInfo fired for it, and there is no guarantee whether requestWillBeSent
or requestWillBeSentExtraInfo will be fired first for the same request.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **associated_cookies** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*BlockedCookieWithReason*](#nodriver.cdp.network.BlockedCookieWithReason)*]*) – 
  * **headers** ([*Headers*](#nodriver.cdp.network.Headers)) – 
  * **connect_timing** ([*ConnectTiming*](#nodriver.cdp.network.ConnectTiming)) – 
  * **client_security_state** ([*ClientSecurityState*](#nodriver.cdp.network.ClientSecurityState) *|* *None*) – 
  * **site_has_cookie_in_other_partition** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 

#### associated_cookies*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BlockedCookieWithReason`](#nodriver.cdp.network.BlockedCookieWithReason)]*

A list of cookies potentially associated to the requested URL. This includes both cookies sent with
the request and the ones not sent; the latter are distinguished by having blockedReason field set.

#### client_security_state*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ClientSecurityState`](#nodriver.cdp.network.ClientSecurityState)]*

The client security state set for the request.

#### connect_timing*: [`ConnectTiming`](#nodriver.cdp.network.ConnectTiming)*

Connection timing information for the request.

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

Raw request headers as they will be sent over the wire.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier. Used to match this information to an existing requestWillBeSent event.

#### site_has_cookie_in_other_partition*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

Whether the site has partitioned cookies stored in a partition different than the current one.

### *class* ResponseReceivedExtraInfo(request_id, blocked_cookies, headers, resource_ip_address_space, status_code, headers_text, cookie_partition_key, cookie_partition_key_opaque)

**EXPERIMENTAL**

Fired when additional information about a responseReceived event is available from the network
stack. Not every responseReceived event will have an additional responseReceivedExtraInfo for
it, and responseReceivedExtraInfo may be fired before or after responseReceived.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **blocked_cookies** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*BlockedSetCookieWithReason*](#nodriver.cdp.network.BlockedSetCookieWithReason)*]*) – 
  * **headers** ([*Headers*](#nodriver.cdp.network.Headers)) – 
  * **resource_ip_address_space** ([*IPAddressSpace*](#nodriver.cdp.network.IPAddressSpace)) – 
  * **status_code** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **headers_text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **cookie_partition_key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **cookie_partition_key_opaque** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 

#### blocked_cookies*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BlockedSetCookieWithReason`](#nodriver.cdp.network.BlockedSetCookieWithReason)]*

A list of cookies which were not stored from the response along with the corresponding
reasons for blocking. The cookies here may not be valid due to syntax errors, which
are represented by the invalid cookie line string instead of a proper cookie.

#### cookie_partition_key*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

The cookie partition key that will be used to store partitioned cookies set in this response.
Only sent when partitioned cookies are enabled.

#### cookie_partition_key_opaque*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

True if partitioned cookies are enabled, but the partition key is not serializeable to string.

#### headers*: [`Headers`](#nodriver.cdp.network.Headers)*

Raw response headers as they were received over the wire.

#### headers_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Raw response header text as it was received over the wire. The raw text may not always be
available, such as in the case of HTTP/2 or QUIC.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier. Used to match this information to another responseReceived event.

#### resource_ip_address_space*: [`IPAddressSpace`](#nodriver.cdp.network.IPAddressSpace)*

The IP address space of the resource. The address space can only be determined once the transport
established the connection, so we can’t send it in `requestWillBeSentExtraInfo`.

#### status_code*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The status code of the response. This is useful in cases the request failed and no responseReceived
event is triggered, which is the case for, e.g., CORS errors. This is also the correct status code
for cached requests, where the status in responseReceived is a 200 and this will be 304.

### *class* TrustTokenOperationDone(status, type_, request_id, top_level_origin, issuer_origin, issued_token_count)

**EXPERIMENTAL**

Fired exactly once for each Trust Token operation. Depending on
the type of the operation and whether the operation succeeded or
failed, the event is fired before the corresponding request was sent
or after the response was received.

* **Parameters:**
  * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **type_** ([*TrustTokenOperationType*](#nodriver.cdp.network.TrustTokenOperationType)) – 
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **top_level_origin** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **issuer_origin** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **issued_token_count** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 

#### issued_token_count*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

The number of obtained Trust Tokens on a successful “Issuance” operation.

#### issuer_origin*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Origin of the issuer in case of a “Issuance” or “Redemption” operation.

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

#### status*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Detailed success or error status of the operation.
‘AlreadyExists’ also signifies a successful operation, as the result
of the operation already exists und thus, the operation was abort
preemptively (e.g. a cache hit).

#### top_level_origin*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Top level origin. The context in which the operation was attempted.

#### type_*: [`TrustTokenOperationType`](#nodriver.cdp.network.TrustTokenOperationType)*

### *class* SubresourceWebBundleMetadataReceived(request_id, urls)

**EXPERIMENTAL**

Fired once when parsing the .wbn file has succeeded.
The event contains the information about the web bundle contents.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **urls** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier. Used to match this information to another event.

#### urls*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

A list of URLs of resources in the subresource Web Bundle.

### *class* SubresourceWebBundleMetadataError(request_id, error_message)

**EXPERIMENTAL**

Fired once when parsing the .wbn file has failed.

* **Parameters:**
  * **request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **error_message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### error_message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Error message

#### request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier. Used to match this information to another event.

### *class* SubresourceWebBundleInnerResponseParsed(inner_request_id, inner_request_url, bundle_request_id)

**EXPERIMENTAL**

Fired when handling requests for resources within a .wbn file.
Note: this will only be fired for resources that are requested by the webpage.

* **Parameters:**
  * **inner_request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **inner_request_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **bundle_request_id** ([*RequestId*](#nodriver.cdp.network.RequestId) *|* *None*) – 

#### bundle_request_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestId`](#nodriver.cdp.network.RequestId)]*

Bundle request identifier. Used to match this information to another event.
This made be absent in case when the instrumentation was enabled only
after webbundle was parsed.

#### inner_request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier of the subresource request

#### inner_request_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL of the subresource resource.

### *class* SubresourceWebBundleInnerResponseError(inner_request_id, inner_request_url, error_message, bundle_request_id)

**EXPERIMENTAL**

Fired when request for resources within a .wbn file failed.

* **Parameters:**
  * **inner_request_id** ([*RequestId*](#nodriver.cdp.network.RequestId)) – 
  * **inner_request_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **error_message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **bundle_request_id** ([*RequestId*](#nodriver.cdp.network.RequestId) *|* *None*) – 

#### bundle_request_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestId`](#nodriver.cdp.network.RequestId)]*

Bundle request identifier. Used to match this information to another event.
This made be absent in case when the instrumentation was enabled only
after webbundle was parsed.

#### error_message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Error message

#### inner_request_id*: [`RequestId`](#nodriver.cdp.network.RequestId)*

Request identifier of the subresource request

#### inner_request_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

URL of the subresource resource.

### *class* ReportingApiReportAdded(report)

**EXPERIMENTAL**

Is sent whenever a new report is added.
And after ‘enableReportingApi’ for all existing reports.

* **Parameters:**
  **report** ([*ReportingApiReport*](#nodriver.cdp.network.ReportingApiReport)) – 

#### report*: [`ReportingApiReport`](#nodriver.cdp.network.ReportingApiReport)*

### *class* ReportingApiReportUpdated(report)

**EXPERIMENTAL**

* **Parameters:**
  **report** ([*ReportingApiReport*](#nodriver.cdp.network.ReportingApiReport)) – 

#### report*: [`ReportingApiReport`](#nodriver.cdp.network.ReportingApiReport)*

### *class* ReportingApiEndpointsChangedForOrigin(origin, endpoints)

**EXPERIMENTAL**

* **Parameters:**
  * **origin** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **endpoints** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*ReportingApiEndpoint*](#nodriver.cdp.network.ReportingApiEndpoint)*]*) – 

#### endpoints*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ReportingApiEndpoint`](#nodriver.cdp.network.ReportingApiEndpoint)]*

#### origin*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Origin of the document(s) which configured the endpoints.
