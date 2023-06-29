from _typeshed import StrOrBytesPath
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import DoubleVec2Like, DoubleVec3Like, Vec2Like, Vec3Like, Vec4Like
from panda3d.core._audio import AudioSound
from panda3d.core._display import DisplayRegion, GraphicsOutput
from panda3d.core._dtoolbase import TypedObject
from panda3d.core._express import Namable
from panda3d.core._gobj import InternalName, Lens, Texture, TextureStage, VertexTransform
from panda3d.core._linmath import LColor, LPoint3, LVecBase2, LVector3, LVertex
from panda3d.core._movies import MovieVideo, MovieVideoCursor
from panda3d.core._pgraph import CullTraverser, GeomNode, NodePath, PandaNode, RenderState, TransformState
from panda3d.core._pnmimage import PfmFile, PNMFileType, PNMImage
from panda3d.core._putil import ClockObject, DrawMask
from panda3d.core._text import TextNode

_ClockObject_Mode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
_PfmVizzer_ColumnType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
_PfmVizzer_MeshFace: TypeAlias = Literal[1, 2, 3]

class CardMaker(Namable):
    """This class generates 2-d "cards", that is, rectangular polygons,
    particularly useful for showing textures etc.  in the 2-d scene graph.
    """

    @overload
    def __init__(self, __param0: CardMaker) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def reset(self) -> None:
        """Resets all the parameters to their initial defaults."""
    @overload
    def set_uv_range(self, tex: Texture) -> None:
        """`(self, ll: LTexCoord, ur: LTexCoord)`; `(self, ll: LTexCoord, lr: LTexCoord, ur: LTexCoord, ul: LTexCoord)`; `(self, ll: LTexCoord3, lr: LTexCoord3, ur: LTexCoord3, ul: LTexCoord3)`; `(self, x: LVector4, y: LVector4, z: LVector4)`:
        Sets the range of UV's that will be applied to the vertices.  If
        set_has_uvs() is true (as it is by default), the vertices will be generated
        with the indicated range of UV's, which will be useful if a texture is
        applied.

        `(self, tex: Texture)`:
        Sets the range of UV's that will be applied to the vertices appropriately
        to show the non-pad region of the texture.
        """
    @overload
    def set_uv_range(self, ll: Vec2Like, ur: Vec2Like) -> None: ...
    @overload
    def set_uv_range(self, x: Vec4Like, y: Vec4Like, z: Vec4Like) -> None: ...
    @overload
    def set_uv_range(self, ll: Vec2Like, lr: Vec2Like, ur: Vec2Like, ul: Vec2Like) -> None: ...
    @overload
    def set_uv_range(self, ll: Vec3Like, lr: Vec3Like, ur: Vec3Like, ul: Vec3Like) -> None: ...
    def set_uv_range_cube(self, face: int) -> None:
        """Sets the range of UV's that will be applied to the vertices appropriately
        for a cube-map face.
        """
    def set_has_uvs(self, flag: bool) -> None:
        """Sets the flag indicating whether vertices will be generated with UV's or
        not.
        """
    def set_has_3d_uvs(self, flag: bool) -> None:
        """Sets the flag indicating whether vertices will be generated with
        3-component UVW's (true) or 2-component UV's (the default, false).
        Normally, this will be implicitly set by setting the uv_range.
        """
    @overload
    def set_frame(self, frame: Vec4Like) -> None:
        """Sets the size of the card."""
    @overload
    def set_frame(self, ll: Vec3Like, lr: Vec3Like, ur: Vec3Like, ul: Vec3Like) -> None: ...
    @overload
    def set_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def set_frame_fullscreen_quad(self) -> None:
        """Sets the card to (-1,1,-1,1), which is appropriate if you plan to parent it
        to render2d and use it as a fullscreen quad.
        """
    @overload
    def set_color(self, color: Vec4Like) -> None:
        """Sets the color of the card."""
    @overload
    def set_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def set_has_normals(self, flag: bool) -> None:
        """Sets the flag indicating whether vertices will be generated with normals or
        not.  Normals are required if you intend to enable lighting on the card,
        but are just wasted space and bandwidth otherwise, so there is a (slight)
        optimization for disabling them.  If enabled, the normals will be generated
        perpendicular to the card's face.
        """
    def set_source_geometry(self, node: PandaNode, frame: Vec4Like) -> None:
        """Sets a node that will be copied (and scaled and translated) to generate the
        frame, instead of generating a new polygon.  The node may contain arbitrary
        geometry that describes a flat polygon contained within the indicated left,
        right, bottom, top frame.

        When generate() is called, the geometry in this node will be scaled and
        translated appropriately to give it the size and aspect ratio specified by
        set_frame().
        """
    def clear_source_geometry(self) -> None:
        """Removes the node specified by an earlier call to set_source_geometry()."""
    def generate(self) -> PandaNode:
        """Generates a GeomNode that renders the specified geometry."""
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
    """This class is similar to CardMaker, but instead of generating ordinary
    cards, it generates a circular rose that represents the projection of a 3-D
    scene through a fisheye lens.  The texture coordinates of the rose are
    defined so that each 2-D vertex has a 3-D UVW that reflects the
    corresponding position in 3-D space of that particular vertex.

    This class is particularly suited for converting cube maps to sphere maps.
    """

    @overload
    def __init__(self, __param0: FisheyeMaker) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def reset(self) -> None:
        """Resets all the parameters to their initial defaults."""
    def set_fov(self, fov: float) -> None:
        """Specifies the field of view of the fisheye projection.  A sphere map will
        have a 360-degree field of view (and this is the default).
        """
    def set_num_vertices(self, num_vertices: int) -> None:
        """Specifies the approximate number of vertices to be used to generate the
        rose.  This is the approximate number of vertices that will be located
        within the rose's unit circle, not counting the inscribing square (if any).
        The actual number of vertices used may be +/- 25% of this value.
        """
    def set_square_inscribed(self, square_inscribed: bool, square_radius: float) -> None:
        """Sets the flag that indicates whether the rose should be inscribed within a
        square.  When this is true, an additional square is generated to inscribed
        the circular rose, with the indicated "radius" (the sides of the square
        will be 2 * square_radius).  The texture coordinates of the square will
        uniformly map to the back pole of the cube map.

        This is mainly useful to provide a good uniform background color for a
        sphere map so that it does not have a sharp circular edge that might
        produce artifacts due to numerical imprecision when mapping.
        """
    def set_reflection(self, reflection: bool) -> None:
        """Sets the flag indicating whether the texture image should be mirrored
        (true) or normal (false).  When this is true, the 3-D texture coordinates
        will be reversed so that the image is appropriate for a reflection.  This
        is the best choice for generating a sphere map from a cube map.  The
        default is false.
        """
    def generate(self) -> PandaNode:
        """Generates a GeomNode that renders the specified geometry."""
    setFov = set_fov
    setNumVertices = set_num_vertices
    setSquareInscribed = set_square_inscribed
    setReflection = set_reflection

class FrameRateMeter(TextNode):
    """This is a special TextNode that automatically updates itself with the
    current frame rate.  It can be placed anywhere in the world where you'd
    like to see the frame rate.

    It also has a special mode in which it may be attached directly to a
    channel or window.  If this is done, it creates a DisplayRegion for itself
    and renders itself in the upper-right-hand corner.
    """

    @overload
    def __init__(self, __param0: FrameRateMeter) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def setup_window(self, window: GraphicsOutput) -> None:
        """Sets up the frame rate meter to create a DisplayRegion to render itself
        into the indicated window.
        """
    def clear_window(self) -> None:
        """Undoes the effect of a previous call to setup_window()."""
    def get_window(self) -> GraphicsOutput:
        """Returns the GraphicsOutput that was passed to setup_window(), or NULL if
        setup_window() has not been called.
        """
    def get_display_region(self) -> DisplayRegion:
        """Returns the DisplayRegion that the meter has created to render itself into
        the window to setup_window(), or NULL if setup_window() has not been
        called.
        """
    def set_update_interval(self, update_interval: float) -> None:
        """Specifies the number of seconds that should elapse between updates to the
        frame rate indication.  This should be reasonably slow (e.g.  0.2 to 1.0)
        so that the calculation of the frame rate text does not itself dominate the
        frame rate.
        """
    def get_update_interval(self) -> float:
        """Returns the number of seconds that will elapse between updates to the frame
        rate indication.
        """
    def set_text_pattern(self, text_pattern: str) -> None:
        """Sets the sprintf() pattern that is used to format the text.  The string
        "%f" or some variant will be replaced with the current frame rate in frames
        per second.
        """
    def get_text_pattern(self) -> str:
        """Returns the sprintf() pattern that is used to format the text."""
    def set_clock_object(self, clock_object: ClockObject | _ClockObject_Mode) -> None:
        """Sets the clock that is used to determine the frame rate.  The default is
        the application's global clock (ClockObject::get_global_clock()).
        """
    def get_clock_object(self) -> ClockObject:
        """Returns the clock that is used to determine the frame rate."""
    def update(self) -> None:
        """You can call this to explicitly force the FrameRateMeter to update itself
        with the latest frame rate information.  Normally, it is not necessary to
        call this explicitly.
        """
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

class GeoMipTerrain(TypedObject):
    """GeoMipTerrain, meaning Panda3D GeoMipMapping, can convert a heightfield
    image into a 3D terrain, consisting of several GeomNodes.  It uses the
    GeoMipMapping algorithm, or Geometrical MipMapping, based on the LOD (Level
    of Detail) algorithm.  For more information about the GeoMipMapping
    algoritm, see this paper, written by Willem H. de Boer:
    https://flipcode.com/articles/article_geomipmaps.pdf
    """

    AFM_off: Final = 0
    AFMOff: Final = 0
    AFM_light: Final = 1
    AFMLight: Final = 1
    AFM_medium: Final = 2
    AFMMedium: Final = 2
    AFM_strong: Final = 3
    AFMStrong: Final = 3
    def __init__(self, name: str) -> None: ...
    def heightfield(self) -> PNMImage:
        """Returns a reference to the heightfield (a PNMImage) contained inside
        GeoMipTerrain.  You can use the reference to alter the heightfield.
        """
    @overload
    def set_heightfield(self, image: PNMImage) -> bool:
        """Loads the specified heightmap image file into the heightfield.  Returns
        true if succeeded, or false if an error has occured.  If the heightmap is
        not a power of two plus one, it is scaled up using a gaussian filter.
        """
    @overload
    def set_heightfield(self, filename: StrOrBytesPath, type: PNMFileType = ...) -> bool: ...
    def color_map(self) -> PNMImage:
        """Returns a reference to the color map (a PNMImage) contained inside
        GeoMipTerrain.  You can use the reference to alter the color map.
        """
    @overload
    def set_color_map(self, image: PNMImage | Texture) -> bool:
        """Loads the specified image as color map.  The next time generate() is
        called, the terrain is painted with this color map using the vertex color
        column.  Returns a boolean indicating whether the operation has succeeded.
        """
    @overload
    def set_color_map(self, path: str) -> bool: ...
    @overload
    def set_color_map(self, filename: StrOrBytesPath, type: PNMFileType = ...) -> bool: ...
    def has_color_map(self) -> bool:
        """Returns whether a color map has been set."""
    def clear_color_map(self) -> None:
        """Clears the color map."""
    def calc_ambient_occlusion(self, radius: float = ..., contrast: float = ..., brightness: float = ...) -> None:
        """Calculates an approximate for the ambient occlusion and stores it in the
        color map, so that it will be written to the vertex colors.  Any existing
        color map will be discarded.  You need to call this before generating the
        geometry.
        """
    def get_elevation(self, x: float, y: float) -> float:
        """Fetches the elevation at (x, y), where the input coordinate is specified in
        pixels.  This ignores the current LOD level and instead provides an
        accurate number.  Linear blending is used for non-integral coordinates.
        Terrain scale is NOT taken into account!  To get accurate normals, please
        multiply this with the terrain Z scale!

        trueElev = terr.get_elevation(x,y) * terr.get_sz();
        """
    @overload
    def get_normal(self, x: int, y: int) -> LVector3:
        """`(self, x: int, y: int)`:
        Fetches the terrain normal at (x, y), where the input coordinate is
        specified in pixels.  This ignores the current LOD level and instead
        provides an accurate number.  Terrain scale is NOT taken into account!  To
        get accurate normals, please divide it by the terrain scale and normalize
        it again, like this:

        LVector3 normal (terr.get_normal(x, y)); normal.set(normal.get_x() /
        root.get_sx(), normal.get_y() / root.get_sy(), normal.get_z() /
        root.get_sz()); normal.normalize();

        `(self, mx: int, my: int, x: int, y: int)`:
        Fetches the terrain normal at (x,y), where the input coordinate is
        specified in pixels.  This ignores the current LOD level and instead
        provides an accurate number.  Terrain scale is NOT taken into account!  To
        get accurate normals, please divide it by the terrain scale and normalize
        it again!
        """
    @overload
    def get_normal(self, mx: int, my: int, x: int, y: int) -> LVector3: ...
    def set_bruteforce(self, bf: bool) -> None:
        """Sets a boolean specifying whether the terrain will be rendered bruteforce.
        If the terrain is rendered bruteforce, there will be no Level of Detail,
        and the update() call will only update the terrain if it is marked dirty.
        """
    def get_bruteforce(self) -> bool:
        """Returns a boolean whether the terrain is rendered bruteforce or not.  See
        set_bruteforce for more information.
        """
    def set_auto_flatten(self, mode: int) -> None:
        """The terrain can be automatically flattened (using flatten_light,
        flatten_medium, or flatten_strong) after each update.  This only affects
        future updates, it doesn't flatten the current terrain.
        """
    @overload
    def set_focal_point(self, fp: DoubleVec2Like | DoubleVec3Like | Vec2Like | Vec3Like) -> None:
        """`(self, fp: LPoint2d)`:
        The focal point is the point at which the terrain will have the highest
        quality (lowest level of detail). Parts farther away from the focal point
        will have a lower quality (higher level of detail). The focal point is
        not taken in respect if bruteforce is set true.

        `(self, x: float, y: float)`:
        Sets the focal point.  GeoMipTerrain generates high-resolution terrain
        around the focal point, and progressively lower and lower resolution
        terrain as you get farther away.  If a point is supplied and not a
        NodePath, make sure it's relative to the terrain.  Only the x and y
        coordinates of the focal point are taken in respect.
        """
    @overload
    def set_focal_point(self, fnp: NodePath) -> None: ...
    @overload
    def set_focal_point(self, x: float, y: float) -> None: ...
    def get_focal_point(self) -> NodePath:
        """Returns the focal point, as a NodePath.  If you have set it to be just a
        point, it will return an empty node at the focal position.
        """
    def get_root(self) -> NodePath:
        """Returns the root of the terrain.  This is a single PandaNode to which all
        the rest of the terrain is parented.  The generate and update operations
        replace the nodes which are parented to this root, but they don't replace
        this root itself.
        """
    def set_block_size(self, newbs: int) -> None:
        """Sets the block size.  If it is not a power of two, the closest power of two
        is used.
        """
    def get_block_size(self) -> int:
        """Gets the block size."""
    def get_max_level(self) -> int:
        """Returns the highest level possible for this block size.  When a block is at
        this level, it will be the worst quality possible.
        """
    def set_min_level(self, minlevel: int) -> None:
        """Sets the minimum level of detail at which blocks may be generated by
        generate() or update(). The default value is 0, which is the highest
        quality.  This value is also taken in respect when generating the terrain
        bruteforce.
        """
    def get_min_level(self) -> int:
        """Gets the minimum level of detail at which blocks may be generated by
        generate() or update(). The default value is 0, which is the highest
        quality.
        """
    def is_dirty(self) -> bool:
        """Returns a bool indicating whether the terrain is marked 'dirty', that means
        the terrain has to be regenerated on the next update() call, because for
        instance the heightfield has changed.  Once the terrain has been
        regenerated, the dirty flag automatically gets reset internally.
        """
    def set_factor(self, factor: float) -> None:
        """DEPRECATED method.  Use set_near/far instead.  Sets the quality factor at
        which blocks must be generated.  The higher this level, the better quality
        the terrain will be, but more expensive to render.  A value of 0 makes the
        terrain the lowest quality possible, depending on blocksize.  The default
        value is 100.
        """
    def set_near_far(self, input_near: float, input_far: float) -> None:
        """Sets the near and far LOD distances in one call."""
    def set_near(self, input_near: float) -> None:
        """Sets the near LOD distance, at which the terrain will be rendered at
        highest quality.  This distance is in the terrain's coordinate space!
        """
    def set_far(self, input_far: float) -> None:
        """Sets the far LOD distance, at which the terrain will be rendered at lowest
        quality.  This distance is in the terrain's coordinate space!
        """
    def get_block_node_path(self, mx: int, my: int) -> NodePath:
        """Returns the NodePath of the specified block.  If auto-flatten is enabled
        and the node is getting removed during the flattening process, it will
        still return a NodePath with the appropriate terrain chunk, but it will be
        in a temporary scenegraph.  Please note that this returns a const object
        and you can not modify the node.  Modify the heightfield instead.
        """
    def get_block_from_pos(self, x: float, y: float) -> LVecBase2:
        """Gets the coordinates of the block at the specified position.  This position
        must be relative to the terrain, not to render.  Returns an array
        containing two values: the block x and the block y coords.  If the
        positions are out of range, the closest block is taken.  Note that the
        VecBase returned does not represent a vector, position, or rotation, but it
        contains the block index of the block which you can use in
        GeoMipTerrain::get_block_node_path.
        """
    def set_border_stitching(self, stitching: bool) -> None:
        """If this value is true, the LOD level at the borders of the terrain will be
        0. This is useful if you have multiple terrains attached and you want to
        stitch them together, to fix seams.  This setting also has effect when
        bruteforce is enabled, although in that case you are probably better off
        with setting the minlevels to the same value.
        """
    def get_border_stitching(self) -> bool:
        """Returns the current stitching setting.  False by default, unless
        set_stitching has been set.
        """
    def get_far(self) -> float:
        """Returns the far LOD distance in the terrain coordinate space"""
    def get_near(self) -> float:
        """Returns the near LOD distance in the terrain coordinate space"""
    def get_flatten_mode(self) -> int:
        """Returns the automatic-flatten mode (e.g., off, flatten_light,
        flatten_medium, or flatten_strong)
        """
    def make_slope_image(self) -> PNMImage:
        """Returns a new grayscale image containing the slope angles.  A white pixel
        value means a vertical slope, while a black pixel will mean that the
        terrain is entirely flat at that pixel.  You can translate it to degrees by
        mapping the greyscale values from 0 to 90 degrees.  The resulting image
        will have the same size as the heightfield image.  The scale will be taken
        into respect -- meaning, if you change the terrain scale, the slope image
        will need to be regenerated in order to be correct.
        """
    def generate(self) -> None:
        """(Re)generates the entire terrain, erasing the current.  This call un-
        flattens the terrain, so make sure you have set auto-flatten if you want to
        keep your terrain flattened.
        """
    def update(self) -> bool:
        """Loops through all of the terrain blocks, and checks whether they need to be
        updated.  If that is indeed the case, it regenerates the mipmap.  Returns a
        true when the terrain has changed.  Returns false when the terrain isn't
        updated at all.  If there is no terrain yet, it generates the entire
        terrain.  This call un-flattens the terrain, so make sure you have set
        auto-flatten if you want to keep your terrain flattened.
        """
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

class HeightfieldTesselator(Namable):
    @overload
    def __init__(self, __param0: HeightfieldTesselator) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def heightfield(self) -> PNMImage:
        """Returns a reference to the heightfield (a PNMImage) contained inside the
        HeightfieldTesselator.  You can use the reference to alter the heightfield.
        """
    def set_heightfield(self, filename: StrOrBytesPath, type: PNMFileType = ...) -> bool:
        """Loads the specified greyscale image file into the heightfield."""
    def set_poly_count(self, n: int) -> None:
        """Sets the polygon-count target.  The tesselator usually manages to come
        within about 20% of the target, plus or minus.
        """
    def set_visibility_radius(self, r: int) -> None:
        """Sets the visibility radius.  Polygons that are completely outside the
        radius (relative to the focal point) are cropped away.  The cropping is
        imperfect (all approximations are conservative), so this should be used in
        conjunction with a far clipping plane, fog, or some other visibility
        limiting mechanism.  The units are in pixels.
        """
    def set_focal_point(self, x: int, y: int) -> None:
        """Sets the focal point.  The tesselator generates high-resolution terrain
        around the focal point, and progressively lower and lower resolution
        terrain as you get farther away.  The units are in pixels.
        """
    def set_horizontal_scale(self, h: float) -> None:
        """Sets the horizontal scale.  The default scale is 1.0, meaning that each
        pixel in the heightfield is 1x1 panda units wide.
        """
    def set_vertical_scale(self, v: float) -> None:
        """Sets the vertical scale.  The default scale is 255.0, meaning that each as
        the gray value ranges from (0-1), the elevation ranges from (0-255) feet.
        """
    def set_max_triangles(self, n: int) -> None:
        """Sets the max triangles per geom."""
    def get_elevation(self, x: float, y: float) -> float:
        """Fetches the elevation at (x,y), where the input coordinate is specified in
        pixels.  This ignores the current tesselation level and instead provides an
        accurate number.  Linear blending is used for non-integral coordinates.
        """
    def generate(self) -> NodePath:
        """Generates a tree of nodes that represents the heightfield.  This can be
        reparented into the scene.
        """
    setHeightfield = set_heightfield
    setPolyCount = set_poly_count
    setVisibilityRadius = set_visibility_radius
    setFocalPoint = set_focal_point
    setHorizontalScale = set_horizontal_scale
    setVerticalScale = set_vertical_scale
    setMaxTriangles = set_max_triangles
    getElevation = get_elevation

class LineSegs(Namable):
    """Encapsulates creation of a series of connected or disconnected line
    segments or points, for drawing paths or rays.  This class doesn't attempt
    to be the smartest it could possibly be; it's intended primarily as a
    visualization and editing tool.
    """

    @overload
    def __init__(self, name: str = ...) -> None:
        """Constructs a LineSegs object, which can be used to create any number of
        disconnected lines or points of various thicknesses and colors through the
        visible scene.  After creating the object, call move_to() and draw_to()
        repeatedly to describe the path, then call create() to create a GeomNode
        which will render the described path.
        """
    @overload
    def __init__(self, __param0: LineSegs) -> None: ...
    def reset(self) -> None:
        """Removes any lines in progress and resets to the initial empty state."""
    @overload
    def set_color(self, color: Vec4Like) -> None:
        """Establishes the color that will be assigned to all vertices created by
        future calls to move_to() and draw_to().
        """
    @overload
    def set_color(self, r: float, g: float, b: float, a: float = ...) -> None: ...
    def set_thickness(self, thick: float) -> None:
        """Establishes the line thickness or point size in pixels that will be
        assigned to all lines and points created by future calls to create().
        """
    @overload
    def move_to(self, v: Vec3Like) -> None:
        """Moves the pen to the given point without drawing a line.  When followed by
        draw_to(), this marks the first point of a line segment; when followed by
        move_to() or create(), this creates a single point.
        """
    @overload
    def move_to(self, x: float, y: float, z: float) -> None: ...
    @overload
    def draw_to(self, v: Vec3Like) -> None:
        """Draws a line segment from the pen's last position (the last call to move_to
        or draw_to) to the indicated point.  move_to() and draw_to() only update
        tables; the actual drawing is performed when create() is called.
        """
    @overload
    def draw_to(self, x: float, y: float, z: float) -> None: ...
    def get_current_position(self) -> LVertex:
        """Returns the pen's current position.  The next call to draw_to() will draw a
        line segment from this point.
        """
    def is_empty(self) -> bool:
        """Returns true if move_to() or draw_to() have not been called since the last
        reset() or create(), false otherwise.
        """
    @overload
    def create(self, dynamic: bool = ...) -> GeomNode:
        """`(self, previous: GeomNode, dynamic: bool = ...)`:
        Appends to an existing GeomNode a new Geom that will render the series of
        line segments and points described via calls to move_to() and draw_to().
        The lines and points are created with the color and thickness established
        by calls to set_color() and set_thickness().

        If dynamic is true, the line segments will be created with the dynamic Geom
        setting, optimizing them for runtime vertex animation.

        `(self, dynamic: bool = ...)`:
        Creates a new GeomNode that will render the series of line segments and
        points described via calls to move_to() and draw_to().  The lines and
        points are created with the color and thickness established by calls to
        set_color() and set_thickness().

        If dynamic is true, the line segments will be created with the dynamic Geom
        setting, optimizing them for runtime vertex animation.
        """
    @overload
    def create(self, previous: GeomNode, dynamic: bool = ...) -> GeomNode: ...
    def get_num_vertices(self) -> int:
        """Returns the total number of line segment and point vertices generated by
        the last call to create().  The positions of these vertices may be read and
        adjusted through get_vertex() and set_vertex().
        """
    def get_vertex(self, n: int) -> LVertex:
        """Returns the nth point or vertex of the line segment sequence generated by
        the last call to create().  The first move_to() generates vertex 0;
        subsequent move_to() and draw_to() calls generate consecutively higher
        vertex numbers.
        """
    @overload
    def set_vertex(self, n: int, vert: Vec3Like) -> None:
        """Moves the nth point or vertex of the line segment sequence generated by the
        last call to create().  The first move_to() generates vertex 0; subsequent
        move_to() and draw_to() calls generate consecutively higher vertex numbers.
        """
    @overload
    def set_vertex(self, vertex: int, x: float, y: float, z: float) -> None: ...
    def get_vertex_color(self, vertex: int) -> LColor:
        """Returns the color of the nth point or vertex."""
    @overload
    def set_vertex_color(self, vertex: int, c: Vec4Like) -> None:
        """Changes the vertex color of the nth point or vertex.  See set_vertex()."""
    @overload
    def set_vertex_color(self, vertex: int, r: float, g: float, b: float, a: float = ...) -> None: ...
    def get_vertices(self) -> tuple[LVertex, ...]: ...
    def get_vertex_colors(self) -> tuple[LColor, ...]: ...
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
    """Mesh drawer creates a single geom object that can be shaped with different
    draw commands.  This is an efficient way to render bunch of billboards,
    particles, fast changing triangles.  Its implemented by recycling same geom
    over and over again.  Max budget specifies how many triangles are allowed.
    Some uses of this class can be : particle system, radar icons, health bars,
    2d icons, 2d ui, bullets, missile trails.  Any that can be drawn with
    triangles can be drawn with this class.  At the low level this uses the
    GeomVertexRewriter's.  The internal geom consists of vertex, normal, uv and
    color channels.
    """

    def __init__(self) -> None:
        """Creates the MeshDrawer low level system."""
    def set_budget(self, budget: int) -> None:
        """Sets the total triangle budget of the drawer.  This will not be exceeded.
        Don't set some thing too large because it will be slow
        """
    def get_budget(self) -> int:
        """Gets the total triangle budget of the drawer"""
    def get_root(self) -> NodePath:
        """Returns the root NodePath.  You should use this node to reparent mesh
        drawer onto the scene might also want to disable depth draw or enable
        transparency.
        """
    def begin(self, camera: NodePath, render: NodePath) -> None:
        """Pass the current camera node and the root node.  Passing the camera is
        required to generate bill boards that face it.
        """
    def tri(
        self,
        v1: Vec3Like,
        c1: Vec4Like,
        uv1: Vec2Like,
        v2: Vec3Like,
        c2: Vec4Like,
        uv2: Vec2Like,
        v3: Vec3Like,
        c3: Vec4Like,
        uv3: Vec2Like,
    ) -> None:
        """Draws a triangle with the given parameters."""
    def particle(self, pos: Vec3Like, frame: Vec4Like, size: float, color: Vec4Like, rotation: float) -> None:
        """Draws a particle that is sort of like a bill board but has an extra
        rotation component.  Frame contains u,v,u-size,v-size quadruple.
        """
    def blended_particle(
        self, pos: Vec3Like, frame1: Vec4Like, frame2: Vec4Like, blend: float, size: float, color: Vec4Like, rotation: float
    ) -> None:
        """Works just like particle but accepts 2 frames and a blend (from 0 to 1)
        component between them Frame contains u,v,u-size,v-size quadruple.
        """
    def billboard(self, pos: Vec3Like, frame: Vec4Like, size: float, color: Vec4Like) -> None:
        """Draws a billboard - particle with no rotation.  Billboards always face the
        camera.  Frame contains u,v,u-size,v-size quadruple.
        """
    def segment(self, start: Vec3Like, stop: Vec3Like, frame: Vec4Like, thickness: float, color: Vec4Like) -> None:
        """Draws a segment a line with a thickness.  That has billboarding effect.
        Frame contains u,v,u-size,v-size quadruple.
        """
    def cross_segment(self, start: Vec3Like, stop: Vec3Like, frame: Vec4Like, thickness: float, color: Vec4Like) -> None:
        """Draws a segment a line with a thickness.  This segment does not use the
        bill boarding behavior and instead draws 2 planes in a cross.  Stars at
        start and ends at stop.  Frame contains u,v,u-size,v-size quadruple.
        """
    def uneven_segment(
        self,
        start: Vec3Like,
        stop: Vec3Like,
        frame: Vec4Like,
        thickness_start: float,
        color_start: Vec4Like,
        thickness_stop: float,
        color_stop: Vec4Like,
    ) -> None:
        """Draws a segment a line with different thickness and color on both sides.
        Stars at start and ends at stop.  Frame contains u,v,u-size,v-size
        quadruple.
        """
    def link_segment(self, pos: Vec3Like, frame: Vec4Like, thickness: float, color: Vec4Like) -> None:
        """Stars or continues linked segment.  Control position, frame, thickness and
        color with parameters.  Frame contains u,v,u-size,v-size quadruple.
        """
    def link_segment_end(self, frame: Vec4Like, color: Vec4Like) -> None:
        """Finish drawing linked segments, needs at least two calls to link_segment
        before it can end the linked segment.  Frame contains u,v,u-size,v-size
        quadruple.
        """
    def explosion(
        self, pos: Vec3Like, frame: Vec4Like, size: float, color: Vec4Like, seed: int, number: int, distance: float
    ) -> None:
        """Draws number of particles in a sphere like emitter.  Frame contains
        u,v,u-size,v-size quadruple.
        """
    def stream(
        self, start: Vec3Like, stop: Vec3Like, frame: Vec4Like, size: float, color: Vec4Like, number: int, offset: float
    ) -> None:
        """Draws a number of particles in a big line with a shift dictated by the
        offset.  Frame contains u,v,u-size,v-size quadruple.
        """
    def geometry(self, node: NodePath) -> None:
        """Draws the geometry that is inside this node path into the MeshDrawer
        object.  This performs a similar functions as RigidBodyCombiner but for
        very dynamic situations that share the same texture like physcal chunks of
        explosions.  It can be a little slow
        """
    def end(self) -> None:
        """Finish the drawing and clearing off the remaining vertexes."""
    setBudget = set_budget
    getBudget = get_budget
    getRoot = get_root
    blendedParticle = blended_particle
    crossSegment = cross_segment
    unevenSegment = uneven_segment
    linkSegment = link_segment
    linkSegmentEnd = link_segment_end

class MeshDrawer2D(TypedObject):
    """This class allows the drawing of 2D objects - mainly based on quads and
    rectangles.  It allows clipping and several high level UI theme functions.
    """

    def __init__(self) -> None:
        """Creates the MeshDrawer2D low level system."""
    def set_budget(self, budget: int) -> None:
        """Sets the total triangle budget of the drawer."""
    def get_budget(self) -> int:
        """Gets the total triangle budget of the drawer."""
    def get_root(self) -> NodePath:
        """Returns the root NodePath."""
    def quad_raw(
        self,
        v1: Vec3Like,
        c1: Vec4Like,
        uv1: Vec2Like,
        v2: Vec3Like,
        c2: Vec4Like,
        uv2: Vec2Like,
        v3: Vec3Like,
        c3: Vec4Like,
        uv3: Vec2Like,
        v4: Vec3Like,
        c4: Vec4Like,
        uv4: Vec2Like,
    ) -> None:
        """Draws a 2D rectangle.  Ignores the clipping rectangle."""
    def rectangle_raw(
        self, x: float, y: float, w: float, h: float, u: float, v: float, us: float, vs: float, color: Vec4Like
    ) -> None: ...
    def set_clip(self, x: float, y: float, w: float, h: float) -> None:
        """Sets the clipping rectangle."""
    def rectangle(
        self, x: float, y: float, w: float, h: float, u: float, v: float, us: float, vs: float, color: Vec4Like
    ) -> None:
        """Draws a 2D rectangle which can be clipped."""
    def rectangle_border(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        r: float,
        t: float,
        l: float,
        b: float,
        tr: float,
        tt: float,
        tl: float,
        tb: float,
        u: float,
        v: float,
        us: float,
        vs: float,
        color: Vec4Like,
    ) -> None:
        """Draws a 2d rectangle, with borders and corders, taken from the surrounding
        texture
        """
    def rectangle_border_tiled(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        r: float,
        t: float,
        l: float,
        b: float,
        tr: float,
        tt: float,
        tl: float,
        tb: float,
        u: float,
        v: float,
        us: float,
        vs: float,
        color: Vec4Like,
    ) -> None:
        """Draws a 2d rectangle, with borders and corders, taken from the surrounding
        texture
        """
    def rectangle_tiled(
        self, x: float, y: float, w: float, h: float, u: float, v: float, us: float, vs: float, color: Vec4Like
    ) -> None:
        """Draws a tiled rectangle, size of tiles is in us and vs"""
    def begin(self) -> None:
        """Opens up the geom for drawing, don't forget to call MeshDrawer2D::end()"""
    def end(self) -> None:
        """Finish the drawing and clearing off the remaining vertexes."""
    setBudget = set_budget
    getBudget = get_budget
    getRoot = get_root
    quadRaw = quad_raw
    rectangleRaw = rectangle_raw
    setClip = set_clip
    rectangleBorder = rectangle_border
    rectangleBorderTiled = rectangle_border_tiled
    rectangleTiled = rectangle_tiled

class MovieTexture(Texture):
    """A texture that fetches video frames from an underlying object of class
    Movie.
    """

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
    def __init__(self, video: MovieVideo) -> None:
        """`(self, video: MovieVideo)`:
        Creates a texture playing the specified movie.

        `(self, name: str)`:
        Creates a blank movie texture.  Movies must be added using do_read_one or
        do_load_one.
        """
    @overload
    def __init__(self, name: str) -> None: ...
    def get_video_length(self) -> float:
        """Returns the length of the video."""
    def get_video_width(self) -> int:
        """Returns the width in texels of the source video stream.  This is not
        necessarily the width of the actual texture, since the texture may have
        been expanded to raise it to a power of 2.
        """
    def get_video_height(self) -> int:
        """Returns the height in texels of the source video stream.  This is not
        necessarily the height of the actual texture, since the texture may have
        been expanded to raise it to a power of 2.
        """
    def get_color_cursor(self, page: int) -> MovieVideoCursor:
        """Returns the MovieVideoCursor that is feeding the color channels for the
        indicated page, where 0 <= page < get_num_pages().
        """
    def get_alpha_cursor(self, page: int) -> MovieVideoCursor:
        """Returns the MovieVideoCursor that is feeding the alpha channel for the
        indicated page, where 0 <= page < get_num_pages().
        """
    def restart(self) -> None:
        """Start playing the movie from where it was last paused.  Has no effect if
        the movie is not paused, or if the movie's cursor is already at the end.
        """
    def stop(self) -> None:
        """Stops a currently playing or looping movie right where it is.  The movie's
        cursor remains frozen at the point where it was stopped.
        """
    def play(self) -> None:
        """Plays the movie from the beginning."""
    def set_time(self, t: float) -> None:
        """Sets the movie's cursor."""
    def get_time(self) -> float:
        """Returns the current value of the movie's cursor.  If the movie's loop count
        is greater than one, then its length is effectively multiplied for the
        purposes of this function.  In other words, the return value will be in the
        range 0.0 to (length * loopcount).
        """
    def set_loop(self, enable: bool) -> None:
        """If true, sets the movie's loop count to 1 billion.  If false, sets the
        movie's loop count to one.
        """
    def get_loop(self) -> bool:
        """Returns true if the movie's loop count is not equal to one."""
    def set_loop_count(self, count: int) -> None:
        """Sets the movie's loop count to the desired value."""
    def get_loop_count(self) -> int:
        """Returns the movie's loop count."""
    def set_play_rate(self, play_rate: float) -> None:
        """Sets the movie's play-rate.  This is the speed at which the movie's cursor
        advances.  The default is to advance 1.0 movie-seconds per real-time
        second.
        """
    def get_play_rate(self) -> float:
        """Gets the movie's play-rate."""
    def is_playing(self) -> bool:
        """Returns true if the movie's cursor is advancing."""
    def synchronize_to(self, sound: AudioSound) -> None:
        """Synchronize this texture to a sound.  Typically, you would load the texture
        and the sound from the same AVI file.
        """
    def unsynchronize(self) -> None:
        """Stop synchronizing with a sound."""
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

class MultitexReducer:
    """This object presents an interface for generating new texture images that
    represent the combined images from one or more individual textures,
    reproducing certain kinds of multitexture effects without depending on
    multitexture support in the hardware.

    This also flattens out texture matrices and removes extra texture
    coordinates from the Geoms.  It is thus not a complete substitute for true
    multitexturing, because it does not lend itself well to dynamic animation
    of the textures once they have been flattened.  It is, however, useful for
    "baking in" a particular multitexture effect.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: MultitexReducer = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def clear(self) -> None: ...
    @overload
    def scan(self, node: NodePath, state_from: NodePath = ...) -> None:
        """`(self, node: NodePath)`:
        Starts scanning the hierarchy beginning at the indicated node.  Any
        GeomNodes discovered in the hierarchy with multitexture will be added to
        internal structures in the MultitexReducer so that a future call to
        flatten() will operate on all of these at once.

        This version of this method does not accumulate state from the parents of
        the indicated node; thus, only multitexture effects that have been applied
        at node and below will be considered.

        `(self, node: NodePath, state_from: NodePath)`:
        Starts scanning the hierarchy beginning at the indicated node.  Any
        GeomNodes discovered in the hierarchy with multitexture will be added to
        internal structures in the MultitexReducer so that a future call to
        flatten() will operate on all of these at once.

        The second parameter represents the NodePath from which to accumulate the
        state that is considered for the multitexture.  Pass an empty NodePath to
        accumulate all the state from the root of the graph, or you may specify
        some other node here in order to not consider nodes above that as
        contributing to the state to be flattened.  This is particularly useful if
        you have some texture stage which is applied globally to a scene (for
        instance, a caustics effect), which you don't want to be considered for
        flattening by the MultitexReducer.
        """
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
    """This VertexTransform gets its matrix from the Transform stored on a node.
    It can also compose its node's transform with another VertexTransform,
    allowing you to build up a chain of NodeVertexTransforms that represent a
    list of composed matrices.
    """

    @property
    def node(self) -> PandaNode: ...
    @property
    def prev(self) -> VertexTransform: ...
    def __init__(self, node: PandaNode, prev: VertexTransform = ...) -> None: ...
    def get_node(self) -> PandaNode:
        """Returns the PandaNode whose transform supplies this object."""
    def get_prev(self) -> VertexTransform:
        """Returns the VertexTransform object whose matrix will be composed with the
        result of this node's transform.
        """
    getNode = get_node
    getPrev = get_prev

class ShaderTerrainMesh(PandaNode):
    """@brief Terrain Renderer class utilizing the GPU
    @details This class provides functionality to render heightfields of large
      sizes utilizing the GPU. Internally a quadtree is used to generate the LODs.
      The final terrain is then rendered using instancing on the GPU. This makes
      it possible to use very large heightfields (8192+) with very reasonable
      performance. The terrain provides options to control the LOD using a
      target triangle width, see ShaderTerrainMesh::set_target_triangle_width().

      Because the Terrain is rendered entirely on the GPU, it needs a special
      vertex shader. There is a default vertex shader available, which you can
      use in your own shaders. IMPORTANT: If you don't set an appropriate shader
      on the terrain, nothing will be visible.
    """

    heightfield: Texture
    chunk_size: int
    generate_patches: bool
    update_enabled: bool
    target_triangle_width: float
    def __init__(self) -> None:
        """@brief Constructs a new Terrain Mesh
        @details This constructs a new terrain mesh. By default, no transform is set
          on the mesh, causing it to range over the unit box from (0, 0, 0) to
          (1, 1, 1). Usually you want to set a custom transform with NodePath::set_scale()
        """
    def set_heightfield(self, heightfield: Texture) -> None:
        """@brief Sets the heightfield texture
        @details This sets the heightfield texture. It should be 16bit
          single channel, and have a power-of-two resolution greater than 32.
          Common sizes are 2048x2048 or 4096x4096.

          You should call generate() after setting the heightfield.

        @param filename Heightfield texture
        """
    def get_heightfield(self) -> Texture:
        """@brief Returns the heightfield
        @details This returns the terrain heightfield, previously set with
          set_heightfield()

        @return Path to the heightfield
        """
    def set_chunk_size(self, chunk_size: int) -> None:
        """@brief Sets the chunk size
        @details This sets the chunk size of the terrain. A chunk is basically the
          smallest unit in LOD. If the chunk size is too small, the terrain will
          perform bad, since there will be way too many chunks. If the chunk size
          is too big, you will not get proper LOD, and might also get bad performance.

          For terrains of the size 4096x4096 or 8192x8192, a chunk size of 32 seems
          to produce good results. For smaller resolutions, you should try out a
          size of 16 or even 8 for very small terrains.

          The amount of chunks generated for the last level equals to
          (heightfield_size / chunk_size) ** 2. The chunk size has to be a power
          of two.

        @param chunk_size Size of the chunks, has to be a power of two
        """
    def get_chunk_size(self) -> int:
        """@brief Returns the chunk size
        @details This returns the chunk size, previously set with set_chunk_size()
        @return Chunk size
        """
    def set_generate_patches(self, generate_patches: bool) -> None:
        """@brief Sets whether to generate patches
        @details If this option is set to true, GeomPatches will be used instead of
          GeomTriangles. This is required when the terrain is used with tesselation
          shaders, since patches are required for tesselation, whereas triangles
          are required for regular rendering.

          If this option is set to true while not using a tesselation shader, the
          terrain will not get rendered, or even produce errors. The same applies
          when this is option is not set, but the terrain is used with tesselation
          shaders.

        @param generate_patches [description]
        """
    def get_generate_patches(self) -> bool:
        """@brief Returns whether to generate patches
        @details This returns whether patches are generated, previously set with
          set_generate_patches()

        @return Whether to generate patches
        """
    def set_update_enabled(self, update_enabled: bool) -> None:
        """@brief Sets whether to enable terrain updates
        @details This flag controls whether the terrain should be updated. If this value
          is set to false, no updating of the terrain will happen. This can be useful
          to debug the culling algorithm used by the terrain.

        @param update_enabled Whether to update the terrain
        """
    def get_update_enabled(self) -> bool:
        """@brief Returns whether the terrain is getting updated
        @details This returns whether the terrain is getting updates, previously set with
          set_update_enabled()

        @return Whether to update the terrain
        """
    def set_target_triangle_width(self, target_triangle_width: float) -> None:
        """@brief Sets the desired triangle width
        @details This sets the desired width a triangle should have in pixels.
          A value of 10.0 for example will make the terrain tesselate everything
          in a way that each triangle edge roughly is 10 pixels wide.
          Of course this will not always accurately match, however you can use this
          setting to control the LOD algorithm of the terrain.

        @param target_triangle_width Desired triangle width in pixels
        """
    def get_target_triangle_width(self) -> float:
        """@brief Returns the target triangle width
        @details This returns the target triangle width, previously set with
          ShaderTerrainMesh::set_target_triangle_width()

        @return Target triangle width
        """
    @overload
    def uv_to_world(self, coord: Vec2Like) -> LPoint3:
        """`(self, coord: LTexCoord)`:
        @brief Transforms a texture coordinate to world space
        @details This transforms a texture coordinatefrom uv-space (0 to 1) to world
          space. This takes the terrains transform into account, and also samples the
          heightmap. This method should be called after generate().

        @param coord Coordinate in uv-space from 0, 0 to 1, 1
        @return World-Space point

        `(self, u: float, v: float)`:
        @see ShaderTerrainMesh::uv_to_world(LTexCoord)
        """
    @overload
    def uv_to_world(self, u: float, v: float) -> LPoint3: ...
    def generate(self) -> bool:
        """@brief Generates the terrain mesh
        @details This generates the terrain mesh, initializing all chunks of the
          internal used quadtree. At this point, a heightfield and a chunk size should
          have been set, otherwise an error is thrown.

          If anything goes wrong, like a missing heightfield, then an error is printed
          and false is returned.

        @return true if the terrain was initialized, false if an error occured
        """
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

class SceneGraphAnalyzerMeter(TextNode):
    """This is a special TextNode that automatically updates itself with output
    from a SceneGraphAnalyzer instance.  It can be placed anywhere in the world
    where you'd like to see the output from SceneGraphAnalyzer.

    It also has a special mode in which it may be attached directly to a
    channel or window.  If this is done, it creates a DisplayRegion for itself
    and renders itself in the upper-right-hand corner.
    """

    @overload
    def __init__(self, __param0: SceneGraphAnalyzerMeter) -> None: ...
    @overload
    def __init__(self, name: str, node: PandaNode) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def setup_window(self, window: GraphicsOutput) -> None:
        """Sets up the frame rate meter to create a DisplayRegion to render itself
        into the indicated window.
        """
    def clear_window(self) -> None:
        """Undoes the effect of a previous call to setup_window()."""
    def get_window(self) -> GraphicsOutput:
        """Returns the GraphicsOutput that was passed to setup_window(), or NULL if
        setup_window() has not been called.
        """
    def get_display_region(self) -> DisplayRegion:
        """Returns the DisplayRegion that the meter has created to render itself into
        the window to setup_window(), or NULL if setup_window() has not been
        called.
        """
    def set_update_interval(self, update_interval: float) -> None:
        """Specifies the number of seconds that should elapse between updates to the
        meter.  This should be reasonably slow (e.g.  0.5 to 2.0) so that the
        calculation of the scene graph analysis does not itself dominate the frame
        rate.
        """
    def get_update_interval(self) -> float:
        """Returns the number of seconds that will elapse between updates to the frame
        rate indication.
        """
    def set_node(self, node: PandaNode) -> None:
        """Sets the node to be analyzed."""
    def get_node(self) -> PandaNode:
        """Returns the node to be analyzed."""
    def update(self) -> None:
        """You can call this to explicitly force the SceneGraphAnalyzerMeter to update
        itself with the latest scene graph analysis information.  Normally, it is
        not necessary to call this explicitly.
        """
    setupWindow = setup_window
    clearWindow = clear_window
    getWindow = get_window
    getDisplayRegion = get_display_region
    setUpdateInterval = set_update_interval
    getUpdateInterval = get_update_interval
    setNode = set_node
    getNode = get_node

class RigidBodyCombiner(PandaNode):
    """This is a special node that combines multiple independently-moving rigid
    nodes into one Geom internally (or as few Geoms as possible), for the
    purposes of improving rendering performance.

    To use it, parent a number of moving objects to this node and call
    collect().  A child node is identified as "moving" if (a) it has a non-
    identity transform initially, or (b) it is a ModelNode with the
    preserve_transform flag set.  Any other nodes will be considered static,
    and later transforms applied to them will not be identified.

    You should call collect() only at startup or if you change the set of
    children; it is a relatively expensive call.

    Once you call collect(), you may change the transforms on the child nodes
    freely without having to call collect() again.

    RenderEffects such as Billboards are not supported below this node.
    """

    @property
    def internal_scene(self) -> NodePath: ...
    def collect(self) -> None:
        """Walks through the entire subgraph of nodes rooted at this node, accumulates
        all of the RenderAttribs and Geoms below this node, flattening them into
        just one Geom (or as few as possible, if there are multiple different
        states).

        Nodes that have transforms on them at the time of collect(), or any
        ModelNodes with the preserve_transform flag, will be identified as "moving"
        nodes, and their transforms will be monitored as they change in future
        frames and each new transform directly applied to the vertices.

        This call must be made after adding any nodes to or removing any nodes from
        the subgraph rooted at this node.  It should not be made too often, as it
        is a relatively expensive call.  If you need to hide children of this node,
        consider scaling them to zero (or very near zero), or moving them behind
        the camera, instead.
        """
    def get_internal_scene(self) -> NodePath:
        """Returns a special NodePath that represents the internal node of this
        object.  This is the node that is actually sent to the graphics card for
        rendering; it contains the collection of the children of this node into as
        few Geoms as possible.

        This node is filled up by the last call to collect().
        """
    getInternalScene = get_internal_scene

class PipeOcclusionCullTraverser(CullTraverser):
    """This specialization of CullTraverser uses the graphics pipe itself to
    perform occlusion culling.  As such, it's likely to be inefficient (since
    it interferes with the pipe's normal mode of rendering), and is mainly
    useful to test other, CPU-based occlusion algorithms.

    This cannot be used in a multithreaded pipeline environment where cull and
    draw are operating simultaneously.

    It can't be defined in the cull subdirectory, because it needs access to
    GraphicsPipe and DisplayRegion and other classes in display.  So we put it
    in grutil instead, for lack of any better ideas.
    """

    def __init__(self, host: GraphicsOutput) -> None: ...
    def upcast_to_CullTraverser(self) -> CullTraverser: ...
    def get_buffer(self) -> GraphicsOutput: ...
    def get_texture(self) -> Texture:
        """Returns a Texture that can be used to visualize the efforts of the
        occlusion cull.
        """
    def set_occlusion_mask(self, occlusion_mask: DrawMask | int) -> None:
        """Specifies the DrawMask that should be set on occlusion polygons for this
        scene.  This identifies the polygons that are to be treated as occluders.
        Polygons that do not have this draw mask set will not be considered
        occluders.
        """
    def get_occlusion_mask(self) -> DrawMask:
        """Returns the DrawMask for occlusion polygons.  See set_occlusion_mask()."""
    upcastToCullTraverser = upcast_to_CullTraverser
    getBuffer = get_buffer
    getTexture = get_texture
    setOcclusionMask = set_occlusion_mask
    getOcclusionMask = get_occlusion_mask

class PfmVizzer:
    """This class aids in the visualization and manipulation of PfmFile objects."""

    CT_texcoord2: Final = 0
    CTTexcoord2: Final = 0
    CT_texcoord3: Final = 1
    CTTexcoord3: Final = 1
    CT_vertex1: Final = 2
    CTVertex1: Final = 2
    CT_vertex2: Final = 3
    CTVertex2: Final = 3
    CT_vertex3: Final = 4
    CTVertex3: Final = 4
    CT_normal3: Final = 5
    CTNormal3: Final = 5
    CT_blend1: Final = 6
    CTBlend1: Final = 6
    CT_aux_vertex1: Final = 7
    CTAuxVertex1: Final = 7
    CT_aux_vertex2: Final = 8
    CTAuxVertex2: Final = 8
    CT_aux_vertex3: Final = 9
    CTAuxVertex3: Final = 9
    MF_front: Final = 1
    MFFront: Final = 1
    MF_back: Final = 2
    MFBack: Final = 2
    MF_both: Final = 3
    MFBoth: Final = 3
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, pfm: PfmFile) -> None:
        """The PfmVizzer constructor receives a reference to a PfmFile which it will
        operate on.  It does not keep ownership of this reference; it is your
        responsibility to ensure the PfmFile does not destruct during the lifetime
        of the PfmVizzer.
        """
    @overload
    def __init__(self, __param0: PfmVizzer) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_pfm(self) -> PfmFile:
        """Returns the reference to the PfmFile manipulated by this PfmVizzer."""
    def project(self, lens: Lens, undist_lut: PfmFile = ...) -> None:
        """Adjusts each (x, y, z) point of the Pfm file by projecting it through the
        indicated lens, converting each point to a (u, v, w) texture coordinate.
        The resulting file can be generated to a mesh (with set_vis_inverse(true)
        and generate_vis_mesh()) that will apply the lens distortion to an
        arbitrary texture image.
        """
    def extrude(self, lens: Lens) -> None:
        """Converts each (u, v, depth) point of the Pfm file to an (x, y, z) point, by
        reversing project().  If the original file is only a 1-d file, assumes that
        it is a depth map with implicit (u, v) coordinates.

        This method is only valid for a linear lens (e.g.  a PerspectiveLens or
        OrthographicLens).  Non-linear lenses don't necessarily compute a sensible
        depth coordinate.
        """
    def set_vis_inverse(self, vis_inverse: bool) -> None:
        """Sets the vis_inverse flag.  When this flag is true, vis meshes and point
        clouds are generated with the 3-d depth value in the texture coordinates,
        and the 2-d index value in the vertex position.  When it is false, meshes
        are generated normally, with the 3-d depth value in the vertex position and
        the 2-d index value in the texture coordinates.

        This may be used in lieu of the lower-level add_vis_column().
        """
    def get_vis_inverse(self) -> bool:
        """Returns the vis_inverse flag.  See set_vis_inverse()."""
    def set_flat_texcoord_name(self, flat_texcoord_name: InternalName | str) -> None:
        """If the flat_texcoord_name is specified, it is the name of an additional
        vertex column that will be created for the "flat" texture coordinates, i.e.
        the original 0..1 values that correspond to the 2-D index position of each
        point in the original pfm file.

        These are the same values that will be assigned to the default texture
        coordinates if the vis_inverse flag is *not* true.

        This may be used in lieu of the lower-level add_vis_column().
        """
    def clear_flat_texcoord_name(self) -> None:
        """Resets the flat_texcoord_name to empty, so that additional texture
        coordinates are not created.

        This may be used in lieu of the lower-level add_vis_column().
        """
    def get_flat_texcoord_name(self) -> InternalName:
        """Returns the flat_texcoord_name.  See set_flat_texcoord_name()."""
    def set_vis_2d(self, vis_2d: bool) -> None:
        """Sets the vis_2d flag.  When this flag is true, only the first two (x, y)
        value of each depth point is considered meaningful; the z component is
        ignored.  This is only relevant for generating visualizations.

        This may be used in lieu of the lower-level add_vis_column().
        """
    def get_vis_2d(self) -> bool:
        """Returns the vis_2d flag.  See set_vis_2d()."""
    def set_keep_beyond_lens(self, keep_beyond_lens: bool) -> None:
        """Sets the keep_beyond_lens flag.  When this flag is true, points that fall
        outside of the normal lens range in project() or in add_vis_column() will
        be retained anyway; when it is false, these points will be discarded.
        """
    def get_keep_beyond_lens(self) -> bool:
        """Returns the keep_beyond_lens flag.  See set_keep_beyond_lens()."""
    def set_vis_blend(self, vis_blend: PNMImage) -> None:
        """Specifies a blending map--a grayscale image--that will be applied to the
        vertex color during generate_vis_mesh() and generate_vis_points().  The
        image size must exactly match the mesh size of the PfmVizzer.

        Ownership of the pointer is not kept by the PfmVizzer; it is your
        responsibility to ensure it does not destruct during the lifetime of the
        PfmVizzer (or at least not before your subsequent call to
        generate_vis_mesh()).
        """
    def clear_vis_blend(self) -> None:
        """Removes the blending map set by a prior call to set_vis_blend()."""
    def get_vis_blend(self) -> PNMImage:
        """Returns the blending map set by the most recent call to set_vis_blend(), or
        NULL if there is no blending map in effect.
        """
    def set_aux_pfm(self, pfm: PfmFile) -> None:
        """Assigns an auxiliary PfmFile to this PfmVizzer.  This file will be queried
        by column types CT_aux_vertex1/2/3, but has no other meaning to the vizzer.
        This size of this PfmFile should exactly match the base PfmFile.  No
        reference count is held and no copy is made; the caller is responsible for
        ensuring that the auxiliary PfmFile will persist throughout the lifetime of
        the PfmVizzer it is assigned to.
        """
    def clear_aux_pfm(self) -> None:
        """Removes the auxiliary PfmFile from this PfmVizzer."""
    def get_aux_pfm(self) -> PfmFile:
        """Returns the reference to the auxiliary PfmFile queried by this PfmVizzer.
        This contains the values that will be reflected in CT_aux_vertex3 etc.  See
        set_aux_pfm().
        """
    def clear_vis_columns(self) -> None:
        """Removes all of the previously-added vis columns in preparation for building
        a new list.  See add_vis_column().
        """
    def add_vis_column(
        self,
        source: _PfmVizzer_ColumnType,
        target: _PfmVizzer_ColumnType,
        name: InternalName | str,
        transform: TransformState = ...,
        lens: Lens = ...,
        undist_lut: PfmFile = ...,
    ) -> None:
        """Adds a new vis column specification to the list of vertex data columns that
        will be generated at the next call to generate_vis_points() or
        generate_vis_mesh().  This advanced interface supercedes the higher-level
        set_vis_inverse(), set_flat_texcoord_name(), and set_vis_2d().

        If you use this advanced interface, you must specify explicitly the
        complete list of data columns to be created in the resulting
        GeomVertexData, by calling add_vis_column() each time.  For each column,
        you specify the source of the column in the PFMFile, the target column and
        name in the GeomVertexData, and an optional transform matrix and/or lens to
        transform and project the point before generating it.
        """
    def generate_vis_points(self) -> NodePath:
        """Creates a point cloud with the points of the pfm as 3-d coordinates in
        space, and texture coordinates ranging from 0 .. 1 based on the position
        within the pfm grid.
        """
    def generate_vis_mesh(self, face: _PfmVizzer_MeshFace = ...) -> NodePath:
        """Creates a triangle mesh with the points of the pfm as 3-d coordinates in
        space, and texture coordinates ranging from 0 .. 1 based on the position
        within the pfm grid.
        """
    def calc_max_u_displacement(self) -> float:
        """Computes the maximum amount of shift, in pixels either left or right, of
        any pixel in the distortion map.  This can be passed to
        make_displacement(); see that function for more information.
        """
    def calc_max_v_displacement(self) -> float:
        """Computes the maximum amount of shift, in pixels either up or down, of any
        pixel in the distortion map.  This can be passed to make_displacement();
        see that function for more information.
        """
    def make_displacement(self, result: PNMImage | PfmFile, max_u: float, max_v: float, for_32bit: bool) -> None:
        """`(self, result: PNMImage, max_u: float, max_v: float, for_32bit: bool)`:
        Assuming the underlying PfmFile is a 2-d distortion mesh, with the U and V
        in the first two components and the third component unused, this computes
        an AfterEffects-style displacement map that represents the same distortion.
        The indicated PNMImage will be filled in with a displacement map image,
        with horizontal shift in the red channel and vertical shift in the green
        channel, where a fully bright (or fully black) pixel indicates a shift of
        max_u or max_v pixels.

        Use calc_max_u_displacement() and calc_max_v_displacement() to compute
        suitable values for max_u and max_v.

        This generates an integer 16-bit displacement image.  It is a good idea,
        though not necessarily essential, to check "Preserve RGB" in the interpret
        footage section for each displacement image.  Set for_32bit true if this is
        meant to be used in a 32-bit project file, and false if it is meant to be
        used in a 16-bit project file.

        `(self, result: PfmFile, max_u: float, max_v: float, for_32bit: bool)`:
        Assuming the underlying PfmFile is a 2-d distortion mesh, with the U and V
        in the first two components and the third component unused, this computes
        an AfterEffects-style displacement map that represents the same distortion.
        The indicated PNMImage will be filled in with a displacement map image,
        with horizontal shift in the red channel and vertical shift in the green
        channel, where a fully bright (or fully black) pixel indicates a shift of
        max_u or max_v pixels.

        Use calc_max_u_displacement() and calc_max_v_displacement() to compute
        suitable values for max_u and max_v.

        This generates a 32-bit floating-point displacement image.  It is essential
        to check "Preserve RGB" in the interpret footage section for each
        displacement image.  Set for_32bit true if this is meant to be used in a
        32-bit project file, and false if it is meant to be used in a 16-bit
        project file.
        """
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
