from _typeshed import StrOrBytesPath
from collections.abc import Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import IntVec2Like, Mat4Like, Vec2Like, Vec4Like
from panda3d.core._dtoolbase import TypeHandle
from panda3d.core._dtoolutil import TextEncoder, ostream
from panda3d.core._express import Namable, TypedReferenceCount
from panda3d.core._gobj import Geom, Texture
from panda3d.core._linmath import LColor, LMatrix4, LPoint3, LVecBase2i, LVecBase4, LVector2
from panda3d.core._pgraph import NodePath, PandaNode, RenderState
from panda3d.core._pnmtext import FreetypeFont
from panda3d.core._prc import ConfigVariableFilename

_GeomEnums_UsageHint: TypeAlias = Literal[0, 1, 2, 3, 4]
_SamplerState_FilterType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
_TextFont_RenderMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
_Texture_Format: TypeAlias = int
_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_TextProperties_Alignment: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_TextProperties_Direction: TypeAlias = Literal[0, 1]

class TextGlyph(TypedReferenceCount):
    """A representation of a single glyph (character) from a font.  This is a
    piece of renderable geometry of some kind.
    """

    @property
    def character(self) -> int: ...
    @property
    def state(self) -> RenderState: ...
    @property
    def advance(self) -> float: ...
    def get_character(self) -> int:
        """Returns the Unicode value that corresponds to the character this glyph
        represents.
        """
    def has_quad(self) -> bool:
        """Returns true if this glyph contains the definition for a simple quad,
        rather than a more complex piece of geometry.

        You may still call get_geom() even if this returns true, which will
        synthesize a Geom for this quad.
        """
    def get_quad(self, dimensions: Vec4Like, texcoords: Vec4Like) -> bool:
        """Assuming that this glyph is representable as a textured quad, returns its
        dimensions and UV range.  Returns false if it is not representable as a
        quad, or if it is whitespace.

        The order of the components is left, bottom, right, top.
        """
    def get_state(self) -> RenderState:
        """Returns the state in which the glyph should be rendered."""
    def get_advance(self) -> float:
        """Returns the distance by which the character pointer should be advanced
        after placing this character; i.e.  the approximate width the character
        takes up on the line.
        """
    def is_whitespace(self) -> bool:
        """Returns true if this glyph represents invisible whitespace, or false if it
        corresponds to some visible character.
        """
    def get_geom(self, usage_hint: _GeomEnums_UsageHint) -> Geom:
        """Returns a Geom that renders the particular glyph.  It will be generated if
        necessary.

        This method will always return a copy of the Geom, so the caller is free to
        modify it.
        """
    getCharacter = get_character
    hasQuad = has_quad
    getQuad = get_quad
    getState = get_state
    getAdvance = get_advance
    isWhitespace = is_whitespace
    getGeom = get_geom

class TextFont(TypedReferenceCount, Namable):
    """An encapsulation of a font; i.e.  a set of glyphs that may be assembled
    together by a TextNode to represent a string of text.

    This is just an abstract interface; see StaticTextFont or DynamicTextFont
    for an actual implementation.
    """

    RM_texture: Final = 0
    RMTexture: Final = 0
    RM_wireframe: Final = 1
    RMWireframe: Final = 1
    RM_polygon: Final = 2
    RMPolygon: Final = 2
    RM_extruded: Final = 3
    RMExtruded: Final = 3
    RM_solid: Final = 4
    RMSolid: Final = 4
    RM_distance_field: Final = 5
    RMDistanceField: Final = 5
    RM_invalid: Final = 6
    RMInvalid: Final = 6
    line_height: float
    space_advance: float
    @property
    def valid(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def upcast_to_TypedReferenceCount(self) -> TypedReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def make_copy(self) -> TextFont: ...
    def is_valid(self) -> bool:
        """Returns true if the font is valid and ready to use, false otherwise."""
    def get_line_height(self) -> float:
        """Returns the number of units high each line of text is."""
    def set_line_height(self, line_height: float) -> None:
        """Changes the number of units high each line of text is."""
    def get_space_advance(self) -> float:
        """Returns the number of units wide a space is."""
    def set_space_advance(self, space_advance: float) -> None:
        """Changes the number of units wide a space is."""
    def get_glyph(self, character: int) -> TextGlyph:
        """Gets the glyph associated with the given character code, as well as an
        optional scaling parameter that should be applied to the glyph's geometry
        and advance parameters.  Returns the glyph on success.  On failure, it may
        still return a printable glyph, or it may return NULL.
        """
    def get_kerning(self, first: int, second: int) -> float:
        """Returns the amount by which to offset the second glyph when it directly
        follows the first glyph.  This is an additional offset that is added on top
        of the advance.
        """
    def write(self, out: ostream, indent_level: int) -> None: ...
    upcastToTypedReferenceCount = upcast_to_TypedReferenceCount
    upcastToNamable = upcast_to_Namable
    makeCopy = make_copy
    isValid = is_valid
    getLineHeight = get_line_height
    setLineHeight = set_line_height
    getSpaceAdvance = get_space_advance
    setSpaceAdvance = set_space_advance
    getGlyph = get_glyph
    getKerning = get_kerning

class DynamicTextGlyph(TextGlyph):
    """A specialization on TextGlyph that is generated and stored by a
    DynamicTextFont.  This keeps some additional information, such as where the
    glyph appears on a texture map.
    """

    @property
    def page(self) -> DynamicTextPage: ...
    def get_page(self) -> DynamicTextPage:
        """Returns the DynamicTextPage that this glyph is on."""
    def intersects(self, x: int, y: int, x_size: int, y_size: int) -> bool:
        """Returns true if the particular position this glyph has been assigned to
        overlaps the rectangle whose top left corner is at x, y and whose size is
        given by x_size, y_size, or false otherwise.
        """
    def get_left(self) -> float:
        """Returns the vertex coordinates that can be used when creating a custom text
        renderer.
        """
    def get_bottom(self) -> float:
        """Returns the vertex coordinates that can be used when creating a custom text
        renderer.
        """
    def get_right(self) -> float:
        """Returns the vertex coordinates that can be used when creating a custom text
        renderer.
        """
    def get_top(self) -> float:
        """Returns the vertex coordinates that can be used when creating a custom text
        renderer.
        """
    def get_uv_left(self) -> float:
        """Returns the UV coordinates that can be used when creating a custom text
        renderer.
        """
    def get_uv_bottom(self) -> float:
        """Returns the UV coordinates that can be used when creating a custom text
        renderer.
        """
    def get_uv_right(self) -> float:
        """Returns the UV coordinates that can be used when creating a custom text
        renderer.
        """
    def get_uv_top(self) -> float:
        """Returns the UV coordinates that can be used when creating a custom text
        renderer.
        """
    getPage = get_page
    getLeft = get_left
    getBottom = get_bottom
    getRight = get_right
    getTop = get_top
    getUvLeft = get_uv_left
    getUvBottom = get_uv_bottom
    getUvRight = get_uv_right
    getUvTop = get_uv_top

class DynamicTextPage(Texture):
    """A single "page" of a DynamicTextFont.  This is a single texture that holds
    a number of glyphs for rendering.  The font starts out with one page, and
    will add more as it needs them.
    """

    def __init__(self, __param0: DynamicTextPage) -> None: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_size(self) -> LVecBase2i:
        """Returns the size of the page (texture), in pixels."""
    def get_x_size(self) -> int:
        """Returns the x size of the page (texture), in pixels."""
    def get_y_size(self) -> int:
        """Returns the y size of the page (texture), in pixels."""
    def is_empty(self) -> bool:
        """Returns true if the page has no glyphs, false otherwise."""
    getSize = get_size
    getXSize = get_x_size
    getYSize = get_y_size
    isEmpty = is_empty

class DynamicTextFont(TextFont, FreetypeFont):  # type: ignore[misc]
    """A DynamicTextFont is a special TextFont object that rasterizes its glyphs
    from a standard font file (e.g.  a TTF file) on the fly.  It requires the
    FreeType 2.0 library (or any higher, backward-compatible version).
    """

    point_size: float
    pixels_per_unit: float
    scale_factor: float
    native_antialias: bool
    texture_margin: int
    poly_margin: float
    page_size: LVecBase2i
    minfilter: _SamplerState_FilterType
    magfilter: _SamplerState_FilterType
    anisotropic_degree: int
    render_mode: _TextFont_RenderMode
    fg: LColor
    bg: LColor
    @property
    def font_pixel_size(self) -> int: ...
    @property
    def tex_format(self) -> _Texture_Format: ...
    @property
    def pages(self) -> Sequence[DynamicTextPage]: ...
    @overload
    def __init__(self, copy: ConfigVariableFilename | DynamicTextFont) -> None:
        """`(self, font_filename: Filename, face_index: int = ...)`:
        The constructor expects the name of some font file that FreeType can read,
        along with face_index, indicating which font within the file to load
        (usually 0).

        `(self, font_data: str, data_length: int, face_index: int)`:
        This constructor accepts a table of data representing the font file, loaded
        from some source other than a filename on disk.
        """
    @overload
    def __init__(self, font_filename: StrOrBytesPath, face_index: int = ...) -> None: ...
    @overload
    def __init__(self, font_data: str, data_length: int, face_index: int) -> None: ...
    def upcast_to_TextFont(self) -> TextFont: ...
    def upcast_to_FreetypeFont(self) -> FreetypeFont: ...
    def make_copy(self) -> TextFont:
        """Returns a new copy of the same font."""
    def get_name(self) -> str:
        """Disambiguates the get_name() method between that inherited from TextFont
        and that inherited from FreetypeFont.
        """
    def set_scale_factor(self, scale_factor: float) -> bool:
        """Sets the factor by which the font is rendered larger by the FreeType
        library before being filtered down to its actual size in the texture as
        specified by set_pixels_per_unit().  This may be set to a number larger
        than 1.0 to improve the font's antialiasing (since FreeType doesn't really
        do a swell job of antialiasing by itself).  There is some performance
        implication for setting this different than 1.0, but it is probably small.

        This should only be called before any characters have been requested out of
        the font, or immediately after calling clear().
        """
    def set_texture_margin(self, texture_margin: int) -> None:
        """Sets the number of pixels of padding that is added around the border of
        each glyph before adding it to the texture map.  This reduces the bleed in
        from neighboring glyphs in the texture map.
        """
    def get_texture_margin(self) -> int:
        """Returns the number of pixels of padding that is added around the border of
        each glyph in the texture map.  See set_texture_margin().
        """
    def set_poly_margin(self, poly_margin: float) -> None:
        """Sets the number of pixels of padding that is included around each glyph in
        the generated polygons.  This helps prevent the edges of the glyphs from
        being cut off at small minifications.  It is not related to the amount of
        extra pixels reserved in the texture map (but it should be set somewhat
        smaller than this number, which is controlled by set_texture_margin(), to
        prevent bleed-in from neighboring letters in the texture).
        """
    def get_poly_margin(self) -> float:
        """Returns the number of pixels of padding that is included around each glyph
        in the generated polygons.  See set_poly_margin().
        """
    @overload
    def set_page_size(self, page_size: IntVec2Like) -> None:
        """Sets the x, y size of the textures that are created for the
        DynamicTextFont.
        """
    @overload
    def set_page_size(self, x_size: int, y_size: int) -> None: ...
    def get_page_size(self) -> LVecBase2i:
        """Returns the size of the textures that are created for the DynamicTextFont.
        See set_page_size().
        """
    def get_page_x_size(self) -> int:
        """Returns the x size of the textures that are created for the
        DynamicTextFont.  See set_page_size().
        """
    def get_page_y_size(self) -> int:
        """Returns the y size of the textures that are created for the
        DynamicTextFont.  See set_page_size().
        """
    def set_minfilter(self, filter: _SamplerState_FilterType) -> None:
        """Sets the filter type used when minimizing the textures created for this
        font.
        """
    def get_minfilter(self) -> _SamplerState_FilterType:
        """Returns the filter type used when minimizing the textures created for this
        font.
        """
    def set_magfilter(self, filter: _SamplerState_FilterType) -> None:
        """Sets the filter type used when enlarging the textures created for this
        font.
        """
    def get_magfilter(self) -> _SamplerState_FilterType:
        """Returns the filter type used when enlarging the textures created for this
        font.
        """
    def set_anisotropic_degree(self, anisotropic_degree: int) -> None:
        """Enables or disables anisotropic filtering on the textures created for this
        font.  The default value is specified by the text-anisotropic-degree
        variable.  See Texture::set_anisotropic_degree().
        """
    def get_anisotropic_degree(self) -> int:
        """Returns the current anisotropic degree for textures created for this font.
        See set_anisotropic_degree().
        """
    def set_render_mode(self, render_mode: _TextFont_RenderMode) -> None:
        """Specifies the way the glyphs on this particular font are generated.  The
        default is RM_texture, which is the only mode supported for bitmap fonts.
        Other modes are possible for most modern fonts.
        """
    def get_render_mode(self) -> _TextFont_RenderMode:
        """Returns the way the glyphs on this particular font are generated.  See
        set_render_mode().
        """
    def set_fg(self, fg: Vec4Like) -> None:
        """Changes the color of the foreground pixels of the font as they are rendered
        into the font texture.  The default is (1, 1, 1, 1), or opaque white, which
        allows text created with the font to be colored individually.  Normally,
        you would not change this unless you really need a particular color effect
        to appear in the font itself.

        This should only be called before any characters have been requested out of
        the font, or immediately after calling clear().
        """
    def get_fg(self) -> LColor:
        """Returns the color of the foreground pixels of the font as they are rendered
        into the font texture.  See set_fg().
        """
    def set_bg(self, bg: Vec4Like) -> None:
        """Changes the color of the background pixels of the font as they are rendered
        into the font texture.  The default is (1, 1, 1, 0), or transparent white,
        which allows text created with the font to be colored individually.  (Note
        that it should not generally be (0, 0, 0, 0), which would tend to bleed
        into the foreground color, unless you have also specified a outline color
        of (0, 0, 0, 1)) .

        Normally, you would not change this unless you really need a particular
        color effect to appear in the font itself.

        This should only be called before any characters have been requested out of
        the font, or immediately after calling clear().
        """
    def get_bg(self) -> LColor:
        """Returns the color of the background pixels of the font as they are rendered
        into the font texture.  See set_bg().
        """
    def set_outline(self, outline_color: Vec4Like, outline_width: float, outline_feather: float) -> None:
        """Sets up the font to have an outline around each font letter.  This is
        achieved via a Gaussian post-process as each letter is generated; there is
        some runtime cost for this effect, but it is minimal as each letter is
        normally generated only once and then cached.

        The color is the desired color of the outline, width is the number of
        points beyond the letter that the outline extends (a typical font is 10
        points high), and feather is a number in the range 0.0 .. 1.0 that controls
        the softness of the outline.  Set the width to 0.0 to disable the outline.

        This should only be called before any characters have been requested out of
        the font, or immediately after calling clear().
        """
    def get_outline_color(self) -> LColor:
        """Returns the color of the outline pixels of the font as they are rendered
        into the font texture.  See set_outline().
        """
    def get_outline_width(self) -> float:
        """Returns the width of the outline pixels of the font, as the number of
        points beyond each letter.  See set_outline().
        """
    def get_outline_feather(self) -> float:
        """Returns the softness of the outline pixels of the font, as a value in the
        range 0.0 to 1.0. See set_outline().
        """
    def get_tex_format(self) -> _Texture_Format:
        """Returns the texture format used to render the individual pages.  This is
        set automatically according to the colors selected.
        """
    def get_num_pages(self) -> int:
        """Returns the number of pages associated with the font.  Initially, the font
        has zero pages; when the first piece of text is rendered with the font, it
        will add additional pages as needed.  Each page is a Texture object that
        contains the images for each of the glyphs currently in use somewhere.
        """
    def get_page(self, n: int) -> DynamicTextPage:
        """Returns the nth page associated with the font.  Initially, the font has
        zero pages; when the first piece of text is rendered with the font, it will
        add additional pages as needed.  Each page is a Texture object that
        contains the images for each of the glyphs currently in use somewhere.
        """
    def garbage_collect(self) -> int:
        """Removes all of the glyphs from the font that are no longer being used by
        any Geoms.  Returns the number of glyphs removed.
        """
    def clear(self) -> None:
        """Drops all the glyphs out of the cache and frees any association with any
        previously-generated pages.

        Calling this frequently can result in wasted texture memory, as any
        previously rendered text will still keep a pointer to the old, previously-
        generated pages.  As long as the previously rendered text remains around,
        the old pages will also remain around.
        """
    def get_pages(self) -> tuple[DynamicTextPage, ...]: ...
    upcastToTextFont = upcast_to_TextFont
    upcastToFreetypeFont = upcast_to_FreetypeFont
    makeCopy = make_copy
    getName = get_name
    setScaleFactor = set_scale_factor
    setTextureMargin = set_texture_margin
    getTextureMargin = get_texture_margin
    setPolyMargin = set_poly_margin
    getPolyMargin = get_poly_margin
    setPageSize = set_page_size
    getPageSize = get_page_size
    getPageXSize = get_page_x_size
    getPageYSize = get_page_y_size
    setMinfilter = set_minfilter
    getMinfilter = get_minfilter
    setMagfilter = set_magfilter
    getMagfilter = get_magfilter
    setAnisotropicDegree = set_anisotropic_degree
    getAnisotropicDegree = get_anisotropic_degree
    setRenderMode = set_render_mode
    getRenderMode = get_render_mode
    setFg = set_fg
    getFg = get_fg
    setBg = set_bg
    getBg = get_bg
    setOutline = set_outline
    getOutlineColor = get_outline_color
    getOutlineWidth = get_outline_width
    getOutlineFeather = get_outline_feather
    getTexFormat = get_tex_format
    getNumPages = get_num_pages
    getPage = get_page
    garbageCollect = garbage_collect
    getPages = get_pages

class FontPool:
    """This is the preferred interface for loading fonts for the TextNode system.
    It is similar to ModelPool and TexturePool in that it unifies references to
    the same filename.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def has_font(filename: str) -> bool:
        """Returns true if the font has ever been loaded, false otherwise."""
    @staticmethod
    def verify_font(filename: str) -> bool:
        """Loads the given filename up into a font, if it has not already been loaded,
        and returns true to indicate success, or false to indicate failure.  If
        this returns true, it is guaranteed that a subsequent call to load_font()
        with the same font name will return a valid Font pointer.
        """
    @staticmethod
    def load_font(filename: str) -> TextFont:
        """Loads the given filename up into a font, if it has not already been loaded,
        and returns the new font.  If a font with the same filename was previously
        loaded, returns that one instead.  If the font file cannot be found,
        returns NULL.
        """
    @staticmethod
    def add_font(filename: str, font: TextFont) -> None:
        """Adds the indicated already-loaded font to the pool.  The font will always
        replace any previously-loaded font in the pool that had the same filename.
        """
    @staticmethod
    def release_font(filename: str) -> None:
        """Removes the indicated font from the pool, indicating it will never be
        loaded again; the font may then be freed.  If this function is never
        called, a reference count will be maintained on every font every loaded,
        and fonts will never be freed.
        """
    @staticmethod
    def release_all_fonts() -> None:
        """Releases all fonts in the pool and restores the pool to the empty state."""
    @staticmethod
    def garbage_collect() -> int:
        """Releases only those fonts in the pool that have a reference count of
        exactly 1; i.e.  only those fonts that are not being used outside of the
        pool.  Returns the number of fonts released.
        """
    @staticmethod
    def list_contents(out: ostream) -> None:
        """Lists the contents of the font pool to the indicated output stream."""
    @staticmethod
    def write(out: ostream) -> None:
        """Lists the contents of the font pool to the indicated output stream."""
    hasFont = has_font
    verifyFont = verify_font
    loadFont = load_font
    addFont = add_font
    releaseFont = release_font
    releaseAllFonts = release_all_fonts
    garbageCollect = garbage_collect
    listContents = list_contents

class GeomTextGlyph(Geom):
    """This is a specialization on Geom for containing a primitive intended to
    represent a TextGlyph.  Its sole purpose is to maintain the geom count on
    the glyph, so we can determine the actual usage count on a dynamic glyph
    (and thus know when it is safe to recycle the glyph).
    """

class StaticTextFont(TextFont):
    """A StaticTextFont is loaded up from a model that was previously generated
    via egg-mkfont, and contains all of its glyphs already generated and
    available for use.  It doesn't require linking with any external libraries
    like FreeType.
    """

    def __init__(self, font_def: PandaNode, cs: _CoordinateSystem = ...) -> None:
        """The constructor expects the root node to a model generated via egg-mkfont,
        which consists of a set of models, one per each character in the font.

        If a CoordinateSystem value is specified, it informs the font of the
        coordinate system in which this model was generated.  "up" in this
        coordinate system will be the direction of the top of the letters.
        """

class TextProperties:
    """This defines the set of visual properties that may be assigned to the
    individual characters of the text.  (Properties which affect the overall
    block of text can only be specified on the TextNode directly).

    Typically, there is just one set of properties on a given block of text,
    which is set directly on the TextNode (TextNode inherits from
    TextProperties). That makes all of the text within a particular block have
    the same appearance.

    This separate class exists in order to implement multiple different kinds
    of text appearing within one block.  The text string itself may reference a
    TextProperties structure by name using the \\1 and \\2 tokens embedded within
    the string; each nested TextProperties structure modifies the appearance of
    subsequent text within the block.
    """

    A_left: Final = 0
    ALeft: Final = 0
    A_right: Final = 1
    ARight: Final = 1
    A_center: Final = 2
    ACenter: Final = 2
    A_boxed_left: Final = 3
    ABoxedLeft: Final = 3
    A_boxed_right: Final = 4
    ABoxedRight: Final = 4
    A_boxed_center: Final = 5
    ABoxedCenter: Final = 5
    D_ltr: Final = 0
    DLtr: Final = 0
    D_rtl: Final = 1
    DRtl: Final = 1
    DtoolClassDict: ClassVar[dict[str, Any]]
    font: TextFont
    small_caps: bool
    small_caps_scale: float
    slant: float
    underscore: bool
    underscore_height: float
    align: _TextProperties_Alignment
    indent: float
    wordwrap: float
    preserve_trailing_whitespace: bool
    text_color: LColor
    shadow_color: LColor
    shadow: LVector2
    bin: str
    draw_order: int
    tab_width: float
    glyph_scale: float
    glyph_shift: float
    text_scale: float
    direction: _TextProperties_Direction
    def __init__(self, copy: TextProperties = ...) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def clear(self) -> None:
        """Unsets all properties that have been specified so far, and resets the
        TextProperties structure to its initial empty state.
        """
    def is_any_specified(self) -> bool:
        """Returns true if any properties have been specified, false otherwise."""
    @staticmethod
    def set_default_font(__param0: TextFont) -> None:
        """Specifies the default font to be used for any TextNode whose font is
        uninitialized or NULL.  See set_font().
        """
    @staticmethod
    def get_default_font() -> TextFont:
        """Specifies the default font to be used for any TextNode whose font is
        uninitialized or NULL.  See set_font().
        """
    def set_font(self, font: TextFont) -> None:
        """Sets the font that will be used when making text.  If this is set to NULL,
        the default font will be used, which can be set via set_default_font().
        """
    def clear_font(self) -> None:
        """Restores the default font to the text."""
    def has_font(self) -> bool: ...
    def get_font(self) -> TextFont:
        """Returns the font currently in use, if any.  If no font is in use, this
        returns the default font.
        """
    def set_small_caps(self, small_caps: bool) -> None:
        """Sets the small_caps flag.  When this is set, lowercase letters are
        generated as scaled-down versions of their uppercase equivalents.  This is
        particularly useful to set for fonts that do not have lowercase letters.

        It is also a good idea to set this for a (dynamic) font that has already
        implemented lowercase letters as scaled-down versions of their uppercase
        equivalents, since without this flag the texture memory may needlessly
        duplicate equivalent glyphs for upper and lowercase letters.  Setting this
        flag causes the texture memory to share the mixed-case letters.

        The amount by which the lowercase letters are scaled is specified by
        set_small_caps_scale().
        """
    def clear_small_caps(self) -> None: ...
    def has_small_caps(self) -> bool: ...
    def get_small_caps(self) -> bool:
        """Returns the small_caps flag.  See set_small_caps()."""
    def set_small_caps_scale(self, small_caps_scale: float) -> None:
        """Sets the scale factor applied to lowercase letters from their uppercase
        equivalents, when the small_caps flag is in effect.  See set_small_caps().
        Normally, this will be a number less than one.
        """
    def clear_small_caps_scale(self) -> None: ...
    def has_small_caps_scale(self) -> bool: ...
    def get_small_caps_scale(self) -> float:
        """Returns the scale factor applied to lowercase letters from their uppercase
        equivalents, when the small_caps flag is in effect.  See set_small_caps()
        and set_small_caps_scale().
        """
    def set_slant(self, slant: float) -> None:
        """Specifies the factor by which the text slants to the right."""
    def clear_slant(self) -> None: ...
    def has_slant(self) -> bool: ...
    def get_slant(self) -> float:
        """Returns the factor by which the text is specified to slant to the right."""
    def set_underscore(self, underscore: bool) -> None:
        """Sets the underscore flag.  When this is set, the text is underscored with a
        one-pixel line the same color as the text foreground, drawn at the
        baseline.
        """
    def clear_underscore(self) -> None: ...
    def has_underscore(self) -> bool: ...
    def get_underscore(self) -> bool:
        """Returns the underscore flag.  See set_underscore()."""
    def set_underscore_height(self, underscore_height: float) -> None:
        """Specifies the vertical height of the underscore, relative to the text
        baseline.  This only has meaning if the underscore mode is enabled with
        set_underscore().
        """
    def clear_underscore_height(self) -> None: ...
    def has_underscore_height(self) -> bool: ...
    def get_underscore_height(self) -> float:
        """Returns the vertical height of the underscore; see set_underscore_height()."""
    def set_align(self, align_type: _TextProperties_Alignment) -> None:
        """Specifies the alignment of the text within its margins."""
    def clear_align(self) -> None:
        """Restores the default alignment of the text."""
    def has_align(self) -> bool: ...
    def get_align(self) -> _TextProperties_Alignment: ...
    def set_indent(self, indent: float) -> None:
        """Specifies the amount of extra space that is inserted before the first
        character of each line.  This can be thought of as a left margin.
        """
    def clear_indent(self) -> None:
        """Removes the indent setting from the text.  Text will be as wide as it is."""
    def has_indent(self) -> bool: ...
    def get_indent(self) -> float: ...
    def set_wordwrap(self, wordwrap: float) -> None:
        """Sets the text up to automatically wordwrap when it exceeds the indicated
        width.  This can be thought of as a right margin or margin width.
        """
    def clear_wordwrap(self) -> None:
        """Removes the wordwrap setting from the text.  Text will be as wide as it is."""
    def has_wordwrap(self) -> bool: ...
    def get_wordwrap(self) -> float: ...
    def set_preserve_trailing_whitespace(self, preserve_trailing_whitespace: bool) -> None:
        """Sets the preserve_trailing_whitespace flag.  When this is set, trailing
        whitespace at the end of the line is not stripped when the text is
        wordwrapped (it is stripped by default).  Since the trailing whitespace is
        invisible, this is important primarily for determining the proper width of
        a frame or card behind the text.
        """
    def clear_preserve_trailing_whitespace(self) -> None: ...
    def has_preserve_trailing_whitespace(self) -> bool: ...
    def get_preserve_trailing_whitespace(self) -> bool:
        """Returns the preserve_trailing_whitespace flag.  See
        set_preserve_trailing_whitespace().
        """
    @overload
    def set_text_color(self, text_color: Vec4Like) -> None: ...
    @overload
    def set_text_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def clear_text_color(self) -> None:
        """Removes the text color specification; the text will be colored whatever it
        was in the source font file.
        """
    def has_text_color(self) -> bool: ...
    def get_text_color(self) -> LColor: ...
    @overload
    def set_shadow_color(self, shadow_color: Vec4Like) -> None: ...
    @overload
    def set_shadow_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def clear_shadow_color(self) -> None:
        """Removes the shadow color specification."""
    def has_shadow_color(self) -> bool: ...
    def get_shadow_color(self) -> LColor: ...
    @overload
    def set_shadow(self, shadow_offset: Vec2Like) -> None:
        """Specifies that the text should be drawn with a shadow, by creating a second
        copy of the text and offsetting it slightly behind the first.
        """
    @overload
    def set_shadow(self, xoffset: float, yoffset: float) -> None: ...
    def clear_shadow(self) -> None:
        """Specifies that a shadow will not be drawn behind the text."""
    def has_shadow(self) -> bool: ...
    def get_shadow(self) -> LVector2:
        """Returns the offset of the shadow as set by set_shadow().  It is an error to
        call this if has_shadow() is false.
        """
    def set_bin(self, bin: str) -> None:
        """Names the CullBin that the text geometry should be assigned to.  If this is
        set, then a CullBinAttrib will be created to explicitly place each
        component in the named bin.

        The draw_order value will also be passed to each CullBinAttrib as
        appropriate; this is particularly useful if this names a CullBinFixed, e.g.
        "fixed".
        """
    def clear_bin(self) -> None:
        """Removes the effect of a previous call to set_bin().  Text will be drawn in
        whatever bin it would like to be drawn in, with no explicit ordering.
        """
    def has_bin(self) -> bool:
        """Returns true if an explicit drawing bin has been set via set_bin(), false
        otherwise.
        """
    def get_bin(self) -> str:
        """Returns the drawing bin set with set_bin(), or empty string if no bin has
        been set.
        """
    def set_draw_order(self, draw_order: int) -> int:
        """Sets the drawing order of text created by the TextNode.  This is actually
        the draw order of the card and frame.  The shadow is drawn at
        _draw_order+1, and the text at _draw_order+2.

        This affects the sorting order assigned to the nodes as they are created,
        and also is passed to whatever bin may be assigned via set_bin().

        The return value is the first unused draw_order number, e.g.  _draw_order +
        3.
        """
    def clear_draw_order(self) -> None: ...
    def has_draw_order(self) -> bool: ...
    def get_draw_order(self) -> int:
        """Returns the drawing order set with set_draw_order()."""
    def set_tab_width(self, tab_width: float) -> None:
        """Sets the width of each tab stop, in screen units.  A tab character embedded
        in the text will advance the horizontal position to the next tab stop.
        """
    def clear_tab_width(self) -> None: ...
    def has_tab_width(self) -> bool: ...
    def get_tab_width(self) -> float:
        """Returns the width set via set_tab_width()."""
    def set_glyph_scale(self, glyph_scale: float) -> None:
        """Specifies the factor by which to scale each letter of the text as it is
        placed, in addition to any scales inherited from the node or from
        set_text_scale(). This can be used (possibly in conjunction with
        set_glyph_shift()) to implement superscripting or subscripting.

        The glyph scale is cumulative when applied to nested TextProperties.  It is
        intended primarily for implementing superscripts, not for scaling the text
        in general.  See also set_text_scale(), which is intended primarily for
        scaling the text in general, and is not cumulative.
        """
    def clear_glyph_scale(self) -> None: ...
    def has_glyph_scale(self) -> bool: ...
    def get_glyph_scale(self) -> float:
        """Returns the scale factor of each letter as specified by set_glyph_scale()."""
    def set_glyph_shift(self, glyph_shift: float) -> None:
        """Specifies a vertical amount to shift each letter of the text as it is
        placed.  This can be used (possibly in conjunction with set_glyph_scale())
        to implement superscripting or subscripting.
        """
    def clear_glyph_shift(self) -> None: ...
    def has_glyph_shift(self) -> bool: ...
    def get_glyph_shift(self) -> float:
        """Returns the vertical shift of each letter as specified by
        set_glyph_shift().
        """
    def set_text_scale(self, text_scale: float) -> None:
        """Specifies the factor by which to scale the text, in addition to any
        scalings imposed by the node, as well as in addition to the glyph scale.

        The text scale is not cumulative when applied to nested TextProperties.
        See also set_glyph_scale(), which is cumulative.
        """
    def clear_text_scale(self) -> None: ...
    def has_text_scale(self) -> bool: ...
    def get_text_scale(self) -> float:
        """Returns the scale factor of the text as specified by set_text_scale()."""
    def set_direction(self, direction: _TextProperties_Direction) -> None:
        """Specifies the text direction.  If none is specified, it will be guessed
        based on the contents of the string.

        @since 1.10.0
        """
    def clear_direction(self) -> None:
        """Clears the text direction setting.  If no text direction is specified, it
        will be guessed based on the contents of the string.

        @since 1.10.0
        """
    def has_direction(self) -> bool:
        """@since 1.10.0"""
    def get_direction(self) -> _TextProperties_Direction:
        """Returns the direction of the text as specified by set_direction().

        @since 1.10.0
        """
    def add_properties(self, other: TextProperties) -> None:
        """Sets any properties that are explicitly specified in other on this object.
        Leaves other properties unchanged.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    isAnySpecified = is_any_specified
    setDefaultFont = set_default_font
    getDefaultFont = get_default_font
    setFont = set_font
    clearFont = clear_font
    hasFont = has_font
    getFont = get_font
    setSmallCaps = set_small_caps
    clearSmallCaps = clear_small_caps
    hasSmallCaps = has_small_caps
    getSmallCaps = get_small_caps
    setSmallCapsScale = set_small_caps_scale
    clearSmallCapsScale = clear_small_caps_scale
    hasSmallCapsScale = has_small_caps_scale
    getSmallCapsScale = get_small_caps_scale
    setSlant = set_slant
    clearSlant = clear_slant
    hasSlant = has_slant
    getSlant = get_slant
    setUnderscore = set_underscore
    clearUnderscore = clear_underscore
    hasUnderscore = has_underscore
    getUnderscore = get_underscore
    setUnderscoreHeight = set_underscore_height
    clearUnderscoreHeight = clear_underscore_height
    hasUnderscoreHeight = has_underscore_height
    getUnderscoreHeight = get_underscore_height
    setAlign = set_align
    clearAlign = clear_align
    hasAlign = has_align
    getAlign = get_align
    setIndent = set_indent
    clearIndent = clear_indent
    hasIndent = has_indent
    getIndent = get_indent
    setWordwrap = set_wordwrap
    clearWordwrap = clear_wordwrap
    hasWordwrap = has_wordwrap
    getWordwrap = get_wordwrap
    setPreserveTrailingWhitespace = set_preserve_trailing_whitespace
    clearPreserveTrailingWhitespace = clear_preserve_trailing_whitespace
    hasPreserveTrailingWhitespace = has_preserve_trailing_whitespace
    getPreserveTrailingWhitespace = get_preserve_trailing_whitespace
    setTextColor = set_text_color
    clearTextColor = clear_text_color
    hasTextColor = has_text_color
    getTextColor = get_text_color
    setShadowColor = set_shadow_color
    clearShadowColor = clear_shadow_color
    hasShadowColor = has_shadow_color
    getShadowColor = get_shadow_color
    setShadow = set_shadow
    clearShadow = clear_shadow
    hasShadow = has_shadow
    getShadow = get_shadow
    setBin = set_bin
    clearBin = clear_bin
    hasBin = has_bin
    getBin = get_bin
    setDrawOrder = set_draw_order
    clearDrawOrder = clear_draw_order
    hasDrawOrder = has_draw_order
    getDrawOrder = get_draw_order
    setTabWidth = set_tab_width
    clearTabWidth = clear_tab_width
    hasTabWidth = has_tab_width
    getTabWidth = get_tab_width
    setGlyphScale = set_glyph_scale
    clearGlyphScale = clear_glyph_scale
    hasGlyphScale = has_glyph_scale
    getGlyphScale = get_glyph_scale
    setGlyphShift = set_glyph_shift
    clearGlyphShift = clear_glyph_shift
    hasGlyphShift = has_glyph_shift
    getGlyphShift = get_glyph_shift
    setTextScale = set_text_scale
    clearTextScale = clear_text_scale
    hasTextScale = has_text_scale
    getTextScale = get_text_scale
    setDirection = set_direction
    clearDirection = clear_direction
    hasDirection = has_direction
    getDirection = get_direction
    addProperties = add_properties
    getClassType = get_class_type

class TextGraphic:
    """This defines a special model that has been constructed for the purposes of
    embedding an arbitrary graphic image within a text paragraph.

    It can be any arbitrary model, though it should be built along the same
    scale as the text, and it should probably be at least mostly two-
    dimensional.  Typically, this means it should be constructed in the X-Z
    plane, and it should have a maximum vertical (Z) height of 1.0.

    The frame specifies an arbitrary bounding volume in the form (left, right,
    bottom, top).  This indicates the amount of space that will be reserved
    within the paragraph.  The actual model is not actually required to fit
    within this rectangle, but if it does not, it may visually overlap with
    nearby text.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    model: NodePath
    frame: LVecBase4
    instance_flag: bool
    @overload
    def __init__(self, __param0: TextGraphic = ...) -> None: ...
    @overload
    def __init__(self, model: NodePath, frame: Vec4Like) -> None: ...
    @overload
    def __init__(self, model: NodePath, left: float, right: float, bottom: float, top: float) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_model(self) -> NodePath:
        """Returns the NodePath associated with the graphic, that renders the desired
        image.
        """
    def set_model(self, model: NodePath) -> None:
        """Changes the NodePath associated with the graphic.  This NodePath should
        contain geometry that will render the desired graphic image.
        """
    def get_frame(self) -> LVecBase4:
        """Returns the frame specified for the graphic.  This is the amount of space
        that will be reserved for the graphic when it is embedded in a text
        paragraph, in the form (left, right, bottom, top).

        The actual graphic, as rendered by the NodePath specified via set_model(),
        should more or less fit within this rectangle.  It is not required to fit
        completely within it, but if it does not, it may visually overlap with
        nearby text.
        """
    @overload
    def set_frame(self, frame: Vec4Like) -> None:
        """Specifies the (left, right, bottom, top) bounding frame for the graphic.
        See get_frame().
        """
    @overload
    def set_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_instance_flag(self) -> bool:
        """Returns the instance_flag.  See set_instance_flag()."""
    def set_instance_flag(self, instance_flag: bool) -> None:
        """Sets the instance_flag.  When this is true, the graphic is directly
        instanced to the scene graph whenever it appears; when it is false, the
        graphic is copied.  The default is false, which is best for most
        applications.  You might need to set it true for special kinds of
        "graphics" like interactive elements, for instance a PGEntry.
        """
    getModel = get_model
    setModel = set_model
    getFrame = get_frame
    setFrame = set_frame
    getInstanceFlag = get_instance_flag
    setInstanceFlag = set_instance_flag

class TextPropertiesManager:
    """This defines all of the TextProperties structures that might be referenced
    by name from an embedded text string.

    A text string, as rendered by a TextNode, can contain embedded references
    to one of the TextProperties defined here, by enclosing the name between \\1
    (ASCII 0x01) characters; this causes a "push" to the named state.  All text
    following the closing \\1 character will then be rendered in the new state.
    The next \\2 (ASCII 0x02) character will then restore the previous state for
    subsequent text.

    For instance, "x\\1up\\1n\\2 + y" indicates that the character "x" will be
    rendered in the normal state, the character "n" will be rendered in the
    "up" state, and then " + y" will be rendered in the normal state again.

    This can also be used to define arbitrary models that can serve as embedded
    graphic images in a text paragraph.  This works similarly; the convention
    is to create a TextGraphic that describes the graphic image, and then
    associate it here via the set_graphic() call.  Then "\\5name\\5" will embed
    the named graphic.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def set_properties(self, name: str, properties: TextProperties) -> None:
        """Defines the TextProperties associated with the indicated name.  When the
        name is subsequently encountered in text embedded between \\1 characters in
        a TextNode string, the following text will be rendered with these
        properties.

        If there was already a TextProperties structure associated with this name,
        it is quietly replaced with the new definition.
        """
    def get_properties(self, name: str) -> TextProperties:
        """Returns the TextProperties associated with the indicated name.  If there
        was not previously a TextProperties associated with this name, a warning is
        printed and then a default TextProperties structure is associated with the
        name, and returned.

        Call has_properties() instead to check whether a particular name has been
        defined.
        """
    def has_properties(self, name: str) -> bool:
        """Returns true if a TextProperties structure has been associated with the
        indicated name, false otherwise.  Normally this means set_properties() has
        been called with this name, but because get_properties() will implicitly
        create a default TextProperties structure, it may also mean simply that
        get_properties() has been called with the indicated name.
        """
    def clear_properties(self, name: str) -> None:
        """Removes the named TextProperties structure from the manager."""
    @overload
    def set_graphic(self, name: str, model: NodePath) -> None:
        """`(self, name: str, model: NodePath)`:
        This flavor of set_graphic implicitly creates a frame for the model using
        the model's actual computed bounding volume, as derived from
        NodePath::calc_tight_bounds().  Create a TextGraphic object first if you
        want to have explicit control of the frame.

        `(self, name: str, graphic: TextGraphic)`:
        Defines the TextGraphic associated with the indicated name.  When the name
        is subsequently encountered in text embedded between \\5 characters in a
        TextNode string, the specified graphic will be embedded in the text at that
        point.

        If there was already a TextGraphic structure associated with this name, it
        is quietly replaced with the new definition.
        """
    @overload
    def set_graphic(self, name: str, graphic: TextGraphic) -> None: ...
    def get_graphic(self, name: str) -> TextGraphic:
        """Returns the TextGraphic associated with the indicated name.  If there was
        not previously a TextGraphic associated with this name, a warning is
        printed and then a default TextGraphic structure is associated with the
        name, and returned.

        Call has_graphic() instead to check whether a particular name has been
        defined.
        """
    def has_graphic(self, name: str) -> bool:
        """Returns true if a TextGraphic structure has been associated with the
        indicated name, false otherwise.  Normally this means set_graphic() has
        been called with this name, but because get_graphic() will implicitly
        create a default TextGraphic structure, it may also mean simply that
        get_graphic() has been called with the indicated name.
        """
    def clear_graphic(self, name: str) -> None:
        """Removes the named TextGraphic structure from the manager."""
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    @staticmethod
    def get_global_ptr() -> TextPropertiesManager:
        """Returns the pointer to the global TextPropertiesManager object."""
    setProperties = set_properties
    getProperties = get_properties
    hasProperties = has_properties
    clearProperties = clear_properties
    setGraphic = set_graphic
    getGraphic = get_graphic
    hasGraphic = has_graphic
    clearGraphic = clear_graphic
    getGlobalPtr = get_global_ptr

class TextAssembler:
    """This class is not normally used directly by user code, but is used by the
    TextNode to lay out a block of text and convert it into rows of Geoms
    according to the TextProperties.  However, user code may take advantage of
    it, if desired, for very low-level text operations.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    usage_hint: _GeomEnums_UsageHint
    max_rows: int
    dynamic_merge: bool
    multiline_mode: bool
    properties: TextProperties
    @overload
    def __init__(self, copy: TextAssembler) -> None: ...
    @overload
    def __init__(self, encoder: TextEncoder) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def clear(self) -> None:
        """Reinitializes the contents of the TextAssembler."""
    def set_usage_hint(self, usage_hint: _GeomEnums_UsageHint) -> None:
        """Specifies the UsageHint that will be applied to generated geometry.  The
        default is UH_static, which is probably the right setting, but if you know
        the TextNode's geometry will have a short lifespan, it may be better to set
        it to UH_stream.  See geomEnums.h.
        """
    def get_usage_hint(self) -> _GeomEnums_UsageHint:
        """Returns the UsageHint that will be applied to generated geometry.  See
        set_usage_hint().
        """
    def set_max_rows(self, max_rows: int) -> None:
        """If max_rows is greater than zero, no more than max_rows will be accepted.
        Text beyond that will be truncated.

        Setting this will not truncate text immediately.  You must follow this up
        with a call to set_wtext() to truncate the existing text.
        """
    def get_max_rows(self) -> int:
        """If max_rows is greater than zero, no more than max_rows will be accepted.
        Text beyond that will be truncated.
        """
    def set_dynamic_merge(self, dynamic_merge: bool) -> None:
        """Sets the dynamic_merge flag.  See TextNode::set_flatten_flags()."""
    def get_dynamic_merge(self) -> bool:
        """Returns the dynamic_merge flag.  See TextNode::set_flatten_flags()."""
    def set_multiline_mode(self, flag: bool) -> None:
        """Sets the multiline mode flag.  Set the multiline mode to allow text to
        wrap.  It defaults to true.
        """
    def get_multiline_mode(self) -> bool:
        """Returns the multline_mode flag.  See TextNode::set_multiline_mode()."""
    def set_properties(self, properties: TextProperties) -> None:
        """Specifies the default TextProperties that are applied to the text in the
        absence of any nested property change sequences.
        """
    @overload
    def get_properties(self, n: int = ...) -> TextProperties:
        """`(self)`:
        Returns the default TextProperties that are applied to the text in the
        absence of any nested property change sequences.

        `(self, n: int)`:
        Returns the TextProperties in effect for the object at the indicated
        position in the pre-wordwrapped string.

        `(self, r: int, c: int)`:
        Returns the TextProperties in effect for the object at the indicated
        position in the indicated row.
        """
    @overload
    def get_properties(self, r: int, c: int) -> TextProperties: ...
    def set_wtext(self, wtext: str) -> bool:
        """Accepts a new text string and associated properties structure, and
        precomputes the wordwrapping layout appropriately.  After this call,
        get_wordwrapped_wtext() and get_num_rows() can be called.

        The return value is true if all the text is accepted, or false if some was
        truncated (see set_max_rows()).
        """
    def set_wsubstr(self, wtext: str, start: int, count: int) -> bool:
        """Replaces the 'count' characters from 'start' of the current text with the
        indicated replacement text.  If the replacement text does not have count
        characters, the length of the string will be changed accordingly.

        The substring may include nested formatting characters, but they must be
        self-contained and self-closed.  The formatting characters are not
        literally saved in the internal string; they are parsed at the time of the
        set_wsubstr() call.

        The return value is true if all the text is accepted, or false if some was
        truncated (see set_max_rows()).
        """
    def get_plain_wtext(self) -> str:
        """Returns a wstring that represents the contents of the text, without any
        embedded properties characters.  If there is an embedded graphic object, a
        zero value is inserted in that position.

        This string has the same length as get_num_characters(), and the characters
        in this string correspond one-to-one with the characters returned by
        get_character(n).
        """
    def get_wordwrapped_plain_wtext(self) -> str:
        """Returns a wstring that represents the contents of the text, with newlines
        inserted according to the wordwrapping.  The string will contain no
        embedded properties characters.  If there is an embedded graphic object, a
        zero value is inserted in that position.

        This string has the same number of newline characters as get_num_rows(),
        and the characters in this string correspond one-to-one with the characters
        returned by get_character(r, c).
        """
    def get_wtext(self) -> str:
        """Returns a wstring that represents the contents of the text.

        The string will contain embedded properties characters, which may not
        exactly match the embedded properties characters of the original string,
        but it will encode the same way.
        """
    def get_wordwrapped_wtext(self) -> str:
        """Returns a wstring that represents the contents of the text, with newlines
        inserted according to the wordwrapping.

        The string will contain embedded properties characters, which may not
        exactly match the embedded properties characters of the original string,
        but it will encode the same way.

        Embedded properties characters will be closed before every newline, then
        reopened (if necessary) on the subsequent character following the newline.
        This means it will be safe to divide the text up at the newline characters
        and treat each line as an independent piece.
        """
    def calc_r(self, n: int) -> int:
        """Computes the row index of the nth character or graphic object in the text
        and returns it.

        If the nth character is not a normal printable character with a position in
        the wordwrapped string, returns -1 (for instance, a soft-hyphen character,
        or a newline character, may not have a corresponding position).
        """
    def calc_c(self, n: int) -> int:
        """Computes the column index of the nth character or graphic object in the
        text and returns it.

        If the nth character is not a normal printable character with a position in
        the wordwrapped string, returns -1 (for instance, a soft-hyphen character,
        or a newline character, may not have a corresponding position).
        """
    def calc_index(self, r: int, c: int) -> int:
        """Computes the character index of the character at the rth row and cth column
        position.  This is the inverse of calc_r_c().

        It is legal for c to exceed the index number of the last column by 1, and
        it is legal for r to exceed the index number of the last row by 1, if c is
        0.
        """
    def get_num_characters(self) -> int:
        """Returns the number of characters of text, before wordwrapping."""
    @overload
    def get_character(self, n: int) -> int:
        """`(self, n: int)`:
        Returns the character at the indicated position in the pre-wordwrapped
        string.  If the object at this position is a graphic object instead of a
        character, returns 0.

        `(self, r: int, c: int)`:
        Returns the character at the indicated position in the indicated row.  If
        the object at this position is a graphic object instead of a character,
        returns 0.
        """
    @overload
    def get_character(self, r: int, c: int) -> int: ...
    @overload
    def get_graphic(self, n: int) -> TextGraphic:
        """`(self, n: int)`:
        Returns the graphic object at the indicated position in the pre-wordwrapped
        string.  If the object at this position is a character instead of a graphic
        object, returns NULL.

        `(self, r: int, c: int)`:
        Returns the graphic object at the indicated position in the indicated row.
        If the object at this position is a character instead of a graphic object,
        returns NULL.
        """
    @overload
    def get_graphic(self, r: int, c: int) -> TextGraphic: ...
    @overload
    def get_width(self, n: int) -> float:
        """`(self, n: int)`:
        Returns the width of the character or object at the indicated position in
        the pre-wordwrapped string.

        `(self, r: int, c: int)`:
        Returns the width of the character or object at the indicated position in
        the indicated row.
        """
    @overload
    def get_width(self, r: int, c: int) -> float: ...
    def get_num_rows(self) -> int:
        """Returns the number of rows of text after it has all been wordwrapped and
        assembled.
        """
    def get_num_cols(self, r: int) -> int:
        """Returns the number of characters and/or graphic objects in the nth row."""
    def get_xpos(self, r: int, c: int) -> float:
        """Returns the x position of the origin of the character or graphic object at
        the indicated position in the indicated row.

        It is legal for c to exceed the index number of the last column by 1, and
        it is legal for r to exceed the index number of the last row by 1, if c is
        0.
        """
    def get_ypos(self, r: int, c: int) -> float:
        """Returns the y position of the origin of all of the characters or graphic
        objects in the indicated row.

        It is legal for r to exceed the index number of the last row by 1.  The
        value of c is presently ignored.
        """
    def assemble_text(self) -> PandaNode:
        """Actually assembles all of the text into a GeomNode, and returns the node
        (or possibly a parent of the node, to keep the shadow separate).  Once this
        has been called, you may query the extents of the text via get_ul(),
        get_lr().
        """
    def get_ul(self) -> LVector2:
        """Returns the upper-left corner of the assembled text, in 2-d text
        coordinates.
        """
    def get_lr(self) -> LVector2:
        """Returns the lower-right corner of the assembled text, in 2-d text
        coordinates.
        """
    @overload
    @staticmethod
    def calc_width(graphic: TextGraphic, properties: TextProperties) -> float:
        """`(graphic: TextGraphic, properties: TextProperties)`:
        Returns the width of a single TextGraphic image.

        `(character: int, properties: TextProperties)`:
        Returns the width of a single character, according to its associated font.
        This also correctly calculates the width of cheesy ligatures and accented
        characters, which may not exist in the font as such.

        This does not take kerning into account, however.
        """
    @overload
    @staticmethod
    def calc_width(character: int, properties: TextProperties) -> float: ...
    @staticmethod
    def has_exact_character(character: int, properties: TextProperties) -> bool:
        """Returns true if the named character exists in the font exactly as named,
        false otherwise.  Note that because Panda can assemble glyphs together
        automatically using cheesy accent marks, this is not a reliable indicator
        of whether a suitable glyph can be rendered for the character.  For that,
        use has_character() instead.

        This returns true for whitespace and Unicode whitespace characters (if they
        exist in the font), but returns false for characters that would render with
        the "invalid glyph".  It also returns false for characters that would be
        synthesized within Panda, but see has_character().
        """
    @staticmethod
    def has_character(character: int, properties: TextProperties) -> bool:
        """Returns true if the named character exists in the font or can be
        synthesized by Panda, false otherwise.  (Panda can synthesize some accented
        characters by combining similar-looking glyphs from the font.)

        This returns true for whitespace and Unicode whitespace characters (if they
        exist in the font), but returns false for characters that would render with
        the "invalid glyph".
        """
    @staticmethod
    def is_whitespace(character: int, properties: TextProperties) -> bool:
        """Returns true if the indicated character represents whitespace in the font,
        or false if anything visible will be rendered for it.

        This returns true for whitespace and Unicode whitespace characters (if they
        exist in the font), and returns false for any other characters, including
        characters that do not exist in the font (these would be rendered with the
        "invalid glyph", which is visible).

        Note that this function can be reliably used to identify Unicode whitespace
        characters only if the font has all of the whitespace characters defined.
        It will return false for any character not in the font, even if it is an
        official Unicode whitespace character.
        """
    setUsageHint = set_usage_hint
    getUsageHint = get_usage_hint
    setMaxRows = set_max_rows
    getMaxRows = get_max_rows
    setDynamicMerge = set_dynamic_merge
    getDynamicMerge = get_dynamic_merge
    setMultilineMode = set_multiline_mode
    getMultilineMode = get_multiline_mode
    setProperties = set_properties
    getProperties = get_properties
    setWtext = set_wtext
    setWsubstr = set_wsubstr
    getPlainWtext = get_plain_wtext
    getWordwrappedPlainWtext = get_wordwrapped_plain_wtext
    getWtext = get_wtext
    getWordwrappedWtext = get_wordwrapped_wtext
    calcR = calc_r
    calcC = calc_c
    calcIndex = calc_index
    getNumCharacters = get_num_characters
    getCharacter = get_character
    getGraphic = get_graphic
    getWidth = get_width
    getNumRows = get_num_rows
    getNumCols = get_num_cols
    getXpos = get_xpos
    getYpos = get_ypos
    assembleText = assemble_text
    getUl = get_ul
    getLr = get_lr
    calcWidth = calc_width
    hasExactCharacter = has_exact_character
    hasCharacter = has_character
    isWhitespace = is_whitespace

class TextNode(PandaNode, TextEncoder, TextProperties):  # type: ignore[misc]
    """The primary interface to this module.  This class does basic text assembly;
    given a string of text and a TextFont object, it creates a piece of
    geometry that may be placed in the 3-d or 2-d world to represent the
    indicated text.

    The TextNode may be used in one of two ways.  Naively, it may simply be
    parented directly into the scene graph and rendered as if it were a
    GeomNode; in this mode, the actual polygon geometry that renders the text
    is not directly visible or accessible, but remains hidden within the
    TextNode.

    The second way TextNode may be used is as a text generator.  To use it in
    this way, do not parent the TextNode to the scene graph; instead, set the
    properties of the text and call generate() to return an ordinary node,
    containing ordinary geometry, which you may use however you like.  Each
    time you call generate() a new node is returned.
    """

    FF_none: Final = 0
    FFNone: Final = 0
    FF_light: Final = 1
    FFLight: Final = 1
    FF_medium: Final = 2
    FFMedium: Final = 2
    FF_strong: Final = 4
    FFStrong: Final = 4
    FF_dynamic_merge: Final = 8
    FFDynamicMerge: Final = 8
    max_rows: int
    frame_color: LColor
    card_color: LColor
    card_texture: Texture
    frame_line_width: float
    frame_corners: bool
    transform: LMatrix4  # type: ignore[assignment]
    coordinate_system: _CoordinateSystem
    usage_hint: _GeomEnums_UsageHint
    flatten_flags: int
    font: TextFont
    """Returns the font currently in use, if any.  If no font is in use, this
    returns the default font.
    """
    small_caps: bool
    """Returns the small_caps flag.  See set_small_caps()."""
    small_caps_scale: float
    """Returns the scale factor applied to lowercase letters from their uppercase
    equivalents, when the small_caps flag is in effect.  See set_small_caps()
    and set_small_caps_scale().
    """
    slant: float
    """Returns the factor by which the text is specified to slant to the right."""
    underscore: bool
    """Returns the underscore flag.  See set_underscore()."""
    underscore_height: float
    """Returns the vertical height of the underscore; see set_underscore_height()."""
    preserve_trailing_whitespace: bool
    """Returns the preserve_trailing_whitespace flag.  See
    set_preserve_trailing_whitespace().
    """
    shadow: LVector2
    """Returns the offset of the shadow as set by set_shadow().  It is an error to
    call this if has_shadow() is false.
    """
    bin: str
    """Returns the drawing bin set with set_bin(), or empty string if no bin has
    been set.
    """
    draw_order: int
    """Returns the drawing order set with set_draw_order()."""
    tab_width: float
    """Returns the width set via set_tab_width()."""
    glyph_scale: float
    """Returns the scale factor of each letter as specified by set_glyph_scale()."""
    glyph_shift: float
    """Returns the vertical shift of each letter as specified by
    set_glyph_shift().
    """
    text_scale: float
    """Returns the scale factor of the text as specified by set_text_scale()."""
    def __init__(self, name: str, copy: TextProperties = ...) -> None:
        """It's sort of a copy constructor: it copies the indicated TextProperties,
        without copying a complete TextNode.
        """
    def upcast_to_PandaNode(self) -> PandaNode: ...
    def upcast_to_TextEncoder(self) -> TextEncoder: ...
    def upcast_to_TextProperties(self) -> TextProperties: ...
    def get_line_height(self) -> float:
        """Returns the number of units high each line of text is.  This is based on
        the font.  Note that it is possible for the text to include nested font
        change commands, in which case the value of this method is questionable.
        """
    def set_max_rows(self, max_rows: int) -> None:
        """Sets the maximum number of rows that may be formatted by the TextNode.  If
        more text than this is attempted, it will be truncated and has_overflow()
        will return true.
        """
    def clear_max_rows(self) -> None:
        """Resets the TextNode's default behavior of not limiting the number of rows
        of text.
        """
    def has_max_rows(self) -> bool:
        """Returns true if a limit on the height of the TextNode has been set via
        set_max_rows(), false otherwise.
        """
    def get_max_rows(self) -> int:
        """Returns the limit on the height of the TextNode specified by
        set_max_rows().
        """
    def has_overflow(self) -> bool:
        """Returns true if the last text set on the text node exceeded the max_rows
        constraint, or false if it all fit.
        """
    @overload
    def set_frame_color(self, frame_color: Vec4Like) -> None: ...
    @overload
    def set_frame_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def get_frame_color(self) -> LColor: ...
    def set_card_border(self, size: float, uv_portion: float) -> None: ...
    def clear_card_border(self) -> None: ...
    def get_card_border_size(self) -> float: ...
    def get_card_border_uv_portion(self) -> float: ...
    def has_card_border(self) -> bool: ...
    @overload
    def set_card_color(self, card_color: Vec4Like) -> None: ...
    @overload
    def set_card_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def get_card_color(self) -> LColor: ...
    def set_card_texture(self, card_texture: Texture) -> None: ...
    def clear_card_texture(self) -> None: ...
    def has_card_texture(self) -> bool: ...
    def get_card_texture(self) -> Texture: ...
    def set_frame_as_margin(self, left: float, right: float, bottom: float, top: float) -> None:
        """Specifies that a border will be drawn around the text when it is next
        created.  The parameters are the amount of additional padding to insert
        between the frame and the text in each dimension, and all should generally
        be positive.
        """
    def set_frame_actual(self, left: float, right: float, bottom: float, top: float) -> None:
        """Similar to set_frame_as_margin, except the frame is specified in actual
        coordinate units (relative to the text's origin), irrespective of the size
        of the text.  The left and bottom coordinates should generally be negative,
        while the right and top coordinates should generally be positive.
        """
    def clear_frame(self) -> None:
        """Specifies that a border will not be drawn around the text."""
    def has_frame(self) -> bool: ...
    def is_frame_as_margin(self) -> bool:
        """If this is true, the frame was set via a call to set_frame_as_margin(), and
        the dimension of the frame as returned by get_frame_as_set() represent a
        margin all around the text.  If false, then the frame was set via a call to
        set_frame_actual(), and the dimensions of the frame as returned by
        get_frame_as_set() are relative to the text's origin.
        """
    def get_frame_as_set(self) -> LVecBase4:
        """Returns the dimensions of the frame as set by set_frame_as_margin() or
        set_frame_actual().  Use is_frame_actual() to determine how to interpret
        the values returned by this function.  It is an error to call this if
        has_frame() is false.
        """
    def get_frame_actual(self) -> LVecBase4:
        """Returns the actual dimensions of the frame around the text.  If the frame
        was set via set_frame_as_margin(), the result returned by this function
        reflects the size of the current text; if the frame was set via
        set_frame_actual(), this returns the values actually set.

        If the text has no frame at all, this returns the dimensions of the text
        itself, as if the frame were set with a margin of 0, 0, 0, 0.
        """
    def set_frame_line_width(self, line_width: float) -> None:
        """Specifies the thickness of the lines that will be used to draw the frame."""
    def get_frame_line_width(self) -> float:
        """Returns the thickness of the lines that will be used to draw the frame."""
    def set_frame_corners(self, corners: bool) -> None:
        """Enables or disables the drawing of corners for the frame.  These are extra
        points drawn at each of the four corners, to soften the ugly edges
        generated when the line width is greater than one.
        """
    def get_frame_corners(self) -> bool: ...
    def set_card_as_margin(self, left: float, right: float, bottom: float, top: float) -> None:
        """Specifies that a (possibly opaque or semitransparent) card will be held
        behind the text when it is next created.  Like set_frame_as_margin, the
        parameters are the amount of additional padding to insert around the text
        in each dimension, and all should generally be positive.
        """
    def set_card_actual(self, left: float, right: float, bottom: float, top: float) -> None:
        """Similar to set_card_as_margin, except the card is specified in actual
        coordinate units (relative to the text's origin), irrespective of the size
        of the text.  The left and bottom coordinates should generally be negative,
        while the right and top coordinates should generally be positive.
        """
    def set_card_decal(self, card_decal: bool) -> None:
        """Sets the card_decal flag.  When this is true, the text is decalled onto the
        card, which is necessary if the TextNode is to be rendered in the 3-d world
        without putting it in a bin.
        """
    def clear_card(self) -> None:
        """Specifies that a card will not be drawn behind the text."""
    def has_card(self) -> bool: ...
    def get_card_decal(self) -> bool:
        """Returns the card_decal flag.  See set_card_decal()."""
    def is_card_as_margin(self) -> bool:
        """If this is true, the card was set via a call to set_card_as_margin(), and
        the dimension of the card as returned by get_card_as_set() represent a
        margin all around the text.  If false, then the card was set via a call to
        set_card_actual(), and the dimensions of the card as returned by
        get_card_as_set() are relative to the text's origin.
        """
    def get_card_as_set(self) -> LVecBase4:
        """Returns the dimensions of the card as set by set_card_as_margin() or
        set_card_actual().  Use is_card_actual() to determine how to interpret the
        values returned by this function.  It is an error to call this if
        has_card() is false.
        """
    def get_card_actual(self) -> LVecBase4:
        """Returns the actual dimensions of the card around the text.  If the card was
        set via set_card_as_margin(), the result returned by this function reflects
        the size of the current text; if the card was set via set_card_actual(),
        this returns the values actually set.

        If the text has no card at all, this returns the dimensions of the text
        itself, as if the card were set with a margin of 0, 0, 0, 0.
        """
    def get_card_transformed(self) -> LVecBase4:
        """Returns the actual card dimensions, transformed by the matrix set by
        set_transform().  This returns the card dimensions in actual coordinates as
        seen by the rest of the world.  Also see get_upper_left_3d() and
        get_lower_right_3d().
        """
    def set_transform(self, transform: Mat4Like) -> None:  # type: ignore[override]
        """Sets an additional transform that is applied to the entire text paragraph."""
    def get_transform(self) -> LMatrix4: ...  # type: ignore[override]
    def set_coordinate_system(self, cs: _CoordinateSystem) -> None:
        """Specifies the coordinate system in which the text will be generated."""
    def get_coordinate_system(self) -> _CoordinateSystem: ...
    def set_usage_hint(self, usage_hint: _GeomEnums_UsageHint) -> None:
        """Specifies the UsageHint that will be applied to generated geometry.  The
        default is UH_static, which is probably the right setting, but if you know
        the TextNode's geometry will have a short lifespan, it may be better to set
        it to UH_stream.  See geomEnums.h.
        """
    def get_usage_hint(self) -> _GeomEnums_UsageHint:
        """Returns the UsageHint that will be applied to generated geometry.  See
        set_usage_hint().
        """
    def set_flatten_flags(self, flatten_flags: int) -> None:
        """Sets the flatten flags.  This should be a union of the
        TextNode::FlattenFlags options.  This controls the degree of flattening
        performed on the TextNode's internal geometry (i.e.  the scene graph
        returned by generate()) each time the text is changed.  In general, more
        flattening means a more optimal result, but it will take more time to
        generate.

        The choice may be any of these three:

        FF_none - No flatten operation is called.  The letters are left as
        independent Geoms.

        FF_light - A flatten_light() operation is called.  The attributes are
        applied to the vertices, but no nodes are removed.

        FF_medium - A flatten_medium() operation is called.  The attributes are
        applied to the vertices, and a few trivial nodes are removed.

        FF_strong - A flatten_strong() operation is called.  The attributes are
        applied to the vertices, and the resulting nodes are aggressively combined
        into as few nodes as possible.

        In addition to the above choices, you may optionally include the following
        flag:

        FF_dynamic_merge - Copy the geoms into a single GeomVertexData as we go,
        instead of relying on the flatten operation at the end.  This pre-flattens
        the text considerably, and may obviate the need for flatten altogether; it
        also tends to improve performance considerably even if you do call flatten.
        However, it is not as fast as not calling flatten at all.

        The default is taken from the text-flatten and text-dynamic-merge config
        variables.
        """
    def get_flatten_flags(self) -> int:
        """Returns the flatten flags.  See set_flatten_flags()."""
    def clear_font(self) -> None:
        """Resets the font to the default font."""
    def clear_wordwrap(self) -> None:
        """Removes the wordwrap setting from the TextNode.  Text will be as wide as it
        is.
        """
    def set_bin(self, bin: str) -> None:
        """Names the GeomBin that the TextNode geometry should be assigned to.  If
        this is set, then a GeomBinTransition will be created to explicitly place
        each component in the named bin.

        The draw_order value will also be passed to each GeomBinTransition as
        appropriate; this is particularly useful if this names a GeomBinFixed, e.g.
        "fixed".
        """
    def set_draw_order(self, draw_order: int) -> int:
        """Sets the drawing order of text created by the TextMaker.  This is actually
        the draw order of the card and frame.  The shadow is drawn at
        _draw_order+1, and the text at _draw_order+2.

        This affects the sorting order assigned to the arcs as they are created,
        and also is passed to whatever bin may be assigned via set_bin().

        The return value is the first unused draw_order number, e.g.  _draw_order +
        3.
        """
    def set_glyph_scale(self, glyph_scale: float) -> None:
        """Specifies the factor by which to scale each letter of the text as it is
        placed.  This can be used (possibly in conjunction with set_glyph_shift())
        to implement superscripting or subscripting.
        """
    def get_wordwrapped_text(self) -> str:
        """Returns a string that represents the contents of the text, as it has been
        formatted by wordwrap rules.

        In earlier versions, this did not contain any embedded special characters
        like \\1 or \\3; now it does.
        """
    @overload
    def calc_width(self, line: str) -> float:
        """`(self, line: str)`:
        Returns the width of a line of text of arbitrary characters.  The line
        should not include the newline character.

        `(self, line: str)`:
        Returns the width of a line of text of arbitrary characters.  The line
        should not include the newline character or any embedded control characters
        like \\1 or \\3.

        `(self, character: int)`:
        Returns the width of a single character of the font, or 0.0 if the
        character is not known.  This may be a wide character (greater than 255).
        """
    @overload
    def calc_width(self, character: int) -> float: ...
    def has_exact_character(self, character: int) -> bool:
        """Returns true if the named character exists in the font exactly as named,
        false otherwise.  Note that because Panda can assemble glyphs together
        automatically using cheesy accent marks, this is not a reliable indicator
        of whether a suitable glyph can be rendered for the character.  For that,
        use has_character() instead.

        This returns true for whitespace and Unicode whitespace characters (if they
        exist in the font), but returns false for characters that would render with
        the "invalid glyph".  It also returns false for characters that would be
        synthesized within Panda, but see has_character().
        """
    def has_character(self, character: int) -> bool:
        """Returns true if the named character exists in the font or can be
        synthesized by Panda, false otherwise.  (Panda can synthesize some accented
        characters by combining similar-looking glyphs from the font.)

        This returns true for whitespace and Unicode whitespace characters (if they
        exist in the font), but returns false for characters that would render with
        the "invalid glyph".
        """
    def is_whitespace(self, character: int) -> bool:
        """Returns true if the indicated character represents whitespace in the font,
        or false if anything visible will be rendered for it.

        This returns true for whitespace and Unicode whitespace characters (if they
        exist in the font), and returns false for any other characters, including
        characters that do not exist in the font (these would be rendered with the
        "invalid glyph", which is visible).

        Note that this function can be reliably used to identify Unicode whitespace
        characters only if the font has all of the whitespace characters defined.
        It will return false for any character not in the font, even if it is an
        official Unicode whitespace character.
        """
    def get_wordwrapped_wtext(self) -> str:
        """Returns a wstring that represents the contents of the text, as it has been
        formatted by wordwrap rules.

        In earlier versions, this did not contain any embedded special characters
        like \\1 or \\3; now it does.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def get_left(self) -> float:
        """Returns the leftmost extent of the text in local 2-d coordinates,
        unmodified by the set_transform() matrix.
        """
    def get_right(self) -> float:
        """Returns the rightmost extent of the text in local 2-d coordinates,
        unmodified by the set_transform() matrix.
        """
    def get_bottom(self) -> float:
        """Returns the bottommost extent of the text in local 2-d coordinates,
        unmodified by the set_transform() matrix.
        """
    def get_top(self) -> float:
        """Returns the topmost extent of the text in local 2-d coordinates, unmodified
        by the set_transform() matrix.
        """
    def get_height(self) -> float:
        """Returns the net height of the text in local 2-d coordinates."""
    def get_width(self) -> float:
        """Returns the net width of the text in local 2-d coordinates."""
    def get_upper_left_3d(self) -> LPoint3:
        """Returns the upper-left extent of the text object, after it has been
        transformed into 3-d space by applying the set_transform() matrix.
        """
    def get_lower_right_3d(self) -> LPoint3:
        """Returns the lower-right extent of the text object, after it has been
        transformed into 3-d space by applying the set_transform() matrix.
        """
    def get_num_rows(self) -> int:
        """Returns the number of rows of text that were generated.  This counts word-
        wrapped rows as well as rows generated due to embedded newlines.
        """
    def generate(self) -> PandaNode:
        """Generates the text, according to the parameters indicated within the
        TextNode, and returns a Node that may be parented within the tree to
        represent it.
        """
    def update(self) -> None:
        """Can be called after the TextNode has been fully configured, to force the
        node to recompute its text immediately, rather than waiting for it to be
        drawn.  This call is optional.
        """
    def force_update(self) -> None:
        """Forces the TextNode to recompute itself now, even if it believes nothing
        has changed.  Normally, this should not need to be called, but it may be
        useful if some properties change outside of the TextNode's knowledge (for
        instance, within the font).
        """
    def get_internal_geom(self) -> PandaNode:
        """Returns the actual node that is used internally to render the text, if the
        TextNode is parented within the scene graph.

        In general, you should not call this method.  Call generate() instead if
        you want to get a handle to geometry that represents the text.  This method
        is provided as a debugging aid only.
        """
    upcastToPandaNode = upcast_to_PandaNode
    upcastToTextEncoder = upcast_to_TextEncoder
    upcastToTextProperties = upcast_to_TextProperties
    getLineHeight = get_line_height
    setMaxRows = set_max_rows
    clearMaxRows = clear_max_rows
    hasMaxRows = has_max_rows
    getMaxRows = get_max_rows
    hasOverflow = has_overflow
    setFrameColor = set_frame_color
    getFrameColor = get_frame_color
    setCardBorder = set_card_border
    clearCardBorder = clear_card_border
    getCardBorderSize = get_card_border_size
    getCardBorderUvPortion = get_card_border_uv_portion
    hasCardBorder = has_card_border
    setCardColor = set_card_color
    getCardColor = get_card_color
    setCardTexture = set_card_texture
    clearCardTexture = clear_card_texture
    hasCardTexture = has_card_texture
    getCardTexture = get_card_texture
    setFrameAsMargin = set_frame_as_margin
    setFrameActual = set_frame_actual
    clearFrame = clear_frame
    hasFrame = has_frame
    isFrameAsMargin = is_frame_as_margin
    getFrameAsSet = get_frame_as_set
    getFrameActual = get_frame_actual
    setFrameLineWidth = set_frame_line_width
    getFrameLineWidth = get_frame_line_width
    setFrameCorners = set_frame_corners
    getFrameCorners = get_frame_corners
    setCardAsMargin = set_card_as_margin
    setCardActual = set_card_actual
    setCardDecal = set_card_decal
    clearCard = clear_card
    hasCard = has_card
    getCardDecal = get_card_decal
    isCardAsMargin = is_card_as_margin
    getCardAsSet = get_card_as_set
    getCardActual = get_card_actual
    getCardTransformed = get_card_transformed
    setTransform = set_transform  # type: ignore[assignment]
    getTransform = get_transform  # type: ignore[assignment]
    setCoordinateSystem = set_coordinate_system
    getCoordinateSystem = get_coordinate_system
    setUsageHint = set_usage_hint
    getUsageHint = get_usage_hint
    setFlattenFlags = set_flatten_flags
    getFlattenFlags = get_flatten_flags
    clearFont = clear_font
    clearWordwrap = clear_wordwrap
    setBin = set_bin
    setDrawOrder = set_draw_order
    setGlyphScale = set_glyph_scale
    getWordwrappedText = get_wordwrapped_text
    calcWidth = calc_width
    hasExactCharacter = has_exact_character
    hasCharacter = has_character
    isWhitespace = is_whitespace
    getWordwrappedWtext = get_wordwrapped_wtext
    getLeft = get_left
    getRight = get_right
    getBottom = get_bottom
    getTop = get_top
    getHeight = get_height
    getWidth = get_width
    getUpperLeft3d = get_upper_left_3d
    getLowerRight3d = get_lower_right_3d
    getNumRows = get_num_rows
    forceUpdate = force_update
    getInternalGeom = get_internal_geom
