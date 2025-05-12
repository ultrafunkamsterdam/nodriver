# FileSystem

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.file_system"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* File(name, last_modified, size, type_)

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### last_modified*: [`TimeSinceEpoch`](network.md#nodriver.cdp.network.TimeSinceEpoch)*

Timestamp

#### size*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Size in bytes

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* Directory(name, nested_directories, nested_files)

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### nested_directories*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### nested_files*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`File`](#nodriver.cdp.file_system.File)]*

Files that are directly nested under this directory.

### *class* BucketFileSystemLocator(storage_key, path_components, bucket_name=None)

#### storage_key*: [`SerializedStorageKey`](storage.md#nodriver.cdp.storage.SerializedStorageKey)*

Storage key

#### path_components*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

Path to the directory using each path component as an array item.

#### bucket_name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

//developer.mozilla.org/en-US/docs/Web/API/Storage_API#storage_buckets)

* **Type:**
  Bucket name. Not passing a `bucketName` will retrieve the default Bucket. (https

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### get_directory(bucket_file_system_locator)

* **Parameters:**
  **bucket_file_system_locator** ([`BucketFileSystemLocator`](#nodriver.cdp.file_system.BucketFileSystemLocator)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Directory`](#nodriver.cdp.file_system.Directory)]
* **Returns:**
  Returns the directory object at the path.

## Events

*There are no events in this module.*
