# Overlay

This domain provides various functionality related to drawing atop the inspected page.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.overlay"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* SourceOrderConfig(parent_outline_color, child_outline_color)

Configuration data for drawing the source order of an elements children.

* **Parameters:**
  * **parent_outline_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA)) – 
  * **child_outline_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA)) – 

#### child_outline_color*: [`RGBA`](dom.md#nodriver.cdp.dom.RGBA)*

the color to outline the child elements in.

#### parent_outline_color*: [`RGBA`](dom.md#nodriver.cdp.dom.RGBA)*

the color to outline the givent element in.

### *class* GridHighlightConfig(show_grid_extension_lines=None, show_positive_line_numbers=None, show_negative_line_numbers=None, show_area_names=None, show_line_names=None, show_track_sizes=None, grid_border_color=None, cell_border_color=None, row_line_color=None, column_line_color=None, grid_border_dash=None, cell_border_dash=None, row_line_dash=None, column_line_dash=None, row_gap_color=None, row_hatch_color=None, column_gap_color=None, column_hatch_color=None, area_border_color=None, grid_background_color=None)

Configuration data for the highlighting of Grid elements.

* **Parameters:**
  * **show_grid_extension_lines** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **show_positive_line_numbers** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **show_negative_line_numbers** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **show_area_names** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **show_line_names** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **show_track_sizes** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **grid_border_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **cell_border_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **row_line_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **column_line_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **grid_border_dash** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **cell_border_dash** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **row_line_dash** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **column_line_dash** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **row_gap_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **row_hatch_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **column_gap_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **column_hatch_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **area_border_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **grid_background_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 

#### area_border_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The named grid areas border color (Default

#### cell_border_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent). Deprecated, please use rowLineColor and columnLineColor instead.

* **Type:**
  The cell border color (default

#### cell_border_dash*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false). Deprecated, please us rowLineDash and columnLineDash instead.

* **Type:**
  Whether the cell border is dashed (default

#### column_gap_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The column gap highlight fill color (default

#### column_hatch_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The column gap hatching fill color (default

#### column_line_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The column line color (default

#### column_line_dash*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Whether column lines are dashed (default

#### grid_background_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The grid container background color (Default

#### grid_border_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The grid container border highlight color (default

#### grid_border_dash*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Whether the grid border is dashed (default

#### row_gap_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The row gap highlight fill color (default

#### row_hatch_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The row gap hatching fill color (default

#### row_line_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The row line color (default

#### row_line_dash*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Whether row lines are dashed (default

#### show_area_names*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Show area name labels (default

#### show_grid_extension_lines*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Whether the extension lines from grid cells to the rulers should be shown (default

#### show_line_names*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Show line name labels (default

#### show_negative_line_numbers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Show Negative line number labels (default

#### show_positive_line_numbers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Show Positive line number labels (default

#### show_track_sizes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Show track size labels (default

### *class* FlexContainerHighlightConfig(container_border=None, line_separator=None, item_separator=None, main_distributed_space=None, cross_distributed_space=None, row_gap_space=None, column_gap_space=None, cross_alignment=None)

Configuration data for the highlighting of Flex container elements.

* **Parameters:**
  * **container_border** ([*LineStyle*](#nodriver.cdp.overlay.LineStyle) *|* *None*) – 
  * **line_separator** ([*LineStyle*](#nodriver.cdp.overlay.LineStyle) *|* *None*) – 
  * **item_separator** ([*LineStyle*](#nodriver.cdp.overlay.LineStyle) *|* *None*) – 
  * **main_distributed_space** ([*BoxStyle*](#nodriver.cdp.overlay.BoxStyle) *|* *None*) – 
  * **cross_distributed_space** ([*BoxStyle*](#nodriver.cdp.overlay.BoxStyle) *|* *None*) – 
  * **row_gap_space** ([*BoxStyle*](#nodriver.cdp.overlay.BoxStyle) *|* *None*) – 
  * **column_gap_space** ([*BoxStyle*](#nodriver.cdp.overlay.BoxStyle) *|* *None*) – 
  * **cross_alignment** ([*LineStyle*](#nodriver.cdp.overlay.LineStyle) *|* *None*) – 

#### column_gap_space*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BoxStyle`](#nodriver.cdp.overlay.BoxStyle)]* *= None*

Style of empty space caused by columns gaps (gap/column-gap).

#### container_border*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LineStyle`](#nodriver.cdp.overlay.LineStyle)]* *= None*

The style of the container border

#### cross_alignment*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LineStyle`](#nodriver.cdp.overlay.LineStyle)]* *= None*

Style of the self-alignment line (align-items).

#### cross_distributed_space*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BoxStyle`](#nodriver.cdp.overlay.BoxStyle)]* *= None*

Style of content-distribution space on the cross axis (align-content).

#### item_separator*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LineStyle`](#nodriver.cdp.overlay.LineStyle)]* *= None*

The style of the separator between items

#### line_separator*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LineStyle`](#nodriver.cdp.overlay.LineStyle)]* *= None*

The style of the separator between lines

#### main_distributed_space*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BoxStyle`](#nodriver.cdp.overlay.BoxStyle)]* *= None*

Style of content-distribution space on the main axis (justify-content).

#### row_gap_space*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BoxStyle`](#nodriver.cdp.overlay.BoxStyle)]* *= None*

Style of empty space caused by row gaps (gap/row-gap).

### *class* FlexItemHighlightConfig(base_size_box=None, base_size_border=None, flexibility_arrow=None)

Configuration data for the highlighting of Flex item elements.

* **Parameters:**
  * **base_size_box** ([*BoxStyle*](#nodriver.cdp.overlay.BoxStyle) *|* *None*) – 
  * **base_size_border** ([*LineStyle*](#nodriver.cdp.overlay.LineStyle) *|* *None*) – 
  * **flexibility_arrow** ([*LineStyle*](#nodriver.cdp.overlay.LineStyle) *|* *None*) – 

#### base_size_border*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LineStyle`](#nodriver.cdp.overlay.LineStyle)]* *= None*

Style of the border around the box representing the item’s base size

#### base_size_box*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BoxStyle`](#nodriver.cdp.overlay.BoxStyle)]* *= None*

Style of the box representing the item’s base size

#### flexibility_arrow*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LineStyle`](#nodriver.cdp.overlay.LineStyle)]* *= None*

Style of the arrow representing if the item grew or shrank

### *class* LineStyle(color=None, pattern=None)

Style information for drawing a line.

* **Parameters:**
  * **color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **pattern** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent)

* **Type:**
  The color of the line (default

#### pattern*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

solid)

* **Type:**
  The line pattern (default

### *class* BoxStyle(fill_color=None, hatch_color=None)

Style information for drawing a box.

* **Parameters:**
  * **fill_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **hatch_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 

#### fill_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent)

* **Type:**
  The background color for the box (default

#### hatch_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent)

* **Type:**
  The hatching color for the box (default

### *class* ContrastAlgorithm(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### AA *= 'aa'*

#### AAA *= 'aaa'*

#### APCA *= 'apca'*

### *class* HighlightConfig(show_info=None, show_styles=None, show_rulers=None, show_accessibility_info=None, show_extension_lines=None, content_color=None, padding_color=None, border_color=None, margin_color=None, event_target_color=None, shape_color=None, shape_margin_color=None, css_grid_color=None, color_format=None, grid_highlight_config=None, flex_container_highlight_config=None, flex_item_highlight_config=None, contrast_algorithm=None, container_query_container_highlight_config=None)

Configuration data for the highlighting of page elements.

* **Parameters:**
  * **show_info** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **show_styles** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **show_rulers** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **show_accessibility_info** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **show_extension_lines** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **content_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **padding_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **border_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **margin_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **event_target_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **shape_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **shape_margin_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **css_grid_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **color_format** ([*ColorFormat*](#nodriver.cdp.overlay.ColorFormat) *|* *None*) – 
  * **grid_highlight_config** ([*GridHighlightConfig*](#nodriver.cdp.overlay.GridHighlightConfig) *|* *None*) – 
  * **flex_container_highlight_config** ([*FlexContainerHighlightConfig*](#nodriver.cdp.overlay.FlexContainerHighlightConfig) *|* *None*) – 
  * **flex_item_highlight_config** ([*FlexItemHighlightConfig*](#nodriver.cdp.overlay.FlexItemHighlightConfig) *|* *None*) – 
  * **contrast_algorithm** ([*ContrastAlgorithm*](#nodriver.cdp.overlay.ContrastAlgorithm) *|* *None*) – 
  * **container_query_container_highlight_config** ([*ContainerQueryContainerHighlightConfig*](#nodriver.cdp.overlay.ContainerQueryContainerHighlightConfig) *|* *None*) – 

#### border_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The border highlight fill color (default

#### color_format*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ColorFormat`](#nodriver.cdp.overlay.ColorFormat)]* *= None*

hex).

* **Type:**
  The color format used to format color styles (default

#### container_query_container_highlight_config*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ContainerQueryContainerHighlightConfig`](#nodriver.cdp.overlay.ContainerQueryContainerHighlightConfig)]* *= None*

all transparent).

* **Type:**
  The container query container highlight configuration (default

#### content_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The content box highlight fill color (default

#### contrast_algorithm*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ContrastAlgorithm`](#nodriver.cdp.overlay.ContrastAlgorithm)]* *= None*

aa).

* **Type:**
  The contrast algorithm to use for the contrast ratio (default

#### css_grid_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The grid layout color (default

#### event_target_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The event target element highlight fill color (default

#### flex_container_highlight_config*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FlexContainerHighlightConfig`](#nodriver.cdp.overlay.FlexContainerHighlightConfig)]* *= None*

all transparent).

* **Type:**
  The flex container highlight configuration (default

#### flex_item_highlight_config*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FlexItemHighlightConfig`](#nodriver.cdp.overlay.FlexItemHighlightConfig)]* *= None*

all transparent).

* **Type:**
  The flex item highlight configuration (default

#### grid_highlight_config*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`GridHighlightConfig`](#nodriver.cdp.overlay.GridHighlightConfig)]* *= None*

all transparent).

* **Type:**
  The grid layout highlight configuration (default

#### margin_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The margin highlight fill color (default

#### padding_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The padding highlight fill color (default

#### shape_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The shape outside fill color (default

#### shape_margin_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The shape margin fill color (default

#### show_accessibility_info*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

true).

* **Type:**
  Whether the a11y info should be shown (default

#### show_extension_lines*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Whether the extension lines from node to the rulers should be shown (default

#### show_info*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Whether the node info tooltip should be shown (default

#### show_rulers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Whether the rulers should be shown (default

#### show_styles*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

false).

* **Type:**
  Whether the node styles in the tooltip (default

### *class* ColorFormat(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### HEX_ *= 'hex'*

#### HSL *= 'hsl'*

#### HWB *= 'hwb'*

#### RGB *= 'rgb'*

### *class* GridNodeHighlightConfig(grid_highlight_config, node_id)

Configurations for Persistent Grid Highlight

* **Parameters:**
  * **grid_highlight_config** ([*GridHighlightConfig*](#nodriver.cdp.overlay.GridHighlightConfig)) – 
  * **node_id** ([*NodeId*](dom.md#nodriver.cdp.dom.NodeId)) – 

#### grid_highlight_config*: [`GridHighlightConfig`](#nodriver.cdp.overlay.GridHighlightConfig)*

A descriptor for the highlight appearance.

#### node_id*: [`NodeId`](dom.md#nodriver.cdp.dom.NodeId)*

Identifier of the node to highlight.

### *class* FlexNodeHighlightConfig(flex_container_highlight_config, node_id)

* **Parameters:**
  * **flex_container_highlight_config** ([*FlexContainerHighlightConfig*](#nodriver.cdp.overlay.FlexContainerHighlightConfig)) – 
  * **node_id** ([*NodeId*](dom.md#nodriver.cdp.dom.NodeId)) – 

#### flex_container_highlight_config*: [`FlexContainerHighlightConfig`](#nodriver.cdp.overlay.FlexContainerHighlightConfig)*

A descriptor for the highlight appearance of flex containers.

#### node_id*: [`NodeId`](dom.md#nodriver.cdp.dom.NodeId)*

Identifier of the node to highlight.

### *class* ScrollSnapContainerHighlightConfig(snapport_border=None, snap_area_border=None, scroll_margin_color=None, scroll_padding_color=None)

* **Parameters:**
  * **snapport_border** ([*LineStyle*](#nodriver.cdp.overlay.LineStyle) *|* *None*) – 
  * **snap_area_border** ([*LineStyle*](#nodriver.cdp.overlay.LineStyle) *|* *None*) – 
  * **scroll_margin_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **scroll_padding_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 

#### scroll_margin_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The margin highlight fill color (default

#### scroll_padding_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The padding highlight fill color (default

#### snap_area_border*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LineStyle`](#nodriver.cdp.overlay.LineStyle)]* *= None*

transparent)

* **Type:**
  The style of the snap area border (default

#### snapport_border*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LineStyle`](#nodriver.cdp.overlay.LineStyle)]* *= None*

transparent)

* **Type:**
  The style of the snapport border (default

### *class* ScrollSnapHighlightConfig(scroll_snap_container_highlight_config, node_id)

* **Parameters:**
  * **scroll_snap_container_highlight_config** ([*ScrollSnapContainerHighlightConfig*](#nodriver.cdp.overlay.ScrollSnapContainerHighlightConfig)) – 
  * **node_id** ([*NodeId*](dom.md#nodriver.cdp.dom.NodeId)) – 

#### node_id*: [`NodeId`](dom.md#nodriver.cdp.dom.NodeId)*

Identifier of the node to highlight.

#### scroll_snap_container_highlight_config*: [`ScrollSnapContainerHighlightConfig`](#nodriver.cdp.overlay.ScrollSnapContainerHighlightConfig)*

A descriptor for the highlight appearance of scroll snap containers.

### *class* HingeConfig(rect, content_color=None, outline_color=None)

Configuration for dual screen hinge

* **Parameters:**
  * **rect** ([*Rect*](dom.md#nodriver.cdp.dom.Rect)) – 
  * **content_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **outline_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 

#### content_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

a dark color).

* **Type:**
  The content box highlight fill color (default

#### outline_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The content box highlight outline color (default

#### rect*: [`Rect`](dom.md#nodriver.cdp.dom.Rect)*

A rectangle represent hinge

### *class* WindowControlsOverlayConfig(show_css, selected_platform, theme_color)

Configuration for Window Controls Overlay

* **Parameters:**
  * **show_css** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **selected_platform** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **theme_color** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

#### selected_platform*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Seleted platforms to show the overlay.

#### show_css*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether the title bar CSS should be shown when emulating the Window Controls Overlay.

#### theme_color*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The theme color defined in app manifest.

### *class* ContainerQueryHighlightConfig(container_query_container_highlight_config, node_id)

* **Parameters:**
  * **container_query_container_highlight_config** ([*ContainerQueryContainerHighlightConfig*](#nodriver.cdp.overlay.ContainerQueryContainerHighlightConfig)) – 
  * **node_id** ([*NodeId*](dom.md#nodriver.cdp.dom.NodeId)) – 

#### container_query_container_highlight_config*: [`ContainerQueryContainerHighlightConfig`](#nodriver.cdp.overlay.ContainerQueryContainerHighlightConfig)*

A descriptor for the highlight appearance of container query containers.

#### node_id*: [`NodeId`](dom.md#nodriver.cdp.dom.NodeId)*

Identifier of the container node to highlight.

### *class* ContainerQueryContainerHighlightConfig(container_border=None, descendant_border=None)

* **Parameters:**
  * **container_border** ([*LineStyle*](#nodriver.cdp.overlay.LineStyle) *|* *None*) – 
  * **descendant_border** ([*LineStyle*](#nodriver.cdp.overlay.LineStyle) *|* *None*) – 

#### container_border*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LineStyle`](#nodriver.cdp.overlay.LineStyle)]* *= None*

The style of the container border.

#### descendant_border*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LineStyle`](#nodriver.cdp.overlay.LineStyle)]* *= None*

The style of the descendants’ borders.

### *class* IsolatedElementHighlightConfig(isolation_mode_highlight_config, node_id)

* **Parameters:**
  * **isolation_mode_highlight_config** ([*IsolationModeHighlightConfig*](#nodriver.cdp.overlay.IsolationModeHighlightConfig)) – 
  * **node_id** ([*NodeId*](dom.md#nodriver.cdp.dom.NodeId)) – 

#### isolation_mode_highlight_config*: [`IsolationModeHighlightConfig`](#nodriver.cdp.overlay.IsolationModeHighlightConfig)*

A descriptor for the highlight appearance of an element in isolation mode.

#### node_id*: [`NodeId`](dom.md#nodriver.cdp.dom.NodeId)*

Identifier of the isolated element to highlight.

### *class* IsolationModeHighlightConfig(resizer_color=None, resizer_handle_color=None, mask_color=None)

* **Parameters:**
  * **resizer_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **resizer_handle_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 
  * **mask_color** ([*RGBA*](dom.md#nodriver.cdp.dom.RGBA) *|* *None*) – 

#### mask_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The fill color for the mask covering non-isolated elements (default

#### resizer_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The fill color of the resizers (default

#### resizer_handle_color*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]* *= None*

transparent).

* **Type:**
  The fill color for resizer handles (default

### *class* InspectMode(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

#### CAPTURE_AREA_SCREENSHOT *= 'captureAreaScreenshot'*

#### NONE *= 'none'*

#### SEARCH_FOR_NODE *= 'searchForNode'*

#### SEARCH_FOR_UA_SHADOW_DOM *= 'searchForUAShadowDOM'*

#### SHOW_DISTANCES *= 'showDistances'*

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

Disables domain notifications.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables domain notifications.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_grid_highlight_objects_for_test(node_ids)

For Persistent Grid testing.

* **Parameters:**
  **node_ids** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NodeId`](dom.md#nodriver.cdp.dom.NodeId)]) – Ids of the node to get highlight object for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]
* **Returns:**
  Grid Highlight data for the node ids provided.

### get_highlight_object_for_test(node_id, include_distance=None, include_style=None, color_format=None, show_accessibility_info=None)

For testing.

* **Parameters:**
  * **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – Id of the node to get highlight object for.
  * **include_distance** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to include distance info.
  * **include_style** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to include style info.
  * **color_format** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ColorFormat`](#nodriver.cdp.overlay.ColorFormat)]) – *(Optional)* The color format to get config with (default: hex).
  * **show_accessibility_info** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* Whether to show accessibility info (default: true).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]
* **Returns:**
  Highlight data for the node.

### get_source_order_highlight_object_for_test(node_id)

For Source Order Viewer testing.

* **Parameters:**
  **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – Id of the node to highlight.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)]
* **Returns:**
  Source order highlight data for the node id provided.

### hide_highlight()

Hides any highlight.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### highlight_frame(frame_id, content_color=None, content_outline_color=None)

Highlights owner element of the frame with given id.
Deprecated: Doesn’t work reliablity and cannot be fixed due to process
separatation (the owner node might be in a different process). Determine
the owner node in the client and use highlightNode.

#### Deprecated
Deprecated since version 1.3.

* **Parameters:**
  * **frame_id** ([`FrameId`](page.md#nodriver.cdp.page.FrameId)) – Identifier of the frame to highlight.
  * **content_color** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]) – *(Optional)* The content box highlight fill color (default: transparent).
  * **content_outline_color** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]) – *(Optional)* The content box highlight outline color (default: transparent).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### highlight_node(highlight_config, node_id=None, backend_node_id=None, object_id=None, selector=None)

Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or
objectId must be specified.

* **Parameters:**
  * **highlight_config** ([`HighlightConfig`](#nodriver.cdp.overlay.HighlightConfig)) – A descriptor for the highlight appearance.
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](dom.md#nodriver.cdp.dom.NodeId)]) – *(Optional)* Identifier of the node to highlight.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Identifier of the backend node to highlight.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* JavaScript object id of the node to be highlighted.
  * **selector** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Selectors to highlight relevant nodes.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### highlight_quad(quad, color=None, outline_color=None)

Highlights given quad. Coordinates are absolute with respect to the main frame viewport.

* **Parameters:**
  * **quad** ([`Quad`](dom.md#nodriver.cdp.dom.Quad)) – Quad to highlight
  * **color** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]) – *(Optional)* The highlight fill color (default: transparent).
  * **outline_color** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]) – *(Optional)* The highlight outline color (default: transparent).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### highlight_rect(x, y, width, height, color=None, outline_color=None)

Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport.

* **Parameters:**
  * **x** ([`int`](https://docs.python.org/3/library/functions.html#int)) – X coordinate
  * **y** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Y coordinate
  * **width** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Rectangle width
  * **height** ([`int`](https://docs.python.org/3/library/functions.html#int)) – Rectangle height
  * **color** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]) – *(Optional)* The highlight fill color (default: transparent).
  * **outline_color** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RGBA`](dom.md#nodriver.cdp.dom.RGBA)]) – *(Optional)* The highlight outline color (default: transparent).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### highlight_source_order(source_order_config, node_id=None, backend_node_id=None, object_id=None)

Highlights the source order of the children of the DOM node with given id or with the given
JavaScript object wrapper. Either nodeId or objectId must be specified.

* **Parameters:**
  * **source_order_config** ([`SourceOrderConfig`](#nodriver.cdp.overlay.SourceOrderConfig)) – A descriptor for the appearance of the overlay drawing.
  * **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](dom.md#nodriver.cdp.dom.NodeId)]) – *(Optional)* Identifier of the node to highlight.
  * **backend_node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]) – *(Optional)* Identifier of the backend node to highlight.
  * **object_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`RemoteObjectId`](runtime.md#nodriver.cdp.runtime.RemoteObjectId)]) – *(Optional)* JavaScript object id of the node to be highlighted.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_inspect_mode(mode, highlight_config=None)

Enters the ‘inspect’ mode. In this mode, elements that user is hovering over are highlighted.
Backend then generates ‘inspectNodeRequested’ event upon element selection.

* **Parameters:**
  * **mode** ([`InspectMode`](#nodriver.cdp.overlay.InspectMode)) – Set an inspection mode.
  * **highlight_config** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`HighlightConfig`](#nodriver.cdp.overlay.HighlightConfig)]) – *(Optional)* A descriptor for the highlight appearance of hovered-over nodes. May be omitted if ``enabled == false``.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_paused_in_debugger_message(message=None)

* **Parameters:**
  **message** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* The message to display, also triggers resume and step over controls.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_ad_highlights(show)

Highlights owner element of all frames detected to be ads.

* **Parameters:**
  **show** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – True for showing ad highlights
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_container_query_overlays(container_query_highlight_configs)

* **Parameters:**
  **container_query_highlight_configs** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ContainerQueryHighlightConfig`](#nodriver.cdp.overlay.ContainerQueryHighlightConfig)]) – An array of node identifiers and descriptors for the highlight appearance.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_debug_borders(show)

Requests that backend shows debug borders on layers

* **Parameters:**
  **show** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – True for showing debug borders
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_flex_overlays(flex_node_highlight_configs)

* **Parameters:**
  **flex_node_highlight_configs** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`FlexNodeHighlightConfig`](#nodriver.cdp.overlay.FlexNodeHighlightConfig)]) – An array of node identifiers and descriptors for the highlight appearance.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_fps_counter(show)

Requests that backend shows the FPS counter

* **Parameters:**
  **show** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – True for showing the FPS counter
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_grid_overlays(grid_node_highlight_configs)

Highlight multiple elements with the CSS Grid overlay.

* **Parameters:**
  **grid_node_highlight_configs** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`GridNodeHighlightConfig`](#nodriver.cdp.overlay.GridNodeHighlightConfig)]) – An array of node identifiers and descriptors for the highlight appearance.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_hinge(hinge_config=None)

Add a dual screen device hinge

* **Parameters:**
  **hinge_config** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`HingeConfig`](#nodriver.cdp.overlay.HingeConfig)]) – *(Optional)* hinge data, null means hideHinge
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_hit_test_borders(show)

Deprecated, no longer has any effect.

#### Deprecated
Deprecated since version 1.3.

* **Parameters:**
  **show** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – True for showing hit-test borders
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

#### Deprecated
Deprecated since version 1.3.

### set_show_isolated_elements(isolated_element_highlight_configs)

Show elements in isolation mode with overlays.

* **Parameters:**
  **isolated_element_highlight_configs** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`IsolatedElementHighlightConfig`](#nodriver.cdp.overlay.IsolatedElementHighlightConfig)]) – An array of node identifiers and descriptors for the highlight appearance.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_layout_shift_regions(result)

Requests that backend shows layout shift regions

* **Parameters:**
  **result** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – True for showing layout shift regions
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_paint_rects(result)

Requests that backend shows paint rectangles

* **Parameters:**
  **result** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – True for showing paint rectangles
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_scroll_bottleneck_rects(show)

Requests that backend shows scroll bottleneck rects

* **Parameters:**
  **show** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – True for showing scroll bottleneck rects
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_scroll_snap_overlays(scroll_snap_highlight_configs)

* **Parameters:**
  **scroll_snap_highlight_configs** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ScrollSnapHighlightConfig`](#nodriver.cdp.overlay.ScrollSnapHighlightConfig)]) – An array of node identifiers and descriptors for the highlight appearance.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_viewport_size_on_resize(show)

Paints viewport size upon main frame resize.

* **Parameters:**
  **show** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether to paint size or not.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_web_vitals(show)

Request that backend shows an overlay with web vital metrics.

* **Parameters:**
  **show** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_show_window_controls_overlay(window_controls_overlay_config=None)

Show Window Controls Overlay for PWA

* **Parameters:**
  **window_controls_overlay_config** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`WindowControlsOverlayConfig`](#nodriver.cdp.overlay.WindowControlsOverlayConfig)]) – *(Optional)* Window Controls Overlay data, null means hide Window Controls Overlay
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* InspectNodeRequested(backend_node_id)

Fired when the node should be inspected. This happens after call to `setInspectMode` or when
user manually inspects an element.

* **Parameters:**
  **backend_node_id** ([*BackendNodeId*](dom.md#nodriver.cdp.dom.BackendNodeId)) – 

#### backend_node_id*: [`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)*

Id of the node to inspect.

### *class* NodeHighlightRequested(node_id)

Fired when the node should be highlighted. This happens after call to `setInspectMode`.

* **Parameters:**
  **node_id** ([*NodeId*](dom.md#nodriver.cdp.dom.NodeId)) – 

#### node_id*: [`NodeId`](dom.md#nodriver.cdp.dom.NodeId)*

### *class* ScreenshotRequested(viewport)

Fired when user asks to capture screenshot of some area on the page.

* **Parameters:**
  **viewport** ([*Viewport*](page.md#nodriver.cdp.page.Viewport)) – 

#### viewport*: [`Viewport`](page.md#nodriver.cdp.page.Viewport)*

Viewport to capture, in device independent pixels (dip).

### *class* InspectModeCanceled

Fired when user cancels the inspect mode.
