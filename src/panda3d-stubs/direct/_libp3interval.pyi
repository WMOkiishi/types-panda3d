from typing import Any, ClassVar, Literal, TypeAlias, overload
from panda3d.core import (
    AnimControl,
    ConfigVariableColor,
    EventQueue,
    LMatrix3f,
    LMatrix4f,
    LVecBase2f,
    LVecBase3f,
    LVecBase4f,
    NodePath,
    TextureStage,
    TypeHandle,
    TypedReferenceCount,
    UnalignedLVecBase4f,
    ostream,
)

_CInterval_State: TypeAlias = Literal[0, 1, 2, 3]
_CInterval_EventType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_CLerpInterval_BlendType: TypeAlias = Literal[0, 1, 2, 3, 4]
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_CMetaInterval_RelativeStart: TypeAlias = Literal[0, 1, 2]
_CMetaInterval_DefType: TypeAlias = Literal[0, 1, 2, 3]

class CInterval(TypedReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    done_event: str
    t: float
    auto_pause: bool
    auto_finish: bool
    manager: CIntervalManager
    play_rate: float
    ET_initialize: ClassVar[Literal[0]]
    ET_instant: ClassVar[Literal[1]]
    ET_step: ClassVar[Literal[2]]
    ET_finalize: ClassVar[Literal[3]]
    ET_reverse_initialize: ClassVar[Literal[4]]
    ET_reverse_instant: ClassVar[Literal[5]]
    ET_reverse_finalize: ClassVar[Literal[6]]
    ET_interrupt: ClassVar[Literal[7]]
    S_initial: ClassVar[Literal[0]]
    S_started: ClassVar[Literal[1]]
    S_paused: ClassVar[Literal[2]]
    S_final: ClassVar[Literal[3]]
    @property
    def name(self) -> str: ...
    @property
    def duration(self) -> float: ...
    @property
    def open_ended(self) -> bool: ...
    @property
    def state(self) -> _CInterval_State: ...
    @property
    def stopped(self) -> bool: ...
    @property
    def playing(self) -> bool: ...
    def __init__(self, __param0: CInterval) -> None: ...
    def __await__(self) -> Any: ...
    def get_name(self) -> str: ...
    def get_duration(self) -> float: ...
    def get_open_ended(self) -> bool: ...
    def get_state(self) -> _CInterval_State: ...
    def is_stopped(self) -> bool: ...
    def set_done_event(self, event: str) -> None: ...
    def get_done_event(self) -> str: ...
    def set_t(self, t: float) -> None: ...
    def get_t(self) -> float: ...
    def set_auto_pause(self, auto_pause: bool) -> None: ...
    def get_auto_pause(self) -> bool: ...
    def set_auto_finish(self, auto_finish: bool) -> None: ...
    def get_auto_finish(self) -> bool: ...
    def set_wants_t_callback(self, wants_t_callback: bool) -> None: ...
    def get_wants_t_callback(self) -> bool: ...
    def set_manager(self, manager: CIntervalManager) -> None: ...
    def get_manager(self) -> CIntervalManager: ...
    def start(self, start_t: float = ..., end_t: float = ..., play_rate: float = ...) -> None: ...
    def loop(self, start_t: float = ..., end_t: float = ..., play_rate: float = ...) -> None: ...
    def pause(self) -> float: ...
    @overload
    def resume(self) -> None: ...
    @overload
    def resume(self, start_t: float) -> None: ...
    def resume_until(self, end_t: float) -> None: ...
    def finish(self) -> None: ...
    def clear_to_initial(self) -> None: ...
    def is_playing(self) -> bool: ...
    def get_play_rate(self) -> float: ...
    def set_play_rate(self, play_rate: float) -> None: ...
    def priv_do_event(self, t: float, event: _CInterval_EventType) -> None: ...
    def priv_initialize(self, t: float) -> None: ...
    def priv_instant(self) -> None: ...
    def priv_step(self, t: float) -> None: ...
    def priv_finalize(self) -> None: ...
    def priv_reverse_initialize(self, t: float) -> None: ...
    def priv_reverse_instant(self) -> None: ...
    def priv_reverse_finalize(self) -> None: ...
    def priv_interrupt(self) -> None: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    def setup_play(self, start_time: float, end_time: float, play_rate: float, do_loop: bool) -> None: ...
    def setup_resume(self) -> None: ...
    def setup_resume_until(self, end_t: float) -> None: ...
    def step_play(self) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getName = get_name
    getDuration = get_duration
    getOpenEnded = get_open_ended
    getState = get_state
    isStopped = is_stopped
    setDoneEvent = set_done_event
    getDoneEvent = get_done_event
    setT = set_t
    getT = get_t
    setAutoPause = set_auto_pause
    getAutoPause = get_auto_pause
    setAutoFinish = set_auto_finish
    getAutoFinish = get_auto_finish
    setWantsTCallback = set_wants_t_callback
    getWantsTCallback = get_wants_t_callback
    setManager = set_manager
    getManager = get_manager
    resumeUntil = resume_until
    clearToInitial = clear_to_initial
    isPlaying = is_playing
    getPlayRate = get_play_rate
    setPlayRate = set_play_rate
    privDoEvent = priv_do_event
    privInitialize = priv_initialize
    privInstant = priv_instant
    privStep = priv_step
    privFinalize = priv_finalize
    privReverseInitialize = priv_reverse_initialize
    privReverseInstant = priv_reverse_instant
    privReverseFinalize = priv_reverse_finalize
    privInterrupt = priv_interrupt
    setupPlay = setup_play
    setupResume = setup_resume
    setupResumeUntil = setup_resume_until
    stepPlay = step_play
    getClassType = get_class_type
    ETInitialize = ET_initialize
    ETInstant = ET_instant
    ETStep = ET_step
    ETFinalize = ET_finalize
    ETReverseInitialize = ET_reverse_initialize
    ETReverseInstant = ET_reverse_instant
    ETReverseFinalize = ET_reverse_finalize
    ETInterrupt = ET_interrupt
    SInitial = S_initial
    SStarted = S_started
    SPaused = S_paused
    SFinal = S_final

class CIntervalManager:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    def set_event_queue(self, event_queue: EventQueue) -> None: ...
    def get_event_queue(self) -> EventQueue: ...
    def add_c_interval(self, interval: CInterval, external: bool) -> int: ...
    def find_c_interval(self, name: str) -> int: ...
    def get_c_interval(self, index: int) -> CInterval: ...
    def remove_c_interval(self, index: int) -> None: ...
    def interrupt(self) -> int: ...
    def get_num_intervals(self) -> int: ...
    def get_max_index(self) -> int: ...
    def step(self) -> None: ...
    def get_next_event(self) -> int: ...
    def get_next_removal(self) -> int: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    @staticmethod
    def get_global_ptr() -> CIntervalManager: ...
    setEventQueue = set_event_queue
    getEventQueue = get_event_queue
    addCInterval = add_c_interval
    findCInterval = find_c_interval
    getCInterval = get_c_interval
    removeCInterval = remove_c_interval
    getNumIntervals = get_num_intervals
    getMaxIndex = get_max_index
    getNextEvent = get_next_event
    getNextRemoval = get_next_removal
    getGlobalPtr = get_global_ptr

class CConstraintInterval(CInterval):
    DtoolClassDict: ClassVar[dict[str, Any]]
    bogus_variable: bool
    def __init__(self, __param0: CConstraintInterval) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class CConstrainHprInterval(CConstraintInterval):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: CConstrainHprInterval) -> None: ...
    @overload
    def __init__(self, name: str, duration: float, node: NodePath, target: NodePath, wrt: bool, hprOffset: _Vec3f = ...) -> None: ...
    def get_node(self) -> NodePath: ...
    def get_target(self) -> NodePath: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNode = get_node
    getTarget = get_target
    getClassType = get_class_type

class CConstrainPosHprInterval(CConstraintInterval):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: CConstrainPosHprInterval) -> None: ...
    @overload
    def __init__(self, name: str, duration: float, node: NodePath, target: NodePath, wrt: bool, posOffset: _Vec3f = ..., hprOffset: _Vec3f = ...) -> None: ...
    def get_node(self) -> NodePath: ...
    def get_target(self) -> NodePath: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNode = get_node
    getTarget = get_target
    getClassType = get_class_type

class CConstrainPosInterval(CConstraintInterval):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: CConstrainPosInterval) -> None: ...
    @overload
    def __init__(self, name: str, duration: float, node: NodePath, target: NodePath, wrt: bool, posOffset: _Vec3f = ...) -> None: ...
    def get_node(self) -> NodePath: ...
    def get_target(self) -> NodePath: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNode = get_node
    getTarget = get_target
    getClassType = get_class_type

class CConstrainTransformInterval(CConstraintInterval):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: CConstrainTransformInterval) -> None: ...
    @overload
    def __init__(self, name: str, duration: float, node: NodePath, target: NodePath, wrt: bool) -> None: ...
    def get_node(self) -> NodePath: ...
    def get_target(self) -> NodePath: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNode = get_node
    getTarget = get_target
    getClassType = get_class_type

class CLerpInterval(CInterval):
    DtoolClassDict: ClassVar[dict[str, Any]]
    BT_no_blend: ClassVar[Literal[0]]
    BT_ease_in: ClassVar[Literal[1]]
    BT_ease_out: ClassVar[Literal[2]]
    BT_ease_in_out: ClassVar[Literal[3]]
    BT_invalid: ClassVar[Literal[4]]
    def __init__(self, __param0: CLerpInterval) -> None: ...
    def get_blend_type(self) -> _CLerpInterval_BlendType: ...
    @staticmethod
    def string_blend_type(blend_type: str) -> _CLerpInterval_BlendType: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getBlendType = get_blend_type
    stringBlendType = string_blend_type
    getClassType = get_class_type
    BTNoBlend = BT_no_blend
    BTEaseIn = BT_ease_in
    BTEaseOut = BT_ease_out
    BTEaseInOut = BT_ease_in_out
    BTInvalid = BT_invalid

class CLerpAnimEffectInterval(CLerpInterval):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: CLerpAnimEffectInterval) -> None: ...
    @overload
    def __init__(self, name: str, duration: float, blend_type: _CLerpInterval_BlendType) -> None: ...
    def add_control(self, control: AnimControl, name: str, begin_effect: float, end_effect: float) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    addControl = add_control
    getClassType = get_class_type

class CLerpNodePathInterval(CLerpInterval):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: CLerpNodePathInterval) -> None: ...
    @overload
    def __init__(self, name: str, duration: float, blend_type: _CLerpInterval_BlendType, bake_in_start: bool, fluid: bool, node: NodePath, other: NodePath) -> None: ...
    def get_node(self) -> NodePath: ...
    def get_other(self) -> NodePath: ...
    def set_start_pos(self, pos: _Vec3f) -> None: ...
    def set_end_pos(self, pos: _Vec3f) -> None: ...
    def set_start_hpr(self, hpr: _Vec3f) -> None: ...
    @overload
    def set_end_hpr(self, quat: _Vec4f) -> None: ...
    @overload
    def set_end_hpr(self, hpr: _Vec3f) -> None: ...
    def set_start_quat(self, quat: _Vec4f) -> None: ...
    @overload
    def set_end_quat(self, quat: _Vec4f) -> None: ...
    @overload
    def set_end_quat(self, hpr: _Vec3f) -> None: ...
    def set_start_scale(self, scale: _Vec3f | float) -> None: ...
    def set_end_scale(self, scale: _Vec3f | float) -> None: ...
    def set_start_shear(self, shear: _Vec3f) -> None: ...
    def set_end_shear(self, shear: _Vec3f) -> None: ...
    def set_start_color(self, color: _Vec4f) -> None: ...
    def set_end_color(self, color: _Vec4f) -> None: ...
    def set_start_color_scale(self, color_scale: _Vec4f) -> None: ...
    def set_end_color_scale(self, color_scale: _Vec4f) -> None: ...
    def set_texture_stage(self, stage: TextureStage) -> None: ...
    def set_start_tex_offset(self, tex_offset: LVecBase2f) -> None: ...
    def set_end_tex_offset(self, tex_offset: LVecBase2f) -> None: ...
    def set_start_tex_rotate(self, tex_rotate: float) -> None: ...
    def set_end_tex_rotate(self, tex_rotate: float) -> None: ...
    def set_start_tex_scale(self, tex_scale: LVecBase2f) -> None: ...
    def set_end_tex_scale(self, tex_scale: LVecBase2f) -> None: ...
    def set_override(self, override: int) -> None: ...
    def get_override(self) -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNode = get_node
    getOther = get_other
    setStartPos = set_start_pos
    setEndPos = set_end_pos
    setStartHpr = set_start_hpr
    setEndHpr = set_end_hpr
    setStartQuat = set_start_quat
    setEndQuat = set_end_quat
    setStartScale = set_start_scale
    setEndScale = set_end_scale
    setStartShear = set_start_shear
    setEndShear = set_end_shear
    setStartColor = set_start_color
    setEndColor = set_end_color
    setStartColorScale = set_start_color_scale
    setEndColorScale = set_end_color_scale
    setTextureStage = set_texture_stage
    setStartTexOffset = set_start_tex_offset
    setEndTexOffset = set_end_tex_offset
    setStartTexRotate = set_start_tex_rotate
    setEndTexRotate = set_end_tex_rotate
    setStartTexScale = set_start_tex_scale
    setEndTexScale = set_end_tex_scale
    setOverride = set_override
    getOverride = get_override
    getClassType = get_class_type

class CMetaInterval(CInterval):
    DtoolClassDict: ClassVar[dict[str, Any]]
    RS_previous_end: ClassVar[Literal[0]]
    RS_previous_begin: ClassVar[Literal[1]]
    RS_level_begin: ClassVar[Literal[2]]
    DT_c_interval: ClassVar[Literal[0]]
    DT_ext_index: ClassVar[Literal[1]]
    DT_push_level: ClassVar[Literal[2]]
    DT_pop_level: ClassVar[Literal[3]]
    @overload
    def __init__(self, __param0: CMetaInterval) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def set_precision(self, precision: float) -> None: ...
    def get_precision(self) -> float: ...
    def clear_intervals(self) -> None: ...
    def push_level(self, name: str, rel_time: float, rel_to: _CMetaInterval_RelativeStart) -> int: ...
    def add_c_interval(self, c_interval: CInterval, rel_time: float = ..., rel_to: _CMetaInterval_RelativeStart = ...) -> int: ...
    def add_ext_index(self, ext_index: int, name: str, duration: float, open_ended: bool, rel_time: float, rel_to: _CMetaInterval_RelativeStart) -> int: ...
    def pop_level(self, duration: float = ...) -> int: ...
    def set_interval_start_time(self, name: str, rel_time: float, rel_to: _CMetaInterval_RelativeStart = ...) -> bool: ...
    def get_interval_start_time(self, name: str) -> float: ...
    def get_interval_end_time(self, name: str) -> float: ...
    def get_num_defs(self) -> int: ...
    def get_def_type(self, n: int) -> _CMetaInterval_DefType: ...
    def get_c_interval(self, n: int) -> CInterval: ...
    def get_ext_index(self, n: int) -> int: ...
    def is_event_ready(self) -> bool: ...
    def get_event_index(self) -> int: ...
    def get_event_t(self) -> float: ...
    def get_event_type(self) -> _CInterval_EventType: ...
    def pop_event(self) -> None: ...
    def timeline(self, out: ostream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setPrecision = set_precision
    getPrecision = get_precision
    clearIntervals = clear_intervals
    pushLevel = push_level
    addCInterval = add_c_interval
    addExtIndex = add_ext_index
    popLevel = pop_level
    setIntervalStartTime = set_interval_start_time
    getIntervalStartTime = get_interval_start_time
    getIntervalEndTime = get_interval_end_time
    getNumDefs = get_num_defs
    getDefType = get_def_type
    getCInterval = get_c_interval
    getExtIndex = get_ext_index
    isEventReady = is_event_ready
    getEventIndex = get_event_index
    getEventT = get_event_t
    getEventType = get_event_type
    popEvent = pop_event
    getClassType = get_class_type
    RSPreviousEnd = RS_previous_end
    RSPreviousBegin = RS_previous_begin
    RSLevelBegin = RS_level_begin
    DTCInterval = DT_c_interval
    DTExtIndex = DT_ext_index
    DTPushLevel = DT_push_level
    DTPopLevel = DT_pop_level

class HideInterval(CInterval):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: HideInterval) -> None: ...
    @overload
    def __init__(self, node: NodePath, name: str = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class LerpBlendType(TypedReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __call__(self, __param0: float) -> float: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class EaseInBlendType(LerpBlendType):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class EaseOutBlendType(LerpBlendType):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class EaseInOutBlendType(LerpBlendType):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class NoBlendType(LerpBlendType):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class ShowInterval(CInterval):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: ShowInterval) -> None: ...
    @overload
    def __init__(self, node: NodePath, name: str = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class WaitInterval(CInterval):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: WaitInterval) -> None: ...
    @overload
    def __init__(self, duration: float) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type