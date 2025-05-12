# CSS

This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles)
have an associated [`id`](https://docs.python.org/3/library/functions.html#id) used in subsequent operations on the related object. Each object type has
a specific [`id`](https://docs.python.org/3/library/functions.html#id) structure, and those are not interchangeable between objects of different kinds.
CSS objects can be loaded using the `get*ForNode()` calls (which accept a DOM node id). A client
can also keep track of stylesheets via the `styleSheetAdded`/`styleSheetRemoved` events and
subsequently load the required stylesheet contents using the `getStyleSheet[Text]()` methods.

*This CDP domain is experimental.*

<a id="module-nodriver.cdp.css"></a>
* [Types]()
* [Commands]()
* [Events]()

## Types

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

### *class* StyleSheetId

### *class* StyleSheetOrigin(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Stylesheet type: “injected” for stylesheets injected via extension, “user-agent” for user-agent
stylesheets, “inspector” for stylesheets created by the inspector (i.e. those holding the “via
inspector” rules), “regular” for regular stylesheets.

#### INJECTED *= 'injected'*

#### USER_AGENT *= 'user-agent'*

#### INSPECTOR *= 'inspector'*

#### REGULAR *= 'regular'*

### *class* PseudoElementMatches(pseudo_type, matches, pseudo_identifier=None)

CSS rule collection for a single pseudo style.

#### pseudo_type*: [`PseudoType`](dom.md#nodriver.cdp.dom.PseudoType)*

Pseudo element type.

#### matches*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`RuleMatch`](#nodriver.cdp.css.RuleMatch)]*

Matches of CSS rules applicable to the pseudo style.

#### pseudo_identifier*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Pseudo element custom ident.

### *class* CSSAnimationStyle(style, name=None)

CSS style coming from animations with the name of the animation.

#### style*: [`CSSStyle`](#nodriver.cdp.css.CSSStyle)*

The style coming from the animation.

#### name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The name of the animation.

### *class* InheritedStyleEntry(matched_css_rules, inline_style=None)

Inherited CSS rule collection from ancestor node.

#### matched_css_rules*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`RuleMatch`](#nodriver.cdp.css.RuleMatch)]*

Matches of CSS rules matching the ancestor node in the style inheritance chain.

#### inline_style*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSStyle`](#nodriver.cdp.css.CSSStyle)]* *= None*

The ancestor node’s inline style, if any, in the style inheritance chain.

### *class* InheritedAnimatedStyleEntry(animation_styles=None, transitions_style=None)

Inherited CSS style collection for animated styles from ancestor node.

#### animation_styles*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSAnimationStyle`](#nodriver.cdp.css.CSSAnimationStyle)]]* *= None*

Styles coming from the animations of the ancestor, if any, in the style inheritance chain.

#### transitions_style*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSStyle`](#nodriver.cdp.css.CSSStyle)]* *= None*

The style coming from the transitions of the ancestor, if any, in the style inheritance chain.

### *class* InheritedPseudoElementMatches(pseudo_elements)

Inherited pseudo element matches from pseudos of an ancestor node.

#### pseudo_elements*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PseudoElementMatches`](#nodriver.cdp.css.PseudoElementMatches)]*

Matches of pseudo styles from the pseudos of an ancestor node.

### *class* RuleMatch(rule, matching_selectors)

Match data for a CSS rule.

#### rule*: [`CSSRule`](#nodriver.cdp.css.CSSRule)*

CSS rule in the match.

#### matching_selectors*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

Matching selector indices in the rule’s selectorList selectors (0-based).

### *class* Value(text, range_=None, specificity=None)

Data for a simple selector (these are delimited by commas in a selector list).

#### text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Value text.

#### range_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceRange`](#nodriver.cdp.css.SourceRange)]* *= None*

Value range in the underlying resource (if available).

#### specificity*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Specificity`](#nodriver.cdp.css.Specificity)]* *= None*

Specificity of the selector.

### *class* Specificity(a, b, c)

Specificity:
[https://drafts.csswg.org/selectors/#specificity-rules](https://drafts.csswg.org/selectors/#specificity-rules)

#### a*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The a component, which represents the number of ID selectors.

#### b*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The b component, which represents the number of class selectors, attributes selectors, and
pseudo-classes.

#### c*: [`int`](https://docs.python.org/3/library/functions.html#int)*

The c component, which represents the number of type selectors and pseudo-elements.

### *class* SelectorList(selectors, text)

Selector list data.

#### selectors*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`Value`](#nodriver.cdp.css.Value)]*

Selectors in the list.

#### text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Rule selector text.

### *class* CSSStyleSheetHeader(style_sheet_id, frame_id, source_url, origin, title, disabled, is_inline, is_mutable, is_constructed, start_line, start_column, length, end_line, end_column, source_map_url=None, owner_node=None, has_source_url=None, loading_failed=None)

CSS stylesheet metainformation.

#### style_sheet_id*: [`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)*

The stylesheet identifier.

#### frame_id*: [`FrameId`](page.md#nodriver.cdp.page.FrameId)*

Owner frame identifier.

#### source_url*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Stylesheet resource URL. Empty if this is a constructed stylesheet created using
new CSSStyleSheet() (but non-empty if this is a constructed stylesheet imported
as a CSS module script).

#### origin*: [`StyleSheetOrigin`](#nodriver.cdp.css.StyleSheetOrigin)*

Stylesheet origin.

#### title*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Stylesheet title.

#### disabled*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Denotes whether the stylesheet is disabled.

#### is_inline*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether this stylesheet is created for STYLE tag by parser. This flag is not set for
document.written STYLE tags.

#### is_mutable*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether this stylesheet is mutable. Inline stylesheets become mutable
after they have been modified via CSSOM API.
`<link>` element’s stylesheets become mutable only if DevTools modifies them.
Constructed stylesheets (new CSSStyleSheet()) are mutable immediately after creation.

#### is_constructed*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

True if this stylesheet is created through new CSSStyleSheet() or imported as a
CSS module script.

#### start_line*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Line offset of the stylesheet within the resource (zero based).

#### start_column*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Column offset of the stylesheet within the resource (zero based).

#### length*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Size of the content (in characters).

#### end_line*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Line offset of the end of the stylesheet within the resource (zero based).

#### end_column*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Column offset of the end of the stylesheet within the resource (zero based).

#### source_map_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

URL of source map associated with the stylesheet (if any).

#### owner_node*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BackendNodeId`](dom.md#nodriver.cdp.dom.BackendNodeId)]* *= None*

The backend id for the owner node of the stylesheet.

#### has_source_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether the sourceURL field value comes from the sourceURL comment.

#### loading_failed*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

If the style sheet was loaded from a network resource, this indicates when the resource failed to load

### *class* CSSRule(selector_list, origin, style, style_sheet_id=None, nesting_selectors=None, media=None, container_queries=None, supports=None, layers=None, scopes=None, rule_types=None, starting_styles=None)

CSS rule representation.

#### selector_list*: [`SelectorList`](#nodriver.cdp.css.SelectorList)*

Rule selector data.

#### origin*: [`StyleSheetOrigin`](#nodriver.cdp.css.StyleSheetOrigin)*

Parent stylesheet’s origin.

#### style*: [`CSSStyle`](#nodriver.cdp.css.CSSStyle)*

Associated style declaration.

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

The css style sheet identifier (absent for user agent stylesheet and user-specified
stylesheet rules) this rule came from.

#### nesting_selectors*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]* *= None*

Array of selectors from ancestor style rules, sorted by distance from the current rule.

#### media*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSMedia`](#nodriver.cdp.css.CSSMedia)]]* *= None*

Media list array (for rules involving media queries). The array enumerates media queries
starting with the innermost one, going outwards.

#### container_queries*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSContainerQuery`](#nodriver.cdp.css.CSSContainerQuery)]]* *= None*

Container query list array (for rules involving container queries).
The array enumerates container queries starting with the innermost one, going outwards.

#### supports*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSSupports`](#nodriver.cdp.css.CSSSupports)]]* *= None*

@supports CSS at-rule array.
The array enumerates @supports at-rules starting with the innermost one, going outwards.

#### layers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSLayer`](#nodriver.cdp.css.CSSLayer)]]* *= None*

Cascade layer array. Contains the layer hierarchy that this rule belongs to starting
with the innermost layer and going outwards.

#### scopes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSScope`](#nodriver.cdp.css.CSSScope)]]* *= None*

@scope CSS at-rule array.
The array enumerates @scope at-rules starting with the innermost one, going outwards.

#### rule_types*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSRuleType`](#nodriver.cdp.css.CSSRuleType)]]* *= None*

The array keeps the types of ancestor CSSRules from the innermost going outwards.

#### starting_styles*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSStartingStyle`](#nodriver.cdp.css.CSSStartingStyle)]]* *= None*

@starting-style CSS at-rule array.
The array enumerates @starting-style at-rules starting with the innermost one, going outwards.

### *class* CSSRuleType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Enum indicating the type of a CSS rule, used to represent the order of a style rule’s ancestors.
This list only contains rule types that are collected during the ancestor rule collection.

#### MEDIA_RULE *= 'MediaRule'*

#### SUPPORTS_RULE *= 'SupportsRule'*

#### CONTAINER_RULE *= 'ContainerRule'*

#### LAYER_RULE *= 'LayerRule'*

#### SCOPE_RULE *= 'ScopeRule'*

#### STYLE_RULE *= 'StyleRule'*

#### STARTING_STYLE_RULE *= 'StartingStyleRule'*

### *class* RuleUsage(style_sheet_id, start_offset, end_offset, used)

CSS coverage information.

#### style_sheet_id*: [`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)*

The css style sheet identifier (absent for user agent stylesheet and user-specified
stylesheet rules) this rule came from.

#### start_offset*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Offset of the start of the rule (including selector) from the beginning of the stylesheet.

#### end_offset*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Offset of the end of the rule body from the beginning of the stylesheet.

#### used*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Indicates whether the rule was actually used by some element in the page.

### *class* SourceRange(start_line, start_column, end_line, end_column)

Text range within a resource. All numbers are zero-based.

#### start_line*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Start line of range.

#### start_column*: [`int`](https://docs.python.org/3/library/functions.html#int)*

Start column of range (inclusive).

#### end_line*: [`int`](https://docs.python.org/3/library/functions.html#int)*

End line of range

#### end_column*: [`int`](https://docs.python.org/3/library/functions.html#int)*

End column of range (exclusive).

### *class* ShorthandEntry(name, value, important=None)

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Shorthand name.

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Shorthand value.

#### important*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether the property has “!important” annotation (implies `false` if absent).

### *class* CSSComputedStyleProperty(name, value)

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Computed style property name.

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Computed style property value.

### *class* CSSStyle(css_properties, shorthand_entries, style_sheet_id=None, css_text=None, range_=None)

CSS style representation.

#### css_properties*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSProperty`](#nodriver.cdp.css.CSSProperty)]*

CSS properties in the style.

#### shorthand_entries*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`ShorthandEntry`](#nodriver.cdp.css.ShorthandEntry)]*

Computed values for all shorthands found in the style.

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

The css style sheet identifier (absent for user agent stylesheet and user-specified
stylesheet rules) this rule came from.

#### css_text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Style declaration text (if available).

#### range_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceRange`](#nodriver.cdp.css.SourceRange)]* *= None*

Style declaration range in the enclosing stylesheet (if available).

### *class* CSSProperty(name, value, important=None, implicit=None, text=None, parsed_ok=None, disabled=None, range_=None, longhand_properties=None)

CSS property declaration data.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The property name.

#### value*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The property value.

#### important*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether the property has “!important” annotation (implies `false` if absent).

#### implicit*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether the property is implicit (implies `false` if absent).

#### text*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The full property text as specified in the style.

#### parsed_ok*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether the property is understood by the browser (implies `true` if absent).

#### disabled*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether the property is disabled by the user (present for source-based properties only).

#### range_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceRange`](#nodriver.cdp.css.SourceRange)]* *= None*

The entire property range in the enclosing style declaration (if available).

#### longhand_properties*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSProperty`](#nodriver.cdp.css.CSSProperty)]]* *= None*

Parsed longhand components of this property if it is a shorthand.
This field will be empty if the given property is not a shorthand.

### *class* CSSMedia(text, source, source_url=None, range_=None, style_sheet_id=None, media_list=None)

CSS media rule descriptor.

#### text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Media query text.

#### source*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

“mediaRule” if specified by a @media rule, “importRule” if
specified by an @import rule, “linkedSheet” if specified by a “media” attribute in a linked
stylesheet’s LINK tag, “inlineSheet” if specified by a “media” attribute in an inline
stylesheet’s STYLE tag.

* **Type:**
  Source of the media query

#### source_url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

URL of the document containing the media query description.

#### range_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceRange`](#nodriver.cdp.css.SourceRange)]* *= None*

The associated rule (@media or @import) header range in the enclosing stylesheet (if
available).

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

Identifier of the stylesheet containing this object (if exists).

#### media_list*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`MediaQuery`](#nodriver.cdp.css.MediaQuery)]]* *= None*

Array of media queries.

### *class* MediaQuery(expressions, active)

Media query descriptor.

#### expressions*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`MediaQueryExpression`](#nodriver.cdp.css.MediaQueryExpression)]*

Array of media query expressions.

#### active*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether the media query condition is satisfied.

### *class* MediaQueryExpression(value, unit, feature, value_range=None, computed_length=None)

Media query expression descriptor.

#### value*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Media query expression value.

#### unit*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Media query expression units.

#### feature*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Media query expression feature.

#### value_range*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceRange`](#nodriver.cdp.css.SourceRange)]* *= None*

The associated range of the value text in the enclosing stylesheet (if available).

#### computed_length*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`float`](https://docs.python.org/3/library/functions.html#float)]* *= None*

Computed length of media query expression (if applicable).

### *class* CSSContainerQuery(text, range_=None, style_sheet_id=None, name=None, physical_axes=None, logical_axes=None, queries_scroll_state=None)

CSS container query rule descriptor.

#### text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Container query text.

#### range_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceRange`](#nodriver.cdp.css.SourceRange)]* *= None*

The associated rule header range in the enclosing stylesheet (if
available).

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

Identifier of the stylesheet containing this object (if exists).

#### name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

Optional name for the container.

#### physical_axes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`PhysicalAxes`](dom.md#nodriver.cdp.dom.PhysicalAxes)]* *= None*

Optional physical axes queried for the container.

#### logical_axes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`LogicalAxes`](dom.md#nodriver.cdp.dom.LogicalAxes)]* *= None*

Optional logical axes queried for the container.

#### queries_scroll_state*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

true if the query contains scroll-state() queries.

### *class* CSSSupports(text, active, range_=None, style_sheet_id=None)

CSS Supports at-rule descriptor.

#### text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Supports rule text.

#### active*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Whether the supports condition is satisfied.

#### range_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceRange`](#nodriver.cdp.css.SourceRange)]* *= None*

The associated rule header range in the enclosing stylesheet (if
available).

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

Identifier of the stylesheet containing this object (if exists).

### *class* CSSScope(text, range_=None, style_sheet_id=None)

CSS Scope at-rule descriptor.

#### text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Scope rule text.

#### range_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceRange`](#nodriver.cdp.css.SourceRange)]* *= None*

The associated rule header range in the enclosing stylesheet (if
available).

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

Identifier of the stylesheet containing this object (if exists).

### *class* CSSLayer(text, range_=None, style_sheet_id=None)

CSS Layer at-rule descriptor.

#### text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Layer name.

#### range_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceRange`](#nodriver.cdp.css.SourceRange)]* *= None*

The associated rule header range in the enclosing stylesheet (if
available).

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

Identifier of the stylesheet containing this object (if exists).

### *class* CSSStartingStyle(range_=None, style_sheet_id=None)

CSS Starting Style at-rule descriptor.

#### range_*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SourceRange`](#nodriver.cdp.css.SourceRange)]* *= None*

The associated rule header range in the enclosing stylesheet (if
available).

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

Identifier of the stylesheet containing this object (if exists).

### *class* CSSLayerData(name, order, sub_layers=None)

CSS Layer data.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Layer name.

#### order*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Layer order. The order determines the order of the layer in the cascade order.
A higher number has higher priority in the cascade order.

#### sub_layers*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSLayerData`](#nodriver.cdp.css.CSSLayerData)]]* *= None*

Direct sub-layers

### *class* PlatformFontUsage(family_name, post_script_name, is_custom_font, glyph_count)

Information about amount of glyphs that were rendered with given font.

#### family_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Font’s family name reported by platform.

#### post_script_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Font’s PostScript name reported by platform.

#### is_custom_font*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

Indicates if the font was downloaded or resolved locally.

#### glyph_count*: [`float`](https://docs.python.org/3/library/functions.html#float)*

Amount of glyphs that were rendered with this font.

### *class* FontVariationAxis(tag, name, min_value, max_value, default_value)

Information about font variation axes for variable fonts

#### tag*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The font-variation-setting tag (a.k.a. “axis tag”).

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

Human-readable variation name in the default language (normally, “en”).

#### min_value*: [`float`](https://docs.python.org/3/library/functions.html#float)*

The minimum value (inclusive) the font supports for this tag.

#### max_value*: [`float`](https://docs.python.org/3/library/functions.html#float)*

The maximum value (inclusive) the font supports for this tag.

#### default_value*: [`float`](https://docs.python.org/3/library/functions.html#float)*

The default value.

### *class* FontFace(font_family, font_style, font_variant, font_weight, font_stretch, font_display, unicode_range, src, platform_font_family, font_variation_axes=None)

Properties of a web font: [https://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-descriptions](https://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-descriptions)
and additional information such as platformFontFamily and fontVariationAxes.

#### font_family*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The font-family.

#### font_style*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The font-style.

#### font_variant*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The font-variant.

#### font_weight*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The font-weight.

#### font_stretch*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The font-stretch.

#### font_display*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The font-display.

#### unicode_range*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The unicode-range.

#### src*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The src.

#### platform_font_family*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The resolved platform font family

#### font_variation_axes*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`FontVariationAxis`](#nodriver.cdp.css.FontVariationAxis)]]* *= None*

Available variation settings (a.k.a. “axes”).

### *class* CSSTryRule(origin, style, style_sheet_id=None)

CSS try rule representation.

#### origin*: [`StyleSheetOrigin`](#nodriver.cdp.css.StyleSheetOrigin)*

Parent stylesheet’s origin.

#### style*: [`CSSStyle`](#nodriver.cdp.css.CSSStyle)*

Associated style declaration.

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

The css style sheet identifier (absent for user agent stylesheet and user-specified
stylesheet rules) this rule came from.

### *class* CSSPositionTryRule(name, origin, style, active, style_sheet_id=None)

CSS @position-try rule representation.

#### name*: [`Value`](#nodriver.cdp.css.Value)*

The prelude dashed-ident name

#### origin*: [`StyleSheetOrigin`](#nodriver.cdp.css.StyleSheetOrigin)*

Parent stylesheet’s origin.

#### style*: [`CSSStyle`](#nodriver.cdp.css.CSSStyle)*

Associated style declaration.

#### active*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

The css style sheet identifier (absent for user agent stylesheet and user-specified
stylesheet rules) this rule came from.

### *class* CSSKeyframesRule(animation_name, keyframes)

CSS keyframes rule representation.

#### animation_name*: [`Value`](#nodriver.cdp.css.Value)*

Animation name.

#### keyframes*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSKeyframeRule`](#nodriver.cdp.css.CSSKeyframeRule)]*

List of keyframes.

### *class* CSSPropertyRegistration(property_name, inherits, syntax, initial_value=None)

Representation of a custom property registration through CSS.registerProperty

#### property_name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### inherits*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### syntax*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### initial_value*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Value`](#nodriver.cdp.css.Value)]* *= None*

### *class* CSSFontPaletteValuesRule(origin, font_palette_name, style, style_sheet_id=None)

CSS font-palette-values rule representation.

#### origin*: [`StyleSheetOrigin`](#nodriver.cdp.css.StyleSheetOrigin)*

Parent stylesheet’s origin.

#### font_palette_name*: [`Value`](#nodriver.cdp.css.Value)*

Associated font palette name.

#### style*: [`CSSStyle`](#nodriver.cdp.css.CSSStyle)*

Associated style declaration.

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

The css style sheet identifier (absent for user agent stylesheet and user-specified
stylesheet rules) this rule came from.

### *class* CSSPropertyRule(origin, property_name, style, style_sheet_id=None)

CSS property at-rule representation.

#### origin*: [`StyleSheetOrigin`](#nodriver.cdp.css.StyleSheetOrigin)*

Parent stylesheet’s origin.

#### property_name*: [`Value`](#nodriver.cdp.css.Value)*

Associated property name.

#### style*: [`CSSStyle`](#nodriver.cdp.css.CSSStyle)*

Associated style declaration.

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

The css style sheet identifier (absent for user agent stylesheet and user-specified
stylesheet rules) this rule came from.

### *class* CSSFunctionParameter(name, type_)

CSS function argument representation.

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The parameter name.

#### type_*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The parameter type.

### *class* CSSFunctionConditionNode(children, condition_text, media=None, container_queries=None, supports=None)

CSS function conditional block representation.

#### children*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSFunctionNode`](#nodriver.cdp.css.CSSFunctionNode)]*

Block body.

#### condition_text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The condition text.

#### media*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSMedia`](#nodriver.cdp.css.CSSMedia)]* *= None*

Media query for this conditional block. Only one type of condition should be set.

#### container_queries*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSContainerQuery`](#nodriver.cdp.css.CSSContainerQuery)]* *= None*

Container query for this conditional block. Only one type of condition should be set.

#### supports*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSSupports`](#nodriver.cdp.css.CSSSupports)]* *= None*

@supports CSS at-rule condition. Only one type of condition should be set.

### *class* CSSFunctionNode(condition=None, style=None)

Section of the body of a CSS function rule.

#### condition*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSFunctionConditionNode`](#nodriver.cdp.css.CSSFunctionConditionNode)]* *= None*

A conditional block. If set, style should not be set.

#### style*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSStyle`](#nodriver.cdp.css.CSSStyle)]* *= None*

Values set by this node. If set, condition should not be set.

### *class* CSSFunctionRule(name, origin, parameters, children, style_sheet_id=None)

CSS function at-rule representation.

#### name*: [`Value`](#nodriver.cdp.css.Value)*

Name of the function.

#### origin*: [`StyleSheetOrigin`](#nodriver.cdp.css.StyleSheetOrigin)*

Parent stylesheet’s origin.

#### parameters*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSFunctionParameter`](#nodriver.cdp.css.CSSFunctionParameter)]*

List of parameters.

#### children*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSFunctionNode`](#nodriver.cdp.css.CSSFunctionNode)]*

Function body.

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

The css style sheet identifier (absent for user agent stylesheet and user-specified
stylesheet rules) this rule came from.

### *class* CSSKeyframeRule(origin, key_text, style, style_sheet_id=None)

CSS keyframe rule representation.

#### origin*: [`StyleSheetOrigin`](#nodriver.cdp.css.StyleSheetOrigin)*

Parent stylesheet’s origin.

#### key_text*: [`Value`](#nodriver.cdp.css.Value)*

Associated key text.

#### style*: [`CSSStyle`](#nodriver.cdp.css.CSSStyle)*

Associated style declaration.

#### style_sheet_id*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]* *= None*

The css style sheet identifier (absent for user agent stylesheet and user-specified
stylesheet rules) this rule came from.

### *class* StyleDeclarationEdit(style_sheet_id, range_, text)

A descriptor of operation to mutate style declaration text.

#### style_sheet_id*: [`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)*

The css style sheet identifier.

#### range_*: [`SourceRange`](#nodriver.cdp.css.SourceRange)*

The range of the style text in the enclosing stylesheet.

#### text*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

New style text.

## Commands

Each command is a generator function. The return
type `Generator[x, y, z]` indicates that the generator
*yields* arguments of type `x`, it must be resumed with
an argument of type `y`, and it returns type `z`. In
this library, types `x` and `y` are the same for all
commands, and `z` is the return type you should pay attention
to. For more information, see
[Getting Started: Commands](../../readme.md#getting-started-commands).

### add_rule(style_sheet_id, rule_text, location, node_for_property_syntax_validation=None)

Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the
position specified by `location`.

* **Parameters:**
  * **style_sheet_id** ([`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)) – The css style sheet identifier where a new rule should be inserted.
  * **rule_text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – The text of a new rule.
  * **location** ([`SourceRange`](#nodriver.cdp.css.SourceRange)) – Text position of a new rule in the target style sheet.
  * **node_for_property_syntax_validation** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](dom.md#nodriver.cdp.dom.NodeId)]) – **(EXPERIMENTAL)** *(Optional)* NodeId for the DOM node in whose context custom property declarations for registered properties should be validated. If omitted, declarations in the new rule text can only be validated statically, which may produce incorrect results if the declaration contains a var() for example.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`CSSRule`](#nodriver.cdp.css.CSSRule)]
* **Returns:**
  The newly created rule.

### collect_class_names(style_sheet_id)

Returns all class names from specified stylesheet.

* **Parameters:**
  **style_sheet_id** ([`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**
  Class name list.

### create_style_sheet(frame_id, force=None)

Creates a new special “via-inspector” stylesheet in the frame with given `frameId`.

* **Parameters:**
  * **frame_id** ([`FrameId`](page.md#nodriver.cdp.page.FrameId)) – Identifier of the frame where “via-inspector” stylesheet should be created.
  * **force** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]) – *(Optional)* If true, creates a new stylesheet for every call. If false, returns a stylesheet previously created by a call with force=false for the frame’s document if it exists or creates a new stylesheet (default: false).
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)]
* **Returns:**
  Identifier of the created “via-inspector” stylesheet.

### disable()

Disables the CSS agent for the given page.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### enable()

Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been
enabled until the result of this command is received.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### force_pseudo_state(node_id, forced_pseudo_classes)

Ensures that the given node will have specified pseudo-classes whenever its style is computed by
the browser.

* **Parameters:**
  * **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – The element id for which to force the pseudo state.
  * **forced_pseudo_classes** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – Element pseudo classes to force when computing the element’s style.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### force_starting_style(node_id, forced)

Ensures that the given node is in its starting-style state.

* **Parameters:**
  * **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – The element id for which to force the starting-style state.
  * **forced** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Boolean indicating if this is on or off.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### get_animated_styles_for_node(node_id)

Returns the styles coming from animations & transitions
including the animation & transition styles coming from inheritance chain.

**EXPERIMENTAL**

* **Parameters:**
  **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSAnimationStyle`](#nodriver.cdp.css.CSSAnimationStyle)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSStyle`](#nodriver.cdp.css.CSSStyle)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`InheritedAnimatedStyleEntry`](#nodriver.cdp.css.InheritedAnimatedStyleEntry)]]]]
* **Returns:**
  A tuple with the following items:
  1. **animationStyles** - *(Optional)* Styles coming from animations.
  2. **transitionsStyle** - *(Optional)* Style coming from transitions.
  3. **inherited** - *(Optional)* Inherited style entries for animationsStyle and transitionsStyle from the inheritance chain of the element.

### get_background_colors(node_id)

* **Parameters:**
  **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – Id of the node to get background colors for.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]]
* **Returns:**
  A tuple with the following items:
  1. **backgroundColors** - *(Optional)* The range of background colors behind this element, if it contains any visible text. If no visible text is present, this will be undefined. In the case of a flat background color, this will consist of simply that color. In the case of a gradient, this will consist of each of the color stops. For anything more complicated, this will be an empty array. Images will be ignored (as if the image had failed to load).
  2. **computedFontSize** - *(Optional)* The computed font size for this node, as a CSS computed value string (e.g. ‘12px’).
  3. **computedFontWeight** - *(Optional)* The computed font weight for this node, as a CSS computed value string (e.g. ‘normal’ or ‘100’).

### get_computed_style_for_node(node_id)

Returns the computed style for a DOM node identified by `nodeId`.

* **Parameters:**
  **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSComputedStyleProperty`](#nodriver.cdp.css.CSSComputedStyleProperty)]]
* **Returns:**
  Computed style for the specified DOM node.

### get_inline_styles_for_node(node_id)

Returns the styles defined inline (explicitly in the “style” attribute and implicitly, using DOM
attributes) for a DOM node identified by `nodeId`.

* **Parameters:**
  **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSStyle`](#nodriver.cdp.css.CSSStyle)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSStyle`](#nodriver.cdp.css.CSSStyle)]]]
* **Returns:**
  A tuple with the following items:
  1. **inlineStyle** - *(Optional)* Inline style for the specified DOM node.
  2. **attributesStyle** - *(Optional)* Attribute-defined element style (e.g. resulting from “width=20 height=100%”).

### get_layers_for_node(node_id)

Returns all layers parsed by the rendering engine for the tree scope of a node.
Given a DOM element identified by nodeId, getLayersForNode returns the root
layer for the nearest ancestor document or shadow root. The layer root contains
the full layer tree for the tree scope and their ordering.

**EXPERIMENTAL**

* **Parameters:**
  **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`CSSLayerData`](#nodriver.cdp.css.CSSLayerData)]
* **Returns:**

### get_location_for_selector(style_sheet_id, selector_text)

Given a CSS selector text and a style sheet ID, getLocationForSelector
returns an array of locations of the CSS selector in the style sheet.

**EXPERIMENTAL**

* **Parameters:**
  * **style_sheet_id** ([`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)) – 
  * **selector_text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`SourceRange`](#nodriver.cdp.css.SourceRange)]]
* **Returns:**

### get_longhand_properties(shorthand_name, value)

**EXPERIMENTAL**

* **Parameters:**
  * **shorthand_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **value** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSProperty`](#nodriver.cdp.css.CSSProperty)]]
* **Returns:**

### get_matched_styles_for_node(node_id)

Returns requested styles for a DOM node identified by `nodeId`.

* **Parameters:**
  **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSStyle`](#nodriver.cdp.css.CSSStyle)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSStyle`](#nodriver.cdp.css.CSSStyle)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`RuleMatch`](#nodriver.cdp.css.RuleMatch)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PseudoElementMatches`](#nodriver.cdp.css.PseudoElementMatches)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`InheritedStyleEntry`](#nodriver.cdp.css.InheritedStyleEntry)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`InheritedPseudoElementMatches`](#nodriver.cdp.css.InheritedPseudoElementMatches)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSKeyframesRule`](#nodriver.cdp.css.CSSKeyframesRule)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSPositionTryRule`](#nodriver.cdp.css.CSSPositionTryRule)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSPropertyRule`](#nodriver.cdp.css.CSSPropertyRule)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSPropertyRegistration`](#nodriver.cdp.css.CSSPropertyRegistration)]], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`CSSFontPaletteValuesRule`](#nodriver.cdp.css.CSSFontPaletteValuesRule)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](dom.md#nodriver.cdp.dom.NodeId)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSFunctionRule`](#nodriver.cdp.css.CSSFunctionRule)]]]]
* **Returns:**
  A tuple with the following items:
  1. **inlineStyle** - *(Optional)* Inline style for the specified DOM node.
  2. **attributesStyle** - *(Optional)* Attribute-defined element style (e.g. resulting from “width=20 height=100%”).
  3. **matchedCSSRules** - *(Optional)* CSS rules matching this node, from all applicable stylesheets.
  4. **pseudoElements** - *(Optional)* Pseudo style matches for this node.
  5. **inherited** - *(Optional)* A chain of inherited styles (from the immediate node parent up to the DOM tree root).
  6. **inheritedPseudoElements** - *(Optional)* A chain of inherited pseudo element styles (from the immediate node parent up to the DOM tree root).
  7. **cssKeyframesRules** - *(Optional)* A list of CSS keyframed animations matching this node.
  8. **cssPositionTryRules** - *(Optional)* A list of CSS @position-try rules matching this node, based on the position-try-fallbacks property.
  9. **activePositionFallbackIndex** - *(Optional)* Index of the active fallback in the applied position-try-fallback property, will not be set if there is no active position-try fallback.
  10. **cssPropertyRules** - *(Optional)* A list of CSS at-property rules matching this node.
  11. **cssPropertyRegistrations** - *(Optional)* A list of CSS property registrations matching this node.
  12. **cssFontPaletteValuesRule** - *(Optional)* A font-palette-values rule matching this node.
  13. **parentLayoutNodeId** - *(Optional)* Id of the first parent element that does not have display: contents.
  14. **cssFunctionRules** - *(Optional)* A list of CSS at-function rules referenced by styles of this node.

### get_media_queries()

Returns all media queries parsed by the rendering engine.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSMedia`](#nodriver.cdp.css.CSSMedia)]]
* **Returns:**

### get_platform_fonts_for_node(node_id)

Requests information about platform fonts which we used to render child TextNodes in the given
node.

* **Parameters:**
  **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`PlatformFontUsage`](#nodriver.cdp.css.PlatformFontUsage)]]
* **Returns:**
  Usage statistics for every employed platform font.

### get_style_sheet_text(style_sheet_id)

Returns the current textual content for a stylesheet.

* **Parameters:**
  **style_sheet_id** ([`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)]
* **Returns:**
  The stylesheet text.

### resolve_values(values, node_id, property_name=None, pseudo_type=None, pseudo_identifier=None)

Resolve the specified values in the context of the provided element.
For example, a value of ‘1em’ is evaluated according to the computed
‘font-size’ of the element and a value ‘calc(1px + 2px)’ will be
resolved to ‘3px’.

* **Parameters:**
  * **values** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – Substitution functions (var()/env()/attr()) and cascade-dependent keywords (revert/revert-layer) do not work.
  * **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – Id of the node in whose context the expression is evaluated
  * **property_name** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – *(Optional)* Only longhands and custom property names are accepted.
  * **pseudo_type** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`PseudoType`](dom.md#nodriver.cdp.dom.PseudoType)]) – **(EXPERIMENTAL)** *(Optional)* Pseudo element type, only works for pseudo elements that generate elements in the tree, such as ::before and ::after.
  * **pseudo_identifier** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – **(EXPERIMENTAL)** *(Optional)* Pseudo element custom ident.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**

### set_container_query_text(style_sheet_id, range_, text)

Modifies the expression of a container query.

**EXPERIMENTAL**

* **Parameters:**
  * **style_sheet_id** ([`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)) – 
  * **range** – 
  * **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`CSSContainerQuery`](#nodriver.cdp.css.CSSContainerQuery)]
* **Returns:**
  The resulting CSS container query rule after modification.

### set_effective_property_value_for_node(node_id, property_name, value)

Find a rule with the given active property for the given node and set the new value for this
property

* **Parameters:**
  * **node_id** ([`NodeId`](dom.md#nodriver.cdp.dom.NodeId)) – The element id for which to set property.
  * **property_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **value** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_keyframe_key(style_sheet_id, range_, key_text)

Modifies the keyframe rule key text.

* **Parameters:**
  * **style_sheet_id** ([`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)) – 
  * **range** – 
  * **key_text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Value`](#nodriver.cdp.css.Value)]
* **Returns:**
  The resulting key text after modification.

### set_local_fonts_enabled(enabled)

Enables/disables rendering of local CSS fonts (enabled by default).

**EXPERIMENTAL**

* **Parameters:**
  **enabled** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – Whether rendering of local fonts is enabled.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### set_media_text(style_sheet_id, range_, text)

Modifies the rule selector.

* **Parameters:**
  * **style_sheet_id** ([`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)) – 
  * **range** – 
  * **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`CSSMedia`](#nodriver.cdp.css.CSSMedia)]
* **Returns:**
  The resulting CSS media rule after modification.

### set_property_rule_property_name(style_sheet_id, range_, property_name)

Modifies the property rule property name.

* **Parameters:**
  * **style_sheet_id** ([`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)) – 
  * **range** – 
  * **property_name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Value`](#nodriver.cdp.css.Value)]
* **Returns:**
  The resulting key text after modification.

### set_rule_selector(style_sheet_id, range_, selector)

Modifies the rule selector.

* **Parameters:**
  * **style_sheet_id** ([`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)) – 
  * **range** – 
  * **selector** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`SelectorList`](#nodriver.cdp.css.SelectorList)]
* **Returns:**
  The resulting selector list after modification.

### set_scope_text(style_sheet_id, range_, text)

Modifies the expression of a scope at-rule.

**EXPERIMENTAL**

* **Parameters:**
  * **style_sheet_id** ([`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)) – 
  * **range** – 
  * **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`CSSScope`](#nodriver.cdp.css.CSSScope)]
* **Returns:**
  The resulting CSS Scope rule after modification.

### set_style_sheet_text(style_sheet_id, text)

Sets the new stylesheet text.

* **Parameters:**
  * **style_sheet_id** ([`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)) – 
  * **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]]
* **Returns:**
  *(Optional)* URL of source map associated with script (if any).

### set_style_texts(edits, node_for_property_syntax_validation=None)

Applies specified style edits one after another in the given order.

* **Parameters:**
  * **edits** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`StyleDeclarationEdit`](#nodriver.cdp.css.StyleDeclarationEdit)]) – 
  * **node_for_property_syntax_validation** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](dom.md#nodriver.cdp.dom.NodeId)]) – **(EXPERIMENTAL)** *(Optional)* NodeId for the DOM node in whose context custom property declarations for registered properties should be validated. If omitted, declarations in the new rule text can only be validated statically, which may produce incorrect results if the declaration contains a var() for example.
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSStyle`](#nodriver.cdp.css.CSSStyle)]]
* **Returns:**
  The resulting styles after modification.

### set_supports_text(style_sheet_id, range_, text)

Modifies the expression of a supports at-rule.

**EXPERIMENTAL**

* **Parameters:**
  * **style_sheet_id** ([`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)) – 
  * **range** – 
  * **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`CSSSupports`](#nodriver.cdp.css.CSSSupports)]
* **Returns:**
  The resulting CSS Supports rule after modification.

### start_rule_usage_tracking()

Enables the selector recording.

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### stop_rule_usage_tracking()

Stop tracking rule usage and return the list of rules that were used since last call to
`takeCoverageDelta` (or since start of coverage instrumentation).

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`RuleUsage`](#nodriver.cdp.css.RuleUsage)]]
* **Returns:**

### take_computed_style_updates()

Polls the next batch of computed style updates.

**EXPERIMENTAL**

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`NodeId`](dom.md#nodriver.cdp.dom.NodeId)]]
* **Returns:**
  The list of node Ids that have their tracked computed styles updated.

### take_coverage_delta()

Obtain list of rules that became used since last call to this method (or since start of coverage
instrumentation).

* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`RuleUsage`](#nodriver.cdp.css.RuleUsage)], [`float`](https://docs.python.org/3/library/functions.html#float)]]
* **Returns:**
  A tuple with the following items:
  1. **coverage** -
  2. **timestamp** - Monotonically increasing time, in seconds.

### track_computed_style_updates(properties_to_track)

Starts tracking the given computed styles for updates. The specified array of properties
replaces the one previously specified. Pass empty array to disable tracking.
Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified.
The changes to computed style properties are only tracked for nodes pushed to the front-end
by the DOM agent. If no changes to the tracked properties occur after the node has been pushed
to the front-end, no updates will be issued for the node.

**EXPERIMENTAL**

* **Parameters:**
  **properties_to_track** ([`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`CSSComputedStyleProperty`](#nodriver.cdp.css.CSSComputedStyleProperty)]) – 
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

### track_computed_style_updates_for_node(node_id=None)

Starts tracking the given node for the computed style updates
and whenever the computed style is updated for node, it queues
a `computedStyleUpdated` event with throttling.
There can only be 1 node tracked for computed style updates
so passing a new node id removes tracking from the previous node.
Pass `undefined` to disable tracking.

**EXPERIMENTAL**

* **Parameters:**
  **node_id** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`NodeId`](dom.md#nodriver.cdp.dom.NodeId)]) – *(Optional)*
* **Return type:**
  [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)[[`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/library/constants.html#None)]

## Events

Generally, you do not need to instantiate CDP events
yourself. Instead, the API creates events for you and then
you use the event’s attributes.

### *class* FontsUpdated(font)

Fires whenever a web font is updated.  A non-empty font parameter indicates a successfully loaded
web font.

#### font*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`FontFace`](#nodriver.cdp.css.FontFace)]*

The web font that has loaded.

### *class* MediaQueryResultChanged

Fires whenever a MediaQuery result changes (for example, after a browser window has been
resized.) The current implementation considers only viewport-dependent media features.

### *class* StyleSheetAdded(header)

Fired whenever an active document stylesheet is added.

#### header*: [`CSSStyleSheetHeader`](#nodriver.cdp.css.CSSStyleSheetHeader)*

Added stylesheet metainfo.

### *class* StyleSheetChanged(style_sheet_id)

Fired whenever a stylesheet is changed as a result of the client operation.

#### style_sheet_id*: [`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)*

### *class* StyleSheetRemoved(style_sheet_id)

Fired whenever an active document stylesheet is removed.

#### style_sheet_id*: [`StyleSheetId`](#nodriver.cdp.css.StyleSheetId)*

Identifier of the removed stylesheet.

### *class* ComputedStyleUpdated(node_id)

**EXPERIMENTAL**

#### node_id*: [`NodeId`](dom.md#nodriver.cdp.dom.NodeId)*

The node id that has updated computed styles.
