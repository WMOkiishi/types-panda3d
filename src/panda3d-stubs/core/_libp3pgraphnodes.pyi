from collections.abc import Sequence
from typing import Any, ClassVar, Literal, TypeAlias, overload
from panda3d.core import (
    AnimInterface,
    CallbackData,
    CallbackObject,
    Camera,
    ConfigVariableColor,
    CullTraverser,
    CullTraverserData,
    GeomVertexAnimationSpec,
    GraphicsOutputBase,
    GraphicsStateGuardianBase,
    LMatrix3f,
    LMatrix4f,
    LPoint3f,
    LVecBase2i,
    LVecBase3f,
    LVecBase3i,
    LVecBase4f,
    LVector3f,
    Light,
    PandaNode,
    RenderState,
    ShaderAttrib,
    Texture,
    TypeHandle,
    TypedReferenceCount,
    UnalignedLVecBase4f,
    ostream,
)

_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_SceneGraphAnalyzer_LodMode: TypeAlias = Literal[0, 1, 2, 3]

class LightNode(Light, PandaNode):
    """A derivative of Light and of PandaNode.  All kinds of Light except
    Spotlight (which must inherit from LensNode instead) inherit from this
    class.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def upcast_to_Light(self) -> Light: ...
    def upcast_to_PandaNode(self) -> PandaNode: ...
    def output(self, out: ostream) -> None:
        """We have to explicitly publish these because they resolve the multiple
        inheritance.
        """
        ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToLight = upcast_to_Light
    upcastToPandaNode = upcast_to_PandaNode
    getClassType = get_class_type

class AmbientLight(LightNode):
    """A light source that seems to illuminate all points in space at once.  This
    kind of light need not actually be part of the scene graph, since it has no
    meaningful position.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class CallbackNode(PandaNode):
    """A special node that can issue arbitrary callbacks to user code, either
    during the cull or draw traversals.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    cull_callback: CallbackObject
    draw_callback: CallbackObject
    def __init__(self, name: str) -> None: ...
    def set_cull_callback(self, object: CallbackObject) -> None:
        """Sets the CallbackObject that will be notified when this node is visited
        during the cull traversal.  This callback will be made during the cull
        thread.
        
        The cull traversal is responsible for determining which nodes are visible
        and within the view frustum, and for accumulating state and transform, and
        generally building up the list of CullableObjects that are to be eventually
        passed to the draw traversal for rendering.
        
        At the time the cull traversal callback is made, the node has been
        determined to be visible and it has passed the bounding-volume test, so it
        lies within the view frustum.
        
        The callback is passed an instance of a NodeCullCallbackData, which
        contains pointers to the CullTraverser and CullTraverserData--enough data
        to examine the current node and its place within the scene graph.  The
        callback *replaces* the normal cull behavior, so if your callback does
        nothing, the cull traversal will not continue below this node.  If you wish
        the cull traversal to continue to visit this node and below, you must call
        cbdata->upcall() from your callback.
        """
        ...
    def clear_cull_callback(self) -> None:
        """Removes the callback set by an earlier call to set_cull_callback()."""
        ...
    def get_cull_callback(self) -> CallbackObject:
        """Returns the CallbackObject set by set_cull_callback()."""
        ...
    def set_draw_callback(self, object: CallbackObject) -> None:
        """Sets the CallbackObject that will be notified when this node is visited
        during the draw traversal.  This callback will be made during the draw
        thread.
        
        The draw traversal is responsible for actually issuing the commands to the
        graphics engine to draw primitives.  Its job is to walk through the list of
        CullableObjects build up by the cull traversal, as quickly as possible,
        issuing the appropriate commands to draw each one.
        
        At the time the draw traversal callback is made, the graphics state has
        been loaded with the correct modelview transform and render state, and the
        primitives (if any) in this node are ready to be drawn.
        
        The callback is passed an instance of a GeomDrawCallbackData, which
        contains pointers to the current state and transform, as well as the
        current GSG.  There is a Geom pointer as well, but it will always be NULL
        to this callback, since the CallbackNode does not itself contain any Geoms.
        """
        ...
    def clear_draw_callback(self) -> None:
        """Removes the callback set by an earlier call to set_draw_callback()."""
        ...
    def get_draw_callback(self) -> CallbackObject:
        """Returns the CallbackObject set by set_draw_callback()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setCullCallback = set_cull_callback
    clearCullCallback = clear_cull_callback
    getCullCallback = get_cull_callback
    setDrawCallback = set_draw_callback
    clearDrawCallback = clear_draw_callback
    getDrawCallback = get_draw_callback
    getClassType = get_class_type

class ComputeNode(PandaNode):
    """A special node, the sole purpose of which is to invoke a dispatch operation
    on the assigned compute shader.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    dispatches: Sequence[LVecBase3i]
    def __init__(self, name: str) -> None:
        """Creates a ComputeNode with the given name.  Use add_dispatch and  also
        assign a shader using a ShaderAttrib.
        """
        ...
    @overload
    def add_dispatch(self, num_groups: LVecBase3i) -> None:
        """Adds a dispatch command with the given number of work groups in the X, Y,
        and Z dimensions.  Any of these values may be set to 1 if the respective
        dimension should not be used.
        """
        ...
    @overload
    def add_dispatch(self, num_groups_x: int, num_groups_y: int, num_groups_z: int) -> None: ...
    def get_num_dispatches(self) -> int:
        """Returns the number of times add_dispatch has been called on this object."""
        ...
    def get_dispatch(self, i: int) -> LVecBase3i:
        """Returns the group counts of the nth dispatch associated with this object."""
        ...
    def set_dispatch(self, i: int, num_groups: LVecBase3i) -> None:
        """Sets the group counts of the nth dispatch associated with this object."""
        ...
    def insert_dispatch(self, i: int, num_groups: LVecBase3i) -> None:
        """Inserts a dispatch command with the given number of work groups in the X,
        Y, and Z dimensions at the given position in the list of dispatch commands.
        Any of these values may be set to 1 if the respective dimension should not
        be used.
        """
        ...
    def remove_dispatch(self, i: int) -> None:
        """Erases the given dispatch index from the list."""
        ...
    def clear_dispatches(self) -> None:
        """Removes all dispatch commands."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_dispatches(self) -> tuple[LVecBase3i, ...]: ...
    addDispatch = add_dispatch
    getNumDispatches = get_num_dispatches
    getDispatch = get_dispatch
    setDispatch = set_dispatch
    insertDispatch = insert_dispatch
    removeDispatch = remove_dispatch
    clearDispatches = clear_dispatches
    getClassType = get_class_type
    getDispatches = get_dispatches

class LightLensNode(Light, Camera):
    """A derivative of Light and of Camera.  The name might be misleading: it does
    not directly derive from LensNode, but through the Camera class.  The
    Camera serves no purpose unless shadows are enabled.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    shadow_buffer_size: LVecBase2i
    @property
    def shadow_caster(self) -> bool: ...
    def upcast_to_Light(self) -> Light: ...
    def upcast_to_Camera(self) -> Camera: ...
    def has_specular_color(self) -> bool:
        """Returns true if this light defines a specular color, false if the specular
        color is derived automatically from the light color.
        """
        ...
    def is_shadow_caster(self) -> bool:
        """Returns whether this light is configured to cast shadows or not."""
        ...
    @overload
    def set_shadow_caster(self, caster: bool) -> None:
        """`(self, caster: bool)`:
        Sets the flag indicating whether this light should cast shadows or not.
        This is the variant without buffer size, meaning that the current buffer
        size will be kept (512x512 is the default). Note that enabling shadows will
        require the shader generator to be enabled on the scene.
        
        `(self, caster: bool, buffer_xsize: int, buffer_ysize: int, sort: int = ...)`:
        Sets the flag indicating whether this light should cast shadows or not.
        The xsize and ysize parameters specify the size of the shadow buffer that
        will be set up, the sort parameter specifies the sort.  Note that enabling
        shadows will require the shader generator to be enabled on the scene.
        """
        ...
    @overload
    def set_shadow_caster(self, caster: bool, buffer_xsize: int, buffer_ysize: int, sort: int = ...) -> None: ...
    def get_shadow_buffer_sort(self) -> int:
        """Returns the sort of the shadow buffer to be created for this light source."""
        ...
    def get_shadow_buffer_size(self) -> LVecBase2i:
        """Returns the size of the shadow buffer to be created for this light source."""
        ...
    def set_shadow_buffer_size(self, size: LVecBase2i) -> None:
        """Sets the size of the shadow buffer to be created for this light source."""
        ...
    def get_shadow_buffer(self, gsg: GraphicsStateGuardianBase) -> GraphicsOutputBase:
        """Returns the buffer that has been constructed for a given GSG, or NULL if no
        such buffer has (yet) been constructed.  This should be used for debugging
        only, you will not need to call this normally.
        """
        ...
    def output(self, out: ostream) -> None:
        """We have to explicitly publish these because they resolve the multiple
        inheritance.
        """
        ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToLight = upcast_to_Light
    upcastToCamera = upcast_to_Camera
    hasSpecularColor = has_specular_color
    isShadowCaster = is_shadow_caster
    setShadowCaster = set_shadow_caster
    getShadowBufferSort = get_shadow_buffer_sort
    getShadowBufferSize = get_shadow_buffer_size
    setShadowBufferSize = set_shadow_buffer_size
    getShadowBuffer = get_shadow_buffer
    getClassType = get_class_type

class DirectionalLight(LightLensNode):
    """A light shining from infinitely far away in a particular direction, like
    sunlight.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    specular_color: LVecBase4f
    point: LPoint3f
    direction: LVector3f
    def __init__(self, name: str) -> None: ...
    def set_specular_color(self, color: _Vec4f) -> None:
        """Sets the color of specular highlights generated by the light."""
        ...
    def clear_specular_color(self) -> None:
        """Clears a custom specular color setting, meaning that the specular color
        will now come from the color.
        """
        ...
    def get_point(self) -> LPoint3f:
        """Returns the point in space at which the light is located.  This is local to
        the coordinate space in which the light is assigned.
        
        This actually has no bearing on the visual effect of the light, since the
        light is rendered as if it were infinitely far away.  This is only used to
        create a visible representation of the light.
        """
        ...
    def set_point(self, point: _Vec3f) -> None:
        """Sets the point in space at which the light is located."""
        ...
    def get_direction(self) -> LVector3f:
        """Returns the direction in which the light is aimed.  This is local to the
        coordinate space in which the light is assigned.
        """
        ...
    def set_direction(self, direction: _Vec3f) -> None:
        """Sets the direction in which the light is aimed."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setSpecularColor = set_specular_color
    clearSpecularColor = clear_specular_color
    getPoint = get_point
    setPoint = set_point
    getDirection = get_direction
    setDirection = set_direction
    getClassType = get_class_type

class LODNode(PandaNode):
    """A Level-of-Detail node.  This selects only one of its children for
    rendering, according to the distance from the camera and the table
    indicated in the associated LOD object.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    lod_scale: float
    center: LPoint3f
    @property
    def ins(self) -> Sequence[float]: ...
    @property
    def outs(self) -> Sequence[float]: ...
    @property
    def lowest_switch(self) -> int: ...
    @property
    def highest_switch(self) -> int: ...
    def __init__(self, name: str) -> None: ...
    @staticmethod
    def make_default_lod(name: str) -> LODNode:
        """Creates a new LODNode of the type specified by the default-lod-type config
        variable.
        """
        ...
    def add_switch(self, _in: float, out: float) -> None:
        """Adds a switch range to the LODNode.  This implies that the corresponding
        child node has been parented to the node.
        
        The sense of in vs.  out distances is as if the object were coming towards
        you from far away: it switches "in" at the far distance, and switches "out"
        at the close distance.  Thus, "in" should be larger than "out".
        """
        ...
    def set_switch(self, index: int, _in: float, out: float) -> bool:
        """Changes the switching range of a particular child of the LODNode.  See
        add_switch().
        """
        ...
    def clear_switches(self) -> None:
        """Removes the set of switching ranges for the LODNode, presumably in
        conjunction with removing all of its children.  See add_switch().
        """
        ...
    def get_num_switches(self) -> int:
        """Returns the number of switch ranges added to the LODNode.  This should
        correspond to the number of children of the node in order for the LODNode
        to function correctly.
        """
        ...
    def get_in(self, index: int) -> float:
        """Returns the "in" distance of the indicated switch range.  This should be
        larger than the "out" distance of the same range.
        """
        ...
    def get_out(self, index: int) -> float:
        """Returns the "out" distance of the indicated switch range.  This should be
        smaller than the "in" distance of the same range.
        """
        ...
    def get_lowest_switch(self) -> int:
        """Returns the index number of the child with the lowest level of detail; that
        is, the one that is designed to be seen from the farthest away.  This is
        usually the first child, but it is not necessarily so.
        """
        ...
    def get_highest_switch(self) -> int:
        """Returns the index number of the child with the highest level of detail;
        that is, the one that is designed to be seen from the closest to the
        camera.  This is usually the last child, but it is not necessarily so.
        """
        ...
    def force_switch(self, index: int) -> None:
        """Forces the LODNode to show the indicated level instead of the level that
        would normally be shown based on the distance from the camera.
        """
        ...
    def clear_force_switch(self) -> None:
        """Undoes the effect of a previous call to force_switch() and releases the
        LODNode to once again display the normal level.
        """
        ...
    def set_lod_scale(self, value: float) -> None:
        """Sets the multiplier for lod distances.  A higher value means you'll see
        farther switchs than normal
        """
        ...
    def get_lod_scale(self) -> float:
        """Returns the multiplier for lod distances"""
        ...
    def set_center(self, center: _Vec3f) -> None:
        """Specifies the center of the LOD.  This is the point that is compared to the
        camera (in camera space) to determine the particular LOD that should be
        chosen.
        """
        ...
    def get_center(self) -> LPoint3f:
        """Returns the center of the LOD.  This is the point that is compared to the
        camera (in camera space) to determine the particular LOD that should be
        chosen.
        """
        ...
    @overload
    def show_switch(self, index: int) -> None:
        """This is provided as a debugging aid.  show_switch() will put the LODNode
        into a special mode where rather than computing and drawing the appropriate
        level of the LOD, a ring is drawn around the LODNode center indicating the
        switch distances from the camera for the indicated level, and the geometry
        of the indicated level is drawn in wireframe.
        
        Multiple different levels can be visualized this way at once.  Call
        hide_switch() or hide_all_switches() to undo this mode and restore the
        LODNode to its normal behavior.
        """
        ...
    @overload
    def show_switch(self, index: int, color: _Vec4f) -> None: ...
    def hide_switch(self, index: int) -> None:
        """Disables a previous call to show_switch()."""
        ...
    def show_all_switches(self) -> None:
        """Shows all levels in their default colors."""
        ...
    def hide_all_switches(self) -> None:
        """Hides all levels, restoring the LODNode to normal operation."""
        ...
    def is_any_shown(self) -> bool:
        """Returns true if any switch has been shown with show_switch(), indicating
        the LODNode is in debug show mode; or false if it is in the normal mode.
        """
        ...
    def verify_child_bounds(self) -> bool:
        """Returns true if the bounding volumes for the geometry of each fhild node
        entirely fits within the switch_in radius for that child, or false
        otherwise.  It is almost always a mistake for the geometry of an LOD level
        to be larger than its switch_in radius.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_ins(self) -> tuple[float, ...]: ...
    def get_outs(self) -> tuple[float, ...]: ...
    makeDefaultLod = make_default_lod
    addSwitch = add_switch
    setSwitch = set_switch
    clearSwitches = clear_switches
    getNumSwitches = get_num_switches
    getIn = get_in
    getOut = get_out
    getLowestSwitch = get_lowest_switch
    getHighestSwitch = get_highest_switch
    forceSwitch = force_switch
    clearForceSwitch = clear_force_switch
    setLodScale = set_lod_scale
    getLodScale = get_lod_scale
    setCenter = set_center
    getCenter = get_center
    showSwitch = show_switch
    hideSwitch = hide_switch
    showAllSwitches = show_all_switches
    hideAllSwitches = hide_all_switches
    isAnyShown = is_any_shown
    verifyChildBounds = verify_child_bounds
    getClassType = get_class_type
    getIns = get_ins
    getOuts = get_outs

class FadeLODNode(LODNode):
    """A Level-of-Detail node with alpha based switching."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    fade_time: float
    fade_state_override: int
    @property
    def fade_bin_name(self) -> str: ...
    @property
    def fade_bin_draw_order(self) -> int: ...
    def __init__(self, name: str) -> None: ...
    def set_fade_time(self, t: float) -> None:
        """set the time taken to complete an LOD switch"""
        ...
    def get_fade_time(self) -> float:
        """get the time taken to complete an LOD switch"""
        ...
    def set_fade_bin(self, name: str, draw_order: int) -> None:
        """Specifies the cull bin and draw order that is assigned to the fading part
        of the geometry during a transition.
        """
        ...
    def get_fade_bin_name(self) -> str:
        """Returns the cull bin that is assigned to the fading part of the geometry
        during a transition.
        """
        ...
    def get_fade_bin_draw_order(self) -> int:
        """Returns the draw order that is assigned (along with the bin name) to the
        fading part of the geometry during a transition.
        """
        ...
    def set_fade_state_override(self, override: int) -> None:
        """Specifies the override value that is applied to the state changes necessary
        to apply the fade effect.  This should be larger than any attrib overrides
        on the fading geometry.
        """
        ...
    def get_fade_state_override(self) -> int:
        """Returns the override value that is applied to the state changes necessary
        to apply the fade effect.  This should be larger than any attrib overrides
        on the fading geometry.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setFadeTime = set_fade_time
    getFadeTime = get_fade_time
    setFadeBin = set_fade_bin
    getFadeBinName = get_fade_bin_name
    getFadeBinDrawOrder = get_fade_bin_draw_order
    setFadeStateOverride = set_fade_state_override
    getFadeStateOverride = get_fade_state_override
    getClassType = get_class_type

class NodeCullCallbackData(CallbackData):
    """This kind of CallbackData is passed to the CallbackObject added to
    CallbackNode:set_cull_callback().
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_trav(self) -> CullTraverser:
        """Returns the CullTraverser in use at the time of the callback.  This object
        contains data that does not change during the traversal, such as the
        DisplayRegion and Camera in use.
        """
        ...
    def get_data(self) -> CullTraverserData:
        """Returns the CullTraverserData in use at the time of the callback.  This
        object contains data that changes at each node of the traversal, such as
        the current node and the current net transform to that node.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getTrav = get_trav
    getData = get_data
    getClassType = get_class_type

class PointLight(LightLensNode):
    """A light originating from a single point in space, and shining in all
    directions.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    specular_color: LVecBase4f
    attenuation: LVecBase3f
    max_distance: float
    point: LPoint3f
    def __init__(self, name: str) -> None: ...
    def set_specular_color(self, color: _Vec4f) -> None:
        """Sets the color of specular highlights generated by the light."""
        ...
    def clear_specular_color(self) -> None:
        """Clears a custom specular color setting, meaning that the specular color
        will now come from the color.
        """
        ...
    def set_attenuation(self, attenuation: _Vec3f) -> None:
        """Sets the terms of the attenuation equation for the light.  These are, in
        order, the constant, linear, and quadratic terms based on the distance from
        the point to the vertex.
        """
        ...
    def get_max_distance(self) -> float:
        """Returns the maximum distance at which the light has any effect, as previously
        specified by set_max_distance.
        """
        ...
    def set_max_distance(self, max_distance: float) -> None:
        """Sets the radius of the light's sphere of influence.  Beyond this distance, the
        light may be attenuated to zero, if this is supported by the shader.
        """
        ...
    def get_point(self) -> LPoint3f:
        """Returns the point in space at which the light is located.  This is local to
        the coordinate space in which the light is assigned, and is usually 0.
        """
        ...
    def set_point(self, point: _Vec3f) -> None:
        """Sets the point in space at which the light is located.  Usually 0."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setSpecularColor = set_specular_color
    clearSpecularColor = clear_specular_color
    setAttenuation = set_attenuation
    getMaxDistance = get_max_distance
    setMaxDistance = set_max_distance
    getPoint = get_point
    setPoint = set_point
    getClassType = get_class_type

class RectangleLight(LightLensNode):
    """This is a type of area light that is an axis aligned rectangle, pointing
    along the Y axis in the positive direction.
    
    @since 1.10.0
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    max_distance: float
    def __init__(self, name: str) -> None: ...
    def get_max_distance(self) -> float:
        """Returns the maximum distance at which the light has any effect, as previously
        specified by set_max_distance.
        """
        ...
    def set_max_distance(self, max_distance: float) -> None:
        """Sets the radius of the light's sphere of influence.  Beyond this distance, the
        light may be attenuated to zero, if this is supported by the shader.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getMaxDistance = get_max_distance
    setMaxDistance = set_max_distance
    getClassType = get_class_type

class SelectiveChildNode(PandaNode):
    """A base class for nodes like LODNode and SequenceNode that select only one
    visible child at a time.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class SequenceNode(SelectiveChildNode, AnimInterface):
    """A node that automatically cycles through rendering each one of its children
    according to its frame rate.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    frame_rate: float
    def __init__(self, name: str) -> None: ...
    def upcast_to_SelectiveChildNode(self) -> SelectiveChildNode: ...
    def upcast_to_AnimInterface(self) -> AnimInterface: ...
    def get_num_frames(self) -> int:
        """Returns the number of frames in the animation.  This is a property of the
        animation and may not be directly adjusted by the user (although it may
        change without warning with certain kinds of animations, since this is a
        virtual method that may be overridden).
        """
        ...
    def set_frame_rate(self, frame_rate: float) -> None:
        """Changes the advertised frame rate of the SequenceNode.  This can be used in
        conjunction with get_play_rate() to change the effective frame rate of the
        node.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToSelectiveChildNode = upcast_to_SelectiveChildNode
    upcastToAnimInterface = upcast_to_AnimInterface
    getNumFrames = get_num_frames
    setFrameRate = set_frame_rate
    getClassType = get_class_type

class ShaderGenerator(TypedReferenceCount):
    """The ShaderGenerator is a device that effectively replaces the classic fixed
    function pipeline with a 'next-gen' fixed function pipeline.  The next-gen
    fixed function pipeline supports features like normal mapping, gloss
    mapping, cartoon lighting, and so forth.  It works by automatically
    generating a shader from a given RenderState.
    
    Currently, there is one ShaderGenerator object per GraphicsStateGuardian.
    It is our intent that in time, people will write classes that derive from
    ShaderGenerator but which yield slightly different results.
    
    The ShaderGenerator owes its existence to the 'Bamboo Team' at Carnegie
    Mellon's Entertainment Technology Center.  This is a group of students who,
    as a semester project, decided that next-gen graphics should be accessible
    to everyone, even if they don't know shader programming.  The group
    consisted of:
    
    Aaron Lo, Programmer Heegun Lee, Programmer Erin Fernandez, Artist/Tester
    Joe Grubb, Artist/Tester Ivan Ortega, Technical Artist/Tester
    
    Thanks to them!
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, gsg: GraphicsStateGuardianBase) -> None:
        """Create a ShaderGenerator.  This has no state, except possibly to cache
        certain results.  The parameter that must be passed is the GSG to which the
        shader generator belongs.
        """
        ...
    @overload
    def __init__(self, __param0: ShaderGenerator) -> None: ...
    def synthesize_shader(self, rs: RenderState, anim: GeomVertexAnimationSpec) -> ShaderAttrib:
        """This is the routine that implements the next-gen fixed function pipeline by
        synthesizing a shader.  It also takes care of setting up any buffers needed
        to produce the requested effects.
        
        Currently supports:
        - flat colors
        - vertex colors
        - lighting
        - normal maps, even multiple
        - gloss maps, but not multiple
        - glow maps, but not multiple
        - materials, but not updates to materials
        - 2D textures
        - all texture stage modes, including combine modes
        - color scale attrib
        - light ramps (for cartoon shading)
        - shadow mapping
        - most texgen modes
        - texmatrix
        - 1D/2D/3D textures, cube textures, 2D tex arrays
        - linear/exp/exp2 fog
        - animation
        
        Potential optimizations
        - omit attenuation calculations if attenuation off
        """
        ...
    def rehash_generated_shaders(self) -> None:
        """Rehashes all the states with generated shaders, removing the ones that are
        no longer fresh.
        
        Call this if certain state has changed in such a way as to require a rerun
        of the shader generator.  This should be rare because in most cases, the
        shader generator will automatically regenerate shaders as necessary.
        
        @since 1.10.0
        """
        ...
    def clear_generated_shaders(self) -> None:
        """Removes all previously generated shaders, requiring all shaders to be
        regenerated.  Does not clear cache of compiled shaders.
        
        @since 1.10.0
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    synthesizeShader = synthesize_shader
    rehashGeneratedShaders = rehash_generated_shaders
    clearGeneratedShaders = clear_generated_shaders
    getClassType = get_class_type

class SphereLight(PointLight):
    """A sphere light is like a point light, except that it represents a sphere
    with a radius, rather than being an infinitely thin point in space.
    
    @since 1.10.0
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    radius: float
    def __init__(self, name: str) -> None: ...
    def get_radius(self) -> float:
        """Returns the radius of the sphere."""
        ...
    def set_radius(self, radius: float) -> None:
        """Sets the radius of the sphere."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getRadius = get_radius
    setRadius = set_radius
    getClassType = get_class_type

class Spotlight(LightLensNode):
    """A light originating from a single point in space, and shining in a
    particular direction, with a cone-shaped falloff.
    
    The Spotlight frustum is defined using a Lens, so it can have any of the
    properties that a camera lens can have.
    
    Note that the class is named Spotlight instead of SpotLight, because
    "spotlight" is a single English word, instead of two words.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    exponent: float
    specular_color: LVecBase4f
    attenuation: LVecBase3f
    max_distance: float
    def __init__(self, name: str) -> None: ...
    def set_exponent(self, exponent: float) -> None:
        """Sets the exponent that controls the amount of light falloff from the center
        of the spotlight.  The light is attenuated by the cosine of the angle
        between the direction of the light and the direction of the point being
        lighted, raised to the power of this exponent.  Thus, higher exponents
        result in a more focused light source, regardless of the field-of-view of
        the lens.
        """
        ...
    def set_specular_color(self, color: _Vec4f) -> None:
        """Sets the color of specular highlights generated by the light."""
        ...
    def clear_specular_color(self) -> None:
        """Clears a custom specular color setting, meaning that the specular color
        will now come from the color.
        """
        ...
    def set_attenuation(self, attenuation: _Vec3f) -> None:
        """Sets the terms of the attenuation equation for the light.  These are, in
        order, the constant, linear, and quadratic terms based on the distance from
        the point to the vertex.
        """
        ...
    def get_max_distance(self) -> float:
        """Returns the maximum distance at which the light has any effect, as previously
        specified by set_max_distance.
        """
        ...
    def set_max_distance(self, max_distance: float) -> None:
        """Sets the radius of the light's sphere of influence.  Beyond this distance, the
        light may be attenuated to zero, if this is supported by the shader.
        """
        ...
    @staticmethod
    def make_spot(pixel_width: int, full_radius: float, fg: _Vec4f, bg: _Vec4f) -> Texture:
        """Returns a newly-generated Texture that renders a circular spot image as
        might be cast from the spotlight.  This may be projected onto target
        geometry (for instance, via NodePath::project_texture()) instead of
        actually enabling the light itself, as a cheesy way to make a high-
        resolution spot appear on the geometry.
        
        pixel_width specifies the height and width of the new texture in pixels,
        full_radius is a value in the range 0..1 that indicates the relative size
        of the fully bright center spot, and fg and bg are the colors of the
        interior and exterior of the spot, respectively.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setExponent = set_exponent
    setSpecularColor = set_specular_color
    clearSpecularColor = clear_specular_color
    setAttenuation = set_attenuation
    getMaxDistance = get_max_distance
    setMaxDistance = set_max_distance
    makeSpot = make_spot
    getClassType = get_class_type

class SwitchNode(SelectiveChildNode):
    """A node that renders only one of its children, according to the user's
    indication.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    visible_child: int
    def __init__(self, name: str) -> None: ...
    def set_visible_child(self, index: int) -> None:
        """Specifies the particular child of this node, by index, that will be
        visible.
        """
        ...
    def get_visible_child(self) -> int:
        """Returns the index of the child that should be visible."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setVisibleChild = set_visible_child
    getVisibleChild = get_visible_child
    getClassType = get_class_type

class UvScrollNode(PandaNode):
    """This node is placed at key points within the scene graph to animate uvs."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    u_speed: float
    v_speed: float
    w_speed: float
    r_speed: float
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, name: str, u_speed: float, v_speed: float, w_speed: float, r_speed: float) -> None: ...
    def set_u_speed(self, u_speed: float) -> None: ...
    def set_v_speed(self, v_speed: float) -> None: ...
    def set_w_speed(self, w_speed: float) -> None: ...
    def set_r_speed(self, r_speed: float) -> None: ...
    def get_u_speed(self) -> float: ...
    def get_v_speed(self) -> float: ...
    def get_w_speed(self) -> float: ...
    def get_r_speed(self) -> float: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setUSpeed = set_u_speed
    setVSpeed = set_v_speed
    setWSpeed = set_w_speed
    setRSpeed = set_r_speed
    getUSpeed = get_u_speed
    getVSpeed = get_v_speed
    getWSpeed = get_w_speed
    getRSpeed = get_r_speed
    getClassType = get_class_type

class SceneGraphAnalyzer:
    """A handy class that can scrub over a scene graph and collect interesting
    statistics on it.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    LM_lowest: ClassVar[Literal[0]]
    LM_highest: ClassVar[Literal[1]]
    LM_all: ClassVar[Literal[2]]
    LM_none: ClassVar[Literal[3]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: SceneGraphAnalyzer) -> None: ...
    def set_lod_mode(self, lod_mode: _SceneGraphAnalyzer_LodMode) -> None:
        """Specifies the mode in which LODNodes are analyzed."""
        ...
    def get_lod_mode(self, lod_mode: _SceneGraphAnalyzer_LodMode) -> _SceneGraphAnalyzer_LodMode:
        """Returns the mode in which LODNodes are analyzed."""
        ...
    def clear(self) -> None:
        """Resets all of the data in the analyzer in preparation for a new run."""
        ...
    def add_node(self, node: PandaNode) -> None:
        """Adds a new node to the set of data for analysis.  Normally, this would only
        be called once, and passed the top of the scene graph, but it's possible to
        repeatedly pass in subgraphs to get an analysis of all the graphs together.
        """
        ...
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Describes all the data collected."""
        ...
    def get_num_nodes(self) -> int: ...
    def get_num_instances(self) -> int: ...
    def get_num_transforms(self) -> int: ...
    def get_num_nodes_with_attribs(self) -> int: ...
    def get_num_lod_nodes(self) -> int: ...
    def get_num_geom_nodes(self) -> int: ...
    def get_num_geoms(self) -> int: ...
    def get_num_geom_vertex_datas(self) -> int: ...
    def get_num_geom_vertex_formats(self) -> int: ...
    def get_vertex_data_size(self) -> int: ...
    def get_num_vertices(self) -> int: ...
    def get_num_normals(self) -> int: ...
    def get_num_colors(self) -> int: ...
    def get_num_texcoords(self) -> int: ...
    def get_num_tris(self) -> int: ...
    def get_num_lines(self) -> int: ...
    def get_num_points(self) -> int: ...
    def get_num_patches(self) -> int: ...
    def get_num_individual_tris(self) -> int: ...
    def get_num_tristrips(self) -> int: ...
    def get_num_triangles_in_strips(self) -> int: ...
    def get_num_trifans(self) -> int: ...
    def get_num_triangles_in_fans(self) -> int: ...
    def get_num_vertices_in_patches(self) -> int: ...
    def get_texture_bytes(self) -> int: ...
    def get_num_long_normals(self) -> int: ...
    def get_num_short_normals(self) -> int: ...
    def get_total_normal_length(self) -> float: ...
    setLodMode = set_lod_mode
    getLodMode = get_lod_mode
    addNode = add_node
    getNumNodes = get_num_nodes
    getNumInstances = get_num_instances
    getNumTransforms = get_num_transforms
    getNumNodesWithAttribs = get_num_nodes_with_attribs
    getNumLodNodes = get_num_lod_nodes
    getNumGeomNodes = get_num_geom_nodes
    getNumGeoms = get_num_geoms
    getNumGeomVertexDatas = get_num_geom_vertex_datas
    getNumGeomVertexFormats = get_num_geom_vertex_formats
    getVertexDataSize = get_vertex_data_size
    getNumVertices = get_num_vertices
    getNumNormals = get_num_normals
    getNumColors = get_num_colors
    getNumTexcoords = get_num_texcoords
    getNumTris = get_num_tris
    getNumLines = get_num_lines
    getNumPoints = get_num_points
    getNumPatches = get_num_patches
    getNumIndividualTris = get_num_individual_tris
    getNumTristrips = get_num_tristrips
    getNumTrianglesInStrips = get_num_triangles_in_strips
    getNumTrifans = get_num_trifans
    getNumTrianglesInFans = get_num_triangles_in_fans
    getNumVerticesInPatches = get_num_vertices_in_patches
    getTextureBytes = get_texture_bytes
    getNumLongNormals = get_num_long_normals
    getNumShortNormals = get_num_short_normals
    getTotalNormalLength = get_total_normal_length
    LMLowest = LM_lowest
    LMHighest = LM_highest
    LMAll = LM_all
    LMNone = LM_none

LNT_pop: Literal[0]
LNT_fade: Literal[1]
LNTPop = LNT_pop
LNTFade = LNT_fade
