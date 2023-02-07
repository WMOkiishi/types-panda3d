from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import IntVec3Like, IntVec4Like, Mat4Like, Vec3Like, Vec4Like
from panda3d.core._display import GraphicsOutput
from panda3d.core._dtoolutil import ostream
from panda3d.core._express import PTA_float, PTA_uchar, ReferenceCount
from panda3d.core._gobj import Shader, Texture
from panda3d.core._linmath import LMatrix3, LVecBase3
from panda3d.core._mathutil import PTA_LMatrix4, PTA_LVecBase2
from panda3d.core._pgraph import Camera, NodePath
from panda3d.core._putil import BitMask32

_GPUCommand_CommandType: TypeAlias = Literal[0, 1, 2, 3, 4]
_RPLight_LightType: TypeAlias = Literal[0, 1, 2]

class GPUCommand:
    """@brief Class for storing data to be transferred to the GPU.
    @details This class can be seen like a packet, to be transferred to the GPU.
      It has a command type, which tells the GPU what to do once it recieved this
      "packet". It stores a limited amount of floating point components.
    """

    CMD_invalid: Final = 0
    CMDInvalid: Final = 0
    CMD_store_light: Final = 1
    CMDStoreLight: Final = 1
    CMD_remove_light: Final = 2
    CMDRemoveLight: Final = 2
    CMD_store_source: Final = 3
    CMDStoreSource: Final = 3
    CMD_remove_sources: Final = 4
    CMDRemoveSources: Final = 4
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: GPUCommand) -> None:
        """@brief Constructs a new GPUCommand with the given command type.
        @details This will construct a new GPUCommand of the given command type.
          The command type should be of GPUCommand::CommandType, and determines
          what data the GPUCommand contains, and how it will be handled.

        @param command_type The type of the GPUCommand
        """
    @overload
    def __init__(self, command_type: _GPUCommand_CommandType) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def push_int(self, v: int) -> None:
        """@brief Appends an integer to the GPUCommand.
        @details This adds an integer to the back of the GPUCommand. Depending on the
          setting in convert_int_to_float, this will either just convert the int to a
          float by casting it, or just do a bitwise copy.

        @param v The integer to append.
        """
    def push_float(self, v: float) -> None:
        """@brief Appends a float to the GPUCommand.
        @details This adds an integer to the back of the GPUCommand. Its used by all
          other push_xxx methods, and simply stores the value, then increments the write
          pointer. When the amount of floats exceeds the capacity of the GPUCommand,
          an error will be printed, and the method returns without doing anything else.

        @param v The float to append.
        """
    def push_vec3(self, v: IntVec3Like | Vec3Like) -> None:
        """`(self, v: LVecBase3)`:
        @brief Appends a 3-component floating point vector to the GPUCommand.
        @details This appends a 3-component floating point vector to the command.
          It basically just calls push_float() for every component, in the order
          x, y, z, which causes the vector to occupy the space of 3 floats.

        @param v Int-Vector to append.

        `(self, v: LVecBase3i)`:
        @brief Appends a 3-component integer vector to the GPUCommand.
        @details This appends a 3-component integer vector to the command.
          It basically just calls push_int() for every component, in the order
          x, y, z, which causes the vector to occupy the space of 3 floats.

        @param v Int-Vector to append.
        """
    def push_vec4(self, v: IntVec4Like | Vec4Like) -> None:
        """`(self, v: LVecBase4)`:
        @brief Appends a 4-component floating point vector to the GPUCommand.
        @details This appends a 4-component floating point vector to the command.
          It basically just calls push_float() for every component, in the order
          x, y, z, which causes the vector to occupy the space of 3 floats.

        @param v Int-Vector to append.

        `(self, v: LVecBase4i)`:
        @brief Appends a 4-component integer vector to the GPUCommand.
        @details This appends a 4-component integer vector to the command.
          It basically just calls push_int() for every component, in the order
          x, y, z, w, which causes the vector to occupy the space of 4 floats.

        @param v Int-Vector to append.
        """
    def push_mat3(self, v: LMatrix3) -> None:
        """@brief Appends a floating point 3x3 matrix to the GPUCommand.
        @details This appends a floating point 3x3 matrix to the GPUCommand, by
          pushing all components in row-order to the command. This occupies a space of
          9 floats.

        @param v Matrix to append
        """
    def push_mat4(self, v: Mat4Like) -> None:
        """@brief Appends a floating point 4x4 matrix to the GPUCommand.
        @details This appends a floating point 4x4 matrix to the GPUCommand, by
          pushing all components in row-order to the command. This occupies a space of
          16 floats.

        @param v Matrix to append
        """
    @staticmethod
    def get_uses_integer_packing() -> bool:
        """@brief Returns whether integers are packed as floats.
        @details This returns how integer are packed into the data stream. If the
          returned value is true, then integers are packed using their binary
          representation converted to floating point format. If the returned value
          is false, then integers are packed by simply casting them to float,
          e.g. val = (float)i;
        @return The integer representation flag
        """
    def write_to(self, dest: PTA_uchar, command_index: int) -> None:
        """@brief Writes the GPU command to a given target.
        @details This method writes all the data of the GPU command to a given target.
          The target should be a pointer to memory being big enough to hold the
          data. Presumably #dest will be a handle to texture memory.
          The command_index controls the offset where the data will be written
          to.

        @param dest Handle to the memory to write the command to
        @param command_index Offset to write the command to. The command will write
          its data to command_index * GPU_COMMAND_ENTRIES. When writing
          the GPUCommand in a GPUCommandList, the command_index will
          most likely be the index of the command in the list.
        """
    def write(self, out: ostream) -> None:
        """@brief Prints out the GPUCommand to the console
        @details This method prints the type, size, and data of the GPUCommand to the
          console. This helps for debugging the contents of the GPUCommand. Keep
          in mind that integers might be shown in their binary float representation,
          depending on the setting in the GPUCommand::convert_int_to_float method.
        """
    pushInt = push_int
    pushFloat = push_float
    pushVec3 = push_vec3
    pushVec4 = push_vec4
    pushMat3 = push_mat3
    pushMat4 = push_mat4
    getUsesIntegerPacking = get_uses_integer_packing
    writeTo = write_to

class GPUCommandList:
    """@brief Class to store a list of commands.
    @details This is a class to store a list of GPUCommands. It provides
      functionality to only provide the a given amount of commands at one time.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def num_commands(self) -> int: ...
    def __init__(self, __param0: GPUCommandList = ...) -> None:
        """@brief Constructs a new GPUCommandList
        @details This constructs a new GPUCommandList. By default, there are no commands
          in the list.
        """
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def add_command(self, cmd: GPUCommand | _GPUCommand_CommandType) -> None:
        """@brief Pushes a GPUCommand to the command list.
        @details This adds a new GPUCommand to the list of commands to be processed.

        @param cmd The command to add
        """
    def get_num_commands(self) -> int:
        """@brief Returns the number of commands in this list.
        @details This returns the amount of commands which are currently stored in this
          list, and are waiting to get processed.
        @return Amount of commands
        """
    def write_commands_to(self, dest: PTA_uchar, limit: int = ...) -> int:
        """@brief Writes the first n-commands to a destination.
        @details This takes the first #limit commands, and writes them to the
          destination using GPUCommand::write_to. See GPUCommand::write_to for
          further information about #dest. The limit controls after how much
          commands the processing will be stopped. All commands which got processed
          will get removed from the list.

        @param dest Destination to write to, see GPUCommand::write_to
        @param limit Maximum amount of commands to process

        @return Amount of commands processed, between 0 and #limit.
        """
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
    def __init__(self, __param0: IESDataset = ...) -> None:
        """@brief Constructs a new empty dataset.
        @details This constructs a new IESDataset with no data set.
        """
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_vertical_angles(self, vertical_angles: PTA_float) -> None:
        """@brief Sets the vertical angles of the dataset.
        @details This sets the list of vertical angles of the dataset.

        @param vertical_angles Vector of all vertical angles.
        """
    def set_horizontal_angles(self, horizontal_angles: PTA_float) -> None:
        """@brief Sets the horizontal angles of the dataset.
        @details This sets the list of horizontal angles of the dataset.

        @param horizontal_angles Vector of all horizontal angles.
        """
    def set_candela_values(self, candela_values: PTA_float) -> None:
        """@brief Sets the candela values.
        @details This sets the candela values of the dataset. They should be an
          interleaved 2D array with the dimensions vertical_angles x horizontal_angles.
          They also should be normalized by dividing by the maximum entry.
        @param candela_values Interleaved 2D-vector of candela values.
        """
    def generate_dataset_texture_into(self, dest_tex: Texture, z: int) -> None:
        """@brief Generates the IES LUT
        @details This generates the LUT into a given dataset texture. The x-axis
          referes to the vertical_angle, whereas the y-axis refers to the
          horizontal angle.

        @param dest_tex Texture to write the LUT into
        @param z Layer to write the LUT into, in case the texture is a 3D Texture or
          2D Texture Array.
        """
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

    LT_empty: Final = 0
    LTEmpty: Final = 0
    LT_point_light: Final = 1
    LTPointLight: Final = 1
    LT_spot_light: Final = 2
    LTSpotLight: Final = 2
    pos: LVecBase3
    color: LVecBase3
    energy: float
    casts_shadows: bool
    shadow_map_resolution: int
    ies_profile: int
    near_plane: float
    @property
    def light_type(self) -> _RPLight_LightType: ...
    def invalidate_shadows(self) -> None:
        """@brief Invalidates the shadows
        @details This invalidates all shadows of the light, causing them to get
          regenerated. This might be the case  when the lights position or similar
          changed. This will cause all shadow sources to be updated, emitting a
          shadow update. Be careful when calling this method if you don't want all
          sources to get updated. If you only have to invalidate a single shadow source,
          use `get_shadow_source(n)->set_needs_update(true)`.
        """
    @overload
    def set_pos(self, pos: Vec3Like) -> None:
        """`(self, pos: LVecBase3)`:
        @brief Sets the position of the light
        @details This sets the position of the light in world space. It will cause
          the light to get invalidated, and resubmitted to the GPU.

        @param pos Position in world space

        `(self, x: float, y: float, z: float)`:
        @brief Sets the position of the light
        @details @copydetails RPLight::set_pos(const LVecBase3 &pos)

        @param x X-component of the position
        @param y Y-component of the position
        @param z Z-component of the position
        """
    @overload
    def set_pos(self, x: float, y: float, z: float) -> None: ...
    def get_pos(self) -> LVecBase3:
        """@brief Returns the position of the light
        @details This returns the position of the light previously set with
          RPLight::set_pos(). The returned position is in world space.
        @return Light-position
        """
    @overload
    def set_color(self, color: Vec3Like) -> None:
        """`(self, color: LVecBase3)`:
        @brief Sets the lights color
        @details This sets the lights color. The color should not include the brightness
          of the light, you should control that with the energy. The color specifies
          the lights "tint" and will get multiplied with its specular and diffuse
          contribution.

          The color will be normalized by dividing by the colors luminance. Setting
          higher values than 1.0 will have no effect.

        @param color Light color

        `(self, r: float, g: float, b: float)`:
        @brief Sets the lights color
        @details @copydetails RPLight::set_color(const LVecBase3 &color)

        @param r Red-component of the color
        @param g Green-component of the color
        @param b Blue-component of the color
        """
    @overload
    def set_color(self, r: float, g: float, b: float) -> None: ...
    def get_color(self) -> LVecBase3:
        """@brief Returns the lights color
        @details This returns the light color, previously set with RPLight::set_color.
          This does not include the energy of the light. It might differ from what
          was set with set_color, because the color is normalized by dividing it
          by its luminance.
        @return Light-color
        """
    def set_color_from_temperature(self, temperature: float) -> None:
        """@brief Sets the lights color from a given color temperature
        @details This sets the lights color, given a temperature. This is more
          physically based than setting a user defined color. The color will be
          computed from the given temperature.

        @param temperature Light temperature
        """
    def set_energy(self, energy: float) -> None:
        """@brief Sets the energy of the light
        @details This sets the energy of the light, which can be seen as the brightness
          of the light. It will get multiplied with the normalized color.

        @param energy energy of the light
        """
    def get_energy(self) -> float:
        """@brief Returns the energy of the light
        @details This returns the energy of the light, previously set with
          RPLight::set_energy.

        @return energy of the light
        """
    def get_light_type(self) -> _RPLight_LightType:
        """@brief Returns the type of the light
        @details This returns the internal type of the light, which was specified
          in the lights constructor. This can be used to distinguish between light
          types.
        @return Type of the light
        """
    def set_casts_shadows(self, flag: bool = ...) -> None:
        """@brief Controls whether the light casts shadows
        @details This sets whether the light casts shadows. You can not change this
          while the light is attached. When flag is set to true, the light will be
          setup to cast shadows, spawning shadow sources based on the lights type.
          If the flag is set to false, the light will be inddicated to cast no shadows.

        @param flag Whether the light casts shadows
        """
    def get_casts_shadows(self) -> bool:
        """@brief Returns whether the light casts shadows
        @details This returns whether the light casts shadows, the returned value
          is the one previously set with RPLight::set_casts_shadows.

        @return true if the light casts shadows, false otherwise
        """
    def set_shadow_map_resolution(self, resolution: int) -> None:
        """@brief Sets the light's shadow map resolution
        @details This sets the light's shadow map resolution. This has no effect
          when the light is not told to cast shadows (Use RPLight::set_casts_shadows).

          When calling this on a light with multiple shadow sources (e.g.
          RPPointLight), this controls the resolution of each source. If the light
          has 6 shadow sources, and you use a resolution of 512x512, the light's
          shadow map will occupy a space of 6 * 512x512 maps in the shadow atlas.

        @param resolution Resolution of the shadow map in pixels
        """
    def get_shadow_map_resolution(self) -> int:
        """@brief Returns the shadow map resolution
        @details This returns the shadow map resolution of each source of the light.
          If the light is not setup to cast shadows, this value is meaningless.
          The returned value is the one previously set with RPLight::set_shadow_map_resolution.

        @return Shadow map resolution in pixels
        """
    def set_ies_profile(self, profile: int) -> None:
        """@brief Sets the IES profile
        @details This sets the ies profile of the light. The parameter should be a
          handle previously returned by RenderPipeline.load_ies_profile. Using a
          value of -1 indicates no ies profile.

          Notice that for IES profiles which cover a whole range, you should use an
          RPPointLight, whereas for ies profiles which only cover the lower
          hemisphere you should use an RPSpotLight for the best performance.

        @param profile IES Profile handle
        """
    def get_ies_profile(self) -> int:
        """@brief Returns the light's IES profile
        @details This returns the IES profile of a light, previously set with
          RPLight::set_ies_profile. In case no ies profile was set, returns -1.

        @return IES Profile handle
        """
    def has_ies_profile(self) -> bool:
        """@brief Returns whether the light has an IES profile assigned
        @details This returns whether the light has an IES profile assigned,
          previously done with RPLight::set_ies_profile.

        @return true if the light has an IES profile assigned, false otherwise
        """
    def clear_ies_profile(self) -> None:
        """@brief Clears the IES profile
        @details This clears the IES profile of the light, telling it to no longer
          use an IES profile, and instead use the default attenuation.
        """
    def set_near_plane(self, near_plane: float) -> None:
        """@brief Sets the near plane of the light
        @details This sets the near plane of all shadow sources of the light. It has
          no effects if the light does not cast shadows. This prevents artifacts from
          objects near to the light. It behaves like Lens::set_near().

          It can also help increasing shadow map precision, low near planes will
          cause the precision to suffer. Try setting the near plane as big as possible.

          If a negative or zero near plane is passed, an assertion is thrown.

        @param near_plane Near-plane
        """
    def get_near_plane(self) -> float:
        """@brief Returns the near plane of the light
        @details This returns the light's near plane, previously set with
          RPLight::set_near_plane. If the light does not cast shadows, this value
          is meaningless.

        @return Near-plane
        """
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
    def __init__(self, __param0: ShadowAtlas) -> None:
        """@brief Constructs a new shadow atlas.
        @details This constructs a new shadow atlas with the given size and tile size.

          The size determines the total size of the atlas in pixels. It should be a
          power-of-two to favour the GPU.

          The tile_size determines the smallest unit of tiles the atlas can store.
          If, for example, a tile_size of 32 is used, then every entry stored must
          have a resolution of 32 or greater, and the resolution must be a multiple
          of 32. This is to optimize the search in the atlas, so the atlas does not
          have to check every pixel, and instead can just check whole tiles.

          If you want to disable the use of tiles, set the tile_size to 1, which
          will make the shadow atlas use pixels instead of tiles.

        @param size Atlas-size in pixels
        @param tile_size tile-size in pixels, or 1 to use no tiles.
        """
    @overload
    def __init__(self, size: int, tile_size: int = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_num_used_tiles(self) -> int:
        """@brief Returns the amount of used tiles
        @details Returns the amount of used tiles in the atlas
        @return Amount of used tiles
        """
    def get_coverage(self) -> float:
        """@brief Returns the amount of used tiles in percentage
        @details This returns in percentage from 0 to 1 how much space of the atlas
          is used right now. A value of 1 means the atlas is completely full, whereas
          a value of 0 means the atlas is completely free.
        @return Atlas usage in percentage
        """
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
    def __init__(self, main_cam_node: NodePath) -> None:
        """@brief Constructs a new TagStateManager
        @details This constructs a new TagStateManager. The #main_cam_node should
          refer to the main scene camera, and will most likely be base.cam.
          It is necessary to pass the camera because the C++ code does not have
          access to the showbase.

        @param main_cam_node The main scene camera
        """
    @overload
    def __init__(self, __param0: TagStateManager) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def apply_state(self, state: str, np: NodePath, shader: Shader, name: str, sort: int) -> None:
        """@brief Applies a given state for a pass to a NodePath
        @details This applies a shader to the given NodePath which is used when the
          NodePath is rendered by any registered camera for that pass.
          It also disables color write depending on the pass.

        @param np The nodepath to apply the shader to
        @param shader A handle to the shader to apply
        @param name Name of the state, should be a unique identifier
        @param sort Determines the sort with which the shader will be applied.
        """
    def cleanup_states(self) -> None:
        """@brief Cleans up all registered states.
        @details This cleans up all states which were registered to the TagStateManager.
          It also calls Camera::clear_tag_states() on the main_cam_node and all attached
          cameras.
        """
    def register_camera(self, state: str, source: Camera) -> None:
        """@brief Registers a new camera which renders a certain pass
        @details This registers a new camera which will be used to render the given
          pass. The TagStateManager will keep track of the camera and
          applies all registered states onto the camera with Camera::set_tag_state.
          It also applies the appropriate camera mask to the camera,
          and sets an initial state to disable color write depending on the pass.

        @param source Camera which will be used to render shadows
        """
    def unregister_camera(self, state: str, source: Camera) -> None:
        """@brief Unregisters a camera from the list of shadow cameras
        @details This unregisters a camera from the list of shadows cameras. It also
          resets all tag states of the camera, and also its initial state.

        @param source Camera to unregister
        """
    def get_mask(self, container_name: str) -> BitMask32:
        """@brief Returns the render mask for the given state
        @details This returns the mask of a given render pass, which can be used
          to either show or hide objects from this pass.

        @param container_name Name of the render-pass
        @return Bit mask of the render pass
        """
    applyState = apply_state
    cleanupStates = cleanup_states
    registerCamera = register_camera
    unregisterCamera = unregister_camera
    getMask = get_mask

class ShadowManager(ReferenceCount):
    atlas_size: int
    @property
    def num_update_slots_left(self) -> int: ...
    @property
    def atlas(self) -> ShadowAtlas: ...
    def __init__(self, __param0: ShadowManager = ...) -> None:
        """@brief Constructs a new shadow atlas
        @details This constructs a new shadow atlas. There are a set of properties
          which should be set before calling ShadowManager::init, see the set-Methods.
          After all properties are set, ShadowManager::init should get called.
          ShadowManager::update should get called on a per frame basis.
        """
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_max_updates(self, max_updates: int) -> None:
        """@brief Sets the maximum amount of updates per frame.
        @details This controls the maximum amount of updated ShadowSources per frame.
          The ShadowManager will take the first <max_updates> ShadowSources, and
          generate shadow maps for them every frame. If there are more ShadowSources
          waiting to get updated than available updates, the sources are sorted by
          priority, and the update of the less important sources is delayed to the
          next frame.

          If the update count is set too low, and there are a lot of ShadowSources
          waiting to get updated, artifacts will occur, and there might be ShadowSources
          which never get updated, due to low priority.

          If an update count of 0 is passed, no updates will happen. This also means
          that there are no shadows. This is not recommended.

          If an update count < 0 is passed, undefined behaviour occurs.

          This method has to get called before ShadowManager::init, otherwise an
          assertion will get triggered.

        @param max_updates Maximum amoumt of updates
        """
    def set_scene(self, scene_parent: NodePath) -> None:
        """@brief Sets the target scene
        @details This sets the target scene for rendering shadows. All shadow cameras
          will be parented to this scene to render shadows.

          Usually the scene will be ShowBase.render. If the scene is an empty or
          invalid NodePath, an assertion will be triggered.

          This method has to get called before calling ShadowManager::init, or an
          assertion will get triggered.

        @param scene_parent The target scene
        """
    def set_tag_state_manager(self, tag_mgr: NodePath | TagStateManager) -> None:
        """@brief Sets the handle to the TagStageManager.
        @details This sets the handle to the TagStateManager used by the pipeline.
          Usually this is RenderPipeline.get_tag_mgr().

          This has to get called before ShadowManager::init, otherwise an assertion
          will get triggered.

        @param tag_mgr [description]
        """
    def set_atlas_graphics_output(self, graphics_output: GraphicsOutput) -> None:
        """@brief Sets the handle to the Shadow targets output
        @details This sets the handle to the GraphicsOutput of the shadow atlas.
          Usually this is RenderTarget.get_internal_buffer(), whereas the RenderTarget
          is the target of the ShadowStage.

          This is used for creating display regions and attaching cameras to them,
          for performing shadow updates.

          This has to get called before ShadowManager::init, otherwise an assertion
          will be triggered.

        @param graphics_output [description]
        """
    def set_atlas_size(self, atlas_size: int) -> None:
        """@brief Sets the shadow atlas size
        @details This sets the desired shadow atlas size. It should be big enough
          to store all important shadow sources, with some buffer, because the shadow
          maps usually won't be fitted perfectly, so gaps can occur.

          This has to get called before calling ShadowManager::init. When calling this
          method after initialization, an assertion will get triggered.

        @param atlas_size Size of the shadow atlas in pixels
        """
    def get_atlas_size(self) -> int:
        """@brief Returns the shadow atlas size.
        @details This returns the shadow atlas size previously set with
          ShadowManager::set_atlas_size.
        @return Shadow atlas size in pixels
        """
    def get_num_update_slots_left(self) -> int:
        """@brief Returns how many update slots are left.
        @details This returns how many update slots are left. You can assume the
          next n calls to add_update will succeed, whereas n is the value returned
          by this function.
        @return Number of update slots left.
        """
    def get_atlas(self) -> ShadowAtlas:
        """@brief Returns a handle to the shadow atlas.
        @details This returns a handle to the internal shadow atlas instance. This
          is only valid after calling ShadowManager::init. Calling this earlier will
          trigger an assertion and undefined behaviour.
        @return The internal ShadowAtlas instance
        """
    def init(self) -> None:
        """@brief Initializes the ShadowManager.
        @details This initializes the ShadowManager. All properties should have
          been set before calling this, otherwise assertions will get triggered.

          This setups everything required for rendering shadows, including the
          shadow atlas and the various shadow cameras. After calling this method,
          no properties can be changed anymore.
        """
    def update(self) -> None:
        """@brief Updates the ShadowManager
        @details This updates the ShadowManager, processing all shadow sources which
          need to get updated.

          This first collects all sources which require an update, sorts them by priority,
          and then processes the first <max_updates> ShadowSources.

          This may not get called before ShadowManager::init, or an assertion will be
          thrown.
        """
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
    def __init__(self, __param0: InternalLightManager = ...) -> None:
        """@brief Constructs the light manager
        @details This constructs the light manager, initializing the light and shadow
          storage. You should set a command list and shadow manager before calling
          InternalLightManager::update. s
        """
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def add_light(self, light: RPLight) -> None:
        """@brief Adds a new light.
        @details This adds a new light to the list of lights. This will throw an
          error and return if the light is already attached. You may only call
          this after the ShadowManager was already set.

          While the light is attached, the light manager keeps a reference to it, so
          the light does not get destructed.

          This also setups the shadows on the light, in case shadows are enabled.
          While a light is attached, you can not change whether it casts shadows or not.
          To do so, detach the light, change the setting, and re-add the light.

          In case no free light slot is available, an error will be printed and no
          action will be performed.

          If no shadow manager was set, an assertion will be triggered.

        @param light The light to add.
        """
    def remove_light(self, light: RPLight) -> None:
        """@brief Removes a light
        @details This detaches a light. This prevents it from being rendered, and also
          cleans up all resources used by that light. If no reference is kept on the
          python side, the light will also get destructed.

          If the light was not previously attached with InternalLightManager::add_light,
          an error will be triggered and nothing happens.

          In case the light was set to cast shadows, all shadow sources are cleaned
          up, and their regions in the shadow atlas are freed.

          All resources used by the light in the light and shadow storage are also
          cleaned up, by emitting cleanup GPUCommands.

          If no shadow manager was set, an assertion will be triggered.

        @param light [description]
        """
    def update(self) -> None:
        """@brief Main update method
        @details This is the main update method of the InternalLightManager. It
          processes all lights and shadow sources, updates them, and notifies the
          GPU about it. This should be called on a per-frame basis.

          If the InternalLightManager was not initialized yet, an assertion is thrown.
        """
    def set_camera_pos(self, pos: Vec3Like) -> None:
        """@brief Sets the camera position
        @details This sets the camera position, which will be used to determine which
          shadow sources have to get updated

        @param mat View projection mat
        """
    def set_shadow_update_distance(self, dist: float) -> None:
        """@brief Sets the maximum shadow update distance
        @details This controls the maximum distance until which shadows are updated.
          If a shadow source is past that distance, it is ignored and no longer recieves
          updates until it is in range again

        @param dist Distance in world space units
        """
    def get_max_light_index(self) -> int:
        """@brief Returns the maximum light index
        @details This returns the maximum light index (also called slot). Any lights
          after that slot are guaranteed to be zero-lights. This is useful when
          iterating over the list of lights, because iteration can be stopped when
          the maximum light index is reached.

          The maximum light index points to the last slot which is used. If no lights
          are attached, -1 is returned. If one light is attached at slot 0, the index
          is 0, if two are attached at the slots 0 and 1, the index is 1, and so on.

          If, for example, two lights are attached at the slots 2 and 5, then the
          index will be 5. Keep in mind that the max-index is not an indicator for
          how many lights are attached. Also, zero lights still may occur when iterating
          over the light lists

        @return Maximum light index
        """
    def get_num_lights(self) -> int:
        """@brief Returns the amount of stored lights.
        @details This returns the amount of stored lights. This behaves unlike
          InternalLightManager::get_max_light_index, and instead returns the true
          amount of lights, which is completely unrelated to the amount of used slots.

        @return Amount of stored lights
        """
    def get_num_shadow_sources(self) -> int:
        """@brief Returns the amount of shadow sources.
        @details This returns the total amount of stored shadow sources. This does
          not denote the amount of updated sources, but instead takes into account
          all sources, even those out of frustum.
        @return Amount of shadow sources.
        """
    def set_shadow_manager(self, mgr: ShadowManager) -> None:
        """@brief Sets the handle to the shadow manager
        @details This sets the handle to the global shadow manager. It is usually
          constructed on the python side, so we need to get a handle to it.

          The manager should be a handle to a ShadowManager instance, and will be
          stored somewhere on the python side most likely. The light manager does not
          keep a reference to it, so the python side should make sure to keep one.

          Be sure to call this before the InternalLightManager::update() method is
          called, otherwise an assertion will get triggered.

        @param mgr The ShadowManager instance
        """
    def get_shadow_manager(self) -> ShadowManager:
        """@brief Returns the internal used ShadowManager
        @details This returns a handle to the internally used shadow manager
        @return Shadow manager
        """
    def set_command_list(self, cmd_list: GPUCommandList) -> None:
        """@brief Sets a handle to the command list
        @details This sets a handle to the global GPUCommandList. This is required to
          emit GPUCommands, which are used for attaching and detaching lights, as well
          as shadow source updates.

          The cmd_list should be a handle to a GPUCommandList handle, and will be
          stored somewhere on the python side most likely. The light manager does not
          keep a reference to it, so the python side should make sure to keep one.

          Be sure to call this before the InternalLightManager::update() method is
          called, otherwise an assertion will get triggered.

        @param cmd_list The GPUCommandList instance
        """
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

    radius: float
    inner_radius: float
    def __init__(self) -> None:
        """@brief Constructs a new point light
        @details This contructs a new point light with default settings. By default
          the light is set to be an infinitely small point light source. You can
          change this with RPPointLight::set_inner_radius.
        """
    def set_radius(self, radius: float) -> None:
        """@brief Sets the radius of the light
        @details This sets the radius of the light. It controls the lights
          influence. After a distance greater than this radius, the light influence
          is zero.

        @param radius Light radius in world space
        """
    def get_radius(self) -> float:
        """@brief Returns the lights radius
        @details This returns the lights radius previously set with
          RPPointLight::set_radius
        @return Light radius in world space
        """
    def set_inner_radius(self, inner_radius: float) -> None:
        """@brief Sets the inner radius of the light
        @details This sets the inner radius of the light. Anything greater than
          zero causes the light to get an area light. This has influence on the
          specular highlights of the light aswell as the shadows.

          The inner radius controls the size of the lights sphere size in world
          space units. A radius of 0 means the light has no inner radius, and the
          light will be have like an infinite small point light source.
          A radius greater than zero will cause the light to behave like it would be
          an emissive sphere with the given inner radius emitting light. This is
          more physically correct.

        @param inner_radius Inner-radius in world space
        """
    def get_inner_radius(self) -> float:
        """@brief Returns the inner radius of the light
        @details This returns the inner radius of the light, previously set with
          RPPointLight::get_inner_radius.
        @return [description]
        """
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
    def __init__(self, __param0: PSSMCameraRig) -> None:
        """@brief Constructs a new PSSM camera rig
        @details This constructs a new camera rig, with a given amount of splits.
          The splits can not be changed later on. Splits are also called Cascades.

          An assertion will be triggered if the splits are below zero.

        @param num_splits Amount of PSSM splits
        """
    @overload
    def __init__(self, num_splits: int) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_pssm_distance(self, distance: float) -> None:
        """@brief Sets the maximum pssm distance.
        @details This sets the maximum distance in world space until which shadows
          are rendered. After this distance, no shadows will be rendered.

          If the distance is below zero, an assertion is triggered.

        @param distance Maximum distance in world space
        """
    def set_sun_distance(self, distance: float) -> None:
        """@brief Sets the suns distance
        @details This sets the distance the cameras will have from the cameras frustum.
          This prevents far objects from having no shadows, which can occur when these
          objects are between the cameras frustum and the sun, but not inside of the
          cameras frustum. Setting the sun distance high enough will move the cameras
          away from the camera frustum, being able to cover those distant objects too.

          If the sun distance is set too high, artifacts will occur due to the reduced
          range of depth. If a value below zero is passed, an assertion will get
          triggered.

        @param distance The sun distance
        """
    def set_use_fixed_film_size(self, flag: bool) -> None:
        """@brief Sets whether to use a fixed film size
        @details This controls if a fixed film size should be used. This will cause
          the camera rig to cache the current film size, and only change it in case
          it gets too small. This provides less flickering when moving, because the
          film size will stay roughly constant. However, to prevent the cached film
          size getting too big, one should call PSSMCameraRig::reset_film_size
          once in a while, otherwise there might be a lot of wasted space.

        @param flag Whether to use a fixed film size
        """
    def set_resolution(self, resolution: int) -> None:
        """@brief Sets the resolution of each split
        @details This sets the resolution of each split. Currently it is equal for
          each split. This is required when using PSSMCameraRig::set_use_stable_csm,
          to compute how bix a texel is.

          It has to match the y-resolution of the pssm shadow map. If an invalid
          resolution is triggered, an assertion is thrown.

        @param resolution The resolution of each split.
        """
    def set_use_stable_csm(self, flag: bool) -> None:
        """@brief Sets whether to use stable CSM snapping.
        @details This option controls if stable CSM snapping should be used. When the
          option is enabled, all splits will snap to their texels, so that when moving,
          no flickering will occur. However, this only works when the splits do not
          change their film size, rotation and angle.

        @param flag Whether to use stable CSM snapping
        """
    def set_logarithmic_factor(self, factor: float) -> None:
        """@brief Sets the logarithmic factor
        @details This sets the logarithmic factor, which is the core of the algorithm.
          PSSM splits the camera frustum based on a linear and a logarithmic factor.
          While a linear factor provides a good distribution, it often is not applicable
          for wider distances. A logarithmic distribution provides a better distribution
          at distance, but suffers from splitting in the near areas.

          The logarithmic factor mixes the logarithmic and linear split distribution,
          to get the best of both. A greater factor will make the distribution more
          logarithmic, while a smaller factor will make it more linear.

          If the factor is below zero, an ssertion is triggered.

        @param factor The logarithmic factor
        """
    def set_border_bias(self, bias: float) -> None:
        """@brief Sets the border bias for each split
        @details This sets the border bias for every split. This increases each
          splits frustum by multiplying it by (1 + bias), and helps reducing artifacts
          at the borders of the splits. Artifacts can occur when the bias is too low,
          because then the filtering will go over the bounds of the split, producing
          invalid results.

          If the bias is below zero, an assertion is thrown.

        @param bias Border bias
        """
    def update(self, cam_node: NodePath, light_vector: Vec3Like) -> None:
        """@brief Updates the PSSM camera rig
        @details This updates the rig with an updated camera position, and a given
          light vector. This should be called on a per-frame basis. It will reposition
          all camera sources to fit the frustum based on the pssm distribution.

          The light vector should be the vector from the light source, not the
          vector to the light source.

        @param cam_node Target camera node
        @param light_vector The vector from the light to any point
        """
    def reset_film_size_cache(self) -> None:
        """@brief Resets the film size cache
        @details In case PSSMCameraRig::set_use_fixed_film_size is used, this resets
          the film size cache. This might lead to a small "jump" in the shadows,
          because the film size changes, however it leads to a better shadow distribution.

          This is the case because when using a fixed film size, the cache will get
          bigger and bigger, whenever the camera moves to a grazing angle. However,
          when moving back to a normal angle, the film size cache still stores this
          big angle, and thus the splits will have a much bigger film size than actualy
          required. To prevent this, call this method once in a while, so an optimal
          distribution is ensured.
        """
    def get_camera(self, index: int) -> NodePath:
        """@brief Returns the n-th camera
        @details This returns the n-th camera of the camera rig, which can be used
          for various stuff like showing its frustum, passing it as a shader input,
          and so on.

          The first camera is the camera which is the camera of the first split,
          which is the split closest to the camera. All cameras follow in descending
          order until to the last camera, which is the split furthest away from the
          camera.

          If an invalid index is passed, an assertion is thrown.

        @param index Index of the camera.
        @return [description]
        """
    def reparent_to(self, parent: NodePath) -> None:
        """@brief Reparents the camera rig
        @details This reparents all cameras to the given parent. Usually the parent
          will be ShowBase.render. The parent should be the same node where the
          main camera is located in, too.

          If an empty parrent is passed, an assertion will get triggered.

        @param parent Parent node path
        """
    def get_mvp_array(self) -> PTA_LMatrix4:
        """@brief Returns a handle to the MVP array
        @details This returns a handle to the array of view-projection matrices
          of the different splits. This can be used for computing shadows. The array
          is a PTALMatrix4 and thus can be directly bound to a shader.

        @return view-projection matrix array
        """
    def get_nearfar_array(self) -> PTA_LVecBase2:
        """@brief Returns a handle to the near and far planes array
        @details This returns a handle to the near and far plane array. Each split
          has an entry in the array, whereas the x component of the vecto denotes the
          near plane, and the y component denotes the far plane of the split.

          This is required because the near and far planes of the splits change
          constantly. To access them in a shader, the shader needs access to the
          array.

        @return Array of near and far planes
        """
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

    radius: float
    fov: float
    direction: LVecBase3
    def __init__(self) -> None:
        """@brief Creates a new spot light
        @details This creates a new spot light with default properties set. You should
          set at least a direction, fov, radius and position to make the light useful.
        """
    def set_radius(self, radius: float) -> None: ...
    def get_radius(self) -> float: ...
    def set_fov(self, fov: float) -> None: ...
    def get_fov(self) -> float: ...
    @overload
    def set_direction(self, direction: Vec3Like) -> None: ...
    @overload
    def set_direction(self, dx: float, dy: float, dz: float) -> None: ...
    def get_direction(self) -> LVecBase3: ...
    @overload
    def look_at(self, point: Vec3Like) -> None: ...
    @overload
    def look_at(self, x: float, y: float, z: float) -> None: ...
    setRadius = set_radius
    getRadius = get_radius
    setFov = set_fov
    getFov = get_fov
    setDirection = set_direction
    getDirection = get_direction
    lookAt = look_at
