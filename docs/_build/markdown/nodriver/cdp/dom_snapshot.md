# DOMSnapshot

This domain facilitates obtaining document snapshots with DOM, layout, and style information.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.dom_snapshot"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* DOMNode(node_type, node_name, node_value, backend_node_id, text_value=None, input_value=None, input_checked=None, option_selected=None, child_node_indexes=None, attributes=None, pseudo_element_indexes=None, layout_node_index=None, document_url=None, base_url=None, content_language=None, document_encoding=None, public_id=None, system_id=None, frame_id=None, content_document_index=None, pseudo_type=None, shadow_root_type=None, is_clickable=None, event_listeners=None, current_source_url=None, origin_url=None, scroll_offset_x=None, scroll_offset_y=None)

A Node in the DOM tree.

* **Parameters:**
  * **node_type** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **node_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **node_value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **backend_node_id** ([*BackendNodeId*](dom.md#nodriver.cdp.dom.BackendNodeId)) – 
  * **text_value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **input_value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **input_checked** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **option_selected** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **child_node_indexes** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]* *|* *None*) – 
  * **attributes** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*NameValue*](#nodriver.cdp.dom_snapshot.NameValue)*]* *|* *None*) – 
  * **pseudo_element_indexes** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]* *|* *None*) – 
  * **layout_node_index** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **document_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **base_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **content_language** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **document_encoding** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **public_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **system_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **frame_id** ([*FrameId*](page.md#nodriver.cdp.page.FrameId) *|* *None*) – 
  * **content_document_index** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **pseudo_type** ([*PseudoType*](dom.md#nodriver.cdp.dom.PseudoType) *|* *None*) – 
  * **shadow_root_type** ([*ShadowRootType*](dom.md#nodriver.cdp.dom.ShadowRootType) *|* *None*) – 
  * **is_clickable** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **event_listeners** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*EventListener*](dom_debugger.md#nodriver.cdp.dom_debugger.EventListener)*]* *|* *None*) – 
  * **current_source_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **origin_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **scroll_offset_x** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **scroll_offset_y** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 

#### attributes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NameValue`](#nodriver.cdp.dom_snapshot.NameValue)]]* *= None*

Attributes of an `Element` node.

#### backend_node_id*: [`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)*

`Node`’s id, corresponds to DOM.Node.backendNodeId.

#### base_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Base URL that `Document` or `FrameOwner` node uses for URL completion.

#### child_node_indexes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]]* *= None*

The indexes of the node’s child nodes in the `domNodes` array returned by `getSnapshot`, if
any.

#### content_document_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

The index of a frame owner element’s content document in the `domNodes` array returned by
`getSnapshot`, if any.

#### content_language*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Only set for documents, contains the document’s content language.

#### current_source_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The selected url for nodes with a srcset attribute.

#### document_encoding*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Only set for documents, contains the document’s character set encoding.

#### document_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Document URL that `Document` or `FrameOwner` node points to.

#### event_listeners*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`EventListener`](dom_debugger.md#nodriver.cdp.dom_debugger.EventListener)]]* *= None*

Details of the node’s event listeners, if any.

#### frame_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FrameId`](page.md#nodriver.cdp.page.FrameId)]* *= None*

Frame ID for frame owner elements and also for the document node.

#### input_checked*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Only set for radio and checkbox input elements, indicates if the element has been checked

#### input_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Only set for input elements, contains the input’s associated text value.

#### is_clickable*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether this DOM node responds to mouse clicks. This includes nodes that have had click
event listeners attached via JavaScript as well as anchor tags that naturally navigate when
clicked.

#### layout_node_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

The index of the node’s related layout tree node in the `layoutTreeNodes` array returned by
`getSnapshot`, if any.

#### node_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`Node`’s nodeName.

#### node_type*: [`int`](https://docs.python.org/3/library/functions.html#int)*

`Node`’s nodeType.

#### node_value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

`Node`’s nodeValue.

#### option_selected*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Only set for option elements, indicates if the element has been selected

#### origin_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The url of the script (if any) that generates this node.

#### pseudo_element_indexes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]]* *= None*

Indexes of pseudo elements associated with this node in the `domNodes` array returned by
`getSnapshot`, if any.

#### pseudo_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`PseudoType`](dom.md#nodriver.cdp.dom.PseudoType)]* *= None*

Type of a pseudo element node.

#### public_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

`DocumentType` node’s publicId.

#### scroll_offset_x*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Scroll offsets, set when this node is a Document.

#### scroll_offset_y*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

#### shadow_root_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ShadowRootType`](dom.md#nodriver.cdp.dom.ShadowRootType)]* *= None*

Shadow root type.

#### system_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

`DocumentType` node’s systemId.

#### text_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Only set for textarea elements, contains the text value.

### *class* InlineTextBox(bounding_box, start_character_index, num_characters)

Details of post layout rendered text positions. The exact layout should not be regarded as
stable and may change between versions.

* **Parameters:**
  * **bounding_box** ([*Rect*](dom.md#nodriver.cdp.dom.Rect)) – 
  * **start_character_index** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **num_characters** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 

#### bounding_box*: [`Rect`](dom.md#nodriver.cdp.dom.Rect)*

The bounding box in document coordinates. Note that scroll offset of the document is ignored.

#### num_characters*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The number of characters in this post layout textbox substring. Characters that would be
represented as a surrogate pair in UTF-16 have length 2.

#### start_character_index*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The starting index in characters, for this post layout textbox substring. Characters that
would be represented as a surrogate pair in UTF-16 have length 2.

### *class* LayoutTreeNode(dom_node_index, bounding_box, layout_text=None, inline_text_nodes=None, style_index=None, paint_order=None, is_stacking_context=None)

Details of an element in the DOM tree with a LayoutObject.

* **Parameters:**
  * **dom_node_index** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **bounding_box** ([*Rect*](dom.md#nodriver.cdp.dom.Rect)) – 
  * **layout_text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **inline_text_nodes** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*InlineTextBox*](#nodriver.cdp.dom_snapshot.InlineTextBox)*]* *|* *None*) – 
  * **style_index** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **paint_order** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **is_stacking_context** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 

#### bounding_box*: [`Rect`](dom.md#nodriver.cdp.dom.Rect)*

The bounding box in document coordinates. Note that scroll offset of the document is ignored.

#### dom_node_index*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The index of the related DOM node in the `domNodes` array returned by `getSnapshot`.

#### inline_text_nodes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`InlineTextBox`](#nodriver.cdp.dom_snapshot.InlineTextBox)]]* *= None*

The post-layout inline text nodes, if any.

#### is_stacking_context*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Set to true to indicate the element begins a new stacking context.

#### layout_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Contents of the LayoutText, if any.

#### paint_order*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Global paint order index, which is determined by the stacking order of the nodes. Nodes
that are painted together will have the same index. Only provided if includePaintOrder in
getSnapshot was true.

#### style_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]* *= None*

Index into the `computedStyles` array returned by `getSnapshot`.

### *class* ComputedStyle(properties)

A subset of the full ComputedStyle as defined by the request whitelist.

* **Parameters:**
  **properties** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*NameValue*](#nodriver.cdp.dom_snapshot.NameValue)*]*) – 

#### properties*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NameValue`](#nodriver.cdp.dom_snapshot.NameValue)]*

Name/value pairs of computed style properties.

### *class* NameValue(name, value)

A name/value pair.

* **Parameters:**
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Attribute/property name.

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Attribute/property value.

### *class* StringIndex

Index of the string in the strings table.

### *class* ArrayOfStrings(iterable=(), /)

Index of the string in the strings table.

### *class* RareStringData(index, value)

Data that is only present on rare nodes.

* **Parameters:**
  * **index** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) – 
  * **value** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)*]*) – 

#### index*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

#### value*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)]*

### *class* RareBooleanData(index)

* **Parameters:**
  **index** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) – 

#### index*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

### *class* RareIntegerData(index, value)

* **Parameters:**
  * **index** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) – 
  * **value** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) – 

#### index*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

#### value*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

### *class* Rectangle(iterable=(), /)

### *class* DocumentSnapshot(document_url, title, base_url, content_language, encoding_name, public_id, system_id, frame_id, nodes, layout, text_boxes, scroll_offset_x=None, scroll_offset_y=None, content_width=None, content_height=None)

Document snapshot.

* **Parameters:**
  * **document_url** ([*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)) – 
  * **title** ([*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)) – 
  * **base_url** ([*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)) – 
  * **content_language** ([*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)) – 
  * **encoding_name** ([*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)) – 
  * **public_id** ([*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)) – 
  * **system_id** ([*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)) – 
  * **frame_id** ([*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)) – 
  * **nodes** ([*NodeTreeSnapshot*](#nodriver.cdp.dom_snapshot.NodeTreeSnapshot)) – 
  * **layout** ([*LayoutTreeSnapshot*](#nodriver.cdp.dom_snapshot.LayoutTreeSnapshot)) – 
  * **text_boxes** ([*TextBoxSnapshot*](#nodriver.cdp.dom_snapshot.TextBoxSnapshot)) – 
  * **scroll_offset_x** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **scroll_offset_y** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **content_width** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **content_height** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 

#### base_url*: [`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)*

Base URL that `Document` or `FrameOwner` node uses for URL completion.

#### content_height*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Document content height.

#### content_language*: [`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)*

Contains the document’s content language.

#### content_width*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Document content width.

#### document_url*: [`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)*

Document URL that `Document` or `FrameOwner` node points to.

#### encoding_name*: [`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)*

Contains the document’s character set encoding.

#### frame_id*: [`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)*

Frame ID for frame owner elements and also for the document node.

#### layout*: [`LayoutTreeSnapshot`](#nodriver.cdp.dom_snapshot.LayoutTreeSnapshot)*

The nodes in the layout tree.

#### nodes*: [`NodeTreeSnapshot`](#nodriver.cdp.dom_snapshot.NodeTreeSnapshot)*

A table with dom nodes.

#### public_id*: [`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)*

`DocumentType` node’s publicId.

#### scroll_offset_x*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Horizontal scroll offset.

#### scroll_offset_y*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Vertical scroll offset.

#### system_id*: [`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)*

`DocumentType` node’s systemId.

#### text_boxes*: [`TextBoxSnapshot`](#nodriver.cdp.dom_snapshot.TextBoxSnapshot)*

The post-layout inline text nodes.

#### title*: [`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)*

Document title.

### *class* NodeTreeSnapshot(parent_index=None, node_type=None, shadow_root_type=None, node_name=None, node_value=None, backend_node_id=None, attributes=None, text_value=None, input_value=None, input_checked=None, option_selected=None, content_document_index=None, pseudo_type=None, pseudo_identifier=None, is_clickable=None, current_source_url=None, origin_url=None)

Table containing nodes.

* **Parameters:**
  * **parent_index** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]* *|* *None*) – 
  * **node_type** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]* *|* *None*) – 
  * **shadow_root_type** ([*RareStringData*](#nodriver.cdp.dom_snapshot.RareStringData) *|* *None*) – 
  * **node_name** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)*]* *|* *None*) – 
  * **node_value** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)*]* *|* *None*) – 
  * **backend_node_id** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*BackendNodeId*](dom.md#nodriver.cdp.dom.BackendNodeId)*]* *|* *None*) – 
  * **attributes** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*ArrayOfStrings*](#nodriver.cdp.dom_snapshot.ArrayOfStrings)*]* *|* *None*) – 
  * **text_value** ([*RareStringData*](#nodriver.cdp.dom_snapshot.RareStringData) *|* *None*) – 
  * **input_value** ([*RareStringData*](#nodriver.cdp.dom_snapshot.RareStringData) *|* *None*) – 
  * **input_checked** ([*RareBooleanData*](#nodriver.cdp.dom_snapshot.RareBooleanData) *|* *None*) – 
  * **option_selected** ([*RareBooleanData*](#nodriver.cdp.dom_snapshot.RareBooleanData) *|* *None*) – 
  * **content_document_index** ([*RareIntegerData*](#nodriver.cdp.dom_snapshot.RareIntegerData) *|* *None*) – 
  * **pseudo_type** ([*RareStringData*](#nodriver.cdp.dom_snapshot.RareStringData) *|* *None*) – 
  * **pseudo_identifier** ([*RareStringData*](#nodriver.cdp.dom_snapshot.RareStringData) *|* *None*) – 
  * **is_clickable** ([*RareBooleanData*](#nodriver.cdp.dom_snapshot.RareBooleanData) *|* *None*) – 
  * **current_source_url** ([*RareStringData*](#nodriver.cdp.dom_snapshot.RareStringData) *|* *None*) – 
  * **origin_url** ([*RareStringData*](#nodriver.cdp.dom_snapshot.RareStringData) *|* *None*) – 

#### attributes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ArrayOfStrings`](#nodriver.cdp.dom_snapshot.ArrayOfStrings)]]* *= None*

Attributes of an `Element` node. Flatten name, value pairs.

#### backend_node_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]]* *= None*

`Node`’s id, corresponds to DOM.Node.backendNodeId.

#### content_document_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RareIntegerData`](#nodriver.cdp.dom_snapshot.RareIntegerData)]* *= None*

The index of the document in the list of the snapshot documents.

#### current_source_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RareStringData`](#nodriver.cdp.dom_snapshot.RareStringData)]* *= None*

The selected url for nodes with a srcset attribute.

#### input_checked*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RareBooleanData`](#nodriver.cdp.dom_snapshot.RareBooleanData)]* *= None*

Only set for radio and checkbox input elements, indicates if the element has been checked

#### input_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RareStringData`](#nodriver.cdp.dom_snapshot.RareStringData)]* *= None*

Only set for input elements, contains the input’s associated text value.

#### is_clickable*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RareBooleanData`](#nodriver.cdp.dom_snapshot.RareBooleanData)]* *= None*

Whether this DOM node responds to mouse clicks. This includes nodes that have had click
event listeners attached via JavaScript as well as anchor tags that naturally navigate when
clicked.

#### node_name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)]]* *= None*

`Node`’s nodeName.

#### node_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]]* *= None*

`Node`’s nodeType.

#### node_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)]]* *= None*

`Node`’s nodeValue.

#### option_selected*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RareBooleanData`](#nodriver.cdp.dom_snapshot.RareBooleanData)]* *= None*

Only set for option elements, indicates if the element has been selected

#### origin_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RareStringData`](#nodriver.cdp.dom_snapshot.RareStringData)]* *= None*

The url of the script (if any) that generates this node.

#### parent_index*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]]* *= None*

Parent node index.

#### pseudo_identifier*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RareStringData`](#nodriver.cdp.dom_snapshot.RareStringData)]* *= None*

Pseudo element identifier for this node. Only present if there is a
valid pseudoType.

#### pseudo_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RareStringData`](#nodriver.cdp.dom_snapshot.RareStringData)]* *= None*

Type of a pseudo element node.

#### shadow_root_type*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RareStringData`](#nodriver.cdp.dom_snapshot.RareStringData)]* *= None*

Type of the shadow root the `Node` is in. String values are equal to the `ShadowRootType` enum.

#### text_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RareStringData`](#nodriver.cdp.dom_snapshot.RareStringData)]* *= None*

Only set for textarea elements, contains the text value.

### *class* LayoutTreeSnapshot(node_index, styles, bounds, text, stacking_contexts, paint_orders=None, offset_rects=None, scroll_rects=None, client_rects=None, blended_background_colors=None, text_color_opacities=None)

Table of details of an element in the DOM tree with a LayoutObject.

* **Parameters:**
  * **node_index** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) – 
  * **styles** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*ArrayOfStrings*](#nodriver.cdp.dom_snapshot.ArrayOfStrings)*]*) – 
  * **bounds** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*Rectangle*](#nodriver.cdp.dom_snapshot.Rectangle)*]*) – 
  * **text** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)*]*) – 
  * **stacking_contexts** ([*RareBooleanData*](#nodriver.cdp.dom_snapshot.RareBooleanData)) – 
  * **paint_orders** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]* *|* *None*) – 
  * **offset_rects** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*Rectangle*](#nodriver.cdp.dom_snapshot.Rectangle)*]* *|* *None*) – 
  * **scroll_rects** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*Rectangle*](#nodriver.cdp.dom_snapshot.Rectangle)*]* *|* *None*) – 
  * **client_rects** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*Rectangle*](#nodriver.cdp.dom_snapshot.Rectangle)*]* *|* *None*) – 
  * **blended_background_colors** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*StringIndex*](#nodriver.cdp.dom_snapshot.StringIndex)*]* *|* *None*) – 
  * **text_color_opacities** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*float*](https://docs.python.org/3/library/functions.html#float)*]* *|* *None*) – 

#### blended_background_colors*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)]]* *= None*

The list of background colors that are blended with colors of overlapping elements.

#### bounds*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Rectangle`](#nodriver.cdp.dom_snapshot.Rectangle)]*

The absolute position bounding box.

#### client_rects*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Rectangle`](#nodriver.cdp.dom_snapshot.Rectangle)]]* *= None*

The client rect of nodes. Only available when includeDOMRects is set to true

#### node_index*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

Index of the corresponding node in the `NodeTreeSnapshot` array returned by `captureSnapshot`.

#### offset_rects*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Rectangle`](#nodriver.cdp.dom_snapshot.Rectangle)]]* *= None*

The offset rect of nodes. Only available when includeDOMRects is set to true

#### paint_orders*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]]* *= None*

Global paint order index, which is determined by the stacking order of the nodes. Nodes
that are painted together will have the same index. Only provided if includePaintOrder in
captureSnapshot was true.

#### scroll_rects*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Rectangle`](#nodriver.cdp.dom_snapshot.Rectangle)]]* *= None*

The scroll rect of nodes. Only available when includeDOMRects is set to true

#### stacking_contexts*: [`RareBooleanData`](#nodriver.cdp.dom_snapshot.RareBooleanData)*

Stacking context information.

#### styles*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ArrayOfStrings`](#nodriver.cdp.dom_snapshot.ArrayOfStrings)]*

Array of indexes specifying computed style strings, filtered according to the `computedStyles` parameter passed to `captureSnapshot`.

#### text*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`StringIndex`](#nodriver.cdp.dom_snapshot.StringIndex)]*

Contents of the LayoutText, if any.

#### text_color_opacities*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`float`](https://docs.python.org/3/library/functions.html#float)]]* *= None*

The list of computed text opacities.

### *class* TextBoxSnapshot(layout_index, bounds, start, length)

Table of details of the post layout rendered text positions. The exact layout should not be regarded as
stable and may change between versions.

* **Parameters:**
  * **layout_index** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) – 
  * **bounds** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*Rectangle*](#nodriver.cdp.dom_snapshot.Rectangle)*]*) – 
  * **start** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) – 
  * **length** ([*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) – 

#### bounds*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Rectangle`](#nodriver.cdp.dom_snapshot.Rectangle)]*

The absolute position bounding box.

#### layout_index*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

Index of the layout tree node that owns this box collection.

#### length*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

The number of characters in this post layout textbox substring. Characters that would be
represented as a surrogate pair in UTF-16 have length 2.

#### start*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

The starting index in characters, for this post layout textbox substring. Characters that
would be represented as a surrogate pair in UTF-16 have length 2.

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../quickstart.md#getting-started-commands).

### capture_snapshot(computed_styles, include_paint_order=None, include_dom_rects=None, include_blended_background_colors=None, include_text_color_opacities=None)

Returns a document snapshot, including the full DOM tree of the root node (including iframes,
template contents, and imported documents) in a flattened array, as well as layout and
white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
flattened.

* **Parameters:**
  * **computed_styles** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – Whitelist of computed styles to return.
  * **include_paint_order** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to include layout object paint orders into the snapshot.
  * **include_dom_rects** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to include DOM rectangles (offsetRects, clientRects, scrollRects) into the snapshot
  * **include_blended_background_colors** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether to include blended background colors in the snapshot (default: false). Blended background color is achieved by blending background colors of all elements that overlap with the current element.
  * **include_text_color_opacities** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – **(EXPERIMENTAL)** *(Optional)* Whether to include text color opacity in the snapshot (default: false). An element might have the opacity property set that affects the text color of the element. The final text color opacity is computed based on the opacity of all overlapping elements.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`DocumentSnapshot`](#nodriver.cdp.dom_snapshot.DocumentSnapshot)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]]
* **Returns:**
  A tuple with the following items:
  1. **documents** - The nodes in the DOM tree. The DOMNode at index 0 corresponds to the root document.
  2. **strings** - Shared string table that all string properties refer to with indexes.

### disable()

Disables DOM snapshot agent for the given page.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables DOM snapshot agent for the given page.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_snapshot(computed_style_whitelist, include_event_listeners=None, include_paint_order=None, include_user_agent_shadow_tree=None)

Returns a document snapshot, including the full DOM tree of the root node (including iframes,
template contents, and imported documents) in a flattened array, as well as layout and
white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
flattened.

#### Deprecated
Deprecated since version 1.3.

* **Parameters:**
  * **computed_style_whitelist** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – Whitelist of computed styles to return.
  * **include_event_listeners** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether or not to retrieve details of DOM listeners (default false).
  * **include_paint_order** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to determine and include the paint order index of LayoutTreeNodes (default false).
  * **include_user_agent_shadow_tree** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to include UA shadow tree in the snapshot (default false).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`DOMNode`](#nodriver.cdp.dom_snapshot.DOMNode)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`LayoutTreeNode`](#nodriver.cdp.dom_snapshot.LayoutTreeNode)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ComputedStyle`](#nodriver.cdp.dom_snapshot.ComputedStyle)]]]
* **Returns:**
  A tuple with the following items:
  1. **domNodes** - The nodes in the DOM tree. The DOMNode at index 0 corresponds to the root document.
  2. **layoutTreeNodes** - The nodes in the layout tree.
  3. **computedStyles** - Whitelisted ComputedStyle properties for each node in the layout tree.

#### Deprecated
Deprecated since version 1.3.

## Events

*There are no events in this module.*
