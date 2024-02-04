# Database

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.database"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* DatabaseId

Unique identifier of Database object.

### *class* Database(id_, domain, name, version)

Database object.

* **Parameters:**
  * **id_** ([*DatabaseId*](#nodriver.cdp.database.DatabaseId)) – 
  * **domain** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### domain*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Database domain.

#### id_*: [`DatabaseId`](#nodriver.cdp.database.DatabaseId)*

Database ID.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Database name.

#### version*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Database version.

### *class* Error(message, code)

Database error.

* **Parameters:**
  * **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **code** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 

#### code*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Error code.

#### message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Error message.

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

Disables database tracking, prevents database events from being sent to the client.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables database tracking, database events will now be delivered to the client.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### execute_sql(database_id, query)

* **Parameters:**
  * **database_id** ([`DatabaseId`](#nodriver.cdp.database.DatabaseId)) – 
  * **query** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Error`](#nodriver.cdp.database.Error)]]]
* **Returns:**
  A tuple with the following items:
  1. **columnNames** -
  2. **values** -
  3. **sqlError** -

### get_database_table_names(database_id)

* **Parameters:**
  **database_id** ([`DatabaseId`](#nodriver.cdp.database.DatabaseId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* AddDatabase(database)

* **Parameters:**
  **database** ([*Database*](#nodriver.cdp.database.Database)) – 

#### database*: [`Database`](#nodriver.cdp.database.Database)*
