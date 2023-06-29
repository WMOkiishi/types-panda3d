from collections.abc import Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import Mat4Like, Vec2Like, Vec3Like, Vec4Like
from panda3d.core._dgraph import DataNode
from panda3d.core._display import DisplayRegion
from panda3d.core._dtoolbase import TypeHandle
from panda3d.core._dtoolutil import ostream
from panda3d.core._event import EventHandler, EventParameter, PointerEventList
from panda3d.core._express import Namable, ReferenceCount, TypedReferenceCount
from panda3d.core._linmath import LMatrix4, LPoint2, LPoint3, LVecBase3, LVecBase4
from panda3d.core._pgraph import GeomNode, NodePath, PandaNode
from panda3d.core._putil import ButtonHandle, ModifierButtons, TypedWritableReferenceCount

_TextEncoder_Encoding: TypeAlias = Literal[0, 1, 2, 2]
_Trackball_ControlMode: TypeAlias = Literal[0, 1, 2, 3, 4]
_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]

class ButtonThrower(DataNode):
    """Throws Panda Events for button down/up events generated within the data
    graph.

    This is a DataNode which is intended to be parented to the data graph below
    a device which is generating a sequence of button events, like a
    MouseAndKeyboard device.  It simply takes each button it finds and throws a
    corresponding event based on the button name via the throw_event() call.
    """

    button_down_event: str
    button_up_event: str
    button_repeat_event: str
    keystroke_event: str
    candidate_event: str
    move_event: str
    raw_button_down_event: str
    raw_button_up_event: str
    prefix: str
    specific_flag: bool
    time_flag: bool
    modifier_buttons: ModifierButtons
    throw_buttons_active: bool
    @property
    def parameters(self) -> Sequence[EventParameter]: ...
    @overload
    def __init__(self, __param0: ButtonThrower) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_button_down_event(self, button_down_event: str) -> None:
        """Specifies the generic event that is generated (if any) each time a key or
        button is depressed.  Unlike the specific events that are unique to each
        key, this same event name is used for *all* button events, and the name of
        the button pressed (possibly with modifier prefixes) will be sent as a
        parameter.

        If this string is empty, no event is generated.  It is possible to generate
        both generic events and specific events for the same button.

        See also set_keystroke_event().
        """
    def get_button_down_event(self) -> str:
        """Returns the button_down_event that has been set on this ButtonThrower.  See
        set_button_down_event().
        """
    def set_button_up_event(self, button_up_event: str) -> None:
        """Specifies the generic event that is generated (if any) each time a key or
        button is released.  See set_button_down_event().
        """
    def get_button_up_event(self) -> str:
        """Returns the button_up_event that has been set on this ButtonThrower.  See
        set_button_up_event().
        """
    def set_button_repeat_event(self, button_repeat_event: str) -> None:
        """Specifies the generic event that is generated (if any) repeatedly while a
        key or button is held down.  Unlike the specific events that are unique to
        each key, this same event name is used for *all* button events, and the
        name of the button pressed (possibly with modifier prefixes) will be sent
        as a parameter.

        If this string is empty, no event is generated.  It is possible to generate
        both generic events and specific events for the same button.

        See also set_keystroke_event().
        """
    def get_button_repeat_event(self) -> str:
        """Returns the button_repeat_event that has been set on this ButtonThrower.
        See set_button_repeat_event().
        """
    def set_keystroke_event(self, keystroke_event: str) -> None:
        """Specifies the event that is generated (if any) for each keystroke that is
        received.  A keystroke is different than a button event: it represents the
        semantic meaning of the sequence of keys that have been pressed.  For
        instance, pressing shift and 4 together will generate the button event
        "shift-4", but it will generate the keystroke "$".

        If a key is held down, keyrepeat will cause the same keystroke event to be
        generated repeatedly.  This is different from the corresponding down event,
        which will only be generated once, followed by a number of button repeat
        events.

        This event is generated with a single wstring parameter, which is a one-
        character string that contains the keystroke generated.  If this event
        string is empty, no event is generated.

        See also set_button_down_event().
        """
    def get_keystroke_event(self) -> str:
        """Returns the keystroke_event that has been set on this ButtonThrower.  See
        set_keystroke_event().
        """
    def set_candidate_event(self, candidate_event: str) -> None:
        """Specifies the event that is generated (if any) for each IME candidate
        string event received.  Events of this nature are received only when the
        user is entering data using a Microsoft Input Method Editor, typically used
        for Asian languages such as Japanese or Korean.

        If you are designing a typing user interface, you should track this event
        to support the use of the IME.  In response to this event, you should
        display the candidate string in the entry box, with the appropriate
        sections highlighted, so the user can scroll through the available choices.

        This event is generated with four parameters, in order: the candidate
        string, the character at which to start the highlight, the character at
        which to end the highlight, and the current cursor position.
        """
    def get_candidate_event(self) -> str:
        """Returns the candidate_event that has been set on this ButtonThrower.  See
        set_candidate_event().
        """
    def set_move_event(self, move_event: str) -> None:
        """Specifies the event that is generated (if any) each time the mouse is moved
        within the window.
        """
    def get_move_event(self) -> str:
        """Returns the move_event that has been set on this ButtonThrower.  See
        set_move_event().
        """
    def set_raw_button_down_event(self, raw_button_down_event: str) -> None:
        """Like set_button_down_event, but uses the raw, untransformed scan key from
        the operating system.  This uses buttons that are independent of the user's
        selected keyboard layout.
        """
    def get_raw_button_down_event(self) -> str:
        """Returns the raw_button_down_event that has been set on this ButtonThrower.
        See set_raw_button_down_event().
        """
    def set_raw_button_up_event(self, raw_button_up_event: str) -> None:
        """Specifies the generic event that is generated (if any) each time a key or
        button is released.  See set_raw_button_down_event().
        """
    def get_raw_button_up_event(self) -> str:
        """Returns the raw_button_up_event that has been set on this ButtonThrower.
        See set_raw_button_up_event().
        """
    def set_prefix(self, prefix: str) -> None:
        """Sets the prefix which is prepended to all specific event names (that is,
        event names generated from the button name itself, as opposed to the
        generic event names like set_button_down_event) thrown by this object.
        """
    def get_prefix(self) -> str:
        """Returns the prefix that has been set on this ButtonThrower.  See
        set_prefix().
        """
    def set_specific_flag(self, specific_flag: bool) -> None:
        """Sets the flag that indicates whether specific events (events prefixed by
        set_prefix, and based on the event name) should be generated at all.  This
        is true by default, but may be disabled if you are only interested in the
        generic events (for instance, events like set_button_down_event).
        """
    def get_specific_flag(self) -> bool:
        """Returns the flag that indicates whether specific events should be
        generated.  See set_specific_flag().
        """
    def set_time_flag(self, time_flag: bool) -> None:
        """Sets the flag that indicates whether the time of the button event should be
        passed as a parameter or not.  When this is true, an additional parameter
        is generated on each event (before all the parameters named by
        add_parameter) that consists of a single double value, and reflects the
        time the button was pressed or released, as a value from
        ClockObject::get_global_clock().
        """
    def get_time_flag(self) -> bool:
        """Returns the flag that indicates whether the time of the button event should
        be passed as a parameter.
        """
    def add_parameter(self, obj: EventParameter | TypedReferenceCount | TypedWritableReferenceCount | float | str | None) -> None:
        """Adds the indicated parameter to the list of parameters that will be passed
        with each event generated by this ButtonThrower.
        """
    def get_num_parameters(self) -> int:
        """Returns the number of parameters that have been added to the list of
        parameters to be passed with each event generated by this ButtonThrower.
        """
    def get_parameter(self, n: int) -> EventParameter:
        """Returns the nth parameter that has been added to the list of parameters
        passed with each event generated by this ButtonThrower.
        """
    def get_modifier_buttons(self) -> ModifierButtons:
        """Returns the set of ModifierButtons that the ButtonThrower will consider
        important enough to prepend the event name with.  Normally, this set will
        be empty, and the ButtonThrower will therefore ignore all ModifierButtons
        attached to the key events, but if one or more buttons have been added to
        this set, and those modifier buttons are set on the button event, then the
        event name will be prepended with the names of the modifier buttons.
        """
    def set_modifier_buttons(self, mods: ModifierButtons) -> None:
        """Changes the set of ModifierButtons that the ButtonThrower will consider
        important enough to prepend the event name with.  Normally, this set will
        be empty, and the ButtonThrower will therefore ignore all ModifierButtons
        attached to the key events, but if one or more buttons have been added to
        this set, then the event name will be prepended with the names of the
        modifier buttons.

        It is recommended that you change this setting by first calling
        get_modifier_buttons(), making adjustments, and passing the new value to
        set_modifier_buttons().  This way the current state of the modifier buttons
        will not be lost.
        """
    def set_throw_buttons_active(self, flag: bool) -> None:
        """Sets the flag that indicates whether the ButtonThrower will only process
        events for the explicitly named buttons or not.  Normally this is false,
        meaning all buttons are processed; set it true to indicate that only some
        buttons should be processed.  See add_throw_button().
        """
    def get_throw_buttons_active(self) -> bool:
        """Returns the flag that indicates whether the ButtonThrower will only process
        events for the explicitly named buttons or not.  See
        set_throw_buttons_active().
        """
    def add_throw_button(self, mods: ModifierButtons, button: ButtonHandle | str) -> bool:
        """Adds a new button to the set of buttons that the ButtonThrower explicitly
        processes.

        If set_throw_buttons_active is false (which is the default), the
        ButtonThrower will process all buttons.  Otherwise, the ButtonThrower will
        only process events for the button(s) explicitly named by this function;
        buttons not on the list will be ignored by this object and passed on
        downstream to the child node(s) in the data graph.  A button that *is* on
        the list will be processed by the ButtonThrower and not passed on to the
        child node(s).

        The return value is true if the button is added, or false if it was already
        in the set.
        """
    def remove_throw_button(self, mods: ModifierButtons, button: ButtonHandle | str) -> bool:
        """Removes the indicated button from the set of buttons that the ButtonThrower
        explicitly processes.  See add_throw_button().

        The return value is true if the button is removed, or false if it was not
        on the set.
        """
    @overload
    def has_throw_button(self, button: ButtonHandle | str) -> bool:
        """`(self, button: ButtonHandle)`:
        Returns true if the indicated button, in conjunction with any nonspecified
        modifier buttons, is on the set of buttons that will be processed by the
        ButtonThrower.  That is to say, returns true if this button was ever passed
        as the second parameter add_throw_button(), regardless of what the first
        parameter was.

        `(self, mods: ModifierButtons, button: ButtonHandle)`:
        Returns true if the indicated button is on the set of buttons that will be
        processed by the ButtonThrower, false otherwise.  See add_throw_button().
        """
    @overload
    def has_throw_button(self, mods: ModifierButtons, button: ButtonHandle | str) -> bool: ...
    def clear_throw_buttons(self) -> None:
        """Empties the set of buttons that were added via add_throw_button().  See
        add_throw_button().
        """
    def get_parameters(self) -> tuple[EventParameter, ...]: ...
    setButtonDownEvent = set_button_down_event
    getButtonDownEvent = get_button_down_event
    setButtonUpEvent = set_button_up_event
    getButtonUpEvent = get_button_up_event
    setButtonRepeatEvent = set_button_repeat_event
    getButtonRepeatEvent = get_button_repeat_event
    setKeystrokeEvent = set_keystroke_event
    getKeystrokeEvent = get_keystroke_event
    setCandidateEvent = set_candidate_event
    getCandidateEvent = get_candidate_event
    setMoveEvent = set_move_event
    getMoveEvent = get_move_event
    setRawButtonDownEvent = set_raw_button_down_event
    getRawButtonDownEvent = get_raw_button_down_event
    setRawButtonUpEvent = set_raw_button_up_event
    getRawButtonUpEvent = get_raw_button_up_event
    setPrefix = set_prefix
    getPrefix = get_prefix
    setSpecificFlag = set_specific_flag
    getSpecificFlag = get_specific_flag
    setTimeFlag = set_time_flag
    getTimeFlag = get_time_flag
    addParameter = add_parameter
    getNumParameters = get_num_parameters
    getParameter = get_parameter
    getModifierButtons = get_modifier_buttons
    setModifierButtons = set_modifier_buttons
    setThrowButtonsActive = set_throw_buttons_active
    getThrowButtonsActive = get_throw_buttons_active
    addThrowButton = add_throw_button
    removeThrowButton = remove_throw_button
    hasThrowButton = has_throw_button
    clearThrowButtons = clear_throw_buttons
    getParameters = get_parameters

class MouseInterfaceNode(DataNode):
    """This is the base class for some classes that monitor the mouse and keyboard
    input and perform some action due to their state.

    It collects together some common interface; in particular, the
    require_button() and related methods.
    """

    def __init__(self, __param0: MouseInterfaceNode) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def require_button(self, button: ButtonHandle | str, is_down: bool) -> None:
        """Indicates that the indicated button must be in the required state (either
        up or down) in order for this particular MouseInterfaceNode to do anything.
        For instance, this may be called to make a Trackball object respect mouse
        input only when the control key is held down.
        """
    def clear_button(self, button: ButtonHandle | str) -> None:
        """Removes any requirement on the indicated button set by an earlier call to
        require_button().
        """
    def clear_all_buttons(self) -> None:
        """Removes all requirements on buttons set by an earlier call to
        require_button().
        """
    requireButton = require_button
    clearButton = clear_button
    clearAllButtons = clear_all_buttons

class DriveInterface(MouseInterfaceNode):
    """This is a TFormer, similar to Trackball, that moves around a transform
    matrix in response to mouse input.  The basic motion is on a horizontal
    plane, as if driving a vehicle.
    """

    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, __param0: DriveInterface) -> None: ...
    def set_forward_speed(self, speed: float) -> None:
        """Sets the speed of full forward motion, when the mouse is at the very top of
        the window.  This is in units (e.g.  feet) per second.
        """
    def get_forward_speed(self) -> float:
        """Returns the speed of full forward motion, when the mouse is at the very top
        of the window.  This is in units (e.g.  feet) per second.
        """
    def set_reverse_speed(self, speed: float) -> None:
        """Sets the speed of full reverse motion, when the mouse is at the very bottom
        of the window.  This is in units (e.g.  feet) per second.
        """
    def get_reverse_speed(self) -> float:
        """Returns the speed of full reverse motion, when the mouse is at the very
        bottom of the window.  This is in units (e.g.  feet) per second.
        """
    def set_rotate_speed(self, speed: float) -> None:
        """Sets the maximum rate at which the user can rotate left or right, when the
        mouse is at the very edge of the window.  This is in degrees per second.
        """
    def get_rotate_speed(self) -> float:
        """Returns the maximum rate at which the user can rotate left or right, when
        the mouse is at the very edge of the window.  This is in degrees per
        second.
        """
    def set_vertical_dead_zone(self, zone: float) -> None:
        """Sets the size of the horizontal bar in the center of the screen that
        represents the "dead zone" of vertical motion: the region in which the
        mouse does not report vertical motion.  This is in a fraction of the window
        height, so 0.5 will set a dead zone as large as half the screen.
        """
    def get_vertical_dead_zone(self) -> float:
        """Returns the size of the horizontal bar in the center of the screen that
        represents the "dead zone" of vertical motion: the region in which the
        mouse does not report vertical motion.  This is in a fraction of the window
        height, so 0.5 will set a dead zone as large as half the screen.
        """
    def set_horizontal_dead_zone(self, zone: float) -> None:
        """Sets the size of the vertical bar in the center of the screen that
        represents the "dead zone" of horizontal motion: the region in which the
        mouse does not report horizontal motion.  This is in a fraction of the
        window width, so 0.5 will set a dead zone as large as half the screen.
        """
    def get_horizontal_dead_zone(self) -> float:
        """Returns the size of the vertical bar in the center of the screen that
        represents the "dead zone" of horizontal motion: the region in which the
        mouse does not report horizontal motion.  This is in a fraction of the
        window width, so 0.5 will set a dead zone as large as half the screen.
        """
    def set_vertical_ramp_up_time(self, ramp_up_time: float) -> None:
        """Sets the amount of time, in seconds, it takes between the time an up or
        down arrow key is pressed and the time it registers full forward or
        backward motion.
        """
    def get_vertical_ramp_up_time(self) -> float:
        """Returns the amount of time, in seconds, it takes between the time an up or
        down arrow key is pressed and the time it registers full forward or
        backward motion.
        """
    def set_vertical_ramp_down_time(self, ramp_down_time: float) -> None:
        """Sets the amount of time, in seconds, it takes between the time an up or
        down arrow key is released and the time it registers no motion.
        """
    def get_vertical_ramp_down_time(self) -> float:
        """Returns the amount of time, in seconds, it takes between the time an up or
        down arrow key is released and the time it registers no motion.
        """
    def set_horizontal_ramp_up_time(self, ramp_up_time: float) -> None:
        """Sets the amount of time, in seconds, it takes between the time a left or
        right arrow key is pressed and the time it registers full rotation.
        """
    def get_horizontal_ramp_up_time(self) -> float:
        """Returns the amount of time, in seconds, it takes between the time a left or
        right arrow key is pressed and the time it registers full rotation.
        """
    def set_horizontal_ramp_down_time(self, ramp_down_time: float) -> None:
        """Sets the amount of time, in seconds, it takes between the time a left or
        right arrow key is released and the time it registers no motion.
        """
    def get_horizontal_ramp_down_time(self) -> float:
        """Returns the amount of time, in seconds, it takes between the time a left or
        right arrow key is released and the time it registers no motion.
        """
    def get_speed(self) -> float:
        """Returns the speed of the previous update in units/sec"""
    def get_rot_speed(self) -> float:
        """Returns the rot_speed of the previous update in units/sec"""
    def reset(self) -> None:
        """Reinitializes the driver to the origin and resets any knowledge about
        buttons being held down.
        """
    def get_pos(self) -> LPoint3:
        """Returns the driver's position."""
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def get_z(self) -> float: ...
    @overload
    def set_pos(self, vec: Vec3Like) -> None:
        """Directly sets the driver's position."""
    @overload
    def set_pos(self, x: float, y: float, z: float) -> None: ...
    def set_x(self, x: float) -> None: ...
    def set_y(self, y: float) -> None: ...
    def set_z(self, z: float) -> None: ...
    def get_hpr(self) -> LVecBase3:
        """Returns the driver's orientation."""
    def get_h(self) -> float: ...
    def get_p(self) -> float: ...
    def get_r(self) -> float: ...
    @overload
    def set_hpr(self, hpr: Vec3Like) -> None:
        """Directly sets the driver's orientation."""
    @overload
    def set_hpr(self, h: float, p: float, r: float) -> None: ...
    def set_h(self, h: float) -> None: ...
    def set_p(self, p: float) -> None: ...
    def set_r(self, r: float) -> None: ...
    def set_force_roll(self, force_roll: float) -> None:
        """This function is no longer used and does nothing.  It will be removed soon."""
    def set_ignore_mouse(self, ignore_mouse: bool) -> None:
        """Changes the state of the ignore_mouse flag.  If this flag is true, the
        DriveInterface will ignore mouse down button events (but still recognize
        mouse up button events); the user will not be able to start the
        DriveInterface going again if it is stopped, but if the user is currently
        holding down a mouse button it will not stop immediately until the user
        eventually releases the button.
        """
    def get_ignore_mouse(self) -> bool:
        """Returns the current setting of the ignore_mouse flag.  See
        set_ignore_mouse().
        """
    def set_force_mouse(self, force_mouse: bool) -> None:
        """Changes the state of the force_mouse flag.  If this flag is true, the mouse
        button need not be held down in order to drive the avatar around.
        """
    def get_force_mouse(self) -> bool:
        """Returns the current setting of the force_mouse flag.  See
        set_force_mouse().
        """
    def set_stop_this_frame(self, stop_this_frame: bool) -> None:
        """If stop_this_frame is true, the next time the frame is computed no motion
        will be allowed, and then the flag is reset to false.  This can be used to
        prevent too much movement when we know a long time has artificially
        elapsed, for instance when we take a screenshot, without munging the clock
        for everything else.
        """
    def get_stop_this_frame(self) -> bool:
        """Returns the current setting of the stop_this_frame flag.  See
        set_stop_this_frame().
        """
    def set_mat(self, mat: Mat4Like) -> None:
        """Stores the indicated transform in the DriveInterface."""
    def get_mat(self) -> LMatrix4:
        """Returns the current transform."""
    def force_dgraph(self) -> None:
        """This is a special kludge for DriveInterface to allow us to avoid the one-
        frame latency after a collision.  It forces an immediate partial data flow
        for all data graph nodes below this node, causing all data nodes that
        depend on this matrix to be updated immediately.
        """
    setForwardSpeed = set_forward_speed
    getForwardSpeed = get_forward_speed
    setReverseSpeed = set_reverse_speed
    getReverseSpeed = get_reverse_speed
    setRotateSpeed = set_rotate_speed
    getRotateSpeed = get_rotate_speed
    setVerticalDeadZone = set_vertical_dead_zone
    getVerticalDeadZone = get_vertical_dead_zone
    setHorizontalDeadZone = set_horizontal_dead_zone
    getHorizontalDeadZone = get_horizontal_dead_zone
    setVerticalRampUpTime = set_vertical_ramp_up_time
    getVerticalRampUpTime = get_vertical_ramp_up_time
    setVerticalRampDownTime = set_vertical_ramp_down_time
    getVerticalRampDownTime = get_vertical_ramp_down_time
    setHorizontalRampUpTime = set_horizontal_ramp_up_time
    getHorizontalRampUpTime = get_horizontal_ramp_up_time
    setHorizontalRampDownTime = set_horizontal_ramp_down_time
    getHorizontalRampDownTime = get_horizontal_ramp_down_time
    getSpeed = get_speed
    getRotSpeed = get_rot_speed
    getPos = get_pos
    getX = get_x
    getY = get_y
    getZ = get_z
    setPos = set_pos
    setX = set_x
    setY = set_y
    setZ = set_z
    getHpr = get_hpr
    getH = get_h
    getP = get_p
    getR = get_r
    setHpr = set_hpr
    setH = set_h
    setP = set_p
    setR = set_r
    setForceRoll = set_force_roll
    setIgnoreMouse = set_ignore_mouse
    getIgnoreMouse = get_ignore_mouse
    setForceMouse = set_force_mouse
    getForceMouse = get_force_mouse
    setStopThisFrame = set_stop_this_frame
    getStopThisFrame = get_stop_this_frame
    setMat = set_mat
    getMat = get_mat
    forceDgraph = force_dgraph

class MouseSubregion(MouseInterfaceNode):
    """The MouseSubregion object scales the mouse inputs from within a rectangular
    region of the screen, as if they were the full-screen inputs.

    If you choose your MouseSubregion coordinates to exactly match a
    DisplayRegion within your window, you end up with a virtual mouse within
    your DisplayRegion.
    """

    @overload
    def __init__(self, __param0: MouseSubregion) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def get_left(self) -> float:
        """Retrieves the x coordinate of the left edge of the rectangle within the
        window.  This number will be in the range [0..1].
        """
    def get_right(self) -> float:
        """Retrieves the x coordinate of the right edge of the rectangle within the
        window.  This number will be in the range [0..1].
        """
    def get_bottom(self) -> float:
        """Retrieves the y coordinate of the bottom edge of the rectangle within the
        window.  This number will be in the range [0..1].
        """
    def get_top(self) -> float:
        """Retrieves the y coordinate of the top edge of the rectangle within the
        window.  This number will be in the range [0..1].
        """
    def set_dimensions(self, l: float, r: float, b: float, t: float) -> None:
        """Changes the region of the window in which the mouse is considered to be
        active.  The parameters are identical to those for a DisplayRegion: they
        range from 0 to 1, where 0,0 is the lower left corner and 1,1 is the upper
        right; (0, 1, 0, 1) represents the whole window.
        """
    getLeft = get_left
    getRight = get_right
    getBottom = get_bottom
    getTop = get_top
    setDimensions = set_dimensions

class MouseWatcherRegion(TypedWritableReferenceCount, Namable):
    """This is the class that defines a rectangular region on the screen for the
    MouseWatcher.
    """

    SF_mouse_button: Final = 1
    SFMouseButton: Final = 1
    SF_other_button: Final = 2
    SFOtherButton: Final = 2
    SF_any_button: Final = 3
    SFAnyButton: Final = 3
    SF_mouse_position: Final = 4
    SFMousePosition: Final = 4
    frame: LVecBase4
    sort: int
    active: bool
    keyboard: bool
    suppress_flags: int
    @property
    def area(self) -> float: ...
    @overload
    def __init__(self, __param0: MouseWatcherRegion) -> None: ...
    @overload
    def __init__(self, name: str, frame: Vec4Like) -> None: ...
    @overload
    def __init__(self, name: str, left: float, right: float, bottom: float, top: float) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    @overload
    def set_frame(self, frame: Vec4Like) -> None: ...
    @overload
    def set_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_frame(self) -> LVecBase4: ...
    def get_area(self) -> float:
        """Returns the area of the rectangular region."""
    def set_sort(self, sort: int) -> None:
        """Changes the sorting order of this particular region.  The sorting order is
        used to resolve conflicts in the case of overlapping region; the region
        with the highest sort value will be preferred, and between regions of the
        same sort value, the smallest region will be preferred.  The default
        sorting order, if none is explicitly specified, is 0.
        """
    def get_sort(self) -> int:
        """Returns the current sorting order of this region.  See set_sort()."""
    def set_active(self, active: bool) -> None:
        """Sets whether the region is active or not.  If it is not active, the
        MouseWatcher will never consider the mouse to be over the region.  The
        region might still receive keypress events if its set_keyboard() flag is
        true.
        """
    def get_active(self) -> bool:
        """Returns whether the region is active or not.  See set_active()."""
    def set_keyboard(self, keyboard: bool) -> None:
        """Sets whether the region is interested in global keyboard events.  If this
        is true, then any keyboard button events will be passed to press() and
        release() regardless of the position of the mouse onscreen; otherwise,
        these events will only be passed if the mouse is over the region.
        """
    def get_keyboard(self) -> bool:
        """Returns whether the region is interested in global keyboard events; see
        set_keyboard().
        """
    def set_suppress_flags(self, suppress_flags: int) -> None:
        """Sets which events are suppressed when the mouse is over the region.  This
        is the union of zero or more various SF_* values.  Normally, this is 0,
        indicating that no events are suppressed.

        If you set this to a non-zero value, for instance SF_mouse_position, then
        the mouse position will not be sent along the data graph when the mouse is
        over this particular region.
        """
    def get_suppress_flags(self) -> int:
        """Returns the current suppress_flags.  See set_suppress_flags()."""
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToNamable = upcast_to_Namable
    setFrame = set_frame
    getFrame = get_frame
    getArea = get_area
    setSort = set_sort
    getSort = get_sort
    setActive = set_active
    getActive = get_active
    setKeyboard = set_keyboard
    getKeyboard = get_keyboard
    setSuppressFlags = set_suppress_flags
    getSuppressFlags = get_suppress_flags

class MouseWatcherBase:
    """This represents a collection of MouseWatcherRegions that may be managed as
    a group.  This is the base class for both MouseWatcherGroup and
    MouseWatcher, and exists so that we don't have to make MouseWatcher inherit
    from ReferenceCount more than once.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def sorted(self) -> bool: ...
    @property
    def regions(self) -> Sequence[MouseWatcherRegion]: ...
    def add_region(self, region: MouseWatcherRegion) -> None:
        """Adds the indicated region to the set of regions in the group.  It is no
        longer an error to call this for the same region more than once.
        """
    def has_region(self, region: MouseWatcherRegion) -> bool:
        """Returns true if the indicated region has already been added to the
        MouseWatcherBase, false otherwise.
        """
    def remove_region(self, region: MouseWatcherRegion) -> bool:
        """Removes the indicated region from the group.  Returns true if it was
        successfully removed, or false if it wasn't there in the first place.
        """
    def find_region(self, name: str) -> MouseWatcherRegion:
        """Returns a pointer to the first region found with the indicated name.  If
        multiple regions share the same name, the one that is returned is
        indeterminate.
        """
    def clear_regions(self) -> None:
        """Removes all the regions from the group."""
    def sort_regions(self) -> None:
        """Sorts all the regions in this group into pointer order."""
    def is_sorted(self) -> bool:
        """Returns true if the group has already been sorted, false otherwise."""
    def get_num_regions(self) -> int:
        """Returns the number of regions in the group."""
    def get_region(self, n: int) -> MouseWatcherRegion:
        """Returns the nth region of the group; returns NULL if there is no nth
        region.  Note that this is not thread-safe; another thread might have
        removed the nth region before you called this method.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def show_regions(self, render2d: NodePath, bin_name: str, draw_order: int) -> None:
        """Enables the visualization of all of the regions handled by this
        MouseWatcherBase.  The supplied NodePath should be the root of the 2-d
        scene graph for the window.
        """
    def set_color(self, color: Vec4Like) -> None:
        """Specifies the color used to draw the region rectangles for the regions
        visualized by show_regions().
        """
    def hide_regions(self) -> None:
        """Stops the visualization created by a previous call to show_regions()."""
    def update_regions(self) -> None:
        """Refreshes the visualization created by show_regions()."""
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_regions(self) -> tuple[MouseWatcherRegion, ...]: ...
    addRegion = add_region
    hasRegion = has_region
    removeRegion = remove_region
    findRegion = find_region
    clearRegions = clear_regions
    sortRegions = sort_regions
    isSorted = is_sorted
    getNumRegions = get_num_regions
    getRegion = get_region
    showRegions = show_regions
    setColor = set_color
    hideRegions = hide_regions
    updateRegions = update_regions
    getClassType = get_class_type
    getRegions = get_regions

class MouseWatcherGroup(MouseWatcherBase, ReferenceCount):
    """This represents a collection of MouseWatcherRegions that may be managed as
    a group.  The implementation for this is in MouseWatcherBase; this class
    exists so that we can inherit from ReferenceCount.
    """

    def upcast_to_MouseWatcherBase(self) -> MouseWatcherBase: ...
    def upcast_to_ReferenceCount(self) -> ReferenceCount: ...
    upcastToMouseWatcherBase = upcast_to_MouseWatcherBase
    upcastToReferenceCount = upcast_to_ReferenceCount

class MouseWatcher(DataNode, MouseWatcherBase):  # type: ignore[misc]
    """This TFormer maintains a list of rectangular regions on the screen that are
    considered special mouse regions; typically these will be click buttons.
    When the mouse passes in or out of one of these regions, or when a button
    is clicked while the mouse is in one of these regions, an event is thrown.

    Mouse events may also be suppressed from the rest of the datagraph in these
    special regions.

    This class can also implement a software mouse pointer by automatically
    generating a transform to apply to a piece of geometry placed under the 2-d
    scene graph.  It will move the geometry around according to the mouse's
    known position.

    Finally, this class can keep a record of the mouse trail.  This is useful
    if you want to know, not just where the mouse is, but the exact sequence of
    movements it took to get there.  This information is mainly useful for
    gesture-recognition code.  To use trail logging, you need to enable the
    generation of pointer events in the GraphicsWindowInputDevice and set the
    trail log duration in the MouseWatcher.  Otherwise, the trail log will be
    empty.
    """

    def __init__(self, name: str = ...) -> None: ...
    def upcast_to_DataNode(self) -> DataNode: ...
    def upcast_to_MouseWatcherBase(self) -> MouseWatcherBase: ...
    def has_mouse(self) -> bool:
        """Returns true if the mouse is anywhere within the window, false otherwise.
        Also see is_mouse_open().
        """
    def is_mouse_open(self) -> bool:
        """Returns true if the mouse is within the window and not over some particular
        MouseWatcherRegion that is marked to suppress mouse events; that is, that
        the mouse is in open space within the window.
        """
    def get_mouse(self) -> LPoint2:
        """It is only valid to call this if has_mouse() returns true.  If so, this
        returns the current position of the mouse within the window.
        """
    def get_mouse_x(self) -> float:
        """It is only valid to call this if has_mouse() returns true.  If so, this
        returns the current X position of the mouse within the window.
        """
    def get_mouse_y(self) -> float:
        """It is only valid to call this if has_mouse() returns true.  If so, this
        returns the current Y position of the mouse within the window.
        """
    @overload
    def set_frame(self, frame: Vec4Like) -> None:
        """`(self, frame: LVecBase4)`:
        Sets the frame of the MouseWatcher.  This determines the coordinate space
        in which the MouseWatcherRegions should be expected to live.  Normally,
        this is left at -1, 1, -1, 1, which is the default setting, and matches the
        mouse coordinate range.

        Whatever values you specify here indicate the shape of the full screen, and
        the MouseWatcherRegions will be given in coordinate space matching it.  For
        instance, if you specify (0, 1, 0, 1), then a MouseWatcherRegion with the
        frame (0, 1, 0, .5) will cover the lower half of the screen.

        `(self, left: float, right: float, bottom: float, top: float)`:
        Sets the frame of the MouseWatcher.  See the next flavor of this method for
        a more verbose explanation.
        """
    @overload
    def set_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_frame(self) -> LVecBase4:
        """Returns the frame of the MouseWatcher.  See set_frame()."""
    @overload
    def is_over_region(self, pos: Vec2Like = ...) -> bool:
        """Returns true if the mouse is over any rectangular region, false otherwise."""
    @overload
    def is_over_region(self, x: float, y: float) -> bool: ...
    @overload
    def get_over_region(self, pos: Vec2Like = ...) -> MouseWatcherRegion:
        """`(self)`:
        Returns the smallest region the mouse is currently over, or NULL if it is
        over no region.

        `(self, pos: LPoint2)`:
        Returns the preferred region the mouse is over.  In the case of overlapping
        regions, the region with the largest sort order is preferred; if two
        regions have the same sort order, then the smaller region is preferred.

        `(self, x: float, y: float)`:
        Returns the smallest region the indicated point is over, or NULL if it is
        over no region.
        """
    @overload
    def get_over_region(self, x: float, y: float) -> MouseWatcherRegion: ...
    def is_button_down(self, button: ButtonHandle | str) -> bool:
        """Returns true if the indicated button is currently being held down, false
        otherwise.
        """
    def set_button_down_pattern(self, pattern: str) -> None:
        """Sets the pattern string that indicates how the event names are generated
        when a button is depressed.  This is a string that may contain any of the
        following:

        %r  - the name of the region the mouse is over %b  - the name of the button
        pressed.

        The event name will be based on the in_pattern string specified here, with
        all occurrences of the above strings replaced with the corresponding
        values.
        """
    def get_button_down_pattern(self) -> str:
        """Returns the string that indicates how event names are generated when a
        button is depressed.  See set_button_down_pattern().
        """
    def set_button_up_pattern(self, pattern: str) -> None:
        """Sets the pattern string that indicates how the event names are generated
        when a button is released.  See set_button_down_pattern().
        """
    def get_button_up_pattern(self) -> str:
        """Returns the string that indicates how event names are generated when a
        button is released.  See set_button_down_pattern().
        """
    def set_button_repeat_pattern(self, pattern: str) -> None:
        """Sets the pattern string that indicates how the event names are generated
        when a button is continuously held and generates keyrepeat "down" events.
        This is a string that may contain any of the following:

        %r  - the name of the region the mouse is over %b  - the name of the button
        pressed.

        The event name will be based on the in_pattern string specified here, with
        all occurrences of the above strings replaced with the corresponding
        values.
        """
    def get_button_repeat_pattern(self) -> str:
        """Returns the string that indicates how event names are names are generated
        when a button is continuously held and generates keyrepeat "down" events.
        See set_button_repeat_pattern().
        """
    def set_enter_pattern(self, pattern: str) -> None:
        """Sets the pattern string that indicates how the event names are generated
        when the mouse enters a region.  This is different from within_pattern, in
        that a mouse is only "entered" in the topmost region at a given time, while
        it might be "within" multiple nested regions.
        """
    def get_enter_pattern(self) -> str:
        """Returns the string that indicates how event names are generated when the
        mouse enters a region.  This is different from within_pattern, in that a
        mouse is only "entered" in the topmost region at a given time, while it
        might be "within" multiple nested regions.
        """
    def set_leave_pattern(self, pattern: str) -> None:
        """Sets the pattern string that indicates how the event names are generated
        when the mouse leaves a region.  This is different from without_pattern, in
        that a mouse is only "entered" in the topmost region at a given time, while
        it might be "within" multiple nested regions.
        """
    def get_leave_pattern(self) -> str:
        """Returns the string that indicates how event names are generated when the
        mouse leaves a region.  This is different from without_pattern, in that a
        mouse is only "entered" in the topmost region at a given time, while it
        might be "within" multiple nested regions.
        """
    def set_within_pattern(self, pattern: str) -> None:
        """Sets the pattern string that indicates how the event names are generated
        when the mouse wanders over a region.  This is different from
        enter_pattern, in that a mouse is only "entered" in the topmost region at a
        given time, while it might be "within" multiple nested regions.
        """
    def get_within_pattern(self) -> str:
        """Returns the string that indicates how event names are generated when the
        mouse wanders over a region.  This is different from enter_pattern, in that
        a mouse is only "entered" in the topmost region at a given time, while it
        might be "within" multiple nested regions.
        """
    def set_without_pattern(self, pattern: str) -> None:
        """Sets the pattern string that indicates how the event names are generated
        when the mouse wanders out of a region.  This is different from
        leave_pattern, in that a mouse is only "entered" in the topmost region at a
        given time, while it might be "within" multiple nested regions.
        """
    def get_without_pattern(self) -> str:
        """Returns the string that indicates how event names are generated when the
        mouse wanders out of a region.  This is different from leave_pattern, in
        that a mouse is only "entered" in the topmost region at a given time, while
        it might be "within" multiple nested regions.
        """
    def set_geometry(self, node: PandaNode) -> None:
        """Sets the node that will be transformed each frame by the mouse's
        coordinates.  It will also be hidden when the mouse goes outside the
        window.  This can be used to implement a software mouse pointer for when a
        hardware (or system) mouse pointer is unavailable.
        """
    def has_geometry(self) -> bool:
        """Returns true if a software mouse pointer has been setup via set_geometry(),
        or false otherwise.  See set_geometry().
        """
    def get_geometry(self) -> PandaNode:
        """Returns the node that has been set as the software mouse pointer, or NULL
        if no node has been set.  See has_geometry() and set_geometry().
        """
    def clear_geometry(self) -> None:
        """Stops the use of the software cursor set up via set_geometry()."""
    def set_extra_handler(self, eh: EventHandler) -> None:
        """As an optimization for the C++ Gui, an extra handler can be registered with
        a mouseWatcher so that events can be dealt with much sooner.
        """
    def get_extra_handler(self) -> EventHandler:
        """As an optimization for the C++ Gui, an extra handler can be registered with
        a mouseWatcher so that events can be dealt with much sooner.
        """
    def set_modifier_buttons(self, mods: ModifierButtons) -> None:
        """Sets the buttons that should be monitored as modifier buttons for
        generating events to the MouseWatcherRegions.
        """
    def get_modifier_buttons(self) -> ModifierButtons:
        """Returns the set of buttons that are being monitored as modifier buttons, as
        well as their current state.
        """
    def set_display_region(self, dr: DisplayRegion) -> None:
        """Constrains the MouseWatcher to watching the mouse within a particular
        indicated region of the screen.  DataNodes parented under the MouseWatcher
        will observe the mouse and keyboard events only when the mouse is within
        the indicated region, and the observed range will be from -1 .. 1 across
        the region.

        Do not delete the DisplayRegion while it is owned by the MouseWatcher.
        """
    def clear_display_region(self) -> None:
        """Removes the display region constraint from the MouseWatcher, and restores
        it to the default behavior of watching the whole window.
        """
    def get_display_region(self) -> DisplayRegion:
        """Returns the display region the MouseWatcher is constrained to by
        set_display_region(), or NULL if it is not constrained.
        """
    def has_display_region(self) -> bool:
        """Returns true if the MouseWatcher has been constrained to a particular
        region of the screen via set_display_region(), or false otherwise.  If this
        returns true, get_display_region() may be used to return the particular
        region.
        """
    def add_group(self, group: MouseWatcherGroup) -> bool:
        """Adds the indicated group of regions to the set of regions the MouseWatcher
        will monitor each frame.

        Since the MouseWatcher itself inherits from MouseWatcherBase, this
        operation is normally not necessary--you can simply add the Regions you
        care about one at a time.  Adding a complete group is useful when you may
        want to explicitly remove the regions as a group later.

        Returns true if the group was successfully added, or false if it was
        already on the list.
        """
    def remove_group(self, group: MouseWatcherGroup) -> bool:
        """Removes the indicated group from the set of extra groups associated with
        the MouseWatcher.  Returns true if successful, or false if the group was
        already removed or was never added via add_group().
        """
    def replace_group(self, old_group: MouseWatcherGroup, new_group: MouseWatcherGroup) -> bool:
        """Atomically removes old_group from the MouseWatcher, and replaces it with
        new_group.  Presumably old_group and new_group might have some regions in
        common; these are handled properly.

        If old_group is not already present, simply adds new_group and returns
        false.  Otherwise, removes old_group and adds new_group, and then returns
        true.
        """
    def get_num_groups(self) -> int:
        """Returns the number of separate groups added to the MouseWatcher via
        add_group().
        """
    def get_group(self, n: int) -> MouseWatcherGroup:
        """Returns the nth group added to the MouseWatcher via add_group()."""
    def set_inactivity_timeout(self, timeout: float) -> None:
        """Sets an inactivity timeout on the mouse activity.  When this timeout (in
        seconds) is exceeded with no keyboard or mouse activity, all currently-held
        buttons are automatically released.  This is intended to help protect
        against people who inadvertently (or intentionally) leave a keyboard key
        stuck down and then wander away from the keyboard.

        Also, when this timeout expires, the event specified by
        set_inactivity_timeout_event() will be generated.
        """
    def has_inactivity_timeout(self) -> bool:
        """Returns true if an inactivity timeout has been set, false otherwise."""
    def get_inactivity_timeout(self) -> float:
        """Returns the inactivity timeout that has been set.  It is an error to call
        this if has_inactivity_timeout() returns false.
        """
    def clear_inactivity_timeout(self) -> None:
        """Removes the inactivity timeout and restores the MouseWatcher to its default
        behavior of allowing a key to be held indefinitely.
        """
    def set_inactivity_timeout_event(self, event: str) -> None:
        """Specifies the event string that will be generated when the inactivity
        timeout counter expires.  See set_inactivity_timeout().
        """
    def get_inactivity_timeout_event(self) -> str:
        """Returns the event string that will be generated when the inactivity timeout
        counter expires.  See set_inactivity_timeout().
        """
    def get_trail_log(self) -> PointerEventList:
        """Obtain the mouse trail log.  This is a PointerEventList.  Does not make a
        copy, therefore, this PointerEventList will be updated each time
        process_events gets called.

        To use trail logging, you need to enable the generation of pointer events
        in the GraphicsWindowInputDevice and set the trail log duration in the
        MouseWatcher.  Otherwise, the trail log will be empty.
        """
    def num_trail_recent(self) -> int:
        """This counter indicates how many events were added to the trail log this
        frame.  The trail log is updated once per frame, during the process_events
        operation.
        """
    def set_trail_log_duration(self, duration: float) -> None:
        """If the duration is nonzero, causes the MouseWatcher to log the mouse's
        trail.  Events older than the specified duration are discarded.  If the
        duration is zero, logging is disabled.
        """
    def get_trail_node(self) -> GeomNode:
        """Returns a GeomNode that represents the mouse trail.  The intent is that you
        should reparent this GeomNode to Render2D, and then forget about it.  The
        MouseWatcher will continually update the trail node.  There is only one
        trail node, it does not create a new one each time you call get_trail_node.

        This is not a particularly beautiful way to render a mouse trail.  It is
        intended more for debugging purposes than for finished applications.  Even
        so, It is suggested that you might want to apply a line thickness and
        antialias mode to the line --- doing so makes it look a lot better.
        """
    def clear_trail_node(self) -> None:
        """If you have previously fetched the trail node using get_trail_node, then
        the MouseWatcher is continually updating the trail node every frame.  Using
        clear_trail_node causes the MouseWatcher to forget the trail node and stop
        updating it.
        """
    def clear_trail_log(self) -> None:
        """Clears the mouse trail log.  This does not prevent further accumulation of
        the log given future events.
        """
    def note_activity(self) -> None:
        """Can be used in conjunction with the inactivity timeout to inform the
        MouseWatcher that the user has just performed some action which proves
        he/she is present.  It may be necessary to call this for external events,
        such as joystick action, that the MouseWatcher might otherwise not know
        about.  This will reset the current inactivity timer.  When the inactivity
        timer reaches the length of time specified by set_inactivity_timeout(),
        with no keyboard or mouse activity and no calls to note_activity(), then
        any buttons held will be automatically released.
        """
    def get_groups(self) -> tuple[MouseWatcherGroup, ...]: ...
    upcastToDataNode = upcast_to_DataNode
    upcastToMouseWatcherBase = upcast_to_MouseWatcherBase
    hasMouse = has_mouse
    isMouseOpen = is_mouse_open
    getMouse = get_mouse
    getMouseX = get_mouse_x
    getMouseY = get_mouse_y
    setFrame = set_frame
    getFrame = get_frame
    isOverRegion = is_over_region
    getOverRegion = get_over_region
    isButtonDown = is_button_down
    setButtonDownPattern = set_button_down_pattern
    getButtonDownPattern = get_button_down_pattern
    setButtonUpPattern = set_button_up_pattern
    getButtonUpPattern = get_button_up_pattern
    setButtonRepeatPattern = set_button_repeat_pattern
    getButtonRepeatPattern = get_button_repeat_pattern
    setEnterPattern = set_enter_pattern
    getEnterPattern = get_enter_pattern
    setLeavePattern = set_leave_pattern
    getLeavePattern = get_leave_pattern
    setWithinPattern = set_within_pattern
    getWithinPattern = get_within_pattern
    setWithoutPattern = set_without_pattern
    getWithoutPattern = get_without_pattern
    setGeometry = set_geometry
    hasGeometry = has_geometry
    getGeometry = get_geometry
    clearGeometry = clear_geometry
    setExtraHandler = set_extra_handler
    getExtraHandler = get_extra_handler
    setModifierButtons = set_modifier_buttons
    getModifierButtons = get_modifier_buttons
    setDisplayRegion = set_display_region
    clearDisplayRegion = clear_display_region
    getDisplayRegion = get_display_region
    hasDisplayRegion = has_display_region
    addGroup = add_group
    removeGroup = remove_group
    replaceGroup = replace_group
    getNumGroups = get_num_groups
    getGroup = get_group
    setInactivityTimeout = set_inactivity_timeout
    hasInactivityTimeout = has_inactivity_timeout
    getInactivityTimeout = get_inactivity_timeout
    clearInactivityTimeout = clear_inactivity_timeout
    setInactivityTimeoutEvent = set_inactivity_timeout_event
    getInactivityTimeoutEvent = get_inactivity_timeout_event
    getTrailLog = get_trail_log
    numTrailRecent = num_trail_recent
    setTrailLogDuration = set_trail_log_duration
    getTrailNode = get_trail_node
    clearTrailNode = clear_trail_node
    clearTrailLog = clear_trail_log
    noteActivity = note_activity
    getGroups = get_groups

class MouseWatcherParameter:
    """This is sent along as a parameter to most events generated for a region to
    indicate the mouse and button state for the event.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def has_button(self) -> bool:
        """Returns true if this parameter has an associated mouse or keyboard button,
        false otherwise.
        """
    def get_button(self) -> ButtonHandle:
        """Returns the mouse or keyboard button associated with this event.  If
        has_button(), above, returns false, this returns ButtonHandle::none().
        """
    def is_keyrepeat(self) -> bool:
        """Returns true if the button-down even was generated due to keyrepeat, or
        false if it was an original button down.
        """
    def has_keycode(self) -> bool:
        """Returns true if this parameter has an associated keycode, false otherwise."""
    def get_keycode(self) -> int:
        """Returns the keycode associated with this event.  If has_keycode(), above,
        returns false, this returns 0.
        """
    def has_candidate(self) -> bool:
        """Returns true if this parameter has an associated candidate string, false
        otherwise.
        """
    def get_candidate_string_encoded(self, encoding: _TextEncoder_Encoding = ...) -> str:
        """Returns the candidate string associated with this event.  If
        has_candidate(), above, returns false, this returns the empty string.
        """
    def get_highlight_start(self) -> int:
        """Returns the first highlighted character in the candidate string."""
    def get_highlight_end(self) -> int:
        """Returns one more than the last highlighted character in the candidate
        string.
        """
    def get_cursor_pos(self) -> int:
        """Returns the position of the user's edit cursor within the candidate string."""
    def get_modifier_buttons(self) -> ModifierButtons:
        """Returns the set of modifier buttons that were being held down while the
        event was generated.
        """
    def has_mouse(self) -> bool:
        """Returns true if this parameter has an associated mouse position, false
        otherwise.
        """
    def get_mouse(self) -> LPoint2:
        """Returns the mouse position at the time the event was generated, in the
        normalized range (-1 .. 1).  It is valid to call this only if has_mouse()
        returned true.
        """
    def is_outside(self) -> bool:
        """Returns true if the mouse was outside the region at the time the event was
        generated, false otherwise.  This is only valid for "release" type events.
        """
    def output(self, out: ostream) -> None: ...
    hasButton = has_button
    getButton = get_button
    isKeyrepeat = is_keyrepeat
    hasKeycode = has_keycode
    getKeycode = get_keycode
    hasCandidate = has_candidate
    getCandidateStringEncoded = get_candidate_string_encoded
    getHighlightStart = get_highlight_start
    getHighlightEnd = get_highlight_end
    getCursorPos = get_cursor_pos
    getModifierButtons = get_modifier_buttons
    hasMouse = has_mouse
    getMouse = get_mouse
    isOutside = is_outside

class Trackball(MouseInterfaceNode):
    """Trackball acts like Performer in trackball mode.  It can either spin around
    a piece of geometry directly, or it can spin around a camera with the
    inverse transform to make it appear that the whole world is spinning.

    The Trackball object actually just places a transform in the data graph;
    parent a Transform2SG node under it to actually transform objects (or
    cameras) in the world.
    """

    CM_default: Final = 0
    CMDefault: Final = 0
    CM_truck: Final = 1
    CMTruck: Final = 1
    CM_pan: Final = 2
    CMPan: Final = 2
    CM_dolly: Final = 3
    CMDolly: Final = 3
    CM_roll: Final = 4
    CMRoll: Final = 4
    @overload
    def __init__(self, __param0: Trackball) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def reset(self) -> None:
        """Reinitializes all transforms to identity."""
    def get_forward_scale(self) -> float:
        """Returns the scale factor applied to forward and backward motion.  See
        set_forward_scale().
        """
    def set_forward_scale(self, fwdscale: float) -> None:
        """Changes the scale factor applied to forward and backward motion.  The
        larger this number, the faster the model will move in response to dollying
        in and out.
        """
    def get_pos(self) -> LPoint3:
        """Return the offset from the center of rotation."""
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def get_z(self) -> float: ...
    @overload
    def set_pos(self, vec: Vec3Like) -> None:
        """Directly set the offset from the rotational origin."""
    @overload
    def set_pos(self, x: float, y: float, z: float) -> None: ...
    def set_x(self, x: float) -> None: ...
    def set_y(self, y: float) -> None: ...
    def set_z(self, z: float) -> None: ...
    def get_hpr(self) -> LVecBase3:
        """Return the trackball's orientation."""
    def get_h(self) -> float: ...
    def get_p(self) -> float: ...
    def get_r(self) -> float: ...
    @overload
    def set_hpr(self, hpr: Vec3Like) -> None:
        """Directly set the mover's orientation."""
    @overload
    def set_hpr(self, h: float, p: float, r: float) -> None: ...
    def set_h(self, h: float) -> None: ...
    def set_p(self, p: float) -> None: ...
    def set_r(self, r: float) -> None: ...
    def reset_origin_here(self) -> None:
        """Reposition the center of rotation to coincide with the current translation
        offset.  Future rotations will be about the current origin.
        """
    def move_origin(self, x: float, y: float, z: float) -> None:
        """Moves the center of rotation by the given amount."""
    def get_origin(self) -> LPoint3:
        """Returns the current center of rotation."""
    def set_origin(self, origin: Vec3Like) -> None:
        """Directly sets the center of rotation."""
    def set_control_mode(self, control_mode: _Trackball_ControlMode) -> None:
        """Sets the control mode.  Normally this is CM_default, which means each mouse
        button serves its normal function.  When it is CM_truck, CM_pan, CM_dolly,
        or CM_roll, all of the mouse buttons serve the indicated function instead
        of their normal function.  This can be used in conjunction with some
        external way of changing modes.
        """
    def get_control_mode(self) -> _Trackball_ControlMode:
        """Returns the control mode.  See set_control_mode()."""
    def set_invert(self, flag: bool) -> None:
        """Sets the invert flag.  When this is set, the inverse matrix is generated,
        suitable for joining to a camera, instead of parenting the scene under it.
        """
    def get_invert(self) -> bool:
        """Returns the invert flag.  When this is set, the inverse matrix is
        generated, suitable for joining to a camera, instead of parenting the scene
        under it.
        """
    def set_rel_to(self, rel_to: NodePath) -> None:
        """Sets the NodePath that all trackball manipulations are to be assumed to be
        relative to.  For instance, set your camera node here to make the trackball
        motion camera relative.  The default is the empty path, which means
        trackball motion is in global space.
        """
    def get_rel_to(self) -> NodePath:
        """Returns the NodePath that all trackball manipulations are relative to, or
        the empty path.
        """
    def set_coordinate_system(self, cs: _CoordinateSystem) -> None:
        """Sets the coordinate system of the Trackball.  Normally, this is the default
        coordinate system.  This changes the axes the Trackball manipulates so that
        the user interface remains consistent across different coordinate systems.
        """
    def get_coordinate_system(self) -> _CoordinateSystem:
        """Returns the coordinate system of the Trackball.  See
        set_coordinate_system().
        """
    def set_mat(self, mat: Mat4Like) -> None:
        """Stores the indicated transform in the trackball.  This is a transform in
        global space, regardless of the rel_to node.
        """
    def get_mat(self) -> LMatrix4:
        """Returns the matrix represented by the trackball rotation."""
    def get_trans_mat(self) -> LMatrix4:
        """Returns the actual transform that will be applied to the scene graph.  This
        is the same as get_mat(), unless invert is in effect.
        """
    getForwardScale = get_forward_scale
    setForwardScale = set_forward_scale
    getPos = get_pos
    getX = get_x
    getY = get_y
    getZ = get_z
    setPos = set_pos
    setX = set_x
    setY = set_y
    setZ = set_z
    getHpr = get_hpr
    getH = get_h
    getP = get_p
    getR = get_r
    setHpr = set_hpr
    setH = set_h
    setP = set_p
    setR = set_r
    resetOriginHere = reset_origin_here
    moveOrigin = move_origin
    getOrigin = get_origin
    setOrigin = set_origin
    setControlMode = set_control_mode
    getControlMode = get_control_mode
    setInvert = set_invert
    getInvert = get_invert
    setRelTo = set_rel_to
    getRelTo = get_rel_to
    setCoordinateSystem = set_coordinate_system
    getCoordinateSystem = get_coordinate_system
    setMat = set_mat
    getMat = get_mat
    getTransMat = get_trans_mat

class Transform2SG(DataNode):
    """input: Transform (matrix)

    output: none, but applies the matrix as the transform transition for a
    given arc of the scene graph.
    """

    @overload
    def __init__(self, __param0: Transform2SG) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_node(self, node: PandaNode) -> None:
        """Sets the node that this object will adjust."""
    def get_node(self) -> PandaNode:
        """Returns the node that this object will adjust, or NULL if the node has not
        yet been set.
        """
    setNode = set_node
    getNode = get_node
