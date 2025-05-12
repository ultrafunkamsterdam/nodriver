<a id="element"></a>

# Element class

Some words about the Element class

### *class* Element(node, tab, tree=None)

#### *property* tag

#### *property* tag_name

#### *property* node_id

#### *property* backend_node_id

#### *property* node_type

#### *property* node_name

#### *property* local_name

#### *property* node_value

#### *property* parent_id

#### *property* child_node_count

#### *property* attributes

#### *property* document_url

#### *property* base_url

#### *property* public_id

#### *property* system_id

#### *property* internal_subset

#### *property* xml_version

#### *property* value

#### *property* pseudo_type

#### *property* pseudo_identifier

#### *property* shadow_root_type

#### *property* frame_id

#### *property* content_document

#### *property* shadow_roots

#### *property* template_content

#### *property* pseudo_elements

#### *property* imported_document

#### *property* distributed_nodes

#### *property* is_svg

#### *property* compatibility_mode

#### *property* assigned_slot

#### *property* tab

#### *property* shadow_children

#### *async* save_to_dom()

saves element to dom
:return:
:rtype:

#### *async* remove_from_dom()

removes the element from dom

#### *async* update(\_node=None)

updates element to retrieve more properties. for example this enables
[`children`](#nodriver.Element.children) and [`parent`](#nodriver.Element.parent) attributes.

also resolves js opbject which is stored object in [`remote_object`](#nodriver.Element.remote_object)

usually you will get element nodes by the usage of

[`Tab.query_selector_all()`](tab.md#nodriver.Tab.query_selector_all)

[`Tab.find_elements_by_text()`](tab.md#nodriver.Tab.find_elements_by_text)

those elements are already updated and you can browse through children directly.

The reason for a seperate call instead of doing it at initialization,
is because when you are retrieving 100+ elements this becomes quite expensive.

therefore, it is not advised to call this method on a bunch of blocks (100+) at the same time.

* **Returns:**
* **Return type:**

#### *property* node

#### *property* tree*: [Node](../cdp/dom.md#nodriver.cdp.dom.Node)*

#### *property* attrs

attributes are stored here, however, you can set them directly on the element object as well.
:return:
:rtype:

#### *property* parent*: [Element](#nodriver.Element) | [None](https://docs.python.org/3/library/constants.html#None)*

get the parent element (node) of current element(node)
:return:
:rtype:

#### *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List)[[Element](#nodriver.Element)] | [str](https://docs.python.org/3/library/stdtypes.html#str)*

returns the elements’ children. those children also have a children property
so you can browse through the entire tree as well.
:return:
:rtype:

#### *property* remote_object*: [RemoteObject](../cdp/runtime.md#nodriver.cdp.runtime.RemoteObject)*

#### *property* object_id*: [RemoteObjectId](../cdp/runtime.md#nodriver.cdp.runtime.RemoteObjectId)*

#### *async* click()

Click the element.

* **Returns:**
* **Return type:**

#### *async* get_js_attributes()

#### *async* apply(js_function, return_by_value=True)

apply javascript to this element. the given js_function string should accept the js element as parameter,
and can be a arrow function, or function declaration.
eg:

> - ‘(elem) => { elem.value = “blabla”; consolelog(elem); alert(JSON.stringify(elem); } ‘
> - ‘elem => elem.play()’
> - function myFunction(elem) { alert(elem) }
* **Parameters:**
  * **js_function** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the js function definition which received this element.
  * **return_by_value** – 
* **Returns:**
* **Return type:**

#### *async* get_position(abs=False)

* **Return type:**
  `Position`

#### *async* mouse_click(button='left', buttons=1, modifiers=0, \_until_event=None)

native click (on element) . note: this likely does not work atm, use click() instead

* **Parameters:**
  * **button** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – str (default = “left”)
  * **buttons** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – which button (default 1 = left)
  * **modifiers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Bit field representing pressed modifier keys.
    Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
  * **\_until_event** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`type`](https://docs.python.org/3/library/functions.html#type)]) – internal. event to wait for before returning
* **Returns:**

#### *async* click_mouse(button='left', buttons=1, modifiers=0, \_until_event=None)

native click (on element) . note: this likely does not work atm, use click() instead

* **Parameters:**
  * **button** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – str (default = “left”)
  * **buttons** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – which button (default 1 = left)
  * **modifiers** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]) – *(Optional)* Bit field representing pressed modifier keys.
    Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
  * **\_until_event** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`type`](https://docs.python.org/3/library/functions.html#type)]) – internal. event to wait for before returning
* **Returns:**

#### *async* mouse_move()

moves mouse (not click), to element position. when an element has an
hover/mouseover effect, this would trigger it

#### *async* mouse_drag(destination, relative=False, steps=1)

drag an element to another element or target coordinates. dragging of elements should be supported  by the site of course

* **Parameters:**
  * **destination** ([*Element*](#nodriver.Element) *or* *coordinate as x**,**y tuple*) – another element where to drag to, or a tuple (x,y) of ints representing coordinate
  * **relative** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) – when True, treats coordinate as relative. for example (-100, 200) will move left 100px and down 200px
  * **steps** ([*int*](https://docs.python.org/3/library/functions.html#int)) – move in <steps> points, this could make it look more “natural” (default 1),
    but also a lot slower.
    for very smooth action use 50-100
* **Returns:**
* **Return type:**

#### *async* scroll_into_view()

scrolls element into view

#### *async* clear_input(\_until_event=None)

clears an input field

#### *async* send_keys(text)

send text to an input field, or any other html element.

hint, if you ever get stuck where using py:meth:~click
does not work, sending the keystroke n or rn or a spacebar work wonders!

* **Parameters:**
  **text** ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) – text to send
* **Returns:**
  None

#### *async* send_file(\*file_paths)

some form input require a file (upload), a full path needs to be provided.
this method sends 1 or more file(s) to the input field.

needles to say, but make sure the field accepts multiple files if you want to send more files.
otherwise the browser might crash.

example :
await fileinputElement.send_file(‘c:/temp/image.png’, ‘c:/users/myuser/lol.gif’)

#### *async* focus()

focus the current element. often useful in form (select) fields

#### *async* select_option()

for form (select) fields. when you have queried the options you can call this method on the option object.
02/08/2024: fixed the problem where events are not fired when programattically selecting an option.

calling `option.select_option()` will use that option as selected value.
does not work in all cases.

#### *async* set_value(value)

#### *async* set_text(value)

#### *async* get_html()

#### *property* text*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

gets the text contents of this element
note: this includes text in the form of script content, as those are also just ‘text nodes’

* **Returns:**
* **Return type:**

#### *property* text_all

gets the text contents of this element, and it’s children in a concatenated string
note: this includes text in the form of script content, as those are also just ‘text nodes’
:return:
:rtype:

#### *async* query_selector_all(selector)

like js querySelectorAll()

#### *async* query_selector(selector)

like js querySelector()

#### *async* save_screenshot(filename='auto', format='jpeg', scale=1)

Saves a screenshot of this element (only)
This is not the same as [`Tab.save_screenshot`](tab.md#nodriver.Tab.save_screenshot), which saves a “regular” screenshot

When the element is hidden, or has no size, or is otherwise not capturable, a RuntimeError is raised

* **Parameters:**
  * **filename** (*PathLike*) – uses this as the save path
  * **format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – jpeg or png (defaults to jpeg)
  * **scale** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`int`](https://docs.python.org/3/library/functions.html#int), [`float`](https://docs.python.org/3/library/functions.html#float), [`None`](https://docs.python.org/3/library/constants.html#None)]) – the scale of the screenshot, eg: 1 = size as is, 2 = double, 0.5 is half
* **Returns:**
  the path/filename of saved screenshot
* **Return type:**
  [str](https://docs.python.org/3/library/stdtypes.html#str)

#### *async* flash(duration=0.5)

displays for a short time a red dot on the element (only if the element itself is visible)

* **Parameters:**
  * **coords** (*x**,**y*) – x,y
  * **duration** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`float`](https://docs.python.org/3/library/functions.html#float), [`int`](https://docs.python.org/3/library/functions.html#int)]) – seconds (default 0.5)
* **Returns:**
* **Return type:**

#### *async* highlight_overlay()

highlights the element devtools-style. To remove the highlight,
call the method again.
:return:
:rtype:

#### *async* record_video(filename=None, folder=None, duration=None)

experimental option.

* **Parameters:**
  * **filename** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – the desired filename
  * **folder** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]) – the download folder path
  * **duration** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`int`](https://docs.python.org/3/library/functions.html#int), [`float`](https://docs.python.org/3/library/functions.html#float), [`None`](https://docs.python.org/3/library/constants.html#None)]) – record for this many seconds and then download

on html5 video nodes, you can call this method to start recording of the video.

when any of the follow happens:

- video ends
- calling videoelement(‘pause’)
- video stops

the video recorded will be downloaded.

#### *async* is_recording()
