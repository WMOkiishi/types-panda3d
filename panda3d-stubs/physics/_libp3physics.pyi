from collections.abc import Sequence
from typing import Any, ClassVar, Literal, TypeAlias, overload
from panda3d.core import (
    CollisionHandlerPusher,
    ConfigVariableColor,
    LMatrix3f,
    LMatrix4f,
    LOrientationf,
    LPoint3f,
    LRotationf,
    LVecBase3f,
    LVecBase4f,
    LVector3f,
    NodePath,
    PandaNode,
    ReferenceCount,
    TypeHandle,
    TypedReferenceCount,
    UnalignedLVecBase4f,
    ostream,
)

_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_LinearDistanceForce_FalloffType: TypeAlias = Literal[0, 1, 2]

class PhysicsObject(TypedReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    active: bool
    mass: float
    position: LPoint3f
    last_position: LPoint3f
    velocity: LVector3f
    terminal_velocity: float
    oriented: bool
    orientation: LOrientationf
    rotation: LRotationf
    @property
    def implicit_velocity(self) -> LVector3f: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: PhysicsObject) -> None: ...
    def assign(self, other: PhysicsObject) -> PhysicsObject: ...
    def set_active(self, flag: bool) -> None: ...
    def get_active(self) -> bool: ...
    def set_mass(self, __param0: float) -> None: ...
    def get_mass(self) -> float: ...
    @overload
    def set_position(self, pos: _Vec3f) -> None: ...
    @overload
    def set_position(self, x: float, y: float, z: float) -> None: ...
    def get_position(self) -> LPoint3f: ...
    def reset_position(self, pos: _Vec3f) -> None: ...
    def set_last_position(self, pos: _Vec3f) -> None: ...
    def get_last_position(self) -> LPoint3f: ...
    @overload
    def set_velocity(self, vel: _Vec3f) -> None: ...
    @overload
    def set_velocity(self, x: float, y: float, z: float) -> None: ...
    def get_velocity(self) -> LVector3f: ...
    def get_implicit_velocity(self) -> LVector3f: ...
    def add_torque(self, torque: _Vec4f) -> None: ...
    def add_impulse(self, impulse: _Vec3f) -> None: ...
    def add_impact(self, offset_from_center_of_mass: _Vec3f, impulse: _Vec3f) -> None: ...
    def add_local_torque(self, torque: _Vec4f) -> None: ...
    def add_local_impulse(self, impulse: _Vec3f) -> None: ...
    def add_local_impact(self, offset_from_center_of_mass: _Vec3f, impulse: _Vec3f) -> None: ...
    def set_terminal_velocity(self, tv: float) -> None: ...
    def get_terminal_velocity(self) -> float: ...
    def set_oriented(self, flag: bool) -> None: ...
    def get_oriented(self) -> bool: ...
    def set_orientation(self, orientation: LOrientationf) -> None: ...
    def get_orientation(self) -> LOrientationf: ...
    def reset_orientation(self, orientation: LOrientationf) -> None: ...
    def set_rotation(self, rotation: _Vec4f) -> None: ...
    def get_rotation(self) -> LRotationf: ...
    def get_inertial_tensor(self) -> LMatrix4f: ...
    def get_lcs(self) -> LMatrix4f: ...
    def make_copy(self) -> PhysicsObject: ...
    def set_name(self, name: str) -> None: ...
    def get_name(self) -> str: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent: int = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type

class PhysicsObjectCollection:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: PhysicsObjectCollection) -> None: ...
    def __getitem__(self, index: int) -> PhysicsObject: ...
    def __len__(self) -> int: ...
    def __iadd__(self, other: PhysicsObjectCollection) -> PhysicsObjectCollection: ...
    def __add__(self, other: PhysicsObjectCollection) -> PhysicsObjectCollection: ...
    def assign(self, copy: PhysicsObjectCollection) -> PhysicsObjectCollection: ...
    def add_physics_object(self, physics_object: PhysicsObject) -> None: ...
    def remove_physics_object(self, physics_object: PhysicsObject) -> bool: ...
    def add_physics_objects_from(self, other: PhysicsObjectCollection) -> None: ...
    def remove_physics_objects_from(self, other: PhysicsObjectCollection) -> None: ...
    def remove_duplicate_physics_objects(self) -> None: ...
    def has_physics_object(self, physics_object: PhysicsObject) -> bool: ...
    def clear(self) -> None: ...
    def is_empty(self) -> bool: ...
    def get_num_physics_objects(self) -> int: ...
    def get_physics_object(self, index: int) -> PhysicsObject: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
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
    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_active(self) -> bool: ...
    def set_active(self, active: bool) -> None: ...
    def is_linear(self) -> bool: ...
    def get_force_node(self) -> ForceNode: ...
    def get_force_node_path(self) -> NodePath: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getActive = get_active
    setActive = set_active
    isLinear = is_linear
    getForceNode = get_force_node
    getForceNodePath = get_force_node_path
    getClassType = get_class_type

class LinearForce(BaseForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def set_amplitude(self, a: float) -> None: ...
    def set_mass_dependent(self, m: bool) -> None: ...
    def get_amplitude(self) -> float: ...
    def get_mass_dependent(self) -> bool: ...
    def set_vector_masks(self, x: bool, y: bool, z: bool) -> None: ...
    def get_vector_masks(self) -> LVector3f: ...
    def get_vector(self, po: PhysicsObject) -> LVector3f: ...
    def make_copy(self) -> LinearForce: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setAmplitude = set_amplitude
    setMassDependent = set_mass_dependent
    getAmplitude = get_amplitude
    getMassDependent = get_mass_dependent
    setVectorMasks = set_vector_masks
    getVectorMasks = get_vector_masks
    getVector = get_vector
    makeCopy = make_copy
    getClassType = get_class_type

class AngularForce(BaseForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def make_copy(self) -> AngularForce: ...
    def get_quat(self, po: PhysicsObject) -> LRotationf: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    makeCopy = make_copy
    getQuat = get_quat
    getClassType = get_class_type

class Physical(TypedReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def linear_forces(self) -> Sequence[LinearForce]: ...
    @property
    def angular_forces(self) -> Sequence[AngularForce]: ...
    @property
    def viscosity(self) -> float: ...
    @property
    def objects(self) -> PhysicsObjectCollection: ...
    @overload
    def __init__(self, total_objects: int = ..., pre_alloc: bool = ...) -> None: ...
    @overload
    def __init__(self, copy: Physical) -> None: ...
    def get_physics_manager(self) -> PhysicsManager: ...
    def get_physical_node(self) -> PhysicalNode: ...
    def get_physical_node_path(self) -> NodePath: ...
    def get_phys_body(self) -> PhysicsObject: ...
    def clear_linear_forces(self) -> None: ...
    def clear_angular_forces(self) -> None: ...
    def clear_physics_objects(self) -> None: ...
    def add_linear_force(self, f: LinearForce) -> None: ...
    def add_angular_force(self, f: AngularForce) -> None: ...
    def add_physics_object(self, po: PhysicsObject) -> None: ...
    def remove_linear_force(self, f: LinearForce) -> None: ...
    def remove_angular_force(self, f: AngularForce) -> None: ...
    def get_num_linear_forces(self) -> int: ...
    def get_linear_force(self, index: int) -> LinearForce: ...
    def get_num_angular_forces(self) -> int: ...
    def get_angular_force(self, index: int) -> AngularForce: ...
    def set_viscosity(self, viscosity: float) -> None: ...
    def get_viscosity(self) -> float: ...
    def get_objects(self) -> PhysicsObjectCollection: ...
    def output(self, out: ostream = ...) -> None: ...
    def write_physics_objects(self, out: ostream = ..., indent: int = ...) -> None: ...
    def write_linear_forces(self, out: ostream = ..., indent: int = ...) -> None: ...
    def write_angular_forces(self, out: ostream = ..., indent: int = ...) -> None: ...
    def write(self, out: ostream = ..., indent: int = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type
    getLinearForces = get_linear_forces
    getAngularForces = get_angular_forces

class PhysicalNode(PandaNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    physicals: Sequence[Physical]
    def __init__(self, name: str) -> None: ...
    def clear(self) -> None: ...
    def get_physical(self, index: int) -> Physical: ...
    def get_num_physicals(self) -> int: ...
    def add_physical(self, physical: Physical) -> None: ...
    def add_physicals_from(self, other: PhysicalNode) -> None: ...
    def set_physical(self, index: int, physical: Physical) -> None: ...
    def insert_physical(self, index: int, physical: Physical) -> None: ...
    @overload
    def remove_physical(self, physical: Physical) -> None: ...
    @overload
    def remove_physical(self, index: int) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_physicals(self) -> tuple[Physical, ...]: ...
    getPhysical = get_physical
    getNumPhysicals = get_num_physicals
    addPhysical = add_physical
    addPhysicalsFrom = add_physicals_from
    setPhysical = set_physical
    insertPhysical = insert_physical
    removePhysical = remove_physical
    getClassType = get_class_type
    getPhysicals = get_physicals

class ActorNode(PhysicalNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: ActorNode) -> None: ...
    def get_physics_object(self) -> PhysicsObject: ...
    def set_contact_vector(self, contact_vector: _Vec3f) -> None: ...
    def get_contact_vector(self) -> LVector3f: ...
    def update_transform(self) -> None: ...
    def set_transform_limit(self, limit: float) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getPhysicsObject = get_physics_object
    setContactVector = set_contact_vector
    getContactVector = get_contact_vector
    updateTransform = update_transform
    setTransformLimit = set_transform_limit
    getClassType = get_class_type

class BaseIntegrator(ReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: BaseIntegrator) -> None: ...
    def output(self, out: ostream) -> None: ...
    def write_precomputed_linear_matrices(self, out: ostream, indent: int = ...) -> None: ...
    def write_precomputed_angular_matrices(self, out: ostream, indent: int = ...) -> None: ...
    def write(self, out: ostream, indent: int = ...) -> None: ...
    writePrecomputedLinearMatrices = write_precomputed_linear_matrices
    writePrecomputedAngularMatrices = write_precomputed_angular_matrices

class AngularIntegrator(BaseIntegrator):
    DtoolClassDict: ClassVar[dict[str, Any]]

class AngularEulerIntegrator(AngularIntegrator):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...

class AngularVectorForce(AngularForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: AngularVectorForce) -> None: ...
    @overload
    def __init__(self, quat: _Vec4f) -> None: ...
    @overload
    def __init__(self, h: float, p: float, r: float) -> None: ...
    def set_quat(self, quat: _Vec4f) -> None: ...
    def set_hpr(self, h: float, p: float, r: float) -> None: ...
    def get_local_quat(self) -> LRotationf: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setQuat = set_quat
    setHpr = set_hpr
    getLocalQuat = get_local_quat
    getClassType = get_class_type

class ForceNode(PandaNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    forces: Sequence[BaseForce]
    def __init__(self, name: str) -> None: ...
    def clear(self) -> None: ...
    def get_force(self, index: int) -> BaseForce: ...
    def get_num_forces(self) -> int: ...
    def add_force(self, force: BaseForce) -> None: ...
    def add_forces_from(self, other: ForceNode) -> None: ...
    def set_force(self, index: int, force: BaseForce) -> None: ...
    def insert_force(self, index: int, force: BaseForce) -> None: ...
    @overload
    def remove_force(self, force: BaseForce) -> None: ...
    @overload
    def remove_force(self, index: int) -> None: ...
    def write_forces(self, out: ostream, indent: int = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_forces(self) -> tuple[BaseForce, ...]: ...
    getForce = get_force
    getNumForces = get_num_forces
    addForce = add_force
    addForcesFrom = add_forces_from
    setForce = set_force
    insertForce = insert_force
    removeForce = remove_force
    writeForces = write_forces
    getClassType = get_class_type
    getForces = get_forces

class LinearControlForce(LinearForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, po: PhysicsObject = ..., a: float = ..., mass: bool = ...) -> None: ...
    @overload
    def __init__(self, copy: LinearControlForce) -> None: ...
    def clear_physics_object(self) -> None: ...
    def set_physics_object(self, po: PhysicsObject) -> None: ...
    def get_physics_object(self) -> PhysicsObject: ...
    @overload
    def set_vector(self, v: _Vec3f) -> None: ...
    @overload
    def set_vector(self, x: float, y: float, z: float) -> None: ...
    def get_local_vector(self) -> LVector3f: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    clearPhysicsObject = clear_physics_object
    setPhysicsObject = set_physics_object
    getPhysicsObject = get_physics_object
    setVector = set_vector
    getLocalVector = get_local_vector
    getClassType = get_class_type

class LinearCylinderVortexForce(LinearForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, radius: float = ..., length: float = ..., coef: float = ..., a: float = ..., md: bool = ...) -> None: ...
    @overload
    def __init__(self, copy: LinearCylinderVortexForce) -> None: ...
    def set_coef(self, coef: float) -> None: ...
    def get_coef(self) -> float: ...
    def set_radius(self, radius: float) -> None: ...
    def get_radius(self) -> float: ...
    def set_length(self, length: float) -> None: ...
    def get_length(self) -> float: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setCoef = set_coef
    getCoef = get_coef
    setRadius = set_radius
    getRadius = get_radius
    setLength = set_length
    getLength = get_length
    getClassType = get_class_type

class LinearDistanceForce(LinearForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    FT_ONE_OVER_R: ClassVar[Literal[0]]
    FT_ONE_OVER_R_SQUARED: ClassVar[Literal[1]]
    FT_ONE_OVER_R_CUBED: ClassVar[Literal[2]]
    def set_radius(self, r: float) -> None: ...
    def set_falloff_type(self, ft: _LinearDistanceForce_FalloffType) -> None: ...
    def set_force_center(self, p: _Vec3f) -> None: ...
    def get_radius(self) -> float: ...
    def get_falloff_type(self) -> _LinearDistanceForce_FalloffType: ...
    def get_force_center(self) -> LPoint3f: ...
    def get_scalar_term(self) -> float: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setRadius = set_radius
    setFalloffType = set_falloff_type
    setForceCenter = set_force_center
    getRadius = get_radius
    getFalloffType = get_falloff_type
    getForceCenter = get_force_center
    getScalarTerm = get_scalar_term
    getClassType = get_class_type
    FTONEOVERR = FT_ONE_OVER_R
    FTONEOVERRSQUARED = FT_ONE_OVER_R_SQUARED
    FTONEOVERRCUBED = FT_ONE_OVER_R_CUBED

class LinearIntegrator(BaseIntegrator):
    DtoolClassDict: ClassVar[dict[str, Any]]

class LinearEulerIntegrator(LinearIntegrator):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...

class LinearFrictionForce(LinearForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, coef: float = ..., a: float = ..., m: bool = ...) -> None: ...
    @overload
    def __init__(self, copy: LinearFrictionForce) -> None: ...
    def set_coef(self, coef: float) -> None: ...
    def get_coef(self) -> float: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setCoef = set_coef
    getCoef = get_coef
    getClassType = get_class_type

class LinearRandomForce(LinearForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class LinearJitterForce(LinearRandomForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, a: float = ..., m: bool = ...) -> None: ...
    @overload
    def __init__(self, copy: LinearJitterForce) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class LinearNoiseForce(LinearRandomForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, a: float = ..., m: bool = ...) -> None: ...
    @overload
    def __init__(self, copy: LinearNoiseForce) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class LinearSinkForce(LinearDistanceForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: LinearSinkForce) -> None: ...
    @overload
    def __init__(self, p: _Vec3f, f: _LinearDistanceForce_FalloffType, r: float, a: float = ..., m: bool = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class LinearSourceForce(LinearDistanceForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: LinearSourceForce) -> None: ...
    @overload
    def __init__(self, p: _Vec3f, f: _LinearDistanceForce_FalloffType, r: float, a: float = ..., mass: bool = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class LinearUserDefinedForce(LinearForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: LinearUserDefinedForce) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class LinearVectorForce(LinearForce):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, x: float = ..., y: float = ..., z: float = ..., a: float = ..., mass: bool = ...) -> None: ...
    @overload
    def __init__(self, copy: LinearVectorForce) -> None: ...
    @overload
    def __init__(self, vec: _Vec3f, a: float = ..., mass: bool = ...) -> None: ...
    @overload
    def set_vector(self, v: _Vec3f) -> None: ...
    @overload
    def set_vector(self, x: float, y: float, z: float) -> None: ...
    def get_local_vector(self) -> LVector3f: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setVector = set_vector
    getLocalVector = get_local_vector
    getClassType = get_class_type

class PhysicsCollisionHandler(CollisionHandlerPusher):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    def set_almost_stationary_speed(self, speed: float) -> None: ...
    def get_almost_stationary_speed(self) -> float: ...
    def set_static_friction_coef(self, coef: float) -> None: ...
    def get_static_friction_coef(self) -> float: ...
    def set_dynamic_friction_coef(self, coef: float) -> None: ...
    def get_dynamic_friction_coef(self) -> float: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setAlmostStationarySpeed = set_almost_stationary_speed
    getAlmostStationarySpeed = get_almost_stationary_speed
    setStaticFrictionCoef = set_static_friction_coef
    getStaticFrictionCoef = get_static_friction_coef
    setDynamicFrictionCoef = set_dynamic_friction_coef
    getDynamicFrictionCoef = get_dynamic_friction_coef
    getClassType = get_class_type

class PhysicsManager:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: PhysicsManager) -> None: ...
    def attach_linear_integrator(self, i: LinearIntegrator) -> None: ...
    def attach_angular_integrator(self, i: AngularIntegrator) -> None: ...
    def attach_physical(self, p: Physical) -> None: ...
    def attach_physicalnode(self, p: PhysicalNode) -> None: ...
    def attach_physical_node(self, p: PhysicalNode) -> None: ...
    def add_linear_force(self, f: LinearForce) -> None: ...
    def add_angular_force(self, f: AngularForce) -> None: ...
    def clear_linear_forces(self) -> None: ...
    def clear_angular_forces(self) -> None: ...
    def clear_physicals(self) -> None: ...
    def set_viscosity(self, viscosity: float) -> None: ...
    def get_viscosity(self) -> float: ...
    def remove_physical(self, p: Physical) -> None: ...
    def remove_physical_node(self, p: PhysicalNode) -> None: ...
    def remove_linear_force(self, f: LinearForce) -> None: ...
    def remove_angular_force(self, f: AngularForce) -> None: ...
    @overload
    def do_physics(self, dt: float) -> None: ...
    @overload
    def do_physics(self, dt: float, p: Physical) -> None: ...
    def init_random_seed(self) -> None: ...
    def output(self, out: ostream) -> None: ...
    def write_physicals(self, out: ostream, indent: int = ...) -> None: ...
    def write_linear_forces(self, out: ostream, indent: int = ...) -> None: ...
    def write_angular_forces(self, out: ostream, indent: int = ...) -> None: ...
    def write(self, out: ostream, indent: int = ...) -> None: ...
    def debug_output(self, out: ostream, indent: int = ...) -> None: ...
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
