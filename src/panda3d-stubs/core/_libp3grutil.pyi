from os import PathLike
from typing import Any, ClassVar, Literal, TypeAlias, overload

_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike
_Vec3d: TypeAlias = LVecBase3d | LMatrix3d.Row | LMatrix3d.CRow
_PfmVizzer_ColumnType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
_PfmVizzer_MeshFace: TypeAlias = Literal[1, 2, 3]

class CardMaker(Namable):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: CardMaker) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def reset(self) -> None: ...
    @overload
    def set_uv_range(self, tex: Texture) -> None: ...
    @overload
    def set_uv_range(self, ll: LVecBase2f, ur: LVecBase2f) -> None: ...
    @overload
    def set_uv_range(self, x: _Vec4f, y: _Vec4f, z: _Vec4f) -> None: ...
    @overload
    def set_uv_range(self, ll: LVecBase2f, lr: LVecBase2f, ur: LVecBase2f, ul: LVecBase2f) -> None: ...
    @overload
    def set_uv_range(self, ll: _Vec3f, lr: _Vec3f, ur: _Vec3f, ul: _Vec3f) -> None: ...
    def set_uv_range_cube(self, face: int) -> None: ...
    def set_has_uvs(self, flag: bool) -> None: ...
    def set_has_3d_uvs(self, flag: bool) -> None: ...
    @overload
    def set_frame(self, frame: _Vec4f) -> None: ...
    @overload
    def set_frame(self, ll: _Vec3f, lr: _Vec3f, ur: _Vec3f, ul: _Vec3f) -> None: ...
    @overload
    def set_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def set_frame_fullscreen_quad(self) -> None: ...
    @overload
    def set_color(self, color: _Vec4f) -> None: ...
    @overload
    def set_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def set_has_normals(self, flag: bool) -> None: ...
    def set_source_geometry(self, node: PandaNode, frame: _Vec4f) -> None: ...
    def clear_source_geometry(self) -> None: ...
    def generate(self) -> PandaNode: ...
    setUvRange = set_uv_range
    setUvRangeCube = set_uv_range_cube
    setHasUvs = set_has_uvs
    setHas3dUvs = set_has_3d_uvs
    setFrame = set_frame
    setFrameFullscreenQuad = set_frame_fullscreen_quad
    setColor = set_color
    setHasNormals = set_has_normals
    setSourceGeometry = set_source_geometry
    clearSourceGeometry = clear_source_geometry

class FisheyeMaker(Namable):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: FisheyeMaker) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def reset(self) -> None: ...
    def set_fov(self, fov: float) -> None: ...
    def set_num_vertices(self, num_vertices: int) -> None: ...
    def set_square_inscribed(self, square_inscribed: bool, square_radius: float) -> None: ...
    def set_reflection(self, reflection: bool) -> None: ...
    def generate(self) -> PandaNode: ...
    setFov = set_fov
    setNumVertices = set_num_vertices
    setSquareInscribed = set_square_inscribed
    setReflection = set_reflection

class FrameRateMeter(TextNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: FrameRateMeter) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def setup_window(self, window: GraphicsOutput) -> None: ...
    def clear_window(self) -> None: ...
    def get_window(self) -> GraphicsOutput: ...
    def get_display_region(self) -> DisplayRegion: ...
    def set_update_interval(self, update_interval: float) -> None: ...
    def get_update_interval(self) -> float: ...
    def set_text_pattern(self, text_pattern: str) -> None: ...
    def get_text_pattern(self) -> str: ...
    def set_clock_object(self, clock_object: ClockObject) -> None: ...
    def get_clock_object(self) -> ClockObject: ...
    def update(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setupWindow = setup_window
    clearWindow = clear_window
    getWindow = get_window
    getDisplayRegion = get_display_region
    setUpdateInterval = set_update_interval
    getUpdateInterval = get_update_interval
    setTextPattern = set_text_pattern
    getTextPattern = get_text_pattern
    setClockObject = set_clock_object
    getClockObject = get_clock_object
    getClassType = get_class_type

class GeoMipTerrain(TypedObject):
    DtoolClassDict: ClassVar[dict[str, Any]]
    AFM_off: ClassVar[Literal[0]]
    AFM_light: ClassVar[Literal[1]]
    AFM_medium: ClassVar[Literal[2]]
    AFM_strong: ClassVar[Literal[3]]
    def __init__(self, name: str) -> None: ...
    def heightfield(self) -> PNMImage: ...
    @overload
    def set_heightfield(self, image: PNMImage) -> bool: ...
    @overload
    def set_heightfield(self, filename: _Filename, type: PNMFileType = ...) -> bool: ...
    def color_map(self) -> PNMImage: ...
    @overload
    def set_color_map(self, image: PNMImage | Texture) -> bool: ...
    @overload
    def set_color_map(self, path: str) -> bool: ...
    @overload
    def set_color_map(self, filename: _Filename, type: PNMFileType = ...) -> bool: ...
    def has_color_map(self) -> bool: ...
    def clear_color_map(self) -> None: ...
    def calc_ambient_occlusion(self, radius: float = ..., contrast: float = ..., brightness: float = ...) -> None: ...
    def get_elevation(self, x: float, y: float) -> float: ...
    @overload
    def get_normal(self, x: int, y: int) -> LVector3f: ...
    @overload
    def get_normal(self, mx: int, my: int, x: int, y: int) -> LVector3f: ...
    def set_bruteforce(self, bf: bool) -> None: ...
    def get_bruteforce(self) -> bool: ...
    def set_auto_flatten(self, mode: int) -> None: ...
    @overload
    def set_focal_point(self, fp: LVecBase2d | LVecBase2f | _Vec3d | _Vec3f) -> None: ...
    @overload
    def set_focal_point(self, fnp: NodePath) -> None: ...
    @overload
    def set_focal_point(self, x: float, y: float) -> None: ...
    def get_focal_point(self) -> NodePath: ...
    def get_root(self) -> NodePath: ...
    def set_block_size(self, newbs: int) -> None: ...
    def get_block_size(self) -> int: ...
    def get_max_level(self) -> int: ...
    def set_min_level(self, minlevel: int) -> None: ...
    def get_min_level(self) -> int: ...
    def is_dirty(self) -> bool: ...
    def set_factor(self, factor: float) -> None: ...
    def set_near_far(self, input_near: float, input_far: float) -> None: ...
    def set_near(self, input_near: float) -> None: ...
    def set_far(self, input_far: float) -> None: ...
    def get_block_node_path(self, mx: int, my: int) -> NodePath: ...
    def get_block_from_pos(self, x: float, y: float) -> LVecBase2f: ...
    def set_border_stitching(self, stitching: bool) -> None: ...
    def get_border_stitching(self) -> bool: ...
    def get_far(self) -> float: ...
    def get_near(self) -> float: ...
    def get_flatten_mode(self) -> int: ...
    def make_slope_image(self) -> PNMImage: ...
    def generate(self) -> None: ...
    def update(self) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setHeightfield = set_heightfield
    colorMap = color_map
    setColorMap = set_color_map
    hasColorMap = has_color_map
    clearColorMap = clear_color_map
    calcAmbientOcclusion = calc_ambient_occlusion
    getElevation = get_elevation
    getNormal = get_normal
    setBruteforce = set_bruteforce
    getBruteforce = get_bruteforce
    setAutoFlatten = set_auto_flatten
    setFocalPoint = set_focal_point
    getFocalPoint = get_focal_point
    getRoot = get_root
    setBlockSize = set_block_size
    getBlockSize = get_block_size
    getMaxLevel = get_max_level
    setMinLevel = set_min_level
    getMinLevel = get_min_level
    isDirty = is_dirty
    setFactor = set_factor
    setNearFar = set_near_far
    setNear = set_near
    setFar = set_far
    getBlockNodePath = get_block_node_path
    getBlockFromPos = get_block_from_pos
    setBorderStitching = set_border_stitching
    getBorderStitching = get_border_stitching
    getFar = get_far
    getNear = get_near
    getFlattenMode = get_flatten_mode
    makeSlopeImage = make_slope_image
    getClassType = get_class_type
    AFMOff = AFM_off
    AFMLight = AFM_light
    AFMMedium = AFM_medium
    AFMStrong = AFM_strong

class HeightfieldTesselator(Namable):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: HeightfieldTesselator) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def heightfield(self) -> PNMImage: ...
    def set_heightfield(self, filename: _Filename, type: PNMFileType = ...) -> bool: ...
    def set_poly_count(self, n: int) -> None: ...
    def set_visibility_radius(self, r: int) -> None: ...
    def set_focal_point(self, x: int, y: int) -> None: ...
    def set_horizontal_scale(self, h: float) -> None: ...
    def set_vertical_scale(self, v: float) -> None: ...
    def set_max_triangles(self, n: int) -> None: ...
    def get_elevation(self, x: float, y: float) -> float: ...
    def generate(self) -> NodePath: ...
    setHeightfield = set_heightfield
    setPolyCount = set_poly_count
    setVisibilityRadius = set_visibility_radius
    setFocalPoint = set_focal_point
    setHorizontalScale = set_horizontal_scale
    setVerticalScale = set_vertical_scale
    setMaxTriangles = set_max_triangles
    getElevation = get_elevation

class LineSegs(Namable):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, __param0: LineSegs) -> None: ...
    def reset(self) -> None: ...
    @overload
    def set_color(self, color: _Vec4f) -> None: ...
    @overload
    def set_color(self, r: float, g: float, b: float, a: float = ...) -> None: ...
    def set_thickness(self, thick: float) -> None: ...
    @overload
    def move_to(self, v: _Vec3f) -> None: ...
    @overload
    def move_to(self, x: float, y: float, z: float) -> None: ...
    @overload
    def draw_to(self, v: _Vec3f) -> None: ...
    @overload
    def draw_to(self, x: float, y: float, z: float) -> None: ...
    def get_current_position(self) -> LPoint3f: ...
    def is_empty(self) -> bool: ...
    @overload
    def create(self, dynamic: bool = ...) -> GeomNode: ...
    @overload
    def create(self, previous: GeomNode, dynamic: bool = ...) -> GeomNode: ...
    def get_num_vertices(self) -> int: ...
    def get_vertex(self, n: int) -> LPoint3f: ...
    @overload
    def set_vertex(self, n: int, vert: _Vec3f) -> None: ...
    @overload
    def set_vertex(self, vertex: int, x: float, y: float, z: float) -> None: ...
    def get_vertex_color(self, vertex: int) -> LVecBase4f: ...
    @overload
    def set_vertex_color(self, vertex: int, c: _Vec4f) -> None: ...
    @overload
    def set_vertex_color(self, vertex: int, r: float, g: float, b: float, a: float = ...) -> None: ...
    def get_vertices(self) -> tuple[LPoint3f, ...]: ...
    def get_vertex_colors(self) -> tuple[LVecBase4f, ...]: ...
    setColor = set_color
    setThickness = set_thickness
    moveTo = move_to
    drawTo = draw_to
    getCurrentPosition = get_current_position
    isEmpty = is_empty
    getNumVertices = get_num_vertices
    getVertex = get_vertex
    setVertex = set_vertex
    getVertexColor = get_vertex_color
    setVertexColor = set_vertex_color
    getVertices = get_vertices
    getVertexColors = get_vertex_colors

class MeshDrawer(TypedObject):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    def set_budget(self, budget: int) -> None: ...
    def get_budget(self) -> int: ...
    def get_root(self) -> NodePath: ...
    def begin(self, camera: NodePath, render: NodePath) -> None: ...
    def tri(self, v1: _Vec3f, c1: _Vec4f, uv1: LVecBase2f, v2: _Vec3f, c2: _Vec4f, uv2: LVecBase2f, v3: _Vec3f, c3: _Vec4f, uv3: LVecBase2f) -> None: ...
    def particle(self, pos: _Vec3f, frame: _Vec4f, size: float, color: _Vec4f, rotation: float) -> None: ...
    def blended_particle(self, pos: _Vec3f, frame1: _Vec4f, frame2: _Vec4f, blend: float, size: float, color: _Vec4f, rotation: float) -> None: ...
    def billboard(self, pos: _Vec3f, frame: _Vec4f, size: float, color: _Vec4f) -> None: ...
    def segment(self, start: _Vec3f, stop: _Vec3f, frame: _Vec4f, thickness: float, color: _Vec4f) -> None: ...
    def cross_segment(self, start: _Vec3f, stop: _Vec3f, frame: _Vec4f, thickness: float, color: _Vec4f) -> None: ...
    def uneven_segment(self, start: _Vec3f, stop: _Vec3f, frame: _Vec4f, thickness_start: float, color_start: _Vec4f, thickness_stop: float, color_stop: _Vec4f) -> None: ...
    def link_segment(self, pos: _Vec3f, frame: _Vec4f, thickness: float, color: _Vec4f) -> None: ...
    def link_segment_end(self, frame: _Vec4f, color: _Vec4f) -> None: ...
    def explosion(self, pos: _Vec3f, frame: _Vec4f, size: float, color: _Vec4f, seed: int, number: int, distance: float) -> None: ...
    def stream(self, start: _Vec3f, stop: _Vec3f, frame: _Vec4f, size: float, color: _Vec4f, number: int, offset: float) -> None: ...
    def geometry(self, node: NodePath) -> None: ...
    def end(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setBudget = set_budget
    getBudget = get_budget
    getRoot = get_root
    blendedParticle = blended_particle
    crossSegment = cross_segment
    unevenSegment = uneven_segment
    linkSegment = link_segment
    linkSegmentEnd = link_segment_end
    getClassType = get_class_type

class MeshDrawer2D(TypedObject):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    def set_budget(self, budget: int) -> None: ...
    def get_budget(self) -> int: ...
    def get_root(self) -> NodePath: ...
    def quad_raw(self, v1: _Vec3f, c1: _Vec4f, uv1: LVecBase2f, v2: _Vec3f, c2: _Vec4f, uv2: LVecBase2f, v3: _Vec3f, c3: _Vec4f, uv3: LVecBase2f, v4: _Vec3f, c4: _Vec4f, uv4: LVecBase2f) -> None: ...
    def rectangle_raw(self, x: float, y: float, w: float, h: float, u: float, v: float, us: float, vs: float, color: _Vec4f) -> None: ...
    def set_clip(self, x: float, y: float, w: float, h: float) -> None: ...
    def rectangle(self, x: float, y: float, w: float, h: float, u: float, v: float, us: float, vs: float, color: _Vec4f) -> None: ...
    def rectangle_border(self, x: float, y: float, w: float, h: float, r: float, t: float, l: float, b: float, tr: float, tt: float, tl: float, tb: float, u: float, v: float, us: float, vs: float, color: _Vec4f) -> None: ...
    def rectangle_border_tiled(self, x: float, y: float, w: float, h: float, r: float, t: float, l: float, b: float, tr: float, tt: float, tl: float, tb: float, u: float, v: float, us: float, vs: float, color: _Vec4f) -> None: ...
    def rectangle_tiled(self, x: float, y: float, w: float, h: float, u: float, v: float, us: float, vs: float, color: _Vec4f) -> None: ...
    def begin(self) -> None: ...
    def end(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setBudget = set_budget
    getBudget = get_budget
    getRoot = get_root
    quadRaw = quad_raw
    rectangleRaw = rectangle_raw
    setClip = set_clip
    rectangleBorder = rectangle_border
    rectangleBorderTiled = rectangle_border_tiled
    rectangleTiled = rectangle_tiled
    getClassType = get_class_type

class MovieTexture(Texture):
    DtoolClassDict: ClassVar[dict[str, Any]]
    time: float
    loop: bool
    loop_count: int
    play_rate: float
    @property
    def video_length(self) -> float: ...
    @property
    def video_width(self) -> int: ...
    @property
    def video_height(self) -> int: ...
    @property
    def playing(self) -> bool: ...
    @overload
    def __init__(self, video: MovieVideo) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def get_video_length(self) -> float: ...
    def get_video_width(self) -> int: ...
    def get_video_height(self) -> int: ...
    def get_color_cursor(self, page: int) -> MovieVideoCursor: ...
    def get_alpha_cursor(self, page: int) -> MovieVideoCursor: ...
    def restart(self) -> None: ...
    def stop(self) -> None: ...
    def play(self) -> None: ...
    def set_time(self, t: float) -> None: ...
    def get_time(self) -> float: ...
    def set_loop(self, enable: bool) -> None: ...
    def get_loop(self) -> bool: ...
    def set_loop_count(self, count: int) -> None: ...
    def get_loop_count(self) -> int: ...
    def set_play_rate(self, play_rate: float) -> None: ...
    def get_play_rate(self) -> float: ...
    def is_playing(self) -> bool: ...
    def synchronize_to(self, sound: AudioSound) -> None: ...
    def unsynchronize(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getVideoLength = get_video_length
    getVideoWidth = get_video_width
    getVideoHeight = get_video_height
    getColorCursor = get_color_cursor
    getAlphaCursor = get_alpha_cursor
    setTime = set_time
    getTime = get_time
    setLoop = set_loop
    getLoop = get_loop
    setLoopCount = set_loop_count
    getLoopCount = get_loop_count
    setPlayRate = set_play_rate
    getPlayRate = get_play_rate
    isPlaying = is_playing
    synchronizeTo = synchronize_to
    getClassType = get_class_type

class MultitexReducer:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: MultitexReducer) -> None: ...
    def clear(self) -> None: ...
    @overload
    def scan(self, node: NodePath) -> None: ...
    @overload
    def scan(self, node: NodePath, state_from: NodePath) -> None: ...
    @overload
    def scan(self, node: PandaNode, state: RenderState, transform: TransformState) -> None: ...
    def set_target(self, stage: TextureStage) -> None: ...
    def set_use_geom(self, use_geom: bool) -> None: ...
    def set_allow_tex_mat(self, allow_tex_mat: bool) -> None: ...
    def flatten(self, window: GraphicsOutput) -> None: ...
    setTarget = set_target
    setUseGeom = set_use_geom
    setAllowTexMat = set_allow_tex_mat

class NodeVertexTransform(VertexTransform):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def node(self) -> PandaNode: ...
    @property
    def prev(self) -> VertexTransform: ...
    def __init__(self, node: PandaNode, prev: VertexTransform = ...) -> None: ...
    def get_node(self) -> PandaNode: ...
    def get_prev(self) -> VertexTransform: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNode = get_node
    getPrev = get_prev
    getClassType = get_class_type

class ShaderTerrainMesh(PandaNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    heightfield: Texture
    chunk_size: int
    generate_patches: bool
    update_enabled: bool
    target_triangle_width: float
    def __init__(self) -> None: ...
    def set_heightfield(self, heightfield: Texture) -> None: ...
    def get_heightfield(self) -> Texture: ...
    def set_chunk_size(self, chunk_size: int) -> None: ...
    def get_chunk_size(self) -> int: ...
    def set_generate_patches(self, generate_patches: bool) -> None: ...
    def get_generate_patches(self) -> bool: ...
    def set_update_enabled(self, update_enabled: bool) -> None: ...
    def get_update_enabled(self) -> bool: ...
    def set_target_triangle_width(self, target_triangle_width: float) -> None: ...
    def get_target_triangle_width(self) -> float: ...
    @overload
    def uv_to_world(self, coord: LVecBase2f) -> LPoint3f: ...
    @overload
    def uv_to_world(self, u: float, v: float) -> LPoint3f: ...
    def generate(self) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setHeightfield = set_heightfield
    getHeightfield = get_heightfield
    setChunkSize = set_chunk_size
    getChunkSize = get_chunk_size
    setGeneratePatches = set_generate_patches
    getGeneratePatches = get_generate_patches
    setUpdateEnabled = set_update_enabled
    getUpdateEnabled = get_update_enabled
    setTargetTriangleWidth = set_target_triangle_width
    getTargetTriangleWidth = get_target_triangle_width
    uvToWorld = uv_to_world
    getClassType = get_class_type

class SceneGraphAnalyzerMeter(TextNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: SceneGraphAnalyzerMeter) -> None: ...
    @overload
    def __init__(self, name: str, node: PandaNode) -> None: ...
    def setup_window(self, window: GraphicsOutput) -> None: ...
    def clear_window(self) -> None: ...
    def get_window(self) -> GraphicsOutput: ...
    def get_display_region(self) -> DisplayRegion: ...
    def set_update_interval(self, update_interval: float) -> None: ...
    def get_update_interval(self) -> float: ...
    def set_node(self, node: PandaNode) -> None: ...
    def get_node(self) -> PandaNode: ...
    def update(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setupWindow = setup_window
    clearWindow = clear_window
    getWindow = get_window
    getDisplayRegion = get_display_region
    setUpdateInterval = set_update_interval
    getUpdateInterval = get_update_interval
    setNode = set_node
    getNode = get_node
    getClassType = get_class_type

class RigidBodyCombiner(PandaNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def internal_scene(self) -> NodePath: ...
    def __init__(self, name: str) -> None: ...
    def collect(self) -> None: ...
    def get_internal_scene(self) -> NodePath: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getInternalScene = get_internal_scene
    getClassType = get_class_type

class PipeOcclusionCullTraverser(CullTraverser):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, host: GraphicsOutput) -> None: ...
    def upcast_to_CullTraverser(self) -> CullTraverser: ...
    def set_scene(self, scene_setup: SceneSetup, gsg: GraphicsStateGuardianBase, dr_incomplete_render: bool) -> None: ...
    def end_traverse(self) -> None: ...
    def get_buffer(self) -> GraphicsOutput: ...
    def get_texture(self) -> Texture: ...
    def set_occlusion_mask(self, occlusion_mask: BitMask_uint32_t_32) -> None: ...
    def get_occlusion_mask(self) -> BitMask_uint32_t_32: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToCullTraverser = upcast_to_CullTraverser
    setScene = set_scene
    endTraverse = end_traverse
    getBuffer = get_buffer
    getTexture = get_texture
    setOcclusionMask = set_occlusion_mask
    getOcclusionMask = get_occlusion_mask
    getClassType = get_class_type

class PfmVizzer:
    DtoolClassDict: ClassVar[dict[str, Any]]
    CT_texcoord2: ClassVar[Literal[0]]
    CT_texcoord3: ClassVar[Literal[1]]
    CT_vertex1: ClassVar[Literal[2]]
    CT_vertex2: ClassVar[Literal[3]]
    CT_vertex3: ClassVar[Literal[4]]
    CT_normal3: ClassVar[Literal[5]]
    CT_blend1: ClassVar[Literal[6]]
    CT_aux_vertex1: ClassVar[Literal[7]]
    CT_aux_vertex2: ClassVar[Literal[8]]
    CT_aux_vertex3: ClassVar[Literal[9]]
    MF_front: ClassVar[Literal[1]]
    MF_back: ClassVar[Literal[2]]
    MF_both: ClassVar[Literal[3]]
    @overload
    def __init__(self, pfm: PfmFile) -> None: ...
    @overload
    def __init__(self, __param0: PfmVizzer) -> None: ...
    def get_pfm(self) -> PfmFile: ...
    def project(self, lens: Lens, undist_lut: PfmFile = ...) -> None: ...
    def extrude(self, lens: Lens) -> None: ...
    def set_vis_inverse(self, vis_inverse: bool) -> None: ...
    def get_vis_inverse(self) -> bool: ...
    def set_flat_texcoord_name(self, flat_texcoord_name: InternalName) -> None: ...
    def clear_flat_texcoord_name(self) -> None: ...
    def get_flat_texcoord_name(self) -> InternalName: ...
    def set_vis_2d(self, vis_2d: bool) -> None: ...
    def get_vis_2d(self) -> bool: ...
    def set_keep_beyond_lens(self, keep_beyond_lens: bool) -> None: ...
    def get_keep_beyond_lens(self) -> bool: ...
    def set_vis_blend(self, vis_blend: PNMImage) -> None: ...
    def clear_vis_blend(self) -> None: ...
    def get_vis_blend(self) -> PNMImage: ...
    def set_aux_pfm(self, pfm: PfmFile) -> None: ...
    def clear_aux_pfm(self) -> None: ...
    def get_aux_pfm(self) -> PfmFile: ...
    def clear_vis_columns(self) -> None: ...
    def add_vis_column(self, source: _PfmVizzer_ColumnType, target: _PfmVizzer_ColumnType, name: InternalName, transform: TransformState = ..., lens: Lens = ..., undist_lut: PfmFile = ...) -> None: ...
    def generate_vis_points(self) -> NodePath: ...
    def generate_vis_mesh(self, face: _PfmVizzer_MeshFace = ...) -> NodePath: ...
    def calc_max_u_displacement(self) -> float: ...
    def calc_max_v_displacement(self) -> float: ...
    def make_displacement(self, result: PNMImage | PfmFile, max_u: float, max_v: float, for_32bit: bool) -> None: ...
    getPfm = get_pfm
    setVisInverse = set_vis_inverse
    getVisInverse = get_vis_inverse
    setFlatTexcoordName = set_flat_texcoord_name
    clearFlatTexcoordName = clear_flat_texcoord_name
    getFlatTexcoordName = get_flat_texcoord_name
    setVis2d = set_vis_2d
    getVis2d = get_vis_2d
    setKeepBeyondLens = set_keep_beyond_lens
    getKeepBeyondLens = get_keep_beyond_lens
    setVisBlend = set_vis_blend
    clearVisBlend = clear_vis_blend
    getVisBlend = get_vis_blend
    setAuxPfm = set_aux_pfm
    clearAuxPfm = clear_aux_pfm
    getAuxPfm = get_aux_pfm
    clearVisColumns = clear_vis_columns
    addVisColumn = add_vis_column
    generateVisPoints = generate_vis_points
    generateVisMesh = generate_vis_mesh
    calcMaxUDisplacement = calc_max_u_displacement
    calcMaxVDisplacement = calc_max_v_displacement
    makeDisplacement = make_displacement
    CTTexcoord2 = CT_texcoord2
    CTTexcoord3 = CT_texcoord3
    CTVertex1 = CT_vertex1
    CTVertex2 = CT_vertex2
    CTVertex3 = CT_vertex3
    CTNormal3 = CT_normal3
    CTBlend1 = CT_blend1
    CTAuxVertex1 = CT_aux_vertex1
    CTAuxVertex2 = CT_aux_vertex2
    CTAuxVertex3 = CT_aux_vertex3
    MFFront = MF_front
    MFBack = MF_back
    MFBoth = MF_both