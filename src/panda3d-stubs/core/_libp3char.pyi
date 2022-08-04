from typing import Any, ClassVar, TypeAlias, overload
from panda3d.core import (
    LMatrix3f,
    LMatrix4f,
    LVecBase3f,
    MovingPartMatrix,
    MovingPartScalar,
    NodePathCollection,
    PandaNode,
    PartBundle,
    PartBundleHandle,
    PartBundleNode,
    PartGroup,
    RenderEffect,
    TransformState,
    TypeHandle,
    UnalignedLMatrix4f,
    VertexSlider,
    VertexTransform,
    ostream,
)

_Mat4f: TypeAlias = LMatrix4f | UnalignedLMatrix4f
_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow

class CharacterJoint(MovingPartMatrix):
    """This represents one joint of the character's animation, containing an
    animating transform matrix.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, character: Character, root: PartBundle, parent: PartGroup, name: str, default_value: _Mat4f) -> None: ...
    def add_net_transform(self, node: PandaNode) -> bool: ...
    def remove_net_transform(self, node: PandaNode) -> bool: ...
    def has_net_transform(self, node: PandaNode) -> bool: ...
    def clear_net_transforms(self) -> None: ...
    def get_net_transforms(self) -> NodePathCollection: ...
    def add_local_transform(self, node: PandaNode) -> bool: ...
    def remove_local_transform(self, node: PandaNode) -> bool: ...
    def has_local_transform(self, node: PandaNode) -> bool: ...
    def clear_local_transforms(self) -> None: ...
    def get_local_transforms(self) -> NodePathCollection: ...
    @overload
    def get_transform(self) -> LMatrix4f: ...
    @overload
    def get_transform(self, transform: _Mat4f) -> None: ...
    def get_transform_state(self) -> TransformState: ...
    def get_net_transform(self, transform: _Mat4f) -> None: ...
    def get_character(self) -> Character: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    addNetTransform = add_net_transform
    removeNetTransform = remove_net_transform
    hasNetTransform = has_net_transform
    clearNetTransforms = clear_net_transforms
    getNetTransforms = get_net_transforms
    addLocalTransform = add_local_transform
    removeLocalTransform = remove_local_transform
    hasLocalTransform = has_local_transform
    clearLocalTransforms = clear_local_transforms
    getLocalTransforms = get_local_transforms
    getTransform = get_transform
    getTransformState = get_transform_state
    getNetTransform = get_net_transform
    getCharacter = get_character
    getClassType = get_class_type

class CharacterSlider(MovingPartScalar):
    """This is a morph slider within the character.  It's simply a single
    floating-point value that animates generally between 0 and 1, that controls
    the effects of one or more morphs within the character.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, parent: PartGroup, name: str) -> None: ...
    @overload
    def __init__(self, parent: PartGroup, name: str, default_value: float) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class CharacterVertexSlider(VertexSlider):
    """This is a specialization on VertexSlider that returns the slider value
    associated with a particular CharacterSlider object.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, char_slider: CharacterSlider) -> None: ...
    def get_char_slider(self) -> CharacterSlider: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getCharSlider = get_char_slider
    getClassType = get_class_type

class JointVertexTransform(VertexTransform):
    """This is a specialization on VertexTransform that returns the transform
    necessary to move vertices as if they were assigned to the indicated joint.
    The geometry itself should be parented to the scene graph at the level of
    the character's root joint; that is, it should not be parented under a node
    directly animated by any joints.
    
    Multiple combinations of these with different weights are used to implement
    soft-skinned vertices for an animated character.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, joint: CharacterJoint) -> None: ...
    def get_joint(self) -> CharacterJoint: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getJoint = get_joint
    getClassType = get_class_type

class Character(PartBundleNode):
    """An animated character, with skeleton-morph animation and either soft-
    skinned or hard-skinned vertices.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: Character) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def get_bundle(self, i: int) -> CharacterJointBundle: ...
    @overload
    def merge_bundles(self, old_bundle: PartBundle, other_bundle: PartBundle) -> None: ...
    @overload
    def merge_bundles(self, old_bundle_handle: PartBundleHandle, other_bundle_handle: PartBundleHandle) -> None: ...
    def set_lod_animation(self, center: _Vec3f, far_distance: float, near_distance: float, delay_factor: float) -> None: ...
    def clear_lod_animation(self) -> None: ...
    def find_joint(self, name: str) -> CharacterJoint: ...
    def find_slider(self, name: str) -> CharacterSlider: ...
    def write_parts(self, out: ostream) -> None: ...
    def write_part_values(self, out: ostream) -> None: ...
    def update_to_now(self) -> None: ...
    def update(self) -> None: ...
    def force_update(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getBundle = get_bundle
    mergeBundles = merge_bundles
    setLodAnimation = set_lod_animation
    clearLodAnimation = clear_lod_animation
    findJoint = find_joint
    findSlider = find_slider
    writeParts = write_parts
    writePartValues = write_part_values
    updateToNow = update_to_now
    forceUpdate = force_update
    getClassType = get_class_type

class CharacterJointBundle(PartBundle):
    """The collection of all the joints and sliders in the character."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str = ...) -> None: ...
    def get_node(self, n: int) -> Character: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNode = get_node
    getClassType = get_class_type

class CharacterJointEffect(RenderEffect):
    """This effect will be added automatically to a node by
    CharacterJoint::add_net_transform() and
    CharacterJoint::add_local_transform().
    
    The effect binds the node back to the character, so that querying the
    relative transform of the affected node will automatically force the
    indicated character to be updated first.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def make(character: Character) -> RenderEffect: ...
    def get_character(self) -> Character: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getCharacter = get_character
    getClassType = get_class_type
