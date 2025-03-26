Network
=======

Network domain allows tracking network activities of the page. It exposes information about http,
file, data and other requests and responses, their headers, bodies, timing, etc.

.. module:: nodriver.cdp.network

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: ResourceType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: LoaderId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RequestId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: InterceptionId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ErrorReason
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TimeSinceEpoch
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: MonotonicTime
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Headers
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ConnectionType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CookieSameSite
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CookiePriority
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CookieSourceScheme
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ResourceTiming
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ResourcePriority
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PostDataEntry
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Request
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SignedCertificateTimestamp
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SecurityDetails
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CertificateTransparencyCompliance
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BlockedReason
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CorsError
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CorsErrorStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ServiceWorkerResponseSource
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TrustTokenParams
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TrustTokenOperationType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AlternateProtocolUsage
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ServiceWorkerRouterSource
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ServiceWorkerRouterInfo
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Response
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebSocketRequest
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebSocketResponse
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebSocketFrame
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CachedResource
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Initiator
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CookiePartitionKey
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Cookie
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SetCookieBlockedReason
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CookieBlockedReason
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CookieExemptionReason
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BlockedSetCookieWithReason
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ExemptedSetCookieWithReason
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AssociatedCookie
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CookieParam
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AuthChallenge
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AuthChallengeResponse
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: InterceptionStage
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RequestPattern
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SignedExchangeSignature
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SignedExchangeHeader
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SignedExchangeErrorField
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SignedExchangeError
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SignedExchangeInfo
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ContentEncoding
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DirectSocketDnsQueryType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DirectTCPSocketOptions
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PrivateNetworkRequestPolicy
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: IPAddressSpace
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ConnectTiming
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ClientSecurityState
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CrossOriginOpenerPolicyValue
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CrossOriginOpenerPolicyStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CrossOriginEmbedderPolicyValue
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CrossOriginEmbedderPolicyStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ContentSecurityPolicySource
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ContentSecurityPolicyStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SecurityIsolationStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReportStatus
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReportId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReportingApiReport
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReportingApiEndpoint
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: LoadNetworkResourcePageResult
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: LoadNetworkResourceOptions
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

.. autofunction:: can_clear_browser_cache

.. autofunction:: can_clear_browser_cookies

.. autofunction:: can_emulate_network_conditions

.. autofunction:: clear_accepted_encodings_override

.. autofunction:: clear_browser_cache

.. autofunction:: clear_browser_cookies

.. autofunction:: continue_intercepted_request

.. autofunction:: delete_cookies

.. autofunction:: disable

.. autofunction:: emulate_network_conditions

.. autofunction:: enable

.. autofunction:: enable_reporting_api

.. autofunction:: get_all_cookies

.. autofunction:: get_certificate

.. autofunction:: get_cookies

.. autofunction:: get_request_post_data

.. autofunction:: get_response_body

.. autofunction:: get_response_body_for_interception

.. autofunction:: get_security_isolation_status

.. autofunction:: load_network_resource

.. autofunction:: replay_xhr

.. autofunction:: search_in_response_body

.. autofunction:: set_accepted_encodings

.. autofunction:: set_attach_debug_stack

.. autofunction:: set_blocked_ur_ls

.. autofunction:: set_bypass_service_worker

.. autofunction:: set_cache_disabled

.. autofunction:: set_cookie

.. autofunction:: set_cookie_controls

.. autofunction:: set_cookies

.. autofunction:: set_extra_http_headers

.. autofunction:: set_request_interception

.. autofunction:: set_user_agent_override

.. autofunction:: stream_resource_content

.. autofunction:: take_response_body_for_interception_as_stream

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: DataReceived
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: EventSourceMessageReceived
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: LoadingFailed
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: LoadingFinished
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RequestIntercepted
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RequestServedFromCache
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RequestWillBeSent
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ResourceChangedPriority
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SignedExchangeReceived
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ResponseReceived
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebSocketClosed
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebSocketCreated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebSocketFrameError
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebSocketFrameReceived
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebSocketFrameSent
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebSocketHandshakeResponseReceived
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebSocketWillSendHandshakeRequest
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebTransportCreated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebTransportConnectionEstablished
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: WebTransportClosed
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DirectTCPSocketCreated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DirectTCPSocketOpened
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DirectTCPSocketAborted
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DirectTCPSocketClosed
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RequestWillBeSentExtraInfo
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ResponseReceivedExtraInfo
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ResponseReceivedEarlyHints
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TrustTokenOperationDone
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PolicyUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SubresourceWebBundleMetadataReceived
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SubresourceWebBundleMetadataError
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SubresourceWebBundleInnerResponseParsed
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SubresourceWebBundleInnerResponseError
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReportingApiReportAdded
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReportingApiReportUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ReportingApiEndpointsChangedForOrigin
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
