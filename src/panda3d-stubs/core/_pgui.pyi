from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import Vec2Like, Vec3Like, Vec4Like
from panda3d.core._audio import AudioSound
from panda3d.core._dtoolutil import ostream
from panda3d.core._gobj import Texture
from panda3d.core._linmath import LColor, LMatrix4, LVecBase2, LVecBase4, LVector3
from panda3d.core._pgraph import NodePath, PandaNode, TransformState
from panda3d.core._putil import ButtonHandle, TypedWritableReferenceCount
from panda3d.core._text import TextGraphic, TextNode, TextProperties
from panda3d.core._tform import MouseWatcher, MouseWatcherGroup, MouseWatcherParameter, MouseWatcherRegion

_PGFrameStyle_Type: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]

class PGFrameStyle:
    T_none: Final = 0
    TNone: Final = 0
    T_flat: Final = 1
    TFlat: Final = 1
    T_bevel_out: Final = 2
    TBevelOut: Final = 2
    T_bevel_in: Final = 3
    TBevelIn: Final = 3
    T_groove: Final = 4
    TGroove: Final = 4
    T_ridge: Final = 5
    TRidge: Final = 5
    T_texture_border: Final = 6
    TTextureBorder: Final = 6
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: PGFrameStyle = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def set_type(self, type: _PGFrameStyle_Type) -> None:
        """Sets the basic type of frame."""
    def get_type(self) -> _PGFrameStyle_Type:
        """Returns the basic type of frame."""
    @overload
    def set_color(self, color: Vec4Like) -> None:
        """Sets the dominant color of the frame."""
    @overload
    def set_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def get_color(self) -> LColor:
        """Returns the dominant color of the frame."""
    def set_texture(self, texture: Texture) -> None:
        """Specifies a texture that should be applied to the frame."""
    def has_texture(self) -> bool:
        """Returns true if a texture has been applied to the frame."""
    def get_texture(self) -> Texture:
        """Returns the texture that has been applied to the frame, or NULL if no
        texture has been applied.
        """
    def clear_texture(self) -> None:
        """Removes the texture from the frame."""
    @overload
    def set_width(self, width: Vec2Like) -> None:
        """Sets the width parameter, which has meaning only for certain frame types.
        For instance, this is the width of the bevel for T_bevel_in or T_bevel_out.
        The units are in screen units.
        """
    @overload
    def set_width(self, x: float, y: float) -> None: ...
    def get_width(self) -> LVecBase2:
        """Returns the width parameter, which has meaning only for certain frame
        types.  For instance, this is the width of the bevel for T_bevel_in or
        T_bevel_out.  The units are in screen units.
        """
    @overload
    def set_uv_width(self, uv_width: Vec2Like) -> None:
        """Sets the uv_width parameter, which indicates the amount of the texture that
        is consumed by the inner bevel--the width in texture space of the amount
        indicated by set_width.
        """
    @overload
    def set_uv_width(self, u: float, v: float) -> None: ...
    def get_uv_width(self) -> LVecBase2:
        """See set_uv_width()."""
    @overload
    def set_visible_scale(self, visible_scale: Vec2Like) -> None:
        """Sets a scale factor on the visible representation of the frame, in the X
        and Y directions.  If this scale factor is other than 1, it will affect the
        size of the visible frame representation within the actual frame border.
        """
    @overload
    def set_visible_scale(self, x: float, y: float) -> None: ...
    def get_visible_scale(self) -> LVecBase2:
        """Returns the scale factor on the visible representation of the frame, in the
        X and Y directions.  If this scale factor is other than 1, it will affect
        the size of the visible frame representation within the actual frame
        border.
        """
    def get_internal_frame(self, frame: Vec4Like) -> LVecBase4:
        """Computes the size of the internal frame, given the indicated external
        frame, appropriate for this kind of frame style.  This simply subtracts the
        border width for those frame styles that include a border.
        """
    def output(self, out: ostream) -> None: ...
    setType = set_type
    getType = get_type
    setColor = set_color
    getColor = get_color
    setTexture = set_texture
    hasTexture = has_texture
    getTexture = get_texture
    clearTexture = clear_texture
    setWidth = set_width
    getWidth = get_width
    setUvWidth = set_uv_width
    getUvWidth = get_uv_width
    setVisibleScale = set_visible_scale
    getVisibleScale = get_visible_scale
    getInternalFrame = get_internal_frame

class PGItem(PandaNode):
    """This is the base class for all the various kinds of gui widget objects.

    It is a Node which corresponds to a rectangular region on the screen, and
    it may have any number of "state" subgraphs, one of which is rendered at
    any given time according to its current state.

    The PGItem node must be parented to the scene graph somewhere beneath a
    PGTop node in order for this behavior to work.
    """

    @overload
    def set_frame(self, frame: Vec4Like) -> None:
        """Sets the bounding rectangle of the item, in local coordinates.  This is the
        region on screen within which the mouse will be considered to be within the
        item.  Normally, it should correspond to the bounding rectangle of the
        visible geometry of the item.
        """
    @overload
    def set_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_frame(self) -> LVecBase4:
        """Returns the bounding rectangle of the item.  See set_frame().  It is an
        error to call this if has_frame() returns false.
        """
    def has_frame(self) -> bool:
        """Returns true if the item has a bounding rectangle; see set_frame()."""
    def clear_frame(self) -> None:
        """Removes the bounding rectangle from the item.  It will no longer be
        possible to position the mouse within the item; see set_frame().
        """
    def set_state(self, state: int) -> None:  # type: ignore[override]
        """Sets the "state" of this particular PGItem.

        The PGItem node will render as if it were the subgraph assigned to the
        corresponding index via set_state_def().
        """
    def get_state(self) -> int:  # type: ignore[override]
        """Returns the "state" of this particular PGItem.  See set_state()."""
    def set_active(self, active: bool) -> None:
        """Sets whether the PGItem is active for mouse watching.  This is not
        necessarily related to the active/inactive appearance of the item, which is
        controlled by set_state(), but it does affect whether it responds to mouse
        events.
        """
    def get_active(self) -> bool:
        """Returns whether the PGItem is currently active for mouse events.  See
        set_active().
        """
    def set_focus(self, focus: bool) -> None:
        """Sets whether the PGItem currently has keyboard focus.  This simply means
        that the item may respond to keyboard events as well as to mouse events;
        precisely what this means is up to the individual item.

        Only one PGItem in the world is allowed to have focus at any given time.
        Setting the focus on any other item automatically disables the focus from
        the previous item.
        """
    def get_focus(self) -> bool:
        """Returns whether the PGItem currently has focus for keyboard events.  See
        set_focus().
        """
    def set_background_focus(self, focus: bool) -> None:
        """Sets the background_focus flag for this item.  When background_focus is
        enabled, the item will receive keypress events even if it is not in focus;
        in fact, even if it is not onscreen.  Unlike normal focus, many items may
        have background_focus simultaneously.
        """
    def get_background_focus(self) -> bool:
        """Returns whether background_focus is currently enabled.  See
        set_background_focus().
        """
    def set_suppress_flags(self, suppress_flags: int) -> None:
        """This is just an interface to set the suppress flags on the underlying
        MouseWatcherRegion.  See MouseWatcherRegion::set_suppress_flags().
        """
    def get_suppress_flags(self) -> int:
        """This is just an interface to get the suppress flags on the underlying
        MouseWatcherRegion.  See MouseWatcherRegion::get_suppress_flags().
        """
    def get_num_state_defs(self) -> int:
        """Returns one more than the highest-numbered state def that was ever assigned
        to the PGItem.  The complete set of state defs assigned may then be
        retrieved by indexing from 0 to (get_num_state_defs() - 1).

        This is only an upper limit on the actual number of state defs, since there
        may be holes in the list.
        """
    def clear_state_def(self, state: int) -> None:
        """Resets the NodePath assigned to the indicated state to its initial default,
        with only a frame representation if appropriate.
        """
    def has_state_def(self, state: int) -> bool:
        """Returns true if get_state_def() has ever been called for the indicated
        state (thus defining a render subgraph for this state index), false
        otherwise.
        """
    def get_state_def(self, state: int) -> NodePath:
        """Returns the Node that is the root of the subgraph that will be drawn when
        the PGItem is in the indicated state.  The first time this is called for a
        particular state index, it may create the Node.
        """
    def instance_to_state_def(self, state: int, path: NodePath) -> NodePath:
        """Parents an instance of the bottom node of the indicated NodePath to the
        indicated state index.
        """
    def get_frame_style(self, state: int) -> PGFrameStyle:
        """Returns the kind of frame that will be drawn behind the item when it is in
        the indicated state.
        """
    def set_frame_style(self, state: int, style: PGFrameStyle) -> None:
        """Changes the kind of frame that will be drawn behind the item when it is in
        the indicated state.
        """
    def get_id(self) -> str:
        """Returns the unique ID assigned to this PGItem.  This will be assigned to
        the region created with the MouseWatcher, and will thus be used to generate
        event names.
        """
    def set_id(self, id: str) -> None:
        """Set the unique ID assigned to this PGItem.  It is the user's responsibility
        to ensure that this ID is unique.

        Normally, this should not need to be called, as the PGItem will assign
        itself an ID when it is created, but this function allows the user to
        decide to redefine the ID to be something possibly more meaningful.
        """
    @staticmethod
    def get_enter_prefix() -> str:
        """Returns the prefix that is used to define the enter event for all PGItems.
        The enter event is the concatenation of this string followed by get_id().
        """
    @staticmethod
    def get_exit_prefix() -> str:
        """Returns the prefix that is used to define the exit event for all PGItems.
        The exit event is the concatenation of this string followed by get_id().
        """
    @staticmethod
    def get_within_prefix() -> str:
        """Returns the prefix that is used to define the within event for all PGItems.
        The within event is the concatenation of this string followed by get_id().
        """
    @staticmethod
    def get_without_prefix() -> str:
        """Returns the prefix that is used to define the without event for all
        PGItems.  The without event is the concatenation of this string followed by
        get_id().
        """
    @staticmethod
    def get_focus_in_prefix() -> str:
        """Returns the prefix that is used to define the focus_in event for all
        PGItems.  The focus_in event is the concatenation of this string followed
        by get_id().

        Unlike most item events, this event is thrown with no parameters.
        """
    @staticmethod
    def get_focus_out_prefix() -> str:
        """Returns the prefix that is used to define the focus_out event for all
        PGItems.  The focus_out event is the concatenation of this string followed
        by get_id().

        Unlike most item events, this event is thrown with no parameters.
        """
    @staticmethod
    def get_press_prefix() -> str:
        """Returns the prefix that is used to define the press event for all PGItems.
        The press event is the concatenation of this string followed by a button
        name, followed by a hyphen and get_id().
        """
    @staticmethod
    def get_repeat_prefix() -> str:
        """Returns the prefix that is used to define the repeat event for all PGItems.
        The repeat event is the concatenation of this string followed by a button
        name, followed by a hyphen and get_id().
        """
    @staticmethod
    def get_release_prefix() -> str:
        """Returns the prefix that is used to define the release event for all
        PGItems.  The release event is the concatenation of this string followed by
        a button name, followed by a hyphen and get_id().
        """
    @staticmethod
    def get_keystroke_prefix() -> str:
        """Returns the prefix that is used to define the keystroke event for all
        PGItems.  The keystroke event is the concatenation of this string followed
        by a hyphen and get_id().
        """
    def get_enter_event(self) -> str:
        """Returns the event name that will be thrown when the item is active and the
        mouse enters its frame, but not any nested frames.
        """
    def get_exit_event(self) -> str:
        """Returns the event name that will be thrown when the item is active and the
        mouse exits its frame, or enters a nested frame.
        """
    def get_within_event(self) -> str:
        """Returns the event name that will be thrown when the item is active and the
        mouse moves within the boundaries of the frame.  This is different from the
        enter_event in that the mouse is considered within the frame even if it is
        also within a nested frame.
        """
    def get_without_event(self) -> str:
        """Returns the event name that will be thrown when the item is active and the
        mouse moves completely outside the boundaries of the frame.  This is
        different from the exit_event in that the mouse is considered within the
        frame even if it is also within a nested frame.
        """
    def get_focus_in_event(self) -> str:
        """Returns the event name that will be thrown when the item gets the keyboard
        focus.
        """
    def get_focus_out_event(self) -> str:
        """Returns the event name that will be thrown when the item loses the keyboard
        focus.
        """
    def get_press_event(self, button: ButtonHandle | str) -> str:
        """Returns the event name that will be thrown when the item is active and the
        indicated mouse or keyboard button is depressed while the mouse is within
        the frame.
        """
    def get_repeat_event(self, button: ButtonHandle | str) -> str:
        """Returns the event name that will be thrown when the item is active and the
        indicated mouse or keyboard button is continuously held down while the
        mouse is within the frame.
        """
    def get_release_event(self, button: ButtonHandle | str) -> str:
        """Returns the event name that will be thrown when the item is active and the
        indicated mouse or keyboard button, formerly clicked down is within the
        frame, is released.
        """
    def get_keystroke_event(self) -> str:
        """Returns the event name that will be thrown when the item is active and any
        key is pressed by the user.
        """
    def get_frame_inv_xform(self) -> LMatrix4:
        """Returns the inverse of the frame transform matrix"""
    def set_sound(self, event: str, sound: AudioSound) -> None:
        """Sets the sound that will be played whenever the indicated event occurs."""
    def clear_sound(self, event: str) -> None:
        """Removes the sound associated with the indicated event."""
    def get_sound(self, event: str) -> AudioSound:
        """Returns the sound associated with the indicated event, or NULL if there is
        no associated sound.
        """
    def has_sound(self, event: str) -> bool:
        """Returns true if there is a sound associated with the indicated event, or
        false otherwise.
        """
    @staticmethod
    def get_text_node() -> TextNode:
        """Returns the TextNode object that will be used by all PGItems to generate
        default labels given a string.  This can be loaded with the default font,
        etc.
        """
    @staticmethod
    def set_text_node(node: TextNode) -> None:
        """Changes the TextNode object that will be used by all PGItems to generate
        default labels given a string.  This can be loaded with the default font,
        etc.
        """
    @staticmethod
    def get_focus_item() -> PGItem:
        """Returns the one PGItem in the world that currently has keyboard focus, if
        any, or NULL if no item has keyboard focus.  Use PGItem::set_focus() to
        activate or deactivate keyboard focus on a particular item.
        """
    def get_state_defs(self) -> tuple[NodePath, ...]: ...
    setFrame = set_frame
    getFrame = get_frame
    hasFrame = has_frame
    clearFrame = clear_frame
    setState = set_state  # type: ignore[assignment]
    getState = get_state  # type: ignore[assignment]
    setActive = set_active
    getActive = get_active
    setFocus = set_focus
    getFocus = get_focus
    setBackgroundFocus = set_background_focus
    getBackgroundFocus = get_background_focus
    setSuppressFlags = set_suppress_flags
    getSuppressFlags = get_suppress_flags
    getNumStateDefs = get_num_state_defs
    clearStateDef = clear_state_def
    hasStateDef = has_state_def
    getStateDef = get_state_def
    instanceToStateDef = instance_to_state_def
    getFrameStyle = get_frame_style
    setFrameStyle = set_frame_style
    getId = get_id
    setId = set_id
    getEnterPrefix = get_enter_prefix
    getExitPrefix = get_exit_prefix
    getWithinPrefix = get_within_prefix
    getWithoutPrefix = get_without_prefix
    getFocusInPrefix = get_focus_in_prefix
    getFocusOutPrefix = get_focus_out_prefix
    getPressPrefix = get_press_prefix
    getRepeatPrefix = get_repeat_prefix
    getReleasePrefix = get_release_prefix
    getKeystrokePrefix = get_keystroke_prefix
    getEnterEvent = get_enter_event
    getExitEvent = get_exit_event
    getWithinEvent = get_within_event
    getWithoutEvent = get_without_event
    getFocusInEvent = get_focus_in_event
    getFocusOutEvent = get_focus_out_event
    getPressEvent = get_press_event
    getRepeatEvent = get_repeat_event
    getReleaseEvent = get_release_event
    getKeystrokeEvent = get_keystroke_event
    getFrameInvXform = get_frame_inv_xform
    setSound = set_sound
    clearSound = clear_sound
    getSound = get_sound
    hasSound = has_sound
    getTextNode = get_text_node
    setTextNode = set_text_node
    getFocusItem = get_focus_item
    getStateDefs = get_state_defs

class PGButton(PGItem):
    """This is a particular kind of PGItem that is specialized to behave like a
    normal button object.  It keeps track of its own state, and handles mouse
    events sensibly.
    """

    S_ready: Final = 0
    SReady: Final = 0
    S_depressed: Final = 1
    SDepressed: Final = 1
    S_rollover: Final = 2
    SRollover: Final = 2
    S_inactive: Final = 3
    SInactive: Final = 3
    @property
    def click_prefix(self) -> str: ...
    @overload
    def setup(self, ready: NodePath, depressed: NodePath = ...) -> None:
        """`(self, ready: NodePath)`; `(self, ready: NodePath, depressed: NodePath)`; `(self, ready: NodePath, depressed: NodePath, rollover: NodePath)`; `(self, ready: NodePath, depressed: NodePath, rollover: NodePath, inactive: NodePath)`:
        Sets up the button using the indicated NodePath as arbitrary geometry.

        `(self, label: str, bevel: float = ...)`:
        Sets up the button as a default text button using the indicated label
        string.  The TextNode defined by PGItem::get_text_node() will be used to
        create the label geometry.  This automatically sets up the frame according
        to the size of the text.
        """
    @overload
    def setup(self, label: str, bevel: float = ...) -> None: ...
    @overload
    def setup(self, ready: NodePath, depressed: NodePath, rollover: NodePath, inactive: NodePath = ...) -> None: ...
    def add_click_button(self, button: ButtonHandle | str) -> bool:
        """Adds the indicated button to the set of buttons that can effectively
        "click" the PGButton.  Normally, this is just MouseButton::one().  Returns
        true if the button was added, or false if it was already there.
        """
    def remove_click_button(self, button: ButtonHandle | str) -> bool:
        """Removes the indicated button from the set of buttons that can effectively
        "click" the PGButton.  Normally, this is just MouseButton::one().  Returns
        true if the button was removed, or false if it was not in the set.
        """
    def has_click_button(self, button: ButtonHandle | str) -> bool:
        """Returns true if the indicated button is on the set of buttons that can
        effectively "click" the PGButton.  Normally, this is just
        MouseButton::one().
        """
    def is_button_down(self) -> bool:
        """Returns true if the user is currently holding the mouse button down on the
        button, false otherwise.
        """
    @staticmethod
    def get_click_prefix() -> str:
        """Returns the prefix that is used to define the click event for all
        PGButtons.  The click event is the concatenation of this string followed by
        get_id().
        """
    def get_click_event(self, button: ButtonHandle | str) -> str:
        """Returns the event name that will be thrown when the button is clicked
        normally.
        """
    addClickButton = add_click_button
    removeClickButton = remove_click_button
    hasClickButton = has_click_button
    isButtonDown = is_button_down
    getClickPrefix = get_click_prefix
    getClickEvent = get_click_event

class PGTop(PandaNode):
    """The "top" node of the new Panda GUI system.  This node must be parented to
    the 2-d scene graph, and all PG objects should be parented to this node or
    somewhere below it.  PG objects not parented within this hierarchy will not
    be clickable.

    This node begins the special traversal of the PG objects that registers
    each node within the MouseWatcher and forces everything to render in a
    depth-first, left-to-right order, appropriate for 2-d objects.
    """

    def set_mouse_watcher(self, watcher: MouseWatcher) -> None:
        """Sets the MouseWatcher pointer that the PGTop object registers its PG items
        with.  This must be set before the PG items are active.
        """
    def get_mouse_watcher(self) -> MouseWatcher:
        """Returns the MouseWatcher pointer that the PGTop object registers its PG
        items with, or NULL if the MouseWatcher has not yet been set.
        """
    def get_group(self) -> MouseWatcherGroup:
        """Returns the MouseWatcherGroup pointer that the PGTop object registers its
        PG items with, or NULL if the MouseWatcher has not yet been set.
        """
    def set_start_sort(self, start_sort: int) -> None:
        """Specifies the sort index that is assigned during the traversal to the first
        PGItem that is discovered during traversal.  Subsequent PGItems will be
        assigned consecutively higher sort indexes.

        This number is used by the MouseWatcher system to rank the clickable mouse
        regions in the same order in which the items are rendered, so that items on
        top will receive mouse priority.

        Normally, it makes the most sense to leave this initial value at its
        default value of 0, unless you need the PGItems to have a particular sort
        value with respect to some other objects in the scene (particularly with a
        second PGTop node).
        """
    def get_start_sort(self) -> int:
        """Returns the sort index that is assigned during the traversal to the first
        PGItem that is discovered during traversal.  See set_start_sort().
        """
    setMouseWatcher = set_mouse_watcher
    getMouseWatcher = get_mouse_watcher
    getGroup = get_group
    setStartSort = set_start_sort
    getStartSort = get_start_sort

class PGEntry(PGItem):
    """This is a particular kind of PGItem that handles simple one-line or short
    multi-line text entries, of the sort where the user can type any string.

    A PGEntry does all of its internal manipulation on a wide string, so it can
    store the full Unicode character set.  The interface can support either the
    wide string getters and setters, or the normal 8-bit string getters and
    setters, which use whatever encoding method is specified by the associated
    TextNode.
    """

    S_focus: Final = 0
    SFocus: Final = 0
    S_no_focus: Final = 1
    SNoFocus: Final = 1
    S_inactive: Final = 2
    SInactive: Final = 2
    def setup(self, width: float, num_lines: int) -> None:
        """Sets up the entry for normal use.  The width is the maximum width of
        characters that will be typed, and num_lines is the integer number of lines
        of text of the entry.  Both of these together determine the size of the
        entry, based on the TextNode in effect.
        """
    def setup_minimal(self, width: float, num_lines: int) -> None:
        """Sets up the entry without creating any frame or other decoration."""
    def set_text(self, text: str) -> bool:
        """Changes the text currently displayed within the entry.  This uses the
        Unicode encoding currently specified for the "focus" TextNode; therefore,
        the TextNode must exist before calling set_text().

        The return value is true if all the text is accepted, or false if some was
        truncated (see set_max_width(), etc.).
        """
    def get_plain_text(self) -> str:
        """Returns the text currently displayed within the entry, without any embedded
        properties characters.

        This uses the Unicode encoding currently specified for the "focus"
        TextNode; therefore, the TextNode must exist before calling get_text().
        """
    def get_text(self) -> str:
        """Returns the text currently displayed within the entry.  This uses the
        Unicode encoding currently specified for the "focus" TextNode; therefore,
        the TextNode must exist before calling get_text().
        """
    def get_num_characters(self) -> int:
        """Returns the number of characters of text in the entry.  This is the actual
        number of visible characters, not counting implicit newlines due to
        wordwrapping, or formatted characters for text properties changes.  If
        there is an embedded TextGraphic object, it counts as one character.

        This is also the length of the string returned by get_plain_text().
        """
    def get_character(self, n: int) -> int:
        """Returns the character at the indicated position in the entry.  If the
        object at this position is a graphic object instead of a character, returns
        0.
        """
    def get_graphic(self, n: int) -> TextGraphic:
        """Returns the graphic object at the indicated position in the pre-wordwrapped
        string.  If the object at this position is a character instead of a graphic
        object, returns NULL.
        """
    def get_properties(self, n: int) -> TextProperties:
        """Returns the TextProperties in effect for the object at the indicated
        position in the pre-wordwrapped string.
        """
    def set_cursor_position(self, position: int) -> None:
        """Sets the current position of the cursor.  This is the position within the
        text at which the next letter typed by the user will be inserted; normally
        it is the same as the length of the text.
        """
    def get_cursor_position(self) -> int:
        """Returns the current position of the cursor."""
    def get_cursor_X(self) -> float: ...
    def get_cursor_Y(self) -> float: ...
    def set_max_chars(self, max_chars: int) -> None:
        """Sets the maximum number of characters that may be typed into the entry.
        This is a limit on the number of characters, as opposed to the width of the
        entry; see also set_max_width().

        If this is 0, there is no limit.
        """
    def get_max_chars(self) -> int:
        """Returns the current maximum number of characters that may be typed into the
        entry, or 0 if there is no limit.  See set_max_chars().
        """
    def set_max_width(self, max_width: float) -> None:
        """Sets the maximum width of all characters that may be typed into the entry.
        This is a limit on the width of the formatted text, not a fixed limit on
        the number of characters; also set_max_chars().

        If this is 0, there is no limit.

        If _num_lines is more than 1, rather than being a fixed width on the whole
        entry, this becomes instead the wordwrap width (and the width limit on the
        entry is essentially _max_width * _num_lines).
        """
    def get_max_width(self) -> float:
        """Returns the current maximum width of the characters that may be typed into
        the entry, or 0 if there is no limit.  See set_max_width().
        """
    def set_num_lines(self, num_lines: int) -> None:
        """Sets the number of lines of text the PGEntry will use.  This only has
        meaning if _max_width is not 0; _max_width indicates the wordwrap width of
        each line.
        """
    def get_num_lines(self) -> int:
        """Returns the number of lines of text the PGEntry will use, if _max_width is
        not 0.  See set_num_lines().
        """
    def set_blink_rate(self, blink_rate: float) -> None:
        """Sets the number of times per second the cursor will blink while the entry
        has keyboard focus.

        If this is 0, the cursor does not blink, but is held steady.
        """
    def get_blink_rate(self) -> float:
        """Returns the number of times per second the cursor will blink, or 0 if the
        cursor is not to blink.
        """
    def get_cursor_def(self) -> NodePath:
        """Returns the Node that will be rendered to represent the cursor.  You can
        attach suitable cursor geometry to this node.
        """
    def clear_cursor_def(self) -> None:
        """Removes all the children from the cursor_def node, in preparation for
        adding a new definition.
        """
    def set_cursor_keys_active(self, flag: bool) -> None:
        """Sets whether the arrow keys (and home/end) control movement of the cursor.
        If true, they are active; if false, they are ignored.
        """
    def get_cursor_keys_active(self) -> bool:
        """Returns whether the arrow keys are currently set to control movement of the
        cursor; see set_cursor_keys_active().
        """
    def set_obscure_mode(self, flag: bool) -> None:
        """Specifies whether obscure mode should be enabled.  In obscure mode, a
        string of asterisks is displayed instead of the literal text, e.g.  for
        entering passwords.

        In obscure mode, the width of the text is computed based on the width of
        the string of asterisks, not on the width of the actual text.  This has
        implications on the maximum length of text that may be entered if max_width
        is in effect.
        """
    def get_obscure_mode(self) -> bool:
        """Specifies whether obscure mode is enabled.  See set_obscure_mode()."""
    def set_overflow_mode(self, flag: bool) -> None:
        """Specifies whether overflow mode should be enabled.  In overflow mode, text
        can overflow the boundaries of the Entry element horizontally.

        Overflow mode only works when the number of lines is 1.
        """
    def get_overflow_mode(self) -> bool:
        """Specifies whether overflow mode is enabled.  See set_overflow_mode()."""
    def set_candidate_active(self, candidate_active: str) -> None:
        """Specifies the name of the TextProperties structure added to the
        TextPropertiesManager that will be used to render candidate strings from
        the IME, used for typing characters in east Asian languages.  Each
        candidate string represents one possible way to interpret the sequence of
        keys the user has just entered; it should not be considered typed yet, but
        it is important for the user to be able to see what he is considering
        entering.

        This particular method sets the properties for the subset of the current
        candidate string that the user can actively scroll through.
        """
    def get_candidate_active(self) -> str:
        """See set_candidate_active()."""
    def set_candidate_inactive(self, candidate_inactive: str) -> None:
        """Specifies the name of the TextProperties structure added to the
        TextPropertiesManager that will be used to render candidate strings from
        the IME, used for typing characters in east Asian languages.  Each
        candidate string represents one possible way to interpret the sequence of
        keys the user has just entered; it should not be considered typed yet, but
        it is important for the user to be able to see what he is considering
        entering.

        This particular method sets the properties for the subset of the current
        candidate string that the user is not actively scrolling through.
        """
    def get_candidate_inactive(self) -> str:
        """See set_candidate_inactive()."""
    def set_text_def(self, state: int, node: TextNode) -> None:
        """Changes the TextNode that will be used to render the text within the entry
        when the entry is in the indicated state.  The default if nothing is
        specified is the same TextNode returned by PGItem::get_text_node().
        """
    def get_text_def(self, state: int) -> TextNode:
        """Returns the TextNode that will be used to render the text within the entry
        when the entry is in the indicated state.  See set_text_def().
        """
    @staticmethod
    def get_accept_prefix() -> str:
        """Returns the prefix that is used to define the accept event for all
        PGEntries.  The accept event is the concatenation of this string followed
        by get_id().
        """
    @staticmethod
    def get_accept_failed_prefix() -> str:
        """Returns the prefix that is used to define the accept failed event for all
        PGEntries.  This event is the concatenation of this string followed by
        get_id().
        """
    @staticmethod
    def get_overflow_prefix() -> str:
        """Returns the prefix that is used to define the overflow event for all
        PGEntries.  The overflow event is the concatenation of this string followed
        by get_id().
        """
    @staticmethod
    def get_type_prefix() -> str:
        """Returns the prefix that is used to define the type event for all PGEntries.
        The type event is the concatenation of this string followed by get_id().
        """
    @staticmethod
    def get_erase_prefix() -> str:
        """Returns the prefix that is used to define the erase event for all
        PGEntries.  The erase event is the concatenation of this string followed by
        get_id().
        """
    @staticmethod
    def get_cursormove_prefix() -> str:
        """Returns the prefix that is used to define the cursor event for all
        PGEntries.  The cursor event is the concatenation of this string followed
        by get_id().
        """
    def get_accept_event(self, button: ButtonHandle | str) -> str:
        """Returns the event name that will be thrown when the entry is accepted
        normally.
        """
    def get_accept_failed_event(self, button: ButtonHandle | str) -> str:
        """Returns the event name that will be thrown when the entry cannot accept an
        input
        """
    def get_overflow_event(self) -> str:
        """Returns the event name that will be thrown when too much text is attempted
        to be entered into the PGEntry, exceeding either the limit set via
        set_max_chars() or via set_max_width().
        """
    def get_type_event(self) -> str:
        """Returns the event name that will be thrown whenever the user extends the
        text by typing.
        """
    def get_erase_event(self) -> str:
        """Returns the event name that will be thrown whenever the user erases
        characters in the text.
        """
    def get_cursormove_event(self) -> str:
        """Returns the event name that will be thrown whenever the cursor moves"""
    def set_wtext(self, wtext: str) -> bool:
        """Changes the text currently displayed within the entry.

        The return value is true if all the text is accepted, or false if some was
        truncated (see set_max_width(), etc.).
        """
    def get_plain_wtext(self) -> str:
        """Returns the text currently displayed within the entry, without any embedded
        properties characters.
        """
    def get_wtext(self) -> str:
        """Returns the text currently displayed within the entry."""
    def set_accept_enabled(self, enabled: bool) -> None:
        """Sets whether the input may be accepted--use to disable submission by the
        user
        """
    def is_wtext(self) -> bool:
        """Returns true if any of the characters in the string returned by get_wtext()
        are out of the range of an ASCII character (and, therefore, get_wtext()
        should be called in preference to get_text()).
        """
    setupMinimal = setup_minimal
    setText = set_text
    getPlainText = get_plain_text
    getText = get_text
    getNumCharacters = get_num_characters
    getCharacter = get_character
    getGraphic = get_graphic
    getProperties = get_properties
    setCursorPosition = set_cursor_position
    getCursorPosition = get_cursor_position
    getCursorX = get_cursor_X
    getCursorY = get_cursor_Y
    setMaxChars = set_max_chars
    getMaxChars = get_max_chars
    setMaxWidth = set_max_width
    getMaxWidth = get_max_width
    setNumLines = set_num_lines
    getNumLines = get_num_lines
    setBlinkRate = set_blink_rate
    getBlinkRate = get_blink_rate
    getCursorDef = get_cursor_def
    clearCursorDef = clear_cursor_def
    setCursorKeysActive = set_cursor_keys_active
    getCursorKeysActive = get_cursor_keys_active
    setObscureMode = set_obscure_mode
    getObscureMode = get_obscure_mode
    setOverflowMode = set_overflow_mode
    getOverflowMode = get_overflow_mode
    setCandidateActive = set_candidate_active
    getCandidateActive = get_candidate_active
    setCandidateInactive = set_candidate_inactive
    getCandidateInactive = get_candidate_inactive
    setTextDef = set_text_def
    getTextDef = get_text_def
    getAcceptPrefix = get_accept_prefix
    getAcceptFailedPrefix = get_accept_failed_prefix
    getOverflowPrefix = get_overflow_prefix
    getTypePrefix = get_type_prefix
    getErasePrefix = get_erase_prefix
    getCursormovePrefix = get_cursormove_prefix
    getAcceptEvent = get_accept_event
    getAcceptFailedEvent = get_accept_failed_event
    getOverflowEvent = get_overflow_event
    getTypeEvent = get_type_event
    getEraseEvent = get_erase_event
    getCursormoveEvent = get_cursormove_event
    setWtext = set_wtext
    getPlainWtext = get_plain_wtext
    getWtext = get_wtext
    setAcceptEnabled = set_accept_enabled
    isWtext = is_wtext

class PGMouseWatcherParameter(TypedWritableReferenceCount, MouseWatcherParameter):
    """This specialization on MouseWatcherParameter allows us to tag on additional
    elements to events for the gui system, and also inherits from
    TypedWritableReferenceCount so we can attach this thing to an event.
    """

    def __init__(self, __param0: PGMouseWatcherParameter) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_MouseWatcherParameter(self) -> MouseWatcherParameter: ...
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToMouseWatcherParameter = upcast_to_MouseWatcherParameter

class PGMouseWatcherBackground(MouseWatcherRegion):
    """This is a special kind of MouseWatcherRegion that doesn't have a rectangle
    and is never active, but just quietly listens for keypresses and sends them
    to all the PGItems with background focus.
    """

    def __init__(self, __param0: PGMouseWatcherBackground = ...) -> None: ...

class PGVirtualFrame(PGItem):
    """This represents a frame that is rendered as a window onto another (possibly
    much larger) canvas.  You can only see the portion of the canvas that is
    below the window at any given time.

    This works simply by automatically defining a scissor effect to be applied
    to a special child node, called the canvas_node, of the PGVirtualFrame
    node.  Every object that is parented to the canvas_node will be clipped by
    the scissor effect.  Also, you can modify the canvas_transform through
    convenience methods here, which actually modifies the transform on the
    canvas_node.

    The net effect is that the virtual canvas is arbitrarily large, and we can
    peek at it through the scissor region, and scroll through different parts
    of it by modifying the canvas_transform.

    See PGScrollFrame for a specialization of this class that handles the
    traditional scrolling canvas, with scroll bars.
    """

    def __init__(self, name: str = ...) -> None: ...
    def setup(self, width: float, height: float) -> None:
        """Creates a PGVirtualFrame with the indicated dimensions."""
    @overload
    def set_clip_frame(self, clip_frame: Vec4Like) -> None:
        """Sets the bounding rectangle of the clip frame.  This is the size of the
        small window through which we can see the virtual canvas.  Normally, this
        is the same size as the actual frame or smaller (typically it is smaller by
        the size of the bevel, or to make room for scroll bars).
        """
    @overload
    def set_clip_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_clip_frame(self) -> LVecBase4:
        """Returns the bounding rectangle of the clip frame.  See set_clip_frame().
        If has_clip_frame() is false, this returns the item's actual frame.
        """
    def has_clip_frame(self) -> bool:
        """Returns true if the clip frame has been set; see set_clip_frame().  If it
        has not been set, objects in the virtual frame will not be clipped.
        """
    def clear_clip_frame(self) -> None:
        """Removes the clip frame from the item.  This disables clipping."""
    def set_canvas_transform(self, transform: TransformState) -> None:
        """Changes the transform of the virtual canvas.  This transform is applied to
        all child nodes of the canvas_node.
        """
    def get_canvas_transform(self) -> TransformState:
        """Returns the transform of the virtual canvas.  This transform is applied to
        all child nodes of the canvas_node.
        """
    def get_canvas_node(self) -> PandaNode:
        """Returns the special node that holds all of the children that appear in the
        virtual canvas.
        """
    def get_canvas_parent(self) -> PandaNode:
        """Returns the parent node of the canvas_node."""
    setClipFrame = set_clip_frame
    getClipFrame = get_clip_frame
    hasClipFrame = has_clip_frame
    clearClipFrame = clear_clip_frame
    setCanvasTransform = set_canvas_transform
    getCanvasTransform = get_canvas_transform
    getCanvasNode = get_canvas_node
    getCanvasParent = get_canvas_parent

class PGSliderBar(PGItem):
    """This is a particular kind of PGItem that draws a little bar with a slider
    that moves from left to right indicating a value between the ranges.

    This is used as an implementation for both DirectSlider and for
    DirectScrollBar.
    """

    def __init__(self, name: str = ...) -> None: ...
    def upcast_to_PGItem(self) -> PGItem: ...
    def setup_scroll_bar(self, vertical: bool, length: float, width: float, bevel: float) -> None:
        """Creates PGSliderBar that represents a vertical or horizontal scroll bar (if
        vertical is true or false, respectively), with additional buttons for
        scrolling, and a range of 0 .. 1.

        length here is the measurement along the scroll bar, and width is the
        measurement across the scroll bar, whether it is vertical or horizontal (so
        for a horizontal scroll bar, the length is actually the x dimension, and
        the width is the y dimension).
        """
    def setup_slider(self, vertical: bool, length: float, width: float, bevel: float) -> None:
        """Creates PGSliderBar that represents a slider that the user can use to
        control an analog quantity.

        This is functionally the same as a scroll bar, but it has a distinctive
        look.
        """
    def set_axis(self, axis: Vec3Like) -> None:
        """Specifies the axis of the slider bar's motion.  This should be only one of
        four vectors: (1, 0, 0), (0, 0, 1), (-1, 0, 0), or (0, 0, -1).

        This specifies the vector in which the thumb moves when it is moving from
        the minimum to the maximum value.

        The axis must be parallel to one of the screen axes, and it must be
        normalized.  Hence, it may only be one of the above four possibilities;
        anything else is an error and will result in indeterminate behavior.

        Normally, you should not try to set the axis directly.
        """
    def get_axis(self) -> LVector3:
        """Returns the axis of the slider bar's motion.  See set_axis()."""
    def set_range(self, min_value: float, max_value: float) -> None:
        """Sets the minimum and maxmimum value for the slider."""
    def get_min_value(self) -> float:
        """Returns the value when the slider is all the way to the left."""
    def get_max_value(self) -> float:
        """Returns the value when the slider is all the way to the right."""
    def set_scroll_size(self, scroll_size: float) -> None:
        """Specifies the amount the slider will move when the user clicks on the left
        or right buttons.
        """
    def get_scroll_size(self) -> float:
        """Returns the value last set by set_scroll_size()."""
    def set_page_size(self, page_size: float) -> None:
        """Specifies the amount of data contained in a single page.  This indicates
        how much the thumb will jump when the trough is directly clicked; and if
        resize_thumb is true, it also controls the visible size of the thumb
        button.
        """
    def get_page_size(self) -> float:
        """Returns the value last set by set_page_size()."""
    def set_value(self, value: float) -> None:
        """Sets the current value of the slider programmatically.  This should range
        between get_min_value() and get_max_value().
        """
    def get_value(self) -> float:
        """Returns the current value of the slider."""
    def set_ratio(self, ratio: float) -> None:
        """Sets the current value of the slider, expressed in the range 0 .. 1."""
    def get_ratio(self) -> float:
        """Returns the current value of the slider, expressed in the range 0 .. 1."""
    def is_button_down(self) -> bool:
        """Returns true if the user is currently holding down the mouse button to
        manipulate the slider.  When true, calls to set_ratio() or set_value() will
        have no effect.
        """
    def set_resize_thumb(self, resize_thumb: bool) -> None:
        """Sets the resize_thumb flag.  When this is true, the thumb button's frame
        will be adjusted so that its width visually represents the page size.  When
        this is false, the thumb button will be left alone.
        """
    def get_resize_thumb(self) -> bool:
        """Returns the resize_thumb flag.  See set_resize_thumb()."""
    def set_manage_pieces(self, manage_pieces: bool) -> None:
        """Sets the manage_pieces flag.  When this is true, the sub-pieces of the
        slider bar--that is, the thumb, and the left and right scroll buttons--are
        automatically positioned and/or resized when the slider bar's overall frame
        is changed.
        """
    def get_manage_pieces(self) -> bool:
        """Returns the manage_pieces flag.  See set_manage_pieces()."""
    def set_thumb_button(self, thumb_button: PGButton) -> None:
        """Sets the PGButton object that will serve as the thumb for this slider.
        This button visually represents the position of the slider, and can be
        dragged left and right by the user.

        It is the responsibility of the caller to ensure that the button object is
        parented to the PGSliderBar node.
        """
    def clear_thumb_button(self) -> None:
        """Removes the thumb button object from control of the frame.  It is your
        responsibility to actually remove or hide the button itself.
        """
    def get_thumb_button(self) -> PGButton:
        """Returns the PGButton that serves as the thumb for this slider, or NULL if
        it is not set.
        """
    def set_left_button(self, left_button: PGButton) -> None:
        """Sets the PGButton object that will serve as the left scroll button for this
        slider.  This button is optional; if present, the user can click on it to
        move scroll_size units at a time to the left.

        It is the responsibility of the caller to ensure that the button object is
        parented to the PGSliderBar node.
        """
    def clear_left_button(self) -> None:
        """Removes the left button object from control of the frame.  It is your
        responsibility to actually remove or hide the button itself.
        """
    def get_left_button(self) -> PGButton:
        """Returns the PGButton that serves as the left scroll button for this slider,
        if any, or NULL if it is not set.
        """
    def set_right_button(self, right_button: PGButton) -> None:
        """Sets the PGButton object that will serve as the right scroll button for
        this slider.  This button is optional; if present, the user can click on it
        to move scroll_size units at a time to the right.

        It is the responsibility of the caller to ensure that the button object is
        parented to the PGSliderBar node.
        """
    def clear_right_button(self) -> None:
        """Removes the right button object from control of the frame.  It is your
        responsibility to actually remove or hide the button itself.
        """
    def get_right_button(self) -> PGButton:
        """Returns the PGButton that serves as the right scroll button for this
        slider, if any, or NULL if it is not set.
        """
    @staticmethod
    def get_adjust_prefix() -> str:
        """Returns the prefix that is used to define the adjust event for all
        PGSliderBars.  The adjust event is the concatenation of this string
        followed by get_id().
        """
    def get_adjust_event(self) -> str:
        """Returns the event name that will be thrown when the slider bar value is
        adjusted by the user or programmatically.
        """
    def remanage(self) -> None:
        """Manages the position and size of the scroll bars and the thumb.  Normally
        this should not need to be called directly.
        """
    def recompute(self) -> None:
        """Recomputes the position and size of the thumb.  Normally this should not
        need to be called directly.
        """
    upcastToPGItem = upcast_to_PGItem
    setupScrollBar = setup_scroll_bar
    setupSlider = setup_slider
    setAxis = set_axis
    getAxis = get_axis
    setRange = set_range
    getMinValue = get_min_value
    getMaxValue = get_max_value
    setScrollSize = set_scroll_size
    getScrollSize = get_scroll_size
    setPageSize = set_page_size
    getPageSize = get_page_size
    setValue = set_value
    getValue = get_value
    setRatio = set_ratio
    getRatio = get_ratio
    isButtonDown = is_button_down
    setResizeThumb = set_resize_thumb
    getResizeThumb = get_resize_thumb
    setManagePieces = set_manage_pieces
    getManagePieces = get_manage_pieces
    setThumbButton = set_thumb_button
    clearThumbButton = clear_thumb_button
    getThumbButton = get_thumb_button
    setLeftButton = set_left_button
    clearLeftButton = clear_left_button
    getLeftButton = get_left_button
    setRightButton = set_right_button
    clearRightButton = clear_right_button
    getRightButton = get_right_button
    getAdjustPrefix = get_adjust_prefix
    getAdjustEvent = get_adjust_event

class PGScrollFrame(PGVirtualFrame):
    """This is a special kind of frame that pretends to be much larger than it
    actually is.  You can scroll through the frame, as if you're looking
    through a window at the larger frame beneath.  All children of this frame
    node are scrolled and clipped as if they were children of the larger,
    virtual frame.

    This is implemented as a specialization of PGVirtualFrame, which handles
    the meat of the virtual canvas.  This class adds automatic support for
    scroll bars, and restricts the virtual transform to translate only (no
    scale or rotate).
    """

    def upcast_to_PGVirtualFrame(self) -> PGVirtualFrame: ...
    def setup(  # type: ignore[override]
        self, width: float, height: float, left: float, right: float, bottom: float, top: float, slider_width: float, bevel: float
    ) -> None:
        """Creates a PGScrollFrame with the indicated dimensions, and the indicated
        virtual frame.
        """
    @overload
    def set_virtual_frame(self, virtual_frame: Vec4Like) -> None:
        """Sets the bounding rectangle of the virtual frame.  This is the size of the
        large, virtual canvas which we can see only a portion of at any given time.
        """
    @overload
    def set_virtual_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_virtual_frame(self) -> LVecBase4:
        """Returns the bounding rectangle of the virtual frame.  See
        set_virtual_frame().  If has_virtual_frame() is false, this returns the
        item's clip frame.
        """
    def has_virtual_frame(self) -> bool:
        """Returns true if the virtual frame has a bounding rectangle; see
        set_virtual_frame().  Most PGScrollFrame objects will have a virtual frame.
        """
    def clear_virtual_frame(self) -> None:
        """Removes the virtual frame from the item.  This effectively sets the virtual
        frame to the same size as the clip frame.  Scrolling will no longer be
        possible.
        """
    def set_manage_pieces(self, manage_pieces: bool) -> None:
        """Sets the manage_pieces flag.  When this is true, the sub-pieces of the
        scroll frame--that is, the two scroll bars--are automatically positioned
        and/or resized when the scroll frame's overall frame is changed.  They are
        also automatically resized to fill in the gap when one or the other is
        hidden.
        """
    def get_manage_pieces(self) -> bool:
        """Returns the manage_pieces flag.  See set_manage_pieces()."""
    def set_auto_hide(self, auto_hide: bool) -> None:
        """Sets the auto_hide flag.  When this is true, the two scroll bars are
        automatically hidden if they are not needed (that is, if the virtual frame
        would fit within the clip frame without them), and they are automatically
        shown when they are needed.

        Setting this flag true forces the manage_pieces flag to also be set true.
        """
    def get_auto_hide(self) -> bool:
        """Returns the auto_hide flag.  See set_auto_hide()."""
    def set_horizontal_slider(self, horizontal_slider: PGSliderBar) -> None:
        """Sets the PGSliderBar object that will serve as the horizontal scroll bar
        for this frame.  It is your responsibility to parent this slider bar to the
        frame and move it to the appropriate place.
        """
    def clear_horizontal_slider(self) -> None:
        """Removes the horizontal scroll bar from control of the frame.  It is your
        responsibility to actually remove or hide the object itself.
        """
    def get_horizontal_slider(self) -> PGSliderBar:
        """Returns the PGSliderBar that serves as the horizontal scroll bar for this
        frame, if any, or NULL if it is not set.
        """
    def set_vertical_slider(self, vertical_slider: PGSliderBar) -> None:
        """Sets the PGSliderBar object that will serve as the vertical scroll bar for
        this frame.  It is your responsibility to parent this slider bar to the
        frame and move it to the appropriate place.
        """
    def clear_vertical_slider(self) -> None:
        """Removes the vertical scroll bar from control of the frame.  It is your
        responsibility to actually remove or hide the object itself.
        """
    def get_vertical_slider(self) -> PGSliderBar:
        """Returns the PGSliderBar that serves as the vertical scroll bar for this
        frame, if any, or NULL if it is not set.
        """
    def remanage(self) -> None:
        """Manages the position and size of the scroll bars.  Normally this should not
        need to be called directly.
        """
    def recompute(self) -> None:
        """Forces the PGScrollFrame to recompute itself right now.  Normally this
        should not be required.
        """
    upcastToPGVirtualFrame = upcast_to_PGVirtualFrame
    setVirtualFrame = set_virtual_frame
    getVirtualFrame = get_virtual_frame
    hasVirtualFrame = has_virtual_frame
    clearVirtualFrame = clear_virtual_frame
    setManagePieces = set_manage_pieces
    getManagePieces = get_manage_pieces
    setAutoHide = set_auto_hide
    getAutoHide = get_auto_hide
    setHorizontalSlider = set_horizontal_slider
    clearHorizontalSlider = clear_horizontal_slider
    getHorizontalSlider = get_horizontal_slider
    setVerticalSlider = set_vertical_slider
    clearVerticalSlider = clear_vertical_slider
    getVerticalSlider = get_vertical_slider

class PGWaitBar(PGItem):
    """This is a particular kind of PGItem that draws a little bar that fills from
    left to right to indicate a slow process gradually completing, like a
    traditional "wait, loading" bar.
    """

    def __init__(self, name: str = ...) -> None: ...
    def setup(self, width: float, height: float, range: float) -> None:
        """Creates a PGWaitBar with the indicated dimensions, with the indicated
        maximum range.
        """
    def set_range(self, range: float) -> None:
        """Sets the value at which the WaitBar indicates 100%."""
    def get_range(self) -> float:
        """Returns the value at which the WaitBar indicates 100%."""
    def set_value(self, value: float) -> None:
        """Sets the current value of the bar.  This should range between 0 and
        get_range().
        """
    def get_value(self) -> float:
        """Returns the current value of the bar."""
    def get_percent(self) -> float:
        """Returns the percentage complete."""
    def set_bar_style(self, style: PGFrameStyle) -> None:
        """Sets the kind of frame that is drawn on top of the WaitBar to represent the
        amount completed.
        """
    def get_bar_style(self) -> PGFrameStyle:
        """Returns the kind of frame that is drawn on top of the WaitBar to represent
        the amount completed.
        """
    setRange = set_range
    getRange = get_range
    setValue = set_value
    getValue = get_value
    getPercent = get_percent
    setBarStyle = set_bar_style
    getBarStyle = get_bar_style
