# Fetch

A domain for letting clients substitute browser’s network layer with client code.

<a id="module-nodriver.cdp.fetch"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* RequestId

Unique request identifier.
Note that this does not identify individual HTTP requests that are part of
a network request.

### *class* RequestStage(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Stages of the request to handle. Request will intercept before the request is
sent. Response will intercept after the response is received (but before response
body is received).

#### REQUEST *= 'Request'*

#### RESPONSE *= 'Response'*

### *class* RequestPattern(url_pattern=None, resource_type=None, request_stage=None)

#### url_pattern*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Wildcards (`'*'` -> zero or more, `'?'` -> exactly one) are allowed. Escape character is
backslash. Omitting is equivalent to `"*"`.

#### resource_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ResourceType`](network.md#nodriver.cdp.network.ResourceType)]* *= None*

If set, only requests for matching resource types will be intercepted.

#### request_stage*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestStage`](#nodriver.cdp.fetch.RequestStage)]* *= None*

Stage at which to begin intercepting requests. Default is Request.

### *class* HeaderEntry(name, value)

Response HTTP header entry

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

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

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### continue_request(request_id, url=None, method=None, post_data=None, headers=None, intercept_response=None)

Continues the request, optionally modifying some of its parameters.

* **Parameters:**
  * **request_id** ([`RequestId`](#nodriver.cdp.fetch.RequestId)) – An id the client received in requestPaused event.
  * **url** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If set, the request url will be modified in a way that’s not observable by page.
  * **method** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If set, the request method is overridden.
  * **post_data** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If set, overrides the post data in the request. (Encoded as a base64 string when passed over JSON)
  * **headers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`HeaderEntry`](#nodriver.cdp.fetch.HeaderEntry)]]) – *(Optional)* If set, overrides the request headers. Note that the overrides do not extend to subsequent redirect hops, if a redirect happens. Another override may be applied to a different request produced by a redirect.
  * **intercept_response** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* If set, overrides response interception behavior for this request.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### continue_response(request_id, response_code=None, response_phrase=None, response_headers=None, binary_response_headers=None)

Continues loading of the paused response, optionally modifying the
response headers. If either responseCode or headers are modified, all of them
must be present.

**EXPERIMENTAL**

* **Parameters:**
  * **request_id** ([`RequestId`](#nodriver.cdp.fetch.RequestId)) – An id the client received in requestPaused event.
  * **response_code** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* An HTTP response code. If absent, original response code will be used.
  * **response_phrase** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* A textual representation of responseCode. If absent, a standard phrase matching responseCode is used.
  * **response_headers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`HeaderEntry`](#nodriver.cdp.fetch.HeaderEntry)]]) – *(Optional)* Response headers. If absent, original response headers will be used.
  * **binary_response_headers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Alternative way of specifying response headers as a 0-separated series of name: value pairs. Prefer the above method unless you need to represent some non-UTF8 values that can’t be transmitted over the protocol as text. (Encoded as a base64 string when passed over JSON)
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### continue_with_auth(request_id, auth_challenge_response)

Continues a request supplying authChallengeResponse following authRequired event.

* **Parameters:**
  * **request_id** ([`RequestId`](#nodriver.cdp.fetch.RequestId)) – An id the client received in authRequired event.
  * **auth_challenge_response** ([`AuthChallengeResponse`](#nodriver.cdp.fetch.AuthChallengeResponse)) – Response to  with an authChallenge.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### disable()

Disables the fetch domain.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable(patterns=None, handle_auth_requests=None)

Enables issuing of requestPaused events. A request will be paused until client
calls one of failRequest, fulfillRequest or continueRequest/continueWithAuth.

* **Parameters:**
  * **patterns** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`RequestPattern`](#nodriver.cdp.fetch.RequestPattern)]]) – *(Optional)* If specified, only requests matching any of these patterns will produce fetchRequested event and will be paused until clients response. If not set, all requests will be affected.
  * **handle_auth_requests** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, authRequired events will be issued and requests will be paused expecting a call to continueWithAuth.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### fail_request(request_id, error_reason)

Causes the request to fail with specified reason.

* **Parameters:**
  * **request_id** ([`RequestId`](#nodriver.cdp.fetch.RequestId)) – An id the client received in requestPaused event.
  * **error_reason** ([`ErrorReason`](network.md#nodriver.cdp.network.ErrorReason)) – Causes the request to fail with the given reason.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### fulfill_request(request_id, response_code, response_headers=None, binary_response_headers=None, body=None, response_phrase=None)

Provides response to the request.

* **Parameters:**
  * **request_id** ([`RequestId`](#nodriver.cdp.fetch.RequestId)) – An id the client received in requestPaused event.
  * **response_code** ([`int`](https://docs.python.org/3/library/functions.html#int)) – An HTTP response code.
  * **response_headers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`HeaderEntry`](#nodriver.cdp.fetch.HeaderEntry)]]) – *(Optional)* Response headers.
  * **binary_response_headers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Alternative way of specifying response headers as a 0-separated series of name: value pairs. Prefer the above method unless you need to represent some non-UTF8 values that can’t be transmitted over the protocol as text. (Encoded as a base64 string when passed over JSON)
  * **body** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* A response body. If absent, original response body will be used if the request is intercepted at the response stage and empty body will be used if the request is intercepted at the request stage. (Encoded as a base64 string when passed over JSON)
  * **response_phrase** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* A textual representation of responseCode. If absent, a standard phrase matching responseCode is used.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_response_body(request_id)

Causes the body of the response to be received from the server and
returned as a single string. May only be issued for a request that
is paused in the Response stage and is mutually exclusive with
takeResponseBodyForInterceptionAsStream. Calling other methods that
affect the request or disabling fetch domain before body is received
results in an undefined behavior.
Note that the response body is not available for redirects. Requests
paused in the \_redirect 

```
received_
```

 state may be differentiated by
`responseCode` and presence of `location` response header, see
comments to `requestPaused` for details.

* **Parameters:**
  **request_id** ([`RequestId`](#nodriver.cdp.fetch.RequestId)) – Identifier for the intercepted request to get body for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`bool`](https://docs.python.org/3/library/functions.html#bool)]]
* **Returns:**
  A tuple with the following items:
  1. **body** - Response body.
  2. **base64Encoded** - True, if content was sent as base64.

### take_response_body_as_stream(request_id)

Returns a handle to the stream representing the response body.
The request must be paused in the HeadersReceived stage.
Note that after this command the request can’t be continued
as is – client either needs to cancel it or to provide the
response body.
The stream only supports sequential read, IO.read will fail if the position
is specified.
This method is mutually exclusive with getResponseBody.
Calling other methods that affect the request or disabling fetch
domain before body is received results in an undefined behavior.

* **Parameters:**
  **request_id** ([`RequestId`](#nodriver.cdp.fetch.RequestId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`StreamHandle`](io.md#nodriver.cdp.io.StreamHandle)]
* **Returns:**

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* RequestPaused(request_id, request, frame_id, resource_type, response_error_reason, response_status_code, response_status_text, response_headers, network_id, redirected_request_id)

Issued when the domain is enabled and the request URL matches the
specified filter. The request is paused until the client responds
with one of continueRequest, failRequest or fulfillRequest.
The stage of the request can be determined by presence of responseErrorReason
and responseStatusCode – the request is at the response stage if either
of these fields is present and in the request stage otherwise.
Redirect responses and subsequent requests are reported similarly to regular
responses and requests. Redirect responses may be distinguished by the value
of `responseStatusCode` (which is one of 301, 302, 303, 307, 308) along with
presence of the `location` header. Requests resulting from a redirect will
have `redirectedRequestId` field set.

#### request_id*: [`RequestId`](#nodriver.cdp.fetch.RequestId)*

Each request the page makes will have a unique id.

#### request*: [`Request`](network.md#nodriver.cdp.network.Request)*

The details of the request.

#### frame_id*: [`FrameId`](page.md#nodriver.cdp.page.FrameId)*

The id of the frame that initiated the request.

#### resource_type*: [`ResourceType`](network.md#nodriver.cdp.network.ResourceType)*

How the requested resource will be used.

#### response_error_reason*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ErrorReason`](network.md#nodriver.cdp.network.ErrorReason)]*

Response error if intercepted at response stage.

#### response_status_code*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

Response code if intercepted at response stage.

#### response_status_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Response status text if intercepted at response stage.

#### response_headers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`HeaderEntry`](#nodriver.cdp.fetch.HeaderEntry)]]*

Response headers if intercepted at the response stage.

#### network_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestId`](network.md#nodriver.cdp.network.RequestId)]*

If the intercepted request had a corresponding Network.requestWillBeSent event fired for it,
then this networkId will be the same as the requestId present in the requestWillBeSent event.

#### redirected_request_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RequestId`](#nodriver.cdp.fetch.RequestId)]*

If the request is due to a redirect response from the server, the id of the request that
has caused the redirect.

### *class* AuthRequired(request_id, request, frame_id, resource_type, auth_challenge)

Issued when the domain is enabled with handleAuthRequests set to true.
The request is paused until client responds with continueWithAuth.

#### request_id*: [`RequestId`](#nodriver.cdp.fetch.RequestId)*

Each request the page makes will have a unique id.

#### request*: [`Request`](network.md#nodriver.cdp.network.Request)*

The details of the request.

#### frame_id*: [`FrameId`](page.md#nodriver.cdp.page.FrameId)*

The id of the frame that initiated the request.

#### resource_type*: [`ResourceType`](network.md#nodriver.cdp.network.ResourceType)*

How the requested resource will be used.

#### auth_challenge*: [`AuthChallenge`](#nodriver.cdp.fetch.AuthChallenge)*

Details of the Authorization Challenge encountered.
If this is set, client should respond with continueRequest that
contains AuthChallengeResponse.
