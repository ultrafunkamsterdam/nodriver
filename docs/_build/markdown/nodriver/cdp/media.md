# Media

This domain allows detailed inspection of media elements

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.media"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* PlayerId

Players will get an ID that is unique within the agent context.

### *class* Timestamp(x=0, /)

### *class* PlayerMessage(level, message)

Have one type per entry in MediaLogRecord::Type
Corresponds to kMessage

#### level*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Keep in sync with MediaLogMessageLevel
We are currently keeping the message level ‘error’ separate from the
PlayerError type because right now they represent different things,
this one being a DVLOG(ERROR) style log message that gets printed
based on what log level is selected in the UI, and the other is a
representation of a media::PipelineStatus object. Soon however we’re
going to be moving away from using PipelineStatus for errors and
introducing a new error type which should hopefully let us integrate
the error log level into the PlayerError type.

#### message*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* PlayerProperty(name, value)

Corresponds to kMediaPropertyChange

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* PlayerEvent(timestamp, value)

Corresponds to kMediaEventTriggered

#### timestamp*: [`Timestamp`](#nodriver.cdp.media.Timestamp)*

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* PlayerErrorSourceLocation(file, line)

Represents logged source line numbers reported in an error.
NOTE: file and line are from chromium c++ implementation code, not js.

#### file*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### line*: [`int`](https://docs.python.org/3/library/functions.html#int)*

### *class* PlayerError(error_type, code, stack, cause, data)

Corresponds to kMediaError

#### error_type*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### code*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Code is the numeric enum entry for a specific set of error codes, such
as PipelineStatusCodes in media/base/pipeline_status.h

#### stack*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PlayerErrorSourceLocation`](#nodriver.cdp.media.PlayerErrorSourceLocation)]*

A trace of where this error was caused / where it passed through.

#### cause*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PlayerError`](#nodriver.cdp.media.PlayerError)]*

Errors potentially have a root cause error, ie, a DecoderError might be
caused by an WindowsError

#### data*: [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)*

Extra data attached to an error, such as an HRESULT, Video Codec, etc.

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

Disables the Media domain.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables the Media domain

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* PlayerPropertiesChanged(player_id, properties)

This can be called multiple times, and can be used to set / override /
remove player properties. A null propValue indicates removal.

#### player_id*: [`PlayerId`](#nodriver.cdp.media.PlayerId)*

#### properties*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PlayerProperty`](#nodriver.cdp.media.PlayerProperty)]*

### *class* PlayerEventsAdded(player_id, events)

Send events as a list, allowing them to be batched on the browser for less
congestion. If batched, events must ALWAYS be in chronological order.

#### player_id*: [`PlayerId`](#nodriver.cdp.media.PlayerId)*

#### events*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PlayerEvent`](#nodriver.cdp.media.PlayerEvent)]*

### *class* PlayerMessagesLogged(player_id, messages)

Send a list of any messages that need to be delivered.

#### player_id*: [`PlayerId`](#nodriver.cdp.media.PlayerId)*

#### messages*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PlayerMessage`](#nodriver.cdp.media.PlayerMessage)]*

### *class* PlayerErrorsRaised(player_id, errors)

Send a list of any errors that need to be delivered.

#### player_id*: [`PlayerId`](#nodriver.cdp.media.PlayerId)*

#### errors*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PlayerError`](#nodriver.cdp.media.PlayerError)]*

### *class* PlayersCreated(players)

Called whenever a player is created, or when a new agent joins and receives
a list of active players. If an agent is restored, it will receive the full
list of player ids and all events again.

#### players*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PlayerId`](#nodriver.cdp.media.PlayerId)]*
