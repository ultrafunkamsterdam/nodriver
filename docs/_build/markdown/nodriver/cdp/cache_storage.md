# CacheStorage

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.cache_storage"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* CacheId

Unique identifier of the Cache object.

### *class* CachedResponseType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

type of HTTP response cached

#### BASIC *= 'basic'*

#### CORS *= 'cors'*

#### DEFAULT *= 'default'*

#### ERROR *= 'error'*

#### OPAQUE_RESPONSE *= 'opaqueResponse'*

#### OPAQUE_REDIRECT *= 'opaqueRedirect'*

### *class* DataEntry(request_url, request_method, request_headers, response_time, response_status, response_status_text, response_type, response_headers)

Data entry.

#### request_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Request URL.

#### request_method*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Request method.

#### request_headers*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Header`](#nodriver.cdp.cache_storage.Header)]*

Request headers

#### response_time*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Number of seconds since epoch.

#### response_status*: [`int`](https://docs.python.org/3/library/functions.html#int)*

HTTP response status code.

#### response_status_text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

HTTP response status text.

#### response_type*: [`CachedResponseType`](#nodriver.cdp.cache_storage.CachedResponseType)*

HTTP response type

#### response_headers*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Header`](#nodriver.cdp.cache_storage.Header)]*

Response headers

### *class* Cache(cache_id, security_origin, storage_key, cache_name, storage_bucket=None)

Cache identifier.

#### cache_id*: [`CacheId`](#nodriver.cdp.cache_storage.CacheId)*

An opaque unique id of the cache.

#### security_origin*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Security origin of the cache.

#### storage_key*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Storage key of the cache.

#### cache_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The name of the cache.

#### storage_bucket*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StorageBucket`](storage.md#nodriver.cdp.storage.StorageBucket)]* *= None*

Storage bucket of the cache.

### *class* Header(name, value)

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* CachedResponse(body)

Cached response

#### body*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Entry content, base64-encoded. (Encoded as a base64 string when passed over JSON)

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### delete_cache(cache_id)

Deletes a cache.

* **Parameters:**
  **cache_id** ([`CacheId`](#nodriver.cdp.cache_storage.CacheId)) – Id of cache for deletion.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### delete_entry(cache_id, request)

Deletes a cache entry.

* **Parameters:**
  * **cache_id** ([`CacheId`](#nodriver.cdp.cache_storage.CacheId)) – Id of cache where the entry will be deleted.
  * **request** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – URL spec of the request.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### request_cache_names(security_origin=None, storage_key=None, storage_bucket=None)

Requests cache names.

* **Parameters:**
  * **security_origin** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* At least and at most one of securityOrigin, storageKey, storageBucket must be specified. Security origin.
  * **storage_key** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Storage key.
  * **storage_bucket** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StorageBucket`](storage.md#nodriver.cdp.storage.StorageBucket)]) – *(Optional)* Storage bucket. If not specified, it uses the default bucket.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Cache`](#nodriver.cdp.cache_storage.Cache)]]
* **Returns:**
  Caches for the security origin.

### request_cached_response(cache_id, request_url, request_headers)

Fetches cache entry.

* **Parameters:**
  * **cache_id** ([`CacheId`](#nodriver.cdp.cache_storage.CacheId)) – Id of cache that contains the entry.
  * **request_url** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – URL spec of the request.
  * **request_headers** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Header`](#nodriver.cdp.cache_storage.Header)]) – headers of the request.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`CachedResponse`](#nodriver.cdp.cache_storage.CachedResponse)]
* **Returns:**
  Response read from the cache.

### request_entries(cache_id, skip_count=None, page_size=None, path_filter=None)

Requests data from cache.

* **Parameters:**
  * **cache_id** ([`CacheId`](#nodriver.cdp.cache_storage.CacheId)) – ID of cache to get entries from.
  * **skip_count** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Number of records to skip.
  * **page_size** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Number of records to fetch.
  * **path_filter** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* If present, only return the entries containing this substring in the path
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`DataEntry`](#nodriver.cdp.cache_storage.DataEntry)], [`float`](https://docs.python.org/3/library/functions.html#float)]]
* **Returns:**
  A tuple with the following items:
  1. **cacheDataEntries** - Array of object store data entries.
  2. **returnCount** - Count of returned entries from this storage. If pathFilter is empty, it is the count of all entries from this storage.

## Events

*There are no events in this module.*
