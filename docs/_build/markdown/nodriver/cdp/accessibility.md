# Accessibility

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.accessibility"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* AXNodeId

Unique accessibility node identifier.

### *class* AXValueType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of possible property types.

#### BOOLEAN *= 'boolean'*

#### BOOLEAN_OR_UNDEFINED *= 'booleanOrUndefined'*

#### COMPUTED_STRING *= 'computedString'*

#### DOM_RELATION *= 'domRelation'*

#### IDREF *= 'idref'*

#### IDREF_LIST *= 'idrefList'*

#### INTEGER *= 'integer'*

#### INTERNAL_ROLE *= 'internalRole'*

#### NODE *= 'node'*

#### NODE_LIST *= 'nodeList'*

#### NUMBER *= 'number'*

#### ROLE *= 'role'*

#### STRING *= 'string'*

#### TOKEN *= 'token'*

#### TOKEN_LIST *= 'tokenList'*

#### TRISTATE *= 'tristate'*

#### VALUE_UNDEFINED *= 'valueUndefined'*

### *class* AXValueSourceType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of possible property sources.

#### ATTRIBUTE *= 'attribute'*

#### CONTENTS *= 'contents'*

#### IMPLICIT *= 'implicit'*

#### PLACEHOLDER *= 'placeholder'*

#### RELATED_ELEMENT *= 'relatedElement'*

#### STYLE *= 'style'*

### *class* AXValueNativeSourceType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum of possible native property sources (as a subtype of a particular AXValueSourceType).

#### DESCRIPTION *= 'description'*

#### FIGCAPTION *= 'figcaption'*

#### LABEL *= 'label'*

#### LABELFOR *= 'labelfor'*

#### LABELWRAPPED *= 'labelwrapped'*

#### LEGEND *= 'legend'*

#### OTHER *= 'other'*

#### RUBYANNOTATION *= 'rubyannotation'*

#### TABLECAPTION *= 'tablecaption'*

#### TITLE *= 'title'*

### *class* AXValueSource(type_, value=None, attribute=None, attribute_value=None, superseded=None, native_source=None, native_source_value=None, invalid=None, invalid_reason=None)

A single source for a computed AX property.

* **Parameters:**
  * **type_** ([*AXValueSourceType*](#nodriver.cdp.accessibility.AXValueSourceType)) – 
  * **value** ([*AXValue*](#nodriver.cdp.accessibility.AXValue) *|* *None*) – 
  * **attribute** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **attribute_value** ([*AXValue*](#nodriver.cdp.accessibility.AXValue) *|* *None*) – 
  * **superseded** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **native_source** ([*AXValueNativeSourceType*](#nodriver.cdp.accessibility.AXValueNativeSourceType) *|* *None*) – 
  * **native_source_value** ([*AXValue*](#nodriver.cdp.accessibility.AXValue) *|* *None*) – 
  * **invalid** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **invalid_reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### attribute*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The name of the relevant attribute, if any.

#### attribute_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AXValue`](#nodriver.cdp.accessibility.AXValue)]* *= None*

The value of the relevant attribute, if any.

#### invalid*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether the value for this property is invalid.

#### invalid_reason*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Reason for the value being invalid, if it is.

#### native_source*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AXValueNativeSourceType`](#nodriver.cdp.accessibility.AXValueNativeSourceType)]* *= None*

The native markup source for this value, e.g. a `<label>` element.

#### native_source_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AXValue`](#nodriver.cdp.accessibility.AXValue)]* *= None*

The value, such as a node or node list, of the native source.

#### superseded*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether this source is superseded by a higher priority source.

#### type_*: [`AXValueSourceType`](#nodriver.cdp.accessibility.AXValueSourceType)*

What type of source this is.

#### value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AXValue`](#nodriver.cdp.accessibility.AXValue)]* *= None*

The value of this property source.

### *class* AXRelatedNode(backend_dom_node_id, idref=None, text=None)

* **Parameters:**
  * **backend_dom_node_id** ([*BackendNodeId*](dom.md#nodriver.cdp.dom.BackendNodeId)) – 
  * **idref** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### backend_dom_node_id*: [`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)*

The BackendNodeId of the related DOM node.

#### idref*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The IDRef value provided, if any.

#### text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The text alternative of this node in the current context.

### *class* AXProperty(name, value)

* **Parameters:**
  * **name** ([*AXPropertyName*](#nodriver.cdp.accessibility.AXPropertyName)) – 
  * **value** ([*AXValue*](#nodriver.cdp.accessibility.AXValue)) – 

#### name*: [`AXPropertyName`](#nodriver.cdp.accessibility.AXPropertyName)*

The name of this property.

#### value*: [`AXValue`](#nodriver.cdp.accessibility.AXValue)*

The value of this property.

### *class* AXValue(type_, value=None, related_nodes=None, sources=None)

A single computed AX property.

* **Parameters:**
  * **type_** ([*AXValueType*](#nodriver.cdp.accessibility.AXValueType)) – 
  * **value** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **related_nodes** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*AXRelatedNode*](#nodriver.cdp.accessibility.AXRelatedNode)*]* *|* *None*) – 
  * **sources** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*AXValueSource*](#nodriver.cdp.accessibility.AXValueSource)*]* *|* *None*) – 

#### related_nodes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AXRelatedNode`](#nodriver.cdp.accessibility.AXRelatedNode)]]* *= None*

One or more related nodes, if applicable.

#### sources*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AXValueSource`](#nodriver.cdp.accessibility.AXValueSource)]]* *= None*

The sources which contributed to the computation of this property.

#### type_*: [`AXValueType`](#nodriver.cdp.accessibility.AXValueType)*

The type of this value.

#### value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]* *= None*

The computed value of this property.

### *class* AXPropertyName(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Values of AXProperty name:
- from ‘busy’ to ‘roledescription’: states which apply to every AX node
- from ‘live’ to ‘root’: attributes which apply to nodes in live regions
- from ‘autocomplete’ to ‘valuetext’: attributes which apply to widgets
- from ‘checked’ to ‘selected’: states which apply to widgets
- from ‘activedescendant’ to ‘owns’ - relationships between elements other than parent/child/sibling.

#### ACTIVEDESCENDANT *= 'activedescendant'*

#### ATOMIC *= 'atomic'*

#### AUTOCOMPLETE *= 'autocomplete'*

#### BUSY *= 'busy'*

#### CHECKED *= 'checked'*

#### CONTROLS *= 'controls'*

#### DESCRIBEDBY *= 'describedby'*

#### DETAILS *= 'details'*

#### DISABLED *= 'disabled'*

#### EDITABLE *= 'editable'*

#### ERRORMESSAGE *= 'errormessage'*

#### EXPANDED *= 'expanded'*

#### FLOWTO *= 'flowto'*

#### FOCUSABLE *= 'focusable'*

#### FOCUSED *= 'focused'*

#### HAS_POPUP *= 'hasPopup'*

#### HIDDEN *= 'hidden'*

#### HIDDEN_ROOT *= 'hiddenRoot'*

#### INVALID *= 'invalid'*

#### KEYSHORTCUTS *= 'keyshortcuts'*

#### LABELLEDBY *= 'labelledby'*

#### LEVEL *= 'level'*

#### LIVE *= 'live'*

#### MODAL *= 'modal'*

#### MULTILINE *= 'multiline'*

#### MULTISELECTABLE *= 'multiselectable'*

#### ORIENTATION *= 'orientation'*

#### OWNS *= 'owns'*

#### PRESSED *= 'pressed'*

#### READONLY *= 'readonly'*

#### RELEVANT *= 'relevant'*

#### REQUIRED *= 'required'*

#### ROLEDESCRIPTION *= 'roledescription'*

#### ROOT *= 'root'*

#### SELECTED *= 'selected'*

#### SETTABLE *= 'settable'*

#### VALUEMAX *= 'valuemax'*

#### VALUEMIN *= 'valuemin'*

#### VALUETEXT *= 'valuetext'*

### *class* AXNode(node_id, ignored, ignored_reasons=None, role=None, chrome_role=None, name=None, description=None, value=None, properties=None, parent_id=None, child_ids=None, backend_dom_node_id=None, frame_id=None)

A node in the accessibility tree.

* **Parameters:**
  * **node_id** ([*AXNodeId*](#nodriver.cdp.accessibility.AXNodeId)) – 
  * **ignored** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **ignored_reasons** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*AXProperty*](#nodriver.cdp.accessibility.AXProperty)*]* *|* *None*) – 
  * **role** ([*AXValue*](#nodriver.cdp.accessibility.AXValue) *|* *None*) – 
  * **chrome_role** ([*AXValue*](#nodriver.cdp.accessibility.AXValue) *|* *None*) – 
  * **name** ([*AXValue*](#nodriver.cdp.accessibility.AXValue) *|* *None*) – 
  * **description** ([*AXValue*](#nodriver.cdp.accessibility.AXValue) *|* *None*) – 
  * **value** ([*AXValue*](#nodriver.cdp.accessibility.AXValue) *|* *None*) – 
  * **properties** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*AXProperty*](#nodriver.cdp.accessibility.AXProperty)*]* *|* *None*) – 
  * **parent_id** ([*AXNodeId*](#nodriver.cdp.accessibility.AXNodeId) *|* *None*) – 
  * **child_ids** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*AXNodeId*](#nodriver.cdp.accessibility.AXNodeId)*]* *|* *None*) – 
  * **backend_dom_node_id** ([*BackendNodeId*](dom.md#nodriver.cdp.dom.BackendNodeId) *|* *None*) – 
  * **frame_id** ([*FrameId*](page.md#nodriver.cdp.page.FrameId) *|* *None*) – 

#### backend_dom_node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

The backend ID for the associated DOM node, if any.

#### child_ids*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AXNodeId`](#nodriver.cdp.accessibility.AXNodeId)]]* *= None*

IDs for each of this node’s child nodes.

#### chrome_role*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AXValue`](#nodriver.cdp.accessibility.AXValue)]* *= None*

This `Node`’s Chrome raw role.

#### description*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AXValue`](#nodriver.cdp.accessibility.AXValue)]* *= None*

The accessible description for this `Node`.

#### frame_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]* *= None*

The frame ID for the frame associated with this nodes document.

#### ignored*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether this node is ignored for accessibility

#### ignored_reasons*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AXProperty`](#nodriver.cdp.accessibility.AXProperty)]]* *= None*

Collection of reasons why this node is hidden.

#### name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AXValue`](#nodriver.cdp.accessibility.AXValue)]* *= None*

The accessible name for this `Node`.

#### node_id*: [`AXNodeId`](#nodriver.cdp.accessibility.AXNodeId)*

Unique identifier for this node.

#### parent_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AXNodeId`](#nodriver.cdp.accessibility.AXNodeId)]* *= None*

ID for this node’s parent.

#### properties*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AXProperty`](#nodriver.cdp.accessibility.AXProperty)]]* *= None*

All other properties

#### role*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AXValue`](#nodriver.cdp.accessibility.AXValue)]* *= None*

This `Node`’s role, whether explicit or implicit.

#### value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AXValue`](#nodriver.cdp.accessibility.AXValue)]* *= None*

The value for this `Node`.

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

Disables the accessibility domain.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables the accessibility domain which causes `AXNodeId`’s to remain consistent between method calls.
This turns on accessibility for the page, which can impact performance until accessibility is disabled.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_ax_node_and_ancestors(node_id=None, backend_node_id=None, object_id=None)

Fetches a node and all ancestors up to and including the root.
Requires `enable()` to have been called previously.

**EXPERIMENTAL**

* **Parameters:**
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](dom.md#nodriver.cdp.dom.NodeId)]) – *(Optional)* Identifier of the node to get.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Identifier of the backend node to get.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* JavaScript object id of the node wrapper to get.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AXNode`](#nodriver.cdp.accessibility.AXNode)]]
* **Returns:**

### get_child_ax_nodes(id_, frame_id=None)

Fetches a particular accessibility node by AXNodeId.
Requires `enable()` to have been called previously.

**EXPERIMENTAL**

* **Parameters:**
  * **id** – 
  * **frame_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]) – *(Optional)* The frame in whose document the node resides. If omitted, the root frame is used.
  * **id_** ([*AXNodeId*](#nodriver.cdp.accessibility.AXNodeId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AXNode`](#nodriver.cdp.accessibility.AXNode)]]
* **Returns:**

### get_full_ax_tree(depth=None, frame_id=None)

Fetches the entire accessibility tree for the root Document

**EXPERIMENTAL**

* **Parameters:**
  * **depth** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* The maximum depth at which descendants of the root node should be retrieved. If omitted, the full tree is returned.
  * **frame_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]) – *(Optional)* The frame for whose document the AX tree should be retrieved. If omited, the root frame is used.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AXNode`](#nodriver.cdp.accessibility.AXNode)]]
* **Returns:**

### get_partial_ax_tree(node_id=None, backend_node_id=None, object_id=None, fetch_relatives=None)

Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists.

**EXPERIMENTAL**

* **Parameters:**
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](dom.md#nodriver.cdp.dom.NodeId)]) – *(Optional)* Identifier of the node to get the partial accessibility tree for.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Identifier of the backend node to get the partial accessibility tree for.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* JavaScript object id of the node wrapper to get the partial accessibility tree for.
  * **fetch_relatives** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to fetch this node’s ancestors, siblings and children. Defaults to true.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AXNode`](#nodriver.cdp.accessibility.AXNode)]]
* **Returns:**
  The `Accessibility.AXNode` for this DOM node, if it exists, plus its ancestors, siblings and children, if requested.

### get_root_ax_node(frame_id=None)

Fetches the root node.
Requires `enable()` to have been called previously.

**EXPERIMENTAL**

* **Parameters:**
  **frame_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]) – *(Optional)* The frame in whose document the node resides. If omitted, the root frame is used.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`AXNode`](#nodriver.cdp.accessibility.AXNode)]
* **Returns:**

### query_ax_tree(node_id=None, backend_node_id=None, object_id=None, accessible_name=None, role=None)

Query a DOM node’s accessibility subtree for accessible name and role.
This command computes the name and role for all nodes in the subtree, including those that are
ignored for accessibility, and returns those that mactch the specified name and role. If no DOM
node is specified, or the DOM node does not exist, the command returns an error. If neither
`accessibleName` or `role` is specified, it returns all the accessibility nodes in the subtree.

**EXPERIMENTAL**

* **Parameters:**
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](dom.md#nodriver.cdp.dom.NodeId)]) – *(Optional)* Identifier of the node for the root to query.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Identifier of the backend node for the root to query.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* JavaScript object id of the node wrapper for the root to query.
  * **accessible_name** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Find nodes with this computed name.
  * **role** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Find nodes with this computed role.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AXNode`](#nodriver.cdp.accessibility.AXNode)]]
* **Returns:**
  A list of `Accessibility.AXNode` matching the specified attributes, including nodes that are ignored for accessibility.

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* LoadComplete(root)

**EXPERIMENTAL**

The loadComplete event mirrors the load complete event sent by the browser to assistive
technology when the web page has finished loading.

* **Parameters:**
  **root** ([*AXNode*](#nodriver.cdp.accessibility.AXNode)) – 

#### root*: [`AXNode`](#nodriver.cdp.accessibility.AXNode)*

New document root node.

### *class* NodesUpdated(nodes)

**EXPERIMENTAL**

The nodesUpdated event is sent every time a previously requested node has changed the in tree.

* **Parameters:**
  **nodes** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*AXNode*](#nodriver.cdp.accessibility.AXNode)*]*) – 

#### nodes*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AXNode`](#nodriver.cdp.accessibility.AXNode)]*

Updated node data.
