DOM
===

This domain exposes DOM read/write operations. Each DOM Node is represented with its mirror object
that has an `id`. This `id` can be used to get additional information on the Node, resolve it into
the JavaScript object wrapper, etc. It is important that client receives DOM events only for the
nodes that are known to the client. Backend keeps track of the nodes that were sent to the client
and never sends the same node twice. It is client's responsibility to collect information about
the nodes that were sent to the client. Note that `iframe` owner elements will return
corresponding document elements as their child nodes.

.. module:: nodriver.cdp.dom

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: NodeId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BackendNodeId
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BackendNode
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PseudoType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ShadowRootType
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CompatibilityMode
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PhysicalAxes
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: LogicalAxes
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ScrollOrientation
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Node
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DetachedElementInfo
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: RGBA
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Quad
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: BoxModel
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ShapeOutsideInfo
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: Rect
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CSSComputedStyleProperty
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

Commands
--------

Each command is a generator function. The return
type ``Generator[x, y, z]`` indicates that the generator
*yields* arguments of type ``x``, it must be resumed with
an argument of type ``y``, and it returns type ``z``. In
this library, types ``x`` and ``y`` are the same for all
commands, and ``z`` is the return type you should pay attention
to. For more information, see
:ref:`Getting Started: Commands <getting-started-commands>`.

.. autofunction:: collect_class_names_from_subtree

.. autofunction:: copy_to

.. autofunction:: describe_node

.. autofunction:: disable

.. autofunction:: discard_search_results

.. autofunction:: enable

.. autofunction:: focus

.. autofunction:: get_anchor_element

.. autofunction:: get_attributes

.. autofunction:: get_box_model

.. autofunction:: get_container_for_node

.. autofunction:: get_content_quads

.. autofunction:: get_detached_dom_nodes

.. autofunction:: get_document

.. autofunction:: get_element_by_relation

.. autofunction:: get_file_info

.. autofunction:: get_flattened_document

.. autofunction:: get_frame_owner

.. autofunction:: get_node_for_location

.. autofunction:: get_node_stack_traces

.. autofunction:: get_nodes_for_subtree_by_style

.. autofunction:: get_outer_html

.. autofunction:: get_querying_descendants_for_container

.. autofunction:: get_relayout_boundary

.. autofunction:: get_search_results

.. autofunction:: get_top_layer_elements

.. autofunction:: hide_highlight

.. autofunction:: highlight_node

.. autofunction:: highlight_rect

.. autofunction:: mark_undoable_state

.. autofunction:: move_to

.. autofunction:: perform_search

.. autofunction:: push_node_by_path_to_frontend

.. autofunction:: push_nodes_by_backend_ids_to_frontend

.. autofunction:: query_selector

.. autofunction:: query_selector_all

.. autofunction:: redo

.. autofunction:: remove_attribute

.. autofunction:: remove_node

.. autofunction:: request_child_nodes

.. autofunction:: request_node

.. autofunction:: resolve_node

.. autofunction:: scroll_into_view_if_needed

.. autofunction:: set_attribute_value

.. autofunction:: set_attributes_as_text

.. autofunction:: set_file_input_files

.. autofunction:: set_inspected_node

.. autofunction:: set_node_name

.. autofunction:: set_node_stack_traces_enabled

.. autofunction:: set_node_value

.. autofunction:: set_outer_html

.. autofunction:: undo

Events
------

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event's attributes.

.. autoclass:: AttributeModified
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: AttributeRemoved
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: CharacterDataModified
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ChildNodeCountUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ChildNodeInserted
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ChildNodeRemoved
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DistributedNodesUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DocumentUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: InlineStyleInvalidated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PseudoElementAdded
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: TopLayerElementsUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ScrollableFlagUpdated
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: PseudoElementRemoved
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: SetChildNodes
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ShadowRootPopped
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: ShadowRootPushed
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json
