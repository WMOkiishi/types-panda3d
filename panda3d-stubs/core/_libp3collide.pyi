from collections.abc import Iterable, Sequence
from typing import Any, ClassVar, TypeAlias, overload

_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor

class CollisionSolid(CopyOnWriteObject):
    DtoolClassDict: ClassVar[dict[str, Any]]
    tangible: bool
    respect_effective_normal: bool
    bounds: BoundingVolume
    @property
    def collision_origin(self) -> LPoint3f: ...
    def get_collision_origin(self) -> LPoint3f: ...
    def set_tangible(self, tangible: bool) -> None: ...
    def is_tangible(self) -> bool: ...
    def set_effective_normal(self, effective_normal: _Vec3f) -> None: ...
    def clear_effective_normal(self) -> None: ...
    def has_effective_normal(self) -> bool: ...
    def get_effective_normal(self) -> LVector3f: ...
    def set_respect_effective_normal(self, respect_effective_normal: bool) -> None: ...
    def get_respect_effective_normal(self) -> bool: ...
    def get_bounds(self) -> BoundingVolume: ...
    def set_bounds(self, bounding_volume: BoundingVolume) -> None: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type

class CollisionBox(CollisionSolid):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def center(self) -> LPoint3f: ...
    @property
    def min(self) -> LPoint3f: ...
    @property
    def max(self) -> LPoint3f: ...
    @property
    def dimensions(self) -> LVector3f: ...
    @overload
    def __init__(self, min: _Vec3f, max: _Vec3f) -> None: ...
    @overload
    def __init__(self, center: _Vec3f, x: float, y: float, z: float) -> None: ...
    def get_num_points(self) -> int: ...
    def get_point_aabb(self, n: int) -> LPoint3f: ...
    def get_point(self, n: int) -> LPoint3f: ...
    def get_num_planes(self) -> int: ...
    def set_plane(self, n: int) -> LPlanef: ...
    def get_plane(self, n: int) -> LPlanef: ...
    @overload
    def set_center(self, center: _Vec3f) -> None: ...
    @overload
    def set_center(self, x: float, y: float, z: float) -> None: ...
    def get_center(self) -> LPoint3f: ...
    def get_min(self) -> LPoint3f: ...
    def get_max(self) -> LPoint3f: ...
    def get_dimensions(self) -> LVector3f: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type

class CollisionCapsule(CollisionSolid):
    DtoolClassDict: ClassVar[dict[str, Any]]
    point_a: LPoint3f
    point_b: LPoint3f
    radius: float
    @overload
    def __init__(self, a: _Vec3f, db: _Vec3f, radius: float) -> None: ...
    @overload
    def __init__(self, ax: float, ay: float, az: float, bx: float, by: float, bz: float, radius: float) -> None: ...
    @overload
    def set_point_a(self, a: _Vec3f) -> None: ...
    @overload
    def set_point_a(self, x: float, y: float, z: float) -> None: ...
    def get_point_a(self) -> LPoint3f: ...
    @overload
    def set_point_b(self, b: _Vec3f) -> None: ...
    @overload
    def set_point_b(self, x: float, y: float, z: float) -> None: ...
    def get_point_b(self) -> LPoint3f: ...
    def set_radius(self, radius: float) -> None: ...
    def get_radius(self) -> float: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setPointA = set_point_a
    getPointA = get_point_a
    setPointB = set_point_b
    getPointB = get_point_b
    setRadius = set_radius
    getRadius = get_radius
    getClassType = get_class_type

class CollisionHandler(TypedReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: CollisionHandler) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class CollisionNode(PandaNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    from_collide_mask: BitMask_uint32_t_32
    into_collide_mask: BitMask_uint32_t_32
    solids: Sequence[CollisionSolid]
    collider_sort: int
    @property
    def default_collide_mask(self) -> BitMask_uint32_t_32: ...
    def __init__(self, name: str) -> None: ...
    def set_collide_mask(self, mask: BitMask_uint32_t_32) -> None: ...
    def set_from_collide_mask(self, mask: BitMask_uint32_t_32) -> None: ...
    def set_into_collide_mask(self, mask: BitMask_uint32_t_32) -> None: ...
    def get_from_collide_mask(self) -> BitMask_uint32_t_32: ...
    def get_into_collide_mask(self) -> BitMask_uint32_t_32: ...
    def clear_solids(self) -> None: ...
    def get_num_solids(self) -> int: ...
    def get_solid(self, n: int) -> CollisionSolid: ...
    def modify_solid(self, n: int) -> CollisionSolid: ...
    def set_solid(self, n: int, solid: CollisionSolid) -> None: ...
    def insert_solid(self, n: int, solid: CollisionSolid) -> None: ...
    def remove_solid(self, n: int) -> None: ...
    def add_solid(self, solid: CollisionSolid) -> int: ...
    def get_collider_sort(self) -> int: ...
    def set_collider_sort(self, sort: int) -> None: ...
    @staticmethod
    def get_default_collide_mask() -> BitMask_uint32_t_32: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type
    getSolids = get_solids

class CollisionTraverser(Namable):
    DtoolClassDict: ClassVar[dict[str, Any]]
    respect_preV_transform: bool
    respect_prev_transform: bool
    recorder: CollisionRecorder
    @property
    def colliders(self) -> Sequence[NodePath]: ...
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, __param0: CollisionTraverser) -> None: ...
    def set_respect_prev_transform(self, flag: bool) -> None: ...
    def get_respect_prev_transform(self) -> bool: ...
    def add_collider(self, collider: NodePath, handler: CollisionHandler) -> None: ...
    def remove_collider(self, collider: NodePath) -> bool: ...
    def has_collider(self, collider: NodePath) -> bool: ...
    def get_num_colliders(self) -> int: ...
    def get_collider(self, n: int) -> NodePath: ...
    def get_handler(self, collider: NodePath) -> CollisionHandler: ...
    def clear_colliders(self) -> None: ...
    def traverse(self, root: NodePath) -> None: ...
    def set_recorder(self, recorder: CollisionRecorder) -> None: ...
    def has_recorder(self) -> bool: ...
    def get_recorder(self) -> CollisionRecorder: ...
    def clear_recorder(self) -> None: ...
    def show_collisions(self, root: NodePath) -> CollisionVisualizer: ...
    def hide_collisions(self) -> None: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type
    getColliders = get_colliders

class CollisionRecorder(TypedObject):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class CollisionEntry(TypedWritableReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
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
    def get_from(self) -> CollisionSolid: ...
    def has_into(self) -> bool: ...
    def get_into(self) -> CollisionSolid: ...
    def get_from_node(self) -> CollisionNode: ...
    def get_into_node(self) -> PandaNode: ...
    def get_from_node_path(self) -> NodePath: ...
    def get_into_node_path(self) -> NodePath: ...
    def set_t(self, t: float) -> None: ...
    def get_t(self) -> float: ...
    def collided(self) -> bool: ...
    def reset_collided(self) -> None: ...
    def get_respect_prev_transform(self) -> bool: ...
    def set_surface_point(self, point: _Vec3f) -> None: ...
    def set_surface_normal(self, normal: _Vec3f) -> None: ...
    def set_interior_point(self, point: _Vec3f) -> None: ...
    def has_surface_point(self) -> bool: ...
    def has_surface_normal(self) -> bool: ...
    def has_interior_point(self) -> bool: ...
    def set_contact_pos(self, pos: _Vec3f) -> None: ...
    def set_contact_normal(self, normal: _Vec3f) -> None: ...
    def has_contact_pos(self) -> bool: ...
    def has_contact_normal(self) -> bool: ...
    def get_surface_point(self, space: NodePath) -> LPoint3f: ...
    def get_surface_normal(self, space: NodePath) -> LVector3f: ...
    def get_interior_point(self, space: NodePath) -> LPoint3f: ...
    def get_all(self, space: NodePath, surface_point: _Vec3f, surface_normal: _Vec3f, interior_point: _Vec3f) -> bool: ...
    def get_contact_pos(self, space: NodePath) -> LPoint3f: ...
    def get_contact_normal(self, space: NodePath) -> LVector3f: ...
    def get_all_contact_info(self, space: NodePath, contact_pos: _Vec3f, contact_normal: _Vec3f) -> bool: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type

class CollisionPlane(CollisionSolid):
    DtoolClassDict: ClassVar[dict[str, Any]]
    plane: LPlanef
    @property
    def normal(self) -> LVector3f: ...
    @overload
    def __init__(self, copy: CollisionPlane) -> None: ...
    @overload
    def __init__(self, plane: _Vec4f) -> None: ...
    def get_normal(self) -> LVector3f: ...
    def dist_to_plane(self, point: _Vec3f) -> float: ...
    def set_plane(self, plane: _Vec4f) -> None: ...
    def get_plane(self) -> LPlanef: ...
    def flip(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNormal = get_normal
    distToPlane = dist_to_plane
    setPlane = set_plane
    getPlane = get_plane
    getClassType = get_class_type

class CollisionFloorMesh(CollisionSolid):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def vertices(self) -> Sequence[LPoint3f]: ...
    @property
    def triangles(self) -> Sequence[LPoint3i]: ...
    def __init__(self) -> None: ...
    def add_vertex(self, vert: _Vec3f) -> None: ...
    def add_triangle(self, pointA: int, pointB: int, pointC: int) -> None: ...
    def get_num_vertices(self) -> int: ...
    def get_vertex(self, index: int) -> LPoint3f: ...
    def get_num_triangles(self) -> int: ...
    def get_triangle(self, index: int) -> LPoint3i: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_vertices(self) -> tuple[LPoint3f, ...]: ...
    def get_triangles(self) -> tuple[LPoint3i, ...]: ...
    addVertex = add_vertex
    addTriangle = add_triangle
    getNumVertices = get_num_vertices
    getVertex = get_vertex
    getNumTriangles = get_num_triangles
    getTriangle = get_triangle
    getClassType = get_class_type
    getVertices = get_vertices
    getTriangles = get_triangles

class CollisionPolygon(CollisionPlane):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def points(self) -> Sequence[LPoint3f]: ...
    @property
    def valid(self) -> bool: ...
    @property
    def concave(self) -> bool: ...
    @overload
    def __init__(self, a: _Vec3f, b: _Vec3f, c: _Vec3f) -> None: ...
    @overload
    def __init__(self, a: _Vec3f, b: _Vec3f, c: _Vec3f, d: _Vec3f) -> None: ...
    def get_num_points(self) -> int: ...
    def get_point(self, n: int) -> LPoint3f: ...
    @overload
    @staticmethod
    def verify_points(a: Iterable[LPoint3f], b: _Vec3f, c: _Vec3f) -> bool: ...
    @overload
    @staticmethod
    def verify_points(a: _Vec3f, b: _Vec3f, c: _Vec3f, d: _Vec3f) -> bool: ...
    def is_valid(self) -> bool: ...
    def is_concave(self) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_points(self) -> tuple[LPoint3f, ...]: ...
    getNumPoints = get_num_points
    getPoint = get_point
    verifyPoints = verify_points
    isValid = is_valid
    isConcave = is_concave
    getClassType = get_class_type
    getPoints = get_points

class CollisionHandlerEvent(CollisionHandler):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def in_patterns(self) -> Sequence[str]: ...
    @property
    def again_patterns(self) -> Sequence[str]: ...
    @property
    def out_patterns(self) -> Sequence[str]: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: CollisionHandlerEvent) -> None: ...
    def clear_in_patterns(self) -> None: ...
    def add_in_pattern(self, in_pattern: str) -> None: ...
    def set_in_pattern(self, in_pattern: str) -> None: ...
    def get_num_in_patterns(self) -> int: ...
    def get_in_pattern(self, n: int) -> str: ...
    def clear_again_patterns(self) -> None: ...
    def add_again_pattern(self, again_pattern: str) -> None: ...
    def set_again_pattern(self, again_pattern: str) -> None: ...
    def get_num_again_patterns(self) -> int: ...
    def get_again_pattern(self, n: int) -> str: ...
    def clear_out_patterns(self) -> None: ...
    def add_out_pattern(self, out_pattern: str) -> None: ...
    def set_out_pattern(self, out_pattern: str) -> None: ...
    def get_num_out_patterns(self) -> int: ...
    def get_out_pattern(self, n: int) -> str: ...
    def clear(self) -> None: ...
    def flush(self) -> None: ...
    def write_datagram(self, destination: Datagram) -> None: ...
    def read_datagram(self, source: DatagramIterator) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type
    getInPatterns = get_in_patterns
    getAgainPatterns = get_again_patterns
    getOutPatterns = get_out_patterns

class CollisionHandlerPhysical(CollisionHandlerEvent):
    DtoolClassDict: ClassVar[dict[str, Any]]
    center: NodePath
    @overload
    def add_collider(self, collider: NodePath, target: NodePath) -> None: ...
    @overload
    def add_collider(self, collider: NodePath, target: NodePath, drive_interface: DriveInterface) -> None: ...
    def remove_collider(self, collider: NodePath) -> bool: ...
    def has_collider(self, collider: NodePath) -> bool: ...
    def clear_colliders(self) -> None: ...
    def set_center(self, center: NodePath) -> None: ...
    def clear_center(self) -> None: ...
    def get_center(self) -> NodePath: ...
    def has_center(self) -> bool: ...
    def has_contact(self) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    addCollider = add_collider
    removeCollider = remove_collider
    hasCollider = has_collider
    clearColliders = clear_colliders
    setCenter = set_center
    clearCenter = clear_center
    getCenter = get_center
    hasCenter = has_center
    hasContact = has_contact
    getClassType = get_class_type

class CollisionHandlerFloor(CollisionHandlerPhysical):
    DtoolClassDict: ClassVar[dict[str, Any]]
    offset: float
    reach: float
    max_velocity: float
    def __init__(self) -> None: ...
    def set_offset(self, offset: float) -> None: ...
    def get_offset(self) -> float: ...
    def set_reach(self, reach: float) -> None: ...
    def get_reach(self) -> float: ...
    def set_max_velocity(self, max_vel: float) -> None: ...
    def get_max_velocity(self) -> float: ...
    def write_datagram(self, destination: Datagram) -> None: ...
    def read_datagram(self, source: DatagramIterator) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setOffset = set_offset
    getOffset = get_offset
    setReach = set_reach
    getReach = get_reach
    setMaxVelocity = set_max_velocity
    getMaxVelocity = get_max_velocity
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type

class CollisionHandlerPusher(CollisionHandlerPhysical):
    DtoolClassDict: ClassVar[dict[str, Any]]
    horizontal: bool
    def __init__(self) -> None: ...
    def set_horizontal(self, flag: bool) -> None: ...
    def get_horizontal(self) -> bool: ...
    def write_datagram(self, destination: Datagram) -> None: ...
    def read_datagram(self, source: DatagramIterator) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setHorizontal = set_horizontal
    getHorizontal = get_horizontal
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type

class CollisionHandlerFluidPusher(CollisionHandlerPusher):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class CollisionHandlerGravity(CollisionHandlerPhysical):
    DtoolClassDict: ClassVar[dict[str, Any]]
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
    def contact_normal(self) -> LVector3f: ...
    def __init__(self) -> None: ...
    def set_offset(self, offset: float) -> None: ...
    def get_offset(self) -> float: ...
    def set_reach(self, reach: float) -> None: ...
    def get_reach(self) -> float: ...
    def get_airborne_height(self) -> float: ...
    def is_on_ground(self) -> bool: ...
    def get_impact_velocity(self) -> float: ...
    def get_contact_normal(self) -> LVector3f: ...
    def add_velocity(self, velocity: float) -> None: ...
    def set_velocity(self, velocity: float) -> None: ...
    def get_velocity(self) -> float: ...
    def set_gravity(self, gravity: float) -> None: ...
    def get_gravity(self) -> float: ...
    def set_max_velocity(self, max_vel: float) -> None: ...
    def get_max_velocity(self) -> float: ...
    def set_legacy_mode(self, legacy_mode: bool) -> None: ...
    def get_legacy_mode(self) -> bool: ...
    def write_datagram(self, destination: Datagram) -> None: ...
    def read_datagram(self, source: DatagramIterator) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type

class CollisionHandlerHighestEvent(CollisionHandlerEvent):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: CollisionHandlerHighestEvent) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class CollisionHandlerQueue(CollisionHandler):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def entries(self) -> Sequence[CollisionEntry]: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: CollisionHandlerQueue) -> None: ...
    def sort_entries(self) -> None: ...
    def clear_entries(self) -> None: ...
    def get_num_entries(self) -> int: ...
    def get_entry(self, n: int) -> CollisionEntry: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_entries(self) -> tuple[CollisionEntry, ...]: ...
    sortEntries = sort_entries
    clearEntries = clear_entries
    getNumEntries = get_num_entries
    getEntry = get_entry
    getClassType = get_class_type
    getEntries = get_entries

class CollisionSphere(CollisionSolid):
    DtoolClassDict: ClassVar[dict[str, Any]]
    center: LPoint3f
    radius: float
    @overload
    def __init__(self, center: _Vec3f, radius: float) -> None: ...
    @overload
    def __init__(self, cx: float, cy: float, cz: float, radius: float) -> None: ...
    @overload
    def set_center(self, center: _Vec3f) -> None: ...
    @overload
    def set_center(self, x: float, y: float, z: float) -> None: ...
    def get_center(self) -> LPoint3f: ...
    def set_radius(self, radius: float) -> None: ...
    def get_radius(self) -> float: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setCenter = set_center
    getCenter = get_center
    setRadius = set_radius
    getRadius = get_radius
    getClassType = get_class_type

class CollisionInvSphere(CollisionSphere):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, center: _Vec3f, radius: float) -> None: ...
    @overload
    def __init__(self, cx: float, cy: float, cz: float, radius: float) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class CollisionRay(CollisionSolid):
    DtoolClassDict: ClassVar[dict[str, Any]]
    origin: LPoint3f
    direction: LVector3f
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, origin: _Vec3f, direction: _Vec3f) -> None: ...
    @overload
    def __init__(self, ox: float, oy: float, oz: float, dx: float, dy: float, dz: float) -> None: ...
    @overload
    def set_origin(self, origin: _Vec3f) -> None: ...
    @overload
    def set_origin(self, x: float, y: float, z: float) -> None: ...
    def get_origin(self) -> LPoint3f: ...
    @overload
    def set_direction(self, direction: _Vec3f) -> None: ...
    @overload
    def set_direction(self, x: float, y: float, z: float) -> None: ...
    def get_direction(self) -> LVector3f: ...
    @overload
    def set_from_lens(self, camera: LensNode, point: LVecBase2f) -> bool: ...
    @overload
    def set_from_lens(self, camera: LensNode, px: float, py: float) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setOrigin = set_origin
    getOrigin = get_origin
    setDirection = set_direction
    getDirection = get_direction
    setFromLens = set_from_lens
    getClassType = get_class_type

class CollisionLine(CollisionRay):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, origin: _Vec3f, direction: _Vec3f) -> None: ...
    @overload
    def __init__(self, ox: float, oy: float, oz: float, dx: float, dy: float, dz: float) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class CollisionParabola(CollisionSolid):
    DtoolClassDict: ClassVar[dict[str, Any]]
    parabola: LParabolaf
    t1: float
    t2: float
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, parabola: LParabolaf, t1: float, t2: float) -> None: ...
    def set_parabola(self, parabola: LParabolaf) -> None: ...
    def get_parabola(self) -> LParabolaf: ...
    def set_t1(self, t1: float) -> None: ...
    def get_t1(self) -> float: ...
    def set_t2(self, t2: float) -> None: ...
    def get_t2(self) -> float: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setParabola = set_parabola
    getParabola = get_parabola
    setT1 = set_t1
    getT1 = get_t1
    setT2 = set_t2
    getT2 = get_t2
    getClassType = get_class_type

class CollisionSegment(CollisionSolid):
    DtoolClassDict: ClassVar[dict[str, Any]]
    point_a: LPoint3f
    point_b: LPoint3f
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, a: _Vec3f, db: _Vec3f) -> None: ...
    @overload
    def __init__(self, ax: float, ay: float, az: float, bx: float, by: float, bz: float) -> None: ...
    @overload
    def set_point_a(self, a: _Vec3f) -> None: ...
    @overload
    def set_point_a(self, x: float, y: float, z: float) -> None: ...
    def get_point_a(self) -> LPoint3f: ...
    @overload
    def set_point_b(self, b: _Vec3f) -> None: ...
    @overload
    def set_point_b(self, x: float, y: float, z: float) -> None: ...
    def get_point_b(self) -> LPoint3f: ...
    @overload
    def set_from_lens(self, camera: LensNode, point: LVecBase2f) -> bool: ...
    @overload
    def set_from_lens(self, camera: LensNode, px: float, py: float) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setPointA = set_point_a
    getPointA = get_point_a
    setPointB = set_point_b
    getPointB = get_point_b
    setFromLens = set_from_lens
    getClassType = get_class_type

class CollisionVisualizer(PandaNode, CollisionRecorder):
    DtoolClassDict: ClassVar[dict[str, Any]]
    point_scale: float
    normal_scale: float
    @overload
    def __init__(self, copy: CollisionVisualizer) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def upcast_to_PandaNode(self) -> PandaNode: ...
    def upcast_to_CollisionRecorder(self) -> CollisionRecorder: ...
    def set_point_scale(self, point_scale: float) -> None: ...
    def get_point_scale(self) -> float: ...
    def set_normal_scale(self, normal_scale: float) -> None: ...
    def get_normal_scale(self) -> float: ...
    def clear(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToPandaNode = upcast_to_PandaNode
    upcastToCollisionRecorder = upcast_to_CollisionRecorder
    setPointScale = set_point_scale
    getPointScale = get_point_scale
    setNormalScale = set_normal_scale
    getNormalScale = get_normal_scale
    getClassType = get_class_type

CollisionTube = CollisionCapsule
