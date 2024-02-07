from __future__ import annotations

import asyncio
import json
import logging
import pathlib
import secrets
import typing

from . import util
from ._contradict import ContraDict
from .config import PathLike
from .. import cdp

logger = logging.getLogger(__name__)

if typing.TYPE_CHECKING:
    from .tab import Tab


class Registry(ContraDict):
    def __setitem__(self, key, value):
        print("registry setitem", key)
        super().__setitem__(key, value)

    def __getitem__(self, item):
        print("registry getitem", item)
        return super().__getitem__(item)


def create(node: cdp.dom.Node, tab: Tab, tree: typing.Optional[cdp.dom.Node] = None):
    """
    factory for Elements
    this is used with Tab.query_selector(_all), since we already have the tree,
    we don't need to fetch it for every single element.

    :param node: cdp dom node representation
    :type node: cdp.dom.Node
    :param tab: the target object to which this element belongs
    :type tab: Tab
    :param tree: [Optional] the full node tree to which <node> belongs, enhances performance.
                when not provided, you need to call `await elem.update()` before using .children / .parent
    :type tree:
    """

    elem = Element(node, tab, tree)

    return elem


class Element:
    def __init__(self, node: cdp.dom.Node, tab: Tab, tree: cdp.dom.Node = None):
        """
        Represents an (HTML) DOM Element

        :param node: cdp dom node representation
        :type node: cdp.dom.Node
        :param tab: the target object to which this element belongs
        :type tab: Tab
        """
        if not node:
            raise Exception("node cannot be None")
        self._tab = tab
        # if node.node_name == 'IFRAME':
        #     self._node = node.content_document
        # else:
        self._node = node
        self._tree = tree
        self._parent = None
        self._remote_object = None
        self._attrs = ContraDict(silent=True)
        self._make_attrs()

    @property
    def node_id(self):
        return self.node.node_id

    @property
    def backend_node_id(self):
        return self.node.backend_node_id

    @property
    def node_type(self):
        return self.node.node_type

    @property
    def node_name(self):
        return self.node.node_name

    @property
    def local_name(self):
        return self.node.local_name

    @property
    def node_value(self):
        return self.node.node_value

    @property
    def parent_id(self):
        return self.node.parent_id

    @property
    def child_node_count(self):
        return self.node.child_node_count

    @property
    def attributes(self):
        return self.node.attributes

    @property
    def document_url(self):
        return self.node.document_url

    @property
    def base_url(self):
        return self.node.base_url

    @property
    def public_id(self):
        return self.node.public_id

    @property
    def system_id(self):
        return self.node.system_id

    @property
    def internal_subset(self):
        return self.node.internal_subset

    @property
    def xml_version(self):
        return self.node.xml_version

    @property
    def value(self):
        return self.node.value

    @property
    def pseudo_type(self):
        return self.node.pseudo_type

    @property
    def pseudo_identifier(self):
        return self.node.pseudo_identifier

    @property
    def shadow_root_type(self):
        return self.node.shadow_root_type

    @property
    def frame_id(self):
        return self.node.frame_id

    @property
    def content_document(self):
        return self.node.content_document

    @property
    def shadow_roots(self):
        return self.node.shadow_roots

    @property
    def template_content(self):
        return self.node.template_content

    @property
    def pseudo_elements(self):
        return self.node.pseudo_elements

    @property
    def imported_document(self):
        return self.node.imported_document

    @property
    def distributed_nodes(self):
        return self.node.distributed_nodes

    @property
    def is_svg(self):
        return self.node.is_svg

    @property
    def compatibility_mode(self):
        return self.node.compatibility_mode

    @property
    def assigned_slot(self):
        return self.node.assigned_slot

    @property
    def tab(self):
        return self._tab

    def __getattr__(self, item):
        # returns None when attribute is not found
        # instead of raising AttributeError
        x = getattr(self.attrs, item, None)
        if x:
            return x
        x = getattr(self.node, item, None)

        return x

    def __setattr__(self, key, value):
        if key[0] != "_":
            if key[1:] not in vars(self).keys():
                self.attrs.__setattr__(key, value)
                return
        super().__setattr__(key, value)

    def __setitem__(self, key, value):
        if key[0] != "_":
            if key[1:] not in vars(self).keys():
                self.attrs[key] = value

    def __getitem__(self, item):
        return self.attrs.get(item, None)

    async def save_to_dom(self):
        self._remote_object = await self._tab.send(
            cdp.dom.resolve_node(backend_node_id=self.backend_node_id)
        )
        await self._tab.send(cdp.dom.set_outer_html(self.node_id, outer_html=str(self)))
        await self.update()

    async def remove_from_dom(self):
        if not self.tree:
            self._tree = await self._tab.send(cdp.dom.get_document(-1, True))
        self._tree = util.remove_from_tree(self.tree, self.node)

    async def update(self, _node=None):
        """
        updates element to retrieve more properties. for example this enables
        :py:obj:`~children` and :py:obj:`~parent` attributes.

        also resolves js opbject which is stored object in :py:obj:`~remote_object`

        usually you will get element nodes by the usage of

        :py:meth:`Tab.query_selector_all()`

        :py:meth:`Tab.find_elements_by_text()`

        those elements are already updated and you can browse through children directly.

        The reason for a seperate call instead of doing it at initialization,
        is because when you are retrieving 100+ elements this becomes quite expensive.

        therefore, it is not advised to call this method on a bunch of blocks (100+) at the same time.

        :return:
        :rtype:
        """
        if _node:
            self._node = _node
        # self._children.clear()
        self._parent = None
        doc = await self._tab.send(cdp.dom.get_document(-1, True))
        # if self.node_name != "IFRAME":
        updated_node = util.filter_recurse(
            doc, lambda n: n.backend_node_id == self._node.backend_node_id
        )
        self._node = updated_node
        self._tree = doc

        self._remote_object = await self._tab.send(
            cdp.dom.resolve_node(backend_node_id=self.backend_node_id)
        )
        self.attrs.clear()
        self._make_attrs()
        if self.node_name != "IFRAME":
            parent_node = util.filter_recurse(
                doc, lambda n: n.node_id == updated_node.parent_id
            )
            if not parent_node:
                # could happen if node is for example <html>
                return self
            self._parent = create(parent_node, tab=self._tab, tree=self._tree)
        return self

    @property
    def node(self):
        return self._node

    @property
    def tree(self) -> cdp.dom.Node:
        return self._tree
        # raise RuntimeError("you should first call  `await update()` on this object to populate it's tree")

    @tree.setter
    def tree(self, tree: cdp.dom.Node):
        self._tree = tree

    @property
    def parent(self) -> typing.Union[Element, None]:
        # if self._parent:
        #     return self._parent
        if not self.tree:
            raise RuntimeError("could not get parent since the element has no tree set")
        parent_node = util.filter_recurse(
            self.tree, lambda n: n.node_id == self.parent_id
        )
        if not parent_node:
            return None
        parent_element = create(parent_node, tab=self._tab, tree=self.tree)
        return parent_element
        # self._parent = parent_element
        # return self._parent

    @property
    def attrs(self):
        """
        attributes are stored here, however, you can set them directly on the element object as well.
        :return:
        :rtype:
        """
        return self._attrs

    @property
    def children(self) -> typing.Union[typing.List[Element], str]:
        """
        returns the elements' children. those children also have a children property
        so you can browse through the entire tree as well.
        :return:
        :rtype:
        """
        _children = []
        if self._node.node_name == "IFRAME":
            # iframes are not exact the same as other nodes
            # the children of iframes are found under
            # the .content_document property, which is of more
            # use than the node itself
            frame = self._node.content_document
            if not frame.child_node_count:
                return []
            for child in frame.children:
                child_elem = create(child, self._tab, frame)
                if child_elem:
                    _children.append(child_elem)
            # self._node = frame
            return _children
        elif not self.node.child_node_count:
            return []
        if self.node.children:
            for child in self.node.children:
                child_elem = create(child, self._tab, self.tree)
                if child_elem:
                    _children.append(child_elem)
        return _children

    @property
    def remote_object(self) -> cdp.runtime.RemoteObject:
        return self._remote_object

    @property
    def object_id(self) -> cdp.runtime.RemoteObjectId:
        try:
            return self.remote_object.object_id
        except AttributeError:
            pass

    async def click(self):
        """
        Click the element.

        :return:
        :rtype:
        """
        self._remote_object = await self._tab.send(
            cdp.dom.resolve_node(backend_node_id=self.backend_node_id)
        )
        arguments = [cdp.runtime.CallArgument(object_id=self._remote_object.object_id)]
        await self.flash(0.25)
        await self._tab.send(
            cdp.runtime.call_function_on(
                "(el) => el.click()",
                object_id=self._remote_object.object_id,
                arguments=arguments,
                await_promise=True,
                user_gesture=True,
                return_by_value=True,
            )
        )

    async def get_js_attributes(self):
        return ContraDict(
            json.loads(
                await self.apply(
                    """
            function (e) {
                let o = {}
                for(let k in e){
                    o[k] = e[k]
                }
                return JSON.stringify(o)
            }
            """
                )
            )
        )

    def __await__(self):
        return self.update().__await__()

    def __call__(self, js_method):
        """
        calling the element object will call a js method on the object
        eg, element.play() in case of a video element, it will call .play()
        :param js_method:
        :type js_method:
        :return:
        :rtype:
        """
        return self.apply(f"(e) => e['{js_method}']()")

    async def apply(self, js_function, return_by_value=True):
        self._remote_object = await self._tab.send(
            cdp.dom.resolve_node(backend_node_id=self.backend_node_id)
        )
        result: typing.Tuple[
            cdp.runtime.RemoteObject, typing.Any
        ] = await self._tab.send(
            cdp.runtime.call_function_on(
                js_function,
                object_id=self._remote_object.object_id,
                arguments=[
                    cdp.runtime.CallArgument(object_id=self._remote_object.object_id)
                ],
                return_by_value=True,
                user_gesture=True,
            )
        )
        if result and result[0]:
            if return_by_value:
                return result[0].value
            return result[0]
        elif result[1]:
            return result[1]

    async def get_position(self, abs=False) -> Position:
        await self.update()
        quads = await self._tab.send(
            cdp.dom.get_content_quads(object_id=self.remote_object.object_id)
        )
        try:
            pos = Position(quads[0])
            if abs:
                scroll_y = (await self.conn.evaluate("window.scrollY")).value
                scroll_x = (await self.conn.evaluate("window.scrollX")).value
                abs_x = pos.left + scroll_x + (pos.width / 2)
                abs_y = pos.top + scroll_y + (pos.height / 2)
                pos.abs_x = abs_x
                pos.abs_y = abs_y
            return pos
        except IndexError:
            logger.debug(
                "no content quads for %s. mostly caused by element which is not 'in plain sight'"
                % self
            )

    async def mouse_click(
        self,
        button: str = "left",
        buttons: typing.Optional[int] = 1,
        modifiers: typing.Optional[int] = 0,
        _until_event: typing.Optional[type] = None,
    ):
        """native click (on element) . note: this likely does not work atm, use click() instead

        :param button: str (default = "left")
        :param buttons: which button (default 1 = left)
        :param modifiers: *(Optional)* Bit field representing pressed modifier keys.
                Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
        :param _until_event: internal. event to wait for before returning
        :return:

        """
        try:
            center = (await self.get_position()).center
        except AttributeError:
            return
        if not center:
            logger.warning("could not calculate box model for %s", self)
            return

        logger.debug("clicking on location %.2f, %.2f" % center)

        await asyncio.gather(
            self._tab.send(
                cdp.input_.dispatch_mouse_event(
                    "mousePressed",
                    x=center[0],
                    y=center[1],
                    modifiers=modifiers,
                    button=cdp.input_.MouseButton(button),
                    buttons=buttons,
                    click_count=1,
                )
            ),
            self._tab.send(
                cdp.input_.dispatch_mouse_event(
                    "mouseReleased",
                    x=center[0],
                    y=center[1],
                    modifiers=modifiers,
                    button=cdp.input_.MouseButton(button),
                    buttons=buttons,
                    click_count=1,
                )
            ),
        )

    async def mouse_move(self):
        """moves mouse (not click), to element position. when an element has an
        hover/mouseover effect, this would trigger it"""
        try:
            center = (await self.get_position()).center
        except AttributeError:
            logger.debug("did not find location for %s", self)
            return
        logger.debug(
            "mouse move to location %.2f, %.2f where %s is located", *center, self
        )
        await self._tab.send(
            cdp.input_.dispatch_mouse_event("mouseMoved", x=center[0], y=center[1])
        )
        await self._tab
        await self._tab.send(
            cdp.input_.dispatch_mouse_event("mouseReleased", x=center[0], y=center[1])
        )

    async def scroll_into_view(self):
        """scrolls element into view"""
        await self.tab.send(
            cdp.dom.scroll_into_view_if_needed(backend_node_id=self.backend_node_id)
        )

        # await self.apply("""(el) => el.scrollIntoView(false)""")

    async def clear_input(self, _until_event: type = None):
        """clears an input field"""
        return await self.apply('function (element) { element.value = "" } ')

    async def send_keys(self, text: str):
        """
        send text to an input field, or any other html element.

        hint, if you ever get stuck where using py:meth:`~click`
        does not work, sending the keystroke \\n or \\r\\n or a spacebar work wonders!

        :param text: text to send
        :return: None
        """
        await self.apply("(elem) => elem.focus()")
        [
            await self._tab.send(cdp.input_.dispatch_key_event("char", text=char))
            for char in list(text)
        ]

    async def send_file(self, *file_paths: str):
        """
        some form input require a file (upload).
        this method sends 1 or more file(s) to the input field.

        needles to say, but make sure the field accepts multiple files if you want to send more files.
        otherwise the browser might crash.

        example :
        `await fileinputElement.send_file('c:/temp/image.png', 'c:/users/myuser/lol.gif')`

        """
        await self._tab.send(
            cdp.dom.set_file_input_files(
                files=[*file_paths],
                backend_node_id=self.backend_node_id,
                object_id=self.object_id,
            )
        )

    async def focus(self):
        """focus the current element. often useful in form (select) fields"""
        return await self.apply("(element) => element.focus()")

    async def select_option(self):
        """for form (select) fields. when you have queried the options you can call this method on the option object

        calling :func:`option.select_option()` will use that option as selected value.
        does not work in all cases.

        """
        if self.node_name == "OPTION":
            return await self.apply("(o) => o.selected = true")

    async def set_value(self, value):
        await self._tab.send(cdp.dom.set_node_value(node_id=self.node_id, value=value))

    async def set_text(self, value):
        if not self.node_type == 3:
            if self.child_node_count == 1:
                child_node = self.children[0]
                await child_node.set_text(value)
                await self.update()
                return
            else:
                raise RuntimeError("could only set value of text nodes")
        await self.update()
        await self._tab.send(cdp.dom.set_node_value(node_id=self.node_id, value=value))

    async def get_html(self):
        return await self._tab.send(
            cdp.dom.get_outer_html(backend_node_id=self.backend_node_id)
        )

    @property
    def text(self) -> str:
        """
        gets the text contents of this element
        note: this includes text in the form of script content, as those are also just 'text nodes'

        :return:
        :rtype:
        """
        text_node = util.filter_recurse(self.node, lambda n: n.node_type == 3)
        if text_node:
            return text_node.node_value
        return ""

    @property
    def text_all(self):
        """
        gets the text contents of this element, and it's children in a concatenated string
        note: this includes text in the form of script content, as those are also just 'text nodes'
        :return:
        :rtype:
        """
        text_nodes = util.filter_recurse_all(self.node, lambda n: n.node_type == 3)
        return " ".join([n.node_value for n in text_nodes])

    async def query_selector_all(self, selector: str):
        if self.node_name == "IFRAME":
            return await self.tab.query_selector_all(selector, _node=self)
        await self
        return await self._tab.query_selector_all(selector, self)

    async def query_selector(self, selector):
        if self.node_name == "IFRAME":
            return await self.tab.query_selector(selector, self)

        await self
        return await self._tab.query_selector(selector, self)

    #
    async def save_screenshot(
        self,
        filename: typing.Optional[PathLike] = "auto",
        format: typing.Optional[str] = "jpeg",
        scale: typing.Optional[typing.Union[int, float]] = 1,
    ):
        """
        Saves a screenshot of this element (only)
        This is not the same as :py:obj:`Tab.save_screenshot`, which saves a "regular" screenshot

        When the element is hidden, or has no size, or is otherwise not capturable, a RuntimeError is raised

        :param filename: uses this as the save path
        :type filename: PathLike
        :param format: jpeg or png (defaults to jpeg)
        :type format: str
        :param scale: the scale of the screenshot, eg: 1 = size as is, 2 = double, 0.5 is half
        :return: the path/filename of saved screenshot
        :rtype: str
        """

        import urllib.parse
        import datetime
        import base64

        pos = await self.get_position()
        if not pos:
            raise RuntimeError(
                "could not determine position of element. probably because it's not in view, or hidden"
            )
        viewport = pos.to_viewport(scale)
        path = None
        await self.tab
        if not filename or filename == "auto":
            parsed = urllib.parse.urlparse(self.tab.target.url)
            parts = parsed.path.split("/")
            last_part = parts[-1]
            last_part = last_part.rsplit("?", 1)[0]
            dt_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            candidate = f"{parsed.hostname}__{last_part}_{dt_str}"
            ext = ""
            if format.lower() in ["jpg", "jpeg"]:
                ext = ".jpg"
                format = "jpeg"
            elif format.lower() in ["png"]:
                ext = ".png"
                format = "png"
            path = pathlib.Path(candidate + ext)
        else:
            path = pathlib.Path(filename)

        path.parent.mkdir(parents=True, exist_ok=True)
        data = await self._tab.send(
            cdp.page.capture_screenshot(
                format, clip=viewport, capture_beyond_viewport=True
            )
        )
        data_bytes = base64.b64decode(data)
        if not path:
            raise RuntimeError("invalid filename or path: '%s'" % filename)
        path.write_bytes(data_bytes)
        return str(path)

    async def flash(self, duration: typing.Union[float, int] = 0.5):
        """
        displays for a short time a red dot on the element (only if the element itself is visible)

        :param coords: x,y
        :type coords: x,y
        :param duration: seconds (default 0.5)
        :type duration:
        :return:
        :rtype:
        """
        if not self.remote_object:
            self._remote_object = await self._tab.send(
                cdp.dom.resolve_node(backend_node_id=self.backend_node_id)
            )
        style = (
            "position:absolute;z-index:99999999;padding:0;margin:0; left:50% ;"
            "transform: translate(-50%, -50%);"
            "top: 50% ; width:1em;height:1em;border-radius:50%;background:red;opacity:0;"
            "animation:show-pointer-ani {:.2f}s ease 1;"
        ).format(duration)
        script = (
            """
            (targetElement) => {{
                var css = document.styleSheets[0];
                for( let css of [...document.styleSheets]) {{
                    try {{
                        css.insertRule(`
                        @keyframes show-pointer-ani {{
                              0% {{ opacity: 1; transform: scale(2, 2);}}
                              25% {{ transform: scale(5,5) }}
                              50% {{ transform: scale(3, 3);}}
                              75%: {{ transform: scale(2,2) }}
                              100% {{ transform: scale(1, 1); opacity: 0;}}
                        }}`,css.cssRules.length);
                        break;
                    }} catch (e) {{
                        console.log(e)
                    }}
                }};
                var _d = document.createElement('div');
                _d.style = `{0:s}`;
                _d.id = `{1:s}`;
                targetElement.insertAdjacentElement('afterBegin', _d);
                                
                setTimeout( () => document.getElementById('{1:s}').remove(), {2:d});
            }}
            """.format(
                style,
                secrets.token_hex(8),
                int(duration * 1000),
            )
            .replace("  ", "")
            .replace("\n", "")
        )
        arguments = [cdp.runtime.CallArgument(object_id=self._remote_object.object_id)]
        await self._tab.send(
            cdp.runtime.call_function_on(
                script,
                object_id=self._remote_object.object_id,
                arguments=arguments,
                await_promise=True,
                user_gesture=True,
            )
        )

    async def record_video(
        self,
        filename: typing.Optional[str] = None,
        folder: typing.Optional[str] = None,
        duration: typing.Optional[typing.Union[int, float]] = None,
    ):
        """
        experimental option.

        :param filename: the desired filename
        :param folder: the download folder path
        :param duration: record for this many seconds and then download

        on html5 video nodes, you can call this method to start recording of the video.

        when any of the follow happens:

        - video ends
        - calling videoelement('pause')
        - video stops

        the video recorded will be downloaded.

        """
        if self.node_name != "VIDEO":
            raise RuntimeError(
                "record_video can only be called on html5 video elements"
            )
        if not folder:
            directory_path = pathlib.Path.cwd() / "downloads"
        else:
            directory_path = pathlib.Path(folder)

        directory_path.mkdir(exist_ok=True)
        await self._tab.send(
            cdp.browser.set_download_behavior(
                "allow", download_path=str(directory_path)
            )
        )
        await self("pause")
        await self.apply(
            """
            function extractVid(vid) {{
                    
                      var duration = {duration:.1f}; 
                      var stream = vid.captureStream();
                      var mr = new MediaRecorder(stream, {{audio:true, video:true}})
                      mr.ondataavailable  = function(e) {{
                          vid['_recording'] = false
                          var blob = e.data;
                          f = new File([blob], {{name: {filename}, type:'octet/stream'}});
                          var objectUrl = URL.createObjectURL(f);
                          var link = document.createElement('a');
                          link.setAttribute('href', objectUrl)
                          link.setAttribute('download', {filename})
                          link.style.display = 'none'

                          document.body.appendChild(link)

                          link.click()

                          document.body.removeChild(link)
                       }}
                       
                       mr.start()
                       vid.addEventListener('ended' , (e) => mr.stop())
                       vid.addEventListener('pause' , (e) => mr.stop())
                       vid.addEventListener('abort', (e) => mr.stop())
                       
                       
                       if ( duration ) {{ 
                            setTimeout(() => {{ vid.pause(); vid.play() }}, duration);
                       }}
                       vid['_recording'] = true
                  ;}}
                
            """.format(
                filename=f'"{filename}"' if filename else 'document.title + ".mp4"',
                duration=int(duration * 1000) if duration else 0,
            )
        )
        await self("play")
        await self._tab

    async def is_recording(self):
        return await self.apply('(vid) => vid["_recording"]')

    def _make_attrs(self):
        sav = None
        if self.node.attributes:
            for i, a in enumerate(self.node.attributes):
                if i == 0 or i % 2 == 0:
                    if a == "class":
                        a = "class_"
                    sav = a
                else:
                    if sav:
                        self.attrs[sav] = a

    def __repr__(self):
        tag_name = self.node.node_name.lower()
        content = ""

        # collect all text from this leaf
        if self.child_node_count:
            if self.child_node_count == 1:
                if self.children:
                    content += str(self.children[0])

            elif self.child_node_count > 1:
                if self.children:
                    for child in self.children:
                        content += str(child)

        if self.node.node_type == 3:  # we could be a text node ourselves
            content += self.node_value

            # return text only, no tag names
            # this makes it look most natural, and compatible with other hml libs

            return content

        attrs = " ".join(
            [f'{k if k != "class_" else "class"}="{v}"' for k, v in self.attrs.items()]
        )
        s = f"<{tag_name} {attrs}>{content}</{tag_name}>"
        return s


class Position(cdp.dom.Quad):
    """helper class for element positioning"""

    def __init__(self, points):
        super().__init__(points)
        (
            self.left,
            self.top,
            self.right,
            self.top,
            self.right,
            self.bottom,
            self.left,
            self.bottom,
        ) = points
        self.abs_x: float = 0
        self.abs_y: float = 0
        self.x = self.left
        self.y = self.top
        self.height, self.width = (self.bottom - self.top, self.right - self.left)
        self.center = (
            self.left + (self.width / 2),
            self.top + (self.height / 2),
        )

    def to_viewport(self, scale=1):
        return cdp.page.Viewport(
            x=self.x, y=self.y, width=self.width, height=self.height, scale=scale
        )

    def __repr__(self):
        return f"<Position(x={self.left}, y={self.top}, width={self.width}, height={self.height})>"
