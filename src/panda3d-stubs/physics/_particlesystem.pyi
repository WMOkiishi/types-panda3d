from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import Vec2Like, Vec3Like, Vec4Like
from panda3d.core._dtoolbase import TypeHandle
from panda3d.core._dtoolutil import ostream
from panda3d.core._express import ReferenceCount, TypedReferenceCount
from panda3d.core._gobj import Texture
from panda3d.core._linmath import LColor, LPoint2, LPoint3, LTexCoord, LVector3
from panda3d.core._pgraph import GeomNode, NodePath, PandaNode
from panda3d.physics._physics import Physical

_BaseParticleEmitter_emissionType: TypeAlias = Literal[0, 1, 2]
_BaseParticleRenderer_ParticleRendererAlphaMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_ColorBlendAttrib_Mode: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_ColorBlendAttrib_Operand: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
_PointParticleRenderer_PointParticleBlendType: TypeAlias = Literal[0, 1, 2]
_BaseParticleRenderer_ParticleRendererBlendMethod: TypeAlias = Literal[0, 1, 2]
_SparkleParticleRenderer_SparkleParticleLifeScale: TypeAlias = Literal[0, 1]
_SpriteAnim_SourceType: TypeAlias = Literal[0, 1]

class BaseParticleEmitter(ReferenceCount):
    ET_EXPLICIT: Final = 0
    ETEXPLICIT: Final = 0
    ET_RADIATE: Final = 1
    ETRADIATE: Final = 1
    ET_CUSTOM: Final = 2
    ETCUSTOM: Final = 2
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def make_copy(self) -> BaseParticleEmitter: ...
    def generate(self, pos: Vec3Like, vel: Vec3Like) -> None:
        """parent generation function"""
    def set_emission_type(self, et: _BaseParticleEmitter_emissionType) -> None:
        """emission type assignment"""
    def set_amplitude(self, a: float) -> None:
        """amplitude assignment"""
    def set_amplitude_spread(self, _as: float) -> None:
        """amplitude spread assignment"""
    def set_offset_force(self, of: Vec3Like) -> None:
        """this is a constant force applied to all particles"""
    def set_explicit_launch_vector(self, elv: Vec3Like) -> None:
        """assignment of explicit emission launch vector"""
    def set_radiate_origin(self, ro: Vec3Like) -> None:
        """assignment of radiate emission origin point"""
    def get_emission_type(self) -> _BaseParticleEmitter_emissionType:
        """emission type query"""
    def get_amplitude(self) -> float:
        """amplitude query"""
    def get_amplitude_spread(self) -> float:
        """amplitude spread query"""
    def get_offset_force(self) -> LVector3:
        """user-defined force"""
    def get_explicit_launch_vector(self) -> LVector3:
        """query for explicit emission launch vector"""
    def get_radiate_origin(self) -> LPoint3:
        """query for explicit emission launch vector"""
    def output(self, out: ostream) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    makeCopy = make_copy
    setEmissionType = set_emission_type
    setAmplitude = set_amplitude
    setAmplitudeSpread = set_amplitude_spread
    setOffsetForce = set_offset_force
    setExplicitLaunchVector = set_explicit_launch_vector
    setRadiateOrigin = set_radiate_origin
    getEmissionType = get_emission_type
    getAmplitude = get_amplitude
    getAmplitudeSpread = get_amplitude_spread
    getOffsetForce = get_offset_force
    getExplicitLaunchVector = get_explicit_launch_vector
    getRadiateOrigin = get_radiate_origin

class RingEmitter(BaseParticleEmitter):
    """Describes a planar ring region in which particles are generated."""

    def __init__(self, copy: RingEmitter = ...) -> None:
        """`(self)`:
        constructor

        `(self, copy: RingEmitter)`:
        copy constructor
        """
    def set_radius(self, r: float) -> None: ...
    def set_angle(self, angle: float) -> None: ...
    def set_radius_spread(self, spread: float) -> None: ...
    def set_uniform_emission(self, uniform_emission: int) -> None: ...
    def get_radius(self) -> float: ...
    def get_angle(self) -> float: ...
    def get_radius_spread(self) -> float: ...
    def get_uniform_emission(self) -> int: ...
    setRadius = set_radius
    setAngle = set_angle
    setRadiusSpread = set_radius_spread
    setUniformEmission = set_uniform_emission
    getRadius = get_radius
    getAngle = get_angle
    getRadiusSpread = get_radius_spread
    getUniformEmission = get_uniform_emission

class ArcEmitter(RingEmitter):
    """Describes a planar ring region in which particles are generated."""

    def __init__(self, copy: ArcEmitter = ...) -> None:
        """`(self)`:
        constructor

        `(self, copy: ArcEmitter)`:
        copy constructor
        """
    def set_start_angle(self, angle: float) -> None: ...
    def set_end_angle(self, angle: float) -> None: ...
    def set_arc(self, startAngle: float, endAngle: float) -> None: ...
    def get_start_angle(self) -> float: ...
    def get_end_angle(self) -> float: ...
    setStartAngle = set_start_angle
    setEndAngle = set_end_angle
    setArc = set_arc
    getStartAngle = get_start_angle
    getEndAngle = get_end_angle

class BaseParticleFactory(ReferenceCount):
    """Pure Virtual base class for creating particles"""

    def set_lifespan_base(self, lb: float) -> None:
        """public"""
    def set_lifespan_spread(self, ls: float) -> None:
        """public"""
    def set_mass_base(self, mb: float) -> None:
        """public"""
    def set_mass_spread(self, ms: float) -> None:
        """public"""
    def set_terminal_velocity_base(self, tvb: float) -> None:
        """public"""
    def set_terminal_velocity_spread(self, tvs: float) -> None:
        """public"""
    def get_lifespan_base(self) -> float:
        """public"""
    def get_lifespan_spread(self) -> float:
        """public"""
    def get_mass_base(self) -> float:
        """public"""
    def get_mass_spread(self) -> float:
        """public"""
    def get_terminal_velocity_base(self) -> float:
        """public"""
    def get_terminal_velocity_spread(self) -> float:
        """public"""
    def output(self, out: ostream) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    setLifespanBase = set_lifespan_base
    setLifespanSpread = set_lifespan_spread
    setMassBase = set_mass_base
    setMassSpread = set_mass_spread
    setTerminalVelocityBase = set_terminal_velocity_base
    setTerminalVelocitySpread = set_terminal_velocity_spread
    getLifespanBase = get_lifespan_base
    getLifespanSpread = get_lifespan_spread
    getMassBase = get_mass_base
    getMassSpread = get_mass_spread
    getTerminalVelocityBase = get_terminal_velocity_base
    getTerminalVelocitySpread = get_terminal_velocity_spread

class BaseParticleRenderer(ReferenceCount):
    """Pure virtual particle renderer base class"""

    PR_ALPHA_NONE: Final = 0
    PRALPHANONE: Final = 0
    PR_ALPHA_OUT: Final = 1
    PRALPHAOUT: Final = 1
    PR_ALPHA_IN: Final = 2
    PRALPHAIN: Final = 2
    PR_ALPHA_IN_OUT: Final = 3
    PRALPHAINOUT: Final = 3
    PR_ALPHA_USER: Final = 4
    PRALPHAUSER: Final = 4
    PR_NOT_INITIALIZED_YET: Final = 5
    PRNOTINITIALIZEDYET: Final = 5
    PP_NO_BLEND: Final = 0
    PPNOBLEND: Final = 0
    PP_BLEND_LINEAR: Final = 1
    PPBLENDLINEAR: Final = 1
    PP_BLEND_CUBIC: Final = 2
    PPBLENDCUBIC: Final = 2
    def get_render_node(self) -> GeomNode:
        """Query the geomnode pointer"""
    def get_render_node_path(self) -> NodePath:
        """Query the geomnode pointer"""
    def set_alpha_mode(self, am: _BaseParticleRenderer_ParticleRendererAlphaMode) -> None: ...
    def get_alpha_mode(self) -> _BaseParticleRenderer_ParticleRendererAlphaMode: ...
    def set_user_alpha(self, ua: float) -> None:
        """sets alpha for "user" alpha mode"""
    def get_user_alpha(self) -> float:
        """gets alpha for "user" alpha mode"""
    def set_color_blend_mode(
        self, bm: _ColorBlendAttrib_Mode, oa: _ColorBlendAttrib_Operand = ..., ob: _ColorBlendAttrib_Operand = ...
    ) -> None:
        """sets the ColorBlendAttrib on the _render_node"""
    def set_ignore_scale(self, ignore_scale: bool) -> None:
        """Sets the "ignore scale" flag.  When this is true, particles will be drawn
        as if they had no scale, regardless of whatever scale might be inherited
        from above the render node in the scene graph.

        This flag is mainly useful to support legacy code that was written for a
        very early version of Panda, whose sprite particle renderer had a bug that
        incorrectly ignored the inherited scale.
        """
    def get_ignore_scale(self) -> bool:
        """Returns the "ignore scale" flag.  See set_ignore_scale()."""
    def output(self, out: ostream) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    getRenderNode = get_render_node
    getRenderNodePath = get_render_node_path
    setAlphaMode = set_alpha_mode
    getAlphaMode = get_alpha_mode
    setUserAlpha = set_user_alpha
    getUserAlpha = get_user_alpha
    setColorBlendMode = set_color_blend_mode
    setIgnoreScale = set_ignore_scale
    getIgnoreScale = get_ignore_scale

class BoxEmitter(BaseParticleEmitter):
    """Describes a voluminous box region in which particles are generated."""

    def __init__(self, copy: BoxEmitter = ...) -> None:
        """`(self)`:
        constructor

        `(self, copy: BoxEmitter)`:
        copy constructor
        """
    def set_min_bound(self, vmin: Vec3Like) -> None:
        """boundary assignment"""
    def set_max_bound(self, vmax: Vec3Like) -> None:
        """boundary assignment"""
    def get_min_bound(self) -> LPoint3:
        """boundary accessor"""
    def get_max_bound(self) -> LPoint3:
        """boundary accessor"""
    setMinBound = set_min_bound
    setMaxBound = set_max_bound
    getMinBound = get_min_bound
    getMaxBound = get_max_bound

class ColorInterpolationFunctionConstant:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_color_a(self) -> LColor: ...
    def set_color_a(self, c: Vec4Like) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getColorA = get_color_a
    setColorA = set_color_a
    getClassType = get_class_type

class ColorInterpolationFunctionLinear(ColorInterpolationFunctionConstant):
    def get_color_b(self) -> LColor: ...
    def set_color_b(self, c: Vec4Like) -> None: ...
    getColorB = get_color_b
    setColorB = set_color_b

class ColorInterpolationFunctionStepwave(ColorInterpolationFunctionLinear):
    def get_width_a(self) -> float: ...
    def get_width_b(self) -> float: ...
    def set_width_a(self, w: float) -> None: ...
    def set_width_b(self, w: float) -> None: ...
    getWidthA = get_width_a
    getWidthB = get_width_b
    setWidthA = set_width_a
    setWidthB = set_width_b

class ColorInterpolationFunctionSinusoid(ColorInterpolationFunctionLinear):
    def get_period(self) -> float: ...
    def set_period(self, p: float) -> None: ...
    getPeriod = get_period
    setPeriod = set_period

class ColorInterpolationSegment(ReferenceCount):
    def __init__(self, s: ColorInterpolationSegment) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_function(self) -> TypedReferenceCount:
        """INLINE ColorInterpolationFunction* get_function() const;"""
    def get_time_begin(self) -> float: ...
    def get_time_end(self) -> float: ...
    def is_modulated(self) -> bool: ...
    def get_id(self) -> int: ...
    def is_enabled(self) -> bool: ...
    def set_time_begin(self, time: float) -> None: ...
    def set_time_end(self, time: float) -> None: ...
    def set_is_modulated(self, flag: bool) -> None: ...
    def set_enabled(self, enabled: bool) -> None: ...
    getFunction = get_function
    getTimeBegin = get_time_begin
    getTimeEnd = get_time_end
    isModulated = is_modulated
    getId = get_id
    isEnabled = is_enabled
    setTimeBegin = set_time_begin
    setTimeEnd = set_time_end
    setIsModulated = set_is_modulated
    setEnabled = set_enabled

class ColorInterpolationManager(ReferenceCount):
    @overload
    def __init__(self, copy: ColorInterpolationManager = ...) -> None: ...
    @overload
    def __init__(self, c: Vec4Like) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def add_constant(
        self, time_begin: float = ..., time_end: float = ..., color: Vec4Like = ..., is_modulated: bool = ...
    ) -> int: ...
    def add_linear(
        self,
        time_begin: float = ...,
        time_end: float = ...,
        color_a: Vec4Like = ...,
        color_b: Vec4Like = ...,
        is_modulated: bool = ...,
    ) -> int: ...
    def add_stepwave(
        self,
        time_begin: float = ...,
        time_end: float = ...,
        color_a: Vec4Like = ...,
        color_b: Vec4Like = ...,
        width_a: float = ...,
        width_b: float = ...,
        is_modulated: bool = ...,
    ) -> int: ...
    def add_sinusoid(
        self,
        time_begin: float = ...,
        time_end: float = ...,
        color_a: Vec4Like = ...,
        color_b: Vec4Like = ...,
        period: float = ...,
        is_modulated: bool = ...,
    ) -> int: ...
    def set_default_color(self, c: Vec4Like) -> None: ...
    def get_segment(self, seg_id: int) -> ColorInterpolationSegment: ...
    def get_segment_id_list(self) -> str: ...
    def clear_segment(self, seg_id: int) -> None: ...
    def clear_to_initial(self) -> None: ...
    addConstant = add_constant
    addLinear = add_linear
    addStepwave = add_stepwave
    addSinusoid = add_sinusoid
    setDefaultColor = set_default_color
    getSegment = get_segment
    getSegmentIdList = get_segment_id_list
    clearSegment = clear_segment
    clearToInitial = clear_to_initial

class DiscEmitter(BaseParticleEmitter):
    """Describes a planar disc region from which particles are generated"""

    def __init__(self, copy: DiscEmitter = ...) -> None:
        """`(self)`:
        constructor

        `(self, copy: DiscEmitter)`:
        copy constructor
        """
    def set_radius(self, r: float) -> None: ...
    def set_outer_angle(self, o_angle: float) -> None: ...
    def set_inner_angle(self, i_angle: float) -> None: ...
    def set_outer_magnitude(self, o_mag: float) -> None: ...
    def set_inner_magnitude(self, i_mag: float) -> None: ...
    def set_cubic_lerping(self, clerp: bool) -> None: ...
    def get_radius(self) -> float: ...
    def get_outer_angle(self) -> float: ...
    def get_inner_angle(self) -> float: ...
    def get_outer_magnitude(self) -> float: ...
    def get_inner_magnitude(self) -> float: ...
    def get_cubic_lerping(self) -> bool: ...
    setRadius = set_radius
    setOuterAngle = set_outer_angle
    setInnerAngle = set_inner_angle
    setOuterMagnitude = set_outer_magnitude
    setInnerMagnitude = set_inner_magnitude
    setCubicLerping = set_cubic_lerping
    getRadius = get_radius
    getOuterAngle = get_outer_angle
    getInnerAngle = get_inner_angle
    getOuterMagnitude = get_outer_magnitude
    getInnerMagnitude = get_inner_magnitude
    getCubicLerping = get_cubic_lerping

class GeomParticleRenderer(BaseParticleRenderer):
    @overload
    def __init__(self, am: _BaseParticleRenderer_ParticleRendererAlphaMode = ..., geom_node: PandaNode = ...) -> None: ...
    @overload
    def __init__(self, copy: GeomParticleRenderer) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_geom_node(self, node: PandaNode) -> None: ...
    def get_geom_node(self) -> PandaNode: ...
    def get_color_interpolation_manager(self) -> ColorInterpolationManager: ...
    def set_x_scale_flag(self, animate_x_ratio: bool) -> None: ...
    def set_y_scale_flag(self, animate_y_ratio: bool) -> None: ...
    def set_z_scale_flag(self, animate_z_ratio: bool) -> None: ...
    def set_initial_x_scale(self, initial_x_scale: float) -> None: ...
    def set_final_x_scale(self, final_x_scale: float) -> None: ...
    def set_initial_y_scale(self, initial_y_scale: float) -> None: ...
    def set_final_y_scale(self, final_y_scale: float) -> None: ...
    def set_initial_z_scale(self, initial_z_scale: float) -> None: ...
    def set_final_z_scale(self, final_z_scale: float) -> None: ...
    def get_x_scale_flag(self) -> bool: ...
    def get_y_scale_flag(self) -> bool: ...
    def get_z_scale_flag(self) -> bool: ...
    def get_initial_x_scale(self) -> float: ...
    def get_final_x_scale(self) -> float: ...
    def get_initial_y_scale(self) -> float: ...
    def get_final_y_scale(self) -> float: ...
    def get_initial_z_scale(self) -> float: ...
    def get_final_z_scale(self) -> float: ...
    setGeomNode = set_geom_node
    getGeomNode = get_geom_node
    getColorInterpolationManager = get_color_interpolation_manager
    setXScaleFlag = set_x_scale_flag
    setYScaleFlag = set_y_scale_flag
    setZScaleFlag = set_z_scale_flag
    setInitialXScale = set_initial_x_scale
    setFinalXScale = set_final_x_scale
    setInitialYScale = set_initial_y_scale
    setFinalYScale = set_final_y_scale
    setInitialZScale = set_initial_z_scale
    setFinalZScale = set_final_z_scale
    getXScaleFlag = get_x_scale_flag
    getYScaleFlag = get_y_scale_flag
    getZScaleFlag = get_z_scale_flag
    getInitialXScale = get_initial_x_scale
    getFinalXScale = get_final_x_scale
    getInitialYScale = get_initial_y_scale
    getFinalYScale = get_final_y_scale
    getInitialZScale = get_initial_z_scale
    getFinalZScale = get_final_z_scale

class LineEmitter(BaseParticleEmitter):
    """Describes a linear region in which particles are generated."""

    def __init__(self, copy: LineEmitter = ...) -> None:
        """constructor"""
    def set_endpoint1(self, point: Vec3Like) -> None:
        """endpoint assignment"""
    def set_endpoint2(self, point: Vec3Like) -> None:
        """endpoint assignment"""
    def get_endpoint1(self) -> LPoint3:
        """endpoint accessor"""
    def get_endpoint2(self) -> LPoint3:
        """endpoint accessor"""
    setEndpoint1 = set_endpoint1
    setEndpoint2 = set_endpoint2
    getEndpoint1 = get_endpoint1
    getEndpoint2 = get_endpoint2

class LineParticleRenderer(BaseParticleRenderer):
    @overload
    def __init__(self, copy: LineParticleRenderer = ...) -> None: ...
    @overload
    def __init__(self, head: Vec4Like, tail: Vec4Like, alpha_mode: _BaseParticleRenderer_ParticleRendererAlphaMode) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_head_color(self, c: Vec4Like) -> None: ...
    def set_tail_color(self, c: Vec4Like) -> None: ...
    def get_head_color(self) -> LColor: ...
    def get_tail_color(self) -> LColor: ...
    def set_line_scale_factor(self, sf: float) -> None:
        """accessor"""
    def get_line_scale_factor(self) -> float:
        """accessor"""
    setHeadColor = set_head_color
    setTailColor = set_tail_color
    getHeadColor = get_head_color
    getTailColor = get_tail_color
    setLineScaleFactor = set_line_scale_factor
    getLineScaleFactor = get_line_scale_factor

class ParticleSystem(Physical):
    """Contains and manages a particle system."""

    @overload
    def __init__(self, pool_size: int = ...) -> None:
        """`(self, copy: ParticleSystem)`:
        Copy Constructor.

        `(self, pool_size: int = ...)`:
        Default Constructor.
        """
    @overload
    def __init__(self, copy: ParticleSystem) -> None: ...
    def set_pool_size(self, size: int) -> None:
        """accessqueries"""
    def set_birth_rate(self, new_br: float) -> None: ...
    def set_soft_birth_rate(self, new_br: float) -> None: ...
    def set_litter_size(self, new_ls: int) -> None: ...
    def set_litter_spread(self, new_ls: int) -> None: ...
    def set_local_velocity_flag(self, lv: bool) -> None: ...
    def set_system_grows_older_flag(self, sgo: bool) -> None: ...
    def set_system_lifespan(self, sl: float) -> None: ...
    def set_system_age(self, age: float) -> None: ...
    def set_active_system_flag(self, a: bool) -> None: ...
    def set_spawn_on_death_flag(self, sod: bool) -> None: ...
    def set_spawn_render_node(self, node: PandaNode) -> None: ...
    def set_spawn_render_node_path(self, node: NodePath) -> None: ...
    def set_template_system_flag(self, tsf: bool) -> None: ...
    def set_render_parent(self, node: NodePath | PandaNode) -> None: ...
    def set_renderer(self, r: BaseParticleRenderer) -> None: ...
    def set_emitter(self, e: BaseParticleEmitter) -> None: ...
    def set_factory(self, f: BaseParticleFactory) -> None: ...
    def set_floor_z(self, z: float) -> None: ...
    def clear_floor_z(self) -> None: ...
    def get_pool_size(self) -> int: ...
    def get_birth_rate(self) -> float: ...
    def get_soft_birth_rate(self) -> float: ...
    def get_litter_size(self) -> int: ...
    def get_litter_spread(self) -> int: ...
    def get_local_velocity_flag(self) -> bool: ...
    def get_system_grows_older_flag(self) -> bool: ...
    def get_system_lifespan(self) -> float: ...
    def get_system_age(self) -> float: ...
    def get_active_system_flag(self) -> bool: ...
    def get_spawn_on_death_flag(self) -> bool: ...
    def get_spawn_render_node(self) -> PandaNode: ...
    def get_spawn_render_node_path(self) -> NodePath: ...
    def get_i_was_spawned_flag(self) -> bool: ...
    def get_living_particles(self) -> int: ...
    def get_render_parent(self) -> NodePath: ...
    def get_renderer(self) -> BaseParticleRenderer: ...
    def get_emitter(self) -> BaseParticleEmitter: ...
    def get_factory(self) -> BaseParticleFactory: ...
    def get_floor_z(self) -> float: ...
    def get_tics_since_birth(self) -> float: ...
    def add_spawn_template(self, ps: ParticleSystem) -> None: ...
    def clear_spawn_templates(self) -> None: ...
    def render(self) -> None:
        """Populates an attached GeomNode structure with the particle geometry for
        rendering.  This is a wrapper for accessability.
        """
    def induce_labor(self) -> None:
        """Forces the birth of a particle litter this frame by resetting
        _tics_since_birth
        """
    def clear_to_initial(self) -> None:
        """Resets the system to its start state by resizing to 0, then resizing back
        to current size.
        """
    def soft_stop(self, br: float = ...) -> None:
        """Causes system to use birth rate set by set_soft_birth_rate()"""
    @overload
    def soft_start(self, br: float = ...) -> None:
        """`(self, br: float = ...)`:
        Causes system to use birth rate set by set_birth_rate()

        `(self, br: float, first_birth_delay: float)`:
        Causes system to use birth rate set by set_birth_rate(), with the system's
        first birth being delayed by the value of first_birth_delay. Note that a
        negative delay is perfectly valid, causing the first birth to happen
        sooner rather than later.
        """
    @overload
    def soft_start(self, br: float, first_birth_delay: float) -> None: ...
    def update(self, dt: float) -> None: ...
    def write_free_particle_fifo(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def write_spawn_templates(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    setPoolSize = set_pool_size
    setBirthRate = set_birth_rate
    setSoftBirthRate = set_soft_birth_rate
    setLitterSize = set_litter_size
    setLitterSpread = set_litter_spread
    setLocalVelocityFlag = set_local_velocity_flag
    setSystemGrowsOlderFlag = set_system_grows_older_flag
    setSystemLifespan = set_system_lifespan
    setSystemAge = set_system_age
    setActiveSystemFlag = set_active_system_flag
    setSpawnOnDeathFlag = set_spawn_on_death_flag
    setSpawnRenderNode = set_spawn_render_node
    setSpawnRenderNodePath = set_spawn_render_node_path
    setTemplateSystemFlag = set_template_system_flag
    setRenderParent = set_render_parent
    setRenderer = set_renderer
    setEmitter = set_emitter
    setFactory = set_factory
    setFloorZ = set_floor_z
    clearFloorZ = clear_floor_z
    getPoolSize = get_pool_size
    getBirthRate = get_birth_rate
    getSoftBirthRate = get_soft_birth_rate
    getLitterSize = get_litter_size
    getLitterSpread = get_litter_spread
    getLocalVelocityFlag = get_local_velocity_flag
    getSystemGrowsOlderFlag = get_system_grows_older_flag
    getSystemLifespan = get_system_lifespan
    getSystemAge = get_system_age
    getActiveSystemFlag = get_active_system_flag
    getSpawnOnDeathFlag = get_spawn_on_death_flag
    getSpawnRenderNode = get_spawn_render_node
    getSpawnRenderNodePath = get_spawn_render_node_path
    getIWasSpawnedFlag = get_i_was_spawned_flag
    getLivingParticles = get_living_particles
    getRenderParent = get_render_parent
    getRenderer = get_renderer
    getEmitter = get_emitter
    getFactory = get_factory
    getFloorZ = get_floor_z
    getTicsSinceBirth = get_tics_since_birth
    addSpawnTemplate = add_spawn_template
    clearSpawnTemplates = clear_spawn_templates
    induceLabor = induce_labor
    clearToInitial = clear_to_initial
    softStop = soft_stop
    softStart = soft_start
    writeFreeParticleFifo = write_free_particle_fifo
    writeSpawnTemplates = write_spawn_templates

class PointEmitter(BaseParticleEmitter):
    """Describes a planar ring region in which particles are generated."""

    def __init__(self, copy: PointEmitter = ...) -> None:
        """`(self)`:
        constructor

        `(self, copy: PointEmitter)`:
        copy constructor
        """
    def set_location(self, p: Vec3Like) -> None:
        """point setting"""
    def get_location(self) -> LPoint3: ...
    setLocation = set_location
    getLocation = get_location

class PointParticleFactory(BaseParticleFactory):
    def __init__(self, copy: PointParticleFactory = ...) -> None:
        """`(self)`:
        default constructor

        `(self, copy: PointParticleFactory)`:
        copy constructor
        """
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...

class PointParticleRenderer(BaseParticleRenderer):
    PP_ONE_COLOR: Final = 0
    PPONECOLOR: Final = 0
    PP_BLEND_LIFE: Final = 1
    PPBLENDLIFE: Final = 1
    PP_BLEND_VEL: Final = 2
    PPBLENDVEL: Final = 2
    @overload
    def __init__(
        self,
        ad: _BaseParticleRenderer_ParticleRendererAlphaMode = ...,
        point_size: float = ...,
        bt: _PointParticleRenderer_PointParticleBlendType = ...,
        bm: _BaseParticleRenderer_ParticleRendererBlendMethod = ...,
        sc: Vec4Like = ...,
        ec: Vec4Like = ...,
    ) -> None:
        """`(self, ad: _BaseParticleRenderer_ParticleRendererAlphaMode = ..., point_size: float = ..., bt: _PointParticleRenderer_PointParticleBlendType = ..., bm: _BaseParticleRenderer_ParticleRendererBlendMethod = ..., sc: LColor = ..., ec: LColor = ...)`:
        special constructor

        `(self, copy: PointParticleRenderer)`:
        Copy constructor
        """
    @overload
    def __init__(self, copy: PointParticleRenderer) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_point_size(self, point_size: float) -> None: ...
    def set_start_color(self, sc: Vec4Like) -> None: ...
    def set_end_color(self, ec: Vec4Like) -> None: ...
    def set_blend_type(self, bt: _PointParticleRenderer_PointParticleBlendType) -> None: ...
    def set_blend_method(self, bm: _BaseParticleRenderer_ParticleRendererBlendMethod) -> None: ...
    def get_point_size(self) -> float: ...
    def get_start_color(self) -> LColor: ...
    def get_end_color(self) -> LColor: ...
    def get_blend_type(self) -> _PointParticleRenderer_PointParticleBlendType: ...
    def get_blend_method(self) -> _BaseParticleRenderer_ParticleRendererBlendMethod: ...
    setPointSize = set_point_size
    setStartColor = set_start_color
    setEndColor = set_end_color
    setBlendType = set_blend_type
    setBlendMethod = set_blend_method
    getPointSize = get_point_size
    getStartColor = get_start_color
    getEndColor = get_end_color
    getBlendType = get_blend_type
    getBlendMethod = get_blend_method

class RectangleEmitter(BaseParticleEmitter):
    """Describes a planar square region in which particles are generated."""

    def __init__(self, copy: RectangleEmitter = ...) -> None:
        """`(self)`:
        constructor

        `(self, copy: RectangleEmitter)`:
        copy constructor
        """
    def set_min_bound(self, vmin: Vec2Like) -> None:
        """boundary set"""
    def set_max_bound(self, vmax: Vec2Like) -> None:
        """boundary set"""
    def get_min_bound(self) -> LPoint2:
        """boundary get"""
    def get_max_bound(self) -> LPoint2:
        """boundary get"""
    setMinBound = set_min_bound
    setMaxBound = set_max_bound
    getMinBound = get_min_bound
    getMaxBound = get_max_bound

class SparkleParticleRenderer(BaseParticleRenderer):
    """pretty sparkly things."""

    SP_NO_SCALE: Final = 0
    SPNOSCALE: Final = 0
    SP_SCALE: Final = 1
    SPSCALE: Final = 1
    @overload
    def __init__(self, copy: SparkleParticleRenderer = ...) -> None:
        """`(self)`:
        Default Constructor

        `(self, copy: SparkleParticleRenderer)`:
        Copy Constructor
        """
    @overload
    def __init__(
        self,
        center: Vec4Like,
        edge: Vec4Like,
        birth_radius: float,
        death_radius: float,
        life_scale: _SparkleParticleRenderer_SparkleParticleLifeScale,
        alpha_mode: _BaseParticleRenderer_ParticleRendererAlphaMode,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_center_color(self, c: Vec4Like) -> None: ...
    def set_edge_color(self, c: Vec4Like) -> None: ...
    def set_birth_radius(self, radius: float) -> None: ...
    def set_death_radius(self, radius: float) -> None: ...
    def set_life_scale(self, __param0: _SparkleParticleRenderer_SparkleParticleLifeScale) -> None: ...
    def get_center_color(self) -> LColor: ...
    def get_edge_color(self) -> LColor: ...
    def get_birth_radius(self) -> float: ...
    def get_death_radius(self) -> float: ...
    def get_life_scale(self) -> _SparkleParticleRenderer_SparkleParticleLifeScale: ...
    setCenterColor = set_center_color
    setEdgeColor = set_edge_color
    setBirthRadius = set_birth_radius
    setDeathRadius = set_death_radius
    setLifeScale = set_life_scale
    getCenterColor = get_center_color
    getEdgeColor = get_edge_color
    getBirthRadius = get_birth_radius
    getDeathRadius = get_death_radius
    getLifeScale = get_life_scale

class SphereSurfaceEmitter(BaseParticleEmitter):
    """Describes a curved space in which particles are generated."""

    def __init__(self, copy: SphereSurfaceEmitter = ...) -> None:
        """`(self)`:
        constructor

        `(self, copy: SphereSurfaceEmitter)`:
        copy constructor
        """
    def set_radius(self, r: float) -> None: ...
    def get_radius(self) -> float: ...
    setRadius = set_radius
    getRadius = get_radius

class SphereVolumeEmitter(BaseParticleEmitter):
    """Describes a voluminous spherical region in which particles are generated."""

    def __init__(self, copy: SphereVolumeEmitter = ...) -> None:
        """`(self)`:
        constructor

        `(self, copy: SphereVolumeEmitter)`:
        copy constructor
        """
    def set_radius(self, r: float) -> None: ...
    def get_radius(self) -> float: ...
    setRadius = set_radius
    getRadius = get_radius

class SpriteAnim(ReferenceCount):
    """Helper class used by SpriteParticleRenderer to keep track of its textures
    and their respective UVs and source types.
    """

    ST_texture: Final = 0
    STTexture: Final = 0
    ST_from_node: Final = 1
    STFromNode: Final = 1
    def __init__(self, __param0: SpriteAnim) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @overload
    def set_source_info(self, tex: str) -> None: ...
    @overload
    def set_source_info(self, model: str, node: str) -> None: ...
    def get_source_type(self) -> _SpriteAnim_SourceType: ...
    def get_tex_source(self) -> str: ...
    def get_model_source(self) -> str: ...
    def get_node_source(self) -> str: ...
    def get_num_frames(self) -> int: ...
    setSourceInfo = set_source_info
    getSourceType = get_source_type
    getTexSource = get_tex_source
    getModelSource = get_model_source
    getNodeSource = get_node_source
    getNumFrames = get_num_frames

class SpriteParticleRenderer(BaseParticleRenderer):
    """Renders a particle system with high-speed nasty trick sprites."""

    @overload
    def __init__(self, tex: Texture = ...) -> None:
        """`(self, copy: SpriteParticleRenderer)`:
        copy constructor

        `(self, tex: Texture = ...)`:
        constructor
        """
    @overload
    def __init__(self, copy: SpriteParticleRenderer) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @overload
    def set_from_node(self, node_path: NodePath, size_from_texels: bool = ...) -> None:
        """`(self, node_path: NodePath, size_from_texels: bool = ...)`:
        Sets the properties on this renderer from the geometry referenced by the
        indicated NodePath.  This should be a reference to a GeomNode or a
        SequenceNode; it extracts out the texture and UV range from the node.

        This will remove all previously added textures and animations.  It will
        also resize the renderer to match this new geometry.

        If node_path refers to a GeomNode(or has one beneath it) the texture, its
        size, and UV data will be extracted from that.

        If node_path references a SequenceNode(or has one beneath it) with multiple
        GeomNodes beneath it, the size data will correspond only to the first
        GeomNode found with a valid texture, while the texture and UV information
        will be stored for each individual node.

        If size_from_texels is true, the particle size is based on the number of
        texels in the source image; otherwise, it is based on the size of the first
        polygon found in the node.

        model and node are the two items used to construct node_path.  If the
        source type is important, use set_from_node(NodePath,string,string,bool)
        instead.

        `(self, node_path: NodePath, model: str, node: str, size_from_texels: bool = ...)`:
        If the source type is important, use this one.

        model and node should lead to node_path like this: node_path =
        loader.loadModel(model).find(node)

        This will remove all previously add textures and resize the renderer to
        match the new geometry.
        """
    @overload
    def set_from_node(self, node_path: NodePath, model: str, node: str, size_from_texels: bool = ...) -> None: ...
    @overload
    def add_from_node(self, node_path: NodePath, size_from_texels: bool = ..., resize: bool = ...) -> None:
        """`(self, node_path: NodePath, size_from_texels: bool = ..., resize: bool = ...)`:
        This will allow the renderer to randomly choose from more than one texture
        or sequence at particle birth.

        If resize is true, or if there are no textures currently on the renderer,
        it will force the renderer to use the size information from this node from
        now on.  (Default is false)

        `(self, node_path: NodePath, model: str, node: str, size_from_texels: bool = ..., resize: bool = ...)`:
        This will allow the renderer to randomly choose from more than one texture
        or sequence at particle birth.

        If the source type is important, use this one.

        model and node should lead to node_path like this: node_path =
        loader.loadModel(model).find(node)

        If resize is true, or if there are no textures currently on the renderer,
        it will force the renderer to use the size information from this node from
        now on.  (Default is false)
        """
    @overload
    def add_from_node(
        self, node_path: NodePath, model: str, node: str, size_from_texels: bool = ..., resize: bool = ...
    ) -> None: ...
    def set_texture(self, tex: Texture, texels_per_unit: float = ...) -> None:
        """Sets the renderer up to render the entire texture image.  The scale of each
        particle is based on the size of the texture in each dimension, modified by
        texels_per_unit.

        Used to set the size of the particles.  Will clear all previously loaded
        textures and animations.
        """
    def add_texture(self, tex: Texture, texels_per_unit: float = ..., resize: bool = ...) -> None:
        """Adds texture to image pool, effectively creating a single frame animation
        that can be selected at particle birth.  This should only be called after a
        previous call to set_texture().
        """
    def remove_animation(self, n: int) -> None:
        """Removes an animation texture set from the renderer."""
    @overload
    def set_ll_uv(self, ll_uv: Vec2Like) -> None:
        """Sets the UV coordinate of the lower-left corner of all the sprites
        generated by this renderer.  Normally this is (0, 0), but it might be set
        to something else to use only a portion of the texture.
        """
    @overload
    def set_ll_uv(self, ll_uv: Vec2Like, anim: int, frame: int) -> None: ...
    @overload
    def set_ur_uv(self, ur_uv: Vec2Like) -> None:
        """Sets the UV coordinate of the upper-right corner of all the sprites
        generated by this renderer.  Normally this is (1, 1), but it might be set
        to something else to use only a portion of the texture.
        """
    @overload
    def set_ur_uv(self, ur_uv: Vec2Like, anim: int, frame: int) -> None: ...
    def set_size(self, width: float, height: float) -> None:
        """Sets the size of each particle in world units."""
    def set_color(self, color: Vec4Like) -> None: ...
    def set_x_scale_flag(self, animate_x_ratio: bool) -> None: ...
    def set_y_scale_flag(self, animate_y_ratio: bool) -> None: ...
    def set_anim_angle_flag(self, animate_theta: bool) -> None: ...
    def set_initial_x_scale(self, initial_x_scale: float) -> None: ...
    def set_final_x_scale(self, final_x_scale: float) -> None: ...
    def set_initial_y_scale(self, initial_y_scale: float) -> None: ...
    def set_final_y_scale(self, final_y_scale: float) -> None: ...
    def set_nonanimated_theta(self, theta: float) -> None: ...
    def set_alpha_blend_method(self, bm: _BaseParticleRenderer_ParticleRendererBlendMethod) -> None: ...
    def set_alpha_disable(self, ad: bool) -> None: ...
    def set_animate_frames_enable(self, an: bool) -> None: ...
    def set_animate_frames_rate(self, r: float) -> None: ...
    def set_animate_frames_index(self, i: int) -> None: ...
    @overload
    def get_texture(self) -> Texture: ...
    @overload
    def get_texture(self, anim: int, frame: int) -> Texture: ...
    def get_num_anims(self) -> int: ...
    def get_anim(self, n: int) -> SpriteAnim: ...
    def get_last_anim(self) -> SpriteAnim: ...
    def get_color_interpolation_manager(self) -> ColorInterpolationManager: ...
    @overload
    def get_ll_uv(self) -> LTexCoord:
        """Returns the UV coordinate of the lower-left corner; see set_ll_uv()."""
    @overload
    def get_ll_uv(self, anim: int, frame: int) -> LTexCoord: ...
    @overload
    def get_ur_uv(self) -> LTexCoord:
        """`(self)`:
        Returns the UV coordinate of the lower-left corner; see set_ur_uv().

        `(self, anim: int, frame: int)`:
        Returns the UV coordinate of the upper-right corner; see set_ur_uv().
        """
    @overload
    def get_ur_uv(self, anim: int, frame: int) -> LTexCoord: ...
    def get_width(self) -> float:
        """Returns the width of each particle in world units."""
    def get_height(self) -> float:
        """Returns the height of each particle in world units."""
    def get_color(self) -> LColor: ...
    def get_x_scale_flag(self) -> bool: ...
    def get_y_scale_flag(self) -> bool: ...
    def get_anim_angle_flag(self) -> bool: ...
    def get_initial_x_scale(self) -> float: ...
    def get_final_x_scale(self) -> float: ...
    def get_initial_y_scale(self) -> float: ...
    def get_final_y_scale(self) -> float: ...
    def get_nonanimated_theta(self) -> float: ...
    def get_alpha_blend_method(self) -> _BaseParticleRenderer_ParticleRendererBlendMethod: ...
    def get_alpha_disable(self) -> bool: ...
    def get_animate_frames_enable(self) -> bool: ...
    def get_animate_frames_rate(self) -> float: ...
    def get_animate_frames_index(self) -> int: ...
    def get_anims(self) -> tuple[SpriteAnim, ...]: ...
    setFromNode = set_from_node
    addFromNode = add_from_node
    setTexture = set_texture
    addTexture = add_texture
    removeAnimation = remove_animation
    setLlUv = set_ll_uv
    setUrUv = set_ur_uv
    setSize = set_size
    setColor = set_color
    setXScaleFlag = set_x_scale_flag
    setYScaleFlag = set_y_scale_flag
    setAnimAngleFlag = set_anim_angle_flag
    setInitialXScale = set_initial_x_scale
    setFinalXScale = set_final_x_scale
    setInitialYScale = set_initial_y_scale
    setFinalYScale = set_final_y_scale
    setNonanimatedTheta = set_nonanimated_theta
    setAlphaBlendMethod = set_alpha_blend_method
    setAlphaDisable = set_alpha_disable
    setAnimateFramesEnable = set_animate_frames_enable
    setAnimateFramesRate = set_animate_frames_rate
    setAnimateFramesIndex = set_animate_frames_index
    getTexture = get_texture
    getNumAnims = get_num_anims
    getAnim = get_anim
    getLastAnim = get_last_anim
    getColorInterpolationManager = get_color_interpolation_manager
    getLlUv = get_ll_uv
    getUrUv = get_ur_uv
    getWidth = get_width
    getHeight = get_height
    getColor = get_color
    getXScaleFlag = get_x_scale_flag
    getYScaleFlag = get_y_scale_flag
    getAnimAngleFlag = get_anim_angle_flag
    getInitialXScale = get_initial_x_scale
    getFinalXScale = get_final_x_scale
    getInitialYScale = get_initial_y_scale
    getFinalYScale = get_final_y_scale
    getNonanimatedTheta = get_nonanimated_theta
    getAlphaBlendMethod = get_alpha_blend_method
    getAlphaDisable = get_alpha_disable
    getAnimateFramesEnable = get_animate_frames_enable
    getAnimateFramesRate = get_animate_frames_rate
    getAnimateFramesIndex = get_animate_frames_index
    getAnims = get_anims

class TangentRingEmitter(BaseParticleEmitter):
    """Describes a planar ring region in which tangent particles are generated,
    and particles fly off tangential to the ring.
    """

    def __init__(self, copy: TangentRingEmitter = ...) -> None:
        """`(self)`:
        constructor

        `(self, copy: TangentRingEmitter)`:
        copy constructor
        """
    def set_radius(self, r: float) -> None: ...
    def set_radius_spread(self, spread: float) -> None: ...
    def get_radius(self) -> float: ...
    def get_radius_spread(self) -> float: ...
    setRadius = set_radius
    setRadiusSpread = set_radius_spread
    getRadius = get_radius
    getRadiusSpread = get_radius_spread

class ZSpinParticleFactory(BaseParticleFactory):
    def __init__(self, copy: ZSpinParticleFactory = ...) -> None:
        """`(self)`:
        constructor

        `(self, copy: ZSpinParticleFactory)`:
        copy constructor
        """
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_initial_angle(self, angle: float) -> None: ...
    def set_final_angle(self, angle: float) -> None: ...
    def set_initial_angle_spread(self, spread: float) -> None: ...
    def set_final_angle_spread(self, spread: float) -> None: ...
    def get_initial_angle(self) -> float: ...
    def get_final_angle(self) -> float: ...
    def get_initial_angle_spread(self) -> float: ...
    def get_final_angle_spread(self) -> float: ...
    def set_angular_velocity(self, v: float) -> None: ...
    def get_angular_velocity(self) -> float: ...
    def set_angular_velocity_spread(self, spread: float) -> None: ...
    def get_angular_velocity_spread(self) -> float: ...
    def enable_angular_velocity(self, bEnabled: bool) -> None: ...
    def get_angular_velocity_enabled(self) -> bool: ...
    setInitialAngle = set_initial_angle
    setFinalAngle = set_final_angle
    setInitialAngleSpread = set_initial_angle_spread
    setFinalAngleSpread = set_final_angle_spread
    getInitialAngle = get_initial_angle
    getFinalAngle = get_final_angle
    getInitialAngleSpread = get_initial_angle_spread
    getFinalAngleSpread = get_final_angle_spread
    setAngularVelocity = set_angular_velocity
    getAngularVelocity = get_angular_velocity
    setAngularVelocitySpread = set_angular_velocity_spread
    getAngularVelocitySpread = get_angular_velocity_spread
    enableAngularVelocity = enable_angular_velocity
    getAngularVelocityEnabled = get_angular_velocity_enabled

class ParticleSystemManager:
    """Manages a set of individual ParticleSystem objects, so that each individual
    one doesn't have to be updated and rendered every frame See Also :
    particleSystemManager.cxx
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, every_nth_frame: int = ...) -> None:
        """default constructor"""
    @overload
    def __init__(self, __param0: ParticleSystemManager) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_frame_stepping(self, every_nth_frame: int) -> None: ...
    def get_frame_stepping(self) -> int: ...
    def attach_particlesystem(self, ps: ParticleSystem) -> None: ...
    def remove_particlesystem(self, ps: ParticleSystem) -> None:
        """removes a ps from the maintenance list"""
    def clear(self) -> None: ...
    @overload
    def do_particles(self, dt: float) -> None:
        """`(self, dt: float)`:
        does an update and render for each ps in the list.  this is probably the
        one you want to use.  Rendering is the expensive operation, and particles
        REALLY should at least be updated every frame, so nth_frame stepping
        applies only to rendering.

        `(self, dt: float, ps: ParticleSystem, do_render: bool = ...)`:
        does an update and an optional render for a specific ps.  Since rendering
        is the expensive operation, multiple updates could be applied before
        calling the final render.
        """
    @overload
    def do_particles(self, dt: float, ps: ParticleSystem, do_render: bool = ...) -> None: ...
    def output(self, out: ostream) -> None:
        """Write a string representation of this instance to <out>."""
    def write_ps_list(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    setFrameStepping = set_frame_stepping
    getFrameStepping = get_frame_stepping
    attachParticlesystem = attach_particlesystem
    removeParticlesystem = remove_particlesystem
    doParticles = do_particles
    writePsList = write_ps_list
