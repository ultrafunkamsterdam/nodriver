# Security

Security

<a id="module-nodriver.cdp.security"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* CertificateId

An internal certificate ID value.

### *class* MixedContentType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

A description of mixed content (HTTP resources on HTTPS pages), as defined by
[https://www.w3.org/TR/mixed-content/#categories](https://www.w3.org/TR/mixed-content/#categories)

#### BLOCKABLE *= 'blockable'*

#### NONE *= 'none'*

#### OPTIONALLY_BLOCKABLE *= 'optionally-blockable'*

### *class* SecurityState(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The security level of a page or resource.

#### INFO *= 'info'*

#### INSECURE *= 'insecure'*

#### INSECURE_BROKEN *= 'insecure-broken'*

#### NEUTRAL *= 'neutral'*

#### SECURE *= 'secure'*

#### UNKNOWN *= 'unknown'*

### *class* CertificateSecurityState(protocol, key_exchange, cipher, certificate, subject_name, issuer, valid_from, valid_to, certificate_has_weak_signature, certificate_has_sha1_signature, modern_ssl, obsolete_ssl_protocol, obsolete_ssl_key_exchange, obsolete_ssl_cipher, obsolete_ssl_signature, key_exchange_group=None, mac=None, certificate_network_error=None)

Details about the security state of the page certificate.

* **Parameters:**
  * **protocol** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **key_exchange** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **cipher** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **certificate** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **subject_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **issuer** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **valid_from** ([*TimeSinceEpoch*](network.md#nodriver.cdp.network.TimeSinceEpoch)) – 
  * **valid_to** ([*TimeSinceEpoch*](network.md#nodriver.cdp.network.TimeSinceEpoch)) – 
  * **certificate_has_weak_signature** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **certificate_has_sha1_signature** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **modern_ssl** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **obsolete_ssl_protocol** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **obsolete_ssl_key_exchange** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **obsolete_ssl_cipher** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **obsolete_ssl_signature** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **key_exchange_group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **mac** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **certificate_network_error** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### certificate*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Page certificate.

#### certificate_has_sha1_signature*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if the certificate has a SHA1 signature in the chain.

#### certificate_has_weak_signature*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if the certificate uses a weak signature aglorithm.

#### certificate_network_error*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The highest priority network error code, if the certificate has an error.

#### cipher*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Cipher name.

#### issuer*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name of the issuing CA.

#### key_exchange*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Key Exchange used by the connection, or the empty string if not applicable.

#### key_exchange_group*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

(EC)DH group used by the connection, if applicable.

#### mac*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

TLS MAC. Note that AEAD ciphers do not have separate MACs.

#### modern_ssl*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if modern SSL

#### obsolete_ssl_cipher*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if the connection is using an obsolete SSL cipher.

#### obsolete_ssl_key_exchange*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if the connection is using an obsolete SSL key exchange.

#### obsolete_ssl_protocol*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if the connection is using an obsolete SSL protocol.

#### obsolete_ssl_signature*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if the connection is using an obsolete SSL signature.

#### protocol*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Protocol name (e.g. “TLS 1.2” or “QUIC”).

#### subject_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Certificate subject name.

#### valid_from*: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

Certificate valid from date.

#### valid_to*: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

Certificate valid to (expiration) date

### *class* SafetyTipStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### BAD_REPUTATION *= 'badReputation'*

#### LOOKALIKE *= 'lookalike'*

### *class* SafetyTipInfo(safety_tip_status, safe_url=None)

* **Parameters:**
  * **safety_tip_status** ([*SafetyTipStatus*](#nodriver.cdp.security.SafetyTipStatus)) – 
  * **safe_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### safe_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The URL the safety tip suggested (“Did you mean?”). Only filled in for lookalike matches.

#### safety_tip_status*: [`SafetyTipStatus`](#nodriver.cdp.security.SafetyTipStatus)*

Describes whether the page triggers any safety tips or reputation warnings. Default is unknown.

### *class* VisibleSecurityState(security_state, security_state_issue_ids, certificate_security_state=None, safety_tip_info=None)

Security state information about the page.

* **Parameters:**
  * **security_state** ([*SecurityState*](#nodriver.cdp.security.SecurityState)) – 
  * **security_state_issue_ids** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **certificate_security_state** ([*CertificateSecurityState*](#nodriver.cdp.security.CertificateSecurityState) *|* *None*) – 
  * **safety_tip_info** ([*SafetyTipInfo*](#nodriver.cdp.security.SafetyTipInfo) *|* *None*) – 

#### certificate_security_state*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CertificateSecurityState`](#nodriver.cdp.security.CertificateSecurityState)]* *= None*

Security state details about the page certificate.

#### safety_tip_info*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SafetyTipInfo`](#nodriver.cdp.security.SafetyTipInfo)]* *= None*

The type of Safety Tip triggered on the page. Note that this field will be set even if the Safety Tip UI was not actually shown.

#### security_state*: [`SecurityState`](#nodriver.cdp.security.SecurityState)*

The security level of the page.

#### security_state_issue_ids*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Array of security state issues ids.

### *class* SecurityStateExplanation(security_state, title, summary, description, mixed_content_type, certificate, recommendations=None)

An explanation of an factor contributing to the security state.

* **Parameters:**
  * **security_state** ([*SecurityState*](#nodriver.cdp.security.SecurityState)) – 
  * **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **summary** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **mixed_content_type** ([*MixedContentType*](#nodriver.cdp.security.MixedContentType)) – 
  * **certificate** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **recommendations** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]* *|* *None*) – 

#### certificate*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Page certificate.

#### description*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Full text explanation of the factor.

#### mixed_content_type*: [`MixedContentType`](#nodriver.cdp.security.MixedContentType)*

The type of mixed content described by the explanation.

#### recommendations*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

Recommendations to fix any issues.

#### security_state*: [`SecurityState`](#nodriver.cdp.security.SecurityState)*

Security state representing the severity of the factor being explained.

#### summary*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Short phrase describing the type of factor.

#### title*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Title describing the type of factor.

### *class* InsecureContentStatus(ran_mixed_content, displayed_mixed_content, contained_mixed_form, ran_content_with_cert_errors, displayed_content_with_cert_errors, ran_insecure_content_style, displayed_insecure_content_style)

Information about insecure content on the page.

* **Parameters:**
  * **ran_mixed_content** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **displayed_mixed_content** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **contained_mixed_form** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **ran_content_with_cert_errors** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **displayed_content_with_cert_errors** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **ran_insecure_content_style** ([*SecurityState*](#nodriver.cdp.security.SecurityState)) – 
  * **displayed_insecure_content_style** ([*SecurityState*](#nodriver.cdp.security.SecurityState)) – 

#### contained_mixed_form*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Always false.

#### displayed_content_with_cert_errors*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Always false.

#### displayed_insecure_content_style*: [`SecurityState`](#nodriver.cdp.security.SecurityState)*

Always set to unknown.

#### displayed_mixed_content*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Always false.

#### ran_content_with_cert_errors*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Always false.

#### ran_insecure_content_style*: [`SecurityState`](#nodriver.cdp.security.SecurityState)*

Always set to unknown.

#### ran_mixed_content*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Always false.

### *class* CertificateErrorAction(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The action to take when a certificate error occurs. continue will continue processing the
request and cancel will cancel the request.

#### CANCEL *= 'cancel'*

#### CONTINUE *= 'continue'*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../quickstart.md#getting-started-commands).

### disable()

Disables tracking security state changes.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables tracking security state changes.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### handle_certificate_error(event_id, action)

Handles a certificate error that fired a certificateError event.

#### Deprecated
Deprecated since version 1.3.

* **Parameters:**
  * **event_id** ([`int`](https://docs.python.org/3/library/functions.html#int)) – The ID of the event.
  * **action** ([`CertificateErrorAction`](#nodriver.cdp.security.CertificateErrorAction)) – The action to take on the certificate error.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### set_ignore_certificate_errors(ignore)

Enable/disable whether all certificate errors should be ignored.

* **Parameters:**
  **ignore** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – If true, all certificate errors will be ignored.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_override_certificate_errors(override)

Enable/disable overriding certificate errors. If enabled, all certificate error events need to
be handled by the DevTools client and should be answered with `handleCertificateError` commands.

#### Deprecated
Deprecated since version 1.3.

* **Parameters:**
  **override** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – If true, certificate errors will be overridden.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* CertificateError(event_id, error_type, request_url)

There is a certificate error. If overriding certificate errors is enabled, then it should be
handled with the `handleCertificateError` command. Note: this event does not fire if the
certificate error has been allowed internally. Only one client per target should override
certificate errors at the same time.

#### Deprecated
Deprecated since version 1.3.

#### error_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The type of the error.

#### event_id*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The ID of the event.

#### request_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The url that was requested.

### *class* VisibleSecurityStateChanged(visible_security_state)

**EXPERIMENTAL**

The security state of the page changed.

* **Parameters:**
  **visible_security_state** ([*VisibleSecurityState*](#nodriver.cdp.security.VisibleSecurityState)) – 

#### visible_security_state*: [`VisibleSecurityState`](#nodriver.cdp.security.VisibleSecurityState)*

Security state information about the page.

### *class* SecurityStateChanged(security_state, scheme_is_cryptographic, explanations, insecure_content_status, summary)

The security state of the page changed. No longer being sent.

#### Deprecated
Deprecated since version 1.3.

#### explanations*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SecurityStateExplanation`](#nodriver.cdp.security.SecurityStateExplanation)]*

Previously a list of explanations for the security state. Now always
empty.

#### insecure_content_status*: [`InsecureContentStatus`](#nodriver.cdp.security.InsecureContentStatus)*

Information about insecure content on the page.

#### scheme_is_cryptographic*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if the page was loaded over cryptographic transport such as HTTPS.

#### security_state*: [`SecurityState`](#nodriver.cdp.security.SecurityState)*

Security state.

#### summary*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Overrides user-visible description of the state. Always omitted.
