# WebAuthn

This domain allows configuring virtual authenticators to test the WebAuthn
API.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.web_authn"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* AuthenticatorId

### *class* AuthenticatorProtocol(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### CTAP2 *= 'ctap2'*

#### U2F *= 'u2f'*

### *class* Ctap2Version(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### CTAP2_0 *= 'ctap2_0'*

#### CTAP2_1 *= 'ctap2_1'*

### *class* AuthenticatorTransport(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### BLE *= 'ble'*

#### CABLE *= 'cable'*

#### INTERNAL *= 'internal'*

#### NFC *= 'nfc'*

#### USB *= 'usb'*

### *class* VirtualAuthenticatorOptions(protocol, transport, ctap2_version=None, has_resident_key=None, has_user_verification=None, has_large_blob=None, has_cred_blob=None, has_min_pin_length=None, has_prf=None, automatic_presence_simulation=None, is_user_verified=None, default_backup_eligibility=None, default_backup_state=None)

* **Parameters:**
  * **protocol** ([*AuthenticatorProtocol*](#nodriver.cdp.web_authn.AuthenticatorProtocol)) – 
  * **transport** ([*AuthenticatorTransport*](#nodriver.cdp.web_authn.AuthenticatorTransport)) – 
  * **ctap2_version** ([*Ctap2Version*](#nodriver.cdp.web_authn.Ctap2Version) *|* *None*) – 
  * **has_resident_key** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **has_user_verification** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **has_large_blob** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **has_cred_blob** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **has_min_pin_length** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **has_prf** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **automatic_presence_simulation** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **is_user_verified** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **default_backup_eligibility** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **default_backup_state** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 

#### automatic_presence_simulation*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

If set to true, tests of user presence will succeed immediately.
Otherwise, they will not be resolved. Defaults to true.

#### ctap2_version*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Ctap2Version`](#nodriver.cdp.web_authn.Ctap2Version)]* *= None*

Defaults to ctap2_0. Ignored if `protocol` == u2f.

#### default_backup_eligibility*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Credentials created by this authenticator will have the backup
eligibility (BE) flag set to this value. Defaults to false.
[https://w3c.github.io/webauthn/#sctn-credential-backup](https://w3c.github.io/webauthn/#sctn-credential-backup)

#### default_backup_state*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Credentials created by this authenticator will have the backup state
(BS) flag set to this value. Defaults to false.
[https://w3c.github.io/webauthn/#sctn-credential-backup](https://w3c.github.io/webauthn/#sctn-credential-backup)

#### has_cred_blob*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

If set to true, the authenticator will support the credBlob extension.
[https://fidoalliance.org/specs/fido-v2.1-rd-20201208/fido-client-to-authenticator-protocol-v2.1-rd-20201208.html#sctn-credBlob-extension](https://fidoalliance.org/specs/fido-v2.1-rd-20201208/fido-client-to-authenticator-protocol-v2.1-rd-20201208.html#sctn-credBlob-extension)
Defaults to false.

#### has_large_blob*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

If set to true, the authenticator will support the largeBlob extension.
[https://w3c.github.io/webauthn#largeBlob](https://w3c.github.io/webauthn#largeBlob)
Defaults to false.

#### has_min_pin_length*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

If set to true, the authenticator will support the minPinLength extension.
[https://fidoalliance.org/specs/fido-v2.1-ps-20210615/fido-client-to-authenticator-protocol-v2.1-ps-20210615.html#sctn-minpinlength-extension](https://fidoalliance.org/specs/fido-v2.1-ps-20210615/fido-client-to-authenticator-protocol-v2.1-ps-20210615.html#sctn-minpinlength-extension)
Defaults to false.

#### has_prf*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

If set to true, the authenticator will support the prf extension.
[https://w3c.github.io/webauthn/#prf-extension](https://w3c.github.io/webauthn/#prf-extension)
Defaults to false.

#### has_resident_key*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Defaults to false.

#### has_user_verification*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Defaults to false.

#### is_user_verified*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Sets whether User Verification succeeds or fails for an authenticator.
Defaults to false.

#### protocol*: [`AuthenticatorProtocol`](#nodriver.cdp.web_authn.AuthenticatorProtocol)*

#### transport*: [`AuthenticatorTransport`](#nodriver.cdp.web_authn.AuthenticatorTransport)*

### *class* Credential(credential_id, is_resident_credential, private_key, sign_count, rp_id=None, user_handle=None, large_blob=None)

* **Parameters:**
  * **credential_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **is_resident_credential** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **private_key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **sign_count** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **rp_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **user_handle** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **large_blob** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### credential_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### is_resident_credential*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### large_blob*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The large blob associated with the credential.
See [https://w3c.github.io/webauthn/#sctn-large-blob-extension](https://w3c.github.io/webauthn/#sctn-large-blob-extension) (Encoded as a base64 string when passed over JSON)

#### private_key*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The ECDSA P-256 private key in PKCS#8 format. (Encoded as a base64 string when passed over JSON)

#### rp_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Relying Party ID the credential is scoped to. Must be set when adding a
credential.

#### sign_count*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Signature counter. This is incremented by one for each successful
assertion.
See [https://w3c.github.io/webauthn/#signature-counter](https://w3c.github.io/webauthn/#signature-counter)

#### user_handle*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

An opaque byte sequence with a maximum size of 64 bytes mapping the
credential to a specific user. (Encoded as a base64 string when passed over JSON)

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../quickstart.md#getting-started-commands).

### add_credential(authenticator_id, credential)

Adds the credential to the specified authenticator.

* **Parameters:**
  * **authenticator_id** ([`AuthenticatorId`](#nodriver.cdp.web_authn.AuthenticatorId)) – 
  * **credential** ([`Credential`](#nodriver.cdp.web_authn.Credential)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### add_virtual_authenticator(options)

Creates and adds a virtual authenticator.

* **Parameters:**
  **options** ([`VirtualAuthenticatorOptions`](#nodriver.cdp.web_authn.VirtualAuthenticatorOptions)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`AuthenticatorId`](#nodriver.cdp.web_authn.AuthenticatorId)]
* **Returns:**

### clear_credentials(authenticator_id)

Clears all the credentials from the specified device.

* **Parameters:**
  **authenticator_id** ([`AuthenticatorId`](#nodriver.cdp.web_authn.AuthenticatorId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### disable()

Disable the WebAuthn domain.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable(enable_ui=None)

Enable the WebAuthn domain and start intercepting credential storage and
retrieval with a virtual authenticator.

* **Parameters:**
  **enable_ui** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to enable the WebAuthn user interface. Enabling the UI is recommended for debugging and demo purposes, as it is closer to the real experience. Disabling the UI is recommended for automated testing. Supported at the embedder’s discretion if UI is available. Defaults to false.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_credential(authenticator_id, credential_id)

Returns a single credential stored in the given virtual authenticator that
matches the credential ID.

* **Parameters:**
  * **authenticator_id** ([`AuthenticatorId`](#nodriver.cdp.web_authn.AuthenticatorId)) – 
  * **credential_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Credential`](#nodriver.cdp.web_authn.Credential)]
* **Returns:**

### get_credentials(authenticator_id)

Returns all the credentials stored in the given virtual authenticator.

* **Parameters:**
  **authenticator_id** ([`AuthenticatorId`](#nodriver.cdp.web_authn.AuthenticatorId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Credential`](#nodriver.cdp.web_authn.Credential)]]
* **Returns:**

### remove_credential(authenticator_id, credential_id)

Removes a credential from the authenticator.

* **Parameters:**
  * **authenticator_id** ([`AuthenticatorId`](#nodriver.cdp.web_authn.AuthenticatorId)) – 
  * **credential_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### remove_virtual_authenticator(authenticator_id)

Removes the given authenticator.

* **Parameters:**
  **authenticator_id** ([`AuthenticatorId`](#nodriver.cdp.web_authn.AuthenticatorId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_automatic_presence_simulation(authenticator_id, enabled)

Sets whether tests of user presence will succeed immediately (if true) or fail to resolve (if false) for an authenticator.
The default is true.

* **Parameters:**
  * **authenticator_id** ([`AuthenticatorId`](#nodriver.cdp.web_authn.AuthenticatorId)) – 
  * **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_response_override_bits(authenticator_id, is_bogus_signature=None, is_bad_uv=None, is_bad_up=None)

Resets parameters isBogusSignature, isBadUV, isBadUP to false if they are not present.

* **Parameters:**
  * **authenticator_id** ([`AuthenticatorId`](#nodriver.cdp.web_authn.AuthenticatorId)) – 
  * **is_bogus_signature** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If isBogusSignature is set, overrides the signature in the authenticator response to be zero. Defaults to false.
  * **is_bad_uv** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If isBadUV is set, overrides the UV bit in the flags in the authenticator response to be zero. Defaults to false.
  * **is_bad_up** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If isBadUP is set, overrides the UP bit in the flags in the authenticator response to be zero. Defaults to false.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_user_verified(authenticator_id, is_user_verified)

Sets whether User Verification succeeds or fails for an authenticator.
The default is true.

* **Parameters:**
  * **authenticator_id** ([`AuthenticatorId`](#nodriver.cdp.web_authn.AuthenticatorId)) – 
  * **is_user_verified** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* CredentialAdded(authenticator_id, credential)

Triggered when a credential is added to an authenticator.

* **Parameters:**
  * **authenticator_id** ([*AuthenticatorId*](#nodriver.cdp.web_authn.AuthenticatorId)) – 
  * **credential** ([*Credential*](#nodriver.cdp.web_authn.Credential)) – 

#### authenticator_id*: [`AuthenticatorId`](#nodriver.cdp.web_authn.AuthenticatorId)*

#### credential*: [`Credential`](#nodriver.cdp.web_authn.Credential)*

### *class* CredentialAsserted(authenticator_id, credential)

Triggered when a credential is used in a webauthn assertion.

* **Parameters:**
  * **authenticator_id** ([*AuthenticatorId*](#nodriver.cdp.web_authn.AuthenticatorId)) – 
  * **credential** ([*Credential*](#nodriver.cdp.web_authn.Credential)) – 

#### authenticator_id*: [`AuthenticatorId`](#nodriver.cdp.web_authn.AuthenticatorId)*

#### credential*: [`Credential`](#nodriver.cdp.web_authn.Credential)*
