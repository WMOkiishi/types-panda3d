from collections.abc import Mapping, Sequence
from os import PathLike
from typing import Any, ClassVar, Literal, TypeAlias, overload

_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_Mat4f: TypeAlias = LMatrix4f | UnalignedLMatrix4f
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike
_PartBundle_BlendType: TypeAlias = Literal[0, 1, 2, 3]

class AnimGroup(TypedWritableReferenceCount, Namable):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def children(self) -> Sequence[AnimGroup]: ...
    @overload
    def __init__(self, __param0: AnimGroup) -> None: ...
    @overload
    def __init__(self, parent: AnimGroup, name: str) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def get_num_children(self) -> int: ...
    def get_child(self, n: int) -> AnimGroup: ...
    def get_child_named(self, name: str) -> AnimGroup: ...
    def find_child(self, name: str) -> AnimGroup: ...
    def sort_descendants(self) -> None: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_children(self) -> tuple[AnimGroup, ...]: ...
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToNamable = upcast_to_Namable
    getNumChildren = get_num_children
    getChild = get_child
    getChildNamed = get_child_named
    findChild = find_child
    sortDescendants = sort_descendants
    getClassType = get_class_type
    getChildren = get_children

class AnimBundle(AnimGroup):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def base_frame_rate(self) -> float: ...
    @property
    def num_frames(self) -> int: ...
    @overload
    def __init__(self, __param0: AnimBundle) -> None: ...
    @overload
    def __init__(self, name: str, fps: float, num_frames: int) -> None: ...
    def copy_bundle(self) -> AnimBundle: ...
    def get_base_frame_rate(self) -> float: ...
    def get_num_frames(self) -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    copyBundle = copy_bundle
    getBaseFrameRate = get_base_frame_rate
    getNumFrames = get_num_frames
    getClassType = get_class_type

class AnimBundleNode(PandaNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def bundle(self) -> AnimBundle: ...
    def __init__(self, name: str, bundle: AnimBundle) -> None: ...
    def get_bundle(self) -> AnimBundle: ...
    @staticmethod
    def find_anim_bundle(root: PandaNode) -> AnimBundle: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getBundle = get_bundle
    findAnimBundle = find_anim_bundle
    getClassType = get_class_type

class PartGroup(TypedWritableReferenceCount, Namable):
    DtoolClassDict: ClassVar[dict[str, Any]]
    HMF_ok_part_extra: ClassVar[Literal[1]]
    HMF_ok_anim_extra: ClassVar[Literal[2]]
    HMF_ok_wrong_root_name: ClassVar[Literal[4]]
    @property
    def children(self) -> Sequence[PartGroup]: ...
    def __init__(self, parent: PartGroup, name: str) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def is_character_joint(self) -> bool: ...
    def make_copy(self) -> PartGroup: ...
    def copy_subgraph(self) -> PartGroup: ...
    def get_num_children(self) -> int: ...
    def get_child(self, n: int) -> PartGroup: ...
    def get_child_named(self, name: str) -> PartGroup: ...
    def find_child(self, name: str) -> PartGroup: ...
    def sort_descendants(self) -> None: ...
    def apply_freeze(self, transform: TransformState) -> bool: ...
    def apply_freeze_matrix(self, pos: _Vec3f, hpr: _Vec3f, scale: _Vec3f) -> bool: ...
    def apply_freeze_scalar(self, value: float) -> bool: ...
    def apply_control(self, node: PandaNode) -> bool: ...
    def clear_forced_channel(self) -> bool: ...
    def get_forced_channel(self) -> AnimChannelBase: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    def write_with_value(self, out: ostream, indent_level: int) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_children(self) -> tuple[PartGroup, ...]: ...
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToNamable = upcast_to_Namable
    isCharacterJoint = is_character_joint
    makeCopy = make_copy
    copySubgraph = copy_subgraph
    getNumChildren = get_num_children
    getChild = get_child
    getChildNamed = get_child_named
    findChild = find_child
    sortDescendants = sort_descendants
    applyFreeze = apply_freeze
    applyFreezeMatrix = apply_freeze_matrix
    applyFreezeScalar = apply_freeze_scalar
    applyControl = apply_control
    clearForcedChannel = clear_forced_channel
    getForcedChannel = get_forced_channel
    writeWithValue = write_with_value
    getClassType = get_class_type
    getChildren = get_children
    HMFOkPartExtra = HMF_ok_part_extra
    HMFOkAnimExtra = HMF_ok_anim_extra
    HMFOkWrongRootName = HMF_ok_wrong_root_name

class AnimControl(TypedReferenceCount, AnimInterface, Namable):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def upcast_to_TypedReferenceCount(self) -> TypedReferenceCount: ...
    def upcast_to_AnimInterface(self) -> AnimInterface: ...
    def upcast_to_Namable(self) -> Namable: ...
    def is_pending(self) -> bool: ...
    def wait_pending(self) -> None: ...
    def has_anim(self) -> bool: ...
    def set_pending_done_event(self, done_event: str) -> None: ...
    def get_pending_done_event(self) -> str: ...
    def get_part(self) -> PartBundle: ...
    def get_anim(self) -> AnimBundle: ...
    def get_channel_index(self) -> int: ...
    def get_bound_joints(self) -> BitArray: ...
    def set_anim_model(self, model: PandaNode) -> None: ...
    def get_anim_model(self) -> PandaNode: ...
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToTypedReferenceCount = upcast_to_TypedReferenceCount
    upcastToAnimInterface = upcast_to_AnimInterface
    upcastToNamable = upcast_to_Namable
    isPending = is_pending
    waitPending = wait_pending
    hasAnim = has_anim
    setPendingDoneEvent = set_pending_done_event
    getPendingDoneEvent = get_pending_done_event
    getPart = get_part
    getAnim = get_anim
    getChannelIndex = get_channel_index
    getBoundJoints = get_bound_joints
    setAnimModel = set_anim_model
    getAnimModel = get_anim_model
    getClassType = get_class_type

class AnimChannelBase(AnimGroup):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_type(self) -> TypeHandle: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getType = get_type
    getClassType = get_class_type

class AnimChannel_ACMatrixSwitchType(AnimChannelBase):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_value(self, frame: int, value: _Mat4f) -> None: ...
    def get_value_no_scale_shear(self, frame: int, value: _Mat4f) -> None: ...
    def get_scale(self, frame: int, scale: _Vec3f) -> None: ...
    def get_hpr(self, frame: int, hpr: _Vec3f) -> None: ...
    def get_quat(self, frame: int, quat: _Vec4f) -> None: ...
    def get_pos(self, frame: int, pos: _Vec3f) -> None: ...
    def get_shear(self, frame: int, shear: _Vec3f) -> None: ...
    def get_value_type(self) -> TypeHandle: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getValue = get_value
    getValueNoScaleShear = get_value_no_scale_shear
    getScale = get_scale
    getHpr = get_hpr
    getQuat = get_quat
    getPos = get_pos
    getShear = get_shear
    getValueType = get_value_type
    getClassType = get_class_type

class AnimChannel_ACScalarSwitchType(AnimChannelBase):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_scale(self, frame: int, scale: _Vec3f) -> None: ...
    def get_hpr(self, frame: int, hpr: _Vec3f) -> None: ...
    def get_quat(self, frame: int, quat: _Vec4f) -> None: ...
    def get_pos(self, frame: int, pos: _Vec3f) -> None: ...
    def get_shear(self, frame: int, shear: _Vec3f) -> None: ...
    def get_value_type(self) -> TypeHandle: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getScale = get_scale
    getHpr = get_hpr
    getQuat = get_quat
    getPos = get_pos
    getShear = get_shear
    getValueType = get_value_type
    getClassType = get_class_type

class AnimChannelMatrixDynamic(AnimChannel_ACMatrixSwitchType):
    DtoolClassDict: ClassVar[dict[str, Any]]
    value_node: PandaNode
    def set_value(self, value: TransformState | _Mat4f) -> None: ...
    def set_value_node(self, node: PandaNode) -> None: ...
    def get_value_transform(self) -> TransformState: ...
    def get_value_node(self) -> PandaNode: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setValue = set_value
    setValueNode = set_value_node
    getValueTransform = get_value_transform
    getValueNode = get_value_node
    getClassType = get_class_type

class AnimChannelMatrixXfmTable(AnimChannel_ACMatrixSwitchType):
    DtoolClassDict: ClassVar[dict[str, Any]]
    tables: Mapping[Any, ConstPointerToArray_float]
    def __init__(self, parent: AnimGroup, name: str) -> None: ...
    @staticmethod
    def is_valid_id(table_id: str) -> bool: ...
    def set_table(self, table_id: str, table: ConstPointerToArray_float | PointerToArray_float) -> None: ...
    def get_table(self, table_id: str) -> ConstPointerToArray_float: ...
    def clear_all_tables(self) -> None: ...
    def has_table(self, table_id: str) -> bool: ...
    def clear_table(self, table_id: str) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    isValidId = is_valid_id
    setTable = set_table
    getTable = get_table
    clearAllTables = clear_all_tables
    hasTable = has_table
    clearTable = clear_table
    getClassType = get_class_type

class AnimChannelScalarDynamic(AnimChannel_ACScalarSwitchType):
    DtoolClassDict: ClassVar[dict[str, Any]]
    value: float
    value_node: PandaNode
    def set_value(self, value: float) -> None: ...
    def set_value_node(self, node: PandaNode) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setValue = set_value
    setValueNode = set_value_node
    getClassType = get_class_type

class AnimChannelScalarTable(AnimChannel_ACScalarSwitchType):
    DtoolClassDict: ClassVar[dict[str, Any]]
    table: ConstPointerToArray_float
    def __init__(self, parent: AnimGroup, name: str) -> None: ...
    def set_table(self, table: ConstPointerToArray_float | PointerToArray_float) -> None: ...
    def get_table(self) -> ConstPointerToArray_float: ...
    def has_table(self) -> bool: ...
    def clear_table(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setTable = set_table
    getTable = get_table
    hasTable = has_table
    clearTable = clear_table
    getClassType = get_class_type

class AnimControlCollection:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: AnimControlCollection) -> None: ...
    def store_anim(self, control: AnimControl, name: str) -> None: ...
    def find_anim(self, name: str) -> AnimControl: ...
    def unbind_anim(self, name: str) -> bool: ...
    def get_num_anims(self) -> int: ...
    def get_anim(self, n: int) -> AnimControl: ...
    def get_anim_name(self, n: int) -> str: ...
    def clear_anims(self) -> None: ...
    @overload
    def play(self, anim_name: str) -> bool: ...
    @overload
    def play(self, anim_name: str, _from: float, to: float) -> bool: ...
    @overload
    def loop(self, anim_name: str, restart: bool) -> bool: ...
    @overload
    def loop(self, anim_name: str, restart: bool, _from: float, to: float) -> bool: ...
    def stop(self, anim_name: str) -> bool: ...
    def pose(self, anim_name: str, frame: float) -> bool: ...
    @overload
    def play_all(self) -> None: ...
    @overload
    def play_all(self, _from: float, to: float) -> None: ...
    @overload
    def loop_all(self, restart: bool) -> None: ...
    @overload
    def loop_all(self, restart: bool, _from: float, to: float) -> None: ...
    def stop_all(self) -> bool: ...
    def pose_all(self, frame: float) -> None: ...
    @overload
    def get_frame(self) -> int: ...
    @overload
    def get_frame(self, anim_name: str) -> int: ...
    @overload
    def get_num_frames(self) -> int: ...
    @overload
    def get_num_frames(self, anim_name: str) -> int: ...
    @overload
    def is_playing(self) -> bool: ...
    @overload
    def is_playing(self, anim_name: str) -> bool: ...
    def which_anim_playing(self) -> str: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    def get_anims(self) -> tuple[AnimControl, ...]: ...
    def get_anim_names(self) -> tuple[str, ...]: ...
    storeAnim = store_anim
    findAnim = find_anim
    unbindAnim = unbind_anim
    getNumAnims = get_num_anims
    getAnim = get_anim
    getAnimName = get_anim_name
    clearAnims = clear_anims
    playAll = play_all
    loopAll = loop_all
    stopAll = stop_all
    poseAll = pose_all
    getFrame = get_frame
    getNumFrames = get_num_frames
    isPlaying = is_playing
    whichAnimPlaying = which_anim_playing
    getAnims = get_anims
    getAnimNames = get_anim_names

class AnimPreloadTable(CopyOnWriteObject):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    def get_num_anims(self) -> int: ...
    def find_anim(self, basename: str) -> int: ...
    def get_basename(self, n: int) -> str: ...
    def get_base_frame_rate(self, n: int) -> float: ...
    def get_num_frames(self, n: int) -> int: ...
    def clear_anims(self) -> None: ...
    def remove_anim(self, n: int) -> None: ...
    def add_anim(self, basename: str, base_frame_rate: float, num_frames: int) -> None: ...
    def add_anims_from(self, other: AnimPreloadTable) -> None: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNumAnims = get_num_anims
    findAnim = find_anim
    getBasename = get_basename
    getBaseFrameRate = get_base_frame_rate
    getNumFrames = get_num_frames
    clearAnims = clear_anims
    removeAnim = remove_anim
    addAnim = add_anim
    addAnimsFrom = add_anims_from
    getClassType = get_class_type

class PartSubset:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: PartSubset) -> None: ...
    def assign(self, copy: PartSubset) -> PartSubset: ...
    def add_include_joint(self, name: GlobPattern) -> None: ...
    def add_exclude_joint(self, name: GlobPattern) -> None: ...
    def append(self, other: PartSubset) -> None: ...
    def output(self, out: ostream) -> None: ...
    def is_include_empty(self) -> bool: ...
    def matches_include(self, joint_name: str) -> bool: ...
    def matches_exclude(self, joint_name: str) -> bool: ...
    addIncludeJoint = add_include_joint
    addExcludeJoint = add_exclude_joint
    isIncludeEmpty = is_include_empty
    matchesInclude = matches_include
    matchesExclude = matches_exclude

class BindAnimRequest(ModelLoadRequest):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: BindAnimRequest) -> None: ...
    @overload
    def __init__(self, name: str, filename: _Filename, options: LoaderOptions, loader: Loader, control: AnimControl, hierarchy_match_flags: int, subset: PartSubset) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class PartBundle(PartGroup):
    DtoolClassDict: ClassVar[dict[str, Any]]
    blend_type: _PartBundle_BlendType
    anim_blend_flag: bool
    frame_blend_flag: bool
    root_xform: LMatrix4f
    BT_linear: ClassVar[Literal[0]]
    BT_normalized_linear: ClassVar[Literal[1]]
    BT_componentwise: ClassVar[Literal[2]]
    BT_componentwise_quat: ClassVar[Literal[3]]
    @property
    def nodes(self) -> Sequence[PartBundleNode]: ...
    def __init__(self, name: str = ...) -> None: ...
    def get_anim_preload(self) -> AnimPreloadTable: ...
    def modify_anim_preload(self) -> AnimPreloadTable: ...
    def set_anim_preload(self, table: AnimPreloadTable) -> None: ...
    def clear_anim_preload(self) -> None: ...
    def merge_anim_preloads(self, other: PartBundle) -> None: ...
    def set_blend_type(self, bt: _PartBundle_BlendType) -> None: ...
    def get_blend_type(self) -> _PartBundle_BlendType: ...
    def set_anim_blend_flag(self, anim_blend_flag: bool) -> None: ...
    def get_anim_blend_flag(self) -> bool: ...
    def set_frame_blend_flag(self, frame_blend_flag: bool) -> None: ...
    def get_frame_blend_flag(self) -> bool: ...
    def set_root_xform(self, root_xform: _Mat4f) -> None: ...
    def xform(self, mat: _Mat4f) -> None: ...
    def get_root_xform(self) -> LMatrix4f: ...
    def apply_transform(self, transform: TransformState) -> PartBundle: ...
    def get_num_nodes(self) -> int: ...
    def get_node(self, n: int) -> PartBundleNode: ...
    def clear_control_effects(self) -> None: ...
    def set_control_effect(self, control: AnimControl, effect: float) -> None: ...
    def get_control_effect(self, control: AnimControl) -> float: ...
    def output(self, out: ostream) -> None: ...
    def bind_anim(self, anim: AnimBundle, hierarchy_match_flags: int = ..., subset: PartSubset = ...) -> AnimControl: ...
    def load_bind_anim(self, loader: Loader, filename: _Filename, hierarchy_match_flags: int, subset: PartSubset, allow_async: bool) -> AnimControl: ...
    def wait_pending(self) -> None: ...
    @overload
    def freeze_joint(self, joint_name: str, value: float) -> bool: ...
    @overload
    def freeze_joint(self, joint_name: str, transform: TransformState) -> bool: ...
    @overload
    def freeze_joint(self, joint_name: str, pos: _Vec3f, hpr: _Vec3f, scale: _Vec3f) -> bool: ...
    def control_joint(self, joint_name: str, node: PandaNode) -> bool: ...
    def release_joint(self, joint_name: str) -> bool: ...
    def update(self) -> bool: ...
    def force_update(self) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_nodes(self) -> tuple[PartBundleNode, ...]: ...
    getAnimPreload = get_anim_preload
    modifyAnimPreload = modify_anim_preload
    setAnimPreload = set_anim_preload
    clearAnimPreload = clear_anim_preload
    mergeAnimPreloads = merge_anim_preloads
    setBlendType = set_blend_type
    getBlendType = get_blend_type
    setAnimBlendFlag = set_anim_blend_flag
    getAnimBlendFlag = get_anim_blend_flag
    setFrameBlendFlag = set_frame_blend_flag
    getFrameBlendFlag = get_frame_blend_flag
    setRootXform = set_root_xform
    getRootXform = get_root_xform
    applyTransform = apply_transform
    getNumNodes = get_num_nodes
    getNode = get_node
    clearControlEffects = clear_control_effects
    setControlEffect = set_control_effect
    getControlEffect = get_control_effect
    bindAnim = bind_anim
    loadBindAnim = load_bind_anim
    waitPending = wait_pending
    freezeJoint = freeze_joint
    controlJoint = control_joint
    releaseJoint = release_joint
    forceUpdate = force_update
    getClassType = get_class_type
    getNodes = get_nodes
    BTLinear = BT_linear
    BTNormalizedLinear = BT_normalized_linear
    BTComponentwise = BT_componentwise
    BTComponentwiseQuat = BT_componentwise_quat

class PartBundleNode(PandaNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def bundles(self) -> Sequence[PartBundle]: ...
    @property
    def bundle_handles(self) -> Sequence[PartBundleHandle]: ...
    def __init__(self, name: str, bundle: PartBundle) -> None: ...
    def get_num_bundles(self) -> int: ...
    def get_bundle(self, n: int) -> PartBundle: ...
    def get_bundle_handle(self, n: int) -> PartBundleHandle: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_bundles(self) -> tuple[PartBundle, ...]: ...
    def get_bundle_handles(self) -> tuple[PartBundleHandle, ...]: ...
    getNumBundles = get_num_bundles
    getBundle = get_bundle
    getBundleHandle = get_bundle_handle
    getClassType = get_class_type
    getBundles = get_bundles
    getBundleHandles = get_bundle_handles

class PartBundleHandle(ReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    bundle: PartBundle
    @overload
    def __init__(self, bundle: PartBundle) -> None: ...
    @overload
    def __init__(self, __param0: PartBundleHandle) -> None: ...
    def get_bundle(self) -> PartBundle: ...
    def set_bundle(self, bundle: PartBundle) -> None: ...
    getBundle = get_bundle
    setBundle = set_bundle

class MovingPartBase(PartGroup):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_max_bound(self) -> int: ...
    def get_bound(self, n: int) -> AnimChannelBase: ...
    def output_value(self, out: ostream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getMaxBound = get_max_bound
    getBound = get_bound
    outputValue = output_value
    getClassType = get_class_type

class MovingPartMatrix(MovingPart_ACMatrixSwitchType):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class MovingPart_ACMatrixSwitchType(MovingPartBase):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_value(self) -> LMatrix4f: ...
    def get_default_value(self) -> LMatrix4f: ...
    getClassType = get_class_type
    getValue = get_value
    getDefaultValue = get_default_value

class MovingPartScalar(MovingPart_ACScalarSwitchType):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class MovingPart_ACScalarSwitchType(MovingPartBase):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_value(self) -> float: ...
    def get_default_value(self) -> float: ...
    getClassType = get_class_type
    getValue = get_value
    getDefaultValue = get_default_value

def auto_bind(root_node: PandaNode, controls: AnimControlCollection, hierarchy_match_flags: int = ...) -> None: ...
autoBind = auto_bind
AnimChannelACMatrixSwitchType = AnimChannel_ACMatrixSwitchType
AnimChannelMatrix = AnimChannel_ACMatrixSwitchType
AnimChannelACScalarSwitchType = AnimChannel_ACScalarSwitchType
AnimChannelScalar = AnimChannel_ACScalarSwitchType
MovingPartACMatrixSwitchType = MovingPart_ACMatrixSwitchType
MovingPartACScalarSwitchType = MovingPart_ACScalarSwitchType
