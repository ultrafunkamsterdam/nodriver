# Extensions

Defines commands and events for browser extensions. Available if the client
is connected using the –remote-debugging-pipe flag and
the –enable-unsafe-extension-debugging flag is set.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.extensions"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

*There are no types in this module.*

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### load_unpacked(path)

Installs an unpacked extension from the filesystem similar to
–load-extension CLI flags. Returns extension ID once the extension
has been installed.

* **Parameters:**
  **path** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Absolute file path.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**
  Extension id.

## Events

*There are no events in this module.*
