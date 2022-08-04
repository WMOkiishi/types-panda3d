from typing import Any, ClassVar, TypeAlias, overload
from panda3d.core import (
    ConfigVariableColor,
    DisplayRegion,
    GeomNode,
    GraphicsEngine,
    GraphicsOutput,
    LMatrix4f,
    LVecBase4f,
    Lens,
    NodePath,
    PandaNode,
    PfmFile,
    TypeHandle,
    UnalignedLVecBase4f,
    UpdateSeq,
)

_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor

class CylindricalLens(Lens):
    """A cylindrical lens.  This is the kind of lens generally used for extremely
    wide panoramic shots.  It behaves like a normal perspective lens in the
    vertical direction, but it is non-linear in the horizontal dimension: a
    point on the film corresponds to a point in space in linear proportion to
    its angle to the camera, not to its straight-line distance from the center.
    
    This allows up to 360 degree lenses in the horizontal dimension, with
    relatively little distortion.  The distortion is not very apparent between
    two relatively nearby points on the film, but it becomes increasingly
    evident as you compare points widely spaced on the film.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class FisheyeLens(Lens):
    """A fisheye lens.  This nonlinear lens introduces a spherical distortion to
    the image, which is minimal at small angles from the lens, and increases at
    larger angles from the lens.  The field of view may extend to 360 degrees.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class ProjectionScreen(PandaNode):
    """A ProjectionScreen implements a simple system for projective texturing.
    The ProjectionScreen node is the parent of a hierarchy of geometry that is
    considered a "screen"; the ProjectionScreen will automatically recompute
    all the UV's (for a particular texture stage) on its subordinate geometry
    according to the relative position and lens parameters of the indicated
    LensNode.
    
    All this does is recompute UV's; the caller is responsible for applying the
    appropriate texture(s) to the geometry.
    
    This does not take advantage of any hardware-assisted projective texturing;
    all of the UV's are computed in the CPU.  (Use NodePath::project_texture()
    to enable hardware-assisted projective texturing.)  However, the
    ProjectionScreen interface does support any kind of lens, linear or
    nonlinear, that might be defined using the Lens interface, including
    fisheye and cylindrical lenses.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str = ...) -> None: ...
    def set_projector(self, projector: NodePath) -> None: ...
    def get_projector(self) -> NodePath: ...
    def clear_undist_lut(self) -> None: ...
    def set_undist_lut(self, undist_lut: PfmFile) -> None: ...
    def has_undist_lut(self) -> bool: ...
    def get_undist_lut(self) -> PfmFile: ...
    def generate_screen(self, projector: NodePath, screen_name: str, num_x_verts: int, num_y_verts: int, distance: float, fill_ratio: float) -> GeomNode: ...
    def regenerate_screen(self, projector: NodePath, screen_name: str, num_x_verts: int, num_y_verts: int, distance: float, fill_ratio: float) -> None: ...
    def make_flat_mesh(self, this_np: NodePath, camera: NodePath) -> PandaNode: ...
    def set_texcoord_name(self, texcoord_name: str) -> None: ...
    def get_texcoord_name(self) -> str: ...
    def set_invert_uvs(self, invert_uvs: bool) -> None: ...
    def get_invert_uvs(self) -> bool: ...
    def set_texcoord_3d(self, texcoord_3d: bool) -> None: ...
    def get_texcoord_3d(self) -> bool: ...
    def set_vignette_on(self, vignette_on: bool) -> None: ...
    def get_vignette_on(self) -> bool: ...
    def set_vignette_color(self, vignette_color: _Vec4f) -> None: ...
    def get_vignette_color(self) -> LVecBase4f: ...
    def set_frame_color(self, frame_color: _Vec4f) -> None: ...
    def get_frame_color(self) -> LVecBase4f: ...
    def set_auto_recompute(self, auto_recompute: bool) -> None: ...
    def get_auto_recompute(self) -> bool: ...
    def recompute(self) -> None: ...
    def get_last_screen(self) -> UpdateSeq: ...
    @overload
    def recompute_if_stale(self) -> bool: ...
    @overload
    def recompute_if_stale(self, this_np: NodePath) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setProjector = set_projector
    getProjector = get_projector
    clearUndistLut = clear_undist_lut
    setUndistLut = set_undist_lut
    hasUndistLut = has_undist_lut
    getUndistLut = get_undist_lut
    generateScreen = generate_screen
    regenerateScreen = regenerate_screen
    makeFlatMesh = make_flat_mesh
    setTexcoordName = set_texcoord_name
    getTexcoordName = get_texcoord_name
    setInvertUvs = set_invert_uvs
    getInvertUvs = get_invert_uvs
    setTexcoord3d = set_texcoord_3d
    getTexcoord3d = get_texcoord_3d
    setVignetteOn = set_vignette_on
    getVignetteOn = get_vignette_on
    setVignetteColor = set_vignette_color
    getVignetteColor = get_vignette_color
    setFrameColor = set_frame_color
    getFrameColor = get_frame_color
    setAutoRecompute = set_auto_recompute
    getAutoRecompute = get_auto_recompute
    getLastScreen = get_last_screen
    recomputeIfStale = recompute_if_stale
    getClassType = get_class_type

class NonlinearImager:
    """This class object combines the rendered output of a 3-d from one or more
    linear (e.g.  perspective) cameras, as seen through a single, possibly
    nonlinear camera.
    
    This can be used to generate real-time imagery of a 3-d scene using a
    nonlinear camera, for instance a fisheye camera, even though the underlying
    graphics engine may only support linear cameras.  It can also pre-distort
    imagery to compensate for off-axis projectors, and/or curved screens of any
    complexity.
    
    
    
    A NonlinearImager may be visualized as a dark room into which a number of
    projection screens have been placed, of arbitrary size and shape and at any
    arbitrary position and orientation to each other.  Onto each of these
    screens is projected the view as seen by a normal perspective camera that
    exists in the world (that is, under render).
    
    There also exist in the room one or more (possibly nonlinear) cameras,
    called viewers, that observe these screens.  The image of the projection
    screens seen by each viewer is finally displayed on the viewer's associated
    DisplayRegion.  By placing the viewer(s) appropriately relative to the
    screens, and by choosing suitable lens properties for the viewer(s), you
    can achieve a wide variety of distortion effects.
    
    
    
    There are several different LensNode (Camera) objects involved at each
    stage in the process.  To help keep them all straight, different words are
    used to refer to each different kind of Camera used within this object.
    The camera(s) under render, that capture the original view of the world to
    be projected onto the screens, are called source cameras, and are set per
    screen via set_source_camera().  The LensNode that is associated with each
    screen to project the image as seen from the screen's source camera is
    called a projector; these are set via the ProjectionScreen::set_projector()
    interface.  Finally, the cameras that view the whole configuration of
    screens are called viewers; each of these is associated with a
    DisplayRegion, and they are set via set_viewer_camera().
    
    Of all these lenses, only the source cameras must use linear (that is,
    perspective or orthographic) lenses.  The projectors and viewers may be any
    arbitrary lens, linear or otherwise.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: NonlinearImager) -> None: ...
    @overload
    def add_screen(self, screen: ProjectionScreen) -> int: ...
    @overload
    def add_screen(self, screen: NodePath, name: str) -> int: ...
    def find_screen(self, screen: NodePath) -> int: ...
    def remove_screen(self, index: int) -> None: ...
    def remove_all_screens(self) -> None: ...
    def get_num_screens(self) -> int: ...
    def get_screen(self, index: int) -> NodePath: ...
    def get_buffer(self, index: int) -> GraphicsOutput: ...
    def set_texture_size(self, index: int, width: int, height: int) -> None: ...
    def set_source_camera(self, index: int, source_camera: NodePath) -> None: ...
    def set_screen_active(self, index: int, active: bool) -> None: ...
    def get_screen_active(self, index: int) -> bool: ...
    def add_viewer(self, dr: DisplayRegion) -> int: ...
    def find_viewer(self, dr: DisplayRegion) -> int: ...
    def remove_viewer(self, index: int) -> None: ...
    def remove_all_viewers(self) -> None: ...
    def set_viewer_camera(self, index: int, viewer_camera: NodePath) -> None: ...
    def get_viewer_camera(self, index: int) -> NodePath: ...
    def get_viewer_scene(self, index: int) -> NodePath: ...
    def get_num_viewers(self) -> int: ...
    def get_viewer(self, index: int) -> DisplayRegion: ...
    def get_dark_room(self) -> NodePath: ...
    def get_graphics_engine(self) -> GraphicsEngine: ...
    def recompute(self) -> None: ...
    def get_screens(self) -> tuple[NodePath, ...]: ...
    def get_buffers(self) -> tuple[GraphicsOutput, ...]: ...
    def get_viewers(self) -> tuple[DisplayRegion, ...]: ...
    addScreen = add_screen
    findScreen = find_screen
    removeScreen = remove_screen
    removeAllScreens = remove_all_screens
    getNumScreens = get_num_screens
    getScreen = get_screen
    getBuffer = get_buffer
    setTextureSize = set_texture_size
    setSourceCamera = set_source_camera
    setScreenActive = set_screen_active
    getScreenActive = get_screen_active
    addViewer = add_viewer
    findViewer = find_viewer
    removeViewer = remove_viewer
    removeAllViewers = remove_all_viewers
    setViewerCamera = set_viewer_camera
    getViewerCamera = get_viewer_camera
    getViewerScene = get_viewer_scene
    getNumViewers = get_num_viewers
    getViewer = get_viewer
    getDarkRoom = get_dark_room
    getGraphicsEngine = get_graphics_engine
    getScreens = get_screens
    getBuffers = get_buffers
    getViewers = get_viewers

class OSphereLens(Lens):
    """A OSphereLens is a special nonlinear lens that doesn't correspond to any
    real physical lenses.  It's primarily useful for generating 360-degree
    wraparound images while avoiding the distortion associated with fisheye
    images.
    
    A OSphereLens is similar to a Cylindrical lens and PSphereLens, except that
    it is orthographic in the vertical direction.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class PSphereLens(Lens):
    """A PSphereLens is a special nonlinear lens that doesn't correspond to any
    real physical lenses.  It's primarily useful for generating 360-degree
    wraparound images while avoiding the distortion associated with fisheye
    images.
    
    A PSphereLens is similar to a cylindrical lens, except it is also curved in
    the vertical direction.  This allows it to extend to both poles in the
    vertical direction.  The mapping is similar to what many modeling packages
    call a sphere mapping: the x coordinate is proportional to azimuth, while
    the y coordinate is proportional to altitude.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type
