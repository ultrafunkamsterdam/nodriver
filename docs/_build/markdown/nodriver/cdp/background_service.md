# BackgroundService

Defines events for background web platform features.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.background_service"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* ServiceName(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

The Background Service that will be associated with the commands/events.
Every Background Service operates independently, but they share the same
API.

#### BACKGROUND_FETCH *= 'backgroundFetch'*

#### BACKGROUND_SYNC *= 'backgroundSync'*

#### PUSH_MESSAGING *= 'pushMessaging'*

#### NOTIFICATIONS *= 'notifications'*

#### PAYMENT_HANDLER *= 'paymentHandler'*

#### PERIODIC_BACKGROUND_SYNC *= 'periodicBackgroundSync'*

### *class* EventMetadata(key, value)

A key-value pair for additional event information to pass along.

#### key*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* BackgroundServiceEvent(timestamp, origin, service_worker_registration_id, service, event_name, instance_id, event_metadata, storage_key)

#### timestamp*: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

Timestamp of the event (in seconds).

#### origin*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The origin this event belongs to.

#### service_worker_registration_id*: [`RegistrationID`](service_worker.md#nodriver.cdp.service_worker.RegistrationID)*

The Service Worker ID that initiated the event.

#### service*: [`ServiceName`](#nodriver.cdp.background_service.ServiceName)*

The Background Service this event belongs to.

#### event_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

A description of the event.

#### instance_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

An identifier that groups related events together.

#### event_metadata*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`EventMetadata`](#nodriver.cdp.background_service.EventMetadata)]*

A list of event-specific information.

#### storage_key*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Storage key this event belongs to.

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### clear_events(service)

Clears all stored data for the service.

* **Parameters:**
  **service** ([`ServiceName`](#nodriver.cdp.background_service.ServiceName)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_recording(should_record, service)

Set the recording state for the service.

* **Parameters:**
  * **should_record** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
  * **service** ([`ServiceName`](#nodriver.cdp.background_service.ServiceName)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### start_observing(service)

Enables event updates for the service.

* **Parameters:**
  **service** ([`ServiceName`](#nodriver.cdp.background_service.ServiceName)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### stop_observing(service)

Disables event updates for the service.

* **Parameters:**
  **service** ([`ServiceName`](#nodriver.cdp.background_service.ServiceName)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* RecordingStateChanged(is_recording, service)

Called when the recording state for the service has been updated.

#### is_recording*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### service*: [`ServiceName`](#nodriver.cdp.background_service.ServiceName)*

### *class* BackgroundServiceEventReceived(background_service_event)

Called with all existing backgroundServiceEvents when enabled, and all new
events afterwards if enabled and recording.

#### background_service_event*: [`BackgroundServiceEvent`](#nodriver.cdp.background_service.BackgroundServiceEvent)*
