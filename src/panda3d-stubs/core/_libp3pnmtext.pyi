from os import PathLike
from typing import Any, ClassVar, Literal, TypeAlias, overload
from panda3d.core import (
    ConfigVariableColor,
    ConfigVariableFilename,
    Filename,
    LMatrix4f,
    LVecBase4f,
    Namable,
    PNMImage,
    UnalignedLVecBase4f,
)

_FreetypeFont_WindingOrder: TypeAlias = Literal[0, 1, 2, 3]
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike
_PNMTextMaker_Alignment: TypeAlias = Literal[0, 1, 2]

class FreetypeFont(Namable):
    """This is a common base class for both DynamicTextFont and PNMTextMaker.
    Both of these are utility classes that use the FreeType library to generate
    glyphs from fonts; this class abstracts out that common wrapper around
    FreeType.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    winding_order: _FreetypeFont_WindingOrder
    WO_default: ClassVar[Literal[0]]
    WO_left: ClassVar[Literal[1]]
    WO_right: ClassVar[Literal[2]]
    WO_invalid: ClassVar[Literal[3]]
    def set_point_size(self, point_size: float) -> bool:
        """Sets the point size of the font.  This controls the apparent size of the
        font onscreen.  By convention, a 10 point font is about 1 screen unit high.
        
        This should only be called before any characters have been requested out of
        the font, or immediately after calling clear().
        """
        ...
    def get_point_size(self) -> float:
        """Returns the point size of the font."""
        ...
    def set_pixels_per_unit(self, pixels_per_unit: float) -> bool:
        """Set the resolution of the texture map, and hence the clarity of the
        resulting font.  This sets the number of pixels in the texture map that are
        used for each onscreen unit.
        
        Setting this number larger results in an easier to read font, but at the
        cost of more texture memory.
        
        This should only be called before any characters have been requested out of
        the font, or immediately after calling clear().
        """
        ...
    def get_pixels_per_unit(self) -> float:
        """Returns the resolution of the texture map.  See set_pixels_per_unit()."""
        ...
    def set_pixel_size(self, pixel_size: float) -> bool:
        """Computes the appropriate pixels_per_unit value to set the size of the font
        in the texture to the indicated number of pixels.  This is just another way
        to specify pixels_per_unit().
        """
        ...
    def get_pixel_size(self) -> float:
        """Returns the size of the font in pixels, as it appears in the texture."""
        ...
    def set_scale_factor(self, scale_factor: float) -> bool:
        """Sets the factor by which the font is rendered larger by the FreeType
        library before being filtered down to its actual size in the texture as
        specified by set_pixels_per_unit().  This may be set to a number larger
        than 1.0 to improve the font's antialiasing (since FreeType doesn't really
        do a swell job of antialiasing by itself).  There is some performance
        implication for setting this different than 1.0.
        
        This should only be called before any characters have been requested out of
        the font, or immediately after calling clear().
        """
        ...
    def get_scale_factor(self) -> float:
        """Returns the antialiasing scale factor.  See set_scale_factor()."""
        ...
    def set_native_antialias(self, native_antialias: bool) -> None:
        """Sets whether the Freetype library's built-in antialias mode is enabled.
        There are two unrelated ways to achieve antialiasing: with Freetype's
        native antialias mode, and with the use of a scale_factor greater than one.
        By default, both modes are enabled.
        
        At low resolutions, some fonts may do better with one mode or the other.
        In general, Freetype's native antialiasing will produce less blurry
        results, but may introduce more artifacts.
        """
        ...
    def get_native_antialias(self) -> bool:
        """Returns whether Freetype's built-in antialias mode is enabled.  See
        set_native_antialias().
        """
        ...
    def get_font_pixel_size(self) -> int:
        """This is used to report whether the requested pixel size is being only
        approximated by a fixed-pixel-size font.  This returns 0 in the normal
        case, in which a scalable font is used, or the fixed-pixel-size font has
        exactly the requested pixel size.
        
        If this returns non-zero, it is the pixel size of the font that we are
        using to approximate our desired size.
        """
        ...
    def get_line_height(self) -> float:
        """Returns the number of units high each line of text is."""
        ...
    def get_space_advance(self) -> float:
        """Returns the number of units wide a space is."""
        ...
    @staticmethod
    def get_points_per_unit() -> float:
        """Returns the point size of the font that is one Panda unit high.  This is an
        arbitrary Panda convention for text, and is set to 10.0.
        """
        ...
    @staticmethod
    def get_points_per_inch() -> float:
        """Returns the number of points in one inch.  This is a universal typographic
        convention.
        """
        ...
    def set_winding_order(self, winding_order: _FreetypeFont_WindingOrder) -> None:
        """Specifies an explicitly winding order on this particular font.  This is
        only necessary if the render_mode is RM_polygon or RM_solid, and only if
        FreeType appears to guess wrong on this font.  Normally, you should leave
        this at WO_default.
        """
        ...
    def get_winding_order(self) -> _FreetypeFont_WindingOrder:
        """Returns the winding order set via set_winding_order()."""
        ...
    setPointSize = set_point_size
    getPointSize = get_point_size
    setPixelsPerUnit = set_pixels_per_unit
    getPixelsPerUnit = get_pixels_per_unit
    setPixelSize = set_pixel_size
    getPixelSize = get_pixel_size
    setScaleFactor = set_scale_factor
    getScaleFactor = get_scale_factor
    setNativeAntialias = set_native_antialias
    getNativeAntialias = get_native_antialias
    getFontPixelSize = get_font_pixel_size
    getLineHeight = get_line_height
    getSpaceAdvance = get_space_advance
    getPointsPerUnit = get_points_per_unit
    getPointsPerInch = get_points_per_inch
    setWindingOrder = set_winding_order
    getWindingOrder = get_winding_order
    WODefault = WO_default
    WOLeft = WO_left
    WORight = WO_right
    WOInvalid = WO_invalid

class PNMTextGlyph:
    """A single glyph in a PNMTextMaker."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: PNMTextGlyph) -> None: ...
    @overload
    def __init__(self, advance: float) -> None: ...
    def get_advance(self) -> int:
        """Returns the number of pixels by which the pen should be advanced after
        rendering this glyph.
        """
        ...
    @overload
    def place(self, dest_image: PNMImage, xp: int, yp: int, fg: _Vec4f) -> None:
        """Copies the glyph to the indicated destination image at the indicated
        origin.  It colors the glyph pixels the indicated foreground color, blends
        antialiased pixels with the appropriate amount of the foreground color and
        the existing background color, and leaves other pixels alone.
        """
        ...
    @overload
    def place(self, dest_image: PNMImage, xp: int, yp: int, fg: _Vec4f, interior: _Vec4f) -> None:
        """This flavor of place() also fills in the interior color.  This requires
        that determine_interior was called earlier.
        """
        ...
    def get_left(self) -> int:
        """Returns the x coordinate of the leftmost pixel in the glyph."""
        ...
    def get_right(self) -> int:
        """Returns the x coordinate of the rightmost pixel in the glyph."""
        ...
    def get_bottom(self) -> int:
        """Returns the y coordinate of the bottommost pixel in the glyph."""
        ...
    def get_top(self) -> int:
        """Returns the y coordinate of the topmost pixel in the glyph."""
        ...
    def get_height(self) -> int:
        """Returns the height of the glyph in pixels."""
        ...
    def get_width(self) -> int:
        """Returns the width of the glyph in pixels."""
        ...
    def get_value(self, x: int, y: int) -> float:
        """Returns the value of the indicated pixel of the glyph.  The result is in
        the range [0, 1], where 0 indicates the pixel is not part of the glyph, and
        1 indicates it is.  Intermediate values are used to represent antialiasing.
        """
        ...
    def get_interior_flag(self, x: int, y: int) -> bool:
        """Returns true if the indicated pixel represents a pixel in the interior of a
        hollow font, false otherwise.
        """
        ...
    getAdvance = get_advance
    getLeft = get_left
    getRight = get_right
    getBottom = get_bottom
    getTop = get_top
    getHeight = get_height
    getWidth = get_width
    getValue = get_value
    getInteriorFlag = get_interior_flag

class PNMTextMaker(FreetypeFont):
    """This object uses the Freetype library to generate text directly into an
    image.  It is different from the TextNode/DynamicTextFont interface, which
    use the Freetype library to generate text in the scene graph, to be
    rendered onscreen via the Panda render traversal.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    A_left: ClassVar[Literal[0]]
    A_right: ClassVar[Literal[1]]
    A_center: ClassVar[Literal[2]]
    @overload
    def __init__(self, copy: FreetypeFont) -> None:
        """The constructor expects the name of some font file that FreeType can read,
        along with face_index, indicating which font within the file to load
        (usually 0).
        """
        ...
    @overload
    def __init__(self, font_filename: _Filename, face_index: int) -> None: ...
    @overload
    def __init__(self, font_data: str, data_length: int, face_index: int) -> None: ...
    def is_valid(self) -> bool:
        """Returns true if the PNMTextMaker is valid and ready to generate text, false
        otherwise.
        """
        ...
    def set_align(self, align_type: _PNMTextMaker_Alignment) -> None: ...
    def get_align(self) -> _PNMTextMaker_Alignment: ...
    def set_interior_flag(self, interior_flag: bool) -> None:
        """Sets the flag that indicates whether the interior of hollow fonts is
        identified as a preprocess as each glyph is loaded.  If this flag is true,
        you may specify an interior color along with a fg and bg color when you
        place text; if the flag is false, the interior color is ignored.
        
        It is generally best to set_native_antialias(0) when using this feature.
        Also, this works best when the pixel size is not very small.
        """
        ...
    def get_interior_flag(self) -> bool: ...
    def set_fg(self, fg: _Vec4f) -> None:
        """Sets the foreground color of text that will be generated by future calls to
        generate_into().  This is the color that all of the "on" pixels in the font
        will show as.
        """
        ...
    def get_fg(self) -> LVecBase4f:
        """Returns the foreground color of text that will be generated by future calls
        to generate_into().
        """
        ...
    def set_interior(self, interior: _Vec4f) -> None:
        """Sets the color that will be used to render the interior portions of hollow
        fonts in future calls to generate_into().  This is respected only if
        interior_flag is true.
        """
        ...
    def get_interior(self) -> LVecBase4f:
        """Returns the color that will be used to render the interior portions of
        hollow fonts.
        """
        ...
    def set_distance_field_radius(self, radius: int) -> None:
        """If this is set to something other than 0, Panda will generate a signed
        distance field with the given radius.
        """
        ...
    def get_distance_field_radius(self) -> int:
        """Returns the radius previously set with set_distance_field_radius, or 0
        otherwise.
        """
        ...
    def generate_into(self, text: str, dest_image: PNMImage, x: int, y: int) -> int:
        """Generates a single line of text into the indicated image at the indicated
        position; the return value is the total width in pixels.
        """
        ...
    def calc_width(self, text: str) -> int:
        """Returns the width in pixels of the indicated line of text."""
        ...
    def get_glyph(self, character: int) -> PNMTextGlyph:
        """Returns the glyph for the indicated index, or NULL if it is not defined in
        the font.
        """
        ...
    isValid = is_valid
    setAlign = set_align
    getAlign = get_align
    setInteriorFlag = set_interior_flag
    getInteriorFlag = get_interior_flag
    setFg = set_fg
    getFg = get_fg
    setInterior = set_interior
    getInterior = get_interior
    setDistanceFieldRadius = set_distance_field_radius
    getDistanceFieldRadius = get_distance_field_radius
    generateInto = generate_into
    calcWidth = calc_width
    getGlyph = get_glyph
    ALeft = A_left
    ARight = A_right
    ACenter = A_center
