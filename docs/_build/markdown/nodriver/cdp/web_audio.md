# WebAudio

This domain allows inspection of Web Audio API.
[https://webaudio.github.io/web-audio-api/](https://webaudio.github.io/web-audio-api/)

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.web_audio"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* GraphObjectId

An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in Web Audio API

### *class* ContextType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of BaseAudioContext types

#### REALTIME *= 'realtime'*

#### OFFLINE *= 'offline'*

### *class* ContextState(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of AudioContextState from the spec

#### SUSPENDED *= 'suspended'*

#### RUNNING *= 'running'*

#### CLOSED *= 'closed'*

#### INTERRUPTED *= 'interrupted'*

### *class* NodeType

Enum of AudioNode types

### *class* ChannelCountMode(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of AudioNode::ChannelCountMode from the spec

#### CLAMPED_MAX *= 'clamped-max'*

#### EXPLICIT *= 'explicit'*

#### MAX_ *= 'max'*

### *class* ChannelInterpretation(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of AudioNode::ChannelInterpretation from the spec

#### DISCRETE *= 'discrete'*

#### SPEAKERS *= 'speakers'*

### *class* ParamType

Enum of AudioParam types

### *class* AutomationRate(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of AudioParam::AutomationRate from the spec

#### A_RATE *= 'a-rate'*

#### K_RATE *= 'k-rate'*

### *class* ContextRealtimeData(current_time, render_capacity, callback_interval_mean, callback_interval_variance)

Fields in AudioContext that change in real-time.

#### current_time*: [`float`](https://docs.python.org/3/library/functions.html#float)*

The current context time in second in BaseAudioContext.

#### render_capacity*: [`float`](https://docs.python.org/3/library/functions.html#float)*

The time spent on rendering graph divided by render quantum duration,
and multiplied by 100. 100 means the audio renderer reached the full
capacity and glitch may occur.

#### callback_interval_mean*: [`float`](https://docs.python.org/3/library/functions.html#float)*

A running mean of callback interval.

#### callback_interval_variance*: [`float`](https://docs.python.org/3/library/functions.html#float)*

A running variance of callback interval.

### *class* BaseAudioContext(context_id, context_type, context_state, callback_buffer_size, max_output_channel_count, sample_rate, realtime_data=None)

Protocol object for BaseAudioContext

#### context_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### context_type*: [`ContextType`](#nodriver.cdp.web_audio.ContextType)*

#### context_state*: [`ContextState`](#nodriver.cdp.web_audio.ContextState)*

#### callback_buffer_size*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Platform-dependent callback buffer size.

#### max_output_channel_count*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Number of output channels supported by audio hardware in use.

#### sample_rate*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Context sample rate.

#### realtime_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ContextRealtimeData`](#nodriver.cdp.web_audio.ContextRealtimeData)]* *= None*

### *class* AudioListener(listener_id, context_id)

Protocol object for AudioListener

#### listener_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### context_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

### *class* AudioNode(node_id, context_id, node_type, number_of_inputs, number_of_outputs, channel_count, channel_count_mode, channel_interpretation)

Protocol object for AudioNode

#### node_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### context_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### node_type*: [`NodeType`](#nodriver.cdp.web_audio.NodeType)*

#### number_of_inputs*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### number_of_outputs*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### channel_count*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### channel_count_mode*: [`ChannelCountMode`](#nodriver.cdp.web_audio.ChannelCountMode)*

#### channel_interpretation*: [`ChannelInterpretation`](#nodriver.cdp.web_audio.ChannelInterpretation)*

### *class* AudioParam(param_id, node_id, context_id, param_type, rate, default_value, min_value, max_value)

Protocol object for AudioParam

#### param_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### node_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### context_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### param_type*: [`ParamType`](#nodriver.cdp.web_audio.ParamType)*

#### rate*: [`AutomationRate`](#nodriver.cdp.web_audio.AutomationRate)*

#### default_value*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### min_value*: [`float`](https://docs.python.org/3/library/functions.html#float)*

#### max_value*: [`float`](https://docs.python.org/3/library/functions.html#float)*

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

Disables the WebAudio domain.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables the WebAudio domain and starts sending context lifetime events.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_realtime_data(context_id)

Fetch the realtime data from the registered contexts.

* **Parameters:**
  **context_id** ([`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`ContextRealtimeData`](#nodriver.cdp.web_audio.ContextRealtimeData)]
* **Returns:**

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* ContextCreated(context)

Notifies that a new BaseAudioContext has been created.

#### context*: [`BaseAudioContext`](#nodriver.cdp.web_audio.BaseAudioContext)*

### *class* ContextWillBeDestroyed(context_id)

Notifies that an existing BaseAudioContext will be destroyed.

#### context_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

### *class* ContextChanged(context)

Notifies that existing BaseAudioContext has changed some properties (id stays the same)..

#### context*: [`BaseAudioContext`](#nodriver.cdp.web_audio.BaseAudioContext)*

### *class* AudioListenerCreated(listener)

Notifies that the construction of an AudioListener has finished.

#### listener*: [`AudioListener`](#nodriver.cdp.web_audio.AudioListener)*

### *class* AudioListenerWillBeDestroyed(context_id, listener_id)

Notifies that a new AudioListener has been created.

#### context_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### listener_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

### *class* AudioNodeCreated(node)

Notifies that a new AudioNode has been created.

#### node*: [`AudioNode`](#nodriver.cdp.web_audio.AudioNode)*

### *class* AudioNodeWillBeDestroyed(context_id, node_id)

Notifies that an existing AudioNode has been destroyed.

#### context_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### node_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

### *class* AudioParamCreated(param)

Notifies that a new AudioParam has been created.

#### param*: [`AudioParam`](#nodriver.cdp.web_audio.AudioParam)*

### *class* AudioParamWillBeDestroyed(context_id, node_id, param_id)

Notifies that an existing AudioParam has been destroyed.

#### context_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### node_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### param_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

### *class* NodesConnected(context_id, source_id, destination_id, source_output_index, destination_input_index)

Notifies that two AudioNodes are connected.

#### context_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### source_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### destination_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### source_output_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]*

#### destination_input_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]*

### *class* NodesDisconnected(context_id, source_id, destination_id, source_output_index, destination_input_index)

Notifies that AudioNodes are disconnected. The destination can be null, and it means all the outgoing connections from the source are disconnected.

#### context_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### source_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### destination_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### source_output_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]*

#### destination_input_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]*

### *class* NodeParamConnected(context_id, source_id, destination_id, source_output_index)

Notifies that an AudioNode is connected to an AudioParam.

#### context_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### source_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### destination_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### source_output_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]*

### *class* NodeParamDisconnected(context_id, source_id, destination_id, source_output_index)

Notifies that an AudioNode is disconnected to an AudioParam.

#### context_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### source_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### destination_id*: [`GraphObjectId`](#nodriver.cdp.web_audio.GraphObjectId)*

#### source_output_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]*
