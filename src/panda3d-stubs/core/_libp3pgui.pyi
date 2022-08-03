from typing import Any, ClassVar, Literal, TypeAlias, overload

_PGFrameStyle_Type: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow

class PGFrameStyle:
    DtoolClassDict: ClassVar[dict[str, Any]]
    T_none: ClassVar[Literal[0]]
    T_flat: ClassVar[Literal[1]]
    T_bevel_out: ClassVar[Literal[2]]
    T_bevel_in: ClassVar[Literal[3]]
    T_groove: ClassVar[Literal[4]]
    T_ridge: ClassVar[Literal[5]]
    T_texture_border: ClassVar[Literal[6]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: PGFrameStyle) -> None: ...
    def assign(self, copy: PGFrameStyle) -> PGFrameStyle: ...
    def set_type(self, type: _PGFrameStyle_Type) -> None: ...
    def get_type(self) -> _PGFrameStyle_Type: ...
    @overload
    def set_color(self, color: _Vec4f) -> None: ...
    @overload
    def set_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def get_color(self) -> LVecBase4f: ...
    def set_texture(self, texture: Texture) -> None: ...
    def has_texture(self) -> bool: ...
    def get_texture(self) -> Texture: ...
    def clear_texture(self) -> None: ...
    @overload
    def set_width(self, width: LVecBase2f) -> None: ...
    @overload
    def set_width(self, x: float, y: float) -> None: ...
    def get_width(self) -> LVecBase2f: ...
    @overload
    def set_uv_width(self, uv_width: LVecBase2f) -> None: ...
    @overload
    def set_uv_width(self, u: float, v: float) -> None: ...
    def get_uv_width(self) -> LVecBase2f: ...
    @overload
    def set_visible_scale(self, visible_scale: LVecBase2f) -> None: ...
    @overload
    def set_visible_scale(self, x: float, y: float) -> None: ...
    def get_visible_scale(self) -> LVecBase2f: ...
    def get_internal_frame(self, frame: _Vec4f) -> LVecBase4f: ...
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
    TNone = T_none
    TFlat = T_flat
    TBevelOut = T_bevel_out
    TBevelIn = T_bevel_in
    TGroove = T_groove
    TRidge = T_ridge
    TTextureBorder = T_texture_border

class PGItem(PandaNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str) -> None: ...
    def set_name(self, name: str) -> None: ...
    @overload
    def set_frame(self, frame: _Vec4f) -> None: ...
    @overload
    def set_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_frame(self) -> LVecBase4f: ...
    def has_frame(self) -> bool: ...
    def clear_frame(self) -> None: ...
    def set_state(self, state: int) -> None: ...
    def get_state(self) -> int: ...
    def set_active(self, active: bool) -> None: ...
    def get_active(self) -> bool: ...
    def set_focus(self, focus: bool) -> None: ...
    def get_focus(self) -> bool: ...
    def set_background_focus(self, focus: bool) -> None: ...
    def get_background_focus(self) -> bool: ...
    def set_suppress_flags(self, suppress_flags: int) -> None: ...
    def get_suppress_flags(self) -> int: ...
    def get_num_state_defs(self) -> int: ...
    def clear_state_def(self, state: int) -> None: ...
    def has_state_def(self, state: int) -> bool: ...
    def get_state_def(self, state: int) -> NodePath: ...
    def instance_to_state_def(self, state: int, path: NodePath) -> NodePath: ...
    def get_frame_style(self, state: int) -> PGFrameStyle: ...
    def set_frame_style(self, state: int, style: PGFrameStyle) -> None: ...
    def get_id(self) -> str: ...
    def set_id(self, id: str) -> None: ...
    @staticmethod
    def get_enter_prefix() -> str: ...
    @staticmethod
    def get_exit_prefix() -> str: ...
    @staticmethod
    def get_within_prefix() -> str: ...
    @staticmethod
    def get_without_prefix() -> str: ...
    @staticmethod
    def get_focus_in_prefix() -> str: ...
    @staticmethod
    def get_focus_out_prefix() -> str: ...
    @staticmethod
    def get_press_prefix() -> str: ...
    @staticmethod
    def get_repeat_prefix() -> str: ...
    @staticmethod
    def get_release_prefix() -> str: ...
    @staticmethod
    def get_keystroke_prefix() -> str: ...
    def get_enter_event(self) -> str: ...
    def get_exit_event(self) -> str: ...
    def get_within_event(self) -> str: ...
    def get_without_event(self) -> str: ...
    def get_focus_in_event(self) -> str: ...
    def get_focus_out_event(self) -> str: ...
    def get_press_event(self, button: ButtonHandle) -> str: ...
    def get_repeat_event(self, button: ButtonHandle) -> str: ...
    def get_release_event(self, button: ButtonHandle) -> str: ...
    def get_keystroke_event(self) -> str: ...
    def get_frame_inv_xform(self) -> LMatrix4f: ...
    def set_sound(self, event: str, sound: AudioSound) -> None: ...
    def clear_sound(self, event: str) -> None: ...
    def get_sound(self, event: str) -> AudioSound: ...
    def has_sound(self, event: str) -> bool: ...
    @staticmethod
    def get_text_node() -> TextNode: ...
    @staticmethod
    def set_text_node(node: TextNode) -> None: ...
    @staticmethod
    def get_focus_item() -> PGItem: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_state_defs(self) -> tuple[NodePath, ...]: ...
    setName = set_name
    setFrame = set_frame
    getFrame = get_frame
    hasFrame = has_frame
    clearFrame = clear_frame
    setState = set_state
    getState = get_state
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
    getClassType = get_class_type
    getStateDefs = get_state_defs

class PGButton(PGItem):
    DtoolClassDict: ClassVar[dict[str, Any]]
    S_ready: ClassVar[Literal[0]]
    S_depressed: ClassVar[Literal[1]]
    S_rollover: ClassVar[Literal[2]]
    S_inactive: ClassVar[Literal[3]]
    @property
    def click_prefix(self) -> str: ...
    def __init__(self, name: str) -> None: ...
    @overload
    def setup(self, ready: NodePath) -> None: ...
    @overload
    def setup(self, label: str, bevel: float = ...) -> None: ...
    @overload
    def setup(self, ready: NodePath, depressed: NodePath) -> None: ...
    @overload
    def setup(self, ready: NodePath, depressed: NodePath, rollover: NodePath) -> None: ...
    @overload
    def setup(self, ready: NodePath, depressed: NodePath, rollover: NodePath, inactive: NodePath) -> None: ...
    def add_click_button(self, button: ButtonHandle) -> bool: ...
    def remove_click_button(self, button: ButtonHandle) -> bool: ...
    def has_click_button(self, button: ButtonHandle) -> bool: ...
    def is_button_down(self) -> bool: ...
    @staticmethod
    def get_click_prefix() -> str: ...
    def get_click_event(self, button: ButtonHandle) -> str: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    addClickButton = add_click_button
    removeClickButton = remove_click_button
    hasClickButton = has_click_button
    isButtonDown = is_button_down
    getClickPrefix = get_click_prefix
    getClickEvent = get_click_event
    getClassType = get_class_type
    SReady = S_ready
    SDepressed = S_depressed
    SRollover = S_rollover
    SInactive = S_inactive

class PGTop(PandaNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str) -> None: ...
    def set_mouse_watcher(self, watcher: MouseWatcher) -> None: ...
    def get_mouse_watcher(self) -> MouseWatcher: ...
    def get_group(self) -> MouseWatcherGroup: ...
    def set_start_sort(self, start_sort: int) -> None: ...
    def get_start_sort(self) -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setMouseWatcher = set_mouse_watcher
    getMouseWatcher = get_mouse_watcher
    getGroup = get_group
    setStartSort = set_start_sort
    getStartSort = get_start_sort
    getClassType = get_class_type

class PGEntry(PGItem):
    DtoolClassDict: ClassVar[dict[str, Any]]
    S_focus: ClassVar[Literal[0]]
    S_no_focus: ClassVar[Literal[1]]
    S_inactive: ClassVar[Literal[2]]
    def __init__(self, name: str) -> None: ...
    def setup(self, width: float, num_lines: int) -> None: ...
    def setup_minimal(self, width: float, num_lines: int) -> None: ...
    def set_text(self, text: str) -> bool: ...
    def get_plain_text(self) -> str: ...
    def get_text(self) -> str: ...
    def get_num_characters(self) -> int: ...
    def get_character(self, n: int) -> int: ...
    def get_graphic(self, n: int) -> TextGraphic: ...
    def get_properties(self, n: int) -> TextProperties: ...
    def set_cursor_position(self, position: int) -> None: ...
    def get_cursor_position(self) -> int: ...
    def get_cursor_X(self) -> float: ...
    def get_cursor_Y(self) -> float: ...
    def set_max_chars(self, max_chars: int) -> None: ...
    def get_max_chars(self) -> int: ...
    def set_max_width(self, max_width: float) -> None: ...
    def get_max_width(self) -> float: ...
    def set_num_lines(self, num_lines: int) -> None: ...
    def get_num_lines(self) -> int: ...
    def set_blink_rate(self, blink_rate: float) -> None: ...
    def get_blink_rate(self) -> float: ...
    def get_cursor_def(self) -> NodePath: ...
    def clear_cursor_def(self) -> None: ...
    def set_cursor_keys_active(self, flag: bool) -> None: ...
    def get_cursor_keys_active(self) -> bool: ...
    def set_obscure_mode(self, flag: bool) -> None: ...
    def get_obscure_mode(self) -> bool: ...
    def set_overflow_mode(self, flag: bool) -> None: ...
    def get_overflow_mode(self) -> bool: ...
    def set_candidate_active(self, candidate_active: str) -> None: ...
    def get_candidate_active(self) -> str: ...
    def set_candidate_inactive(self, candidate_inactive: str) -> None: ...
    def get_candidate_inactive(self) -> str: ...
    def set_text_def(self, state: int, node: TextNode) -> None: ...
    def get_text_def(self, state: int) -> TextNode: ...
    @staticmethod
    def get_accept_prefix() -> str: ...
    @staticmethod
    def get_accept_failed_prefix() -> str: ...
    @staticmethod
    def get_overflow_prefix() -> str: ...
    @staticmethod
    def get_type_prefix() -> str: ...
    @staticmethod
    def get_erase_prefix() -> str: ...
    @staticmethod
    def get_cursormove_prefix() -> str: ...
    def get_accept_event(self, button: ButtonHandle) -> str: ...
    def get_accept_failed_event(self, button: ButtonHandle) -> str: ...
    def get_overflow_event(self) -> str: ...
    def get_type_event(self) -> str: ...
    def get_erase_event(self) -> str: ...
    def get_cursormove_event(self) -> str: ...
    def set_wtext(self, wtext: str) -> bool: ...
    def get_plain_wtext(self) -> str: ...
    def get_wtext(self) -> str: ...
    def set_accept_enabled(self, enabled: bool) -> None: ...
    def is_wtext(self) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type
    SFocus = S_focus
    SNoFocus = S_no_focus
    SInactive = S_inactive

class PGMouseWatcherParameter(TypedWritableReferenceCount, MouseWatcherParameter):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: PGMouseWatcherParameter) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_MouseWatcherParameter(self) -> MouseWatcherParameter: ...
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToMouseWatcherParameter = upcast_to_MouseWatcherParameter
    getClassType = get_class_type

class PGMouseWatcherBackground(MouseWatcherRegion):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: PGMouseWatcherBackground) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class PGVirtualFrame(PGItem):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str = ...) -> None: ...
    def setup(self, width: float, height: float) -> None: ...
    @overload
    def set_clip_frame(self, clip_frame: _Vec4f) -> None: ...
    @overload
    def set_clip_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_clip_frame(self) -> LVecBase4f: ...
    def has_clip_frame(self) -> bool: ...
    def clear_clip_frame(self) -> None: ...
    def set_canvas_transform(self, transform: TransformState) -> None: ...
    def get_canvas_transform(self) -> TransformState: ...
    def get_canvas_node(self) -> PandaNode: ...
    def get_canvas_parent(self) -> PandaNode: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setClipFrame = set_clip_frame
    getClipFrame = get_clip_frame
    hasClipFrame = has_clip_frame
    clearClipFrame = clear_clip_frame
    setCanvasTransform = set_canvas_transform
    getCanvasTransform = get_canvas_transform
    getCanvasNode = get_canvas_node
    getCanvasParent = get_canvas_parent
    getClassType = get_class_type

class PGSliderBar(PGItem):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str = ...) -> None: ...
    def upcast_to_PGItem(self) -> PGItem: ...
    def setup_scroll_bar(self, vertical: bool, length: float, width: float, bevel: float) -> None: ...
    def setup_slider(self, vertical: bool, length: float, width: float, bevel: float) -> None: ...
    def set_axis(self, axis: _Vec3f) -> None: ...
    def get_axis(self) -> LVector3f: ...
    def set_range(self, min_value: float, max_value: float) -> None: ...
    def get_min_value(self) -> float: ...
    def get_max_value(self) -> float: ...
    def set_scroll_size(self, scroll_size: float) -> None: ...
    def get_scroll_size(self) -> float: ...
    def set_page_size(self, page_size: float) -> None: ...
    def get_page_size(self) -> float: ...
    def set_value(self, value: float) -> None: ...
    def get_value(self) -> float: ...
    def set_ratio(self, ratio: float) -> None: ...
    def get_ratio(self) -> float: ...
    def is_button_down(self) -> bool: ...
    def set_resize_thumb(self, resize_thumb: bool) -> None: ...
    def get_resize_thumb(self) -> bool: ...
    def set_manage_pieces(self, manage_pieces: bool) -> None: ...
    def get_manage_pieces(self) -> bool: ...
    def set_thumb_button(self, thumb_button: PGButton) -> None: ...
    def clear_thumb_button(self) -> None: ...
    def get_thumb_button(self) -> PGButton: ...
    def set_left_button(self, left_button: PGButton) -> None: ...
    def clear_left_button(self) -> None: ...
    def get_left_button(self) -> PGButton: ...
    def set_right_button(self, right_button: PGButton) -> None: ...
    def clear_right_button(self) -> None: ...
    def get_right_button(self) -> PGButton: ...
    @staticmethod
    def get_adjust_prefix() -> str: ...
    def get_adjust_event(self) -> str: ...
    def set_active(self, active: bool) -> None: ...
    def remanage(self) -> None: ...
    def recompute(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    setActive = set_active
    getClassType = get_class_type

class PGScrollFrame(PGVirtualFrame):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str = ...) -> None: ...
    def upcast_to_PGVirtualFrame(self) -> PGVirtualFrame: ...
    def setup(self, width: float, height: float, left: float, right: float, bottom: float, top: float, slider_width: float, bevel: float) -> None: ...
    @overload
    def set_virtual_frame(self, virtual_frame: _Vec4f) -> None: ...
    @overload
    def set_virtual_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_virtual_frame(self) -> LVecBase4f: ...
    def has_virtual_frame(self) -> bool: ...
    def clear_virtual_frame(self) -> None: ...
    def set_manage_pieces(self, manage_pieces: bool) -> None: ...
    def get_manage_pieces(self) -> bool: ...
    def set_auto_hide(self, auto_hide: bool) -> None: ...
    def get_auto_hide(self) -> bool: ...
    def set_horizontal_slider(self, horizontal_slider: PGSliderBar) -> None: ...
    def clear_horizontal_slider(self) -> None: ...
    def get_horizontal_slider(self) -> PGSliderBar: ...
    def set_vertical_slider(self, vertical_slider: PGSliderBar) -> None: ...
    def clear_vertical_slider(self) -> None: ...
    def get_vertical_slider(self) -> PGSliderBar: ...
    def remanage(self) -> None: ...
    def recompute(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type

class PGWaitBar(PGItem):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str = ...) -> None: ...
    def setup(self, width: float, height: float, range: float) -> None: ...
    def set_range(self, range: float) -> None: ...
    def get_range(self) -> float: ...
    def set_value(self, value: float) -> None: ...
    def get_value(self) -> float: ...
    def get_percent(self) -> float: ...
    def set_bar_style(self, style: PGFrameStyle) -> None: ...
    def get_bar_style(self) -> PGFrameStyle: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setRange = set_range
    getRange = get_range
    setValue = set_value
    getValue = get_value
    getPercent = get_percent
    setBarStyle = set_bar_style
    getBarStyle = get_bar_style
    getClassType = get_class_type