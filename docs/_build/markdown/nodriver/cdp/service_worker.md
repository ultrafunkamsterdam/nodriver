# ServiceWorker

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.service_worker"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* RegistrationID

### *class* ServiceWorkerRegistration(registration_id, scope_url, is_deleted)

ServiceWorker registration.

#### registration_id*: [`RegistrationID`](#nodriver.cdp.service_worker.RegistrationID)*

#### scope_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### is_deleted*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

### *class* ServiceWorkerVersionRunningStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### STOPPED *= 'stopped'*

#### STARTING *= 'starting'*

#### RUNNING *= 'running'*

#### STOPPING *= 'stopping'*

### *class* ServiceWorkerVersionStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### NEW *= 'new'*

#### INSTALLING *= 'installing'*

#### INSTALLED *= 'installed'*

#### ACTIVATING *= 'activating'*

#### ACTIVATED *= 'activated'*

#### REDUNDANT *= 'redundant'*

### *class* ServiceWorkerVersion(version_id, registration_id, script_url, running_status, status, script_last_modified=None, script_response_time=None, controlled_clients=None, target_id=None, router_rules=None)

ServiceWorker version.

#### version_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### registration_id*: [`RegistrationID`](#nodriver.cdp.service_worker.RegistrationID)*

#### script_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### running_status*: [`ServiceWorkerVersionRunningStatus`](#nodriver.cdp.service_worker.ServiceWorkerVersionRunningStatus)*

#### status*: [`ServiceWorkerVersionStatus`](#nodriver.cdp.service_worker.ServiceWorkerVersionStatus)*

#### script_last_modified*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

The Last-Modified header value of the main script.

#### script_response_time*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

The time at which the response headers of the main script were received from the server.
For cached script it is the last time the cache entry was validated.

#### controlled_clients*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`TargetID`](target.md#nodriver.cdp.target.TargetID)]]* *= None*

#### target_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`TargetID`](target.md#nodriver.cdp.target.TargetID)]* *= None*

#### router_rules*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

### *class* ServiceWorkerErrorMessage(error_message, registration_id, version_id, source_url, line_number, column_number)

ServiceWorker error message.

#### error_message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### registration_id*: [`RegistrationID`](#nodriver.cdp.service_worker.RegistrationID)*

#### version_id*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### source_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### line_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

#### column_number*: [`int`](https://docs.python.org/3/library/functions.html#int)*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### deliver_push_message(origin, registration_id, data)

* **Parameters:**
  * **origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **registration_id** ([`RegistrationID`](#nodriver.cdp.service_worker.RegistrationID)) – 
  * **data** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### disable()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### dispatch_periodic_sync_event(origin, registration_id, tag)

* **Parameters:**
  * **origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **registration_id** ([`RegistrationID`](#nodriver.cdp.service_worker.RegistrationID)) – 
  * **tag** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### dispatch_sync_event(origin, registration_id, tag, last_chance)

* **Parameters:**
  * **origin** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **registration_id** ([`RegistrationID`](#nodriver.cdp.service_worker.RegistrationID)) – 
  * **tag** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **last_chance** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_force_update_on_page_load(force_update_on_page_load)

* **Parameters:**
  **force_update_on_page_load** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### skip_waiting(scope_url)

* **Parameters:**
  **scope_url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### start_worker(scope_url)

* **Parameters:**
  **scope_url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### stop_all_workers()

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### stop_worker(version_id)

* **Parameters:**
  **version_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### unregister(scope_url)

* **Parameters:**
  **scope_url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### update_registration(scope_url)

* **Parameters:**
  **scope_url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* WorkerErrorReported(error_message)

#### error_message*: [`ServiceWorkerErrorMessage`](#nodriver.cdp.service_worker.ServiceWorkerErrorMessage)*

### *class* WorkerRegistrationUpdated(registrations)

#### registrations*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ServiceWorkerRegistration`](#nodriver.cdp.service_worker.ServiceWorkerRegistration)]*

### *class* WorkerVersionUpdated(versions)

#### versions*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ServiceWorkerVersion`](#nodriver.cdp.service_worker.ServiceWorkerVersion)]*
