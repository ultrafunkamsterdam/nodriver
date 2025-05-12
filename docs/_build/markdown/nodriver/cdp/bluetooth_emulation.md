# BluetoothEmulation

This domain allows configuring virtual Bluetooth devices to test
the web-bluetooth API.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.bluetooth_emulation"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* CentralState(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Indicates the various states of Central.

#### ABSENT *= 'absent'*

#### POWERED_OFF *= 'powered-off'*

#### POWERED_ON *= 'powered-on'*

### *class* GATTOperationType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Indicates the various types of GATT event.

#### CONNECTION *= 'connection'*

#### DISCOVERY *= 'discovery'*

### *class* ManufacturerData(key, data)

Stores the manufacturer data

#### key*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Company identifier
[https://bitbucket.org/bluetooth-SIG/public/src/main/assigned_numbers/company_identifiers/company_identifiers.yaml](https://bitbucket.org/bluetooth-SIG/public/src/main/assigned_numbers/company_identifiers/company_identifiers.yaml)
[https://usb.org/developers](https://usb.org/developers)

#### data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Manufacturer-specific data (Encoded as a base64 string when passed over JSON)

### *class* ScanRecord(name=None, uuids=None, appearance=None, tx_power=None, manufacturer_data=None)

Stores the byte data of the advertisement packet sent by a Bluetooth device.

#### name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### uuids*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

#### appearance*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Stores the external appearance description of the device.

#### tx_power*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Stores the transmission power of a broadcasting device.

#### manufacturer_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ManufacturerData`](#nodriver.cdp.bluetooth_emulation.ManufacturerData)]]* *= None*

Key is the company identifier and the value is an array of bytes of
manufacturer specific data.

### *class* ScanEntry(device_address, rssi, scan_record)

Stores the advertisement packet information that is sent by a Bluetooth device.

#### device_address*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### rssi*: [`int`](https://docs.python.org/3/library/functions.html#int)*

#### scan_record*: [`ScanRecord`](#nodriver.cdp.bluetooth_emulation.ScanRecord)*

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

Disable the BluetoothEmulation domain.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable(state, le_supported)

Enable the BluetoothEmulation domain.

* **Parameters:**
  * **state** ([`CentralState`](#nodriver.cdp.bluetooth_emulation.CentralState)) – State of the simulated central.
  * **le_supported** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – If the simulated central supports low-energy.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_simulated_central_state(state)

Set the state of the simulated central.

* **Parameters:**
  **state** ([`CentralState`](#nodriver.cdp.bluetooth_emulation.CentralState)) – State of the simulated central.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### simulate_advertisement(entry)

Simulates an advertisement packet described in `entry` being received by
the central.

* **Parameters:**
  **entry** ([`ScanEntry`](#nodriver.cdp.bluetooth_emulation.ScanEntry)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### simulate_gatt_operation_response(address, type_, code)

Simulates the response code from the peripheral with `address` for a
GATT operation of `type`. The `code` value follows the HCI Error Codes from
Bluetooth Core Specification Vol 2 Part D 1.3 List Of Error Codes.

* **Parameters:**
  * **address** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **type** – 
  * **code** ([`int`](https://docs.python.org/3/library/functions.html#int)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### simulate_preconnected_peripheral(address, name, manufacturer_data, known_service_uuids)

Simulates a peripheral with `address`, `name` and `knownServiceUuids`
that has already been connected to the system.

* **Parameters:**
  * **address** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **manufacturer_data** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ManufacturerData`](#nodriver.cdp.bluetooth_emulation.ManufacturerData)]) – 
  * **known_service_uuids** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* GattOperationReceived(address, type_)

Event for when a GATT operation of `type` to the peripheral with `address`
happened.

#### address*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### type_*: [`GATTOperationType`](#nodriver.cdp.bluetooth_emulation.GATTOperationType)*
