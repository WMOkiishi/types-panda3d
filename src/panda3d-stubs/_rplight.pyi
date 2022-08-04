from typing import Any, ClassVar, Literal, TypeAlias, overload
from panda3d.core import (
    BitMask_uint32_t_32,
    Camera,
    ConfigVariableColor,
    GraphicsOutput,
    LMatrix3f,
    LMatrix4f,
    LVecBase3f,
    LVecBase3i,
    LVecBase4f,
    LVecBase4i,
    NodePath,
    PointerToArray_LVecBase2f,
    PointerToArray_UnalignedLMatrix4f,
    PointerToArray_float,
    PointerToArray_unsigned_char,
    ReferenceCount,
    Shader,
    Texture,
    UnalignedLMatrix4f,
    UnalignedLVecBase4f,
    UnalignedLVecBase4i,
    ostream,
)

_GPUCommand_CommandType: TypeAlias = Literal[0, 1, 2, 3, 4]
_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_Vec4i: TypeAlias = LVecBase4i | UnalignedLVecBase4i
_Mat4f: TypeAlias = LMatrix4f | UnalignedLMatrix4f
_RPLight_LightType: TypeAlias = Literal[0, 1, 2]

class GPUCommand:
    """@brief Class for storing data to be transferred to the GPU.
    @details This class can be seen like a packet, to be transferred to the GPU.
      It has a command type, which tells the GPU what to do once it recieved this
      "packet". It stores a limited amount of floating point components.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    CMD_invalid: ClassVar[Literal[0]]
    CMD_store_light: ClassVar[Literal[1]]
    CMD_remove_light: ClassVar[Literal[2]]
    CMD_store_source: ClassVar[Literal[3]]
    CMD_remove_sources: ClassVar[Literal[4]]
    @overload
    def __init__(self, __param0: GPUCommand) -> None: ...
    @overload
    def __init__(self, command_type: _GPUCommand_CommandType) -> None: ...
    def push_int(self, v: int) -> None: ...
    def push_float(self, v: float) -> None: ...
    def push_vec3(self, v: LVecBase3i | _Vec3f) -> None: ...
    def push_vec4(self, v: _Vec4f | _Vec4i) -> None: ...
    def push_mat3(self, v: LMatrix3f) -> None: ...
    def push_mat4(self, v: _Mat4f) -> None: ...
    @staticmethod
    def get_uses_integer_packing() -> bool: ...
    def write_to(self, dest: PointerToArray_unsigned_char, command_index: int) -> None: ...
    def write(self, out: ostream) -> None: ...
    pushInt = push_int
    pushFloat = push_float
    pushVec3 = push_vec3
    pushVec4 = push_vec4
    pushMat3 = push_mat3
    pushMat4 = push_mat4
    getUsesIntegerPacking = get_uses_integer_packing
    writeTo = write_to
    CMDInvalid = CMD_invalid
    CMDStoreLight = CMD_store_light
    CMDRemoveLight = CMD_remove_light
    CMDStoreSource = CMD_store_source
    CMDRemoveSources = CMD_remove_sources

class GPUCommandList:
    """@brief Class to store a list of commands.
    @details This is a class to store a list of GPUCommands. It provides
      functionality to only provide the a given amount of commands at one time.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def num_commands(self) -> int: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: GPUCommandList) -> None: ...
    def add_command(self, cmd: GPUCommand) -> None: ...
    def get_num_commands(self) -> int: ...
    def write_commands_to(self, dest: PointerToArray_unsigned_char, limit: int = ...) -> int: ...
    addCommand = add_command
    getNumCommands = get_num_commands
    writeCommandsTo = write_commands_to

class IESDataset:
    """@brief This class generates a LUT from IES data.
    @details This class is used by the IESLoader to generate a LUT texture which
      is used in the shaders to perform IES lighting. It takes a set of vertical
      and horizontal angles, as well as a set of candela values, which then are
      lineary interpolated onto a 2D LUT Texture.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: IESDataset) -> None: ...
    def set_vertical_angles(self, vertical_angles: PointerToArray_float) -> None: ...
    def set_horizontal_angles(self, horizontal_angles: PointerToArray_float) -> None: ...
    def set_candela_values(self, candela_values: PointerToArray_float) -> None: ...
    def generate_dataset_texture_into(self, dest_tex: Texture, z: int) -> None: ...
    setVerticalAngles = set_vertical_angles
    setHorizontalAngles = set_horizontal_angles
    setCandelaValues = set_candela_values
    generateDatasetTextureInto = generate_dataset_texture_into

class RPLight(ReferenceCount):
    """@brief Base class for Lights
    @details This is the base class for all lights in the render pipeline. It
      stores common properties, and provides methods to modify these.
      It also defines some interface functions which subclasses have to implement.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    pos: LVecBase3f
    color: LVecBase3f
    energy: float
    casts_shadows: bool
    shadow_map_resolution: int
    ies_profile: int
    near_plane: float
    LT_empty: ClassVar[Literal[0]]
    LT_point_light: ClassVar[Literal[1]]
    LT_spot_light: ClassVar[Literal[2]]
    @property
    def light_type(self) -> _RPLight_LightType: ...
    def invalidate_shadows(self) -> None: ...
    @overload
    def set_pos(self, pos: _Vec3f) -> None: ...
    @overload
    def set_pos(self, x: float, y: float, z: float) -> None: ...
    def get_pos(self) -> LVecBase3f: ...
    @overload
    def set_color(self, color: _Vec3f) -> None: ...
    @overload
    def set_color(self, r: float, g: float, b: float) -> None: ...
    def get_color(self) -> LVecBase3f: ...
    def set_color_from_temperature(self, temperature: float) -> None: ...
    def set_energy(self, energy: float) -> None: ...
    def get_energy(self) -> float: ...
    def get_light_type(self) -> _RPLight_LightType: ...
    def set_casts_shadows(self, flag: bool = ...) -> None: ...
    def get_casts_shadows(self) -> bool: ...
    def set_shadow_map_resolution(self, resolution: int) -> None: ...
    def get_shadow_map_resolution(self) -> int: ...
    def set_ies_profile(self, profile: int) -> None: ...
    def get_ies_profile(self) -> int: ...
    def has_ies_profile(self) -> bool: ...
    def clear_ies_profile(self) -> None: ...
    def set_near_plane(self, near_plane: float) -> None: ...
    def get_near_plane(self) -> float: ...
    invalidateShadows = invalidate_shadows
    setPos = set_pos
    getPos = get_pos
    setColor = set_color
    getColor = get_color
    setColorFromTemperature = set_color_from_temperature
    setEnergy = set_energy
    getEnergy = get_energy
    getLightType = get_light_type
    setCastsShadows = set_casts_shadows
    getCastsShadows = get_casts_shadows
    setShadowMapResolution = set_shadow_map_resolution
    getShadowMapResolution = get_shadow_map_resolution
    setIesProfile = set_ies_profile
    getIesProfile = get_ies_profile
    hasIesProfile = has_ies_profile
    clearIesProfile = clear_ies_profile
    setNearPlane = set_near_plane
    getNearPlane = get_near_plane
    LTEmpty = LT_empty
    LTPointLight = LT_point_light
    LTSpotLight = LT_spot_light

class ShadowAtlas:
    """@brief Class which manages distributing shadow maps in an atlas.
    @details This class manages the shadow atlas. It handles finding and reserving
      space for new shadow maps.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def num_used_tiles(self) -> int: ...
    @property
    def coverage(self) -> float: ...
    @overload
    def __init__(self, __param0: ShadowAtlas) -> None: ...
    @overload
    def __init__(self, size: int, tile_size: int = ...) -> None: ...
    def get_num_used_tiles(self) -> int: ...
    def get_coverage(self) -> float: ...
    getNumUsedTiles = get_num_used_tiles
    getCoverage = get_coverage

class TagStateManager:
    """@brief This class handles all different tag states
    @details The TagStateManager stores a list of RenderStates assigned to different
      steps in the pipeline. For example, there are a list of shadow states, which
      are applied whenever objects are rendered from a shadow camera.
    
      The Manager also stores a list of all cameras used in the different stages,
      to keep track of the states used and to be able to attach new states.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, main_cam_node: NodePath) -> None: ...
    @overload
    def __init__(self, __param0: TagStateManager) -> None: ...
    def apply_state(self, state: str, np: NodePath, shader: Shader, name: str, sort: int) -> None: ...
    def cleanup_states(self) -> None: ...
    def register_camera(self, state: str, source: Camera) -> None: ...
    def unregister_camera(self, state: str, source: Camera) -> None: ...
    def get_mask(self, container_name: str) -> BitMask_uint32_t_32: ...
    applyState = apply_state
    cleanupStates = cleanup_states
    registerCamera = register_camera
    unregisterCamera = unregister_camera
    getMask = get_mask

class ShadowManager(ReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    atlas_size: int
    @property
    def num_update_slots_left(self) -> int: ...
    @property
    def atlas(self) -> ShadowAtlas: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: ShadowManager) -> None: ...
    def set_max_updates(self, max_updates: int) -> None: ...
    def set_scene(self, scene_parent: NodePath) -> None: ...
    def set_tag_state_manager(self, tag_mgr: TagStateManager) -> None: ...
    def set_atlas_graphics_output(self, graphics_output: GraphicsOutput) -> None: ...
    def set_atlas_size(self, atlas_size: int) -> None: ...
    def get_atlas_size(self) -> int: ...
    def get_num_update_slots_left(self) -> int: ...
    def get_atlas(self) -> ShadowAtlas: ...
    def init(self) -> None: ...
    def update(self) -> None: ...
    setMaxUpdates = set_max_updates
    setScene = set_scene
    setTagStateManager = set_tag_state_manager
    setAtlasGraphicsOutput = set_atlas_graphics_output
    setAtlasSize = set_atlas_size
    getAtlasSize = get_atlas_size
    getNumUpdateSlotsLeft = get_num_update_slots_left
    getAtlas = get_atlas

class InternalLightManager:
    """@brief Internal class used for handling lights and shadows.
    @details This is the internal class used by the pipeline to handle all
      lights and shadows. It stores references to the lights, manages handling
      the light and shadow slots, and also communicates with the GPU with the
      GPUCommandQueue to store light and shadow source data.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    shadow_manager: ShadowManager
    @property
    def max_light_index(self) -> int: ...
    @property
    def num_lights(self) -> int: ...
    @property
    def num_shadow_sources(self) -> int: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: InternalLightManager) -> None: ...
    def add_light(self, light: RPLight) -> None: ...
    def remove_light(self, light: RPLight) -> None: ...
    def update(self) -> None: ...
    def set_camera_pos(self, pos: _Vec3f) -> None: ...
    def set_shadow_update_distance(self, dist: float) -> None: ...
    def get_max_light_index(self) -> int: ...
    def get_num_lights(self) -> int: ...
    def get_num_shadow_sources(self) -> int: ...
    def set_shadow_manager(self, mgr: ShadowManager) -> None: ...
    def get_shadow_manager(self) -> ShadowManager: ...
    def set_command_list(self, cmd_list: GPUCommandList) -> None: ...
    addLight = add_light
    removeLight = remove_light
    setCameraPos = set_camera_pos
    setShadowUpdateDistance = set_shadow_update_distance
    getMaxLightIndex = get_max_light_index
    getNumLights = get_num_lights
    getNumShadowSources = get_num_shadow_sources
    setShadowManager = set_shadow_manager
    getShadowManager = get_shadow_manager
    setCommandList = set_command_list

class RPPointLight(RPLight):
    """@brief PointLight class
    @details This represents a point light, a light which has a position and
      radius. Checkout the RenderPipeline documentation for more information
      about this type of light.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    radius: float
    inner_radius: float
    def __init__(self) -> None: ...
    def set_radius(self, radius: float) -> None: ...
    def get_radius(self) -> float: ...
    def set_inner_radius(self, inner_radius: float) -> None: ...
    def get_inner_radius(self) -> float: ...
    setRadius = set_radius
    getRadius = get_radius
    setInnerRadius = set_inner_radius
    getInnerRadius = get_inner_radius

class PSSMCameraRig:
    """@brief Main class used for handling PSSM
    @details This is the main class for supporting PSSM, it is used by the PSSM
      plugin to compute the position of the splits.
    
      It supports handling a varying amount of cameras, and fitting those cameras
      into the main camera frustum, to render distant shadows. It also supports
      various optimizations for fitting the frustum, e.g. rotating the sources
      to get a better coverage.
    
      It also provides methods to get arrays of data about the used cameras
      view-projection matrices and their near and far plane, which is required for
      processing the data in the shadow sampling shader.
    
      In this class, there is often referred to "Splits" or also called "Cascades".
      These denote the different cameras which are used to split the frustum,
      and are a common term related to the PSSM algorithm.
    
      To understand the functionality of this class, a detailed knowledge of the
      PSSM algorithm is helpful.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: PSSMCameraRig) -> None: ...
    @overload
    def __init__(self, num_splits: int) -> None: ...
    def set_pssm_distance(self, distance: float) -> None: ...
    def set_sun_distance(self, distance: float) -> None: ...
    def set_use_fixed_film_size(self, flag: bool) -> None: ...
    def set_resolution(self, resolution: int) -> None: ...
    def set_use_stable_csm(self, flag: bool) -> None: ...
    def set_logarithmic_factor(self, factor: float) -> None: ...
    def set_border_bias(self, bias: float) -> None: ...
    def update(self, cam_node: NodePath, light_vector: _Vec3f) -> None: ...
    def reset_film_size_cache(self) -> None: ...
    def get_camera(self, index: int) -> NodePath: ...
    def reparent_to(self, parent: NodePath) -> None: ...
    def get_mvp_array(self) -> PointerToArray_UnalignedLMatrix4f: ...
    def get_nearfar_array(self) -> PointerToArray_LVecBase2f: ...
    setPssmDistance = set_pssm_distance
    setSunDistance = set_sun_distance
    setUseFixedFilmSize = set_use_fixed_film_size
    setResolution = set_resolution
    setUseStableCsm = set_use_stable_csm
    setLogarithmicFactor = set_logarithmic_factor
    setBorderBias = set_border_bias
    resetFilmSizeCache = reset_film_size_cache
    getCamera = get_camera
    reparentTo = reparent_to
    getMvpArray = get_mvp_array
    getNearfarArray = get_nearfar_array

class RPSpotLight(RPLight):
    """@brief SpotLight class
    @details This represents a spot light, a light which has a position, radius,
      direction and FoV. Checkout the RenderPipeline documentation for more
      information about this type of light.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    radius: float
    fov: float
    direction: LVecBase3f
    def __init__(self) -> None: ...
    def set_radius(self, radius: float) -> None: ...
    def get_radius(self) -> float: ...
    def set_fov(self, fov: float) -> None: ...
    def get_fov(self) -> float: ...
    @overload
    def set_direction(self, direction: _Vec3f) -> None: ...
    @overload
    def set_direction(self, dx: float, dy: float, dz: float) -> None: ...
    def get_direction(self) -> LVecBase3f: ...
    @overload
    def look_at(self, point: _Vec3f) -> None: ...
    @overload
    def look_at(self, x: float, y: float, z: float) -> None: ...
    setRadius = set_radius
    getRadius = get_radius
    setFov = set_fov
    getFov = get_fov
    setDirection = set_direction
    getDirection = get_direction
    lookAt = look_at
