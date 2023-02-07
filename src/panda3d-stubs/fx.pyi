from typing import Any, ClassVar, overload
from typing_extensions import Self

from panda3d._typing import Vec4Like
from panda3d.core._display import DisplayRegion, GraphicsEngine, GraphicsOutput
from panda3d.core._gobj import Lens
from panda3d.core._linmath import LColor
from panda3d.core._pgraph import GeomNode, NodePath, PandaNode
from panda3d.core._pnmimage import PfmFile
from panda3d.core._putil import UpdateSeq

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

    def __init__(self) -> None: ...

class FisheyeLens(Lens):
    """A fisheye lens.  This nonlinear lens introduces a spherical distortion to
    the image, which is minimal at small angles from the lens, and increases at
    larger angles from the lens.  The field of view may extend to 360 degrees.
    """

    def __init__(self) -> None: ...

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

    def __init__(self, name: str = ...) -> None: ...
    def set_projector(self, projector: NodePath) -> None:
        """Specifies the LensNode that is to serve as the projector for this screen.
        The relative position of the LensNode to the ProjectionScreen, as well as
        the properties of the lens associated with the LensNode, determines the
        UV's that will be assigned to the geometry within the ProjectionScreen.

        The NodePath must refer to a LensNode (or a Camera).
        """
    def get_projector(self) -> NodePath:
        """Returns the NodePath to the LensNode that is to serve as the projector for
        this screen, or empty if no projector is associated.
        """
    def clear_undist_lut(self) -> None:
        """Removes the distortion lookup table from the projector, if specified."""
    def set_undist_lut(self, undist_lut: PfmFile) -> None:
        """Applies a distortion lookup table to the projector.  This mapping warps the
        lens effect by passing each ray through an indirection table: the point
        (u,v) in the indicated lookup table stores the actual (u,v) that the lens
        produces.

        This does not affect the operation of generate_screen().
        """
    def has_undist_lut(self) -> bool:
        """Returns true if a valid distortion lookup table was provided via
        set_undist_lut(), false otherwise.
        """
    def get_undist_lut(self) -> PfmFile:
        """Returns the distortion lookup table provided via set_undist_lut(), if any."""
    def generate_screen(
        self, projector: NodePath, screen_name: str, num_x_verts: int, num_y_verts: int, distance: float, fill_ratio: float
    ) -> GeomNode:
        """Synthesizes a polygon mesh based on the projection area of the indicated
        projector.  This generates and returns a new GeomNode but does not
        automatically parent it to the ProjectionScreen node; see
        regenerate_screen().

        The specified projector need not be the same as the projector given to the
        ProjectionScreen with set_projector() (although this is often what you
        want).

        num_x_verts and num_y_verts specify the number of vertices to make in the
        grid across the horizontal and vertical dimension of the projector,
        respectively; distance represents the approximate distance of the screen
        from the lens center.

        The fill_ratio parameter specifies the fraction of the image to cover.  If
        it is 1.0, the entire image is shown full-size; if it is 0.9, 10% of the
        image around the edges is not part of the grid (and the grid is drawn
        smaller by the same 10%).  This is intended to work around graphics drivers
        that tend to show dark edges or other unsatisfactory artifacts around the
        edges of textures: render the texture larger than necessary by a certain
        fraction, and make the screen smaller by the inverse fraction.
        """
    def regenerate_screen(
        self, projector: NodePath, screen_name: str, num_x_verts: int, num_y_verts: int, distance: float, fill_ratio: float
    ) -> None:
        """Removes all the children from the ProjectionScreen node, and adds the newly
        generated child returned by generate_screen().
        """
    def make_flat_mesh(self, this_np: NodePath, camera: NodePath) -> PandaNode:
        """Generates a deep copy of the hierarchy at the ProjectionScreen node and
        below, with vertices flattened into two dimensions as if they were seen by
        the indicated camera node.

        This is useful for rendering an image as seen through a non-linear lens.
        The resulting mesh will have vertices in the range [-1, 1] in both x and y,
        and may be then rendered with an ordinary orthographic lens, to generate
        the effect of seeing the image through the specified non-linear lens.

        The returned node has no parent; it is up to the caller to parent it
        somewhere or store it so that it does not get dereferenced and deleted.
        """
    def set_texcoord_name(self, texcoord_name: str) -> None:
        """Specifies the name of the texture coordinates that are generated by this
        particular ProjectionScreen.  This can be used in the presence of
        multitexturing to compute the UV's for just a subset of all of the active
        stages of the multitexture pipeline.
        """
    def get_texcoord_name(self) -> str:
        """Returns the name of the texture coordinates that will be generated by this
        particular ProjectionScreen, as set by set_texcoord_name().
        """
    def set_invert_uvs(self, invert_uvs: bool) -> None:
        """Some OpenGL graphics drivers are known to invert the framebuffer image when
        they copy it to texture.  (This is arguably a problem with the OpenGL spec,
        which seems to be unclear about the proper ordering of pixels in this
        operation.)

        In any case, set this true to compensate for this effect by inverting the
        UV's of the projection screen.  The default is taken from the Configrc
        variable project-invert-uvs.
        """
    def get_invert_uvs(self) -> bool:
        """Returns whether this screen is compensating for a graphics driver inverting
        the framebuffer image.  See set_invert_uvs().
        """
    def set_texcoord_3d(self, texcoord_3d: bool) -> None:
        """Set this true to force 3-D texture coordinates to be created for the
        geometry.  When this is true and the geometry has only 2-D texture
        coordinates, those texture coordinates are dumped in favor of 3-D
        coordinates.  When this is false, whatever texture coordinates already
        exist are preserved as-is.
        """
    def get_texcoord_3d(self) -> bool:
        """See set_texcoord_3d()."""
    def set_vignette_on(self, vignette_on: bool) -> None:
        """Specifies whether vertex-based vignetting should be on.  When this is
        enabled, vertex color will be set on the screen vertices to color the
        screen two distinct colors, usually white and black, for the parts of the
        screen in front of and outside the lens' frustum, respectively.  When this
        is not enabled, the screen color will be left alone.

        This effect generally looks terrible, but it does at least make the
        boundaries of the lens clear.
        """
    def get_vignette_on(self) -> bool:
        """Returns true if vertex-based vignetting is on, false otherwise.  See
        set_vignette_on().
        """
    def set_vignette_color(self, vignette_color: Vec4Like) -> None:
        """Specifies the color the screen will be painted at the portions outside of
        the lens' frustum; i.e.  where the lens can't see it or illuminate it.
        This color is only used if the vignette_on flag is true; see
        set_vignette_on().
        """
    def get_vignette_color(self) -> LColor:
        """Returns the color the screen will be painted at the portions outside of the
        lens' frustum.  See set_vignette_color().
        """
    def set_frame_color(self, frame_color: Vec4Like) -> None:
        """Specifies the color the screen will be painted at the portions outside of
        the lens' frustum; i.e.  where the lens can't see it or illuminate it.
        This color is only used if the vignette_on flag is true; see
        set_vignette_on().
        """
    def get_frame_color(self) -> LColor:
        """Returns the color the screen will be painted at the portions outside of the
        lens' frustum.  See set_frame_color().
        """
    def set_auto_recompute(self, auto_recompute: bool) -> None:
        """Sets the auto_recompute flag.  When this is true, the ProjectionScreen will
        always be recomputed if necessary before the frame is drawn; when it is
        false, an explicit call to recompute_if_stale() may be required.
        """
    def get_auto_recompute(self) -> bool:
        """Returns the auto_recompute flag.  When this is true, the ProjectionScreen
        will always be recomputed if necessary before the frame is drawn; when it
        is false, an explicit call to recompute_if_stale() may be required.
        """
    def recompute(self) -> None:
        """Recomputes all the UV's for geometry below the ProjectionScreen node, as if
        the texture were projected from the associated projector.

        This function is normally called automatically whenever the relevant
        properties change, so it should not normally need to be called directly by
        the user.  However, it does no harm to call this if there is any doubt.
        """
    def get_last_screen(self) -> UpdateSeq:
        """Returns an UpdateSeq corresponding to the last time a screen mesh was
        generated for the ProjectionScreen.  Each time generate_screen() is called,
        this number is incremented; this allows other objects (like
        NonlinearImager) to know when they need to recompute themselves.
        """
    def recompute_if_stale(self, this_np: NodePath = ...) -> bool:
        """Calls recompute() only if the relative transform between the
        ProjectionScreen and the projector has changed, or if any other relevant
        property has changed.  Returns true if recomputed, false otherwise.
        """
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
    def __init__(self, __param0: NonlinearImager = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @overload
    def add_screen(self, screen: ProjectionScreen) -> int:
        """`(self, screen: NodePath, name: str)`:
        Adds a new ProjectionScreen to the list of screens that will be processed
        by the NonlinearImager.  Each ProjectionScreen represents a view into the
        world.  It must be based on a linear camera (or whatever kind of camera is
        respected by the graphics engine).

        Each ProjectionScreen object should already have some screen geometry
        created.

        As each frame is rendered, an offscreen image will be rendered from the
        source camera associated with each ProjectionScreen, and the resulting
        image will be applied to the screen geometry.

        The return value is the index number of the new screen.

        `(self, screen: ProjectionScreen)`:
        This version of this method is deprecated and will soon be removed.  Use
        the version that takes two parameters instead.

        @deprecated Use the version that takes two parameters instead.
        """
    @overload
    def add_screen(self, screen: NodePath, name: str) -> int: ...
    def find_screen(self, screen: NodePath) -> int:
        """Returns the index number of the first appearance of the indicated screen
        within the imager's list, or -1 if it does not appear.
        """
    def remove_screen(self, index: int) -> None:
        """Removes the screen with the indicated index number from the imager."""
    def remove_all_screens(self) -> None:
        """Removes all screens from the imager."""
    def get_num_screens(self) -> int:
        """Returns the number of screens that have been added to the imager."""
    def get_screen(self, index: int) -> NodePath:
        """Returns the nth screen that has been added to the imager."""
    def get_buffer(self, index: int) -> GraphicsOutput:
        """Returns the offscreen buffer that is automatically created for the nth
        projection screen.  This may return NULL if the screen is inactive or if it
        has not been rendered yet.
        """
    def set_texture_size(self, index: int, width: int, height: int) -> None:
        """Sets the width and height of the texture used to render the scene for the
        indicated screen.  This must be less than or equal to the window size, and
        it should be a power of two.

        In general, the larger the texture, the greater the detail of the rendered
        scene.
        """
    def set_source_camera(self, index: int, source_camera: NodePath) -> None:
        """Specifies the camera that will be used to render the image for this
        particular screen.

        The parameter must be a NodePath whose node is a Camera.  The camera itself
        indicates the scene that is to be rendered.
        """
    def set_screen_active(self, index: int, active: bool) -> None:
        """Sets the active flag on the indicated screen.  If the active flag is true,
        the screen will be used; otherwise, it will not appear.
        """
    def get_screen_active(self, index: int) -> bool:
        """Returns the active flag on the indicated screen."""
    def add_viewer(self, dr: DisplayRegion) -> int:
        """Adds the indicated DisplayRegion as a viewer into the NonlinearImager room.
        The camera associated with the DisplayRegion at the time add_viewer() is
        called is used as the initial viewer camera; it may have a nonlinear lens,
        like a fisheye or cylindrical lens.

        This sets up a special scene graph for this DisplayRegion alone and sets up
        the DisplayRegion with a specialty camera.  If future changes to the camera
        are desired, you should use the set_viewer_camera() interface.

        All viewers must share the same GraphicsEngine.

        The return value is the index of the new viewer.
        """
    def find_viewer(self, dr: DisplayRegion) -> int:
        """Returns the index number of the indicated DisplayRegion within the list of
        viewers, or -1 if it is not found.
        """
    def remove_viewer(self, index: int) -> None:
        """Removes the viewer with the indicated index number from the imager."""
    def remove_all_viewers(self) -> None:
        """Removes all viewers from the imager."""
    def set_viewer_camera(self, index: int, viewer_camera: NodePath) -> None:
        """Specifies the LensNode that is to serve as the viewer for this screen.  The
        relative position of the LensNode to the NonlinearImager, as well as the
        properties of the lens associated with the LensNode, determines the UV's
        that will be assigned to the geometry within the NonlinearImager.

        It is not necessary to call this except to change the camera after a viewer
        has been added, since the default is to use whatever camera is associated
        with the DisplayRegion at the time the viewer is added.

        The NodePath must refer to a LensNode (or a Camera).
        """
    def get_viewer_camera(self, index: int) -> NodePath:
        """Returns the NodePath to the LensNode that is to serve as nth viewer for
        this screen.
        """
    def get_viewer_scene(self, index: int) -> NodePath:
        """Returns a pointer to the root node of the internal scene graph for the nth
        viewer, which is used to render all of the screen meshes for this viewer.

        This is the scene graph in which the screen meshes within the dark room
        have been flattened into the appropriate transformation according to the
        viewer's lens properties (and position relative to the screens).  It is
        this scene graph that is finally rendered to the window.
        """
    def get_num_viewers(self) -> int:
        """Returns the number of viewers that have been added to the imager."""
    def get_viewer(self, index: int) -> DisplayRegion:
        """Returns the nth viewer's DisplayRegion that has been added to the imager."""
    def get_dark_room(self) -> NodePath:
        """Returns the NodePath to the root of the dark room scene.  This is the scene
        in which all of the ProjectionScreens and the viewer cameras reside.  It's
        a standalone scene with a few projection screens arranged artfully around
        one or more viewers; it's so named because it's a little virtual theater.

        Normally this scene is not rendered directly; it only exists as an abstract
        concept, and to define the relation between the ProjectionScreens and the
        viewers.  But it may be rendered to help visualize the NonlinearImager's
        behavior.
        """
    def get_graphics_engine(self) -> GraphicsEngine:
        """Returns the GraphicsEngine that all of the viewers added to the
        NonlinearImager have in common.
        """
    def recompute(self) -> None:
        """Forces a regeneration of all the mesh objects, etc."""
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

    def __init__(self) -> None: ...

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

    def __init__(self) -> None: ...
