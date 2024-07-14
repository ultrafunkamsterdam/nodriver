# IndexedDB

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.indexed_db"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* DatabaseWithObjectStores(name, version, object_stores)

Database with an array of object stores.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Database name.

#### version*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Database version (type is not ‘integer’, as the standard
requires the version number to be ‘unsigned long long’)

#### object_stores*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ObjectStore`](#nodriver.cdp.indexed_db.ObjectStore)]*

Object stores in this database.

### *class* ObjectStore(name, key_path, auto_increment, indexes)

Object store.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Object store name.

#### key_path*: [`KeyPath`](#nodriver.cdp.indexed_db.KeyPath)*

Object store key path.

#### auto_increment*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

If true, object store has auto increment flag set.

#### indexes*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ObjectStoreIndex`](#nodriver.cdp.indexed_db.ObjectStoreIndex)]*

Indexes in this object store.

### *class* ObjectStoreIndex(name, key_path, unique, multi_entry)

Object store index.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Index name.

#### key_path*: [`KeyPath`](#nodriver.cdp.indexed_db.KeyPath)*

Index key path.

#### unique*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

If true, index is unique.

#### multi_entry*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

If true, index allows multiple entries for a key.

### *class* Key(type_, number=None, string=None, date=None, array=None)

Key.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Key type.

#### number*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Number value.

#### string*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

String value.

#### date*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Date value.

#### array*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Key`](#nodriver.cdp.indexed_db.Key)]]* *= None*

Array value.

### *class* KeyRange(lower_open, upper_open, lower=None, upper=None)

Key range.

#### lower_open*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

If true lower bound is open.

#### upper_open*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

If true upper bound is open.

#### lower*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Key`](#nodriver.cdp.indexed_db.Key)]* *= None*

Lower bound.

#### upper*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Key`](#nodriver.cdp.indexed_db.Key)]* *= None*

Upper bound.

### *class* DataEntry(key, primary_key, value)

Data entry.

#### key*: [`RemoteObject`](runtime.md#nodriver.cdp.runtime.RemoteObject)*

Key object.

#### primary_key*: [`RemoteObject`](runtime.md#nodriver.cdp.runtime.RemoteObject)*

Primary key object.

#### value*: [`RemoteObject`](runtime.md#nodriver.cdp.runtime.RemoteObject)*

Value object.

### *class* KeyPath(type_, string=None, array=None)

Key path.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Key path type.

#### string*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

String value.

#### array*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

Array value.

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### clear_object_store(database_name, object_store_name, security_origin=None, storage_key=None, storage_bucket=None)

Clears all entries from an object store.

* **Parameters:**
  * **security_origin** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin.
  * **storage_key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Storage key.
  * **storage_bucket** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StorageBucket`](storage.md#nodriver.cdp.storage.StorageBucket)]) – *(Optional)* Storage bucket. If not specified, it uses the default bucket.
  * **database_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Database name.
  * **object_store_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Object store name.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### delete_database(database_name, security_origin=None, storage_key=None, storage_bucket=None)

Deletes a database.

* **Parameters:**
  * **security_origin** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin.
  * **storage_key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Storage key.
  * **storage_bucket** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StorageBucket`](storage.md#nodriver.cdp.storage.StorageBucket)]) – *(Optional)* Storage bucket. If not specified, it uses the default bucket.
  * **database_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Database name.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### delete_object_store_entries(database_name, object_store_name, key_range, security_origin=None, storage_key=None, storage_bucket=None)

Delete a range of entries from an object store

* **Parameters:**
  * **security_origin** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin.
  * **storage_key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Storage key.
  * **storage_bucket** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StorageBucket`](storage.md#nodriver.cdp.storage.StorageBucket)]) – *(Optional)* Storage bucket. If not specified, it uses the default bucket.
  * **database_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **object_store_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **key_range** ([`KeyRange`](#nodriver.cdp.indexed_db.KeyRange)) – Range of entry keys to delete
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### disable()

Disables events from backend.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables events from backend.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_metadata(database_name, object_store_name, security_origin=None, storage_key=None, storage_bucket=None)

Gets metadata of an object store.

* **Parameters:**
  * **security_origin** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin.
  * **storage_key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Storage key.
  * **storage_bucket** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StorageBucket`](storage.md#nodriver.cdp.storage.StorageBucket)]) – *(Optional)* Storage bucket. If not specified, it uses the default bucket.
  * **database_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Database name.
  * **object_store_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Object store name.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`float`](https://docs.python.org/3/library/functions.html#float), [`float`](https://docs.python.org/3/library/functions.html#float)]]
* **Returns:**
  A tuple with the following items:
  1. **entriesCount** - the entries count
  2. **keyGeneratorValue** - the current value of key generator, to become the next inserted key into the object store. Valid if objectStore.autoIncrement is true.

### request_data(database_name, object_store_name, index_name, skip_count, page_size, security_origin=None, storage_key=None, storage_bucket=None, key_range=None)

Requests data from object store or index.

* **Parameters:**
  * **security_origin** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin.
  * **storage_key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Storage key.
  * **storage_bucket** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StorageBucket`](storage.md#nodriver.cdp.storage.StorageBucket)]) – *(Optional)* Storage bucket. If not specified, it uses the default bucket.
  * **database_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Database name.
  * **object_store_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Object store name.
  * **index_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Index name, empty string for object store data requests.
  * **skip_count** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Number of records to skip.
  * **page_size** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Number of records to fetch.
  * **key_range** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`KeyRange`](#nodriver.cdp.indexed_db.KeyRange)]) – *(Optional)* Key range.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`DataEntry`](#nodriver.cdp.indexed_db.DataEntry)], [`bool`](https://docs.python.org/3/library/functions.html#bool)]]
* **Returns:**
  A tuple with the following items:
  1. **objectStoreDataEntries** - Array of object store data entries.
  2. **hasMore** - If true, there are more entries to fetch in the given range.

### request_database(database_name, security_origin=None, storage_key=None, storage_bucket=None)

Requests database with given name in given frame.

* **Parameters:**
  * **security_origin** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin.
  * **storage_key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Storage key.
  * **storage_bucket** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StorageBucket`](storage.md#nodriver.cdp.storage.StorageBucket)]) – *(Optional)* Storage bucket. If not specified, it uses the default bucket.
  * **database_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Database name.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`DatabaseWithObjectStores`](#nodriver.cdp.indexed_db.DatabaseWithObjectStores)]
* **Returns:**
  Database with an array of object stores.

### request_database_names(security_origin=None, storage_key=None, storage_bucket=None)

Requests database names for given security origin.

* **Parameters:**
  * **security_origin** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin.
  * **storage_key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Storage key.
  * **storage_bucket** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StorageBucket`](storage.md#nodriver.cdp.storage.StorageBucket)]) – *(Optional)* Storage bucket. If not specified, it uses the default bucket.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**
  Database names for origin.

## Events

*There are no events in this module.*
