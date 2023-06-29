from _typeshed import StrOrBytesPath
from collections.abc import MutableMapping, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import Mat4Like, Vec3Like, Vec4Like
from panda3d.core._dtoolbase import TypeHandle
from panda3d.core._dtoolutil import GlobPattern, ostream
from panda3d.core._express import CPTA_stdfloat, Namable, PointerToArray_float, ReferenceCount, TypedReferenceCount
from panda3d.core._linmath import LMatrix4
from panda3d.core._pgraph import Loader, ModelLoadRequest, PandaNode, TransformState
from panda3d.core._putil import AnimInterface, BitArray, CopyOnWriteObject, LoaderOptions, TypedWritableReferenceCount

_PartBundle_BlendType: TypeAlias = Literal[0, 1, 2, 3]

class AnimGroup(TypedWritableReferenceCount, Namable):
    """This is the base class for AnimChannel and AnimBundle.  It implements a
    hierarchy of AnimChannels.  The root of the hierarchy must be an
    AnimBundle.
    """

    @property
    def children(self) -> Sequence[AnimGroup]: ...
    @overload
    def __init__(self, __param0: AnimGroup) -> None:
        """Creates the AnimGroup, and adds it to the indicated parent.  The only way
        to delete it subsequently is to delete the entire hierarchy.
        """
    @overload
    def __init__(self, parent: AnimGroup, name: str) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def get_num_children(self) -> int:
        """Returns the number of child nodes of the group."""
    def get_child(self, n: int) -> AnimGroup:
        """Returns the nth child of the group."""
    def get_child_named(self, name: str) -> AnimGroup:
        """Returns the first child found with the indicated name, or NULL if no such
        child exists.  This method searches only the children of this particular
        AnimGroup; it does not recursively search the entire graph.  See also
        find_child().
        """
    def find_child(self, name: str) -> AnimGroup:
        """Returns the first descendant found with the indicated name, or NULL if no
        such descendant exists.  This method searches the entire graph beginning at
        this AnimGroup; see also get_child_named().
        """
    def sort_descendants(self) -> None:
        """Sorts the children nodes at each level of the hierarchy into alphabetical
        order.  This should be done after creating the hierarchy, to guarantee that
        the correct names will match up together when the AnimBundle is later bound
        to a PlayerRoot.
        """
    def output(self, out: ostream) -> None:
        """Writes a one-line description of the group."""
    def write(self, out: ostream, indent_level: int) -> None:
        """Writes a brief description of the group and all of its descendants."""
    def get_children(self) -> tuple[AnimGroup, ...]: ...
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToNamable = upcast_to_Namable
    getNumChildren = get_num_children
    getChild = get_child
    getChildNamed = get_child_named
    findChild = find_child
    sortDescendants = sort_descendants
    getChildren = get_children

class AnimBundle(AnimGroup):
    """This is the root of an AnimChannel hierarchy.  It knows the frame rate and
    number of frames of all the channels in the hierarchy (which must all
    match).
    """

    @property
    def base_frame_rate(self) -> float: ...
    @property
    def num_frames(self) -> int: ...
    @overload
    def __init__(self, __param0: AnimBundle) -> None: ...
    @overload
    def __init__(self, name: str, fps: float, num_frames: int) -> None: ...
    def copy_bundle(self) -> AnimBundle:
        """Returns a full copy of the bundle and its entire tree of nested AnimGroups.
        However, the actual data stored in the leaves--that is, animation tables,
        such as those stored in an AnimChannelMatrixXfmTable--will be shared.
        """
    def get_base_frame_rate(self) -> float:
        """Returns the ideal number of frames per second of the animation, when it is
        running at normal speed.  This may not be the same as the actual playing
        frame rate, as it might have been adjusted through set_play_rate() on the
        AnimControl object.  See AnimControl::get_effective_frame_rate().
        """
    def get_num_frames(self) -> int:
        """Returns the number of frames of animation, or 0 if the animation has no
        fixed number of frames.
        """
    copyBundle = copy_bundle
    getBaseFrameRate = get_base_frame_rate
    getNumFrames = get_num_frames

class AnimBundleNode(PandaNode):
    """This is a node that contains a pointer to an AnimBundle.  Like
    PartBundleNode, it exists solely to make it easy to store AnimBundles in
    the scene graph.
    """

    @property
    def bundle(self) -> AnimBundle: ...
    def __init__(self, name: str, bundle: AnimBundle) -> None:
        """The AnimBundle and its node should be constructed together.  Generally, the
        derived classes of AnimBundleNode will automatically create a AnimBundle of
        the appropriate type, and pass it up to this constructor.
        """
    def get_bundle(self) -> AnimBundle: ...
    @staticmethod
    def find_anim_bundle(root: PandaNode) -> AnimBundle:
        """Recursively walks the scene graph beginning at the indicated node (which
        need not be an AnimBundleNode), and returns the first AnimBundle found.
        Returns NULL if no AnimBundle can be found.
        """
    getBundle = get_bundle
    findAnimBundle = find_anim_bundle

class PartGroup(TypedWritableReferenceCount, Namable):
    """This is the base class for PartRoot and MovingPart.  It defines a hierarchy
    of MovingParts.
    """

    HMF_ok_part_extra: Final = 1
    HMFOkPartExtra: Final = 1
    HMF_ok_anim_extra: Final = 2
    HMFOkAnimExtra: Final = 2
    HMF_ok_wrong_root_name: Final = 4
    HMFOkWrongRootName: Final = 4
    @property
    def children(self) -> Sequence[PartGroup]: ...
    def __init__(self, parent: PartGroup, name: str) -> None:
        """Creates the PartGroup, and adds it to the indicated parent.  The only way
        to delete it subsequently is to delete the entire hierarchy.
        """
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def is_character_joint(self) -> bool:
        """Returns true if this part is a CharacterJoint, false otherwise.  This is a
        tiny optimization over is_of_type(CharacterType::get_class_type()).
        """
    def make_copy(self) -> PartGroup:
        """Allocates and returns a new copy of the node.  Children are not copied, but
        see copy_subgraph().
        """
    def copy_subgraph(self) -> PartGroup:
        """Allocates and returns a new copy of this node and of all of its children."""
    def get_num_children(self) -> int:
        """Returns the number of child nodes of the group."""
    def get_child(self, n: int) -> PartGroup:
        """Returns the nth child of the group."""
    def get_child_named(self, name: str) -> PartGroup:
        """Returns the first child found with the indicated name, or NULL if no such
        child exists.  This method searches only the children of this particular
        PartGroup; it does not recursively search the entire graph.  See also
        find_child().
        """
    def find_child(self, name: str) -> PartGroup:
        """Returns the first descendant found with the indicated name, or NULL if no
        such descendant exists.  This method searches the entire graph beginning at
        this PartGroup; see also get_child_named().
        """
    def sort_descendants(self) -> None:
        """Sorts the children nodes at each level of the hierarchy into alphabetical
        order.  This should be done after creating the hierarchy, to guarantee that
        the correct names will match up together when the AnimBundle is later bound
        to a PlayerRoot.
        """
    def apply_freeze(self, transform: TransformState) -> bool:
        """Freezes this particular joint so that it will always hold the specified
        transform.  Returns true if this is a joint that can be so frozen, false
        otherwise.

        This is normally only called internally by PartBundle::freeze_joint(), but
        you may also call it directly.
        """
    def apply_freeze_matrix(self, pos: Vec3Like, hpr: Vec3Like, scale: Vec3Like) -> bool:
        """Freezes this particular joint so that it will always hold the specified
        transform.  Returns true if this is a joint that can be so frozen, false
        otherwise.

        This is normally only called internally by PartBundle::freeze_joint(), but
        you may also call it directly.
        """
    def apply_freeze_scalar(self, value: float) -> bool:
        """Freezes this particular joint so that it will always hold the specified
        transform.  Returns true if this is a joint that can be so frozen, false
        otherwise.

        This is normally only called internally by PartBundle::freeze_joint(), but
        you may also call it directly.
        """
    def apply_control(self, node: PandaNode) -> bool:
        """Specifies a node to influence this particular joint so that it will always
        hold the node's transform.  Returns true if this is a joint that can be so
        controlled, false otherwise.

        This is normally only called internally by PartBundle::control_joint(), but
        you may also call it directly.
        """
    def clear_forced_channel(self) -> bool:
        """Undoes the effect of a previous call to apply_freeze() or apply_control().
        Returns true if the joint was modified, false otherwise.

        This is normally only called internally by PartBundle::release_joint(), but
        you may also call it directly.
        """
    def get_forced_channel(self) -> AnimChannelBase:
        """Returns the AnimChannelBase that has been forced to this joint by a
        previous call to apply_freeze() or apply_control(), or NULL if no such
        channel has been applied.
        """
    def write(self, out: ostream, indent_level: int) -> None:
        """Writes a brief description of the group and all of its descendants."""
    def write_with_value(self, out: ostream, indent_level: int) -> None:
        """Writes a brief description of the group, showing its current value, and
        that of all of its descendants.
        """
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
    getChildren = get_children

class AnimControl(TypedReferenceCount, AnimInterface, Namable):
    """Controls the timing of a character animation.  An AnimControl object is
    created for each character/bundle binding and manages the state of the
    animation: whether started, stopped, or looping, and the current frame
    number and play rate.
    """

    def upcast_to_TypedReferenceCount(self) -> TypedReferenceCount: ...
    def upcast_to_AnimInterface(self) -> AnimInterface: ...
    def upcast_to_Namable(self) -> Namable: ...
    def is_pending(self) -> bool:
        """Returns true if the AnimControl is being bound asynchronously, and has not
        yet finished.  If this is true, the AnimControl's interface is still
        available and will be perfectly useful (though get_anim() might return
        NULL), but nothing visible will happen immediately.
        """
    def wait_pending(self) -> None:
        """Blocks the current thread until the AnimControl has finished loading and is
        fully bound.
        """
    def has_anim(self) -> bool:
        """Returns true if the AnimControl was successfully loaded, or false if there
        was a problem.  This may return false while is_pending() is true.
        """
    def set_pending_done_event(self, done_event: str) -> None:
        """Specifies an event name that will be thrown when the AnimControl is
        finished binding asynchronously.  If the AnimControl has already finished
        binding, the event will be thrown immediately.
        """
    def get_pending_done_event(self) -> str:
        """Returns the event name that will be thrown when the AnimControl is finished
        binding asynchronously.
        """
    def get_part(self) -> PartBundle:
        """Returns the PartBundle bound in with this AnimControl."""
    def get_anim(self) -> AnimBundle:
        """Returns the AnimBundle bound in with this AnimControl."""
    def get_channel_index(self) -> int:
        """Returns the particular channel index associated with this AnimControl.
        This channel index is the slot on which each AnimGroup is bound to its
        associated PartGroup, for each joint in the animation.

        It will be true that
        get_part()->find_child("n")->get_bound(get_channel_index()) ==
        get_anim()->find_child("n"), for each joint "n".
        """
    def get_bound_joints(self) -> BitArray:
        """Returns the subset of joints controlled by this AnimControl.  Most of the
        time, this will be BitArray::all_on(), for a normal full-body animation.
        For a subset animation, however, this will be just a subset of those bits,
        corresponding to the set of joints and sliders actually bound (as
        enumerated by bind_hierarchy() in depth-first LIFO order).
        """
    def set_anim_model(self, model: PandaNode) -> None:
        """Associates the indicated PandaNode with the AnimControl.  By convention,
        this node represents the root node of the model file that corresponds to
        this AnimControl's animation file, though nothing in this code makes this
        assumption or indeed does anything with this node.

        The purpose of this is simply to allow the AnimControl to keep a reference
        count on the ModelRoot node that generated it, so that the model will not
        disappear from the model pool until it is no longer referenced.
        """
    def get_anim_model(self) -> PandaNode:
        """Retrieves the pointer set via set_anim_model().  See set_anim_model()."""
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

class AnimChannelBase(AnimGroup):
    """Parent class for all animation channels.  An AnimChannel is an arbitrary
    function that changes over time (actually, over frames), usually defined by
    a table read from an egg file (but possibly computed or generated in any
    other way).
    """

class AnimChannel_ACMatrixSwitchType(AnimChannelBase):
    def get_value(self, frame: int, value: Mat4Like) -> None: ...
    def get_value_no_scale_shear(self, frame: int, value: Mat4Like) -> None:
        """These transform-component methods only have meaning for matrix types."""
    def get_scale(self, frame: int, scale: Vec3Like) -> None: ...
    def get_hpr(self, frame: int, hpr: Vec3Like) -> None: ...
    def get_quat(self, frame: int, quat: Vec4Like) -> None: ...
    def get_pos(self, frame: int, pos: Vec3Like) -> None: ...
    def get_shear(self, frame: int, shear: Vec3Like) -> None: ...
    def get_value_type(self) -> TypeHandle: ...
    getValue = get_value
    getValueNoScaleShear = get_value_no_scale_shear
    getScale = get_scale
    getHpr = get_hpr
    getQuat = get_quat
    getPos = get_pos
    getShear = get_shear
    getValueType = get_value_type

class AnimChannel_ACScalarSwitchType(AnimChannelBase):
    def get_scale(self, frame: int, scale: Vec3Like) -> None: ...
    def get_hpr(self, frame: int, hpr: Vec3Like) -> None: ...
    def get_quat(self, frame: int, quat: Vec4Like) -> None: ...
    def get_pos(self, frame: int, pos: Vec3Like) -> None: ...
    def get_shear(self, frame: int, shear: Vec3Like) -> None: ...
    def get_value_type(self) -> TypeHandle: ...
    getScale = get_scale
    getHpr = get_hpr
    getQuat = get_quat
    getPos = get_pos
    getShear = get_shear
    getValueType = get_value_type

class AnimChannelMatrixDynamic(AnimChannel_ACMatrixSwitchType):
    """An animation channel that accepts a matrix each frame from some dynamic
    input provided by code.

    This object operates in two modes: in explicit mode, the programmer should
    call set_value() each frame to indicate the new value; in implicit mode,
    the programmer should call set_value_node() to indicate the node whose
    transform will be copied to the joint each frame.
    """

    value_node: PandaNode
    def set_value(self, value: Mat4Like | TransformState) -> None:
        """`(self, value: LMatrix4)`:
        Explicitly sets the matrix value.

        `(self, value: TransformState)`:
        Explicitly sets the matrix value, using the indicated TransformState object
        as a convenience.
        """
    def set_value_node(self, node: PandaNode) -> None:
        """Specifies a node whose transform will be queried each frame to implicitly
        specify the transform of this joint.
        """
    def get_value_transform(self) -> TransformState:
        """Returns the explicit TransformState value that was set via set_value(), if
        any.
        """
    def get_value_node(self) -> PandaNode:
        """Returns the node that was set via set_value_node(), if any."""
    setValue = set_value
    setValueNode = set_value_node
    getValueTransform = get_value_transform
    getValueNode = get_value_node

class AnimChannelMatrixXfmTable(AnimChannel_ACMatrixSwitchType):
    """An animation channel that issues a matrix each frame, read from a table
    such as might have been read from an egg file.  The table actually consists
    of nine sub-tables, each representing one component of the transform:
    scale, rotate, translate.
    """

    @property
    def tables(self) -> MutableMapping[str, CPTA_stdfloat]: ...
    def __init__(self, parent: AnimGroup, name: str) -> None: ...
    @staticmethod
    def is_valid_id(table_id: str) -> bool:
        """Returns true if the given letter is one of the nine valid table id's."""
    def set_table(self, table_id: str, table: CPTA_stdfloat | PointerToArray_float) -> None:
        """Assigns the indicated table.  table_id is one of 'i', 'j', 'k', for scale,
        'a', 'b', 'c' for shear, 'h', 'p', 'r', for rotation, and 'x', 'y', 'z',
        for translation.  The new table must have either zero, one, or
        get_num_frames() frames.
        """
    def get_table(self, table_id: str) -> CPTA_stdfloat:
        """Returns a pointer to the indicated subtable's data, if it exists, or NULL
        if it does not.
        """
    def clear_all_tables(self) -> None:
        """Removes all the tables from the channel, and resets it to its initial
        state.
        """
    def has_table(self, table_id: str) -> bool:
        """Returns true if the indicated subtable has been assigned."""
    def clear_table(self, table_id: str) -> None:
        """Removes the indicated table from the definition."""
    isValidId = is_valid_id
    setTable = set_table
    getTable = get_table
    clearAllTables = clear_all_tables
    hasTable = has_table
    clearTable = clear_table

class AnimChannelScalarDynamic(AnimChannel_ACScalarSwitchType):
    """An animation channel that accepts a scalar each frame from some dynamic
    input provided by code.

    This object operates in two modes: in explicit mode, the programmer should
    call set_value() each frame to indicate the new value; in implicit mode,
    the programmer should call set_value_node() to indicate the node whose X
    component will be copied to the scalar each frame.
    """

    value: float
    value_node: PandaNode
    def set_value(self, value: float) -> None:
        """Explicitly sets the value.  This will remove any node assigned via
        set_value_node().
        """
    def set_value_node(self, node: PandaNode) -> None:
        """Specifies a node whose transform will be queried each frame to implicitly
        specify the transform of this joint.  This will override the values set by
        set_value().
        """
    setValue = set_value
    setValueNode = set_value_node

class AnimChannelScalarTable(AnimChannel_ACScalarSwitchType):
    """An animation channel that issues a scalar each frame, read from a table
    such as might have been read from an egg file.
    """

    table: CPTA_stdfloat
    def __init__(self, parent: AnimGroup, name: str) -> None: ...
    def set_table(self, table: CPTA_stdfloat | PointerToArray_float) -> None:
        """Assigns the data table."""
    def get_table(self) -> CPTA_stdfloat:
        """Returns a pointer to the table's data, if it exists, or NULL if it does
        not.
        """
    def has_table(self) -> bool:
        """Returns true if the data table has been assigned."""
    def clear_table(self) -> None:
        """Empties the data table."""
    setTable = set_table
    getTable = get_table
    hasTable = has_table
    clearTable = clear_table

class AnimControlCollection:
    """This is a named collection of AnimControl pointers.  An AnimControl may be
    added to the collection by name.  While an AnimControl is associated, its
    reference count is maintained; associating a new AnimControl with the same
    name will decrement the previous control's reference count (and possibly
    delete it, unbinding its animation).
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: AnimControlCollection = ...) -> None:
        """Returns the AnimControl associated with the given name, or NULL if no such
        control has been associated.
        """
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def store_anim(self, control: AnimControl, name: str) -> None:
        """Associates the given AnimControl with this collection under the given name.
        The AnimControl will remain associated until a new AnimControl is
        associated with the same name later, or until unbind_anim() is called with
        this name.
        """
    def find_anim(self, name: str) -> AnimControl:
        """Returns the AnimControl associated with the given name, or NULL if no such
        control has been associated.
        """
    def unbind_anim(self, name: str) -> bool:
        """Removes the AnimControl associated with the given name, if any.  Returns
        true if an AnimControl was removed, false if there was no AnimControl with
        the indicated name.
        """
    def get_num_anims(self) -> int:
        """Returns the number of AnimControls associated with this collection."""
    def get_anim(self, n: int) -> AnimControl:
        """Returns the nth AnimControl associated with this collection."""
    def get_anim_name(self, n: int) -> str:
        """Returns the name of the nth AnimControl associated with this collection."""
    def clear_anims(self) -> None:
        """Disassociates all anims from this collection."""
    @overload
    def play(self, anim_name: str) -> bool:
        """Starts the named animation playing."""
    @overload
    def play(self, anim_name: str, _from: float, to: float) -> bool: ...
    @overload
    def loop(self, anim_name: str, restart: bool) -> bool:
        """Starts the named animation looping."""
    @overload
    def loop(self, anim_name: str, restart: bool, _from: float, to: float) -> bool: ...
    def stop(self, anim_name: str) -> bool:
        """Stops the named animation."""
    def pose(self, anim_name: str, frame: float) -> bool:
        """Sets to a particular frame in the named animation."""
    @overload
    def play_all(self) -> None:
        """`(self)`:
        These functions operate on all anims at once.

        `(self, _from: float, to: float)`:
        Starts all animations playing.
        """
    @overload
    def play_all(self, _from: float, to: float) -> None: ...
    @overload
    def loop_all(self, restart: bool) -> None:
        """Starts all animations looping."""
    @overload
    def loop_all(self, restart: bool, _from: float, to: float) -> None: ...
    def stop_all(self) -> bool:
        """Stops all currently playing animations.  Returns true if any animations
        were stopped, false if none were playing.
        """
    def pose_all(self, frame: float) -> None:
        """Sets all animations to the indicated frame."""
    def get_frame(self, anim_name: str = ...) -> int:
        """`(self)`:
        Returns the current frame in the last-started animation.

        `(self, anim_name: str)`:
        Returns the current frame in the named animation, or 0 if the animation is
        not found.
        """
    def get_num_frames(self, anim_name: str = ...) -> int:
        """`(self)`:
        Returns the total number of frames in the last-started animation.

        `(self, anim_name: str)`:
        Returns the total number of frames in the named animation, or 0 if the
        animation is not found.
        """
    def is_playing(self, anim_name: str = ...) -> bool:
        """`(self)`:
        Returns true if the last-started animation is currently playing, false
        otherwise.

        `(self, anim_name: str)`:
        Returns true if the named animation is currently playing, false otherwise.
        """
    def which_anim_playing(self) -> str:
        """Returns the name of the bound AnimControl currently playing, if any.  If
        more than one AnimControl is currently playing, returns all of the names
        separated by spaces.
        """
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
    """This table records data about a list of animations for a particular model,
    such as number of frames and frame rate.  It's used for implementating
    asynchronous binding.

    This table is normally built by an offline tool, such as egg-optchar.
    """

    def __init__(self) -> None: ...
    def get_num_anims(self) -> int:
        """Returns the number of animation records in the table."""
    def find_anim(self, basename: str) -> int:
        """Returns the index number in the table of the animation record with the
        indicated name, or -1 if the name is not present.  By convention, the
        basename is the filename of the egg or bam file, without the directory part
        and without the extension.  That is, it is
        Filename::get_basename_wo_extension().
        """
    def get_basename(self, n: int) -> str:
        """Returns the basename stored for the nth animation record.  See find_anim()."""
    def get_base_frame_rate(self, n: int) -> float:
        """Returns the frame rate stored for the nth animation record."""
    def get_num_frames(self, n: int) -> int:
        """Returns the number of frames stored for the nth animation record."""
    def clear_anims(self) -> None:
        """Removes all animation records from the table."""
    def remove_anim(self, n: int) -> None:
        """Removes the nth animation records from the table.  This renumbers indexes
        for following animations.
        """
    def add_anim(self, basename: str, base_frame_rate: float, num_frames: int) -> None:
        """Adds a new animation record to the table.  If there is already a record of
        this name, no operation is performed (the original record is unchanged).
        See find_anim().  This will invalidate existing index numbers.
        """
    def add_anims_from(self, other: AnimPreloadTable) -> None:
        """Copies the animation records from the other table into this one.  If a
        given record name exists in both tables, the record in this one supercedes.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    getNumAnims = get_num_anims
    findAnim = find_anim
    getBasename = get_basename
    getBaseFrameRate = get_base_frame_rate
    getNumFrames = get_num_frames
    clearAnims = clear_anims
    removeAnim = remove_anim
    addAnim = add_anim
    addAnimsFrom = add_anims_from

class PartSubset:
    """This class is used to define a subset of part names to apply to the
    PartBundle::bind_anim() operation.  Only those part names within the subset
    will be included in the bind.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: PartSubset = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def add_include_joint(self, name: GlobPattern | str) -> None:
        """Adds the named joint to the list of joints that will be explicitly included
        in the subset.  Any joint at or below a named node will be included in the
        subset (unless a lower node is also listed in the exclude list).

        Since the name is a GlobPattern, it may of course include filename globbing
        characters like * and ?.
        """
    def add_exclude_joint(self, name: GlobPattern | str) -> None:
        """Adds the named joint to the list of joints that will be explicitly
        exlcluded from the subset.  Any joint at or below a named node will not be
        included in the subset (unless a lower node is also listed in the include
        list).

        Since the name is a GlobPattern, it may of course include filename globbing
        characters like * and ?.
        """
    def append(self, other: PartSubset) -> None:
        """Appends the include and exclude list from the other object onto this
        object's lists.
        """
    def output(self, out: ostream) -> None: ...
    def is_include_empty(self) -> bool:
        """Returns true if the include list is completely empty, false otherwise.  If
        it is empty, it is the same thing as including all joints.
        """
    def matches_include(self, joint_name: str) -> bool:
        """Returns true if the indicated name matches a name on the include list,
        false otherwise.
        """
    def matches_exclude(self, joint_name: str) -> bool:
        """Returns true if the indicated name matches a name on the exclude list,
        false otherwise.
        """
    addIncludeJoint = add_include_joint
    addExcludeJoint = add_exclude_joint
    isIncludeEmpty = is_include_empty
    matchesInclude = matches_include
    matchesExclude = matches_exclude

class BindAnimRequest(ModelLoadRequest):
    """This class object manages an asynchronous load-and-bind animation request,
    as issued through PartBundle::load_bind_anim().
    """

    @overload
    def __init__(self, __param0: BindAnimRequest) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        filename: StrOrBytesPath,
        options: LoaderOptions,
        loader: Loader,
        control: AnimControl,
        hierarchy_match_flags: int,
        subset: PartSubset,
    ) -> None: ...

class PartBundle(PartGroup):
    """This is the root of a MovingPart hierarchy.  It defines the hierarchy of
    moving parts that make up an animatable object.
    """

    BT_linear: Final = 0
    BTLinear: Final = 0
    BT_normalized_linear: Final = 1
    BTNormalizedLinear: Final = 1
    BT_componentwise: Final = 2
    BTComponentwise: Final = 2
    BT_componentwise_quat: Final = 3
    BTComponentwiseQuat: Final = 3
    blend_type: _PartBundle_BlendType
    anim_blend_flag: bool
    frame_blend_flag: bool
    root_xform: LMatrix4
    @property
    def nodes(self) -> Sequence[PartBundleNode]: ...
    def __init__(self, name: str = ...) -> None:
        """Normally, a PartBundle constructor should not be called directly--it will
        get created when a PartBundleNode is created.
        """
    def get_anim_preload(self) -> AnimPreloadTable:
        """Returns the AnimPreloadTable associated with the PartBundle.  This table,
        if present, can be used for the benefit of load_bind_anim() to allow
        asynchronous binding.
        """
    def modify_anim_preload(self) -> AnimPreloadTable:
        """Returns a modifiable pointer to the AnimPreloadTable associated with the
        PartBundle, if any.
        """
    def set_anim_preload(self, table: AnimPreloadTable) -> None:
        """Replaces the AnimPreloadTable associated with the PartBundle."""
    def clear_anim_preload(self) -> None:
        """Removes any AnimPreloadTable associated with the PartBundle."""
    def merge_anim_preloads(self, other: PartBundle) -> None:
        """Copies the contents of the other PartBundle's preload table into this one."""
    def set_blend_type(self, bt: _PartBundle_BlendType) -> None:
        """Defines the algorithm that is used when blending multiple frames or
        multiple animations together, when either anim_blend_flag or
        frame_blend_flag is set to true.

        See partBundle.h for a description of the meaning of each of the BlendType
        values.
        """
    def get_blend_type(self) -> _PartBundle_BlendType:
        """Returns the algorithm that is used when blending multiple frames or
        multiple animations together, when either anim_blend_flag or
        frame_blend_flag is set to true.
        """
    def set_anim_blend_flag(self, anim_blend_flag: bool) -> None:
        """Defines the way the character responds to multiple calls to
        set_control_effect()).  By default, this flag is set false, which disallows
        multiple animations.  When this flag is false, it is not necessary to
        explicitly set the control_effect when starting an animation; starting the
        animation will implicitly remove the control_effect from the previous
        animation and set it on the current one.

        However, if this flag is set true, the control_effect must be explicitly
        set via set_control_effect() whenever an animation is to affect the
        character.
        """
    def get_anim_blend_flag(self) -> bool:
        """Returns whether the character allows multiple different animations to be
        bound simultaneously.  See set_anim_blend_flag().
        """
    def set_frame_blend_flag(self, frame_blend_flag: bool) -> None:
        """Specifies whether the character interpolates (blends) between two
        sequential frames of an active animation, showing a smooth intra-frame
        motion, or whether it holds each frame until the next frame is ready,
        showing precisely the specified animation.

        When this value is false, the character holds each frame until the next is
        ready.  When this is true, the character will interpolate between two
        consecutive frames of animation for each frame the animation is onscreen,
        according to the amount of time elapsed between the frames.

        The default value of this flag is determined by the interpolate-frames
        Config.prc variable.

        Use set_blend_type() to change the algorithm that the character uses to
        interpolate matrix positions.
        """
    def get_frame_blend_flag(self) -> bool:
        """Returns whether the character interpolates (blends) between two sequential
        animation frames, or whether it holds the current frame until the next one
        is ready.  See set_frame_blend_flag().
        """
    def set_root_xform(self, root_xform: Mat4Like) -> None:
        """Specifies the transform matrix which is implicitly applied at the root of
        the animated hierarchy.
        """
    def xform(self, mat: Mat4Like) -> None:
        """Applies the indicated transform to the root of the animated hierarchy."""
    def get_root_xform(self) -> LMatrix4:
        """Returns the transform matrix which is implicitly applied at the root of the
        animated hierarchy.
        """
    def apply_transform(self, transform: TransformState) -> PartBundle:
        """Returns a PartBundle that is a duplicate of this one, but with the
        indicated transform applied.  If this is called multiple times with the
        same TransformState pointer, it returns the same PartBundle each time.
        """
    def get_num_nodes(self) -> int:
        """Returns the number of PartBundleNodes that contain a pointer to this
        PartBundle.
        """
    def get_node(self, n: int) -> PartBundleNode:
        """Returns the nth PartBundleNode associated with this PartBundle."""
    def clear_control_effects(self) -> None:
        """Sets the control effect of all AnimControls to zero (but does not "stop"
        the AnimControls).  The character will no longer be affected by any
        animation, and will return to its default pose (unless restore-initial-pose
        is false).

        The AnimControls which are no longer associated will not be using any CPU
        cycles, but they may still be in the "playing" state; if they are later
        reassociated with the PartBundle they will resume at their current frame as
        if they'd been running all along.
        """
    def set_control_effect(self, control: AnimControl, effect: float) -> None:
        """Sets the amount by which the character is affected by the indicated
        AnimControl (and its associated animation).  Normally, this will only be
        zero or one.  Zero indicates the animation does not affect the character,
        and one means it does.

        If the _anim_blend_flag is not false (see set_anim_blend_flag()), it is
        possible to have multiple AnimControls in effect simultaneously.  In this
        case, the effect is a weight that indicates the relative importance of each
        AnimControl to the final animation.
        """
    def get_control_effect(self, control: AnimControl) -> float:
        """Returns the amount by which the character is affected by the indicated
        AnimControl and its associated animation.  See set_control_effect().
        """
    def output(self, out: ostream) -> None:
        """Writes a one-line description of the bundle."""
    def bind_anim(self, anim: AnimBundle, hierarchy_match_flags: int = ..., subset: PartSubset = ...) -> AnimControl:
        """Binds the animation to the bundle, if possible, and returns a new
        AnimControl that can be used to start and stop the animation.  If the anim
        hierarchy does not match the part hierarchy, returns NULL.

        If hierarchy_match_flags is 0, only an exact match is accepted; otherwise,
        it may contain a union of PartGroup::HierarchyMatchFlags values indicating
        conditions that will be tolerated (but warnings will still be issued).

        If subset is specified, it restricts the binding only to the named subtree
        of joints.

        The AnimControl is not stored within the PartBundle; it is the user's
        responsibility to maintain the pointer.  The animation will automatically
        unbind itself when the AnimControl destructs (i.e.  its reference count
        goes to zero).
        """
    def load_bind_anim(
        self, loader: Loader, filename: StrOrBytesPath, hierarchy_match_flags: int, subset: PartSubset, allow_async: bool
    ) -> AnimControl:
        """Binds an animation to the bundle.  The animation is loaded from the disk
        via the indicated Loader object.  In other respects, this behaves similarly
        to bind_anim(), with the addition of asynchronous support.

        If allow_aysnc is true, the load will be asynchronous if possible.  This
        requires that the animation basename can be found in the PartBundle's
        preload table (see get_anim_preload()).

        In an asynchronous load, the animation file will be loaded and bound in a
        sub-thread.  This means that the animation will not necessarily be
        available at the time this method returns.  You may still use the returned
        AnimControl immediately, though, but no visible effect will occur until the
        animation eventually becomes available.

        You can test AnimControl::is_pending() to see if the animation has been
        loaded yet, or wait for it to finish with AnimControl::wait_pending() or
        even PartBundle::wait_pending().  You can also set an event to be triggered
        when the animation finishes loading with
        AnimControl::set_pending_done_event().
        """
    def wait_pending(self) -> None:
        """Blocks the current thread until all currently-pending AnimControls, with a
        nonzero control effect, have been loaded and are properly bound.
        """
    @overload
    def freeze_joint(self, joint_name: str, value: float) -> bool:
        """Specifies that the joint with the indicated name should be frozen with the
        specified transform.  It will henceforth always hold this fixed transform,
        regardless of any animations that may subsequently be bound to the joint.

        Returns true if the joint is successfully frozen, or false if the named
        child is not a joint (or slider) or does not exist.
        """
    @overload
    def freeze_joint(self, joint_name: str, transform: TransformState) -> bool: ...
    @overload
    def freeze_joint(self, joint_name: str, pos: Vec3Like, hpr: Vec3Like, scale: Vec3Like) -> bool: ...
    def control_joint(self, joint_name: str, node: PandaNode) -> bool:
        """Specifies that the joint with the indicated name should be animated with
        the transform on the indicated node.  It will henceforth always follow the
        node's transform, regardless of any animations that may subsequently be
        bound to the joint.

        Returns true if the joint is successfully controlled, or false if the named
        child is not a joint (or slider) or does not exist.
        """
    def release_joint(self, joint_name: str) -> bool:
        """Releases the named joint from the effects of a previous call to
        freeze_joint() or control_joint(). It will henceforth once again follow
        whatever transforms are dictated by the animation.

        Returns true if the joint is released, or false if the named child was not
        previously controlled or frozen, or it does not exist.
        """
    def update(self) -> bool:
        """Updates all the parts in the bundle to reflect the data for the current
        frame (as set in each of the AnimControls).

        Returns true if any part has changed as a result of this, or false
        otherwise.
        """
    def force_update(self) -> bool:
        """Updates all the parts in the bundle to reflect the data for the current
        frame, whether we believe it needs it or not.
        """
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
    getNodes = get_nodes

class PartBundleNode(PandaNode):
    """This is a node that contains a pointer to an PartBundle.  Like
    AnimBundleNode, it exists to make it easy to store PartBundles in the scene
    graph.

    (Unlike AnimBundleNode, however, PartBundleNode has an additional function:
    it is also the base class of the Character node type, which adds additional
    functionality.)
    """

    @property
    def bundles(self) -> Sequence[PartBundle]: ...
    @property
    def bundle_handles(self) -> Sequence[PartBundleHandle]: ...
    def __init__(self, name: str, bundle: PartBundle) -> None:
        """The PartBundle and its node should be constructed together.  Generally, the
        derived classes of PartBundleNode will automatically create a PartBundle of
        the appropriate type, and pass it up to this constructor.
        """
    def get_num_bundles(self) -> int: ...
    def get_bundle(self, n: int) -> PartBundle: ...
    def get_bundle_handle(self, n: int) -> PartBundleHandle:
        """Returns the PartBundleHandle that wraps around the actual nth PartBundle.
        While the PartBundle pointer might later change due to a future flatten
        operation, the PartBundleHandle will not.
        """
    def get_bundles(self) -> tuple[PartBundle, ...]: ...
    def get_bundle_handles(self) -> tuple[PartBundleHandle, ...]: ...
    getNumBundles = get_num_bundles
    getBundle = get_bundle
    getBundleHandle = get_bundle_handle
    getBundles = get_bundles
    getBundleHandles = get_bundle_handles

class PartBundleHandle(ReferenceCount):
    """This is a trivial class returned by PartBundleNode::get_bundle().  Its
    purpose is to hold the actual PartBundle pointer contained within the
    PartBundleNode, so that scene graph flatten operations can safely combine
    or duplicate PartBundles as necessary without affecting high-level bundle
    operations.

    The high-level Actor class defined in direct/src/actor, for instance, will
    store a list of PartBundleHandles instead of on actual PartBundles, so that
    it will be immune to changes from these flatten operations.
    """

    bundle: PartBundle
    @overload
    def __init__(self, bundle: PartBundle) -> None: ...
    @overload
    def __init__(self, __param0: PartBundleHandle) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_bundle(self) -> PartBundle:
        """Returns the actual PartBundle embedded within the handle."""
    def set_bundle(self, bundle: PartBundle) -> None:
        """Changes the actual PartBundle embedded within the handle."""
    getBundle = get_bundle
    setBundle = set_bundle

class MovingPartBase(PartGroup):
    """This is the base class for a single animatable piece that may be bound to
    one channel (or more, if blending is in effect).  It corresponds to, for
    instance, a single joint or slider of a character.

    MovingPartBase does not have a particular value type.  See the derived
    template class, MovingPart, for this.
    """

    def get_max_bound(self) -> int:
        """Returns the number of channels that might be bound to this PartGroup.  This
        might not be the actual number of channels, since there might be holes in
        the list; it is one more than the index number of the highest bound
        channel.  Thus, it is called get_max_bound() instead of get_num_bound().
        """
    def get_bound(self, n: int) -> AnimChannelBase:
        """Returns the nth bound channel on this PartGroup.  n can be determined by
        iterating from 0 to one less than get_max_bound(); or n might be
        AnimControl::get_channel_index().

        This will return NULL if there is no channel bound on the indicated index.
        It is an error to call this if n is less than zero or greater than or equal
        to get_max_bound().
        """
    def output_value(self, out: ostream) -> None: ...
    getMaxBound = get_max_bound
    getBound = get_bound
    outputValue = output_value

class MovingPart_ACMatrixSwitchType(MovingPartBase):
    def get_value(self) -> LMatrix4: ...
    def get_default_value(self) -> LMatrix4: ...
    getValue = get_value
    getDefaultValue = get_default_value

class MovingPartMatrix(MovingPart_ACMatrixSwitchType):
    """This is a particular kind of MovingPart that accepts a matrix each frame."""

class MovingPart_ACScalarSwitchType(MovingPartBase):
    def get_value(self) -> float: ...
    def get_default_value(self) -> float: ...
    getValue = get_value
    getDefaultValue = get_default_value

class MovingPartScalar(MovingPart_ACScalarSwitchType):
    """This is a particular kind of MovingPart that accepts a scalar each frame."""

def auto_bind(root_node: PandaNode, controls: AnimControlCollection, hierarchy_match_flags: int = ...) -> None: ...

autoBind = auto_bind
AnimChannelACMatrixSwitchType = AnimChannel_ACMatrixSwitchType
AnimChannelMatrix = AnimChannel_ACMatrixSwitchType
AnimChannelACScalarSwitchType = AnimChannel_ACScalarSwitchType
AnimChannelScalar = AnimChannel_ACScalarSwitchType
MovingPartACMatrixSwitchType = MovingPart_ACMatrixSwitchType
MovingPartACScalarSwitchType = MovingPart_ACScalarSwitchType
