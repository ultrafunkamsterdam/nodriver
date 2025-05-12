# Animation

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.animation"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* Animation(id_, name, paused_state, play_state, playback_rate, start_time, current_time, type_, source=None, css_id=None, view_or_scroll_timeline=None)

Animation instance.

#### id_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`Animation`’s id.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`Animation`’s name.

#### paused_state*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

`Animation`’s internal paused state.

#### play_state*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`Animation`’s play state.

#### playback_rate*: [`float`](https://docs.python.org/3/library/functions.html#float)*

`Animation`’s playback rate.

#### start_time*: [`float`](https://docs.python.org/3/library/functions.html#float)*

`Animation`’s start time.
Milliseconds for time based animations and
percentage [0 - 100] for scroll driven animations
(i.e. when viewOrScrollTimeline exists).

#### current_time*: [`float`](https://docs.python.org/3/library/functions.html#float)*

`Animation`’s current time.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Animation type of `Animation`.

#### source*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AnimationEffect`](#nodriver.cdp.animation.AnimationEffect)]* *= None*

`Animation`’s source animation node.

#### css_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

A unique ID for `Animation` representing the sources that triggered this CSS
animation/transition.

#### view_or_scroll_timeline*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ViewOrScrollTimeline`](#nodriver.cdp.animation.ViewOrScrollTimeline)]* *= None*

View or scroll timeline

### *class* ViewOrScrollTimeline(axis, source_node_id=None, start_offset=None, end_offset=None, subject_node_id=None)

Timeline instance

#### axis*: [`ScrollOrientation`](dom.md#nodriver.cdp.dom.ScrollOrientation)*

Orientation of the scroll

#### source_node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

Scroll container node

#### start_offset*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Represents the starting scroll position of the timeline
as a length offset in pixels from scroll origin.

#### end_offset*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Represents the ending scroll position of the timeline
as a length offset in pixels from scroll origin.

#### subject_node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

The element whose principal box’s visibility in the
scrollport defined the progress of the timeline.
Does not exist for animations with ScrollTimeline

### *class* AnimationEffect(delay, end_delay, iteration_start, iterations, duration, direction, fill, easing, backend_node_id=None, keyframes_rule=None)

AnimationEffect instance

#### delay*: [`float`](https://docs.python.org/3/library/functions.html#float)*

`AnimationEffect`’s delay.

#### end_delay*: [`float`](https://docs.python.org/3/library/functions.html#float)*

`AnimationEffect`’s end delay.

#### iteration_start*: [`float`](https://docs.python.org/3/library/functions.html#float)*

`AnimationEffect`’s iteration start.

#### iterations*: [`float`](https://docs.python.org/3/library/functions.html#float)*

`AnimationEffect`’s iterations.

#### duration*: [`float`](https://docs.python.org/3/library/functions.html#float)*

`AnimationEffect`’s iteration duration.
Milliseconds for time based animations and
percentage [0 - 100] for scroll driven animations
(i.e. when viewOrScrollTimeline exists).

#### direction*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`AnimationEffect`’s playback direction.

#### fill*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`AnimationEffect`’s fill mode.

#### easing*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`AnimationEffect`’s timing function.

#### backend_node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

`AnimationEffect`’s target node.

#### keyframes_rule*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`KeyframesRule`](#nodriver.cdp.animation.KeyframesRule)]* *= None*

`AnimationEffect`’s keyframes.

### *class* KeyframesRule(keyframes, name=None)

Keyframes Rule

#### keyframes*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`KeyframeStyle`](#nodriver.cdp.animation.KeyframeStyle)]*

List of animation keyframes.

#### name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

CSS keyframed animation’s name.

### *class* KeyframeStyle(offset, easing)

Keyframe Style

#### offset*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Keyframe’s time offset.

#### easing*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`AnimationEffect`’s timing function.

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

Disables animation domain notifications.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables animation domain notifications.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_current_time(id_)

Returns the current time of the an animation.

* **Parameters:**
  **id** – Id of animation.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`float`](https://docs.python.org/3/library/functions.html#float)]
* **Returns:**
  Current time of the page.

### get_playback_rate()

Gets the playback rate of the document timeline.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`float`](https://docs.python.org/3/library/functions.html#float)]
* **Returns:**
  Playback rate for animations on page.

### release_animations(animations)

Releases a set of animations to no longer be manipulated.

* **Parameters:**
  **animations** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – List of animation ids to seek.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### resolve_animation(animation_id)

Gets the remote object of the Animation.

* **Parameters:**
  **animation_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Animation id.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`RemoteObject`](runtime.md#nodriver.cdp.runtime.RemoteObject)]
* **Returns:**
  Corresponding remote object.

### seek_animations(animations, current_time)

Seek a set of animations to a particular time within each animation.

* **Parameters:**
  * **animations** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – List of animation ids to seek.
  * **current_time** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Set the current time of each animation.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_paused(animations, paused)

Sets the paused state of a set of animations.

* **Parameters:**
  * **animations** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – Animations to set the pause state of.
  * **paused** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Paused state to set to.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_playback_rate(playback_rate)

Sets the playback rate of the document timeline.

* **Parameters:**
  **playback_rate** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Playback rate for animations on page
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_timing(animation_id, duration, delay)

Sets the timing of an animation node.

* **Parameters:**
  * **animation_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Animation id.
  * **duration** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Duration of the animation.
  * **delay** ([`float`](https://docs.python.org/3/library/functions.html#float)) – Delay of the animation.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* AnimationCanceled(id_)

Event for when an animation has been cancelled.

#### id_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Id of the animation that was cancelled.

### *class* AnimationCreated(id_)

Event for each animation that has been created.

#### id_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Id of the animation that was created.

### *class* AnimationStarted(animation)

Event for animation that has been started.

#### animation*: [`Animation`](#nodriver.cdp.animation.Animation)*

Animation that was started.

### *class* AnimationUpdated(animation)

Event for animation that has been updated.

#### animation*: [`Animation`](#nodriver.cdp.animation.Animation)*

Animation that was updated.
