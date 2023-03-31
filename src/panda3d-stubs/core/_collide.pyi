from collections.abc import MutableSequence, Sequence
from typing import overload
from typing_extensions import Self

from panda3d._typing import Vec2Like, Vec3Like, Vec4Like
from panda3d.core._dtoolbase import TypedObject
from panda3d.core._dtoolutil import ostream
from panda3d.core._express import Datagram, DatagramIterator, Namable, TypedReferenceCount
from panda3d.core._linmath import LPoint3, LPoint3i, LVector3
from panda3d.core._mathutil import BoundingVolume, LParabola, LPlane
from panda3d.core._pgraph import LensNode, NodePath, PandaNode
from panda3d.core._putil import CollideMask, CopyOnWriteObject, TypedWritableReferenceCount
from panda3d.core._tform import DriveInterface

class CollisionSolid(CopyOnWriteObject):
    """The abstract base class for all things that can collide with other things
    in the world, and all the things they can collide with (except geometry).

    This class and its derivatives really work very similarly to the way
    BoundingVolume and all of its derivatives work.  There's a different
    subclass for each basic shape of solid, and double-dispatch function calls
    handle the subset of the N*N intersection tests that we care about.
    """

    tangible: bool
    respect_effective_normal: bool
    bounds: BoundingVolume
    @property
    def collision_origin(self) -> LPoint3: ...
    def get_collision_origin(self) -> LPoint3: ...
    def set_tangible(self, tangible: bool) -> None:
        """Sets the current state of the 'tangible' flag.  Set this true to make the
        solid tangible, so that a CollisionHandlerPusher will not allow another
        object to intersect it, or false to make it intangible, so that a
        CollisionHandlerPusher will ignore it except to throw an event.
        """
    def is_tangible(self) -> bool:
        """Returns whether the solid is considered 'tangible' or not.  An intangible
        solid has no effect in a CollisionHandlerPusher (except to throw an event);
        it's useful for defining 'trigger' planes and spheres, that cause an effect
        when passed through.
        """
    def set_effective_normal(self, effective_normal: Vec3Like) -> None:
        """Records a false normal for this CollisionSolid that will be reported by the
        collision system with all collisions into it, instead of its actual normal.
        This is useful as a workaround for the problem of an avatar wanting to
        stand on a sloping ground; by storing a false normal, the ground appears to
        be perfectly level, and the avatar does not tend to slide down it.
        """
    def clear_effective_normal(self) -> None:
        """Removes the normal previously set by set_effective_normal()."""
    def has_effective_normal(self) -> bool:
        """Returns true if a special normal was set by set_effective_normal(), false
        otherwise.
        """
    def get_effective_normal(self) -> LVector3:
        """Returns the normal that was set by set_effective_normal().  It is an error
        to call this unless has_effective_normal() returns true.
        """
    def set_respect_effective_normal(self, respect_effective_normal: bool) -> None:
        """This is only meaningful for CollisionSolids that will be added to a
        traverser as colliders.  It is normally true, but if set false, it means
        that this particular solid does not care about the "effective" normal of
        other solids it meets, but rather always uses the true normal.
        """
    def get_respect_effective_normal(self) -> bool:
        """See set_respect_effective_normal()."""
    def get_bounds(self) -> BoundingVolume:
        """Returns the solid's bounding volume."""
    def set_bounds(self, bounding_volume: BoundingVolume) -> None:
        """Returns the solid's bounding volume."""
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    getCollisionOrigin = get_collision_origin
    setTangible = set_tangible
    isTangible = is_tangible
    setEffectiveNormal = set_effective_normal
    clearEffectiveNormal = clear_effective_normal
    hasEffectiveNormal = has_effective_normal
    getEffectiveNormal = get_effective_normal
    setRespectEffectiveNormal = set_respect_effective_normal
    getRespectEffectiveNormal = get_respect_effective_normal
    getBounds = get_bounds
    setBounds = set_bounds

class CollisionBox(CollisionSolid):
    """A cuboid collision volume or object."""

    @property
    def center(self) -> LPoint3: ...
    @property
    def min(self) -> LPoint3: ...
    @property
    def max(self) -> LPoint3: ...
    @property
    def dimensions(self) -> LVector3: ...
    @overload
    def __init__(self, min: Vec3Like, max: Vec3Like) -> None:
        """`(self, min: LPoint3, max: LPoint3)`:
        Create the Box by Specifying the Diagonal Points

        `(self, center: LPoint3, x: float, y: float, z: float)`:
        Create the Box by giving a Center and distances of each of the sides of
        box from the Center.
        """
    @overload
    def __init__(self, center: Vec3Like, x: float, y: float, z: float) -> None: ...
    def get_num_points(self) -> int:
        """Returns 8: the number of vertices of a rectangular solid."""
    def get_point_aabb(self, n: int) -> LPoint3:
        """Returns the nth vertex of the Axis Aligned Bounding Box."""
    def get_point(self, n: int) -> LPoint3:
        """Returns the nth vertex of the OBB."""
    def get_num_planes(self) -> int:
        """Returns 6: the number of faces of a rectangular solid."""
    def set_plane(self, n: int) -> LPlane:
        """Creates the nth face of the rectangular solid."""
    def get_plane(self, n: int) -> LPlane:
        """Returns the nth face of the rectangular solid."""
    @overload
    def set_center(self, center: Vec3Like) -> None: ...
    @overload
    def set_center(self, x: float, y: float, z: float) -> None: ...
    def get_center(self) -> LPoint3: ...
    def get_min(self) -> LPoint3: ...
    def get_max(self) -> LPoint3: ...
    def get_dimensions(self) -> LVector3: ...
    getNumPoints = get_num_points
    getPointAabb = get_point_aabb
    getPoint = get_point
    getNumPlanes = get_num_planes
    setPlane = set_plane
    getPlane = get_plane
    setCenter = set_center
    getCenter = get_center
    getMin = get_min
    getMax = get_max
    getDimensions = get_dimensions

class CollisionCapsule(CollisionSolid):
    """This implements a solid consisting of a cylinder with hemispherical endcaps,
    also known as a capsule or a spherocylinder.

    This shape was previously erroneously called CollisionTube.
    """

    point_a: LPoint3
    point_b: LPoint3
    radius: float
    @overload
    def __init__(self, a: Vec3Like, db: Vec3Like, radius: float) -> None: ...
    @overload
    def __init__(self, ax: float, ay: float, az: float, bx: float, by: float, bz: float, radius: float) -> None: ...
    @overload
    def set_point_a(self, a: Vec3Like) -> None: ...
    @overload
    def set_point_a(self, x: float, y: float, z: float) -> None: ...
    def get_point_a(self) -> LPoint3: ...
    @overload
    def set_point_b(self, b: Vec3Like) -> None: ...
    @overload
    def set_point_b(self, x: float, y: float, z: float) -> None: ...
    def get_point_b(self) -> LPoint3: ...
    def set_radius(self, radius: float) -> None: ...
    def get_radius(self) -> float: ...
    setPointA = set_point_a
    getPointA = get_point_a
    setPointB = set_point_b
    getPointB = get_point_b
    setRadius = set_radius
    getRadius = get_radius

class CollisionHandler(TypedReferenceCount):
    """The abstract interface to a number of classes that decide what to do when a
    collision is detected.  One of these must be assigned to the
    CollisionTraverser that is processing collisions in order to specify how to
    dispatch detected collisions.
    """

    def __init__(self, __param0: CollisionHandler) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...

class CollisionNode(PandaNode):
    """A node in the scene graph that can hold any number of CollisionSolids.
    This may either represent a bit of static geometry in the scene that things
    will collide with, or an animated object twirling around in the world and
    running into things.
    """

    from_collide_mask: CollideMask
    collider_sort: int
    @property
    def solids(self) -> MutableSequence[CollisionSolid]: ...
    @property
    def default_collide_mask(self) -> CollideMask: ...
    def set_collide_mask(self, mask: CollideMask | int) -> None:
        """Simultaneously sets both the "from" and "into" CollideMask values to the
        same thing.
        """
    def set_from_collide_mask(self, mask: CollideMask | int) -> None:
        """Sets the "from" CollideMask.  In order for a collision to be detected from
        this object into another object, the intersection of this object's "from"
        mask and the other object's "into" mask must be nonzero.
        """
    def set_into_collide_mask(self, mask: CollideMask | int) -> None:
        """Sets the "into" CollideMask.  In order for a collision to be detected from
        another object into this object, the intersection of the other object's
        "from" mask and this object's "into" mask must be nonzero.
        """
    def get_from_collide_mask(self) -> CollideMask:
        """Returns the current "from" CollideMask.  In order for a collision to be
        detected from this object into another object, the intersection of this
        object's "from" mask and the other object's "into" mask must be nonzero.
        """
    def get_into_collide_mask(self) -> CollideMask:
        """Returns the current "into" CollideMask.  In order for a collision to be
        detected from another object into this object, the intersection of the
        other object's "from" mask and this object's "into" mask must be nonzero.
        """
    def clear_solids(self) -> None:
        """Removes all solids from the node."""
    def get_num_solids(self) -> int: ...
    def get_solid(self, n: int) -> CollisionSolid: ...
    def modify_solid(self, n: int) -> CollisionSolid: ...
    def set_solid(self, n: int, solid: CollisionSolid) -> None:
        """Replaces the solid with the indicated index."""
    def insert_solid(self, n: int, solid: CollisionSolid) -> None:
        """Inserts the indicated solid to the node at the indicated position."""
    def remove_solid(self, n: int) -> None:
        """Removes the solid with the indicated index.  This will shift all subsequent
        indices down by one.
        """
    def add_solid(self, solid: CollisionSolid) -> int:
        """Adds the indicated solid to the node.  Returns the index of the new solid
        within the node's list of solids.
        """
    def get_collider_sort(self) -> int:
        """Returns the collider_sort value that has been set for this particular node.
        See set_collider_sort().
        """
    def set_collider_sort(self, sort: int) -> None:
        """Sets a particular collider_sort value on this node.  This controls the
        order in which colliders (that is, "from nodes") are grouped together for
        the collision traversal.

        If there are 32 or fewer colliders added to any particular
        CollisionTraverser, then this value has no meaning.  It is only useful if
        there are many colliders, which may force the CollisionTraverser to make
        multiple passes through the data; in that case, it may be a useful
        optimization to group colliders that have similar bounding volumes together
        (by giving them similar sort values).
        """
    @staticmethod
    def get_default_collide_mask() -> CollideMask:
        """Returns the default into_collide_mask assigned to new CollisionNodes."""
    def get_solids(self) -> tuple[CollisionSolid, ...]: ...
    setCollideMask = set_collide_mask
    setFromCollideMask = set_from_collide_mask
    setIntoCollideMask = set_into_collide_mask
    getFromCollideMask = get_from_collide_mask
    getIntoCollideMask = get_into_collide_mask
    clearSolids = clear_solids
    getNumSolids = get_num_solids
    getSolid = get_solid
    modifySolid = modify_solid
    setSolid = set_solid
    insertSolid = insert_solid
    removeSolid = remove_solid
    addSolid = add_solid
    getColliderSort = get_collider_sort
    setColliderSort = set_collider_sort
    getDefaultCollideMask = get_default_collide_mask
    getSolids = get_solids

class CollisionTraverser(Namable):
    """This class manages the traversal through the scene graph to detect
    collisions.  It holds ownership of a number of collider objects, each of
    which is a CollisionNode and an associated CollisionHandler.

    When traverse() is called, it begins at the indicated root and detects all
    collisions with any of its collider objects against nodes at or below the
    indicated root, calling the appropriate CollisionHandler for each detected
    collision.
    """

    respect_preV_transform: bool
    respect_prev_transform: bool
    recorder: CollisionRecorder
    @property
    def colliders(self) -> Sequence[NodePath]: ...
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, __param0: CollisionTraverser) -> None: ...
    def set_respect_prev_transform(self, flag: bool) -> None:
        """Sets the flag that indicates whether the prev_transform stored on a node
        (as updated via set_fluid_pos(), etc.) is respected to calculate
        collisions.  If this is true, certain types of collision tests will be
        enhanced by the information about objects in motion.  If this is false,
        objects are always considered to be static.  The default is false.
        """
    def get_respect_prev_transform(self) -> bool:
        """Returns the flag that indicates whether the prev_transform stored on a node
        is respected to calculate collisions.  See set_respect_prev_transform().
        """
    def add_collider(self, collider: NodePath, handler: CollisionHandler) -> None:
        """Adds a new CollisionNode, representing an object that will be tested for
        collisions into other objects, along with the handler that will serve each
        detected collision.  Each CollisionNode may be served by only one handler
        at a time, but a given handler may serve many CollisionNodes.

        The handler that serves a particular node may be changed from time to time
        by calling add_collider() again on the same node.
        """
    def remove_collider(self, collider: NodePath) -> bool:
        """Removes the collider (and its associated handler) from the set of
        CollisionNodes that will be tested each frame for collisions into other
        objects.  Returns true if the definition was found and removed, false if it
        wasn't present to begin with.
        """
    def has_collider(self, collider: NodePath) -> bool:
        """Returns true if the indicated node is current in the set of nodes that will
        be tested each frame for collisions into other objects.
        """
    def get_num_colliders(self) -> int:
        """Returns the number of CollisionNodes that have been added to the traverser
        via add_collider().
        """
    def get_collider(self, n: int) -> NodePath:
        """Returns the nth CollisionNode that has been added to the traverser via
        add_collider().
        """
    def get_handler(self, collider: NodePath) -> CollisionHandler:
        """Returns the handler that is currently assigned to serve the indicated
        collision node, or NULL if the node is not on the traverser's set of active
        nodes.
        """
    def clear_colliders(self) -> None:
        """Completely empties the set of collision nodes and their associated
        handlers.
        """
    def traverse(self, root: NodePath) -> None:
        """Perform the traversal. Begins at the indicated root and detects all
        collisions with any of its collider objects against nodes at or below the
        indicated root, calling the appropriate CollisionHandler for each detected
        collision.
        """
    def set_recorder(self, recorder: CollisionRecorder) -> None:
        """Uses the indicated CollisionRecorder object to start recording the
        intersection tests made by each subsequent call to traverse() on this
        object.  A particular CollisionRecorder object can only record one
        traverser at a time; if this object has already been assigned to another
        traverser, that assignment is broken.

        This is intended to be used in a debugging mode to try to determine what
        work is being performed by the collision traversal.  Usually, attaching a
        recorder will impose significant runtime overhead.

        This does not transfer ownership of the CollisionRecorder pointer;
        maintenance of that remains the caller's responsibility.  If the
        CollisionRecorder is destructed, it will cleanly remove itself from the
        traverser.
        """
    def has_recorder(self) -> bool:
        """Returns true if the CollisionTraverser has a CollisionRecorder object
        currently assigned, false otherwise.
        """
    def get_recorder(self) -> CollisionRecorder:
        """Returns the CollisionRecorder currently assigned, or NULL if no recorder is
        assigned.
        """
    def clear_recorder(self) -> None:
        """Removes the CollisionRecorder from the traverser and restores normal low-
        overhead operation.
        """
    def show_collisions(self, root: NodePath) -> CollisionVisualizer:
        """This is a high-level function to create a CollisionVisualizer object to
        render the collision tests performed by this traverser.  The supplied root
        should be any node in the scene graph; typically, the top node (e.g.
        render).  The CollisionVisualizer will be attached to this node.
        """
    def hide_collisions(self) -> None:
        """Undoes the effect of a previous call to show_collisions()."""
    def write(self, out: ostream, indent_level: int) -> None: ...
    def get_colliders(self) -> tuple[NodePath, ...]: ...
    setRespectPrevTransform = set_respect_prev_transform
    getRespectPrevTransform = get_respect_prev_transform
    addCollider = add_collider
    removeCollider = remove_collider
    hasCollider = has_collider
    getNumColliders = get_num_colliders
    getCollider = get_collider
    getHandler = get_handler
    clearColliders = clear_colliders
    setRecorder = set_recorder
    hasRecorder = has_recorder
    getRecorder = get_recorder
    clearRecorder = clear_recorder
    showCollisions = show_collisions
    hideCollisions = hide_collisions
    getColliders = get_colliders

class CollisionRecorder(TypedObject):
    """This class is used to help debug the work the collisions system is doing.
    It is a virtual base class that just provides an interface for recording
    collisions tested and detected each frame.
    """

    def output(self, out: ostream) -> None: ...

class CollisionEntry(TypedWritableReferenceCount):
    """Defines a single collision event.  One of these is created for each
    collision detected by a CollisionTraverser, to be dealt with by the
    CollisionHandler.

    A CollisionEntry provides slots for a number of data values (such as
    intersection point and normal) that might or might not be known for each
    collision.  It is up to the handler to determine what information is known
    and to do the right thing with it.
    """

    t: float
    @property
    def from_solid(self) -> CollisionSolid: ...
    @property
    def into_solid(self) -> CollisionSolid: ...
    @property
    def from_node(self) -> CollisionNode: ...
    @property
    def into_node(self) -> PandaNode: ...
    @property
    def from_node_path(self) -> NodePath: ...
    @property
    def into_node_path(self) -> NodePath: ...
    @property
    def respect_prev_transform(self) -> bool: ...
    def get_from(self) -> CollisionSolid:
        """Returns the CollisionSolid pointer for the particular solid that triggered
        this collision.
        """
    def has_into(self) -> bool:
        """Returns true if the "into" solid is, in fact, a CollisionSolid, and its
        pointer is known (in which case get_into() may be called to retrieve it).
        If this returns false, the collision was detected into a GeomNode, and
        there is no CollisionSolid pointer to be retrieved.
        """
    def get_into(self) -> CollisionSolid:
        """Returns the CollisionSolid pointer for the particular solid was collided
        into.  This pointer might be NULL if the collision was into a piece of
        visible geometry, instead of a normal CollisionSolid collision; see
        has_into().
        """
    def get_from_node(self) -> CollisionNode:
        """Returns the node that contains the CollisionSolid that triggered this
        collision.  This will be a node that has been added to a CollisionTraverser
        via add_collider().
        """
    def get_into_node(self) -> PandaNode:
        """Returns the node that contains the CollisionSolid that was collided into.
        This returns a PandaNode pointer instead of something more specific,
        because it might be either a CollisionNode or a GeomNode.

        Also see get_into_node_path().
        """
    def get_from_node_path(self) -> NodePath:
        """Returns the NodePath that represents the CollisionNode that contains the
        CollisionSolid that triggered this collision.  This will be a NodePath that
        has been added to a CollisionTraverser via add_collider().
        """
    def get_into_node_path(self) -> NodePath:
        """Returns the NodePath that represents the specific CollisionNode or GeomNode
        instance that was collided into.  This is the same node returned by
        get_into_node(), represented as a NodePath; however, it may be more useful
        because the NodePath can resolve the particular instance of the node, if
        there is more than one.
        """
    def set_t(self, t: float) -> None:
        """Sets a time value for this collision relative to other CollisionEntries"""
    def get_t(self) -> float:
        """returns time value for this collision relative to other CollisionEntries"""
    def collided(self) -> bool:
        """returns true if this represents an actual collision as opposed to a
        potential collision, needed for iterative collision resolution where path
        of collider changes mid-frame
        """
    def reset_collided(self) -> None:
        """prepare for another collision test"""
    def get_respect_prev_transform(self) -> bool:
        """Returns true if the collision was detected by a CollisionTraverser whose
        respect_prev_transform flag was set true, meaning we should consider motion
        significant in evaluating collisions.
        """
    def set_surface_point(self, point: Vec3Like) -> None:
        """Stores the point, on the surface of the "into" object, at which a collision
        is detected.

        This point is specified in the coordinate space of the "into" object.
        """
    def set_surface_normal(self, normal: Vec3Like) -> None:
        """Stores the surface normal of the "into" object at the point of the
        intersection.

        This normal is specified in the coordinate space of the "into" object.
        """
    def set_interior_point(self, point: Vec3Like) -> None:
        """Stores the point, within the interior of the "into" object, which
        represents the depth to which the "from" object has penetrated.  This can
        also be described as the intersection point on the surface of the "from"
        object (which is inside the "into" object).

        This point is specified in the coordinate space of the "into" object.
        """
    def has_surface_point(self) -> bool:
        """Returns true if the surface point has been specified, false otherwise.  See
        get_surface_point().  Some types of collisions may not compute the surface
        point.
        """
    def has_surface_normal(self) -> bool:
        """Returns true if the surface normal has been specified, false otherwise.
        See get_surface_normal().  Some types of collisions may not compute the
        surface normal.
        """
    def has_interior_point(self) -> bool:
        """Returns true if the interior point has been specified, false otherwise.
        See get_interior_point().  Some types of collisions may not compute the
        interior point.
        """
    def set_contact_pos(self, pos: Vec3Like) -> None:
        """Stores the position of the "from" object at the instant at which the
        collision is first detected.

        This position is specified in the coordinate space of the "into" object.
        """
    def set_contact_normal(self, normal: Vec3Like) -> None:
        """Stores the surface normal of the "into" object at the contact pos.

        This normal is specified in the coordinate space of the "into" object.
        """
    def has_contact_pos(self) -> bool:
        """Returns true if the contact position has been specified, false otherwise.
        See get_contact_pos().  Some types of collisions may not compute the
        contact pos.
        """
    def has_contact_normal(self) -> bool:
        """Returns true if the contact normal has been specified, false otherwise.
        See get_contact_normal().  Some types of collisions may not compute the
        contact normal.
        """
    def get_surface_point(self, space: NodePath) -> LPoint3:
        """Returns the point, on the surface of the "into" object, at which a
        collision is detected.  This can be thought of as the first point of
        intersection.  However the contact point is the actual first point of
        intersection.

        The point will be converted into whichever coordinate space the caller
        specifies.
        """
    def get_surface_normal(self, space: NodePath) -> LVector3:
        """Returns the surface normal of the "into" object at the point at which a
        collision is detected.

        The normal will be converted into whichever coordinate space the caller
        specifies.
        """
    def get_interior_point(self, space: NodePath) -> LPoint3:
        """Returns the point, within the interior of the "into" object, which
        represents the depth to which the "from" object has penetrated.  This can
        also be described as the intersection point on the surface of the "from"
        object (which is inside the "into" object).  It can be thought of as the
        deepest point of intersection.

        The point will be converted into whichever coordinate space the caller
        specifies.
        """
    def get_all(self, space: NodePath, surface_point: Vec3Like, surface_normal: Vec3Like, interior_point: Vec3Like) -> bool:
        """Simultaneously transforms the surface point, surface normal, and interior
        point of the collision into the indicated coordinate space.

        Returns true if all three properties are available, or false if any one of
        them is not.
        """
    def get_contact_pos(self, space: NodePath) -> LPoint3:
        """Returns the position of the "from" object at the instant that a collision
        is first detected.

        The position will be converted into whichever coordinate space the caller
        specifies.
        """
    def get_contact_normal(self, space: NodePath) -> LVector3:
        """Returns the surface normal of the "into" object at the contact position.

        The normal will be converted into whichever coordinate space the caller
        specifies.
        """
    def get_all_contact_info(self, space: NodePath, contact_pos: Vec3Like, contact_normal: Vec3Like) -> bool:
        """Simultaneously transforms the contact position and contact normal of the
        collision into the indicated coordinate space.

        Returns true if all three properties are available, or false if any one of
        them is not.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    getFrom = get_from
    hasInto = has_into
    getInto = get_into
    getFromNode = get_from_node
    getIntoNode = get_into_node
    getFromNodePath = get_from_node_path
    getIntoNodePath = get_into_node_path
    setT = set_t
    getT = get_t
    resetCollided = reset_collided
    getRespectPrevTransform = get_respect_prev_transform
    setSurfacePoint = set_surface_point
    setSurfaceNormal = set_surface_normal
    setInteriorPoint = set_interior_point
    hasSurfacePoint = has_surface_point
    hasSurfaceNormal = has_surface_normal
    hasInteriorPoint = has_interior_point
    setContactPos = set_contact_pos
    setContactNormal = set_contact_normal
    hasContactPos = has_contact_pos
    hasContactNormal = has_contact_normal
    getSurfacePoint = get_surface_point
    getSurfaceNormal = get_surface_normal
    getInteriorPoint = get_interior_point
    getAll = get_all
    getContactPos = get_contact_pos
    getContactNormal = get_contact_normal
    getAllContactInfo = get_all_contact_info

class CollisionPlane(CollisionSolid):
    plane: LPlane
    @property
    def normal(self) -> LVector3: ...
    @overload
    def __init__(self, copy: CollisionPlane) -> None: ...
    @overload
    def __init__(self, plane: Vec4Like) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_normal(self) -> LVector3: ...
    def dist_to_plane(self, point: Vec3Like) -> float: ...
    def set_plane(self, plane: Vec4Like) -> None: ...
    def get_plane(self) -> LPlane: ...
    def flip(self) -> None:
        """Convenience method to flip the plane in-place."""
    getNormal = get_normal
    distToPlane = dist_to_plane
    setPlane = set_plane
    getPlane = get_plane

class CollisionFloorMesh(CollisionSolid):
    """This object represents a solid made entirely of triangles, which will only
    be tested again z axis aligned rays
    """

    @property
    def vertices(self) -> Sequence[LPoint3]: ...
    @property
    def triangles(self) -> Sequence[LPoint3i]: ...
    def __init__(self) -> None:
        """This is only for the convenience of CollisionPolygon.  Normally, you should
        not attempt to create an uninitialized CollisionPlane.
        """
    def add_vertex(self, vert: Vec3Like) -> None:
        """store away a vertex to index against"""
    def add_triangle(self, pointA: int, pointB: int, pointC: int) -> None:
        """store a triangle for processing"""
    def get_num_vertices(self) -> int: ...
    def get_vertex(self, index: int) -> LPoint3: ...
    def get_num_triangles(self) -> int: ...
    def get_triangle(self, index: int) -> LPoint3i: ...
    def get_vertices(self) -> tuple[LPoint3, ...]: ...
    def get_triangles(self) -> tuple[LPoint3i, ...]: ...
    addVertex = add_vertex
    addTriangle = add_triangle
    getNumVertices = get_num_vertices
    getVertex = get_vertex
    getNumTriangles = get_num_triangles
    getTriangle = get_triangle
    getVertices = get_vertices
    getTriangles = get_triangles

class CollisionPolygon(CollisionPlane):
    @property
    def points(self) -> Sequence[LPoint3]: ...
    @property
    def valid(self) -> bool: ...
    @property
    def concave(self) -> bool: ...
    def __init__(self, a: Vec3Like, b: Vec3Like, c: Vec3Like, d: Vec3Like = ...) -> None: ...
    def get_num_points(self) -> int:
        """Returns the number of vertices of the CollisionPolygon."""
    def get_point(self, n: int) -> LPoint3:
        """Returns the nth vertex of the CollisionPolygon, expressed in 3-D space."""
    @staticmethod
    def verify_points(a: Vec3Like, b: Vec3Like, c: Vec3Like, d: Vec3Like = ...) -> bool:
        """Verifies that the indicated set of points will define a valid
        CollisionPolygon: that is, at least three non-collinear points, with no
        points repeated.
        """
    def is_valid(self) -> bool:
        """Returns true if the CollisionPolygon is valid (that is, it has at least
        three vertices), or false otherwise.
        """
    def is_concave(self) -> bool:
        """Returns true if the CollisionPolygon appears to be concave, or false if it
        is safely convex.
        """
    def get_points(self) -> tuple[LPoint3, ...]: ...
    getNumPoints = get_num_points
    getPoint = get_point
    verifyPoints = verify_points
    isValid = is_valid
    isConcave = is_concave
    getPoints = get_points

class CollisionHandlerEvent(CollisionHandler):
    """A specialized kind of CollisionHandler that throws an event for each
    collision detected.  The event thrown may be based on the name of the
    moving object or the struck object, or both.  The first parameter of the
    event will be a pointer to the CollisionEntry that triggered it.
    """

    @property
    def in_patterns(self) -> Sequence[str]: ...
    @property
    def again_patterns(self) -> Sequence[str]: ...
    @property
    def out_patterns(self) -> Sequence[str]: ...
    def __init__(self, __param0: CollisionHandlerEvent = ...) -> None:
        """The default CollisionHandlerEvent will throw no events.  Its pattern
        strings must first be set via a call to add_in_pattern() and/or
        add_out_pattern().
        """
    def clear_in_patterns(self) -> None:
        """Removes all of the previously-added in patterns.  See add_in_pattern."""
    def add_in_pattern(self, in_pattern: str) -> None:
        """Adds a pattern string to the list of events that will be generated in
        response to a collision.  The pattern string describes how the event name
        will be composed.  It is a string that may contain any of the following:

        %fn  - the name of the "from" object's node %in  - the name of the "into"
        object's node %fs  - 't' if "from" is tangible, 'i' if intangible %is  -
        't' if "into" is tangible, 'i' if intangible %ig  - 'c' if the collision is
        into a CollisionNode, 'g' if it is a geom.

        %(tag)fh - generate event only if "from" node has the indicated net tag.
        %(tag)fx - generate event only if "from" node does not have the indicated
        net tag.  %(tag)ih - generate event only if "into" node has the indicated
        net tag.  %(tag)ix - generate event only if "into" node does not have the
        indicated net tag.  %(tag)ft - the indicated net tag value of the "from"
        node.  %(tag)it - the indicated net tag value of the "into" node.

        Parentheses in the above are literal and should be included in the actual
        pattern.

        The event name will be based on the in_pattern string specified here, with
        all occurrences of the above strings replaced with the corresponding
        values.

        In general, the in_pattern event is thrown on the first detection of a
        collision between two particular nodes.  In subsequent passes, as long as a
        collision between those two nodes continues to be detected each frame, the
        again_pattern is thrown.  The first frame in which the collision is no
        longer detected, the out_pattern event is thrown.
        """
    def set_in_pattern(self, in_pattern: str) -> None:
        """This method is deprecated; it completely replaces all the in patterns that
        have previously been set with the indicated pattern.

        @deprecated Use add_in_pattern() instead.
        """
    def get_num_in_patterns(self) -> int:
        """Returns the number of in pattern strings that have been added."""
    def get_in_pattern(self, n: int) -> str:
        """Returns the nth pattern string that indicates how the event names are
        generated for each collision detected.  See add_in_pattern().
        """
    def clear_again_patterns(self) -> None:
        """Removes all of the previously-added in patterns.  See add_again_pattern."""
    def add_again_pattern(self, again_pattern: str) -> None:
        """Adds the pattern string that indicates how the event names are generated
        when a collision between two particular nodes is *still* detected.  This
        event is thrown each consecutive time a collision between two particular
        nodes is detected, starting with the second time.

        In general, the in_pattern event is thrown on the first detection of a
        collision between two particular nodes.  In subsequent passes, as long as a
        collision between those two nodes continues to be detected each frame, the
        again_pattern is thrown.  The first frame in which the collision is no
        longer detected, the out_pattern event is thrown.
        """
    def set_again_pattern(self, again_pattern: str) -> None:
        """This method is deprecated; it completely replaces all the in patterns that
        have previously been set with the indicated pattern.

        @deprecated Use add_again_pattern() instead.
        """
    def get_num_again_patterns(self) -> int:
        """Returns the number of in pattern strings that have been added."""
    def get_again_pattern(self, n: int) -> str:
        """Returns the nth pattern string that indicates how the event names are
        generated for each collision detected.  See add_again_pattern().
        """
    def clear_out_patterns(self) -> None:
        """Removes all of the previously-added in patterns.  See add_out_pattern."""
    def add_out_pattern(self, out_pattern: str) -> None:
        """Adds the pattern string that indicates how the event names are generated
        when a collision between two particular nodes is *no longer* detected.

        In general, the in_pattern event is thrown on the first detection of a
        collision between two particular nodes.  In subsequent passes, as long as a
        collision between those two nodes continues to be detected each frame, the
        again_pattern is thrown.  The first frame in which the collision is no
        longer detected, the out_pattern event is thrown.
        """
    def set_out_pattern(self, out_pattern: str) -> None:
        """This method is deprecated; it completely replaces all the in patterns that
        have previously been set with the indicated pattern.

        @deprecated Use add_out_pattern() instead.
        """
    def get_num_out_patterns(self) -> int:
        """Returns the number of in pattern strings that have been added."""
    def get_out_pattern(self, n: int) -> str:
        """Returns the nth pattern string that indicates how the event names are
        generated for each collision detected.  See add_out_pattern().
        """
    def clear(self) -> None:
        """Empties the list of elements that all colliders are known to be colliding
        with.  No "out" events will be thrown; if the same collision is detected
        next frame, a new "in" event will be thrown for each collision.

        This can be called each frame to defeat the persistent "in" event
        mechanism, which prevents the same "in" event from being thrown repeatedly.
        However, also see add_again_pattern(), which can be used to set the event
        that is thrown when a collision is detected for two or more consecutive
        frames.
        """
    def flush(self) -> None:
        """Same as clear() except "out" events are thrown."""
    def write_datagram(self, destination: Datagram) -> None:
        """Serializes this object, to implement pickle support."""
    def read_datagram(self, source: Datagram | DatagramIterator) -> None:
        """Restores the object state from the given datagram, previously obtained using
        __getstate__.
        """
    def get_in_patterns(self) -> tuple[str, ...]: ...
    def get_again_patterns(self) -> tuple[str, ...]: ...
    def get_out_patterns(self) -> tuple[str, ...]: ...
    clearInPatterns = clear_in_patterns
    addInPattern = add_in_pattern
    setInPattern = set_in_pattern
    getNumInPatterns = get_num_in_patterns
    getInPattern = get_in_pattern
    clearAgainPatterns = clear_again_patterns
    addAgainPattern = add_again_pattern
    setAgainPattern = set_again_pattern
    getNumAgainPatterns = get_num_again_patterns
    getAgainPattern = get_again_pattern
    clearOutPatterns = clear_out_patterns
    addOutPattern = add_out_pattern
    setOutPattern = set_out_pattern
    getNumOutPatterns = get_num_out_patterns
    getOutPattern = get_out_pattern
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getInPatterns = get_in_patterns
    getAgainPatterns = get_again_patterns
    getOutPatterns = get_out_patterns

class CollisionHandlerPhysical(CollisionHandlerEvent):
    """The abstract base class for a number of CollisionHandlers that have some
    physical effect on their moving bodies: they need to update the nodes'
    positions based on the effects of the collision.
    """

    center: NodePath
    def add_collider(self, collider: NodePath, target: NodePath, drive_interface: DriveInterface = ...) -> None:
        """`(self, collider: NodePath, target: NodePath)`:
        Adds a new collider to the list with a NodePath that will be updated with
        the collider's new position, or updates the existing collider with a new
        NodePath object.

        `(self, collider: NodePath, target: NodePath, drive_interface: DriveInterface)`:
        Adds a new collider to the list with a NodePath that will be updated with
        the collider's new position, or updates the existing collider with a new
        NodePath object.

        The indicated DriveInterface will also be updated with the target's new
        transform each frame.  This method should be used when the target is
        directly controlled by a DriveInterface.
        """
    def remove_collider(self, collider: NodePath) -> bool:
        """Removes the collider from the list of colliders that this handler knows
        about.
        """
    def has_collider(self, collider: NodePath) -> bool:
        """Returns true if the handler knows about the indicated collider, false
        otherwise.
        """
    def clear_colliders(self) -> None:
        """Completely empties the list of colliders this handler knows about."""
    def set_center(self, center: NodePath) -> None:
        """Specifies an arbitrary NodePath that the handler is always considered to be
        facing.  It does not detect collisions with surfaces that appear to be
        facing away from this NodePath.  This works best when the collision
        surfaces in question are polygons.
        """
    def clear_center(self) -> None:
        """Clears the center NodePath specified with set_center."""
    def get_center(self) -> NodePath:
        """Returns the NodePath specified with set_center, or the empty NodePath if
        nothing has been specified.
        """
    def has_center(self) -> bool:
        """Returns true if a NodePath has been specified with set_center(), false
        otherwise.
        """
    def has_contact(self) -> bool:
        """Did the handler make any contacts with anything on the last collision pass?
        Depending on how your world is setup, this can be used to tell if the
        handler is out of the world (i.e.  out of bounds). That is the original use
        of this call.
        """
    addCollider = add_collider
    removeCollider = remove_collider
    hasCollider = has_collider
    clearColliders = clear_colliders
    setCenter = set_center
    clearCenter = clear_center
    getCenter = get_center
    hasCenter = has_center
    hasContact = has_contact

class CollisionHandlerFloor(CollisionHandlerPhysical):
    """A specialized kind of CollisionHandler that sets the Z height of the
    collider to a fixed linear offset from the highest detected collision point
    each frame.  It's intended to implement walking around on a floor of
    varying height by casting a ray down from the avatar's head.
    """

    offset: float
    reach: float
    max_velocity: float
    def __init__(self) -> None: ...
    def set_offset(self, offset: float) -> None:
        """Sets the linear offset to add to (or subtract from) the highest detected
        collision point to determine the actual height at which to set the
        collider.
        """
    def get_offset(self) -> float:
        """Returns the linear offset to add to (or subtract from) the highest detected
        collision point to determine the actual height at which to set the
        collider.
        """
    def set_reach(self, reach: float) -> None:
        """Sets the reach to add to (or subtract from) the highest collision point"""
    def get_reach(self) -> float:
        """Returns the reach to add to (or subtract from) the highest collision point"""
    def set_max_velocity(self, max_vel: float) -> None:
        """Sets the maximum speed at which the object will be allowed to descend
        towards a floor below it, in units per second.  Set this to zero to allow
        it to instantly teleport any distance.
        """
    def get_max_velocity(self) -> float:
        """Retrieves the maximum speed at which the object will be allowed to descend
        towards a floor below it, in units per second.  See set_max_velocity().
        """
    setOffset = set_offset
    getOffset = get_offset
    setReach = set_reach
    getReach = get_reach
    setMaxVelocity = set_max_velocity
    getMaxVelocity = get_max_velocity

class CollisionHandlerPusher(CollisionHandlerPhysical):
    """A specialized kind of CollisionHandler that simply pushes back on things
    that attempt to move into solid walls.  This is the simplest kind of "real-
    world" collisions you can have.
    """

    horizontal: bool
    def __init__(self) -> None: ...
    def set_horizontal(self, flag: bool) -> None: ...
    def get_horizontal(self) -> bool: ...
    setHorizontal = set_horizontal
    getHorizontal = get_horizontal

class CollisionHandlerFluidPusher(CollisionHandlerPusher):
    """A CollisionHandlerPusher that makes use of timing and spatial information
    from fluid collisions to improve collision response
    """

class CollisionHandlerGravity(CollisionHandlerPhysical):
    """A specialized kind of CollisionHandler that sets the Z height of the
    collider to a fixed linear offset from the highest detected collision point
    each frame.  It's intended to implement walking around on a floor of
    varying height by casting a ray down from the avatar's head.
    """

    offset: float
    reach: float
    velocity: float
    gravity: float
    max_velocity: float
    @property
    def airborne_height(self) -> float: ...
    @property
    def on_ground(self) -> bool: ...
    @property
    def impact_velocity(self) -> float: ...
    @property
    def contact_normal(self) -> LVector3: ...
    def __init__(self) -> None: ...
    def set_offset(self, offset: float) -> None:
        """Sets the linear offset to add to (or subtract from) the highest detected
        collision point to determine the actual height at which to set the
        collider.
        """
    def get_offset(self) -> float:
        """Returns the linear offset to add to (or subtract from) the highest detected
        collision point to determine the actual height at which to set the
        collider.
        """
    def set_reach(self, reach: float) -> None:
        """Sets the reach to add to (or subtract from) the highest collision point"""
    def get_reach(self) -> float:
        """Returns the reach to add to (or subtract from) the highest collision point"""
    def get_airborne_height(self) -> float:
        """Return the height of the object from the ground.

        The object might not necessarily be at rest.  Use is_on_ground() if you
        want to know whether the object is on the ground and at rest.
        """
    def is_on_ground(self) -> bool:
        """Is the object at rest?"""
    def get_impact_velocity(self) -> float:
        """How hard did the object hit the ground.  This value is set on impact with
        the ground.  You may want to watch (poll) on is_on_ground() and when that is
        true, call get_impact_velocity(). Normally I avoid polling, but we are
        calling is_on_ground() frequently anyway.
        """
    def get_contact_normal(self) -> LVector3: ...
    def add_velocity(self, velocity: float) -> None:
        """Adds the sepcified amount to the current velocity.  This is mostly here
        allow this common operation to be faster for scripting, but it's also more
        concise even in cpp.
        """
    def set_velocity(self, velocity: float) -> None:
        """Sets the current vertical velocity."""
    def get_velocity(self) -> float:
        """Gets the current vertical velocity.

        Generally, negative values mean the object is in free fall; while postive
        values mean the object has vertical thrust.

        A zero value does not necessarily mean the object on the ground, it may
        also be weightless and/or at the apex of its jump.

        See Also: is_on_ground() and get_gravity()
        """
    def set_gravity(self, gravity: float) -> None:
        """Sets the linear gravity force (always plumb)."""
    def get_gravity(self) -> float:
        """Gets the linear gravity force (always plumb)."""
    def set_max_velocity(self, max_vel: float) -> None:
        """Sets the maximum speed at which the object will be allowed to descend
        towards a floor below it, in units per second.  Set this to zero to allow
        it to instantly teleport any distance.
        """
    def get_max_velocity(self) -> float:
        """Retrieves the maximum speed at which the object will be allowed to descend
        towards a floor below it, in units per second.  See set_max_velocity().
        """
    def set_legacy_mode(self, legacy_mode: bool) -> None:
        """Enables old behavior required by Toontown (Sellbot Factory lava room is
        good test case, lava and conveyor belt specifically). Behavior is to throw
        enter/exit events only for floor that the toon is in contact with
        """
    def get_legacy_mode(self) -> bool:
        """returns true if legacy mode is enabled"""
    setOffset = set_offset
    getOffset = get_offset
    setReach = set_reach
    getReach = get_reach
    getAirborneHeight = get_airborne_height
    isOnGround = is_on_ground
    getImpactVelocity = get_impact_velocity
    getContactNormal = get_contact_normal
    addVelocity = add_velocity
    setVelocity = set_velocity
    getVelocity = get_velocity
    setGravity = set_gravity
    getGravity = get_gravity
    setMaxVelocity = set_max_velocity
    getMaxVelocity = get_max_velocity
    setLegacyMode = set_legacy_mode
    getLegacyMode = get_legacy_mode

class CollisionHandlerHighestEvent(CollisionHandlerEvent):
    """A specialized kind of CollisionHandler that throws an event for each
    collision detected.  The event thrown may be based on the name of the
    moving object or the struck object, or both.  The first parameter of the
    event will be a pointer to the CollisionEntry that triggered it.
    """

    def __init__(self, __param0: CollisionHandlerHighestEvent = ...) -> None:
        """The default CollisionHandlerEvent will throw no events.  Its pattern
        strings must first be set via a call to add_in_pattern() and/or
        add_out_pattern().
        """

class CollisionHandlerQueue(CollisionHandler):
    """A special kind of CollisionHandler that does nothing except remember the
    CollisionEntries detected the last pass.  This set of CollisionEntries may
    then be queried by the calling function.  It's primarily useful when a
    simple intersection test is being made, e.g.  for picking from the window.
    """

    @property
    def entries(self) -> Sequence[CollisionEntry]: ...
    def __init__(self, __param0: CollisionHandlerQueue = ...) -> None: ...
    def sort_entries(self) -> None:
        """Sorts all the detected collisions front-to-back by
        from_intersection_point() so that those intersection points closest to the
        collider's origin (e.g., the center of the CollisionSphere, or the point_a
        of a CollisionSegment) appear first.
        """
    def clear_entries(self) -> None:
        """Removes all the entries from the queue."""
    def get_num_entries(self) -> int:
        """Returns the number of CollisionEntries detected last pass."""
    def get_entry(self, n: int) -> CollisionEntry:
        """Returns the nth CollisionEntry detected last pass."""
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def get_entries(self) -> tuple[CollisionEntry, ...]: ...
    sortEntries = sort_entries
    clearEntries = clear_entries
    getNumEntries = get_num_entries
    getEntry = get_entry
    getEntries = get_entries

class CollisionSphere(CollisionSolid):
    """A spherical collision volume or object."""

    center: LPoint3
    radius: float
    @overload
    def __init__(self, center: Vec3Like, radius: float) -> None: ...
    @overload
    def __init__(self, cx: float, cy: float, cz: float, radius: float) -> None: ...
    @overload
    def set_center(self, center: Vec3Like) -> None: ...
    @overload
    def set_center(self, x: float, y: float, z: float) -> None: ...
    def get_center(self) -> LPoint3: ...
    def set_radius(self, radius: float) -> None: ...
    def get_radius(self) -> float: ...
    setCenter = set_center
    getCenter = get_center
    setRadius = set_radius
    getRadius = get_radius

class CollisionInvSphere(CollisionSphere):
    """An inverted sphere: this is a sphere whose collision surface is the inside
    surface of the sphere.  Everything outside the sphere is solid matter;
    everything inside is empty space.  Useful for constraining objects to
    remain within a spherical perimeter.
    """

class CollisionRay(CollisionSolid):
    """An infinite ray, with a specific origin and direction.  It begins at its
    origin and continues in one direction to infinity, and it has no radius.
    Useful for picking from a window, or for gravity effects.
    """

    origin: LPoint3
    direction: LVector3
    @overload
    def __init__(self) -> None:
        """Creates an invalid ray.  This isn't terribly useful; it's expected that the
        user will subsequently adjust the ray via set_origin()/set_direction() or
        set_from_lens().
        """
    @overload
    def __init__(self, origin: Vec3Like, direction: Vec3Like) -> None: ...
    @overload
    def __init__(self, ox: float, oy: float, oz: float, dx: float, dy: float, dz: float) -> None: ...
    @overload
    def set_origin(self, origin: Vec3Like) -> None: ...
    @overload
    def set_origin(self, x: float, y: float, z: float) -> None: ...
    def get_origin(self) -> LPoint3: ...
    @overload
    def set_direction(self, direction: Vec3Like) -> None: ...
    @overload
    def set_direction(self, x: float, y: float, z: float) -> None: ...
    def get_direction(self) -> LVector3: ...
    @overload
    def set_from_lens(self, camera: LensNode, point: Vec2Like) -> bool:
        """`(self, camera: LensNode, point: LPoint2)`:
        Accepts a LensNode and a 2-d point in the range [-1,1].  Sets the
        CollisionRay so that it begins at the LensNode's near plane and extends to
        infinity, making it suitable for picking objects from the screen given a
        camera and a mouse location.

        Returns true if the point was acceptable, false otherwise.

        `(self, camera: LensNode, px: float, py: float)`:
        Accepts a LensNode and a 2-d point in the range [-1,1].  Sets the
        CollisionRay so that it begins at the LensNode's near plane and extends to
        infinity, making it suitable for picking objects from the screen given a
        camera and a mouse location.
        """
    @overload
    def set_from_lens(self, camera: LensNode, px: float, py: float) -> bool: ...
    setOrigin = set_origin
    getOrigin = get_origin
    setDirection = set_direction
    getDirection = get_direction
    setFromLens = set_from_lens

class CollisionLine(CollisionRay):
    """An infinite line, similar to a CollisionRay, except that it extends in both
    directions.  It is, however, directional.
    """

    @overload
    def __init__(self) -> None:
        """Creates an invalid line.  This isn't terribly useful; it's expected that
        the user will subsequently adjust the line via set_origin()/set_direction()
        or set_from_lens().
        """
    @overload
    def __init__(self, origin: Vec3Like, direction: Vec3Like) -> None: ...
    @overload
    def __init__(self, ox: float, oy: float, oz: float, dx: float, dy: float, dz: float) -> None: ...

class CollisionParabola(CollisionSolid):
    """This defines a parabolic arc, or subset of an arc, similar to the path of a
    projectile or falling object.  It is finite, having a specific beginning
    and end, but it is infinitely thin.

    Think of it as a wire bending from point t1 to point t2 along the path of a
    pre-defined parabola.
    """

    parabola: LParabola
    t1: float
    t2: float
    @overload
    def __init__(self) -> None:
        """`(self)`:
        Creates an invalid parabola.

        `(self, parabola: LParabola, t1: float, t2: float)`:
        Creates a parabola with the endpoints between t1 and t2 in the parametric
        space of the parabola.
        """
    @overload
    def __init__(self, parabola: LParabola, t1: float, t2: float) -> None: ...
    def set_parabola(self, parabola: LParabola) -> None:
        """Replaces the parabola specified by this solid."""
    def get_parabola(self) -> LParabola:
        """Returns the parabola specified by this solid."""
    def set_t1(self, t1: float) -> None:
        """Changes the starting point on the parabola."""
    def get_t1(self) -> float:
        """Returns the starting point on the parabola."""
    def set_t2(self, t2: float) -> None:
        """Changes the ending point on the parabola."""
    def get_t2(self) -> float:
        """Returns the ending point on the parabola."""
    setParabola = set_parabola
    getParabola = get_parabola
    setT1 = set_t1
    getT1 = get_t1
    setT2 = set_t2
    getT2 = get_t2

class CollisionSegment(CollisionSolid):
    """A finite line segment, with two specific endpoints but no thickness.  It's
    similar to a CollisionRay, except it does not continue to infinity.

    It does have an ordering, from point A to point B. If more than a single
    point of the segment is intersecting a solid, the reported intersection
    point is generally the closest on the segment to point A.
    """

    point_a: LPoint3
    point_b: LPoint3
    @overload
    def __init__(self) -> None:
        """Creates an invalid segment.  This isn't terribly useful; it's expected that
        the user will subsequently adjust the segment via
        set_origin()/set_direction() or set_from_lens().
        """
    @overload
    def __init__(self, a: Vec3Like, db: Vec3Like) -> None: ...
    @overload
    def __init__(self, ax: float, ay: float, az: float, bx: float, by: float, bz: float) -> None: ...
    @overload
    def set_point_a(self, a: Vec3Like) -> None: ...
    @overload
    def set_point_a(self, x: float, y: float, z: float) -> None: ...
    def get_point_a(self) -> LPoint3: ...
    @overload
    def set_point_b(self, b: Vec3Like) -> None: ...
    @overload
    def set_point_b(self, x: float, y: float, z: float) -> None: ...
    def get_point_b(self) -> LPoint3: ...
    @overload
    def set_from_lens(self, camera: LensNode, point: Vec2Like) -> bool:
        """`(self, camera: LensNode, point: LPoint2)`:
        Accepts a LensNode and a 2-d point in the range [-1,1].  Sets the
        CollisionSegment so that it begins at the LensNode's near plane and extends
        to the far plane, making it suitable for picking objects from the screen
        given a camera and a mouse location.

        Returns true if the point was acceptable, false otherwise.

        `(self, camera: LensNode, px: float, py: float)`:
        Accepts a LensNode and a 2-d point in the range [-1,1].  Sets the
        CollisionSegment so that it begins at the LensNode's near plane and extends
        to the far plane, making it suitable for picking objects from the screen
        given a camera and a mouse location.
        """
    @overload
    def set_from_lens(self, camera: LensNode, px: float, py: float) -> bool: ...
    setPointA = set_point_a
    getPointA = get_point_a
    setPointB = set_point_b
    getPointB = get_point_b
    setFromLens = set_from_lens

class CollisionVisualizer(PandaNode, CollisionRecorder):
    """This class is used to help debug the work the collisions system is doing.
    It shows the polygons that are detected as collisions, as well as those
    that are simply considered for collisions.

    It may be parented anywhere in the scene graph where it will be rendered to
    achieve this.
    """

    point_scale: float
    normal_scale: float
    @overload
    def __init__(self, copy: CollisionVisualizer) -> None:
        """Copy constructor."""
    @overload
    def __init__(self, name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def upcast_to_PandaNode(self) -> PandaNode: ...
    def upcast_to_CollisionRecorder(self) -> CollisionRecorder: ...
    def set_point_scale(self, point_scale: float) -> None:
        """Scales the points that are drawn to represent the surface and interior
        intersection points of the collisions.  By default, these objects are drawn
        at an arbitrary scale which is appropriate if the window units are the
        default range -1 .. 1.  Change this scale accordinatly if the window units
        are measured on some other scale or if you need to observe these objects in
        a smaller window.
        """
    def get_point_scale(self) -> float:
        """Returns the value last set by set_point_scale()."""
    def set_normal_scale(self, normal_scale: float) -> None:
        """Scales the line segments that are drawn to represent the normals of the
        collisions.  By default, these objects are drawn at an arbitrary scale
        which is appropriate if the scene units are measured in feet.  Change this
        scale accordinatly if the scene units are measured on some other scale or
        if you need to observe these normals from farther away.
        """
    def get_normal_scale(self) -> float:
        """Returns the value last set by set_normal_scale()."""
    def clear(self) -> None:
        """Removes all the visualization data from a previous traversal and resets the
        visualizer to empty.
        """
    upcastToPandaNode = upcast_to_PandaNode
    upcastToCollisionRecorder = upcast_to_CollisionRecorder
    setPointScale = set_point_scale
    getPointScale = get_point_scale
    setNormalScale = set_normal_scale
    getNormalScale = get_normal_scale

CollisionTube = CollisionCapsule
