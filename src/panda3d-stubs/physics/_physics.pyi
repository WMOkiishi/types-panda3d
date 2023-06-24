from collections.abc import Iterator, MutableSequence, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import Vec3Like, Vec4Like
from panda3d.core._collide import CollisionHandlerPusher
from panda3d.core._dtoolutil import ostream
from panda3d.core._express import ReferenceCount, TypedReferenceCount
from panda3d.core._linmath import LMatrix4, LOrientation, LPoint3, LQuaternionf, LRotation, LVector3
from panda3d.core._pgraph import NodePath, PandaNode

_LinearDistanceForce_FalloffType: TypeAlias = Literal[0, 1, 2]

class PhysicsObject(TypedReferenceCount):
    """A body on which physics will be applied.  If you're looking to add physical
    motion to your class, do NOT derive from this.  Derive from Physical
    instead.
    """

    active: bool
    mass: float
    position: LPoint3
    last_position: LPoint3
    velocity: LVector3
    terminal_velocity: float
    oriented: bool
    orientation: LOrientation
    rotation: LRotation
    @property
    def implicit_velocity(self) -> LVector3: ...
    def __init__(self, copy: PhysicsObject = ...) -> None:
        """`(self)`:
        Default Constructor

        `(self, copy: PhysicsObject)`:
        copy constructor
        """
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, other: Self) -> Self: ...
    def set_active(self, flag: bool) -> None:
        """Process Flag assignment"""
    def get_active(self) -> bool:
        """Process Flag Query"""
    def set_mass(self, __param0: float) -> None:
        """Set the mass in slugs (or kilograms)."""
    def get_mass(self) -> float:
        """Get the mass in slugs (or kilograms)."""
    @overload
    def set_position(self, pos: Vec3Like) -> None:
        """`(self, pos: LPoint3)`:
        Vector position assignment.  This is also used as the center of mass.

        `(self, x: float, y: float, z: float)`:
        Piecewise position assignment
        """
    @overload
    def set_position(self, x: float, y: float, z: float) -> None: ...
    def get_position(self) -> LPoint3:
        """Position Query"""
    def reset_position(self, pos: Vec3Like) -> None:
        """use this to place an object in a completely new position, that has nothing
        to do with its last position.
        """
    def set_last_position(self, pos: Vec3Like) -> None:
        """Last position assignment"""
    def get_last_position(self) -> LPoint3:
        """Get the position of the physics object at the start of the most recent
        do_physics.
        """
    @overload
    def set_velocity(self, vel: Vec3Like) -> None:
        """`(self, vel: LVector3)`:
        Vector velocity assignment

        `(self, x: float, y: float, z: float)`:
        Piecewise velocity assignment
        """
    @overload
    def set_velocity(self, x: float, y: float, z: float) -> None: ...
    def get_velocity(self) -> LVector3:
        """Velocity Query per second"""
    def get_implicit_velocity(self) -> LVector3:
        """Velocity Query over the last dt"""
    def add_torque(self, torque: Vec4Like) -> None:
        """Adds an torque force (i.e.  an instantanious change in velocity).  This is
        a quicker way to get the angular velocity, add a vector to it and set that
        value to be the new angular velocity.
        """
    def add_impulse(self, impulse: Vec3Like) -> None:
        """Adds an impulse force (i.e.  an instantanious change in velocity).  This is
        a quicker way to get the velocity, add a vector to it and set that value to
        be the new velocity.
        """
    def add_impact(self, offset_from_center_of_mass: Vec3Like, impulse: Vec3Like) -> None:
        """Adds an impulse and/or torque (i.e.  an instantanious change in velocity)
        based on how well the offset and impulse align with the center of mass (aka
        position). If you wanted to immitate this function you could work out the
        impulse and torque and call add_impulse and add_torque respectively.
        offset and force are in global (or parent) coordinates.
        """
    def add_local_torque(self, torque: Vec4Like) -> None:
        """Adds an torque force (i.e.  an instantanious change in velocity).  This is
        a quicker way to get the angular velocity, add a vector to it and set that
        value to be the new angular velocity.
        """
    def add_local_impulse(self, impulse: Vec3Like) -> None:
        """Adds an impulse force (i.e.  an instantanious change in velocity).  This is
        a quicker way to get the velocity, add a vector to it and set that value to
        be the new velocity.
        """
    def add_local_impact(self, offset_from_center_of_mass: Vec3Like, impulse: Vec3Like) -> None:
        """Adds an impulse and/or torque (i.e.  an instantanious change in velocity)
        based on how well the offset and impulse align with the center of mass (aka
        position). If you wanted to immitate this function you could work out the
        impulse and torque and call add_impulse and add_torque respectively.
        offset and force are in local coordinates.
        """
    def set_terminal_velocity(self, tv: float) -> None:
        """tv assignment"""
    def get_terminal_velocity(self) -> float:
        """tv query"""
    def set_oriented(self, flag: bool) -> None:
        """Set flag to determine whether this object should do any rotation or
        orientation calculations.  Optimization.
        """
    def get_oriented(self) -> bool:
        """See set_oriented()."""
    def set_orientation(self, orientation: LQuaternionf) -> None: ...
    def get_orientation(self) -> LOrientation:
        """get current orientation."""
    def reset_orientation(self, orientation: LQuaternionf) -> None:
        """set the orientation while clearing the rotation velocity."""
    def set_rotation(self, rotation: Vec4Like) -> None:
        """set rotation as a quaternion delta per second."""
    def get_rotation(self) -> LRotation:
        """get rotation per second."""
    def get_inertial_tensor(self) -> LMatrix4:
        """returns a transform matrix that represents the object's willingness to be
        forced.
        """
    def get_lcs(self) -> LMatrix4:
        """returns a transform matrix to this object's local coordinate system."""
    def make_copy(self) -> PhysicsObject:
        """dynamic copy."""
    def set_name(self, name: str) -> None: ...
    def get_name(self) -> str: ...
    def output(self, out: ostream) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    setActive = set_active
    getActive = get_active
    setMass = set_mass
    getMass = get_mass
    setPosition = set_position
    getPosition = get_position
    resetPosition = reset_position
    setLastPosition = set_last_position
    getLastPosition = get_last_position
    setVelocity = set_velocity
    getVelocity = get_velocity
    getImplicitVelocity = get_implicit_velocity
    addTorque = add_torque
    addImpulse = add_impulse
    addImpact = add_impact
    addLocalTorque = add_local_torque
    addLocalImpulse = add_local_impulse
    addLocalImpact = add_local_impact
    setTerminalVelocity = set_terminal_velocity
    getTerminalVelocity = get_terminal_velocity
    setOriented = set_oriented
    getOriented = get_oriented
    setOrientation = set_orientation
    getOrientation = get_orientation
    resetOrientation = reset_orientation
    setRotation = set_rotation
    getRotation = get_rotation
    getInertialTensor = get_inertial_tensor
    getLcs = get_lcs
    makeCopy = make_copy
    setName = set_name
    getName = get_name

class PhysicsObjectCollection:
    """This is a set of zero or more PhysicsObjects.  It's handy for returning
    from functions that need to return multiple PhysicsObjects.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: PhysicsObjectCollection = ...) -> None: ...
    def __getitem__(self, index: int) -> PhysicsObject: ...
    def __len__(self) -> int:
        """Returns the number of physics objects in the collection.  This is the same
        thing as get_num_physics_objects().
        """
    def __iadd__(self, other: PhysicsObjectCollection) -> Self: ...
    def __add__(self, other: PhysicsObjectCollection) -> PhysicsObjectCollection: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def __iter__(self) -> Iterator[PhysicsObject]: ...  # Doesn't actually exist
    def assign(self, copy: Self) -> Self: ...
    def add_physics_object(self, physics_object: PhysicsObject) -> None:
        """Adds a new PhysicsObject to the collection."""
    def remove_physics_object(self, physics_object: PhysicsObject) -> bool:
        """Removes the indicated PhysicsObject from the collection.  Returns true if
        the physics_object was removed, false if it was not a member of the
        collection.
        """
    def add_physics_objects_from(self, other: PhysicsObjectCollection) -> None:
        """Adds all the PhysicsObjects indicated in the other collection to this
        collection.  The other physics_objects are simply appended to the end of
        the physics_objects in this list; duplicates are not automatically removed.
        """
    def remove_physics_objects_from(self, other: PhysicsObjectCollection) -> None:
        """Removes from this collection all of the PhysicsObjects listed in the other
        collection.
        """
    def remove_duplicate_physics_objects(self) -> None:
        """Removes any duplicate entries of the same PhysicsObjects on this
        collection.  If a PhysicsObject appears multiple times, the first
        appearance is retained; subsequent appearances are removed.
        """
    def has_physics_object(self, physics_object: PhysicsObject) -> bool:
        """Returns true if the indicated PhysicsObject appears in this collection,
        false otherwise.
        """
    def clear(self) -> None:
        """Removes all PhysicsObjects from the collection."""
    def is_empty(self) -> bool:
        """Returns true if there are no PhysicsObjects in the collection, false
        otherwise.
        """
    def get_num_physics_objects(self) -> int:
        """Returns the number of PhysicsObjects in the collection."""
    def get_physics_object(self, index: int) -> PhysicsObject:
        """Returns the nth PhysicsObject in the collection."""
    def output(self, out: ostream) -> None:
        """Writes a brief one-line description of the PhysicsObjectCollection to the
        indicated output stream.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes a complete multi-line description of the PhysicsObjectCollection to
        the indicated output stream.
        """
    def get_physics_objects(self) -> tuple[PhysicsObject, ...]: ...
    addPhysicsObject = add_physics_object
    removePhysicsObject = remove_physics_object
    addPhysicsObjectsFrom = add_physics_objects_from
    removePhysicsObjectsFrom = remove_physics_objects_from
    removeDuplicatePhysicsObjects = remove_duplicate_physics_objects
    hasPhysicsObject = has_physics_object
    isEmpty = is_empty
    getNumPhysicsObjects = get_num_physics_objects
    getPhysicsObject = get_physics_object
    getPhysicsObjects = get_physics_objects

class BaseForce(TypedReferenceCount):
    """pure virtual base class for all forces that could POSSIBLY exist."""

    def get_active(self) -> bool: ...
    def set_active(self, active: bool) -> None: ...
    def is_linear(self) -> bool: ...
    def get_force_node(self) -> ForceNode: ...
    def get_force_node_path(self) -> NodePath: ...
    def output(self, out: ostream) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    getActive = get_active
    setActive = set_active
    isLinear = is_linear
    getForceNode = get_force_node
    getForceNodePath = get_force_node_path

class LinearForce(BaseForce):
    """A force that acts on a PhysicsObject by way of an Integrator.  This is a
    pure virtual base class.
    """

    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_amplitude(self, a: float) -> None: ...
    def set_mass_dependent(self, m: bool) -> None: ...
    def get_amplitude(self) -> float: ...
    def get_mass_dependent(self) -> bool: ...
    def set_vector_masks(self, x: bool, y: bool, z: bool) -> None: ...
    def get_vector_masks(self) -> LVector3: ...
    def get_vector(self, po: PhysicsObject) -> LVector3: ...
    def make_copy(self) -> LinearForce: ...
    setAmplitude = set_amplitude
    setMassDependent = set_mass_dependent
    getAmplitude = get_amplitude
    getMassDependent = get_mass_dependent
    setVectorMasks = set_vector_masks
    getVectorMasks = get_vector_masks
    getVector = get_vector
    makeCopy = make_copy

class AngularForce(BaseForce):
    """pure virtual parent of all quat-based forces."""

    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def make_copy(self) -> AngularForce: ...
    def get_quat(self, po: PhysicsObject) -> LRotation:
        """access query"""
    makeCopy = make_copy
    getQuat = get_quat

class Physical(TypedReferenceCount):
    """Defines a set of physically modeled attributes.  If you want physics
    applied to your class, derive it from this.
    """

    @property
    def linear_forces(self) -> Sequence[LinearForce]: ...
    @property
    def angular_forces(self) -> Sequence[AngularForce]: ...
    @property
    def viscosity(self) -> float: ...
    @property
    def objects(self) -> PhysicsObjectCollection: ...
    @overload
    def __init__(self, total_objects: int = ..., pre_alloc: bool = ...) -> None:
        """`(self, copy: Physical)`:
        copy constructor (note- does deep copy of pn's) but does NOT attach itself
        to its template's physicsmanager.

        `(self, total_objects: int = ..., pre_alloc: bool = ...)`:
        Default Constructor The idea here is that most physicals will NOT be
        collections of sets (i.e.  particle systems and whatever else).  Because of
        this, the default constructor, unless otherwise specified, will
        automatically allocate and initialize one PhysicalObject.  This makes it
        easier for high-level work.

        pre-alloc is ONLY for multiple-object physicals, and if true, fills the
        physics_object vector with dead nodes, pre-allocating for the speed end of
        the speed-vs-overhead deal.
        """
    @overload
    def __init__(self, copy: Physical) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_physics_manager(self) -> PhysicsManager:
        """helpers"""
    def get_physical_node(self) -> PhysicalNode: ...
    def get_physical_node_path(self) -> NodePath: ...
    def get_phys_body(self) -> PhysicsObject: ...
    def clear_linear_forces(self) -> None:
        """Erases the linear force list"""
    def clear_angular_forces(self) -> None:
        """Erases the angular force list"""
    def clear_physics_objects(self) -> None:
        """Erases the object list"""
    def add_linear_force(self, f: LinearForce) -> None:
        """Adds a linear force to the force list"""
    def add_angular_force(self, f: AngularForce) -> None:
        """Adds an angular force to the force list"""
    def add_physics_object(self, po: PhysicsObject) -> None:
        """Adds an object to the physics object vector"""
    def remove_linear_force(self, f: LinearForce) -> None:
        """removes a linear force from the force list"""
    def remove_angular_force(self, f: AngularForce) -> None:
        """removes an angular force from the force list"""
    def get_num_linear_forces(self) -> int: ...
    def get_linear_force(self, index: int) -> LinearForce: ...
    def get_num_angular_forces(self) -> int: ...
    def get_angular_force(self, index: int) -> AngularForce: ...
    def set_viscosity(self, viscosity: float) -> None:
        """Set the local viscosity."""
    def get_viscosity(self) -> float:
        """Get the local viscosity."""
    def get_objects(self) -> PhysicsObjectCollection: ...
    def output(self, out: ostream = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def write_physics_objects(self, out: ostream = ..., indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def write_linear_forces(self, out: ostream = ..., indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def write_angular_forces(self, out: ostream = ..., indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream = ..., indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def get_linear_forces(self) -> tuple[LinearForce, ...]: ...
    def get_angular_forces(self) -> tuple[AngularForce, ...]: ...
    getPhysicsManager = get_physics_manager
    getPhysicalNode = get_physical_node
    getPhysicalNodePath = get_physical_node_path
    getPhysBody = get_phys_body
    clearLinearForces = clear_linear_forces
    clearAngularForces = clear_angular_forces
    clearPhysicsObjects = clear_physics_objects
    addLinearForce = add_linear_force
    addAngularForce = add_angular_force
    addPhysicsObject = add_physics_object
    removeLinearForce = remove_linear_force
    removeAngularForce = remove_angular_force
    getNumLinearForces = get_num_linear_forces
    getLinearForce = get_linear_force
    getNumAngularForces = get_num_angular_forces
    getAngularForce = get_angular_force
    setViscosity = set_viscosity
    getViscosity = get_viscosity
    getObjects = get_objects
    writePhysicsObjects = write_physics_objects
    writeLinearForces = write_linear_forces
    writeAngularForces = write_angular_forces
    getLinearForces = get_linear_forces
    getAngularForces = get_angular_forces

class PhysicalNode(PandaNode):
    """Graph node that encapsulated a series of physical objects"""

    @property
    def physicals(self) -> MutableSequence[Physical]: ...
    def __init__(self, name: str) -> None:
        """default constructor"""
    def clear(self) -> None: ...
    def get_physical(self, index: int) -> Physical: ...
    def get_num_physicals(self) -> int: ...
    def add_physical(self, physical: Physical) -> None:
        """Adds a Physical to this PhysicalNode.  If it is already added to this node,
        does nothing.  It is an error to add a Physical to multiple PhysicalNodes.
        """
    def add_physicals_from(self, other: PhysicalNode) -> None:
        """append operation"""
    def set_physical(self, index: int, physical: Physical) -> None:
        """replace operation"""
    def insert_physical(self, index: int, physical: Physical) -> None:
        """insert operation"""
    @overload
    def remove_physical(self, physical: Physical) -> None:
        """remove operation"""
    @overload
    def remove_physical(self, index: int) -> None: ...
    def get_physicals(self) -> tuple[Physical, ...]: ...
    getPhysical = get_physical
    getNumPhysicals = get_num_physicals
    addPhysical = add_physical
    addPhysicalsFrom = add_physicals_from
    setPhysical = set_physical
    insertPhysical = insert_physical
    removePhysical = remove_physical
    getPhysicals = get_physicals

class ActorNode(PhysicalNode):
    """Like a physical node, but with a little more.  The actornode assumes
    responsibility for its own transform, and changes in its own PhysicsObject
    will be reflected as transforms.  This relation goes both ways; changes in
    the transform will update the object's position (shoves).
    """

    @overload
    def __init__(self, name: str = ...) -> None:
        """`(self, copy: ActorNode)`:
        Copy Constructor.

        `(self, name: str = ...)`:
        Constructor
        """
    @overload
    def __init__(self, copy: ActorNode) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_physics_object(self) -> PhysicsObject: ...
    def set_contact_vector(self, contact_vector: Vec3Like) -> None: ...
    def get_contact_vector(self) -> LVector3: ...
    def update_transform(self) -> None:
        """this sets the transform generated by the contained Physical, moving the
        node and subsequent geometry.  i.e.  copy from PhysicsObject to PandaNode
        """
    def set_transform_limit(self, limit: float) -> None: ...
    getPhysicsObject = get_physics_object
    setContactVector = set_contact_vector
    getContactVector = get_contact_vector
    updateTransform = update_transform
    setTransformLimit = set_transform_limit

class BaseIntegrator(ReferenceCount):
    """pure virtual integrator class that holds cached matrix information that
    really should be common to any possible child implementation.
    """

    def __init__(self, __param0: BaseIntegrator) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def output(self, out: ostream) -> None:
        """Write a string representation of this instance to <out>."""
    def write_precomputed_linear_matrices(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def write_precomputed_angular_matrices(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    writePrecomputedLinearMatrices = write_precomputed_linear_matrices
    writePrecomputedAngularMatrices = write_precomputed_angular_matrices

class AngularIntegrator(BaseIntegrator):
    """Pure virtual base class for physical modeling.  Takes physically modelable
    objects and applies forces to them.
    """

class AngularEulerIntegrator(AngularIntegrator):
    """Performs Euler integration on a vector of physically modelable objects
    given a quantum dt.
    """

    def __init__(self) -> None:
        """constructor"""

class AngularVectorForce(AngularForce):
    """a simple directed torque force, the angular equivalent of simple vector
    force.
    """

    @overload
    def __init__(self, copy: AngularVectorForce) -> None:
        """`(self, copy: AngularVectorForce)`:
        copy constructor

        `(self, quat: LRotation)`; `(self, h: float, p: float, r: float)`:
        constructor
        """
    @overload
    def __init__(self, quat: Vec4Like) -> None: ...
    @overload
    def __init__(self, h: float, p: float, r: float) -> None: ...
    def set_quat(self, quat: Vec4Like) -> None: ...
    def set_hpr(self, h: float, p: float, r: float) -> None: ...
    def get_local_quat(self) -> LRotation: ...
    setQuat = set_quat
    setHpr = set_hpr
    getLocalQuat = get_local_quat

class ForceNode(PandaNode):
    """A force that lives in the scene graph and is therefore subject to local
    coordinate systems.  An example of this would be simulating gravity in a
    rotating space station.  or something.
    """

    @property
    def forces(self) -> MutableSequence[BaseForce]: ...
    def __init__(self, name: str) -> None:
        """default constructor"""
    def clear(self) -> None: ...
    def get_force(self, index: int) -> BaseForce: ...
    def get_num_forces(self) -> int: ...
    def add_force(self, force: BaseForce) -> None: ...
    def add_forces_from(self, other: ForceNode) -> None:
        """append operation"""
    def set_force(self, index: int, force: BaseForce) -> None:
        """replace operation"""
    def insert_force(self, index: int, force: BaseForce) -> None:
        """insert operation"""
    @overload
    def remove_force(self, force: BaseForce) -> None:
        """remove operation"""
    @overload
    def remove_force(self, index: int) -> None: ...
    def write_forces(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def get_forces(self) -> tuple[BaseForce, ...]: ...
    getForce = get_force
    getNumForces = get_num_forces
    addForce = add_force
    addForcesFrom = add_forces_from
    setForce = set_force
    insertForce = insert_force
    removeForce = remove_force
    writeForces = write_forces
    getForces = get_forces

class LinearControlForce(LinearForce):
    """Simple directed vector force.  This force is different from the others in
    that it can be global and still only affect a single object.  That might
    not make sense for a physics simulation, but it's very handy for a game.
    I.e.  this is the force applied by user on the selected object.
    """

    @overload
    def __init__(self, po: PhysicsObject = ..., a: float = ..., mass: bool = ...) -> None:
        """`(self, copy: LinearControlForce)`:
        Copy Constructor

        `(self, po: PhysicsObject = ..., a: float = ..., mass: bool = ...)`:
        Vector Constructor
        """
    @overload
    def __init__(self, copy: LinearControlForce) -> None: ...
    def clear_physics_object(self) -> None:
        """encapsulating wrapper"""
    def set_physics_object(self, po: PhysicsObject) -> None:
        """encapsulating wrapper"""
    def get_physics_object(self) -> PhysicsObject:
        """piecewise encapsulating wrapper"""
    @overload
    def set_vector(self, v: Vec3Like) -> None:
        """`(self, v: LVector3)`:
        encapsulating wrapper

        `(self, x: float, y: float, z: float)`:
        piecewise encapsulating wrapper
        """
    @overload
    def set_vector(self, x: float, y: float, z: float) -> None: ...
    def get_local_vector(self) -> LVector3: ...
    clearPhysicsObject = clear_physics_object
    setPhysicsObject = set_physics_object
    getPhysicsObject = get_physics_object
    setVector = set_vector
    getLocalVector = get_local_vector

class LinearCylinderVortexForce(LinearForce):
    """Defines a cylinder inside of which all forces are tangential to the theta
    of the particle wrt the z-axis in local coord.  space.  This happens by
    assigning the force a node by which the cylinder is transformed.  Be
    warned- this will suck anything that it can reach directly into orbit and
    will NOT let go.
    """

    @overload
    def __init__(self, radius: float = ..., length: float = ..., coef: float = ..., a: float = ..., md: bool = ...) -> None:
        """`(self, copy: LinearCylinderVortexForce)`:
        copy Constructor

        `(self, radius: float = ..., length: float = ..., coef: float = ..., a: float = ..., md: bool = ...)`:
        Simple Constructor
        """
    @overload
    def __init__(self, copy: LinearCylinderVortexForce) -> None: ...
    def set_coef(self, coef: float) -> None: ...
    def get_coef(self) -> float: ...
    def set_radius(self, radius: float) -> None: ...
    def get_radius(self) -> float: ...
    def set_length(self, length: float) -> None: ...
    def get_length(self) -> float: ...
    setCoef = set_coef
    getCoef = get_coef
    setRadius = set_radius
    getRadius = get_radius
    setLength = set_length
    getLength = get_length

class LinearDistanceForce(LinearForce):
    """Pure virtual class for sinks and sources"""

    FT_ONE_OVER_R: Final = 0
    FTONEOVERR: Final = 0
    FT_ONE_OVER_R_SQUARED: Final = 1
    FTONEOVERRSQUARED: Final = 1
    FT_ONE_OVER_R_CUBED: Final = 2
    FTONEOVERRCUBED: Final = 2
    def set_radius(self, r: float) -> None:
        """set the radius"""
    def set_falloff_type(self, ft: _LinearDistanceForce_FalloffType) -> None:
        """falloff_type encapsulating wrap"""
    def set_force_center(self, p: Vec3Like) -> None:
        """set the force center"""
    def get_radius(self) -> float:
        """radius query"""
    def get_falloff_type(self) -> _LinearDistanceForce_FalloffType:
        """falloff_type query"""
    def get_force_center(self) -> LPoint3:
        """force_center query"""
    def get_scalar_term(self) -> float:
        """calculate the term based on falloff"""
    setRadius = set_radius
    setFalloffType = set_falloff_type
    setForceCenter = set_force_center
    getRadius = get_radius
    getFalloffType = get_falloff_type
    getForceCenter = get_force_center
    getScalarTerm = get_scalar_term

class LinearIntegrator(BaseIntegrator):
    """Pure virtual base class for physical modeling.  Takes physically modelable
    objects and applies forces to them.
    """

class LinearEulerIntegrator(LinearIntegrator):
    """Performs Euler integration on a vector of physically modelable objects
    given a quantum dt.
    """

    def __init__(self) -> None:
        """constructor"""

class LinearFrictionForce(LinearForce):
    """Friction-based drag force"""

    @overload
    def __init__(self, coef: float = ..., a: float = ..., m: bool = ...) -> None:
        """`(self, copy: LinearFrictionForce)`:
        copy constructor

        `(self, coef: float = ..., a: float = ..., m: bool = ...)`:
        Constructor
        """
    @overload
    def __init__(self, copy: LinearFrictionForce) -> None: ...
    def set_coef(self, coef: float) -> None: ...
    def get_coef(self) -> float: ...
    setCoef = set_coef
    getCoef = get_coef

class LinearRandomForce(LinearForce):
    """Pure virtual, parent to noiseForce and jitterForce"""

class LinearJitterForce(LinearRandomForce):
    """Completely random noise force vector.  Not repeatable, reliable, or
    predictable.
    """

    @overload
    def __init__(self, a: float = ..., m: bool = ...) -> None:
        """`(self, copy: LinearJitterForce)`:
        copy constructor

        `(self, a: float = ..., m: bool = ...)`:
        constructor
        """
    @overload
    def __init__(self, copy: LinearJitterForce) -> None: ...

class LinearNoiseForce(LinearRandomForce):
    """Repeating noise force vector."""

    @overload
    def __init__(self, a: float = ..., m: bool = ...) -> None:
        """`(self, copy: LinearNoiseForce)`:
        copy constructor

        `(self, a: float = ..., m: bool = ...)`:
        constructor
        """
    @overload
    def __init__(self, copy: LinearNoiseForce) -> None: ...

class LinearSinkForce(LinearDistanceForce):
    """Attractor force.  Think black hole."""

    @overload
    def __init__(self, copy: LinearSinkForce = ...) -> None:
        """`(self)`; `(self, p: LPoint3, f: _LinearDistanceForce_FalloffType, r: float, a: float = ..., m: bool = ...)`:
        Simple constructor

        `(self, copy: LinearSinkForce)`:
        copy constructor
        """
    @overload
    def __init__(self, p: Vec3Like, f: _LinearDistanceForce_FalloffType, r: float, a: float = ..., m: bool = ...) -> None: ...

class LinearSourceForce(LinearDistanceForce):
    """Repellant force."""

    @overload
    def __init__(self, copy: LinearSourceForce = ...) -> None:
        """`(self)`; `(self, p: LPoint3, f: _LinearDistanceForce_FalloffType, r: float, a: float = ..., mass: bool = ...)`:
        Simple constructor

        `(self, copy: LinearSourceForce)`:
        copy constructor
        """
    @overload
    def __init__(self, p: Vec3Like, f: _LinearDistanceForce_FalloffType, r: float, a: float = ..., mass: bool = ...) -> None: ...

class LinearUserDefinedForce(LinearForce):
    """A programmable force that takes an evaluator function."""

    def __init__(self, copy: LinearUserDefinedForce) -> None:
        """copy constructor"""

class LinearVectorForce(LinearForce):
    """Simple directed vector force.  Suitable for gravity, non-turbulent wind,
    etc...
    """

    @overload
    def __init__(self, x: float = ..., y: float = ..., z: float = ..., a: float = ..., mass: bool = ...) -> None:
        """`(self, vec: LVector3, a: float = ..., mass: bool = ...)`:
        Vector Constructor

        `(self, copy: LinearVectorForce)`:
        Copy Constructor

        `(self, x: float = ..., y: float = ..., z: float = ..., a: float = ..., mass: bool = ...)`:
        Default/Piecewise constructor
        """
    @overload
    def __init__(self, copy: LinearVectorForce) -> None: ...
    @overload
    def __init__(self, vec: Vec3Like, a: float = ..., mass: bool = ...) -> None: ...
    @overload
    def set_vector(self, v: Vec3Like) -> None:
        """`(self, v: LVector3)`:
        encapsulating wrapper

        `(self, x: float, y: float, z: float)`:
        piecewise encapsulating wrapper
        """
    @overload
    def set_vector(self, x: float, y: float, z: float) -> None: ...
    def get_local_vector(self) -> LVector3: ...
    setVector = set_vector
    getLocalVector = get_local_vector

class PhysicsCollisionHandler(CollisionHandlerPusher):
    """A specialized kind of CollisionHandler that simply pushes back on things
    that attempt to move into solid walls.  This also puts forces onto the
    physics objects
    """

    def set_almost_stationary_speed(self, speed: float) -> None:
        """These setters and getter are a bit of a hack:"""
    def get_almost_stationary_speed(self) -> float: ...
    def set_static_friction_coef(self, coef: float) -> None: ...
    def get_static_friction_coef(self) -> float: ...
    def set_dynamic_friction_coef(self, coef: float) -> None: ...
    def get_dynamic_friction_coef(self) -> float: ...
    setAlmostStationarySpeed = set_almost_stationary_speed
    getAlmostStationarySpeed = get_almost_stationary_speed
    setStaticFrictionCoef = set_static_friction_coef
    getStaticFrictionCoef = get_static_friction_coef
    setDynamicFrictionCoef = set_dynamic_friction_coef
    getDynamicFrictionCoef = get_dynamic_friction_coef

class PhysicsManager:
    """Physics don't get much higher-level than this.  Attach as many Physicals
    (particle systems, etc..) as you want, pick an integrator and go.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: PhysicsManager = ...) -> None:
        """Default Constructor.  NOTE: EulerIntegrator is the standard default."""
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def attach_linear_integrator(self, i: LinearIntegrator) -> None:
        """Hooks a linear integrator into the manager"""
    def attach_angular_integrator(self, i: AngularIntegrator) -> None:
        """Hooks an angular integrator into the manager"""
    def attach_physical(self, p: Physical) -> None:
        """Registers a Physical class with the manager"""
    def attach_physicalnode(self, p: PhysicalNode) -> None:
        """Please call attach_physical_node instead."""
    def attach_physical_node(self, p: PhysicalNode) -> None:
        """Registers a physicalnode with the manager"""
    def add_linear_force(self, f: LinearForce) -> None:
        """Adds a global linear force to the physics manager"""
    def add_angular_force(self, f: AngularForce) -> None:
        """Adds a global angular force to the physics manager"""
    def clear_linear_forces(self) -> None:
        """Resets the physics manager force vector"""
    def clear_angular_forces(self) -> None:
        """Resets the physics manager force vector"""
    def clear_physicals(self) -> None:
        """Resets the physics manager objects vector"""
    def set_viscosity(self, viscosity: float) -> None:
        """Set the global viscosity."""
    def get_viscosity(self) -> float:
        """Get the global viscosity."""
    def remove_physical(self, p: Physical) -> None:
        """takes a physical out of the object list"""
    def remove_physical_node(self, p: PhysicalNode) -> None:
        """Removes a physicalnode from the manager"""
    def remove_linear_force(self, f: LinearForce) -> None:
        """takes a linear force out of the physics list"""
    def remove_angular_force(self, f: AngularForce) -> None:
        """takes an angular force out of the physics list"""
    def do_physics(self, dt: float, p: Physical = ...) -> None:
        """`(self, dt: float)`:
        This is the main high-level API call.  Performs integration on every
        attached Physical.

        `(self, dt: float, p: Physical)`:
        This is the main high-level API call.  Performs integration on a single
        physical.  Make sure its associated forces are active.
        """
    def init_random_seed(self) -> None:
        """One-time config function, sets up the random seed used by the physics and
        particle systems.  For synchronizing across distributed computers
        """
    def output(self, out: ostream) -> None:
        """Write a string representation of this instance to <out>."""
    def write_physicals(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def write_linear_forces(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def write_angular_forces(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def debug_output(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    attachLinearIntegrator = attach_linear_integrator
    attachAngularIntegrator = attach_angular_integrator
    attachPhysical = attach_physical
    attachPhysicalnode = attach_physicalnode
    attachPhysicalNode = attach_physical_node
    addLinearForce = add_linear_force
    addAngularForce = add_angular_force
    clearLinearForces = clear_linear_forces
    clearAngularForces = clear_angular_forces
    clearPhysicals = clear_physicals
    setViscosity = set_viscosity
    getViscosity = get_viscosity
    removePhysical = remove_physical
    removePhysicalNode = remove_physical_node
    removeLinearForce = remove_linear_force
    removeAngularForce = remove_angular_force
    doPhysics = do_physics
    initRandomSeed = init_random_seed
    writePhysicals = write_physicals
    writeLinearForces = write_linear_forces
    writeAngularForces = write_angular_forces
    debugOutput = debug_output
