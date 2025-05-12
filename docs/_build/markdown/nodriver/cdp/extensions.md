# Extensions

Defines commands and events for browser extensions.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.extensions"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* StorageArea(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Storage areas.

#### SESSION *= 'session'*

#### LOCAL *= 'local'*

#### SYNC *= 'sync'*

#### MANAGED *= 'managed'*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### clear_storage_items(id_, storage_area)

Clears extension storage in the given `storageArea`.

* **Parameters:**
  * **id** – ID of extension.
  * **storage_area** ([`StorageArea`](#nodriver.cdp.extensions.StorageArea)) – StorageArea to remove data from.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_storage_items(id_, storage_area, keys=None)

Gets data from extension storage in the given `storageArea`. If `keys` is
specified, these are used to filter the result.

* **Parameters:**
  * **id** – ID of extension.
  * **storage_area** ([`StorageArea`](#nodriver.cdp.extensions.StorageArea)) – StorageArea to retrieve data from.
  * **keys** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]) – *(Optional)* Keys to retrieve.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]
* **Returns:**

### load_unpacked(path)

Installs an unpacked extension from the filesystem similar to
–load-extension CLI flags. Returns extension ID once the extension
has been installed. Available if the client is connected using the
–remote-debugging-pipe flag and the –enable-unsafe-extension-debugging
flag is set.

* **Parameters:**
  **path** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Absolute file path.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**
  Extension id.

### remove_storage_items(id_, storage_area, keys)

Removes `keys` from extension storage in the given `storageArea`.

* **Parameters:**
  * **id** – ID of extension.
  * **storage_area** ([`StorageArea`](#nodriver.cdp.extensions.StorageArea)) – StorageArea to remove data from.
  * **keys** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – Keys to remove.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_storage_items(id_, storage_area, values)

Sets `values` in extension storage in the given `storageArea`. The provided `values`
will be merged with existing values in the storage area.

* **Parameters:**
  * **id** – ID of extension.
  * **storage_area** ([`StorageArea`](#nodriver.cdp.extensions.StorageArea)) – StorageArea to set data in.
  * **values** ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict)) – Values to set.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### uninstall(id_)

Uninstalls an unpacked extension (others not supported) from the profile.
Available if the client is connected using the –remote-debugging-pipe flag
and the –enable-unsafe-extension-debugging.

* **Parameters:**
  **id** – Extension id.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

*There are no events in this module.*
