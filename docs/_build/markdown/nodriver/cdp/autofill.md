# Autofill

Defines commands and events for Autofill.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.autofill"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* CreditCard(number, name, expiry_month, expiry_year, cvc)

#### number*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

16-digit credit card number.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Name of the credit card owner.

#### expiry_month*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

2-digit expiry month.

#### expiry_year*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

4-digit expiry year.

#### cvc*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

3-digit card verification code.

### *class* AddressField(name, value)

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

address field name, for example GIVEN_NAME.

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

address field value, for example Jon Doe.

### *class* AddressFields(fields)

A list of address fields.

#### fields*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AddressField`](#nodriver.cdp.autofill.AddressField)]*

### *class* Address(fields)

#### fields*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AddressField`](#nodriver.cdp.autofill.AddressField)]*

fields and values defining an address.

### *class* AddressUI(address_fields)

Defines how an address can be displayed like in chrome://settings/addresses.
Address UI is a two dimensional array, each inner array is an “address information line”, and when rendered in a UI surface should be displayed as such.
The following address UI for instance:
[[{name: “GIVE_NAME”, value: “Jon”}, {name: “FAMILY_NAME”, value: “Doe”}], [{name: “CITY”, value: “Munich”}, {name: “ZIP”, value: “81456”}]]
should allow the receiver to render:
Jon Doe
Munich 81456

#### address_fields*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AddressFields`](#nodriver.cdp.autofill.AddressFields)]*

A two dimension array containing the representation of values from an address profile.

### *class* FillingStrategy(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Specified whether a filled field was done so by using the html autocomplete attribute or autofill heuristics.

#### AUTOCOMPLETE_ATTRIBUTE *= 'autocompleteAttribute'*

#### AUTOFILL_INFERRED *= 'autofillInferred'*

### *class* FilledField(html_type, id_, name, value, autofill_type, filling_strategy, frame_id, field_id)

#### html_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The type of the field, e.g text, password etc.

#### id_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

the html id

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

the html name

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

the field value

#### autofill_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The actual field type, e.g FAMILY_NAME

#### filling_strategy*: [`FillingStrategy`](#nodriver.cdp.autofill.FillingStrategy)*

The filling strategy

#### frame_id*: [`FrameId`](page.md#nodriver.cdp.page.FrameId)*

The frame the field belongs to

#### field_id*: [`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)*

The form field’s DOM node

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

Disables autofill domain notifications.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables autofill domain notifications.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_addresses(addresses)

Set addresses so that developers can verify their forms implementation.

* **Parameters:**
  **addresses** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Address`](#nodriver.cdp.autofill.Address)]) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### trigger(field_id, card, frame_id=None)

Trigger autofill on a form identified by the fieldId.
If the field and related form cannot be autofilled, returns an error.

* **Parameters:**
  * **field_id** ([`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)) – Identifies a field that serves as an anchor for autofill.
  * **frame_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]) – *(Optional)* Identifies the frame that field belongs to.
  * **card** ([`CreditCard`](#nodriver.cdp.autofill.CreditCard)) – Credit card information to fill out the form. Credit card data is not saved.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* AddressFormFilled(filled_fields, address_ui)

Emitted when an address form is filled.

#### filled_fields*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`FilledField`](#nodriver.cdp.autofill.FilledField)]*

Information about the fields that were filled

#### address_ui*: [`AddressUI`](#nodriver.cdp.autofill.AddressUI)*

An UI representation of the address used to fill the form.
Consists of a 2D array where each child represents an address/profile line.
