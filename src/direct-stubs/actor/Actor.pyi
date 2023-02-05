__all__ = ['Actor']

from _typeshed import StrOrBytesPath
from collections.abc import Iterable, Mapping
from typing import ClassVar, SupportsFloat
from typing_extensions import Literal, TypeAlias

from direct.directnotify.Notifier import Notifier
from direct.interval.ActorInterval import ActorInterval
from direct.showbase.DirectObject import DirectObject
from direct.tkpanels.AnimPanel import AnimPanel
from panda3d._typing import Vec3Like
from panda3d.core import (
    AnimBundle,
    AnimControl,
    AnimGroup,
    Character,
    ConfigVariableBool,
    GeomNode,
    LMatrix4f,
    Loader,
    LoaderOptions,
    LODNode,
    ModelNode,
    NodePath,
    PandaNode,
    PartBundle,
    PartBundleHandle,
    PartSubset,
    TransformState,
)

_BlendType: TypeAlias = Literal[0, 1, 2, 3]
_NodePathOrFilepath: TypeAlias = NodePath[PandaNode] | StrOrBytesPath

class Actor(DirectObject, NodePath):
    notify: ClassVar[Notifier]
    partPrefix: ClassVar[str]
    modelLoaderOptions: ClassVar[LoaderOptions]
    animLoaderOptions: ClassVar[LoaderOptions]
    validateSubparts: ClassVar[ConfigVariableBool]
    mergeLODBundles: ConfigVariableBool | bool
    allowAsyncBind: ConfigVariableBool | bool
    Actor_initialized: Literal[1]
    Actor_deleted: Literal[1]
    loader: Loader
    switches: dict[str, tuple[float, float]] | None
    gotName: bool

    class PartDef:
        partBundleNP: NodePath[Character]
        partBundleHandle: PartBundleHandle
        partModel: PandaNode
        def __init__(
            self, partBundleNP: NodePath[Character], partBundleHandle: PartBundleHandle, partModel: PandaNode
        ) -> None: ...
        def get_bundle(self) -> PartBundle: ...
        getBundle = get_bundle

    class AnimDef:
        filename: str | None
        animBundle: AnimBundle | None
        animControl: AnimControl
        def __init__(self, filename: str | None = None, animBundle: AnimBundle | None = None) -> None: ...
        def make_copy(self) -> Actor.AnimDef: ...
        makeCopy = make_copy

    class SubpartDef:
        truePartName: str
        subset: PartSubset
        def __init__(self, truePartName: str, subset: PartSubset = ...) -> None: ...
        def makeCopy(self) -> Actor.SubpartDef: ...

    def __init__(
        self,
        models: dict[str, dict[str, _NodePathOrFilepath] | _NodePathOrFilepath] | _NodePathOrFilepath | None = None,
        anims: dict[str, Mapping[str, str]] | Mapping[str, str] | None = None,
        other: Actor | None = None,
        copy: bool = True,
        lodNode: LODNode | None = None,
        flattenable: bool = True,
        setFinal: bool = False,
        mergeLODBundles: bool | None = None,
        allowAsyncBind: bool | None = None,
        okMissing: bool | None = None,
    ) -> None: ...
    def delete(self) -> None: ...
    def copy_actor(self, other: Actor, overwrite: bool = False) -> None: ...
    def __cmp__(self, other: object) -> Literal[0, 1]: ...
    def list_joints(self, partName: str = 'modelRoot', lodName: str = 'lodRoot') -> None: ...
    def get_actor_info(self) -> list[tuple[str, list[tuple[str, PartBundle, list[tuple[str, str, AnimControl]]]]]]: ...
    def get_anim_names(self) -> list[str]: ...
    def pprint(self) -> None: ...
    def cleanup(self) -> None: ...
    def remove_node(self) -> None: ...  # type: ignore[override]
    def clear_python_data(self) -> None: ...
    def flush(self) -> None: ...
    def get_anim_control_dict(self) -> dict[str, dict[str, dict[str, Actor.AnimDef]]]: ...
    def remove_anim_control_dict(self) -> None: ...
    def get_part_bundle_dict(self) -> dict[str, dict[str, Actor.PartDef]]: ...
    def get_part_bundles(self, partName: str | None = None) -> list[PartBundle]: ...
    def get_lod_names(self) -> list[str]: ...
    def get_part_names(self) -> list[str]: ...
    def get_geom_node(self) -> GeomNode: ...
    def set_geom_node(self, node: GeomNode) -> None: ...
    def get_lod_node(self) -> LODNode: ...
    def set_lod_node(self, node: LODNode | None = None) -> None: ...
    def use_lod(self, lodName: object) -> None: ...
    def print_lod(self) -> None: ...
    def reset_lod(self) -> None: ...
    def add_lod(self, lodName: str, inDist: float = 0, outDist: float = 0, center: Vec3Like | None = None) -> None: ...
    def set_lod(self, lodName: str, inDist: float = 0, outDist: float = 0) -> None: ...
    def get_lod_index(self, lodName: str) -> int: ...
    def get_lod(self, lodName: str) -> NodePath | None: ...
    def has_lod(self) -> bool: ...
    def set_center(self, center: Vec3Like | None) -> None: ...
    def set_lod_animation(self, farDistance: float, nearDistance: float, delayFactor: float) -> None: ...
    def clear_lod_animation(self) -> None: ...
    def update(self, lod: int = 0, partName: str | None = None, lodName: str | None = None, force: bool = False) -> bool: ...
    def get_frame_rate(self, animName: str | None = None, partName: str | None = None) -> float: ...
    def get_base_frame_rate(self, animName: str | None = None, partName: str | None = None) -> float: ...
    def get_play_rate(self, animName: str | None = None, partName: str | None = None) -> float: ...
    def set_play_rate(self, rate: float, animName: str, partName: str | None = None) -> None: ...
    def get_duration(
        self,
        animName: str | None = None,
        partName: str | None = None,
        fromFrame: float | None = None,
        toFrame: float | None = None,
    ) -> float | None: ...
    def get_num_frames(self, animName: str | None = None, partName: str | None = None) -> int: ...
    def get_frame_time(self, anim: str | None, frame: SupportsFloat, partName: str | None = None) -> float: ...
    def get_current_anim(self, partName: str | None = None) -> str | None: ...
    def get_current_frame(self, animName: str | None = None, partName: str | None = None) -> int: ...
    def get_part(self, partName: str, lodName: str = 'lodRoot') -> NodePath[Character]: ...
    def get_part_bundle(self, partName: str, lodName: str = 'lodRoot') -> PartBundle | None: ...
    def remove_part(self, partName: str, lodName: str = 'lodRoot') -> None: ...
    def hide_part(self, partName: str, lodName: str = 'lodRoot') -> None: ...
    def show_part(self, partName: str, lodName: str = 'lodRoot') -> None: ...
    def show_all_parts(self, partName: str, lodName: str = 'lodRoot') -> None: ...
    def expose_joint(
        self, node: NodePath, partName: str, jointName: str, lodName: str = 'lodRoot', localTransform: bool = ...
    ) -> NodePath | None: ...
    def stop_joint(self, partName: str, jointName: str, lodName: str = 'lodRoot') -> None: ...
    def get_joints(self, partName: str | None = None, jointName: str = '*', lodName: str | None = None) -> list[AnimGroup]: ...
    def get_overlapping_joints(
        self, partNameA: str, partNameB: str, jointName: str = '*', lodName: str | None = None
    ) -> set[AnimGroup]: ...
    def get_joint_transform(self, partName: str, jointName: str, lodName: str = 'lodRoot') -> LMatrix4f | None: ...
    def get_joint_transform_state(self, partName: str, jointName: str, lodName: str = 'lodRoot') -> TransformState | None: ...
    def control_joint(
        self, node: NodePath | None, partName: str, jointName: str, lodName: str = 'lodRoot'
    ) -> NodePath[ModelNode]: ...
    def freeze_joint(
        self,
        partName: str,
        jointName: str,
        transform: TransformState | None = None,
        pos: Vec3Like = ...,
        hpr: Vec3Like = ...,
        scale: Vec3Like = ...,
    ) -> None: ...
    def release_joint(self, partName: str, jointName: str) -> None: ...
    def instance(self, path: NodePath, partName: str, jointName: str, lodName: str = 'lodRoot') -> None: ...
    def attach(self, partName: str, anotherPartName: str, jointName: str, lodName: str = 'lodRoot') -> None: ...
    def draw_in_front(
        self, frontPartName: str, backPartName: str, mode: int, root: NodePath | None = None, lodName: str | None = None
    ) -> None: ...
    def fix_bounds(self, partName: str | None = None) -> None: ...
    def fix_bounds_old(self, part: NodePath | None = None) -> None: ...
    def show_all_bounds(self) -> None: ...
    def hide_all_bounds(self) -> None: ...
    def anim_panel(self) -> AnimPanel: ...
    def stop(self, animName: str | None = None, partName: str | None = None) -> None: ...
    def play(
        self, animName: str | None, partName: str | None = None, fromFrame: float | None = None, toFrame: float | None = None
    ) -> None: ...
    def loop(
        self,
        animName: str,
        restart: bool = ...,
        partName: str | None = None,
        fromFrame: float | None = None,
        toFrame: float | None = None,
    ) -> None: ...
    def pingpong(
        self,
        animName: str,
        restart: bool = ...,
        partName: str | None = None,
        fromFrame: float | None = None,
        toFrame: float | None = None,
    ) -> None: ...
    def pose(self, animName: str, frame: int, partName: str | None = None, lodName: str | None = None) -> None: ...
    def set_blend(
        self,
        animBlend: bool | None = None,
        frameBlend: bool | None = None,
        blendType: _BlendType | None = None,
        partName: str | None = None,
    ) -> None: ...
    def enable_blend(self, blendType: _BlendType = 1, partName: str | None = None) -> None: ...
    def disable_blend(self, partName: str | None = None) -> None: ...
    def set_control_effect(
        self, animName: str, effect: float, partName: str | None = None, lodName: str | None = None
    ) -> None: ...
    def get_anim_filename(self, animName: str, partName: str = 'modelRoot') -> str | None: ...
    def get_anim_control(
        self, animName: str, partName: str | None = None, lodName: str | None = None, allowAsyncBind: bool = True
    ) -> AnimControl | None: ...
    def get_anim_controls(
        self, animName: str | None = None, partName: str | None = None, lodName: str | None = None, allowAsyncBind: bool = True
    ) -> list[AnimControl]: ...
    def load_model(
        self,
        modelPath: _NodePathOrFilepath,
        partName: str = 'modelRoot',
        lodName: str = 'lodRoot',
        copy: bool = True,
        okMissing: bool | None = None,
        autoBindAnims: bool = True,
    ) -> None: ...
    def make_subpart(
        self,
        partName: str,
        includeJoints: Iterable[str],
        excludeJoints: Iterable[str] = ...,
        parent: str = 'modelRoot',
        overlapping: bool = False,
    ) -> None: ...
    def set_subparts_complete(self, flag: bool) -> None: ...
    def get_subparts_complete(self) -> bool: ...
    def verify_subparts_complete(self, partName: str | None = None, lodName: str | None = None) -> None: ...
    def load_anims(self, anims: Mapping[str, str], partName: str = 'modelRoot', lodName: str = 'lodRoot') -> None: ...
    def init_anims_on_all_lods(self, partNames: Iterable[str]) -> None: ...
    def load_anims_on_all_lods(self, anims: Mapping[str, str], partName: str = 'modelRoot') -> None: ...
    def post_flatten(self) -> None: ...
    def unload_anims(
        self, anims: Iterable[str] | None = None, partName: str | None = None, lodName: str | None = None
    ) -> None: ...
    def bind_anim(
        self, animName: str, partName: str | None = None, lodName: str | None = None, allowAsyncBind: bool = False
    ) -> None: ...
    def bind_all_anims(self, allowAsyncBind: bool = False) -> None: ...
    def wait_pending(self, partName: str | None = None) -> None: ...
    def actor_interval(
        self,
        animName: str,
        loop: bool = ...,
        constrainedLoop: bool = ...,
        duration: float | None = ...,
        startTime: float | None = ...,
        endTime: float | None = ...,
        startFrame: float | None = ...,
        endFrame: float | None = ...,
        playRate: float = ...,
        name: str | None = ...,
        forceUpdate: bool = ...,
        partName: str | None = ...,
        lodName: str | None = ...,
    ) -> ActorInterval: ...
    def get_anim_blends(
        self, animName: str | None = None, partName: str | None = None, lodName: str | None = None
    ) -> list[tuple[str, list[tuple[str, list[tuple[str, float]]]]]]: ...
    def print_anim_blends(self, animName: str | None = None, partName: str | None = None, lodName: str | None = None) -> None: ...
    def osd_anim_blends(self, animName: str | None = None, partName: str | None = None, lodName: str | None = None) -> None: ...
    def face_away_from_viewer(self) -> None: ...
    def face_towards_viewer(self) -> None: ...
    def rename_part_bundles(self, partName: str, newBundleName: str) -> None: ...
    copyActor = copy_actor
    listJoints = list_joints
    getActorInfo = get_actor_info
    getAnimNames = get_anim_names
    removeNode = remove_node  # type: ignore[assignment]
    clearPythonData = clear_python_data
    getAnimControlDict = get_anim_control_dict
    removeAnimControlDict = remove_anim_control_dict
    getPartBundleDict = get_part_bundle_dict
    getPartBundles = get_part_bundles
    getLODNames = get_lod_names
    getPartNames = get_part_names
    getGeomNode = get_geom_node
    setGeomNode = set_geom_node
    getLODNode = get_lod_node
    setLODNode = set_lod_node
    useLOD = use_lod
    printLOD = print_lod
    resetLOD = reset_lod
    addLOD = add_lod
    setLOD = set_lod
    getLODIndex = get_lod_index
    getLOD = get_lod
    hasLOD = has_lod
    setCenter = set_center
    setLODAnimation = set_lod_animation
    clearLODAnimation = clear_lod_animation
    getFrameRate = get_frame_rate
    getBaseFrameRate = get_base_frame_rate
    getPlayRate = get_play_rate
    setPlayRate = set_play_rate
    getDuration = get_duration
    getNumFrames = get_num_frames
    getFrameTime = get_frame_time
    getCurrentAnim = get_current_anim
    getCurrentFrame = get_current_frame
    getPart = get_part
    getPartBundle = get_part_bundle
    removePart = remove_part
    hidePart = hide_part
    showPart = show_part
    showAllParts = show_all_parts
    exposeJoint = expose_joint
    stopJoint = stop_joint
    getJoints = get_joints
    getOverlappingJoints = get_overlapping_joints
    getJointTransform = get_joint_transform
    getJointTransformState = get_joint_transform_state
    controlJoint = control_joint
    freezeJoint = freeze_joint
    releaseJoint = release_joint
    drawInFront = draw_in_front
    fixBounds = fix_bounds
    fixBounds_old = fix_bounds_old
    showAllBounds = show_all_bounds
    hideAllBounds = hide_all_bounds
    animPanel = anim_panel
    setBlend = set_blend
    enableBlend = enable_blend
    disableBlend = disable_blend
    setControlEffect = set_control_effect
    getAnimFilename = get_anim_filename
    getAnimControl = get_anim_control
    getAnimControls = get_anim_controls
    loadModel = load_model
    makeSubpart = make_subpart
    setSubpartsComplete = set_subparts_complete
    getSubpartsComplete = get_subparts_complete
    verifySubpartsComplete = verify_subparts_complete
    loadAnims = load_anims
    initAnimsOnAllLODs = init_anims_on_all_lods
    loadAnimsOnAllLODs = load_anims_on_all_lods
    postFlatten = post_flatten
    unloadAnims = unload_anims
    bindAnim = bind_anim
    bindAllAnims = bind_all_anims
    waitPending = wait_pending
    actorInterval = actor_interval
    getAnimBlends = get_anim_blends
    printAnimBlends = print_anim_blends
    osdAnimBlends = osd_anim_blends
    faceAwayFromViewer = face_away_from_viewer
    faceTowardsViewer = face_towards_viewer
    renamePartBundles = rename_part_bundles
