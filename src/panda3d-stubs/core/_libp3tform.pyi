from collections.abc import Sequence
from typing import Any, ClassVar, Literal, TypeAlias, overload
from panda3d.core import (
    ButtonHandle,
    ConfigVariableColor,
    DataNode,
    DisplayRegion,
    EventHandler,
    EventParameter,
    GeomNode,
    LMatrix3f,
    LMatrix4f,
    LPoint2f,
    LPoint3f,
    LVecBase2f,
    LVecBase3f,
    LVecBase4f,
    ModifierButtons,
    Namable,
    NodePath,
    PandaNode,
    PointerEventList,
    ReferenceCount,
    TypeHandle,
    TypedWritableReferenceCount,
    UnalignedLMatrix4f,
    UnalignedLVecBase4f,
    ostream,
)

_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_Mat4f: TypeAlias = LMatrix4f | UnalignedLMatrix4f
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
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
    DtoolClassDict: ClassVar[dict[str, Any]]
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
    def set_button_down_event(self, button_down_event: str) -> None: ...
    def get_button_down_event(self) -> str: ...
    def set_button_up_event(self, button_up_event: str) -> None: ...
    def get_button_up_event(self) -> str: ...
    def set_button_repeat_event(self, button_repeat_event: str) -> None: ...
    def get_button_repeat_event(self) -> str: ...
    def set_keystroke_event(self, keystroke_event: str) -> None: ...
    def get_keystroke_event(self) -> str: ...
    def set_candidate_event(self, candidate_event: str) -> None: ...
    def get_candidate_event(self) -> str: ...
    def set_move_event(self, move_event: str) -> None: ...
    def get_move_event(self) -> str: ...
    def set_raw_button_down_event(self, raw_button_down_event: str) -> None: ...
    def get_raw_button_down_event(self) -> str: ...
    def set_raw_button_up_event(self, raw_button_up_event: str) -> None: ...
    def get_raw_button_up_event(self) -> str: ...
    def set_prefix(self, prefix: str) -> None: ...
    def get_prefix(self) -> str: ...
    def set_specific_flag(self, specific_flag: bool) -> None: ...
    def get_specific_flag(self) -> bool: ...
    def set_time_flag(self, time_flag: bool) -> None: ...
    def get_time_flag(self) -> bool: ...
    def add_parameter(self, obj: EventParameter | float | int | str | None) -> None: ...
    def get_num_parameters(self) -> int: ...
    def get_parameter(self, n: int) -> EventParameter: ...
    def get_modifier_buttons(self) -> ModifierButtons: ...
    def set_modifier_buttons(self, mods: ModifierButtons) -> None: ...
    def set_throw_buttons_active(self, flag: bool) -> None: ...
    def get_throw_buttons_active(self) -> bool: ...
    def add_throw_button(self, mods: ModifierButtons, button: ButtonHandle) -> bool: ...
    def remove_throw_button(self, mods: ModifierButtons, button: ButtonHandle) -> bool: ...
    @overload
    def has_throw_button(self, button: ButtonHandle) -> bool: ...
    @overload
    def has_throw_button(self, mods: ModifierButtons, button: ButtonHandle) -> bool: ...
    def clear_throw_buttons(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type
    getParameters = get_parameters

class MouseInterfaceNode(DataNode):
    """This is the base class for some classes that monitor the mouse and keyboard
    input and perform some action due to their state.
    
    It collects together some common interface; in particular, the
    require_button() and related methods.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: MouseInterfaceNode) -> None: ...
    def require_button(self, button: ButtonHandle, is_down: bool) -> None: ...
    def clear_button(self, button: ButtonHandle) -> None: ...
    def clear_all_buttons(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    requireButton = require_button
    clearButton = clear_button
    clearAllButtons = clear_all_buttons
    getClassType = get_class_type

class DriveInterface(MouseInterfaceNode):
    """This is a TFormer, similar to Trackball, that moves around a transform
    matrix in response to mouse input.  The basic motion is on a horizontal
    plane, as if driving a vehicle.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, __param0: DriveInterface) -> None: ...
    def set_forward_speed(self, speed: float) -> None: ...
    def get_forward_speed(self) -> float: ...
    def set_reverse_speed(self, speed: float) -> None: ...
    def get_reverse_speed(self) -> float: ...
    def set_rotate_speed(self, speed: float) -> None: ...
    def get_rotate_speed(self) -> float: ...
    def set_vertical_dead_zone(self, zone: float) -> None: ...
    def get_vertical_dead_zone(self) -> float: ...
    def set_horizontal_dead_zone(self, zone: float) -> None: ...
    def get_horizontal_dead_zone(self) -> float: ...
    def set_vertical_ramp_up_time(self, ramp_up_time: float) -> None: ...
    def get_vertical_ramp_up_time(self) -> float: ...
    def set_vertical_ramp_down_time(self, ramp_down_time: float) -> None: ...
    def get_vertical_ramp_down_time(self) -> float: ...
    def set_horizontal_ramp_up_time(self, ramp_up_time: float) -> None: ...
    def get_horizontal_ramp_up_time(self) -> float: ...
    def set_horizontal_ramp_down_time(self, ramp_down_time: float) -> None: ...
    def get_horizontal_ramp_down_time(self) -> float: ...
    def get_speed(self) -> float: ...
    def get_rot_speed(self) -> float: ...
    def reset(self) -> None: ...
    def get_pos(self) -> LPoint3f: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def get_z(self) -> float: ...
    @overload
    def set_pos(self, vec: _Vec3f) -> None: ...
    @overload
    def set_pos(self, x: float, y: float, z: float) -> None: ...
    def set_x(self, x: float) -> None: ...
    def set_y(self, y: float) -> None: ...
    def set_z(self, z: float) -> None: ...
    def get_hpr(self) -> LVecBase3f: ...
    def get_h(self) -> float: ...
    def get_p(self) -> float: ...
    def get_r(self) -> float: ...
    @overload
    def set_hpr(self, hpr: _Vec3f) -> None: ...
    @overload
    def set_hpr(self, h: float, p: float, r: float) -> None: ...
    def set_h(self, h: float) -> None: ...
    def set_p(self, p: float) -> None: ...
    def set_r(self, r: float) -> None: ...
    def set_force_roll(self, force_roll: float) -> None: ...
    def set_ignore_mouse(self, ignore_mouse: bool) -> None: ...
    def get_ignore_mouse(self) -> bool: ...
    def set_force_mouse(self, force_mouse: bool) -> None: ...
    def get_force_mouse(self) -> bool: ...
    def set_stop_this_frame(self, stop_this_frame: bool) -> None: ...
    def get_stop_this_frame(self) -> bool: ...
    def set_mat(self, mat: _Mat4f) -> None: ...
    def get_mat(self) -> LMatrix4f: ...
    def force_dgraph(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type

class MouseSubregion(MouseInterfaceNode):
    """The MouseSubregion object scales the mouse inputs from within a rectangular
    region of the screen, as if they were the full-screen inputs.
    
    If you choose your MouseSubregion coordinates to exactly match a
    DisplayRegion within your window, you end up with a virtual mouse within
    your DisplayRegion.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: MouseSubregion) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def get_left(self) -> float: ...
    def get_right(self) -> float: ...
    def get_bottom(self) -> float: ...
    def get_top(self) -> float: ...
    def set_dimensions(self, l: float, r: float, b: float, t: float) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getLeft = get_left
    getRight = get_right
    getBottom = get_bottom
    getTop = get_top
    setDimensions = set_dimensions
    getClassType = get_class_type

class MouseWatcherRegion(TypedWritableReferenceCount, Namable):
    """This is the class that defines a rectangular region on the screen for the
    MouseWatcher.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    frame: LVecBase4f
    sort: int
    active: bool
    keyboard: bool
    suppress_flags: int
    SF_mouse_button: ClassVar[Literal[1]]
    SF_other_button: ClassVar[Literal[2]]
    SF_any_button: ClassVar[Literal[3]]
    SF_mouse_position: ClassVar[Literal[4]]
    @property
    def area(self) -> float: ...
    @overload
    def __init__(self, __param0: MouseWatcherRegion) -> None: ...
    @overload
    def __init__(self, name: str, frame: _Vec4f) -> None: ...
    @overload
    def __init__(self, name: str, left: float, right: float, bottom: float, top: float) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    @overload
    def set_frame(self, frame: _Vec4f) -> None: ...
    @overload
    def set_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_frame(self) -> LVecBase4f: ...
    def get_area(self) -> float: ...
    def set_sort(self, sort: int) -> None: ...
    def get_sort(self) -> int: ...
    def set_active(self, active: bool) -> None: ...
    def get_active(self) -> bool: ...
    def set_keyboard(self, keyboard: bool) -> None: ...
    def get_keyboard(self) -> bool: ...
    def set_suppress_flags(self, suppress_flags: int) -> None: ...
    def get_suppress_flags(self) -> int: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type
    SFMouseButton = SF_mouse_button
    SFOtherButton = SF_other_button
    SFAnyButton = SF_any_button
    SFMousePosition = SF_mouse_position

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
    def add_region(self, region: MouseWatcherRegion) -> None: ...
    def has_region(self, region: MouseWatcherRegion) -> bool: ...
    def remove_region(self, region: MouseWatcherRegion) -> bool: ...
    def find_region(self, name: str) -> MouseWatcherRegion: ...
    def clear_regions(self) -> None: ...
    def sort_regions(self) -> None: ...
    def is_sorted(self) -> bool: ...
    def get_num_regions(self) -> int: ...
    def get_region(self, n: int) -> MouseWatcherRegion: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def show_regions(self, render2d: NodePath, bin_name: str, draw_order: int) -> None: ...
    def set_color(self, color: _Vec4f) -> None: ...
    def hide_regions(self) -> None: ...
    def update_regions(self) -> None: ...
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
    DtoolClassDict: ClassVar[dict[str, Any]]
    def upcast_to_MouseWatcherBase(self) -> MouseWatcherBase: ...
    def upcast_to_ReferenceCount(self) -> ReferenceCount: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToMouseWatcherBase = upcast_to_MouseWatcherBase
    upcastToReferenceCount = upcast_to_ReferenceCount
    getClassType = get_class_type

class MouseWatcher(DataNode, MouseWatcherBase):
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
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str = ...) -> None: ...
    def upcast_to_DataNode(self) -> DataNode: ...
    def upcast_to_MouseWatcherBase(self) -> MouseWatcherBase: ...
    def remove_region(self, region: MouseWatcherRegion) -> bool: ...
    def has_mouse(self) -> bool: ...
    def is_mouse_open(self) -> bool: ...
    def get_mouse(self) -> LPoint2f: ...
    def get_mouse_x(self) -> float: ...
    def get_mouse_y(self) -> float: ...
    @overload
    def set_frame(self, frame: _Vec4f) -> None: ...
    @overload
    def set_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_frame(self) -> LVecBase4f: ...
    @overload
    def is_over_region(self) -> bool: ...
    @overload
    def is_over_region(self, pos: LVecBase2f) -> bool: ...
    @overload
    def is_over_region(self, x: float, y: float) -> bool: ...
    @overload
    def get_over_region(self) -> MouseWatcherRegion: ...
    @overload
    def get_over_region(self, pos: LVecBase2f) -> MouseWatcherRegion: ...
    @overload
    def get_over_region(self, x: float, y: float) -> MouseWatcherRegion: ...
    def is_button_down(self, button: ButtonHandle) -> bool: ...
    def set_button_down_pattern(self, pattern: str) -> None: ...
    def get_button_down_pattern(self) -> str: ...
    def set_button_up_pattern(self, pattern: str) -> None: ...
    def get_button_up_pattern(self) -> str: ...
    def set_button_repeat_pattern(self, pattern: str) -> None: ...
    def get_button_repeat_pattern(self) -> str: ...
    def set_enter_pattern(self, pattern: str) -> None: ...
    def get_enter_pattern(self) -> str: ...
    def set_leave_pattern(self, pattern: str) -> None: ...
    def get_leave_pattern(self) -> str: ...
    def set_within_pattern(self, pattern: str) -> None: ...
    def get_within_pattern(self) -> str: ...
    def set_without_pattern(self, pattern: str) -> None: ...
    def get_without_pattern(self) -> str: ...
    def set_geometry(self, node: PandaNode) -> None: ...
    def has_geometry(self) -> bool: ...
    def get_geometry(self) -> PandaNode: ...
    def clear_geometry(self) -> None: ...
    def set_extra_handler(self, eh: EventHandler) -> None: ...
    def get_extra_handler(self) -> EventHandler: ...
    def set_modifier_buttons(self, mods: ModifierButtons) -> None: ...
    def get_modifier_buttons(self) -> ModifierButtons: ...
    def set_display_region(self, dr: DisplayRegion) -> None: ...
    def clear_display_region(self) -> None: ...
    def get_display_region(self) -> DisplayRegion: ...
    def has_display_region(self) -> bool: ...
    def add_group(self, group: MouseWatcherGroup) -> bool: ...
    def remove_group(self, group: MouseWatcherGroup) -> bool: ...
    def replace_group(self, old_group: MouseWatcherGroup, new_group: MouseWatcherGroup) -> bool: ...
    def get_num_groups(self) -> int: ...
    def get_group(self, n: int) -> MouseWatcherGroup: ...
    def set_inactivity_timeout(self, timeout: float) -> None: ...
    def has_inactivity_timeout(self) -> bool: ...
    def get_inactivity_timeout(self) -> float: ...
    def clear_inactivity_timeout(self) -> None: ...
    def set_inactivity_timeout_event(self, event: str) -> None: ...
    def get_inactivity_timeout_event(self) -> str: ...
    def get_trail_log(self) -> PointerEventList: ...
    def num_trail_recent(self) -> int: ...
    def set_trail_log_duration(self, duration: float) -> None: ...
    def get_trail_node(self) -> GeomNode: ...
    def clear_trail_node(self) -> None: ...
    def clear_trail_log(self) -> None: ...
    def note_activity(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_groups(self) -> tuple[MouseWatcherGroup, ...]: ...
    upcastToDataNode = upcast_to_DataNode
    upcastToMouseWatcherBase = upcast_to_MouseWatcherBase
    removeRegion = remove_region
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
    getClassType = get_class_type
    getGroups = get_groups

class MouseWatcherParameter:
    """This is sent along as a parameter to most events generated for a region to
    indicate the mouse and button state for the event.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def has_button(self) -> bool: ...
    def get_button(self) -> ButtonHandle: ...
    def is_keyrepeat(self) -> bool: ...
    def has_keycode(self) -> bool: ...
    def get_keycode(self) -> int: ...
    def has_candidate(self) -> bool: ...
    @overload
    def get_candidate_string_encoded(self) -> str: ...
    @overload
    def get_candidate_string_encoded(self, encoding: _TextEncoder_Encoding) -> str: ...
    def get_highlight_start(self) -> int: ...
    def get_highlight_end(self) -> int: ...
    def get_cursor_pos(self) -> int: ...
    def get_modifier_buttons(self) -> ModifierButtons: ...
    def has_mouse(self) -> bool: ...
    def get_mouse(self) -> LPoint2f: ...
    def is_outside(self) -> bool: ...
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
    DtoolClassDict: ClassVar[dict[str, Any]]
    CM_default: ClassVar[Literal[0]]
    CM_truck: ClassVar[Literal[1]]
    CM_pan: ClassVar[Literal[2]]
    CM_dolly: ClassVar[Literal[3]]
    CM_roll: ClassVar[Literal[4]]
    @overload
    def __init__(self, __param0: Trackball) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def reset(self) -> None: ...
    def get_forward_scale(self) -> float: ...
    def set_forward_scale(self, fwdscale: float) -> None: ...
    def get_pos(self) -> LPoint3f: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def get_z(self) -> float: ...
    @overload
    def set_pos(self, vec: _Vec3f) -> None: ...
    @overload
    def set_pos(self, x: float, y: float, z: float) -> None: ...
    def set_x(self, x: float) -> None: ...
    def set_y(self, y: float) -> None: ...
    def set_z(self, z: float) -> None: ...
    def get_hpr(self) -> LVecBase3f: ...
    def get_h(self) -> float: ...
    def get_p(self) -> float: ...
    def get_r(self) -> float: ...
    @overload
    def set_hpr(self, hpr: _Vec3f) -> None: ...
    @overload
    def set_hpr(self, h: float, p: float, r: float) -> None: ...
    def set_h(self, h: float) -> None: ...
    def set_p(self, p: float) -> None: ...
    def set_r(self, r: float) -> None: ...
    def reset_origin_here(self) -> None: ...
    def move_origin(self, x: float, y: float, z: float) -> None: ...
    def get_origin(self) -> LPoint3f: ...
    def set_origin(self, origin: _Vec3f) -> None: ...
    def set_control_mode(self, control_mode: _Trackball_ControlMode) -> None: ...
    def get_control_mode(self) -> _Trackball_ControlMode: ...
    def set_invert(self, flag: bool) -> None: ...
    def get_invert(self) -> bool: ...
    def set_rel_to(self, rel_to: NodePath) -> None: ...
    def get_rel_to(self) -> NodePath: ...
    def set_coordinate_system(self, cs: _CoordinateSystem) -> None: ...
    def get_coordinate_system(self) -> _CoordinateSystem: ...
    def set_mat(self, mat: _Mat4f) -> None: ...
    def get_mat(self) -> LMatrix4f: ...
    def get_trans_mat(self) -> LMatrix4f: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type
    CMDefault = CM_default
    CMTruck = CM_truck
    CMPan = CM_pan
    CMDolly = CM_dolly
    CMRoll = CM_roll

class Transform2SG(DataNode):
    """input: Transform (matrix)
    
    output: none, but applies the matrix as the transform transition for a
    given arc of the scene graph.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: Transform2SG) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def set_node(self, node: PandaNode) -> None: ...
    def get_node(self) -> PandaNode: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setNode = set_node
    getNode = get_node
    getClassType = get_class_type
