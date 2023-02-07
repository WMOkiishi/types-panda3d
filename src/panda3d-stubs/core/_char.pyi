from typing import overload
from typing_extensions import Self

from panda3d._typing import Mat4Like, Vec3Like
from panda3d.core._chan import MovingPartMatrix, MovingPartScalar, PartBundle, PartBundleHandle, PartBundleNode, PartGroup
from panda3d.core._dtoolutil import ostream
from panda3d.core._gobj import VertexSlider, VertexTransform
from panda3d.core._linmath import LMatrix4
from panda3d.core._pgraph import NodePathCollection, PandaNode, RenderEffect, TransformState

class CharacterJoint(MovingPartMatrix):
    """This represents one joint of the character's animation, containing an
    animating transform matrix.
    """

    def __init__(self, character: Character, root: PartBundle, parent: PartGroup, name: str, default_value: Mat4Like) -> None: ...
    def add_net_transform(self, node: PandaNode) -> bool:
        """Adds the indicated node to the list of nodes that will be updated each
        frame with the joint's net transform from the root.  Returns true if the
        node is successfully added, false if it had already been added.

        A CharacterJointEffect for this joint's Character will automatically be
        added to the specified node.
        """
    def remove_net_transform(self, node: PandaNode) -> bool:
        """Removes the indicated node from the list of nodes that will be updated each
        frame with the joint's net transform from the root.  Returns true if the
        node is successfully removed, false if it was not on the list.

        If the node has a CharacterJointEffect that matches this joint's Character,
        it will be cleared.
        """
    def has_net_transform(self, node: PandaNode) -> bool:
        """Returns true if the node is on the list of nodes that will be updated each
        frame with the joint's net transform from the root, false otherwise.
        """
    def clear_net_transforms(self) -> None:
        """Removes all nodes from the list of nodes that will be updated each frame
        with the joint's net transform from the root.
        """
    def get_net_transforms(self) -> NodePathCollection:
        """Returns a list of the net transforms set for this node.  Note that this
        returns a list of NodePaths, even though the net transforms are actually a
        list of PandaNodes.
        """
    def add_local_transform(self, node: PandaNode) -> bool:
        """Adds the indicated node to the list of nodes that will be updated each
        frame with the joint's local transform from its parent.  Returns true if
        the node is successfully added, false if it had already been added.

        The Character pointer should be the Character object that owns this joint;
        this will be used to create a CharacterJointEffect for this node.  If it is
        NULL, no such effect will be created.

        A CharacterJointEffect for this joint's Character will automatically be
        added to the specified node.
        """
    def remove_local_transform(self, node: PandaNode) -> bool:
        """Removes the indicated node from the list of nodes that will be updated each
        frame with the joint's local transform from its parent.  Returns true if
        the node is successfully removed, false if it was not on the list.

        If the node has a CharacterJointEffect that matches this joint's Character,
        it will be cleared.
        """
    def has_local_transform(self, node: PandaNode) -> bool:
        """Returns true if the node is on the list of nodes that will be updated each
        frame with the joint's local transform from its parent, false otherwise.
        """
    def clear_local_transforms(self) -> None:
        """Removes all nodes from the list of nodes that will be updated each frame
        with the joint's local transform from its parent.
        """
    def get_local_transforms(self) -> NodePathCollection:
        """Returns a list of the local transforms set for this node.  Note that this
        returns a list of NodePaths, even though the local transforms are actually
        a list of PandaNodes.
        """
    @overload
    def get_transform(self) -> LMatrix4:
        """`(self)`:
        Returns the transform matrix of the joint

        `(self, transform: LMatrix4)`:
        Copies the joint's current transform into the indicated matrix.
        """
    @overload
    def get_transform(self, transform: Mat4Like) -> None: ...
    def get_transform_state(self) -> TransformState: ...
    def get_net_transform(self, transform: Mat4Like) -> None:
        """Copies the joint's current net transform (composed from the root of the
        character joint hierarchy) into the indicated matrix.
        """
    def get_character(self) -> Character:
        """Returns the Character that owns this joint."""
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

class CharacterSlider(MovingPartScalar):
    """This is a morph slider within the character.  It's simply a single
    floating-point value that animates generally between 0 and 1, that controls
    the effects of one or more morphs within the character.
    """

    def __init__(self, parent: PartGroup, name: str, default_value: float = ...) -> None: ...

class CharacterVertexSlider(VertexSlider):
    """This is a specialization on VertexSlider that returns the slider value
    associated with a particular CharacterSlider object.
    """

    def __init__(self, char_slider: CharacterSlider) -> None:
        """Constructs a new object that converts vertices from the indicated joint's
        coordinate space, into the other indicated joint's space.
        """
    def get_char_slider(self) -> CharacterSlider:
        """Returns the CharacterSlider object for which this object returns the slider
        value.
        """
    getCharSlider = get_char_slider

class JointVertexTransform(VertexTransform):
    """This is a specialization on VertexTransform that returns the transform
    necessary to move vertices as if they were assigned to the indicated joint.
    The geometry itself should be parented to the scene graph at the level of
    the character's root joint; that is, it should not be parented under a node
    directly animated by any joints.

    Multiple combinations of these with different weights are used to implement
    soft-skinned vertices for an animated character.
    """

    def __init__(self, joint: CharacterJoint) -> None:
        """Constructs a new object that converts vertices from the indicated joint's
        coordinate space, into the other indicated joint's space.
        """
    def get_joint(self) -> CharacterJoint:
        """Returns the joint for which this object returns the transform."""
    getJoint = get_joint

class Character(PartBundleNode):
    """An animated character, with skeleton-morph animation and either soft-
    skinned or hard-skinned vertices.
    """

    @overload
    def __init__(self, __param0: Character) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_bundle(self, i: int) -> CharacterJointBundle: ...
    @overload
    def merge_bundles(self, old_bundle: PartBundle, other_bundle: PartBundle) -> None:
        """`(self, old_bundle: PartBundle, other_bundle: PartBundle)`:
        Merges old_bundle with new_bundle.  old_bundle must be one of the
        PartBundles within this node.  At the end of this call, the old_bundle
        pointer within this node will be replaced with the new_bundle pointer, and
        all geometry within this node will be updated to reference new_bundle.

        @deprecated Use the newer version of this method, below.

        `(self, old_bundle_handle: PartBundleHandle, other_bundle_handle: PartBundleHandle)`:
        Merges old_bundle_handle->get_bundle() with new_bundle.  old_bundle_handle
        must be one of the PartBundleHandle within this node.  At the end of this
        call, the bundle pointer within the old_bundle_handle will be replaced with
        that within the new_bundle_handle pointer, and all geometry within this
        node will be updated to reference new_bundle.

        Normally, this is called when the two bundles have the same, or nearly the
        same, hierarchies.  In this case, new_bundle will simply be assigned over
        the old_bundle position.  However, if any joints are present in one bundle
        or the other, new_bundle will be modified to contain the union of all
        joints.

        The geometry below this node is also updated to reference new_bundle,
        instead of the original old_bundle.

        This method is intended to unify two different models that share a common
        skeleton, for instance, different LOD's of the same model.
        """
    @overload
    def merge_bundles(self, old_bundle_handle: PartBundleHandle, other_bundle_handle: PartBundleHandle) -> None: ...
    def set_lod_animation(self, center: Vec3Like, far_distance: float, near_distance: float, delay_factor: float) -> None:
        """Activates a special mode in which the character animates less frequently as
        it gets further from the camera.  This is intended as a simple optimization
        to minimize the effort of computing animation for lots of characters that
        may not necessarily be very important to animate every frame.

        If the character is closer to the camera than near_distance, then it is
        animated its normal rate, every frame.  If the character is exactly
        far_distance away, it is animated only every delay_factor seconds (which
        should be a number greater than 0).  If the character is between
        near_distance and far_distance, its animation rate is linearly interpolated
        according to its distance between the two.  The interpolation function
        continues beyond far_distance, so that the character is animated
        increasingly less frequently as it gets farther away.

        The distance calculations are made from center, which is a fixed point
        relative to the character node, to the camera's lod center or cull center
        node (or to the camera node itself).

        If multiple cameras are viewing the character in any given frame, the
        closest one counts.
        """
    def clear_lod_animation(self) -> None:
        """Undoes the effect of a recent call to set_lod_animation().  Henceforth, the
        character will animate every frame, regardless of its distance from the
        camera.
        """
    def find_joint(self, name: str) -> CharacterJoint:
        """Returns a pointer to the joint with the given name, if there is such a
        joint, or NULL if there is no such joint.  This will not return a pointer
        to a slider.
        """
    def find_slider(self, name: str) -> CharacterSlider:
        """Returns a pointer to the slider with the given name, if there is such a
        slider, or NULL if there is no such slider.  This will not return a pointer
        to a joint.
        """
    def write_parts(self, out: ostream) -> None:
        """Writes a list of the Character's joints and sliders, in their hierchical
        structure, to the indicated output stream.
        """
    def write_part_values(self, out: ostream) -> None:
        """Writes a list of the Character's joints and sliders, along with each
        current position, in their hierchical structure, to the indicated output
        stream.
        """
    def update_to_now(self) -> None:
        """Advances the character's frame to the current time, and then calls
        update().  This can be used by show code to force an update of the
        character's position to the current frame, regardless of whether the
        character is currently onscreen and animating.

        @deprecated Call update() instead.
        """
    def update(self) -> None:
        """Recalculates the Character's joints and vertices for the current frame.
        Normally this is performed automatically during the render and need not be
        called explicitly.
        """
    def force_update(self) -> None:
        """Recalculates the character even if we think it doesn't need it."""
    getBundle = get_bundle  # type: ignore[assignment]
    mergeBundles = merge_bundles
    setLodAnimation = set_lod_animation
    clearLodAnimation = clear_lod_animation
    findJoint = find_joint
    findSlider = find_slider
    writeParts = write_parts
    writePartValues = write_part_values
    updateToNow = update_to_now
    forceUpdate = force_update

class CharacterJointBundle(PartBundle):
    """The collection of all the joints and sliders in the character."""

    def __init__(self, name: str = ...) -> None:
        """Normally, there is no need to create a CharacterJointBundle directly.  The
        Character node will automatically create one for itself.
        """
    def get_node(self, n: int) -> Character:
        """Returns the nth Character associated with this PartBundle."""
    getNode = get_node

class CharacterJointEffect(RenderEffect):
    """This effect will be added automatically to a node by
    CharacterJoint::add_net_transform() and
    CharacterJoint::add_local_transform().

    The effect binds the node back to the character, so that querying the
    relative transform of the affected node will automatically force the
    indicated character to be updated first.
    """

    @staticmethod
    def make(character: Character) -> RenderEffect:
        """Constructs a new CharacterJointEffect object that references the indicated
        character.  When a relative get_transform() is called on the node that
        contains the CharacterJointEffect, it will implicitly call
        character->update() first.
        """
    def get_character(self) -> Character:
        """Returns the Character that will get update() called on it when this node's
        relative transform is queried, or NULL if there is no such character.
        """
    getCharacter = get_character
