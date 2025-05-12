# FedCm

This domain allows interacting with the FedCM dialog.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.fed_cm"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* LoginState(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Whether this is a sign-up or sign-in action for this account, i.e.
whether this account has ever been used to sign in to this RP before.

#### SIGN_IN *= 'SignIn'*

#### SIGN_UP *= 'SignUp'*

### *class* DialogType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The types of FedCM dialogs.

#### ACCOUNT_CHOOSER *= 'AccountChooser'*

#### AUTO_REAUTHN *= 'AutoReauthn'*

#### CONFIRM_IDP_LOGIN *= 'ConfirmIdpLogin'*

#### ERROR *= 'Error'*

### *class* DialogButton(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The buttons on the FedCM dialog.

#### CONFIRM_IDP_LOGIN_CONTINUE *= 'ConfirmIdpLoginContinue'*

#### ERROR_GOT_IT *= 'ErrorGotIt'*

#### ERROR_MORE_DETAILS *= 'ErrorMoreDetails'*

### *class* AccountUrlType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The URLs that each account has

#### TERMS_OF_SERVICE *= 'TermsOfService'*

#### PRIVACY_POLICY *= 'PrivacyPolicy'*

### *class* Account(account_id, email, name, given_name, picture_url, idp_config_url, idp_login_url, login_state, terms_of_service_url=None, privacy_policy_url=None)

Corresponds to IdentityRequestAccount

#### account_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### email*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### given_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### picture_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### idp_config_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### idp_login_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### login_state*: [`LoginState`](#nodriver.cdp.fed_cm.LoginState)*

#### terms_of_service_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

These two are only set if the loginState is signUp

#### privacy_policy_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### click_dialog_button(dialog_id, dialog_button)

* **Parameters:**
  * **dialog_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **dialog_button** ([`DialogButton`](#nodriver.cdp.fed_cm.DialogButton)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### disable()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### dismiss_dialog(dialog_id, trigger_cooldown=None)

* **Parameters:**
  * **dialog_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **trigger_cooldown** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)*
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable(disable_rejection_delay=None)

* **Parameters:**
  **disable_rejection_delay** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Allows callers to disable the promise rejection delay that would normally happen, if this is unimportant to what’s being tested. (step 4 of [https://fedidcg.github.io/FedCM/#browser-api-rp-sign-in](https://fedidcg.github.io/FedCM/#browser-api-rp-sign-in))
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### open_url(dialog_id, account_index, account_url_type)

* **Parameters:**
  * **dialog_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **account_index** ([`int`](https://docs.python.org/3/library/functions.html#int)) – 
  * **account_url_type** ([`AccountUrlType`](#nodriver.cdp.fed_cm.AccountUrlType)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### reset_cooldown()

Resets the cooldown time, if any, to allow the next FedCM call to show
a dialog even if one was recently dismissed by the user.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### select_account(dialog_id, account_index)

* **Parameters:**
  * **dialog_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **account_index** ([`int`](https://docs.python.org/3/library/functions.html#int)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* DialogShown(dialog_id, dialog_type, accounts, title, subtitle)

#### dialog_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### dialog_type*: [`DialogType`](#nodriver.cdp.fed_cm.DialogType)*

#### accounts*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Account`](#nodriver.cdp.fed_cm.Account)]*

#### title*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

These exist primarily so that the caller can verify the
RP context was used appropriately.

#### subtitle*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

### *class* DialogClosed(dialog_id)

Triggered when a dialog is closed, either by user action, JS abort,
or a command below.

#### dialog_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*
