from collections.abc import Callable, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import Mat4Like, Vec3Like, Vec4Like
from panda3d.core._collide import CollisionBox, CollisionCapsule, CollisionNode, CollisionPlane, CollisionSphere
from panda3d.core._dtoolbase import TypedObject
from panda3d.core._dtoolutil import ostream
from panda3d.core._express import PTA_int, PTA_stdfloat, TypedReferenceCount
from panda3d.core._gobj import Geom, GeomVertexArrayFormat, GeomVertexFormat, InternalName, Texture
from panda3d.core._linmath import LMatrix3, LMatrix4, LPoint3, LVecBase3, LVecBase3i, LVector3
from panda3d.core._mathutil import BoundingBox, BoundingSphere, LPlane, LPlanef, PTA_LVecBase3
from panda3d.core._parametrics import NurbsCurveEvaluator, NurbsSurfaceEvaluator
from panda3d.core._pgraph import NodePath, NodePathCollection, PandaNode, TransformState
from panda3d.core._pnmimage import PNMImage
from panda3d.core._putil import CallbackData, CallbackObject, CollideMask, TypedWritableReferenceCount

_BulletUpAxis: TypeAlias = Literal[0, 1, 2]
_BulletConstraint_ConstraintParam: TypeAlias = Literal[1, 2, 3, 4]
_BulletSoftBodyConfig_AeroModel: TypeAlias = Literal[0, 1, 2, 3, 4]
_BulletSoftBodyConfig_CollisionFlag: TypeAlias = Literal[1, 2, 15, 16, 32, 48, 64]

class BulletRayHit:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def node(self) -> PandaNode: ...
    @property
    def hit_pos(self) -> LPoint3: ...
    @property
    def hit_normal(self) -> LVector3: ...
    @property
    def hit_fraction(self) -> float: ...
    @property
    def shape_part(self) -> int: ...
    @property
    def triangle_index(self) -> int: ...
    def __init__(self, __param0: BulletRayHit = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def empty() -> BulletRayHit:
        """Named constructor intended to be used for asserts with have to return a
        concrete value.
        """
    def get_node(self) -> PandaNode: ...
    def get_hit_pos(self) -> LPoint3: ...
    def get_hit_normal(self) -> LVector3: ...
    def get_hit_fraction(self) -> float: ...
    def get_shape_part(self) -> int: ...
    def get_triangle_index(self) -> int: ...
    getNode = get_node
    getHitPos = get_hit_pos
    getHitNormal = get_hit_normal
    getHitFraction = get_hit_fraction
    getShapePart = get_shape_part
    getTriangleIndex = get_triangle_index

class BulletAllHitsRayResult:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def from_pos(self) -> LPoint3: ...
    @property
    def to_pos(self) -> LPoint3: ...
    @property
    def closest_hit_fraction(self) -> float: ...
    @property
    def hits(self) -> Sequence[BulletRayHit]: ...
    @staticmethod
    def empty() -> BulletAllHitsRayResult:
        """Named constructor intended to be used for asserts with have to return a
        concrete value.
        """
    def get_from_pos(self) -> LPoint3: ...
    def get_to_pos(self) -> LPoint3: ...
    def has_hits(self) -> bool: ...
    def get_closest_hit_fraction(self) -> float: ...
    def get_num_hits(self) -> int: ...
    def get_hit(self, idx: int) -> BulletRayHit: ...
    def get_hits(self) -> tuple[BulletRayHit, ...]: ...
    getFromPos = get_from_pos
    getToPos = get_to_pos
    hasHits = has_hits
    getClosestHitFraction = get_closest_hit_fraction
    getNumHits = get_num_hits
    getHit = get_hit
    getHits = get_hits

class BulletShape(TypedWritableReferenceCount):
    margin: float
    @property
    def polyhedral(self) -> bool: ...
    @property
    def convex(self) -> bool: ...
    @property
    def convex_2d(self) -> bool: ...
    @property
    def concave(self) -> bool: ...
    @property
    def infinite(self) -> bool: ...
    @property
    def non_moving(self) -> bool: ...
    @property
    def soft_body(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def shape_bounds(self) -> BoundingSphere: ...
    def is_polyhedral(self) -> bool: ...
    def is_convex(self) -> bool: ...
    def is_convex_2d(self) -> bool: ...
    def is_concave(self) -> bool: ...
    def is_infinite(self) -> bool: ...
    def is_non_moving(self) -> bool: ...
    def is_soft_body(self) -> bool: ...
    def set_margin(self, margin: float) -> None: ...
    def get_name(self) -> str: ...
    def get_margin(self) -> float: ...
    def get_shape_bounds(self) -> BoundingSphere:
        """Returns the current bounds of this collision shape."""
    isPolyhedral = is_polyhedral
    isConvex = is_convex
    isConvex2d = is_convex_2d
    isConcave = is_concave
    isInfinite = is_infinite
    isNonMoving = is_non_moving
    isSoftBody = is_soft_body
    setMargin = set_margin
    getName = get_name
    getMargin = get_margin
    getShapeBounds = get_shape_bounds

class BulletBaseCharacterControllerNode(PandaNode): ...

class BulletBodyNode(PandaNode):
    static: bool
    """Static and kinematic"""
    kinematic: bool
    collision_notification: bool
    collision_response: bool
    contact_processing_threshold: float
    active: bool
    """Deactivation"""
    deactivation_time: float
    deactivation_enabled: bool
    debug_enabled: bool
    restitution: float
    """Friction and Restitution"""
    friction: float
    anisotropic_friction: LVecBase3
    ccd_swept_sphere_radius: float
    """CCD"""
    ccd_motion_threshold: float
    @property
    def shapes(self) -> Sequence[BulletShape]: ...
    @property
    def shape_pos(self) -> Sequence[LPoint3]: ...
    @property
    def shape_mat(self) -> Sequence[LMatrix4]: ...
    @property
    def shape_transform(self) -> Sequence[TransformState]: ...
    @property
    def shape_bounds(self) -> BoundingSphere: ...
    @property
    def contact_response(self) -> bool: ...
    def add_shape(self, shape: BulletShape, xform: TransformState = ...) -> None:
        """Shapes"""
    def remove_shape(self, shape: BulletShape) -> None: ...
    def get_num_shapes(self) -> int: ...
    def get_shape(self, idx: int) -> BulletShape: ...
    def get_shape_pos(self, idx: int) -> LPoint3: ...
    def get_shape_mat(self, idx: int) -> LMatrix4: ...
    def get_shape_transform(self, idx: int) -> TransformState: ...
    def get_shape_bounds(self) -> BoundingSphere:
        """Returns the current bounds of all collision shapes owned by this body."""
    def add_shapes_from_collision_solids(self, cnode: CollisionNode) -> None: ...
    def is_static(self) -> bool:
        """Static and kinematic"""
    def is_kinematic(self) -> bool: ...
    def set_static(self, value: bool) -> None: ...
    def set_kinematic(self, value: bool) -> None: ...
    def set_into_collide_mask(self, mask: CollideMask | int) -> None:
        """Contacts"""
    def notify_collisions(self, value: bool) -> None: ...
    def notifies_collisions(self) -> bool: ...
    def set_collision_response(self, value: bool) -> None: ...
    def get_collision_response(self) -> bool: ...
    def check_collision_with(self, node: PandaNode) -> bool: ...
    def has_contact_response(self) -> bool: ...
    def get_contact_processing_threshold(self) -> float: ...
    def set_contact_processing_threshold(self, threshold: float) -> None:
        """The constraint solver can discard solving contacts, if the distance is
        above this threshold.
        """
    def is_active(self) -> bool:
        """Deactivation"""
    def set_active(self, active: bool, force: bool = ...) -> None: ...
    def force_active(self, active: bool) -> None: ...
    def set_deactivation_time(self, dt: float) -> None: ...
    def get_deactivation_time(self) -> float: ...
    def set_deactivation_enabled(self, enabled: bool) -> None:
        """If true, this object will be deactivated after a certain amount of time has
        passed without movement.  If false, the object will always remain active.
        """
    def is_deactivation_enabled(self) -> bool: ...
    def set_debug_enabled(self, enabled: bool) -> None:
        """Enables or disables the debug visualisation for this collision object.  By
        default the debug visualisation is enabled.
        """
    def is_debug_enabled(self) -> bool:
        """Returns TRUE if the debug visualisation is enabled for this collision
        object, and FALSE if the debug visualisation is disabled.
        """
    def get_restitution(self) -> float:
        """Friction and Restitution"""
    def set_restitution(self, restitution: float) -> None: ...
    def get_friction(self) -> float: ...
    def set_friction(self, friction: float) -> None: ...
    def has_anisotropic_friction(self) -> bool: ...
    def set_anisotropic_friction(self, friction: Vec3Like) -> None: ...
    def get_anisotropic_friction(self) -> LVecBase3: ...
    def get_ccd_swept_sphere_radius(self) -> float: ...
    def get_ccd_motion_threshold(self) -> float: ...
    def set_ccd_swept_sphere_radius(self, radius: float) -> None: ...
    def set_ccd_motion_threshold(self, threshold: float) -> None: ...
    def set_transform_dirty(self) -> None:
        """This method enforces an update of the Bullet transform, that is copies the
        scene graph transform to the Bullet transform.  This is achieved by alling
        the protected PandaNode hook 'transform_changed'.
        """
    def get_shapes(self) -> tuple[BulletShape, ...]: ...
    addShape = add_shape
    removeShape = remove_shape
    getNumShapes = get_num_shapes
    getShape = get_shape
    getShapePos = get_shape_pos
    getShapeMat = get_shape_mat
    getShapeTransform = get_shape_transform
    getShapeBounds = get_shape_bounds
    addShapesFromCollisionSolids = add_shapes_from_collision_solids
    isStatic = is_static
    isKinematic = is_kinematic
    setStatic = set_static
    setKinematic = set_kinematic
    setIntoCollideMask = set_into_collide_mask
    notifyCollisions = notify_collisions
    notifiesCollisions = notifies_collisions
    setCollisionResponse = set_collision_response
    getCollisionResponse = get_collision_response
    checkCollisionWith = check_collision_with
    hasContactResponse = has_contact_response
    getContactProcessingThreshold = get_contact_processing_threshold
    setContactProcessingThreshold = set_contact_processing_threshold
    isActive = is_active
    setActive = set_active
    forceActive = force_active
    setDeactivationTime = set_deactivation_time
    getDeactivationTime = get_deactivation_time
    setDeactivationEnabled = set_deactivation_enabled
    isDeactivationEnabled = is_deactivation_enabled
    setDebugEnabled = set_debug_enabled
    isDebugEnabled = is_debug_enabled
    getRestitution = get_restitution
    setRestitution = set_restitution
    getFriction = get_friction
    setFriction = set_friction
    hasAnisotropicFriction = has_anisotropic_friction
    setAnisotropicFriction = set_anisotropic_friction
    getAnisotropicFriction = get_anisotropic_friction
    getCcdSweptSphereRadius = get_ccd_swept_sphere_radius
    getCcdMotionThreshold = get_ccd_motion_threshold
    setCcdSweptSphereRadius = set_ccd_swept_sphere_radius
    setCcdMotionThreshold = set_ccd_motion_threshold
    setTransformDirty = set_transform_dirty
    getShapes = get_shapes

class BulletBoxShape(BulletShape):
    @property
    def half_extents_with_margin(self) -> LVecBase3: ...
    @property
    def half_extents_without_margin(self) -> LVecBase3: ...
    @overload
    def __init__(self, copy: BulletBoxShape) -> None: ...
    @overload
    def __init__(self, halfExtents: Vec3Like) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_half_extents_without_margin(self) -> LVecBase3: ...
    def get_half_extents_with_margin(self) -> LVecBase3: ...
    @staticmethod
    def make_from_solid(solid: CollisionBox) -> BulletBoxShape: ...
    getHalfExtentsWithoutMargin = get_half_extents_without_margin
    getHalfExtentsWithMargin = get_half_extents_with_margin
    makeFromSolid = make_from_solid

class BulletCapsuleShape(BulletShape):
    @property
    def radius(self) -> float: ...
    @property
    def height(self) -> float: ...
    @overload
    def __init__(self, copy: BulletCapsuleShape) -> None: ...
    @overload
    def __init__(self, radius: float, height: float, up: _BulletUpAxis = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def make_from_solid(solid: CollisionCapsule) -> BulletCapsuleShape:
        """Constructs a new BulletCapsuleShape using the information from a
        CollisionCapsule from the builtin collision system.
        """
    def get_radius(self) -> float:
        """Returns the radius that was used to construct this capsule."""
    def get_half_height(self) -> float:
        """Returns half of get_height().
        @deprecated see get_height() instead.
        """
    makeFromSolid = make_from_solid
    getRadius = get_radius
    getHalfHeight = get_half_height

class BulletCharacterControllerNode(BulletBaseCharacterControllerNode):
    gravity: float
    max_slope: float
    @property
    def shape(self) -> BulletShape: ...
    @property
    def on_ground(self) -> bool: ...
    def __init__(self, shape: BulletShape, step_height: float, name: str = ...) -> None: ...
    def set_linear_movement(self, velocity: Vec3Like, is_local: bool) -> None: ...
    def set_angular_movement(self, omega: float) -> None: ...
    def get_shape(self) -> BulletShape: ...
    def set_gravity(self, gravity: float) -> None: ...
    def get_gravity(self) -> float: ...
    def set_fall_speed(self, fall_speed: float) -> None: ...
    def set_jump_speed(self, jump_speed: float) -> None: ...
    def set_max_jump_height(self, max_jump_height: float) -> None: ...
    def set_max_slope(self, max_slope: float) -> None: ...
    def get_max_slope(self) -> float: ...
    def set_use_ghost_sweep_test(self, value: bool) -> None: ...
    def is_on_ground(self) -> bool: ...
    def can_jump(self) -> bool: ...
    def do_jump(self) -> None: ...
    setLinearMovement = set_linear_movement
    setAngularMovement = set_angular_movement
    getShape = get_shape
    setGravity = set_gravity
    getGravity = get_gravity
    setFallSpeed = set_fall_speed
    setJumpSpeed = set_jump_speed
    setMaxJumpHeight = set_max_jump_height
    setMaxSlope = set_max_slope
    getMaxSlope = get_max_slope
    setUseGhostSweepTest = set_use_ghost_sweep_test
    isOnGround = is_on_ground
    canJump = can_jump
    doJump = do_jump

class BulletClosestHitRayResult:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def from_pos(self) -> LPoint3: ...
    @property
    def to_pos(self) -> LPoint3: ...
    @property
    def node(self) -> PandaNode: ...
    @property
    def hit_pos(self) -> LPoint3: ...
    @property
    def hit_normal(self) -> LVector3: ...
    @property
    def hit_fraction(self) -> float: ...
    @property
    def shape_part(self) -> int: ...
    @property
    def triangle_index(self) -> int: ...
    def __init__(self, __param0: BulletClosestHitRayResult) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def empty() -> BulletClosestHitRayResult:
        """Named constructor intended to be used for asserts with have to return a
        concrete value.
        """
    def get_from_pos(self) -> LPoint3: ...
    def get_to_pos(self) -> LPoint3: ...
    def has_hit(self) -> bool: ...
    def get_node(self) -> PandaNode: ...
    def get_hit_pos(self) -> LPoint3: ...
    def get_hit_normal(self) -> LVector3: ...
    def get_hit_fraction(self) -> float: ...
    def get_shape_part(self) -> int: ...
    def get_triangle_index(self) -> int: ...
    getFromPos = get_from_pos
    getToPos = get_to_pos
    hasHit = has_hit
    getNode = get_node
    getHitPos = get_hit_pos
    getHitNormal = get_hit_normal
    getHitFraction = get_hit_fraction
    getShapePart = get_shape_part
    getTriangleIndex = get_triangle_index

class BulletClosestHitSweepResult:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def from_pos(self) -> LPoint3: ...
    @property
    def to_pos(self) -> LPoint3: ...
    @property
    def node(self) -> PandaNode: ...
    @property
    def hit_pos(self) -> LPoint3: ...
    @property
    def hit_normal(self) -> LVector3: ...
    @property
    def hit_fraction(self) -> float: ...
    def __init__(self, __param0: BulletClosestHitSweepResult) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def empty() -> BulletClosestHitSweepResult:
        """Named constructor intended to be used for asserts with have to return a
        concrete value.
        """
    def get_from_pos(self) -> LPoint3: ...
    def get_to_pos(self) -> LPoint3: ...
    def has_hit(self) -> bool: ...
    def get_node(self) -> PandaNode: ...
    def get_hit_pos(self) -> LPoint3: ...
    def get_hit_normal(self) -> LVector3: ...
    def get_hit_fraction(self) -> float: ...
    getFromPos = get_from_pos
    getToPos = get_to_pos
    hasHit = has_hit
    getNode = get_node
    getHitPos = get_hit_pos
    getHitNormal = get_hit_normal
    getHitFraction = get_hit_fraction

class BulletConeShape(BulletShape):
    @property
    def radius(self) -> float: ...
    @property
    def height(self) -> float: ...
    @overload
    def __init__(self, copy: BulletConeShape) -> None: ...
    @overload
    def __init__(self, radius: float, height: float, up: _BulletUpAxis = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_radius(self) -> float:
        """Returns the radius that was passed into the constructor."""
    def get_height(self) -> float:
        """Returns the height that was passed into the constructor."""
    getRadius = get_radius
    getHeight = get_height

class BulletConstraint(TypedReferenceCount):
    CP_erp: Final = 1
    CPErp: Final = 1
    CP_stop_erp: Final = 2
    CPStopErp: Final = 2
    CP_cfm: Final = 3
    CPCfm: Final = 3
    CP_stop_cfm: Final = 4
    CPStopCfm: Final = 4
    debug_draw_size: float
    breaking_threshold: float
    enabled: bool
    @property
    def rigid_body_a(self) -> BulletRigidBodyNode: ...
    @property
    def rigid_body_b(self) -> BulletRigidBodyNode: ...
    @property
    def applied_impulse(self) -> float: ...
    def get_rigid_body_a(self) -> BulletRigidBodyNode: ...
    def get_rigid_body_b(self) -> BulletRigidBodyNode: ...
    def enable_feedback(self, value: bool) -> None: ...
    def set_debug_draw_size(self, size: float) -> None: ...
    def get_debug_draw_size(self) -> float: ...
    def get_applied_impulse(self) -> float: ...
    def set_breaking_threshold(self, threshold: float) -> None:
        """Sets the applied impulse limit for breaking the constraint.  If the limit
        is exceeded the constraint will be disabled.  Disabled constraints are not
        removed from the world, and can be re-enabled.
        """
    def get_breaking_threshold(self) -> float:
        """Returns the applied impluse limit for breaking the constraint."""
    def set_enabled(self, enabled: bool) -> None: ...
    def is_enabled(self) -> bool:
        """Returns TRUE if the constraint is enabled."""
    def set_param(self, num: _BulletConstraint_ConstraintParam, value: float, axis: int = ...) -> None: ...
    def get_param(self, num: _BulletConstraint_ConstraintParam, axis: int = ...) -> float: ...
    getRigidBodyA = get_rigid_body_a
    getRigidBodyB = get_rigid_body_b
    enableFeedback = enable_feedback
    setDebugDrawSize = set_debug_draw_size
    getDebugDrawSize = get_debug_draw_size
    getAppliedImpulse = get_applied_impulse
    setBreakingThreshold = set_breaking_threshold
    getBreakingThreshold = get_breaking_threshold
    setEnabled = set_enabled
    isEnabled = is_enabled
    setParam = set_param
    getParam = get_param

class BulletRigidBodyNode(BulletBodyNode):
    mass: float
    inertia: LVector3
    linear_velocity: LVector3
    """Velocity"""
    angular_velocity: LVector3
    linear_damping: float
    """Damping"""
    angular_damping: float
    linear_sleep_threshold: float
    """Deactivation thresholds"""
    angular_sleep_threshold: float
    gravity: LVector3
    linear_factor: LVector3
    """Restrict movement"""
    angular_factor: LVector3
    @property
    def inv_mass(self) -> float: ...
    @property
    def inv_inertia_diag_local(self) -> LVector3: ...
    @property
    def inv_inertia_tensor_world(self) -> LMatrix3: ...
    @property
    def total_force(self) -> LVector3: ...
    @property
    def total_torque(self) -> LVector3: ...
    def __init__(self, name: str = ...) -> None: ...
    def set_mass(self, mass: float) -> None:
        """Sets the mass of a rigid body.  This also modifies the inertia, which is
        automatically computed from the shape of the body.  Setting a value of zero
        for mass will make the body static.  A value of zero can be considered an
        infinite mass.
        """
    def get_mass(self) -> float:
        """Returns the total mass of a rigid body.  A value of zero means that the
        body is staic, i.e.  has an infinite mass.
        """
    def get_inv_mass(self) -> float:
        """Returns the inverse mass of a rigid body."""
    def set_inertia(self, inertia: Vec3Like) -> None:
        """Sets the inertia of a rigid body.  Inertia is given as a three-component
        vector.  A component value of zero means infinite inertia along this
        direction.  Setting the intertia will override the value which is
        automatically calculated from the rigid bodies shape.  However, it is
        possible that automatic calculation of intertia is trigger after calling
        this method, and thus overwriting the explicitly set value again.  This
        happens when: (a) the mass is set after the inertia.  (b) a shape is added
        or removed from the body.  (c) the scale of the body changed.
        """
    def get_inertia(self) -> LVector3:
        """Returns the inertia of the rigid body.  Inertia is given as a three
        component vector.  A component value of zero means infinite inertia along
        this direction.
        """
    def get_inv_inertia_diag_local(self) -> LVector3: ...
    def get_inv_inertia_tensor_world(self) -> LMatrix3: ...
    def get_linear_velocity(self) -> LVector3:
        """Velocity"""
    def get_angular_velocity(self) -> LVector3: ...
    def set_linear_velocity(self, velocity: Vec3Like) -> None: ...
    def set_angular_velocity(self, velocity: Vec3Like) -> None: ...
    def get_linear_damping(self) -> float:
        """Damping"""
    def get_angular_damping(self) -> float: ...
    def set_linear_damping(self, value: float) -> None: ...
    def set_angular_damping(self, value: float) -> None: ...
    def clear_forces(self) -> None:
        """Forces"""
    def apply_force(self, force: Vec3Like, pos: Vec3Like) -> None: ...
    def apply_central_force(self, force: Vec3Like) -> None: ...
    def apply_impulse(self, impulse: Vec3Like, pos: Vec3Like) -> None: ...
    def apply_central_impulse(self, impulse: Vec3Like) -> None: ...
    def apply_torque(self, torque: Vec3Like) -> None: ...
    def apply_torque_impulse(self, torque: Vec3Like) -> None: ...
    def get_total_force(self) -> LVector3: ...
    def get_total_torque(self) -> LVector3: ...
    def get_linear_sleep_threshold(self) -> float:
        """Deactivation thresholds"""
    def get_angular_sleep_threshold(self) -> float: ...
    def set_linear_sleep_threshold(self, threshold: float) -> None: ...
    def set_angular_sleep_threshold(self, threshold: float) -> None: ...
    def set_gravity(self, gravity: Vec3Like) -> None:
        """Gravity"""
    def get_gravity(self) -> LVector3: ...
    def get_linear_factor(self) -> LVector3:
        """Restrict movement"""
    def get_angular_factor(self) -> LVector3: ...
    def set_linear_factor(self, factor: Vec3Like) -> None: ...
    def set_angular_factor(self, factor: Vec3Like) -> None: ...
    def pick_dirty_flag(self) -> bool:
        """Returns TRUE if the transform of the rigid body has changed at least once
        since the last call to this method.
        """
    setMass = set_mass
    getMass = get_mass
    getInvMass = get_inv_mass
    setInertia = set_inertia
    getInertia = get_inertia
    getInvInertiaDiagLocal = get_inv_inertia_diag_local
    getInvInertiaTensorWorld = get_inv_inertia_tensor_world
    getLinearVelocity = get_linear_velocity
    getAngularVelocity = get_angular_velocity
    setLinearVelocity = set_linear_velocity
    setAngularVelocity = set_angular_velocity
    getLinearDamping = get_linear_damping
    getAngularDamping = get_angular_damping
    setLinearDamping = set_linear_damping
    setAngularDamping = set_angular_damping
    clearForces = clear_forces
    applyForce = apply_force
    applyCentralForce = apply_central_force
    applyImpulse = apply_impulse
    applyCentralImpulse = apply_central_impulse
    applyTorque = apply_torque
    applyTorqueImpulse = apply_torque_impulse
    getTotalForce = get_total_force
    getTotalTorque = get_total_torque
    getLinearSleepThreshold = get_linear_sleep_threshold
    getAngularSleepThreshold = get_angular_sleep_threshold
    setLinearSleepThreshold = set_linear_sleep_threshold
    setAngularSleepThreshold = set_angular_sleep_threshold
    setGravity = set_gravity
    getGravity = get_gravity
    getLinearFactor = get_linear_factor
    getAngularFactor = get_angular_factor
    setLinearFactor = set_linear_factor
    setAngularFactor = set_angular_factor
    pickDirtyFlag = pick_dirty_flag

class BulletConeTwistConstraint(BulletConstraint):
    fix_threshold: float
    @property
    def frame_a(self) -> TransformState: ...
    @property
    def frame_b(self) -> TransformState: ...
    @overload
    def __init__(self, node_a: BulletRigidBodyNode, frame_a: TransformState) -> None: ...
    @overload
    def __init__(
        self, node_a: BulletRigidBodyNode, node_b: BulletRigidBodyNode, frame_a: TransformState, frame_b: TransformState
    ) -> None: ...
    @overload
    def set_limit(self, index: int, value: float) -> None: ...
    @overload
    def set_limit(
        self, swing1: float, swing2: float, twist: float, softness: float = ..., bias: float = ..., relaxation: float = ...
    ) -> None: ...
    def set_damping(self, damping: float) -> None: ...
    def get_fix_threshold(self) -> float: ...
    def set_fix_threshold(self, threshold: float) -> None: ...
    def enable_motor(self, enable: bool) -> None: ...
    def set_max_motor_impulse(self, max_impulse: float) -> None: ...
    def set_max_motor_impulse_normalized(self, max_impulse: float) -> None: ...
    def set_motor_target(self, quat: Vec4Like) -> None: ...
    def set_motor_target_in_constraint_space(self, quat: Vec4Like) -> None: ...
    def set_frames(self, ts_a: TransformState, ts_b: TransformState) -> None: ...
    def get_frame_a(self) -> TransformState: ...
    def get_frame_b(self) -> TransformState: ...
    setLimit = set_limit
    setDamping = set_damping
    getFixThreshold = get_fix_threshold
    setFixThreshold = set_fix_threshold
    enableMotor = enable_motor
    setMaxMotorImpulse = set_max_motor_impulse
    setMaxMotorImpulseNormalized = set_max_motor_impulse_normalized
    setMotorTarget = set_motor_target
    setMotorTargetInConstraintSpace = set_motor_target_in_constraint_space
    setFrames = set_frames
    getFrameA = get_frame_a
    getFrameB = get_frame_b

class BulletManifoldPoint:
    DtoolClassDict: ClassVar[dict[str, Any]]
    applied_impulse: float
    lateral_friction_initialized: bool
    lateral_friction_dir1: LVector3
    lateral_friction_dir2: LVector3
    contact_motion1: float
    contact_motion2: float
    combined_friction: float
    combined_restitution: float
    applied_impulse_lateral1: float
    applied_impulse_lateral2: float
    contact_cfm1: float
    contact_cfm2: float
    @property
    def life_time(self) -> int: ...
    @property
    def distance(self) -> float: ...
    @property
    def position_world_on_a(self) -> LPoint3: ...
    @property
    def position_world_on_b(self) -> LPoint3: ...
    @property
    def normal_world_on_b(self) -> LVector3: ...
    @property
    def local_point_a(self) -> LPoint3: ...
    @property
    def local_point_b(self) -> LPoint3: ...
    @property
    def part_id0(self) -> int: ...
    @property
    def part_id1(self) -> int: ...
    @property
    def index0(self) -> int: ...
    @property
    def index1(self) -> int: ...
    def get_life_time(self) -> int: ...
    def get_distance(self) -> float: ...
    def get_applied_impulse(self) -> float: ...
    def get_position_world_on_a(self) -> LPoint3: ...
    def get_position_world_on_b(self) -> LPoint3: ...
    def get_normal_world_on_b(self) -> LVector3: ...
    def get_local_point_a(self) -> LPoint3: ...
    def get_local_point_b(self) -> LPoint3: ...
    def get_part_id0(self) -> int: ...
    def get_part_id1(self) -> int: ...
    def get_index0(self) -> int: ...
    def get_index1(self) -> int: ...
    def set_lateral_friction_initialized(self, value: bool) -> None: ...
    def set_lateral_friction_dir1(self, dir: Vec3Like) -> None: ...
    def set_lateral_friction_dir2(self, dir: Vec3Like) -> None: ...
    def set_contact_motion1(self, value: float) -> None: ...
    def set_contact_motion2(self, value: float) -> None: ...
    def set_combined_friction(self, value: float) -> None: ...
    def set_combined_restitution(self, value: float) -> None: ...
    def set_applied_impulse(self, value: float) -> None: ...
    def set_applied_impulse_lateral1(self, value: float) -> None: ...
    def set_applied_impulse_lateral2(self, value: float) -> None: ...
    def set_contact_cfm1(self, value: float) -> None: ...
    def set_contact_cfm2(self, value: float) -> None: ...
    def get_lateral_friction_initialized(self) -> bool: ...
    def get_lateral_friction_dir1(self) -> LVector3: ...
    def get_lateral_friction_dir2(self) -> LVector3: ...
    def get_contact_motion1(self) -> float: ...
    def get_contact_motion2(self) -> float: ...
    def get_combined_friction(self) -> float: ...
    def get_combined_restitution(self) -> float: ...
    def get_applied_impulse_lateral1(self) -> float: ...
    def get_applied_impulse_lateral2(self) -> float: ...
    def get_contact_cfm1(self) -> float: ...
    def get_contact_cfm2(self) -> float: ...
    getLifeTime = get_life_time
    getDistance = get_distance
    getAppliedImpulse = get_applied_impulse
    getPositionWorldOnA = get_position_world_on_a
    getPositionWorldOnB = get_position_world_on_b
    getNormalWorldOnB = get_normal_world_on_b
    getLocalPointA = get_local_point_a
    getLocalPointB = get_local_point_b
    getPartId0 = get_part_id0
    getPartId1 = get_part_id1
    getIndex0 = get_index0
    getIndex1 = get_index1
    setLateralFrictionInitialized = set_lateral_friction_initialized
    setLateralFrictionDir1 = set_lateral_friction_dir1
    setLateralFrictionDir2 = set_lateral_friction_dir2
    setContactMotion1 = set_contact_motion1
    setContactMotion2 = set_contact_motion2
    setCombinedFriction = set_combined_friction
    setCombinedRestitution = set_combined_restitution
    setAppliedImpulse = set_applied_impulse
    setAppliedImpulseLateral1 = set_applied_impulse_lateral1
    setAppliedImpulseLateral2 = set_applied_impulse_lateral2
    setContactCfm1 = set_contact_cfm1
    setContactCfm2 = set_contact_cfm2
    getLateralFrictionInitialized = get_lateral_friction_initialized
    getLateralFrictionDir1 = get_lateral_friction_dir1
    getLateralFrictionDir2 = get_lateral_friction_dir2
    getContactMotion1 = get_contact_motion1
    getContactMotion2 = get_contact_motion2
    getCombinedFriction = get_combined_friction
    getCombinedRestitution = get_combined_restitution
    getAppliedImpulseLateral1 = get_applied_impulse_lateral1
    getAppliedImpulseLateral2 = get_applied_impulse_lateral2
    getContactCfm1 = get_contact_cfm1
    getContactCfm2 = get_contact_cfm2

class BulletContactCallbackData(CallbackData):
    @property
    def manifold(self) -> BulletManifoldPoint: ...
    @property
    def node0(self) -> PandaNode: ...
    @property
    def node1(self) -> PandaNode: ...
    @property
    def part_id0(self) -> int: ...
    @property
    def part_id1(self) -> int: ...
    @property
    def index0(self) -> int: ...
    @property
    def index1(self) -> int: ...
    def __init__(
        self, mp: BulletManifoldPoint, node0: PandaNode, node1: PandaNode, id0: int, id1: int, index0: int, index1: int
    ) -> None: ...
    def get_manifold(self) -> BulletManifoldPoint: ...
    def get_node0(self) -> PandaNode: ...
    def get_node1(self) -> PandaNode: ...
    def get_part_id0(self) -> int: ...
    def get_part_id1(self) -> int: ...
    def get_index0(self) -> int: ...
    def get_index1(self) -> int: ...
    getManifold = get_manifold
    getNode0 = get_node0
    getNode1 = get_node1
    getPartId0 = get_part_id0
    getPartId1 = get_part_id1
    getIndex0 = get_index0
    getIndex1 = get_index1

class BulletContact:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def manifold_point(self) -> BulletManifoldPoint: ...
    @property
    def node0(self) -> PandaNode: ...
    @property
    def node1(self) -> PandaNode: ...
    @property
    def idx0(self) -> int: ...
    @property
    def idx1(self) -> int: ...
    @property
    def part_id0(self) -> int: ...
    @property
    def part_id1(self) -> int: ...
    def get_manifold_point(self) -> BulletManifoldPoint: ...
    def get_node0(self) -> PandaNode: ...
    def get_node1(self) -> PandaNode: ...
    def get_idx0(self) -> int: ...
    def get_idx1(self) -> int: ...
    def get_part_id0(self) -> int: ...
    def get_part_id1(self) -> int: ...
    getManifoldPoint = get_manifold_point
    getNode0 = get_node0
    getNode1 = get_node1
    getIdx0 = get_idx0
    getIdx1 = get_idx1
    getPartId0 = get_part_id0
    getPartId1 = get_part_id1

class BulletContactResult:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def contacts(self) -> Sequence[BulletContact]: ...
    def get_num_contacts(self) -> int: ...
    def get_contact(self, idx: int) -> BulletContact: ...
    def get_contacts(self) -> tuple[BulletContact, ...]: ...
    getNumContacts = get_num_contacts
    getContact = get_contact
    getContacts = get_contacts

class BulletDebugNode(PandaNode):
    wireframe: bool
    constraints: bool
    bounding_boxes: bool
    normals: bool
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, __param0: BulletDebugNode) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def draw_mask_changed(self) -> None: ...
    def show_wireframe(self, show: bool) -> None:
        """If true, displays collision shapes in wireframe mode."""
    def show_constraints(self, show: bool) -> None:
        """If true, display limits defined for constraints, e.g. a pivot axis or maximum
        amplitude.
        """
    def show_bounding_boxes(self, show: bool) -> None:
        """If true, displays axis aligned bounding boxes for objects."""
    def show_normals(self, show: bool) -> None:
        """If true, displays normal vectors for triangle mesh and heightfield faces."""
    def get_show_wireframe(self) -> bool: ...
    def get_show_constraints(self) -> bool: ...
    def get_show_bounding_boxes(self) -> bool: ...
    def get_show_normals(self) -> bool: ...
    drawMaskChanged = draw_mask_changed
    showWireframe = show_wireframe
    showConstraints = show_constraints
    showBoundingBoxes = show_bounding_boxes
    showNormals = show_normals
    getShowWireframe = get_show_wireframe
    getShowConstraints = get_show_constraints
    getShowBoundingBoxes = get_show_bounding_boxes
    getShowNormals = get_show_normals

class BulletGhostNode(BulletBodyNode):
    @property
    def overlapping_nodes(self) -> Sequence[PandaNode]: ...
    def __init__(self, name: str = ...) -> None: ...
    def get_num_overlapping_nodes(self) -> int:
        """Overlapping"""
    def get_overlapping_node(self, idx: int) -> PandaNode: ...
    def get_overlapping_nodes(self) -> tuple[PandaNode, ...]: ...
    getNumOverlappingNodes = get_num_overlapping_nodes
    getOverlappingNode = get_overlapping_node
    getOverlappingNodes = get_overlapping_nodes

class BulletSoftBodyNodeElement:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def pos(self) -> LPoint3: ...
    @property
    def velocity(self) -> LVector3: ...
    @property
    def normal(self) -> LVector3: ...
    @property
    def inv_mass(self) -> float: ...
    @property
    def area(self) -> float: ...
    @property
    def attached(self) -> int: ...
    def __init__(self, __param0: BulletSoftBodyNodeElement) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def empty() -> BulletSoftBodyNodeElement:
        """Named constructor intended to be used for asserts with have to return a
        concrete value.
        """
    def get_pos(self) -> LPoint3: ...
    def get_velocity(self) -> LVector3: ...
    def get_normal(self) -> LVector3: ...
    def get_inv_mass(self) -> float: ...
    def get_area(self) -> float: ...
    def is_attached(self) -> int: ...
    getPos = get_pos
    getVelocity = get_velocity
    getNormal = get_normal
    getInvMass = get_inv_mass
    getArea = get_area
    isAttached = is_attached

class BulletSoftBodyNode(BulletBodyNode):
    wind_velocity: LVector3
    @property
    def cfg(self) -> BulletSoftBodyConfig: ...
    @property
    def world_info(self) -> BulletSoftBodyWorldInfo: ...
    @property
    def aabb(self) -> BoundingBox: ...
    @property
    def num_clusters(self) -> int: ...
    @property
    def materials(self) -> Sequence[BulletSoftBodyMaterial]: ...
    @property
    def nodes(self) -> Sequence[BulletSoftBodyNodeElement]: ...
    def get_cfg(self) -> BulletSoftBodyConfig: ...
    def get_world_info(self) -> BulletSoftBodyWorldInfo: ...
    def generate_bending_constraints(self, distance: int, material: BulletSoftBodyMaterial = ...) -> None: ...
    def randomize_constraints(self) -> None: ...
    def set_volume_mass(self, mass: float) -> None:
        """Mass, volume, density"""
    def set_volume_density(self, density: float) -> None: ...
    def set_total_mass(self, mass: float, fromfaces: bool = ...) -> None: ...
    def set_total_density(self, density: float) -> None: ...
    def set_mass(self, node: int, mass: float) -> None: ...
    def get_mass(self, node: int) -> float: ...
    def get_total_mass(self) -> float: ...
    def get_volume(self) -> float: ...
    def add_force(self, force: Vec3Like, node: int = ...) -> None: ...
    def set_velocity(self, velocity: Vec3Like) -> None: ...
    def add_velocity(self, velocity: Vec3Like, node: int = ...) -> None: ...
    def set_wind_velocity(self, velocity: Vec3Like) -> None: ...
    def get_wind_velocity(self) -> LVector3: ...
    def set_pose(self, bvolume: bool, bframe: bool) -> None: ...
    def get_aabb(self) -> BoundingBox: ...
    def generate_clusters(self, k: int, maxiterations: int = ...) -> None:
        """Cluster"""
    def release_cluster(self, index: int) -> None: ...
    def release_clusters(self) -> None: ...
    def get_num_clusters(self) -> int: ...
    def cluster_com(self, cluster: int) -> LVecBase3: ...
    def link_geom(self, geom: Geom) -> None:
        """Rendering"""
    def unlink_geom(self) -> None: ...
    def link_curve(self, curve: NurbsCurveEvaluator) -> None: ...
    def unlink_curve(self) -> None: ...
    def link_surface(self, surface: NurbsSurfaceEvaluator) -> None: ...
    def unlink_surface(self) -> None: ...
    @overload
    def append_anchor(self, node: int, body: BulletRigidBodyNode, disable: bool = ...) -> None:
        """Anchors"""
    @overload
    def append_anchor(self, node: int, body: BulletRigidBodyNode, pivot: Vec3Like, disable: bool = ...) -> None: ...
    @overload
    def append_linear_joint(
        self, body: BulletBodyNode, pos: Vec3Like, erp: float = ..., cfm: float = ..., split: float = ...
    ) -> None: ...
    @overload
    def append_linear_joint(
        self, body: BulletBodyNode, cluster: int, erp: float = ..., cfm: float = ..., split: float = ...
    ) -> None: ...
    def append_angular_joint(
        self,
        body: BulletBodyNode,
        axis: Vec3Like,
        erp: float = ...,
        cfm: float = ...,
        split: float = ...,
        control: BulletSoftBodyControl = ...,
    ) -> None: ...
    def get_num_materials(self) -> int:
        """Materials"""
    def get_material(self, idx: int) -> BulletSoftBodyMaterial: ...
    def append_material(self) -> BulletSoftBodyMaterial: ...
    def get_num_nodes(self) -> int: ...
    def get_node(self, idx: int) -> BulletSoftBodyNodeElement: ...
    def get_closest_node_index(self, point: Vec3Like, local: bool) -> int:
        """Returns the index of the node which is closest to the given point.  The
        distance between each node and the given point is computed in world space
        if local=false, and in local space if local=true.
        """
    @staticmethod
    def make_rope(info: BulletSoftBodyWorldInfo, _from: Vec3Like, to: Vec3Like, res: int, fixeds: int) -> BulletSoftBodyNode:
        """Factory"""
    @staticmethod
    def make_patch(
        info: BulletSoftBodyWorldInfo,
        corner00: Vec3Like,
        corner10: Vec3Like,
        corner01: Vec3Like,
        corner11: Vec3Like,
        resx: int,
        resy: int,
        fixeds: int,
        gendiags: bool,
    ) -> BulletSoftBodyNode: ...
    @staticmethod
    def make_ellipsoid(info: BulletSoftBodyWorldInfo, center: Vec3Like, radius: Vec3Like, res: int) -> BulletSoftBodyNode: ...
    @overload
    @staticmethod
    def make_tri_mesh(info: BulletSoftBodyWorldInfo, geom: Geom, randomizeConstraints: bool = ...) -> BulletSoftBodyNode: ...
    @overload
    @staticmethod
    def make_tri_mesh(
        info: BulletSoftBodyWorldInfo, points: PTA_LVecBase3, indices: PTA_int, randomizeConstraints: bool = ...
    ) -> BulletSoftBodyNode: ...
    @overload
    @staticmethod
    def make_tet_mesh(
        info: BulletSoftBodyWorldInfo, points: PTA_LVecBase3, indices: PTA_int, tetralinks: bool = ...
    ) -> BulletSoftBodyNode: ...
    @overload
    @staticmethod
    def make_tet_mesh(info: BulletSoftBodyWorldInfo, ele: str, face: str, node: str) -> BulletSoftBodyNode: ...
    def get_materials(self) -> tuple[BulletSoftBodyMaterial, ...]: ...
    def get_nodes(self) -> tuple[BulletSoftBodyNodeElement, ...]: ...
    getCfg = get_cfg
    getWorldInfo = get_world_info
    generateBendingConstraints = generate_bending_constraints
    randomizeConstraints = randomize_constraints
    setVolumeMass = set_volume_mass
    setVolumeDensity = set_volume_density
    setTotalMass = set_total_mass
    setTotalDensity = set_total_density
    setMass = set_mass
    getMass = get_mass
    getTotalMass = get_total_mass
    getVolume = get_volume
    addForce = add_force
    setVelocity = set_velocity
    addVelocity = add_velocity
    setWindVelocity = set_wind_velocity
    getWindVelocity = get_wind_velocity
    setPose = set_pose
    getAabb = get_aabb
    generateClusters = generate_clusters
    releaseCluster = release_cluster
    releaseClusters = release_clusters
    getNumClusters = get_num_clusters
    clusterCom = cluster_com
    linkGeom = link_geom
    unlinkGeom = unlink_geom
    linkCurve = link_curve
    unlinkCurve = unlink_curve
    linkSurface = link_surface
    unlinkSurface = unlink_surface
    appendAnchor = append_anchor
    appendLinearJoint = append_linear_joint
    appendAngularJoint = append_angular_joint
    getNumMaterials = get_num_materials
    getMaterial = get_material
    appendMaterial = append_material
    getNumNodes = get_num_nodes
    getNode = get_node
    getClosestNodeIndex = get_closest_node_index
    makeRope = make_rope
    makePatch = make_patch
    makeEllipsoid = make_ellipsoid
    makeTriMesh = make_tri_mesh
    makeTetMesh = make_tet_mesh
    getMaterials = get_materials
    getNodes = get_nodes

class BulletSoftBodyConfig:
    CF_rigid_vs_soft_mask: Final = 15
    CFRigidVsSoftMask: Final = 15
    CF_sdf_rigid_soft: Final = 1
    CFSdfRigidSoft: Final = 1
    CF_cluster_rigid_soft: Final = 2
    CFClusterRigidSoft: Final = 2
    CF_soft_vs_soft_mask: Final = 48
    CFSoftVsSoftMask: Final = 48
    CF_vertex_face_soft_soft: Final = 16
    CFVertexFaceSoftSoft: Final = 16
    CF_cluster_soft_soft: Final = 32
    CFClusterSoftSoft: Final = 32
    CF_cluster_self: Final = 64
    CFClusterSelf: Final = 64
    AM_vertex_point: Final = 0
    AMVertexPoint: Final = 0
    AM_vertex_two_sided: Final = 1
    AMVertexTwoSided: Final = 1
    AM_vertex_one_sided: Final = 2
    AMVertexOneSided: Final = 2
    AM_face_two_sided: Final = 3
    AMFaceTwoSided: Final = 3
    AM_face_one_sided: Final = 4
    AMFaceOneSided: Final = 4
    DtoolClassDict: ClassVar[dict[str, Any]]
    aero_model: _BulletSoftBodyConfig_AeroModel
    velocities_correction_factor: float
    damping_coefficient: float
    drag_coefficient: float
    lift_coefficient: float
    pressure_coefficient: float
    volume_conservation_coefficient: float
    dynamic_friction_coefficient: float
    pose_matching_coefficient: float
    rigid_contacts_hardness: float
    kinetic_contacts_hardness: float
    soft_contacts_hardness: float
    anchors_hardness: float
    soft_vs_rigid_hardness: float
    soft_vs_kinetic_hardness: float
    soft_vs_soft_hardness: float
    soft_vs_rigid_impulse_split: float
    soft_vs_kinetic_impulse_split: float
    soft_vs_soft_impulse_split: float
    maxvolume: float
    timescale: float
    positions_solver_iterations: int
    velocities_solver_iterations: int
    drift_solver_iterations: int
    cluster_solver_iterations: int
    def __init__(self, __param0: BulletSoftBodyConfig) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def clear_all_collision_flags(self) -> None: ...
    def set_collision_flag(self, flag: _BulletSoftBodyConfig_CollisionFlag, value: bool) -> None: ...
    def get_collision_flag(self, flag: _BulletSoftBodyConfig_CollisionFlag) -> bool: ...
    def set_aero_model(self, value: _BulletSoftBodyConfig_AeroModel) -> None: ...
    def get_aero_model(self) -> _BulletSoftBodyConfig_AeroModel: ...
    def set_velocities_correction_factor(self, value: float) -> None:
        """Setter for property kVCF."""
    def set_damping_coefficient(self, value: float) -> None:
        """Setter for property kDP."""
    def set_drag_coefficient(self, value: float) -> None:
        """Setter for property kDG."""
    def set_lift_coefficient(self, value: float) -> None:
        """Setter for property kLF."""
    def set_pressure_coefficient(self, value: float) -> None:
        """Setter for property kPR."""
    def set_volume_conservation_coefficient(self, value: float) -> None:
        """Setter for property kVC."""
    def set_dynamic_friction_coefficient(self, value: float) -> None:
        """Setter for property kDF."""
    def set_pose_matching_coefficient(self, value: float) -> None:
        """Setter for property kMT."""
    def set_rigid_contacts_hardness(self, value: float) -> None:
        """Setter for property kCHR."""
    def set_kinetic_contacts_hardness(self, value: float) -> None:
        """Setter for property kKHR."""
    def set_soft_contacts_hardness(self, value: float) -> None:
        """Setter for property kSHR."""
    def set_anchors_hardness(self, value: float) -> None:
        """Setter for property kAHR."""
    def set_soft_vs_rigid_hardness(self, value: float) -> None:
        """Setter for property kSRHR_CL."""
    def set_soft_vs_kinetic_hardness(self, value: float) -> None:
        """Setter for property kSKHR_CL."""
    def set_soft_vs_soft_hardness(self, value: float) -> None:
        """Setter for property kSSHR_CL."""
    def set_soft_vs_rigid_impulse_split(self, value: float) -> None:
        """Setter for property kSR_SPLT_CL."""
    def set_soft_vs_kinetic_impulse_split(self, value: float) -> None:
        """Setter for property kSK_SPLT_CL."""
    def set_soft_vs_soft_impulse_split(self, value: float) -> None:
        """Setter for property kSS_SPLT_CL."""
    def set_maxvolume(self, value: float) -> None:
        """Setter for property maxvolume."""
    def set_timescale(self, value: float) -> None:
        """Setter for property timescale."""
    def set_positions_solver_iterations(self, value: int) -> None:
        """Setter for property piterations."""
    def set_velocities_solver_iterations(self, value: int) -> None:
        """Setter for property viterations."""
    def set_drift_solver_iterations(self, value: int) -> None:
        """Setter for property diterations."""
    def set_cluster_solver_iterations(self, value: int) -> None:
        """Setter for property citerations."""
    def get_velocities_correction_factor(self) -> float:
        """Getter for property kVCF."""
    def get_damping_coefficient(self) -> float:
        """Getter for property kDP."""
    def get_drag_coefficient(self) -> float:
        """Getter for property kDG."""
    def get_lift_coefficient(self) -> float:
        """Getter for property kLF."""
    def get_pressure_coefficient(self) -> float:
        """Getter for property kPR."""
    def get_volume_conservation_coefficient(self) -> float:
        """Getter for property kVC."""
    def get_dynamic_friction_coefficient(self) -> float:
        """Getter for property kDF."""
    def get_pose_matching_coefficient(self) -> float:
        """Getter for property kMT."""
    def get_rigid_contacts_hardness(self) -> float:
        """Getter for property kCHR."""
    def get_kinetic_contacts_hardness(self) -> float:
        """Getter for property kKHR."""
    def get_soft_contacts_hardness(self) -> float:
        """Getter for property kSHR."""
    def get_anchors_hardness(self) -> float:
        """Getter for property kAHR."""
    def get_soft_vs_rigid_hardness(self) -> float:
        """Getter for property kSRHR_CL."""
    def get_soft_vs_kinetic_hardness(self) -> float:
        """Getter for property kSKHR_CL."""
    def get_soft_vs_soft_hardness(self) -> float:
        """Getter for property kSSHR_CL."""
    def get_soft_vs_rigid_impulse_split(self) -> float:
        """Getter for property kSR_SPLT_CL."""
    def get_soft_vs_kinetic_impulse_split(self) -> float:
        """Getter for property kSK_SPLT_CL."""
    def get_soft_vs_soft_impulse_split(self) -> float:
        """Getter for property kSS_SPLT_CL."""
    def get_maxvolume(self) -> float:
        """Getter for property maxvolume."""
    def get_timescale(self) -> float:
        """Getter for property timescale."""
    def get_positions_solver_iterations(self) -> int:
        """Getter for property piterations."""
    def get_velocities_solver_iterations(self) -> int:
        """Getter for property viterations."""
    def get_drift_solver_iterations(self) -> int:
        """Getter for property diterations."""
    def get_cluster_solver_iterations(self) -> int:
        """Getter for property citerations."""
    clearAllCollisionFlags = clear_all_collision_flags
    setCollisionFlag = set_collision_flag
    getCollisionFlag = get_collision_flag
    setAeroModel = set_aero_model
    getAeroModel = get_aero_model
    setVelocitiesCorrectionFactor = set_velocities_correction_factor
    setDampingCoefficient = set_damping_coefficient
    setDragCoefficient = set_drag_coefficient
    setLiftCoefficient = set_lift_coefficient
    setPressureCoefficient = set_pressure_coefficient
    setVolumeConservationCoefficient = set_volume_conservation_coefficient
    setDynamicFrictionCoefficient = set_dynamic_friction_coefficient
    setPoseMatchingCoefficient = set_pose_matching_coefficient
    setRigidContactsHardness = set_rigid_contacts_hardness
    setKineticContactsHardness = set_kinetic_contacts_hardness
    setSoftContactsHardness = set_soft_contacts_hardness
    setAnchorsHardness = set_anchors_hardness
    setSoftVsRigidHardness = set_soft_vs_rigid_hardness
    setSoftVsKineticHardness = set_soft_vs_kinetic_hardness
    setSoftVsSoftHardness = set_soft_vs_soft_hardness
    setSoftVsRigidImpulseSplit = set_soft_vs_rigid_impulse_split
    setSoftVsKineticImpulseSplit = set_soft_vs_kinetic_impulse_split
    setSoftVsSoftImpulseSplit = set_soft_vs_soft_impulse_split
    setMaxvolume = set_maxvolume
    setTimescale = set_timescale
    setPositionsSolverIterations = set_positions_solver_iterations
    setVelocitiesSolverIterations = set_velocities_solver_iterations
    setDriftSolverIterations = set_drift_solver_iterations
    setClusterSolverIterations = set_cluster_solver_iterations
    getVelocitiesCorrectionFactor = get_velocities_correction_factor
    getDampingCoefficient = get_damping_coefficient
    getDragCoefficient = get_drag_coefficient
    getLiftCoefficient = get_lift_coefficient
    getPressureCoefficient = get_pressure_coefficient
    getVolumeConservationCoefficient = get_volume_conservation_coefficient
    getDynamicFrictionCoefficient = get_dynamic_friction_coefficient
    getPoseMatchingCoefficient = get_pose_matching_coefficient
    getRigidContactsHardness = get_rigid_contacts_hardness
    getKineticContactsHardness = get_kinetic_contacts_hardness
    getSoftContactsHardness = get_soft_contacts_hardness
    getAnchorsHardness = get_anchors_hardness
    getSoftVsRigidHardness = get_soft_vs_rigid_hardness
    getSoftVsKineticHardness = get_soft_vs_kinetic_hardness
    getSoftVsSoftHardness = get_soft_vs_soft_hardness
    getSoftVsRigidImpulseSplit = get_soft_vs_rigid_impulse_split
    getSoftVsKineticImpulseSplit = get_soft_vs_kinetic_impulse_split
    getSoftVsSoftImpulseSplit = get_soft_vs_soft_impulse_split
    getMaxvolume = get_maxvolume
    getTimescale = get_timescale
    getPositionsSolverIterations = get_positions_solver_iterations
    getVelocitiesSolverIterations = get_velocities_solver_iterations
    getDriftSolverIterations = get_drift_solver_iterations
    getClusterSolverIterations = get_cluster_solver_iterations

class BulletSoftBodyWorldInfo:
    DtoolClassDict: ClassVar[dict[str, Any]]
    air_density: float
    water_density: float
    water_offset: float
    water_normal: LVector3
    gravity: LVector3
    def __init__(self, __param0: BulletSoftBodyWorldInfo) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_air_density(self, density: float) -> None: ...
    def set_water_density(self, density: float) -> None: ...
    def set_water_offset(self, offset: float) -> None: ...
    def set_water_normal(self, normal: Vec3Like) -> None: ...
    def set_gravity(self, gravity: Vec3Like) -> None: ...
    def get_air_density(self) -> float: ...
    def get_water_density(self) -> float: ...
    def get_water_offset(self) -> float: ...
    def get_water_normal(self) -> LVector3: ...
    def get_gravity(self) -> LVector3: ...
    def garbage_collect(self, lifetime: int = ...) -> None: ...
    setAirDensity = set_air_density
    setWaterDensity = set_water_density
    setWaterOffset = set_water_offset
    setWaterNormal = set_water_normal
    setGravity = set_gravity
    getAirDensity = get_air_density
    getWaterDensity = get_water_density
    getWaterOffset = get_water_offset
    getWaterNormal = get_water_normal
    getGravity = get_gravity
    garbageCollect = garbage_collect

class BulletSoftBodyMaterial:
    DtoolClassDict: ClassVar[dict[str, Any]]
    linear_stiffness: float
    angular_stiffness: float
    volume_preservation: float
    def __init__(self, __param0: BulletSoftBodyMaterial) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def empty() -> BulletSoftBodyMaterial:
        """Named constructor intended to be used for asserts which have to return a
        concrete value.
        """
    def get_linear_stiffness(self) -> float:
        """Getter for the property m_kLST."""
    def set_linear_stiffness(self, value: float) -> None:
        """Setter for the property m_kLST."""
    def get_angular_stiffness(self) -> float:
        """Getter for the property m_kAST."""
    def set_angular_stiffness(self, value: float) -> None:
        """Setter for the property m_kAST."""
    def get_volume_preservation(self) -> float:
        """Getter for the property m_kVST."""
    def set_volume_preservation(self, value: float) -> None:
        """Setter for the property m_kVST."""
    getLinearStiffness = get_linear_stiffness
    setLinearStiffness = set_linear_stiffness
    getAngularStiffness = get_angular_stiffness
    setAngularStiffness = set_angular_stiffness
    getVolumePreservation = get_volume_preservation
    setVolumePreservation = set_volume_preservation

class BulletVehicleTuning:
    DtoolClassDict: ClassVar[dict[str, Any]]
    suspension_stiffness: float
    suspension_compression: float
    suspension_damping: float
    max_suspension_travel_cm: float
    friction_slip: float
    max_suspension_force: float
    def set_suspension_stiffness(self, value: float) -> None: ...
    def set_suspension_compression(self, value: float) -> None: ...
    def set_suspension_damping(self, value: float) -> None: ...
    def set_max_suspension_travel_cm(self, value: float) -> None: ...
    def set_friction_slip(self, value: float) -> None: ...
    def set_max_suspension_force(self, value: float) -> None: ...
    def get_suspension_stiffness(self) -> float: ...
    def get_suspension_compression(self) -> float: ...
    def get_suspension_damping(self) -> float: ...
    def get_max_suspension_travel_cm(self) -> float: ...
    def get_friction_slip(self) -> float: ...
    def get_max_suspension_force(self) -> float: ...
    setSuspensionStiffness = set_suspension_stiffness
    setSuspensionCompression = set_suspension_compression
    setSuspensionDamping = set_suspension_damping
    setMaxSuspensionTravelCm = set_max_suspension_travel_cm
    setFrictionSlip = set_friction_slip
    setMaxSuspensionForce = set_max_suspension_force
    getSuspensionStiffness = get_suspension_stiffness
    getSuspensionCompression = get_suspension_compression
    getSuspensionDamping = get_suspension_damping
    getMaxSuspensionTravelCm = get_max_suspension_travel_cm
    getFrictionSlip = get_friction_slip
    getMaxSuspensionForce = get_max_suspension_force

class BulletVehicle(TypedReferenceCount):
    """Simulates a raycast vehicle which casts a ray per wheel at the ground as a
    cheap replacement for complex suspension simulation.  The suspension can be
    tuned in various ways.  It is possible to add a (probably) arbitrary number
    of wheels.
    """

    @property
    def chassis(self) -> BulletRigidBodyNode: ...
    @property
    def current_speed_km_hour(self) -> float: ...
    @property
    def forward_vector(self) -> LVector3: ...
    @property
    def wheels(self) -> Sequence[BulletWheel]: ...
    @property
    def tuning(self) -> BulletVehicleTuning:
        """Tuning"""
    def __init__(self, world: BulletWorld, chassis: BulletRigidBodyNode) -> None:
        """Creates a new BulletVehicle instance in the given world and with a chassis
        node.
        """
    def set_coordinate_system(self, up: _BulletUpAxis) -> None:
        """Specifies which axis is "up". Nessecary for the vehicle's suspension to
        work properly!
        """
    def set_steering_value(self, steering: float, idx: int) -> None:
        """Sets the steering value (in degrees) of the wheel with index idx."""
    def set_brake(self, brake: float, idx: int) -> None:
        """Applies braking force to the wheel with index idx."""
    def set_pitch_control(self, pitch: float) -> None: ...
    def get_chassis(self) -> BulletRigidBodyNode:
        """Returns the chassis of this vehicle.  The chassis is a rigid body node."""
    def get_current_speed_km_hour(self) -> float:
        """Returns the current speed in kilometers per hour.  Convert to miles using:
        km/h * 0.62 = mph
        """
    def get_steering_value(self, idx: int) -> float:
        """Returns the steering angle of the wheel with index idx in degrees."""
    def get_forward_vector(self) -> LVector3:
        """Returns the forward vector representing the car's actual direction of
        movement.  The forward vetcor is given in global coordinates.
        """
    def reset_suspension(self) -> None:
        """Resets the vehicle's suspension."""
    def apply_engine_force(self, force: float, idx: int) -> None:
        """Applies force at the wheel with index idx for acceleration."""
    def create_wheel(self) -> BulletWheel:
        """Factory method for creating wheels for this vehicle instance."""
    def get_num_wheels(self) -> int:
        """Returns the number of wheels this vehicle has."""
    def get_wheel(self, idx: int) -> BulletWheel:
        """Returns the BulletWheel with index idx.  Causes an AssertionError if idx is
        equal or larger than the number of wheels.
        """
    def get_tuning(self) -> BulletVehicleTuning:
        """Returns a reference to the BulletVehicleTuning object of this vehicle which
        offers various vehicle-global tuning options.  Make sure to configure this
        before adding wheels!
        """
    def get_wheels(self) -> tuple[BulletWheel, ...]: ...
    setCoordinateSystem = set_coordinate_system
    setSteeringValue = set_steering_value
    setBrake = set_brake
    setPitchControl = set_pitch_control
    getChassis = get_chassis
    getCurrentSpeedKmHour = get_current_speed_km_hour
    getSteeringValue = get_steering_value
    getForwardVector = get_forward_vector
    resetSuspension = reset_suspension
    applyEngineForce = apply_engine_force
    createWheel = create_wheel
    getNumWheels = get_num_wheels
    getWheel = get_wheel
    getTuning = get_tuning
    getWheels = get_wheels

class BulletWheel:
    """One wheel of a BulletVehicle.  Instances should not be created directly but
    using the factory method BulletVehicle::create_wheel().
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    suspension_stiffness: float
    max_suspension_travel_cm: float
    friction_slip: float
    max_suspension_force: float
    wheels_damping_compression: float
    wheels_damping_relaxation: float
    roll_influence: float
    wheel_radius: float
    steering: float
    rotation: float
    delta_rotation: float
    engine_force: float
    brake: float
    skid_info: float
    wheels_suspension_force: float
    suspension_relative_velocity: float
    clipped_inv_connection_point_cs: float
    chassis_connection_point_cs: LPoint3
    wheel_direction_cs: LVector3
    wheel_axle_cs: LVector3
    world_transform: LMatrix4
    front_wheel: bool
    node: PandaNode
    @property
    def raycast_info(self) -> BulletWheelRaycastInfo: ...
    @property
    def suspension_rest_length(self) -> float: ...
    def __init__(self, __param0: BulletWheel) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_suspension_stiffness(self, value: float) -> None:
        """Sets how stiff the suspension shall be."""
    def set_max_suspension_travel_cm(self, value: float) -> None:
        """Sets the maximum distance the suspension can travel out of the resting
        position in centimeters.
        """
    def set_friction_slip(self, value: float) -> None:
        """Sets the slipperyness of the tyre."""
    def set_max_suspension_force(self, value: float) -> None:
        """Sets the maximum suspension force the wheel can handle."""
    def set_wheels_damping_compression(self, value: float) -> None:
        """Sets the damping forces applied when the suspension gets compressed."""
    def set_wheels_damping_relaxation(self, value: float) -> None:
        """Sets the damping forces applied when the suspension relaxes."""
    def set_roll_influence(self, value: float) -> None:
        """Defines a scaling factor for roll forces that affect the chassis.  0.0
        means no roll - the chassis won't ever flip over - while 1.0 means original
        physical behaviour.  Basically, this allows moving the center of mass up
        and down.
        """
    def set_wheel_radius(self, value: float) -> None:
        """Sets the wheel radius."""
    def set_steering(self, value: float) -> None:
        """Sets the steering angle."""
    def set_rotation(self, value: float) -> None: ...
    def set_delta_rotation(self, value: float) -> None: ...
    def set_engine_force(self, value: float) -> None:
        """Defines how much force should be used to rotate the wheel."""
    def set_brake(self, value: float) -> None: ...
    def set_skid_info(self, value: float) -> None: ...
    def set_wheels_suspension_force(self, value: float) -> None: ...
    def set_suspension_relative_velocity(self, value: float) -> None: ...
    def set_clipped_inv_connection_point_cs(self, value: float) -> None: ...
    def set_chassis_connection_point_cs(self, pos: Vec3Like) -> None:
        """Sets the point where the wheel is connected to the chassis."""
    def set_wheel_direction_cs(self, dir: Vec3Like) -> None:
        """Sets the wheel's forward vector.  (Most likely orthogonal to the axle
        vector.)
        """
    def set_wheel_axle_cs(self, axle: Vec3Like) -> None:
        """Determines the wheel axle normal vector."""
    def set_world_transform(self, mat: Mat4Like) -> None: ...
    def set_front_wheel(self, value: bool) -> None:
        """Sets if the wheel is steerable."""
    def set_node(self, node: PandaNode) -> None:
        """Sets the PandaNode which representates the visual appearance of this wheel."""
    def get_suspension_rest_length(self) -> float:
        """Returns the length of the suspension when the vehicle is standing still."""
    def get_suspension_stiffness(self) -> float:
        """Returns the stiffness of the suspension."""
    def get_max_suspension_travel_cm(self) -> float: ...
    def get_friction_slip(self) -> float:
        """Returns how slippery the tyres are."""
    def get_max_suspension_force(self) -> float:
        """Returns the maximum force (weight) the suspension can handle."""
    def get_wheels_damping_compression(self) -> float:
        """Returns the  damping applied to the compressing suspension."""
    def get_wheels_damping_relaxation(self) -> float:
        """Returns the damping applied to the relaxing suspension."""
    def get_roll_influence(self) -> float:
        """Returns the factor by which roll forces are scaled.  See
        set_roll_influence.
        """
    def get_wheel_radius(self) -> float:
        """Returns the wheel radius."""
    def get_steering(self) -> float:
        """Returns the steering angle in degrees."""
    def get_rotation(self) -> float: ...
    def get_delta_rotation(self) -> float: ...
    def get_engine_force(self) -> float:
        """Returns the amount of accelleration force currently applied."""
    def get_brake(self) -> float:
        """Returns the amount of braking force currently applied."""
    def get_skid_info(self) -> float: ...
    def get_wheels_suspension_force(self) -> float: ...
    def get_suspension_relative_velocity(self) -> float: ...
    def get_clipped_inv_connection_point_cs(self) -> float: ...
    def get_chassis_connection_point_cs(self) -> LPoint3:
        """Returns the point where the wheel is connected to the chassis."""
    def get_wheel_direction_cs(self) -> LVector3:
        """Returns the wheel's forward vector relative to the chassis."""
    def get_wheel_axle_cs(self) -> LVector3:
        """Returns the normal vector of the wheel axle."""
    def get_world_transform(self) -> LMatrix4: ...
    def is_front_wheel(self) -> bool:
        """Determines if a wheel is steerable."""
    def get_node(self) -> PandaNode:
        """Returns the PandaNode which representates the visual appearance of this
        wheel, if such a representation has been set previously.
        """
    def get_raycast_info(self) -> BulletWheelRaycastInfo: ...
    setSuspensionStiffness = set_suspension_stiffness
    setMaxSuspensionTravelCm = set_max_suspension_travel_cm
    setFrictionSlip = set_friction_slip
    setMaxSuspensionForce = set_max_suspension_force
    setWheelsDampingCompression = set_wheels_damping_compression
    setWheelsDampingRelaxation = set_wheels_damping_relaxation
    setRollInfluence = set_roll_influence
    setWheelRadius = set_wheel_radius
    setSteering = set_steering
    setRotation = set_rotation
    setDeltaRotation = set_delta_rotation
    setEngineForce = set_engine_force
    setBrake = set_brake
    setSkidInfo = set_skid_info
    setWheelsSuspensionForce = set_wheels_suspension_force
    setSuspensionRelativeVelocity = set_suspension_relative_velocity
    setClippedInvConnectionPointCs = set_clipped_inv_connection_point_cs
    setChassisConnectionPointCs = set_chassis_connection_point_cs
    setWheelDirectionCs = set_wheel_direction_cs
    setWheelAxleCs = set_wheel_axle_cs
    setWorldTransform = set_world_transform
    setFrontWheel = set_front_wheel
    setNode = set_node
    getSuspensionRestLength = get_suspension_rest_length
    getSuspensionStiffness = get_suspension_stiffness
    getMaxSuspensionTravelCm = get_max_suspension_travel_cm
    getFrictionSlip = get_friction_slip
    getMaxSuspensionForce = get_max_suspension_force
    getWheelsDampingCompression = get_wheels_damping_compression
    getWheelsDampingRelaxation = get_wheels_damping_relaxation
    getRollInfluence = get_roll_influence
    getWheelRadius = get_wheel_radius
    getSteering = get_steering
    getRotation = get_rotation
    getDeltaRotation = get_delta_rotation
    getEngineForce = get_engine_force
    getBrake = get_brake
    getSkidInfo = get_skid_info
    getWheelsSuspensionForce = get_wheels_suspension_force
    getSuspensionRelativeVelocity = get_suspension_relative_velocity
    getClippedInvConnectionPointCs = get_clipped_inv_connection_point_cs
    getChassisConnectionPointCs = get_chassis_connection_point_cs
    getWheelDirectionCs = get_wheel_direction_cs
    getWheelAxleCs = get_wheel_axle_cs
    getWorldTransform = get_world_transform
    isFrontWheel = is_front_wheel
    getNode = get_node
    getRaycastInfo = get_raycast_info

class BulletWheelRaycastInfo:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def in_contact(self) -> bool: ...
    @property
    def suspension_length(self) -> float: ...
    @property
    def contact_normal_ws(self) -> LVector3: ...
    @property
    def wheel_direction_ws(self) -> LVector3: ...
    @property
    def wheel_axle_ws(self) -> LVector3: ...
    @property
    def contact_point_ws(self) -> LPoint3: ...
    @property
    def hard_point_ws(self) -> LPoint3: ...
    @property
    def ground_object(self) -> PandaNode: ...
    def __init__(self, __param0: BulletWheelRaycastInfo) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def is_in_contact(self) -> bool: ...
    def get_suspension_length(self) -> float: ...
    def get_contact_normal_ws(self) -> LVector3: ...
    def get_wheel_direction_ws(self) -> LVector3: ...
    def get_wheel_axle_ws(self) -> LVector3: ...
    def get_contact_point_ws(self) -> LPoint3: ...
    def get_hard_point_ws(self) -> LPoint3: ...
    def get_ground_object(self) -> PandaNode: ...
    isInContact = is_in_contact
    getSuspensionLength = get_suspension_length
    getContactNormalWs = get_contact_normal_ws
    getWheelDirectionWs = get_wheel_direction_ws
    getWheelAxleWs = get_wheel_axle_ws
    getContactPointWs = get_contact_point_ws
    getHardPointWs = get_hard_point_ws
    getGroundObject = get_ground_object

class BulletWorld(TypedReferenceCount):
    BA_sweep_and_prune: Final = 0
    BASweepAndPrune: Final = 0
    BA_dynamic_aabb_tree: Final = 1
    BADynamicAabbTree: Final = 1
    FA_mask: Final = 0
    FAMask: Final = 0
    FA_groups_mask: Final = 1
    FAGroupsMask: Final = 1
    FA_callback: Final = 2
    FACallback: Final = 2
    gravity: LVector3
    debug_node: BulletDebugNode
    force_update_all_aabbs: bool
    @property
    def world_info(self) -> BulletSoftBodyWorldInfo: ...
    @property
    def ghosts(self) -> Sequence[BulletGhostNode]: ...
    @property
    def rigid_bodies(self) -> Sequence[BulletRigidBodyNode]: ...
    @property
    def soft_bodies(self) -> Sequence[BulletSoftBodyNode]: ...
    @property
    def characters(self) -> Sequence[BulletBaseCharacterControllerNode]: ...
    @property
    def vehicles(self) -> Sequence[BulletVehicle]: ...
    @property
    def constraints(self) -> Sequence[BulletConstraint]: ...
    @property
    def manifolds(self) -> Sequence[BulletPersistentManifold]: ...
    def __init__(self) -> None: ...
    @overload
    def set_gravity(self, gravity: Vec3Like) -> None: ...
    @overload
    def set_gravity(self, gx: float, gy: float, gz: float) -> None: ...
    def get_gravity(self) -> LVector3: ...
    def do_physics(self, dt: float, max_substeps: int = ..., stepsize: float = ...) -> int: ...
    def get_world_info(self) -> BulletSoftBodyWorldInfo: ...
    def set_debug_node(self, node: BulletDebugNode) -> None: ...
    def clear_debug_node(self) -> None:
        """Removes a debug node that has been assigned to this BulletWorld."""
    def get_debug_node(self) -> BulletDebugNode: ...
    def has_debug_node(self) -> bool: ...
    def attach(self, object: TypedObject) -> None:
        """AttachRemove"""
    def remove(self, object: TypedObject) -> None: ...
    def attach_constraint(self, constraint: BulletConstraint, linked_collision: bool = ...) -> None:
        """Attaches a single constraint to a world.  Collision checks between the
        linked objects will be disabled if the second parameter is set to TRUE.
        """
    def get_num_ghosts(self) -> int:
        """Ghost object"""
    def get_ghost(self, idx: int) -> BulletGhostNode: ...
    def get_num_rigid_bodies(self) -> int:
        """Rigid body"""
    def get_rigid_body(self, idx: int) -> BulletRigidBodyNode: ...
    def get_num_soft_bodies(self) -> int:
        """Soft body"""
    def get_soft_body(self, idx: int) -> BulletSoftBodyNode: ...
    def get_num_characters(self) -> int:
        """Character controller"""
    def get_character(self, idx: int) -> BulletBaseCharacterControllerNode: ...
    def get_num_vehicles(self) -> int: ...
    def get_vehicle(self, idx: int) -> BulletVehicle: ...
    def get_num_constraints(self) -> int:
        """Constraint"""
    def get_constraint(self, idx: int) -> BulletConstraint: ...
    def ray_test_closest(self, from_pos: Vec3Like, to_pos: Vec3Like, mask: CollideMask | int = ...) -> BulletClosestHitRayResult:
        """Raycast and other queries"""
    def ray_test_all(self, from_pos: Vec3Like, to_pos: Vec3Like, mask: CollideMask | int = ...) -> BulletAllHitsRayResult: ...
    def sweep_test_closest(
        self,
        shape: BulletShape,
        from_ts: TransformState,
        to_ts: TransformState,
        mask: CollideMask | int = ...,
        penetration: float = ...,
    ) -> BulletClosestHitSweepResult:
        """Performs a sweep test against all other shapes that match the given group
        mask.  The provided shape must be a convex shape; it is an error to invoke
        this method using a non-convex shape.
        """
    def contact_test(self, node: PandaNode, use_filter: bool = ...) -> BulletContactResult:
        """Performas a test for all bodies which are currently in contact with the
        given body.  The test returns a BulletContactResult object which may
        contain zero, one or more contacts.

        If the optional parameter use_filter is set to TRUE this test will consider
        filter settings.  Otherwise all objects in contact are reported, no matter
        if they would collide or not.
        """
    def contact_test_pair(self, node0: PandaNode, node1: PandaNode) -> BulletContactResult:
        """Performas a test if the two bodies given as parameters are in contact or
        not.  The test returns a BulletContactResult object which may contain zero
        or one contacts.
        """
    def filter_test(self, node0: PandaNode, node1: PandaNode) -> bool:
        """Performs a test if two bodies should collide or not, based on the collision
        filter setting.
        """
    def get_num_manifolds(self) -> int:
        """Manifolds"""
    def get_manifold(self, idx: int) -> BulletPersistentManifold: ...
    def __get_manifold(self, idx: int) -> BulletPersistentManifold: ...
    def set_group_collision_flag(self, group1: int, group2: int, enable: bool) -> None:
        """Collision filtering"""
    def get_group_collision_flag(self, group1: int, group2: int) -> bool: ...
    def set_force_update_all_aabbs(self, force: bool) -> None: ...
    def get_force_update_all_aabbs(self) -> bool: ...
    def set_contact_added_callback(self, obj: Callable | CallbackObject) -> None:
        """Callbacks"""
    def clear_contact_added_callback(self) -> None: ...
    def set_tick_callback(self, obj: Callable | CallbackObject, is_pretick: bool = ...) -> None: ...
    def clear_tick_callback(self) -> None: ...
    def set_filter_callback(self, obj: Callable | CallbackObject) -> None: ...
    def clear_filter_callback(self) -> None: ...
    def attach_ghost(self, node: BulletGhostNode) -> None:
        """@deprecated Please use BulletWorld::attach"""
    def remove_ghost(self, node: BulletGhostNode) -> None:
        """@deprecated Please use BulletWorld::remove"""
    def attach_rigid_body(self, node: BulletRigidBodyNode) -> None:
        """@deprecated Please use BulletWorld::attach"""
    def remove_rigid_body(self, node: BulletRigidBodyNode) -> None:
        """@deprecated Please use BulletWorld::remove"""
    def attach_soft_body(self, node: BulletSoftBodyNode) -> None:
        """@deprecated Please use BulletWorld::attach"""
    def remove_soft_body(self, node: BulletSoftBodyNode) -> None:
        """@deprecated Please use BulletWorld::remove"""
    def attach_character(self, node: BulletBaseCharacterControllerNode) -> None:
        """@deprecated Please use BulletWorld::attach"""
    def remove_character(self, node: BulletBaseCharacterControllerNode) -> None:
        """@deprecated Please use BulletWorld::remove"""
    def attach_vehicle(self, vehicle: BulletVehicle) -> None:
        """@deprecated Please use BulletWorld::attach"""
    def remove_vehicle(self, vehicle: BulletVehicle) -> None:
        """@deprecated Please use BulletWorld::remove"""
    def remove_constraint(self, constraint: BulletConstraint) -> None:
        """@deprecated Please use BulletWorld::remove"""
    def get_ghosts(self) -> tuple[BulletGhostNode, ...]: ...
    def get_rigid_bodies(self) -> tuple[BulletRigidBodyNode, ...]: ...
    def get_soft_bodies(self) -> tuple[BulletSoftBodyNode, ...]: ...
    def get_characters(self) -> tuple[BulletBaseCharacterControllerNode, ...]: ...
    def get_vehicles(self) -> tuple[BulletVehicle, ...]: ...
    def get_constraints(self) -> tuple[BulletConstraint, ...]: ...
    def get_manifolds(self) -> tuple[BulletPersistentManifold, ...]: ...
    setGravity = set_gravity
    getGravity = get_gravity
    doPhysics = do_physics
    getWorldInfo = get_world_info
    setDebugNode = set_debug_node
    clearDebugNode = clear_debug_node
    getDebugNode = get_debug_node
    hasDebugNode = has_debug_node
    attachConstraint = attach_constraint
    getNumGhosts = get_num_ghosts
    getGhost = get_ghost
    getNumRigidBodies = get_num_rigid_bodies
    getRigidBody = get_rigid_body
    getNumSoftBodies = get_num_soft_bodies
    getSoftBody = get_soft_body
    getNumCharacters = get_num_characters
    getCharacter = get_character
    getNumVehicles = get_num_vehicles
    getVehicle = get_vehicle
    getNumConstraints = get_num_constraints
    getConstraint = get_constraint
    rayTestClosest = ray_test_closest
    rayTestAll = ray_test_all
    sweepTestClosest = sweep_test_closest
    contactTest = contact_test
    contactTestPair = contact_test_pair
    filterTest = filter_test
    getNumManifolds = get_num_manifolds
    getManifold = get_manifold
    GetManifold = __get_manifold
    setGroupCollisionFlag = set_group_collision_flag
    getGroupCollisionFlag = get_group_collision_flag
    setForceUpdateAllAabbs = set_force_update_all_aabbs
    getForceUpdateAllAabbs = get_force_update_all_aabbs
    setContactAddedCallback = set_contact_added_callback
    clearContactAddedCallback = clear_contact_added_callback
    setTickCallback = set_tick_callback
    clearTickCallback = clear_tick_callback
    setFilterCallback = set_filter_callback
    clearFilterCallback = clear_filter_callback
    attachGhost = attach_ghost
    removeGhost = remove_ghost
    attachRigidBody = attach_rigid_body
    removeRigidBody = remove_rigid_body
    attachSoftBody = attach_soft_body
    removeSoftBody = remove_soft_body
    attachCharacter = attach_character
    removeCharacter = remove_character
    attachVehicle = attach_vehicle
    removeVehicle = remove_vehicle
    removeConstraint = remove_constraint
    getGhosts = get_ghosts
    getRigidBodies = get_rigid_bodies
    getSoftBodies = get_soft_bodies
    getCharacters = get_characters
    getVehicles = get_vehicles
    getConstraints = get_constraints
    getManifolds = get_manifolds

class BulletPersistentManifold:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def node0(self) -> PandaNode: ...
    @property
    def node1(self) -> PandaNode: ...
    @property
    def manifold_points(self) -> Sequence[BulletManifoldPoint]: ...
    @property
    def contact_breaking_threshold(self) -> float: ...
    @property
    def contact_processing_threshold(self) -> float: ...
    def __init__(self, __param0: BulletPersistentManifold) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_node0(self) -> PandaNode: ...
    def get_node1(self) -> PandaNode: ...
    def get_num_manifold_points(self) -> int: ...
    def get_manifold_point(self, idx: int) -> BulletManifoldPoint: ...
    def __get_manifold_point(self, idx: int) -> BulletManifoldPoint: ...
    def get_contact_breaking_threshold(self) -> float: ...
    def get_contact_processing_threshold(self) -> float: ...
    def clear_manifold(self) -> None: ...
    def get_manifold_points(self) -> tuple[BulletManifoldPoint, ...]: ...
    getNode0 = get_node0
    getNode1 = get_node1
    getNumManifoldPoints = get_num_manifold_points
    getManifoldPoint = get_manifold_point
    GetManifoldPoint = __get_manifold_point
    getContactBreakingThreshold = get_contact_breaking_threshold
    getContactProcessingThreshold = get_contact_processing_threshold
    clearManifold = clear_manifold
    getManifoldPoints = get_manifold_points

class BulletConvexHullShape(BulletShape):
    def __init__(self, copy: BulletConvexHullShape = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def add_point(self, p: Vec3Like) -> None: ...
    def add_array(self, points: PTA_LVecBase3) -> None: ...
    def add_geom(self, geom: Geom, ts: TransformState = ...) -> None: ...
    addPoint = add_point
    addArray = add_array
    addGeom = add_geom

class BulletConvexPointCloudShape(BulletShape):
    @property
    def num_points(self) -> int: ...
    @overload
    def __init__(self, copy: BulletConvexPointCloudShape) -> None: ...
    @overload
    def __init__(self, geom: Geom, scale: Vec3Like = ...) -> None: ...
    @overload
    def __init__(self, points: PTA_LVecBase3, scale: Vec3Like = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_num_points(self) -> int: ...
    getNumPoints = get_num_points

class BulletCylinderShape(BulletShape):
    @property
    def radius(self) -> float: ...
    @property
    def half_extents_without_margin(self) -> LVecBase3: ...
    @property
    def half_extents_with_margin(self) -> LVecBase3: ...
    @overload
    def __init__(self, copy: BulletCylinderShape) -> None: ...
    @overload
    def __init__(self, half_extents: Vec3Like, up: _BulletUpAxis = ...) -> None: ...
    @overload
    def __init__(self, radius: float, height: float, up: _BulletUpAxis = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_radius(self) -> float: ...
    def get_half_extents_without_margin(self) -> LVecBase3: ...
    def get_half_extents_with_margin(self) -> LVecBase3: ...
    getRadius = get_radius
    getHalfExtentsWithoutMargin = get_half_extents_without_margin
    getHalfExtentsWithMargin = get_half_extents_with_margin

class BulletFilterCallbackData(CallbackData):
    collide: bool
    @property
    def node_0(self) -> PandaNode: ...
    @property
    def node_1(self) -> PandaNode: ...
    def __init__(self, node0: PandaNode, node1: PandaNode) -> None: ...
    def get_node_0(self) -> PandaNode: ...
    def get_node_1(self) -> PandaNode: ...
    def set_collide(self, collide: bool) -> None: ...
    def get_collide(self) -> bool: ...
    getNode0 = get_node_0
    getNode1 = get_node_1
    setCollide = set_collide
    getCollide = get_collide

class BulletRotationalLimitMotor:
    """Rotation Limit structure for generic joints."""

    DtoolClassDict: ClassVar[dict[str, Any]]
    motor_enabled: bool
    @property
    def limited(self) -> bool: ...
    @property
    def current_limit(self) -> int: ...
    @property
    def current_error(self) -> float: ...
    @property
    def current_position(self) -> float: ...
    @property
    def accumulated_impulse(self) -> float: ...
    def __init__(self, copy: BulletRotationalLimitMotor) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_motor_enabled(self, enable: bool) -> None: ...
    def set_low_limit(self, limit: float) -> None: ...
    def set_high_limit(self, limit: float) -> None: ...
    def set_target_velocity(self, velocity: float) -> None: ...
    def set_max_motor_force(self, force: float) -> None: ...
    def set_max_limit_force(self, force: float) -> None: ...
    def set_damping(self, damping: float) -> None: ...
    def set_softness(self, softness: float) -> None: ...
    def set_bounce(self, bounce: float) -> None: ...
    def set_normal_cfm(self, cfm: float) -> None: ...
    def set_stop_cfm(self, cfm: float) -> None: ...
    def set_stop_erp(self, erp: float) -> None: ...
    def is_limited(self) -> bool: ...
    def get_motor_enabled(self) -> bool: ...
    def get_current_limit(self) -> int:
        """Retrieves the current value of angle: 0 = free, 1 = at low limit, 2 = at
        high limit.
        """
    def get_current_error(self) -> float: ...
    def get_current_position(self) -> float: ...
    def get_accumulated_impulse(self) -> float: ...
    setMotorEnabled = set_motor_enabled
    setLowLimit = set_low_limit
    setHighLimit = set_high_limit
    setTargetVelocity = set_target_velocity
    setMaxMotorForce = set_max_motor_force
    setMaxLimitForce = set_max_limit_force
    setDamping = set_damping
    setSoftness = set_softness
    setBounce = set_bounce
    setNormalCfm = set_normal_cfm
    setStopCfm = set_stop_cfm
    setStopErp = set_stop_erp
    isLimited = is_limited
    getMotorEnabled = get_motor_enabled
    getCurrentLimit = get_current_limit
    getCurrentError = get_current_error
    getCurrentPosition = get_current_position
    getAccumulatedImpulse = get_accumulated_impulse

class BulletTranslationalLimitMotor:
    """Rotation Limit structure for generic joints."""

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def current_error(self) -> LVector3: ...
    @property
    def current_diff(self) -> LPoint3: ...
    @property
    def accumulated_impulse(self) -> LVector3: ...
    def __init__(self, copy: BulletTranslationalLimitMotor) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_motor_enabled(self, axis: int, enable: bool) -> None: ...
    def set_low_limit(self, limit: Vec3Like) -> None: ...
    def set_high_limit(self, limit: Vec3Like) -> None: ...
    def set_target_velocity(self, velocity: Vec3Like) -> None: ...
    def set_max_motor_force(self, force: Vec3Like) -> None: ...
    def set_damping(self, damping: float) -> None: ...
    def set_softness(self, softness: float) -> None: ...
    def set_restitution(self, restitution: float) -> None: ...
    def set_normal_cfm(self, cfm: Vec3Like) -> None: ...
    def set_stop_erp(self, erp: Vec3Like) -> None: ...
    def set_stop_cfm(self, cfm: Vec3Like) -> None: ...
    def is_limited(self, axis: int) -> bool: ...
    def get_motor_enabled(self, axis: int) -> bool: ...
    def get_current_limit(self, axis: int) -> int:
        """Retrieves the current value of angle: 0 = free, 1 = at low limit, 2 = at
        high limit.
        """
    def get_current_error(self) -> LVector3: ...
    def get_current_diff(self) -> LPoint3: ...
    def get_accumulated_impulse(self) -> LVector3: ...
    setMotorEnabled = set_motor_enabled
    setLowLimit = set_low_limit
    setHighLimit = set_high_limit
    setTargetVelocity = set_target_velocity
    setMaxMotorForce = set_max_motor_force
    setDamping = set_damping
    setSoftness = set_softness
    setRestitution = set_restitution
    setNormalCfm = set_normal_cfm
    setStopErp = set_stop_erp
    setStopCfm = set_stop_cfm
    isLimited = is_limited
    getMotorEnabled = get_motor_enabled
    getCurrentLimit = get_current_limit
    getCurrentError = get_current_error
    getCurrentDiff = get_current_diff
    getAccumulatedImpulse = get_accumulated_impulse

class BulletGenericConstraint(BulletConstraint):
    @property
    def translational_limit_motor(self) -> BulletTranslationalLimitMotor: ...
    @property
    def frame_a(self) -> TransformState: ...
    @property
    def frame_b(self) -> TransformState: ...
    @overload
    def __init__(self, node_a: BulletRigidBodyNode, frame_a: TransformState, use_frame_a: bool) -> None: ...
    @overload
    def __init__(
        self,
        node_a: BulletRigidBodyNode,
        node_b: BulletRigidBodyNode,
        frame_a: TransformState,
        frame_b: TransformState,
        use_frame_a: bool,
    ) -> None: ...
    def get_axis(self, axis: int) -> LVector3:
        """Geometry"""
    def get_pivot(self, axis: int) -> float: ...
    def get_angle(self, axis: int) -> float: ...
    def set_linear_limit(self, axis: int, low: float, high: float) -> None: ...
    def set_angular_limit(self, axis: int, low: float, high: float) -> None: ...
    def get_rotational_limit_motor(self, axis: int) -> BulletRotationalLimitMotor:
        """Motors"""
    def get_translational_limit_motor(self) -> BulletTranslationalLimitMotor: ...
    def set_frames(self, ts_a: TransformState, ts_b: TransformState) -> None:
        """Frames"""
    def get_frame_a(self) -> TransformState: ...
    def get_frame_b(self) -> TransformState: ...
    getAxis = get_axis
    getPivot = get_pivot
    getAngle = get_angle
    setLinearLimit = set_linear_limit
    setAngularLimit = set_angular_limit
    getRotationalLimitMotor = get_rotational_limit_motor
    getTranslationalLimitMotor = get_translational_limit_motor
    setFrames = set_frames
    getFrameA = get_frame_a
    getFrameB = get_frame_b

class BulletHeightfieldShape(BulletShape):
    @overload
    def __init__(self, copy: BulletHeightfieldShape) -> None:
        """`(self, image: PNMImage, max_height: float, up: _BulletUpAxis = ...)`:
        @brief Creates a collision shape suited for terrains from a rectangular image.
        @details Stores the image's brightness values in a vector Bullet can use,
          while rotating it 90 degrees to the right.

        `(self, tex: Texture, max_height: float, up: _BulletUpAxis = ...)`:
        @brief Creates a collision shape suited for terrains from a rectangular texture.
        @details Alternative constructor intended for use with ShaderTerrainMesh. This will
          do bilinear sampling at the corners of all texels. Also works with textures
          that are non-power-of-two and/or rectangular.
        """
    @overload
    def __init__(self, image: PNMImage, max_height: float, up: _BulletUpAxis = ...) -> None: ...
    @overload
    def __init__(self, tex: Texture, max_height: float, up: _BulletUpAxis = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_use_diamond_subdivision(self, flag: bool = ...) -> None: ...
    setUseDiamondSubdivision = set_use_diamond_subdivision

class BulletHelper:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def sb_index(self) -> InternalName:
        """Internal names"""
    @property
    def sb_flip(self) -> InternalName: ...
    def __init__(self, __param0: BulletHelper = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def from_collision_solids(np: NodePath, clear: bool = ...) -> NodePathCollection:
        """Collision shapes"""
    @staticmethod
    def get_sb_index() -> InternalName:
        """Internal names"""
    @staticmethod
    def get_sb_flip() -> InternalName: ...
    @staticmethod
    def add_sb_index_column(format: GeomVertexArrayFormat | GeomVertexFormat) -> GeomVertexFormat:
        """Geom vertex data"""
    @staticmethod
    def add_sb_flip_column(format: GeomVertexArrayFormat | GeomVertexFormat) -> GeomVertexFormat: ...
    @staticmethod
    def make_geom_from_faces(
        node: BulletSoftBodyNode, format: GeomVertexArrayFormat | GeomVertexFormat = ..., two_sided: bool = ...
    ) -> Geom:
        """Geom utils"""
    @staticmethod
    def make_geom_from_links(node: BulletSoftBodyNode, format: GeomVertexArrayFormat | GeomVertexFormat = ...) -> Geom: ...
    @staticmethod
    def make_texcoords_for_patch(geom: Geom, resx: int, resy: int) -> None: ...
    fromCollisionSolids = from_collision_solids
    getSbIndex = get_sb_index
    getSbFlip = get_sb_flip
    addSbIndexColumn = add_sb_index_column
    addSbFlipColumn = add_sb_flip_column
    makeGeomFromFaces = make_geom_from_faces
    makeGeomFromLinks = make_geom_from_links
    makeTexcoordsForPatch = make_texcoords_for_patch

class BulletHingeConstraint(BulletConstraint):
    """The hinge constraint lets two bodies rotate around a given axis while
    adhering to specified limits.  It's motor can apply angular force to them.
    """

    angular_only: bool
    @property
    def hinge_angle(self) -> float: ...
    @property
    def lower_limit(self) -> float: ...
    @property
    def upper_limit(self) -> float: ...
    @property
    def frame_a(self) -> TransformState: ...
    @property
    def frame_b(self) -> TransformState: ...
    @overload
    def __init__(self, node_a: BulletRigidBodyNode, ts_a: TransformState, use_frame_a: bool = ...) -> None:
        """`(self, node_a: BulletRigidBodyNode, node_b: BulletRigidBodyNode, pivot_a: LPoint3, pivot_b: LPoint3, axis_a: LVector3, axis_b: LVector3, use_frame_a: bool = ...)`:
        Creates a hinge connecting node_a to node_b.  The pivot point is the point
        at which the body is fixed to the constraint.  In other words: It specifies
        where on each body the rotation axis should be.  This axis is specified
        using axis_a and axis_b.  Remember, everything is specified in the bodies
        own coordinate system!

        `(self, node_a: BulletRigidBodyNode, node_b: BulletRigidBodyNode, ts_a: TransformState, ts_b: TransformState, use_frame_a: bool = ...)`:
        Constructs a hinge constraint which connects two rigid bodies.

        `(self, node_a: BulletRigidBodyNode, pivot_a: LPoint3, axis_a: LVector3, use_frame_a: bool = ...)`:
        Creates a hinge constraint in the same way as the other constructor, but
        uses the world as second body so that node_a is fixed to some point in mid-
        air for example.

        `(self, node_a: BulletRigidBodyNode, ts_a: TransformState, use_frame_a: bool = ...)`:
        Creates a hinge constraint which connects one rigid body with some fixe
        dpoint in the world.
        """
    @overload
    def __init__(self, node_a: BulletRigidBodyNode, pivot_a: Vec3Like, axis_a: Vec3Like, use_frame_a: bool = ...) -> None: ...
    @overload
    def __init__(
        self,
        node_a: BulletRigidBodyNode,
        node_b: BulletRigidBodyNode,
        ts_a: TransformState,
        ts_b: TransformState,
        use_frame_a: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        node_a: BulletRigidBodyNode,
        node_b: BulletRigidBodyNode,
        pivot_a: Vec3Like,
        pivot_b: Vec3Like,
        axis_a: Vec3Like,
        axis_b: Vec3Like,
        use_frame_a: bool = ...,
    ) -> None: ...
    def get_hinge_angle(self) -> float:
        """Returns the angle between node_a and node_b in degrees."""
    def get_lower_limit(self) -> float:
        """Returns the lower angular limit in degrees."""
    def get_upper_limit(self) -> float:
        """Returns the upper angular limit in degrees."""
    def get_angular_only(self) -> bool: ...
    def set_angular_only(self, value: bool) -> None: ...
    def set_limit(self, low: float, high: float, softness: float = ..., bias: float = ..., relaxation: float = ...) -> None:
        """Sets the lower and upper rotational limits in degrees."""
    def set_axis(self, axis: Vec3Like) -> None:
        """Sets the hinge's rotation axis in world coordinates."""
    def enable_angular_motor(self, enable: bool, target_velocity: float, max_impulse: float) -> None:
        """Applies an impulse to the constraint so that the angle changes at
        target_velocity where max_impulse is the maximum impulse that is used for
        achieving the specified velocity.

        Note that the target_velocity is in radians/second, not degrees.
        """
    def enable_motor(self, enable: bool) -> None: ...
    def set_max_motor_impulse(self, max_impulse: float) -> None:
        """Sets the maximum impulse used to achieve the velocity set in
        enable_angular_motor.
        """
    @overload
    def set_motor_target(self, quat: Vec4Like, dt: float) -> None: ...
    @overload
    def set_motor_target(self, target_angle: float, dt: float) -> None: ...
    def set_frames(self, ts_a: TransformState, ts_b: TransformState) -> None: ...
    def get_frame_a(self) -> TransformState: ...
    def get_frame_b(self) -> TransformState: ...
    getHingeAngle = get_hinge_angle
    getLowerLimit = get_lower_limit
    getUpperLimit = get_upper_limit
    getAngularOnly = get_angular_only
    setAngularOnly = set_angular_only
    setLimit = set_limit
    setAxis = set_axis
    enableAngularMotor = enable_angular_motor
    enableMotor = enable_motor
    setMaxMotorImpulse = set_max_motor_impulse
    setMotorTarget = set_motor_target
    setFrames = set_frames
    getFrameA = get_frame_a
    getFrameB = get_frame_b

class BulletMinkowskiSumShape(BulletShape):
    transform_a: TransformState
    transform_b: TransformState
    @property
    def shape_a(self) -> BulletShape: ...
    @property
    def shape_b(self) -> BulletShape: ...
    @overload
    def __init__(self, copy: BulletMinkowskiSumShape) -> None: ...
    @overload
    def __init__(self, shape_a: BulletShape, shape_b: BulletShape) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_transform_a(self, ts: TransformState) -> None: ...
    def set_transform_b(self, ts: TransformState) -> None: ...
    def get_transform_a(self) -> TransformState: ...
    def get_transform_b(self) -> TransformState: ...
    def get_shape_a(self) -> BulletShape: ...
    def get_shape_b(self) -> BulletShape: ...
    setTransformA = set_transform_a
    setTransformB = set_transform_b
    getTransformA = get_transform_a
    getTransformB = get_transform_b
    getShapeA = get_shape_a
    getShapeB = get_shape_b

class BulletMultiSphereShape(BulletShape):
    @property
    def sphere_count(self) -> int: ...
    @property
    def sphere_pos(self) -> Sequence[LPoint3]: ...
    @property
    def sphere_radius(self) -> Sequence[float]: ...
    @overload
    def __init__(self, copy: BulletMultiSphereShape) -> None: ...
    @overload
    def __init__(self, points: PTA_LVecBase3, radii: PTA_stdfloat) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def get_sphere_count(self) -> int: ...
    def get_sphere_pos(self, index: int) -> LPoint3: ...
    def get_sphere_radius(self, index: int) -> float: ...
    getSphereCount = get_sphere_count
    getSpherePos = get_sphere_pos
    getSphereRadius = get_sphere_radius

class BulletPlaneShape(BulletShape):
    @property
    def plane(self) -> LPlane: ...
    @property
    def plane_normal(self) -> LVector3: ...
    @property
    def plane_constant(self) -> float: ...
    @overload
    def __init__(self, copy: BulletPlaneShape) -> None:
        """Creates a plane shape from a plane definition."""
    @overload
    def __init__(self, plane: Vec4Like) -> None: ...
    @overload
    def __init__(self, normal: Vec3Like, constant: float) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_plane(self) -> LPlane: ...
    def get_plane_normal(self) -> LVector3: ...
    def get_plane_constant(self) -> float: ...
    @staticmethod
    def make_from_solid(solid: CollisionPlane | LPlanef) -> BulletPlaneShape: ...
    getPlane = get_plane
    getPlaneNormal = get_plane_normal
    getPlaneConstant = get_plane_constant
    makeFromSolid = make_from_solid

class BulletSliderConstraint(BulletConstraint):
    lower_linear_limit: float
    """Limits"""
    upper_linear_limit: float
    lower_angular_limit: float
    upper_angular_limit: float
    powered_linear_motor: bool
    target_linear_motor_velocity: float
    max_linear_motor_force: float
    powered_angular_motor: bool
    target_angular_motor_velocity: float
    max_angular_motor_force: float
    @property
    def linear_pos(self) -> float: ...
    @property
    def angular_pos(self) -> float: ...
    @property
    def frame_a(self) -> TransformState: ...
    @property
    def frame_b(self) -> TransformState: ...
    @overload
    def __init__(self, node_a: BulletRigidBodyNode, frame_a: TransformState, useFrame_a: bool) -> None: ...
    @overload
    def __init__(
        self,
        node_a: BulletRigidBodyNode,
        node_b: BulletRigidBodyNode,
        frame_a: TransformState,
        frame_b: TransformState,
        use_frame_a: bool,
    ) -> None: ...
    def get_linear_pos(self) -> float: ...
    def get_angular_pos(self) -> float: ...
    def get_lower_linear_limit(self) -> float:
        """Limits"""
    def get_upper_linear_limit(self) -> float: ...
    def get_lower_angular_limit(self) -> float: ...
    def get_upper_angular_limit(self) -> float: ...
    def set_lower_linear_limit(self, value: float) -> None: ...
    def set_upper_linear_limit(self, value: float) -> None: ...
    def set_lower_angular_limit(self, value: float) -> None: ...
    def set_upper_angular_limit(self, value: float) -> None: ...
    def set_powered_linear_motor(self, on: bool) -> None:
        """Linear motor"""
    def set_target_linear_motor_velocity(self, target_velocity: float) -> None: ...
    def set_max_linear_motor_force(self, max_force: float) -> None: ...
    def get_powered_linear_motor(self) -> bool: ...
    def get_target_linear_motor_velocity(self) -> float: ...
    def get_max_linear_motor_force(self) -> float: ...
    def set_powered_angular_motor(self, on: bool) -> None:
        """Angular motor"""
    def set_target_angular_motor_velocity(self, target_velocity: float) -> None: ...
    def set_max_angular_motor_force(self, max_force: float) -> None: ...
    def get_powered_angular_motor(self) -> bool: ...
    def get_target_angular_motor_velocity(self) -> float: ...
    def get_max_angular_motor_force(self) -> float: ...
    def set_frames(self, ts_a: TransformState, ts_b: TransformState) -> None:
        """Frames"""
    def get_frame_a(self) -> TransformState: ...
    def get_frame_b(self) -> TransformState: ...
    getLinearPos = get_linear_pos
    getAngularPos = get_angular_pos
    getLowerLinearLimit = get_lower_linear_limit
    getUpperLinearLimit = get_upper_linear_limit
    getLowerAngularLimit = get_lower_angular_limit
    getUpperAngularLimit = get_upper_angular_limit
    setLowerLinearLimit = set_lower_linear_limit
    setUpperLinearLimit = set_upper_linear_limit
    setLowerAngularLimit = set_lower_angular_limit
    setUpperAngularLimit = set_upper_angular_limit
    setPoweredLinearMotor = set_powered_linear_motor
    setTargetLinearMotorVelocity = set_target_linear_motor_velocity
    setMaxLinearMotorForce = set_max_linear_motor_force
    getPoweredLinearMotor = get_powered_linear_motor
    getTargetLinearMotorVelocity = get_target_linear_motor_velocity
    getMaxLinearMotorForce = get_max_linear_motor_force
    setPoweredAngularMotor = set_powered_angular_motor
    setTargetAngularMotorVelocity = set_target_angular_motor_velocity
    setMaxAngularMotorForce = set_max_angular_motor_force
    getPoweredAngularMotor = get_powered_angular_motor
    getTargetAngularMotorVelocity = get_target_angular_motor_velocity
    getMaxAngularMotorForce = get_max_angular_motor_force
    setFrames = set_frames
    getFrameA = get_frame_a
    getFrameB = get_frame_b

class BulletSoftBodyControl:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: BulletSoftBodyControl = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_goal(self, goal: float) -> None: ...
    def set_max_torque(self, maxtorque: float) -> None: ...
    def set_angle(self, angle: float) -> None: ...
    def set_sign(self, sign: float) -> None: ...
    setGoal = set_goal
    setMaxTorque = set_max_torque
    setAngle = set_angle
    setSign = set_sign

class BulletSoftBodyShape(BulletShape):
    @property
    def body(self) -> BulletSoftBodyNode: ...
    def get_body(self) -> BulletSoftBodyNode: ...
    getBody = get_body

class BulletSphereShape(BulletShape):
    @property
    def radius(self) -> float: ...
    @overload
    def __init__(self, copy: BulletSphereShape) -> None: ...
    @overload
    def __init__(self, radius: float) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_radius(self) -> float:
        """Returns the radius that was used to construct this sphere."""
    @staticmethod
    def make_from_solid(solid: CollisionSphere) -> BulletSphereShape: ...
    getRadius = get_radius
    makeFromSolid = make_from_solid

class BulletSphericalConstraint(BulletConstraint):
    """A constraint between two rigid bodies, each with a pivot point.  The pivot
    points are described in the body's local space.  The constraint limits
    movement of the two rigid bodies in such a way that the pivot points match
    in global space.  The spherical constraint can be seen as a "ball and
    socket" joint.
    """

    pivot_a: LPoint3
    pivot_b: LPoint3
    @overload
    def __init__(self, node_a: BulletRigidBodyNode, pivot_a: Vec3Like) -> None: ...
    @overload
    def __init__(
        self, node_a: BulletRigidBodyNode, node_b: BulletRigidBodyNode, pivot_a: Vec3Like, pivot_b: Vec3Like
    ) -> None: ...
    def set_pivot_a(self, pivot_a: Vec3Like) -> None:
        """Pivots"""
    def set_pivot_b(self, pivot_b: Vec3Like) -> None: ...
    def get_pivot_in_a(self) -> LPoint3: ...
    def get_pivot_in_b(self) -> LPoint3: ...
    setPivotA = set_pivot_a
    setPivotB = set_pivot_b
    getPivotInA = get_pivot_in_a
    getPivotInB = get_pivot_in_b

class BulletTickCallbackData(CallbackData):
    @property
    def timestep(self) -> float: ...
    def __init__(self, timestep: float) -> None: ...
    def get_timestep(self) -> float: ...
    getTimestep = get_timestep

class BulletTriangleMesh(TypedWritableReferenceCount):
    welding_distance: float
    @property
    def vertices(self) -> Sequence[LPoint3]: ...
    @property
    def triangles(self) -> Sequence[LVecBase3i]: ...
    def __init__(self) -> None: ...
    def add_triangle(self, p0: Vec3Like, p1: Vec3Like, p2: Vec3Like, remove_duplicate_vertices: bool = ...) -> None:
        """Adds a triangle with the indicated coordinates.

        If remove_duplicate_vertices is true, it will make sure that it does not
        add duplicate vertices if they already exist in the triangle mesh, within
        the tolerance specified by set_welding_distance().  This comes at a
        significant performance cost, especially for large meshes.
        """
    def add_array(self, points: PTA_LVecBase3, indices: PTA_int, remove_duplicate_vertices: bool = ...) -> None:
        """Adds triangle information from an array of points and indices referring to
        these points.  This is more efficient than adding triangles one at a time.

        If remove_duplicate_vertices is true, it will make sure that it does not
        add duplicate vertices if they already exist in the triangle mesh, within
        the tolerance specified by set_welding_distance().  This comes at a
        significant performance cost, especially for large meshes.
        """
    def add_geom(self, geom: Geom, remove_duplicate_vertices: bool = ..., ts: TransformState = ...) -> None:
        """Adds the geometry from the indicated Geom from the triangle mesh.  This is
        a one-time copy operation, and future updates to the Geom will not be
        reflected.

        If remove_duplicate_vertices is true, it will make sure that it does not
        add duplicate vertices if they already exist in the triangle mesh, within
        the tolerance specified by set_welding_distance().  This comes at a
        significant performance cost, especially for large meshes.
        """
    def set_welding_distance(self, distance: float) -> None:
        """Sets the square of the distance at which vertices will be merged
        together when adding geometry with remove_duplicate_vertices set to true.

        The default is 0, meaning vertices will only be merged if they have the
        exact same position.
        """
    def preallocate(self, num_verts: int, num_indices: int) -> None:
        """Used to reserve memory in anticipation of the given amount of vertices and
        indices being added to the triangle mesh.  This is useful if you are about
        to call add_triangle() many times, to prevent unnecessary reallocations.
        """
    def get_num_triangles(self) -> int:
        """Returns the number of triangles in this triangle mesh."""
    def get_welding_distance(self) -> float:
        """Returns the value previously set with set_welding_distance(), or the
        value of 0 if none was set.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    addTriangle = add_triangle
    addArray = add_array
    addGeom = add_geom
    setWeldingDistance = set_welding_distance
    getNumTriangles = get_num_triangles
    getWeldingDistance = get_welding_distance

class BulletTriangleMeshShape(BulletShape):
    @property
    def static(self) -> bool: ...
    @property
    def dynamic(self) -> bool: ...
    @overload
    def __init__(self, copy: BulletTriangleMeshShape) -> None:
        """The parameters 'compress' and 'bvh' are only used if 'dynamic' is set to
        FALSE.
        Assumes the lock(bullet global lock) is held by the caller
        """
    @overload
    def __init__(self, mesh: BulletTriangleMesh, dynamic: bool, compress: bool = ..., bvh: bool = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def refit_tree(self, aabb_min: Vec3Like, aabb_max: Vec3Like) -> None: ...
    def is_static(self) -> bool: ...
    def is_dynamic(self) -> bool: ...
    refitTree = refit_tree
    isStatic = is_static
    isDynamic = is_dynamic

X_up: Final = 0
XUp: Final = 0
Y_up: Final = 1
YUp: Final = 1
Z_up: Final = 2
ZUp: Final = 2

def get_default_up_axis() -> _BulletUpAxis: ...
def get_bullet_version() -> int:
    """Returns the version of the linked Bullet library."""

getDefaultUpAxis = get_default_up_axis
getBulletVersion = get_bullet_version
