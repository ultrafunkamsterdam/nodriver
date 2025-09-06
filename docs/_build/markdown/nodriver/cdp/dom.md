# DOM

This domain exposes DOM read/write operations. Each DOM Node is represented with its mirror object
that has an [`id`](https://docs.python.org/3/library/functions.html#id). This [`id`](https://docs.python.org/3/library/functions.html#id) can be used to get additional information on the Node, resolve it into
the JavaScript object wrapper, etc. It is important that client receives DOM events only for the
nodes that are known to the client. Backend keeps track of the nodes that were sent to the client
and never sends the same node twice. It is client’s responsibility to collect information about
the nodes that were sent to the client. Note that `iframe` owner elements will return
corresponding document elements as their child nodes.

<a id="module-nodriver.cdp.dom"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* NodeId

Unique DOM node identifier.

### *class* BackendNodeId

Unique DOM node identifier used to reference a node that may not have been pushed to the
front-end.

### *class* BackendNode(node_type, node_name, backend_node_id)

Backend node with a friendly name.

#### node_type*: [`int`](https://docs.python.org/3/library/functions.html#int)*

`Node`’s nodeType.

#### node_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`Node`’s nodeName.

#### backend_node_id*: [`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId)*

### *class* PseudoType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Pseudo element type.

#### FIRST_LINE *= 'first-line'*

#### FIRST_LETTER *= 'first-letter'*

#### CHECKMARK *= 'checkmark'*

#### BEFORE *= 'before'*

#### AFTER *= 'after'*

#### PICKER_ICON *= 'picker-icon'*

#### INTEREST_HINT *= 'interest-hint'*

#### MARKER *= 'marker'*

#### BACKDROP *= 'backdrop'*

#### COLUMN *= 'column'*

#### SELECTION *= 'selection'*

#### SEARCH_TEXT *= 'search-text'*

#### TARGET_TEXT *= 'target-text'*

#### SPELLING_ERROR *= 'spelling-error'*

#### GRAMMAR_ERROR *= 'grammar-error'*

#### HIGHLIGHT *= 'highlight'*

#### FIRST_LINE_INHERITED *= 'first-line-inherited'*

#### SCROLL_MARKER *= 'scroll-marker'*

#### SCROLL_MARKER_GROUP *= 'scroll-marker-group'*

#### SCROLL_BUTTON *= 'scroll-button'*

#### SCROLLBAR *= 'scrollbar'*

#### SCROLLBAR_THUMB *= 'scrollbar-thumb'*

#### SCROLLBAR_BUTTON *= 'scrollbar-button'*

#### SCROLLBAR_TRACK *= 'scrollbar-track'*

#### SCROLLBAR_TRACK_PIECE *= 'scrollbar-track-piece'*

#### SCROLLBAR_CORNER *= 'scrollbar-corner'*

#### RESIZER *= 'resizer'*

#### INPUT_LIST_BUTTON *= 'input-list-button'*

#### VIEW_TRANSITION *= 'view-transition'*

#### VIEW_TRANSITION_GROUP *= 'view-transition-group'*

#### VIEW_TRANSITION_IMAGE_PAIR *= 'view-transition-image-pair'*

#### VIEW_TRANSITION_GROUP_CHILDREN *= 'view-transition-group-children'*

#### VIEW_TRANSITION_OLD *= 'view-transition-old'*

#### VIEW_TRANSITION_NEW *= 'view-transition-new'*

#### PLACEHOLDER *= 'placeholder'*

#### FILE_SELECTOR_BUTTON *= 'file-selector-button'*

#### DETAILS_CONTENT *= 'details-content'*

#### PICKER *= 'picker'*

#### PERMISSION_ICON *= 'permission-icon'*

### *class* ShadowRootType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Shadow root type.

#### USER_AGENT *= 'user-agent'*

#### OPEN_ *= 'open'*

#### CLOSED *= 'closed'*

### *class* CompatibilityMode(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Document compatibility mode.

#### QUIRKS_MODE *= 'QuirksMode'*

#### LIMITED_QUIRKS_MODE *= 'LimitedQuirksMode'*

#### NO_QUIRKS_MODE *= 'NoQuirksMode'*

### *class* PhysicalAxes(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

ContainerSelector physical axes

#### HORIZONTAL *= 'Horizontal'*

#### VERTICAL *= 'Vertical'*

#### BOTH *= 'Both'*

### *class* LogicalAxes(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

ContainerSelector logical axes

#### INLINE *= 'Inline'*

#### BLOCK *= 'Block'*

#### BOTH *= 'Both'*

### *class* ScrollOrientation(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Physical scroll orientation

#### HORIZONTAL *= 'horizontal'*

#### VERTICAL *= 'vertical'*

### *class* Node(node_id, backend_node_id, node_type, node_name, local_name, node_value, parent_id=None, child_node_count=None, children=None, attributes=None, document_url=None, base_url=None, public_id=None, system_id=None, internal_subset=None, xml_version=None, name=None, value=None, pseudo_type=None, pseudo_identifier=None, shadow_root_type=None, frame_id=None, content_document=None, shadow_roots=None, template_content=None, pseudo_elements=None, imported_document=None, distributed_nodes=None, is_svg=None, compatibility_mode=None, assigned_slot=None, is_scrollable=None)

DOM interaction is implemented in terms of mirror objects that represent the actual DOM nodes.
DOMNode is a base node mirror type.

#### node_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Node identifier that is passed into the rest of the DOM messages as the `nodeId`. Backend
will only push node with given `id` once. It is aware of all requested nodes and will only
fire DOM events for nodes known to the client.

#### backend_node_id*: [`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId)*

The BackendNodeId for this node.

#### node_type*: [`int`](https://docs.python.org/3/library/functions.html#int)*

`Node`’s nodeType.

#### node_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`Node`’s nodeName.

#### local_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`Node`’s localName.

#### node_value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`Node`’s nodeValue.

#### parent_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]* *= None*

The id of the parent node if any.

#### child_node_count*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Child count for `Container` nodes.

#### children*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Node`](#nodriver.cdp.dom.Node)]]* *= None*

Child nodes of this node when requested with children.

#### attributes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

Attributes of the `Element` node in the form of flat array `[name1, value1, name2, value2]`.

#### document_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Document URL that `Document` or `FrameOwner` node points to.

#### base_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Base URL that `Document` or `FrameOwner` node uses for URL completion.

#### public_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

`DocumentType`’s publicId.

#### system_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

`DocumentType`’s systemId.

#### internal_subset*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

`DocumentType`’s internalSubset.

#### xml_version*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

`Document`’s XML version in case of XML documents.

#### name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

`Attr`’s name.

#### value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

`Attr`’s value.

#### pseudo_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`PseudoType`](#nodriver.cdp.dom.PseudoType)]* *= None*

Pseudo element type for this node.

#### pseudo_identifier*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Pseudo element identifier for this node. Only present if there is a
valid pseudoType.

#### shadow_root_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ShadowRootType`](#nodriver.cdp.dom.ShadowRootType)]* *= None*

Shadow root type.

#### frame_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]* *= None*

Frame ID for frame owner elements.

#### content_document*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Node`](#nodriver.cdp.dom.Node)]* *= None*

Content document for frame owner elements.

#### shadow_roots*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Node`](#nodriver.cdp.dom.Node)]]* *= None*

Shadow root list for given element host.

#### template_content*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Node`](#nodriver.cdp.dom.Node)]* *= None*

Content document fragment for template elements.

#### pseudo_elements*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Node`](#nodriver.cdp.dom.Node)]]* *= None*

Pseudo elements associated with this node.

#### imported_document*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Node`](#nodriver.cdp.dom.Node)]* *= None*

Deprecated, as the HTML Imports API has been removed (crbug.com/937746).
This property used to return the imported document for the HTMLImport links.
The property is always undefined now.

#### distributed_nodes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BackendNode`](#nodriver.cdp.dom.BackendNode)]]* *= None*

Distributed nodes for given insertion point.

#### is_svg*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether the node is SVG.

#### compatibility_mode*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CompatibilityMode`](#nodriver.cdp.dom.CompatibilityMode)]* *= None*

#### assigned_slot*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNode`](#nodriver.cdp.dom.BackendNode)]* *= None*

#### is_scrollable*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

### *class* DetachedElementInfo(tree_node, retained_node_ids)

A structure to hold the top-level node of a detached tree and an array of its retained descendants.

#### tree_node*: [`Node`](#nodriver.cdp.dom.Node)*

#### retained_node_ids*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NodeId`](#nodriver.cdp.dom.NodeId)]*

### *class* RGBA(r, g, b, a=None)

A structure holding an RGBA color.

#### r*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The red component, in the [0-255] range.

#### g*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The green component, in the [0-255] range.

#### b*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The blue component, in the [0-255] range.

#### a*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

1).

* **Type:**
  The alpha component, in the [0-1] [range](https://docs.python.org/3/library/stdtypes.html#range) (default

### *class* Quad(iterable=(), /)

An array of quad vertices, x immediately followed by y for each point, points clock-wise.

### *class* BoxModel(content, padding, border, margin, width, height, shape_outside=None)

Box model.

#### content*: [`Quad`](#nodriver.cdp.dom.Quad)*

Content box

#### padding*: [`Quad`](#nodriver.cdp.dom.Quad)*

Padding box

#### border*: [`Quad`](#nodriver.cdp.dom.Quad)*

Border box

#### margin*: [`Quad`](#nodriver.cdp.dom.Quad)*

Margin box

#### width*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Node width

#### height*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Node height

#### shape_outside*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ShapeOutsideInfo`](#nodriver.cdp.dom.ShapeOutsideInfo)]* *= None*

Shape outside coordinates

### *class* ShapeOutsideInfo(bounds, shape, margin_shape)

CSS Shape Outside details.

#### bounds*: [`Quad`](#nodriver.cdp.dom.Quad)*

Shape bounds

#### shape*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]*

Shape coordinate details

#### margin_shape*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]*

Margin shape bounds

### *class* Rect(x, y, width, height)

Rectangle.

#### x*: [`float`](https://docs.python.org/3/library/functions.html#float)*

X coordinate

#### y*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Y coordinate

#### width*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Rectangle width

#### height*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Rectangle height

### *class* CSSComputedStyleProperty(name, value)

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Computed style property name.

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Computed style property value.

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### collect_class_names_from_subtree(node_id)

Collects class names for the node with given id and all of it’s child nodes.

**EXPERIMENTAL**

* **Parameters:**
  **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node to collect class names.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**
  Class name list.

### copy_to(node_id, target_node_id, insert_before_node_id=None)

Creates a deep copy of the specified node and places it into the target container before the
given anchor.

**EXPERIMENTAL**

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node to copy.
  * **target_node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the element to drop the copy into.
  * **insert_before_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]) – *(Optional)* Drop the copy before this node (if absent, the copy becomes the last child of ``targetNodeId``).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`NodeId`](#nodriver.cdp.dom.NodeId)]
* **Returns:**
  Id of the node clone.

### describe_node(node_id=None, backend_node_id=None, object_id=None, depth=None, pierce=None)

Describes node given its id, does not require domain to be enabled. Does not start tracking any
objects, can be used for automation.

* **Parameters:**
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]) – *(Optional)* Identifier of the node.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Identifier of the backend node.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* JavaScript object id of the node wrapper.
  * **depth** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
  * **pierce** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Node`](#nodriver.cdp.dom.Node)]
* **Returns:**
  Node description.

### disable()

Disables DOM agent for the given page.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### discard_search_results(search_id)

Discards search results from the session with the given id. `getSearchResults` should no longer
be called for that search.

**EXPERIMENTAL**

* **Parameters:**
  **search_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Unique search session identifier.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable(include_whitespace=None)

Enables DOM agent for the given page.

* **Parameters:**
  **include_whitespace** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* Whether to include whitespaces in the children array of returned Nodes.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### focus(node_id=None, backend_node_id=None, object_id=None)

Focuses the given element.

* **Parameters:**
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]) – *(Optional)* Identifier of the node.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Identifier of the backend node.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* JavaScript object id of the node wrapper.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### force_show_popover(node_id, enable)

When enabling, this API force-opens the popover identified by nodeId
and keeps it open until disabled.

**EXPERIMENTAL**

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the popover HTMLElement
  * **enable** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – If true, opens the popover and keeps it open. If false, closes the popover if it was previously force-opened.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NodeId`](#nodriver.cdp.dom.NodeId)]]
* **Returns:**
  List of popovers that were closed in order to respect popover stacking order.

### get_anchor_element(node_id, anchor_specifier=None)

Returns the target anchor element of the given anchor query according to
[https://www.w3.org/TR/css-anchor-position-1/#target](https://www.w3.org/TR/css-anchor-position-1/#target).

**EXPERIMENTAL**

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the positioned element from which to find the anchor.
  * **anchor_specifier** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* An optional anchor specifier, as defined in [https://www.w3.org/TR/css-anchor-position-1/#anchor-specifier](https://www.w3.org/TR/css-anchor-position-1/#anchor-specifier). If not provided, it will return the implicit anchor element for the given positioned element.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`NodeId`](#nodriver.cdp.dom.NodeId)]
* **Returns:**
  The anchor element of the given anchor query.

### get_attributes(node_id)

Returns attributes for the specified node.

* **Parameters:**
  **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node to retrieve attributes for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**
  An interleaved array of node attribute names and values.

### get_box_model(node_id=None, backend_node_id=None, object_id=None)

Returns boxes for the given node.

* **Parameters:**
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]) – *(Optional)* Identifier of the node.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Identifier of the backend node.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* JavaScript object id of the node wrapper.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`BoxModel`](#nodriver.cdp.dom.BoxModel)]
* **Returns:**
  Box model for the node.

### get_container_for_node(node_id, container_name=None, physical_axes=None, logical_axes=None, queries_scroll_state=None, queries_anchored=None)

Returns the query container of the given node based on container query
conditions: containerName, physical and logical axes, and whether it queries
scroll-state or anchored elements. If no axes are provided and
queriesScrollState is false, the style container is returned, which is the
direct parent or the closest element with a matching container-name.

**EXPERIMENTAL**

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – 
  * **container_name** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)*
  * **physical_axes** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`PhysicalAxes`](#nodriver.cdp.dom.PhysicalAxes)]) – *(Optional)*
  * **logical_axes** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LogicalAxes`](#nodriver.cdp.dom.LogicalAxes)]) – *(Optional)*
  * **queries_scroll_state** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)*
  * **queries_anchored** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)*
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]]
* **Returns:**
  *(Optional)* The container node for the given node, or null if not found.

### get_content_quads(node_id=None, backend_node_id=None, object_id=None)

Returns quads that describe node position on the page. This method
might return multiple quads for inline nodes.

**EXPERIMENTAL**

* **Parameters:**
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]) – *(Optional)* Identifier of the node.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Identifier of the backend node.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* JavaScript object id of the node wrapper.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Quad`](#nodriver.cdp.dom.Quad)]]
* **Returns:**
  Quads that describe node layout relative to viewport.

### get_detached_dom_nodes()

Returns list of detached nodes

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`DetachedElementInfo`](#nodriver.cdp.dom.DetachedElementInfo)]]
* **Returns:**
  The list of detached nodes

### get_document(depth=None, pierce=None)

Returns the root DOM node (and optionally the subtree) to the caller.
Implicitly enables the DOM domain events for the current target.

* **Parameters:**
  * **depth** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
  * **pierce** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Node`](#nodriver.cdp.dom.Node)]
* **Returns:**
  Resulting node.

### get_element_by_relation(node_id, relation)

Returns the NodeId of the matched element according to certain relations.

**EXPERIMENTAL**

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node from which to query the relation.
  * **relation** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Type of relation to get.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`NodeId`](#nodriver.cdp.dom.NodeId)]
* **Returns:**
  NodeId of the element matching the queried relation.

### get_file_info(object_id)

Returns file information for the given
File wrapper.

**EXPERIMENTAL**

* **Parameters:**
  **object_id** ([`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)) – JavaScript object id of the node wrapper.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**

### get_flattened_document(depth=None, pierce=None)

Returns the root DOM node (and optionally the subtree) to the caller.
Deprecated, as it is not designed to work well with the rest of the DOM agent.
Use DOMSnapshot.captureSnapshot instead.

#### Deprecated
Deprecated since version 1.3.

* **Parameters:**
  * **depth** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
  * **pierce** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Node`](#nodriver.cdp.dom.Node)]]
* **Returns:**
  Resulting node.

#### Deprecated
Deprecated since version 1.3.

### get_frame_owner(frame_id)

Returns iframe node that owns iframe with the given domain.

**EXPERIMENTAL**

* **Parameters:**
  **frame_id** ([`FrameId`](page.md#nodriver.cdp.page.FrameId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]]]
* **Returns:**
  A tuple with the following items:
  1. **backendNodeId** - Resulting node.
  2. **nodeId** - *(Optional)* Id of the node at given coordinates, only when enabled and requested document.

### get_node_for_location(x, y, include_user_agent_shadow_dom=None, ignore_pointer_events_none=None)

Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is
either returned or not.

* **Parameters:**
  * **x** ([`int`](https://docs.python.org/3/library/functions.html#int)) – X coordinate.
  * **y** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Y coordinate.
  * **include_user_agent_shadow_dom** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* False to skip to the nearest non-UA shadow root ancestor (default: false).
  * **ignore_pointer_events_none** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to ignore pointer-events: none on elements and hit test them.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId), [`FrameId`](page.md#nodriver.cdp.page.FrameId), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]]]
* **Returns:**
  A tuple with the following items:
  1. **backendNodeId** - Resulting node.
  2. **frameId** - Frame this node belongs to.
  3. **nodeId** - *(Optional)* Id of the node at given coordinates, only when enabled and requested document.

### get_node_stack_traces(node_id)

Gets stack traces associated with a Node. As of now, only provides stack trace for Node creation.

**EXPERIMENTAL**

* **Parameters:**
  **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node to get stack traces for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StackTrace`](runtime.md#nodriver.cdp.runtime.StackTrace)]]
* **Returns:**
  *(Optional)* Creation stack trace, if available.

### get_nodes_for_subtree_by_style(node_id, computed_styles, pierce=None)

Finds nodes with a given computed style in a subtree.

**EXPERIMENTAL**

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Node ID pointing to the root of a subtree.
  * **computed_styles** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSComputedStyleProperty`](#nodriver.cdp.dom.CSSComputedStyleProperty)]) – The style to filter nodes by (includes nodes if any of properties matches).
  * **pierce** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether or not iframes and shadow roots in the same target should be traversed when returning the results (default is false).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NodeId`](#nodriver.cdp.dom.NodeId)]]
* **Returns:**
  Resulting nodes.

### get_outer_html(node_id=None, backend_node_id=None, object_id=None, include_shadow_dom=None)

Returns node’s HTML markup.

* **Parameters:**
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]) – *(Optional)* Identifier of the node.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Identifier of the backend node.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* JavaScript object id of the node wrapper.
  * **include_shadow_dom** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Include all shadow roots. Equals to false if not specified.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**
  Outer HTML markup.

### get_querying_descendants_for_container(node_id)

Returns the descendants of a container query container that have
container queries against this container.

**EXPERIMENTAL**

* **Parameters:**
  **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the container node to find querying descendants from.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NodeId`](#nodriver.cdp.dom.NodeId)]]
* **Returns:**
  Descendant nodes with container queries against the given container.

### get_relayout_boundary(node_id)

Returns the id of the nearest ancestor that is a relayout boundary.

**EXPERIMENTAL**

* **Parameters:**
  **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`NodeId`](#nodriver.cdp.dom.NodeId)]
* **Returns:**
  Relayout boundary node id for the given node.

### get_search_results(search_id, from_index, to_index)

Returns search results from given `fromIndex` to given `toIndex` from the search with the given
identifier.

**EXPERIMENTAL**

* **Parameters:**
  * **search_id** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Unique search session identifier.
  * **from_index** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Start index of the search result to be returned.
  * **to_index** ([`int`](https://docs.python.org/3/library/functions.html#int)) – End index of the search result to be returned.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NodeId`](#nodriver.cdp.dom.NodeId)]]
* **Returns:**
  Ids of the search result nodes.

### get_top_layer_elements()

Returns NodeIds of current top layer elements.
Top layer is rendered closest to the user within a viewport, therefore its elements always
appear on top of all other content.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NodeId`](#nodriver.cdp.dom.NodeId)]]
* **Returns:**
  NodeIds of top layer elements

### hide_highlight()

Hides any highlight.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### highlight_node()

Highlights DOM node.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### highlight_rect()

Highlights given rectangle.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### mark_undoable_state()

Marks last undoable state.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### move_to(node_id, target_node_id, insert_before_node_id=None)

Moves node into the new container, places it before the given anchor.

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node to move.
  * **target_node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the element to drop the moved node into.
  * **insert_before_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]) – *(Optional)* Drop node before this one (if absent, the moved node becomes the last child of ``targetNodeId``).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`NodeId`](#nodriver.cdp.dom.NodeId)]
* **Returns:**
  New id of the moved node.

### perform_search(query, include_user_agent_shadow_dom=None)

Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or
`cancelSearch` to end this search session.

**EXPERIMENTAL**

* **Parameters:**
  * **query** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Plain text or query selector or XPath search query.
  * **include_user_agent_shadow_dom** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* True to search in user agent shadow DOM.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`int`](https://docs.python.org/3/library/functions.html#int)]]
* **Returns:**
  A tuple with the following items:
  1. **searchId** - Unique search session identifier.
  2. **resultCount** - Number of search results.

### push_node_by_path_to_frontend(path)

Requests that the node is sent to the caller given its path. // FIXME, use XPath

**EXPERIMENTAL**

* **Parameters:**
  **path** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Path to node in the proprietary format.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`NodeId`](#nodriver.cdp.dom.NodeId)]
* **Returns:**
  Id of the node for given path.

### push_nodes_by_backend_ids_to_frontend(backend_node_ids)

Requests that a batch of nodes is sent to the caller given their backend node ids.

**EXPERIMENTAL**

* **Parameters:**
  **backend_node_ids** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId)]) – The array of backend node ids.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NodeId`](#nodriver.cdp.dom.NodeId)]]
* **Returns:**
  The array of ids of pushed nodes that correspond to the backend ids specified in backendNodeIds.

### query_selector(node_id, selector)

Executes `querySelector` on a given node.

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node to query upon.
  * **selector** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Selector string.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`NodeId`](#nodriver.cdp.dom.NodeId)]
* **Returns:**
  Query selector result.

### query_selector_all(node_id, selector)

Executes `querySelectorAll` on a given node.

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node to query upon.
  * **selector** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Selector string.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NodeId`](#nodriver.cdp.dom.NodeId)]]
* **Returns:**
  Query selector result.

### redo()

Re-does the last undone action.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### remove_attribute(node_id, name)

Removes attribute with given name from an element with given id.

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the element to remove attribute from.
  * **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Name of the attribute to remove.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### remove_node(node_id)

Removes node with given id.

* **Parameters:**
  **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node to remove.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### request_child_nodes(node_id, depth=None, pierce=None)

Requests that children of the node with given id are returned to the caller in form of
`setChildNodes` events where not only immediate children are retrieved, but all children down to
the specified depth.

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node to get children for.
  * **depth** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
  * **pierce** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether or not iframes and shadow roots should be traversed when returning the sub-tree (default is false).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### request_node(object_id)

Requests that the node is sent to the caller given the JavaScript node object reference. All
nodes that form the path from the node to the root are also sent to the client as a series of
`setChildNodes` notifications.

* **Parameters:**
  **object_id** ([`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)) – JavaScript object id to convert into node.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`NodeId`](#nodriver.cdp.dom.NodeId)]
* **Returns:**
  Node id for given object.

### resolve_node(node_id=None, backend_node_id=None, object_group=None, execution_context_id=None)

Resolves the JavaScript node object for a given NodeId or BackendNodeId.

* **Parameters:**
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]) – *(Optional)* Id of the node to resolve.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Backend identifier of the node to resolve.
  * **object_group** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Symbolic group name that can be used to release multiple objects.
  * **execution_context_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ExecutionContextId`](runtime.md#nodriver.cdp.runtime.ExecutionContextId)]) – *(Optional)* Execution context in which to resolve the node.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`RemoteObject`](runtime.md#nodriver.cdp.runtime.RemoteObject)]
* **Returns:**
  JavaScript object wrapper for given node.

### scroll_into_view_if_needed(node_id=None, backend_node_id=None, object_id=None, rect=None)

Scrolls the specified rect of the given node into view if not already visible.
Note: exactly one between nodeId, backendNodeId and objectId should be passed
to identify the node.

* **Parameters:**
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]) – *(Optional)* Identifier of the node.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Identifier of the backend node.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* JavaScript object id of the node wrapper.
  * **rect** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Rect`](#nodriver.cdp.dom.Rect)]) – *(Optional)* The rect to be scrolled into view, relative to the node’s border box, in CSS pixels. When omitted, center of the node will be used, similar to Element.scrollIntoView.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_attribute_value(node_id, name, value)

Sets attribute for an element with given id.

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the element to set attribute for.
  * **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Attribute name.
  * **value** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Attribute value.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_attributes_as_text(node_id, text, name=None)

Sets attributes on element with given id. This method is useful when user edits some existing
attribute value and types in several attribute name/value pairs.

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the element to set attributes for.
  * **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Text with a number of attributes. Will parse this text using HTML parser.
  * **name** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Attribute name to replace with new attributes derived from text in case text parsed successfully.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_file_input_files(files, node_id=None, backend_node_id=None, object_id=None)

Sets files for the given file input element.

* **Parameters:**
  * **files** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – Array of file paths to set.
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](#nodriver.cdp.dom.NodeId)]) – *(Optional)* Identifier of the node.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Identifier of the backend node.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* JavaScript object id of the node wrapper.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_inspected_node(node_id)

Enables console to refer to the node with given id via $x (see Command Line API for more details
$x functions).

**EXPERIMENTAL**

* **Parameters:**
  **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – DOM node id to be accessible by means of $x command line API.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_node_name(node_id, name)

Sets node name for a node with given id.

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node to set name for.
  * **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – New node’s name.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`NodeId`](#nodriver.cdp.dom.NodeId)]
* **Returns:**
  New node’s id.

### set_node_stack_traces_enabled(enable)

Sets if stack traces should be captured for Nodes. See `Node.getNodeStackTraces`. Default is disabled.

**EXPERIMENTAL**

* **Parameters:**
  **enable** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Enable or disable.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_node_value(node_id, value)

Sets node value for a node with given id.

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node to set value for.
  * **value** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – New node’s value.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_outer_html(node_id, outer_html)

Sets node HTML markup, returns new node id.

* **Parameters:**
  * **node_id** ([`NodeId`](#nodriver.cdp.dom.NodeId)) – Id of the node to set markup for.
  * **outer_html** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – Outer HTML markup to set.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### undo()

Undoes the last performed action.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* AttributeModified(node_id, name, value)

Fired when `Element`’s attribute is modified.

#### node_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Id of the node that has changed.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Attribute name.

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Attribute value.

### *class* AttributeRemoved(node_id, name)

Fired when `Element`’s attribute is removed.

#### node_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Id of the node that has changed.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

A ttribute name.

### *class* CharacterDataModified(node_id, character_data)

Mirrors `DOMCharacterDataModified` event.

#### node_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Id of the node that has changed.

#### character_data*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

New text value.

### *class* ChildNodeCountUpdated(node_id, child_node_count)

Fired when `Container`’s child node count has changed.

#### node_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Id of the node that has changed.

#### child_node_count*: [`int`](https://docs.python.org/3/library/functions.html#int)*

New node count.

### *class* ChildNodeInserted(parent_node_id, previous_node_id, node)

Mirrors `DOMNodeInserted` event.

#### parent_node_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Id of the node that has changed.

#### previous_node_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Id of the previous sibling.

#### node*: [`Node`](#nodriver.cdp.dom.Node)*

Inserted node data.

### *class* ChildNodeRemoved(parent_node_id, node_id)

Mirrors `DOMNodeRemoved` event.

#### parent_node_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Parent id.

#### node_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Id of the node that has been removed.

### *class* DistributedNodesUpdated(insertion_point_id, distributed_nodes)

**EXPERIMENTAL**

Called when distribution is changed.

#### insertion_point_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Insertion point where distributed nodes were updated.

#### distributed_nodes*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BackendNode`](#nodriver.cdp.dom.BackendNode)]*

Distributed nodes for given insertion point.

### *class* DocumentUpdated

Fired when `Document` has been totally updated. Node ids are no longer valid.

### *class* InlineStyleInvalidated(node_ids)

**EXPERIMENTAL**

Fired when `Element`’s inline style is modified via a CSS property modification.

#### node_ids*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NodeId`](#nodriver.cdp.dom.NodeId)]*

Ids of the nodes for which the inline styles have been invalidated.

### *class* PseudoElementAdded(parent_id, pseudo_element)

**EXPERIMENTAL**

Called when a pseudo element is added to an element.

#### parent_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Pseudo element’s parent element id.

#### pseudo_element*: [`Node`](#nodriver.cdp.dom.Node)*

The added pseudo element.

### *class* TopLayerElementsUpdated

**EXPERIMENTAL**

Called when top layer elements are changed.

### *class* ScrollableFlagUpdated(node_id, is_scrollable)

**EXPERIMENTAL**

Fired when a node’s scrollability state changes.

#### node_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

The id of the node.

#### is_scrollable*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

If the node is scrollable.

### *class* PseudoElementRemoved(parent_id, pseudo_element_id)

**EXPERIMENTAL**

Called when a pseudo element is removed from an element.

#### parent_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Pseudo element’s parent element id.

#### pseudo_element_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

The removed pseudo element id.

### *class* SetChildNodes(parent_id, nodes)

Fired when backend wants to provide client with the missing DOM structure. This happens upon
most of the calls requesting node ids.

#### parent_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Parent node id to populate with children.

#### nodes*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Node`](#nodriver.cdp.dom.Node)]*

Child nodes array.

### *class* ShadowRootPopped(host_id, root_id)

**EXPERIMENTAL**

Called when shadow root is popped from the element.

#### host_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Host element id.

#### root_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Shadow root id.

### *class* ShadowRootPushed(host_id, root)

**EXPERIMENTAL**

Called when shadow root is pushed into the element.

#### host_id*: [`NodeId`](#nodriver.cdp.dom.NodeId)*

Host element id.

#### root*: [`Node`](#nodriver.cdp.dom.Node)*

Shadow root.
