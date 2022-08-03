from collections.abc import Sequence
from os import PathLike
from typing import Any, ClassVar, Literal, TypeAlias, overload

_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_GeomEnums_UsageHint: TypeAlias = Literal[0, 1, 2, 3, 4]
_SamplerState_FilterType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
_TextFont_RenderMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
_Texture_Format: TypeAlias = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike
_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_TextProperties_Alignment: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_TextProperties_Direction: TypeAlias = Literal[0, 1]
_Mat4f: TypeAlias = LMatrix4f | UnalignedLMatrix4f

class TextGlyph(TypedReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def character(self) -> int: ...
    @property
    def state(self) -> RenderState: ...
    @property
    def advance(self) -> float: ...
    def get_character(self) -> int: ...
    def has_quad(self) -> bool: ...
    def get_quad(self, dimensions: _Vec4f, texcoords: _Vec4f) -> bool: ...
    def get_state(self) -> RenderState: ...
    def get_advance(self) -> float: ...
    def is_whitespace(self) -> bool: ...
    def get_geom(self, usage_hint: _GeomEnums_UsageHint) -> Geom: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getCharacter = get_character
    hasQuad = has_quad
    getQuad = get_quad
    getState = get_state
    getAdvance = get_advance
    isWhitespace = is_whitespace
    getGeom = get_geom
    getClassType = get_class_type

class TextFont(TypedReferenceCount, Namable):
    DtoolClassDict: ClassVar[dict[str, Any]]
    line_height: float
    space_advance: float
    RM_texture: ClassVar[Literal[0]]
    RM_wireframe: ClassVar[Literal[1]]
    RM_polygon: ClassVar[Literal[2]]
    RM_extruded: ClassVar[Literal[3]]
    RM_solid: ClassVar[Literal[4]]
    RM_distance_field: ClassVar[Literal[5]]
    RM_invalid: ClassVar[Literal[6]]
    @property
    def valid(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def upcast_to_TypedReferenceCount(self) -> TypedReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def make_copy(self) -> TextFont: ...
    def is_valid(self) -> bool: ...
    def get_line_height(self) -> float: ...
    def set_line_height(self, line_height: float) -> None: ...
    def get_space_advance(self) -> float: ...
    def set_space_advance(self, space_advance: float) -> None: ...
    def get_glyph(self, character: int) -> TextGlyph: ...
    def get_kerning(self, first: int, second: int) -> float: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type
    RMTexture = RM_texture
    RMWireframe = RM_wireframe
    RMPolygon = RM_polygon
    RMExtruded = RM_extruded
    RMSolid = RM_solid
    RMDistanceField = RM_distance_field
    RMInvalid = RM_invalid

class DynamicTextGlyph(TextGlyph):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def page(self) -> DynamicTextPage: ...
    def get_page(self) -> DynamicTextPage: ...
    def intersects(self, x: int, y: int, x_size: int, y_size: int) -> bool: ...
    def get_left(self) -> float: ...
    def get_bottom(self) -> float: ...
    def get_right(self) -> float: ...
    def get_top(self) -> float: ...
    def get_uv_left(self) -> float: ...
    def get_uv_bottom(self) -> float: ...
    def get_uv_right(self) -> float: ...
    def get_uv_top(self) -> float: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getPage = get_page
    getLeft = get_left
    getBottom = get_bottom
    getRight = get_right
    getTop = get_top
    getUvLeft = get_uv_left
    getUvBottom = get_uv_bottom
    getUvRight = get_uv_right
    getUvTop = get_uv_top
    getClassType = get_class_type

class DynamicTextPage(Texture):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: DynamicTextPage) -> None: ...
    def get_size(self) -> LVecBase2i: ...
    def get_x_size(self) -> int: ...
    def get_y_size(self) -> int: ...
    def is_empty(self) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getSize = get_size
    getXSize = get_x_size
    getYSize = get_y_size
    isEmpty = is_empty
    getClassType = get_class_type

class DynamicTextFont(TextFont, FreetypeFont):
    DtoolClassDict: ClassVar[dict[str, Any]]
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
    fg: LVecBase4f
    bg: LVecBase4f
    @property
    def font_pixel_size(self) -> int: ...
    @property
    def tex_format(self) -> _Texture_Format: ...
    @property
    def pages(self) -> Sequence[DynamicTextPage]: ...
    @overload
    def __init__(self, copy: DynamicTextFont) -> None: ...
    @overload
    def __init__(self, font_filename: _Filename, face_index: int = ...) -> None: ...
    @overload
    def __init__(self, font_data: str, data_length: int, face_index: int) -> None: ...
    def upcast_to_TextFont(self) -> TextFont: ...
    def upcast_to_FreetypeFont(self) -> FreetypeFont: ...
    def make_copy(self) -> TextFont: ...
    def get_name(self) -> str: ...
    def set_point_size(self, point_size: float) -> bool: ...
    def get_point_size(self) -> float: ...
    def set_pixels_per_unit(self, pixels_per_unit: float) -> bool: ...
    def get_pixels_per_unit(self) -> float: ...
    def set_scale_factor(self, scale_factor: float) -> bool: ...
    def get_scale_factor(self) -> float: ...
    def set_native_antialias(self, native_antialias: bool) -> None: ...
    def get_native_antialias(self) -> bool: ...
    def get_font_pixel_size(self) -> int: ...
    def get_line_height(self) -> float: ...
    def get_space_advance(self) -> float: ...
    def set_texture_margin(self, texture_margin: int) -> None: ...
    def get_texture_margin(self) -> int: ...
    def set_poly_margin(self, poly_margin: float) -> None: ...
    def get_poly_margin(self) -> float: ...
    @overload
    def set_page_size(self, page_size: LVecBase2i) -> None: ...
    @overload
    def set_page_size(self, x_size: int, y_size: int) -> None: ...
    def get_page_size(self) -> LVecBase2i: ...
    def get_page_x_size(self) -> int: ...
    def get_page_y_size(self) -> int: ...
    def set_minfilter(self, filter: _SamplerState_FilterType) -> None: ...
    def get_minfilter(self) -> _SamplerState_FilterType: ...
    def set_magfilter(self, filter: _SamplerState_FilterType) -> None: ...
    def get_magfilter(self) -> _SamplerState_FilterType: ...
    def set_anisotropic_degree(self, anisotropic_degree: int) -> None: ...
    def get_anisotropic_degree(self) -> int: ...
    def set_render_mode(self, render_mode: _TextFont_RenderMode) -> None: ...
    def get_render_mode(self) -> _TextFont_RenderMode: ...
    def set_fg(self, fg: _Vec4f) -> None: ...
    def get_fg(self) -> LVecBase4f: ...
    def set_bg(self, bg: _Vec4f) -> None: ...
    def get_bg(self) -> LVecBase4f: ...
    def set_outline(self, outline_color: _Vec4f, outline_width: float, outline_feather: float) -> None: ...
    def get_outline_color(self) -> LVecBase4f: ...
    def get_outline_width(self) -> float: ...
    def get_outline_feather(self) -> float: ...
    def get_tex_format(self) -> _Texture_Format: ...
    def get_num_pages(self) -> int: ...
    def get_page(self, n: int) -> DynamicTextPage: ...
    def garbage_collect(self) -> int: ...
    def clear(self) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_pages(self) -> tuple[DynamicTextPage, ...]: ...
    upcastToTextFont = upcast_to_TextFont
    upcastToFreetypeFont = upcast_to_FreetypeFont
    makeCopy = make_copy
    getName = get_name
    setPointSize = set_point_size
    getPointSize = get_point_size
    setPixelsPerUnit = set_pixels_per_unit
    getPixelsPerUnit = get_pixels_per_unit
    setScaleFactor = set_scale_factor
    getScaleFactor = get_scale_factor
    setNativeAntialias = set_native_antialias
    getNativeAntialias = get_native_antialias
    getFontPixelSize = get_font_pixel_size
    getLineHeight = get_line_height
    getSpaceAdvance = get_space_advance
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
    getClassType = get_class_type
    getPages = get_pages

class FontPool:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def has_font(filename: str) -> bool: ...
    @staticmethod
    def verify_font(filename: str) -> bool: ...
    @staticmethod
    def load_font(filename: str) -> TextFont: ...
    @staticmethod
    def add_font(filename: str, font: TextFont) -> None: ...
    @staticmethod
    def release_font(filename: str) -> None: ...
    @staticmethod
    def release_all_fonts() -> None: ...
    @staticmethod
    def garbage_collect() -> int: ...
    @staticmethod
    def list_contents(out: ostream) -> None: ...
    @staticmethod
    def write(out: ostream) -> None: ...
    hasFont = has_font
    verifyFont = verify_font
    loadFont = load_font
    addFont = add_font
    releaseFont = release_font
    releaseAllFonts = release_all_fonts
    garbageCollect = garbage_collect
    listContents = list_contents

class GeomTextGlyph(Geom):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class StaticTextFont(TextFont):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, font_def: PandaNode, cs: _CoordinateSystem = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class TextProperties:
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
    text_color: LVecBase4f
    shadow_color: LVecBase4f
    shadow: LVector2f
    bin: str
    draw_order: int
    tab_width: float
    glyph_scale: float
    glyph_shift: float
    text_scale: float
    direction: _TextProperties_Direction
    A_left: ClassVar[Literal[0]]
    A_right: ClassVar[Literal[1]]
    A_center: ClassVar[Literal[2]]
    A_boxed_left: ClassVar[Literal[3]]
    A_boxed_right: ClassVar[Literal[4]]
    A_boxed_center: ClassVar[Literal[5]]
    D_ltr: ClassVar[Literal[0]]
    D_rtl: ClassVar[Literal[1]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: TextProperties) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def assign(self, copy: TextProperties) -> TextProperties: ...
    def clear(self) -> None: ...
    def is_any_specified(self) -> bool: ...
    @staticmethod
    def set_default_font(__param0: TextFont) -> None: ...
    @staticmethod
    def get_default_font() -> TextFont: ...
    def set_font(self, font: TextFont) -> None: ...
    def clear_font(self) -> None: ...
    def has_font(self) -> bool: ...
    def get_font(self) -> TextFont: ...
    def set_small_caps(self, small_caps: bool) -> None: ...
    def clear_small_caps(self) -> None: ...
    def has_small_caps(self) -> bool: ...
    def get_small_caps(self) -> bool: ...
    def set_small_caps_scale(self, small_caps_scale: float) -> None: ...
    def clear_small_caps_scale(self) -> None: ...
    def has_small_caps_scale(self) -> bool: ...
    def get_small_caps_scale(self) -> float: ...
    def set_slant(self, slant: float) -> None: ...
    def clear_slant(self) -> None: ...
    def has_slant(self) -> bool: ...
    def get_slant(self) -> float: ...
    def set_underscore(self, underscore: bool) -> None: ...
    def clear_underscore(self) -> None: ...
    def has_underscore(self) -> bool: ...
    def get_underscore(self) -> bool: ...
    def set_underscore_height(self, underscore_height: float) -> None: ...
    def clear_underscore_height(self) -> None: ...
    def has_underscore_height(self) -> bool: ...
    def get_underscore_height(self) -> float: ...
    def set_align(self, align_type: _TextProperties_Alignment) -> None: ...
    def clear_align(self) -> None: ...
    def has_align(self) -> bool: ...
    def get_align(self) -> _TextProperties_Alignment: ...
    def set_indent(self, indent: float) -> None: ...
    def clear_indent(self) -> None: ...
    def has_indent(self) -> bool: ...
    def get_indent(self) -> float: ...
    def set_wordwrap(self, wordwrap: float) -> None: ...
    def clear_wordwrap(self) -> None: ...
    def has_wordwrap(self) -> bool: ...
    def get_wordwrap(self) -> float: ...
    def set_preserve_trailing_whitespace(self, preserve_trailing_whitespace: bool) -> None: ...
    def clear_preserve_trailing_whitespace(self) -> None: ...
    def has_preserve_trailing_whitespace(self) -> bool: ...
    def get_preserve_trailing_whitespace(self) -> bool: ...
    @overload
    def set_text_color(self, text_color: _Vec4f) -> None: ...
    @overload
    def set_text_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def clear_text_color(self) -> None: ...
    def has_text_color(self) -> bool: ...
    def get_text_color(self) -> LVecBase4f: ...
    @overload
    def set_shadow_color(self, shadow_color: _Vec4f) -> None: ...
    @overload
    def set_shadow_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def clear_shadow_color(self) -> None: ...
    def has_shadow_color(self) -> bool: ...
    def get_shadow_color(self) -> LVecBase4f: ...
    @overload
    def set_shadow(self, shadow_offset: LVecBase2f) -> None: ...
    @overload
    def set_shadow(self, xoffset: float, yoffset: float) -> None: ...
    def clear_shadow(self) -> None: ...
    def has_shadow(self) -> bool: ...
    def get_shadow(self) -> LVector2f: ...
    def set_bin(self, bin: str) -> None: ...
    def clear_bin(self) -> None: ...
    def has_bin(self) -> bool: ...
    def get_bin(self) -> str: ...
    def set_draw_order(self, draw_order: int) -> int: ...
    def clear_draw_order(self) -> None: ...
    def has_draw_order(self) -> bool: ...
    def get_draw_order(self) -> int: ...
    def set_tab_width(self, tab_width: float) -> None: ...
    def clear_tab_width(self) -> None: ...
    def has_tab_width(self) -> bool: ...
    def get_tab_width(self) -> float: ...
    def set_glyph_scale(self, glyph_scale: float) -> None: ...
    def clear_glyph_scale(self) -> None: ...
    def has_glyph_scale(self) -> bool: ...
    def get_glyph_scale(self) -> float: ...
    def set_glyph_shift(self, glyph_shift: float) -> None: ...
    def clear_glyph_shift(self) -> None: ...
    def has_glyph_shift(self) -> bool: ...
    def get_glyph_shift(self) -> float: ...
    def set_text_scale(self, text_scale: float) -> None: ...
    def clear_text_scale(self) -> None: ...
    def has_text_scale(self) -> bool: ...
    def get_text_scale(self) -> float: ...
    def set_direction(self, direction: _TextProperties_Direction) -> None: ...
    def clear_direction(self) -> None: ...
    def has_direction(self) -> bool: ...
    def get_direction(self) -> _TextProperties_Direction: ...
    def add_properties(self, other: TextProperties) -> None: ...
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
    ALeft = A_left
    ARight = A_right
    ACenter = A_center
    ABoxedLeft = A_boxed_left
    ABoxedRight = A_boxed_right
    ABoxedCenter = A_boxed_center
    DLtr = D_ltr
    DRtl = D_rtl

class TextGraphic:
    DtoolClassDict: ClassVar[dict[str, Any]]
    model: NodePath
    frame: LVecBase4f
    instance_flag: bool
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: TextGraphic) -> None: ...
    @overload
    def __init__(self, model: NodePath, frame: _Vec4f) -> None: ...
    @overload
    def __init__(self, model: NodePath, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_model(self) -> NodePath: ...
    def set_model(self, model: NodePath) -> None: ...
    def get_frame(self) -> LVecBase4f: ...
    @overload
    def set_frame(self, frame: _Vec4f) -> None: ...
    @overload
    def set_frame(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def get_instance_flag(self) -> bool: ...
    def set_instance_flag(self, instance_flag: bool) -> None: ...
    getModel = get_model
    setModel = set_model
    getFrame = get_frame
    setFrame = set_frame
    getInstanceFlag = get_instance_flag
    setInstanceFlag = set_instance_flag

class TextPropertiesManager:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def set_properties(self, name: str, properties: TextProperties) -> None: ...
    def get_properties(self, name: str) -> TextProperties: ...
    def has_properties(self, name: str) -> bool: ...
    def clear_properties(self, name: str) -> None: ...
    @overload
    def set_graphic(self, name: str, model: NodePath) -> None: ...
    @overload
    def set_graphic(self, name: str, graphic: TextGraphic) -> None: ...
    def get_graphic(self, name: str) -> TextGraphic: ...
    def has_graphic(self, name: str) -> bool: ...
    def clear_graphic(self, name: str) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    @staticmethod
    def get_global_ptr() -> TextPropertiesManager: ...
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
    def assign(self, copy: TextAssembler) -> TextAssembler: ...
    def clear(self) -> None: ...
    def set_usage_hint(self, usage_hint: _GeomEnums_UsageHint) -> None: ...
    def get_usage_hint(self) -> _GeomEnums_UsageHint: ...
    def set_max_rows(self, max_rows: int) -> None: ...
    def get_max_rows(self) -> int: ...
    def set_dynamic_merge(self, dynamic_merge: bool) -> None: ...
    def get_dynamic_merge(self) -> bool: ...
    def set_multiline_mode(self, flag: bool) -> None: ...
    def get_multiline_mode(self) -> bool: ...
    def set_properties(self, properties: TextProperties) -> None: ...
    @overload
    def get_properties(self) -> TextProperties: ...
    @overload
    def get_properties(self, n: int) -> TextProperties: ...
    @overload
    def get_properties(self, r: int, c: int) -> TextProperties: ...
    def set_wtext(self, wtext: str) -> bool: ...
    def set_wsubstr(self, wtext: str, start: int, count: int) -> bool: ...
    def get_plain_wtext(self) -> str: ...
    def get_wordwrapped_plain_wtext(self) -> str: ...
    def get_wtext(self) -> str: ...
    def get_wordwrapped_wtext(self) -> str: ...
    def calc_r(self, n: int) -> int: ...
    def calc_c(self, n: int) -> int: ...
    def calc_index(self, r: int, c: int) -> int: ...
    def get_num_characters(self) -> int: ...
    @overload
    def get_character(self, n: int) -> int: ...
    @overload
    def get_character(self, r: int, c: int) -> int: ...
    @overload
    def get_graphic(self, n: int) -> TextGraphic: ...
    @overload
    def get_graphic(self, r: int, c: int) -> TextGraphic: ...
    @overload
    def get_width(self, n: int) -> float: ...
    @overload
    def get_width(self, r: int, c: int) -> float: ...
    def get_num_rows(self) -> int: ...
    def get_num_cols(self, r: int) -> int: ...
    def get_xpos(self, r: int, c: int) -> float: ...
    def get_ypos(self, r: int, c: int) -> float: ...
    def assemble_text(self) -> PandaNode: ...
    def get_ul(self) -> LVector2f: ...
    def get_lr(self) -> LVector2f: ...
    @overload
    @staticmethod
    def calc_width(graphic: TextGraphic, properties: TextProperties) -> float: ...
    @overload
    @staticmethod
    def calc_width(character: int, properties: TextProperties) -> float: ...
    @staticmethod
    def has_exact_character(character: int, properties: TextProperties) -> bool: ...
    @staticmethod
    def has_character(character: int, properties: TextProperties) -> bool: ...
    @staticmethod
    def is_whitespace(character: int, properties: TextProperties) -> bool: ...
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

class TextNode(PandaNode, TextEncoder, TextProperties):
    DtoolClassDict: ClassVar[dict[str, Any]]
    max_rows: int
    frame_color: LVecBase4f
    card_color: LVecBase4f
    card_texture: Texture
    frame_line_width: float
    frame_corners: bool
    transform: LMatrix4f
    coordinate_system: _CoordinateSystem
    usage_hint: _GeomEnums_UsageHint
    flatten_flags: int
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
    text_color: LVecBase4f
    shadow_color: LVecBase4f
    shadow: LVector2f
    bin: str
    draw_order: int
    tab_width: float
    glyph_scale: float
    glyph_shift: float
    text_scale: float
    FF_none: ClassVar[Literal[0]]
    FF_light: ClassVar[Literal[1]]
    FF_medium: ClassVar[Literal[2]]
    FF_strong: ClassVar[Literal[4]]
    FF_dynamic_merge: ClassVar[Literal[8]]
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, name: str, copy: TextProperties) -> None: ...
    def upcast_to_PandaNode(self) -> PandaNode: ...
    def upcast_to_TextEncoder(self) -> TextEncoder: ...
    def upcast_to_TextProperties(self) -> TextProperties: ...
    def get_line_height(self) -> float: ...
    def set_max_rows(self, max_rows: int) -> None: ...
    def clear_max_rows(self) -> None: ...
    def has_max_rows(self) -> bool: ...
    def get_max_rows(self) -> int: ...
    def has_overflow(self) -> bool: ...
    @overload
    def set_frame_color(self, frame_color: _Vec4f) -> None: ...
    @overload
    def set_frame_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def get_frame_color(self) -> LVecBase4f: ...
    def set_card_border(self, size: float, uv_portion: float) -> None: ...
    def clear_card_border(self) -> None: ...
    def get_card_border_size(self) -> float: ...
    def get_card_border_uv_portion(self) -> float: ...
    def has_card_border(self) -> bool: ...
    @overload
    def set_card_color(self, card_color: _Vec4f) -> None: ...
    @overload
    def set_card_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def get_card_color(self) -> LVecBase4f: ...
    def set_card_texture(self, card_texture: Texture) -> None: ...
    def clear_card_texture(self) -> None: ...
    def has_card_texture(self) -> bool: ...
    def get_card_texture(self) -> Texture: ...
    def set_frame_as_margin(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def set_frame_actual(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def clear_frame(self) -> None: ...
    def has_frame(self) -> bool: ...
    def is_frame_as_margin(self) -> bool: ...
    def get_frame_as_set(self) -> LVecBase4f: ...
    def get_frame_actual(self) -> LVecBase4f: ...
    def set_frame_line_width(self, line_width: float) -> None: ...
    def get_frame_line_width(self) -> float: ...
    def set_frame_corners(self, corners: bool) -> None: ...
    def get_frame_corners(self) -> bool: ...
    def set_card_as_margin(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def set_card_actual(self, left: float, right: float, bottom: float, top: float) -> None: ...
    def set_card_decal(self, card_decal: bool) -> None: ...
    def clear_card(self) -> None: ...
    def has_card(self) -> bool: ...
    def get_card_decal(self) -> bool: ...
    def is_card_as_margin(self) -> bool: ...
    def get_card_as_set(self) -> LVecBase4f: ...
    def get_card_actual(self) -> LVecBase4f: ...
    def get_card_transformed(self) -> LVecBase4f: ...
    def set_transform(self, transform: _Mat4f) -> None: ...
    def get_transform(self) -> LMatrix4f: ...
    def set_coordinate_system(self, cs: _CoordinateSystem) -> None: ...
    def get_coordinate_system(self) -> _CoordinateSystem: ...
    def set_usage_hint(self, usage_hint: _GeomEnums_UsageHint) -> None: ...
    def get_usage_hint(self) -> _GeomEnums_UsageHint: ...
    def set_flatten_flags(self, flatten_flags: int) -> None: ...
    def get_flatten_flags(self) -> int: ...
    def set_font(self, font: TextFont) -> None: ...
    def clear_font(self) -> None: ...
    def set_small_caps(self, small_caps: bool) -> None: ...
    def clear_small_caps(self) -> None: ...
    def set_small_caps_scale(self, small_caps_scale: float) -> None: ...
    def clear_small_caps_scale(self) -> None: ...
    def set_slant(self, slant: float) -> None: ...
    def clear_slant(self) -> None: ...
    def set_align(self, align_type: _TextProperties_Alignment) -> None: ...
    def clear_align(self) -> None: ...
    def set_indent(self, indent: float) -> None: ...
    def clear_indent(self) -> None: ...
    def set_wordwrap(self, wordwrap: float) -> None: ...
    def clear_wordwrap(self) -> None: ...
    @overload
    def set_text_color(self, text_color: _Vec4f) -> None: ...
    @overload
    def set_text_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def clear_text_color(self) -> None: ...
    @overload
    def set_shadow_color(self, shadow_color: _Vec4f) -> None: ...
    @overload
    def set_shadow_color(self, r: float, g: float, b: float, a: float) -> None: ...
    def clear_shadow_color(self) -> None: ...
    @overload
    def set_shadow(self, shadow_offset: LVecBase2f) -> None: ...
    @overload
    def set_shadow(self, xoffset: float, yoffset: float) -> None: ...
    def clear_shadow(self) -> None: ...
    def set_bin(self, bin: str) -> None: ...
    def clear_bin(self) -> None: ...
    def set_draw_order(self, draw_order: int) -> int: ...
    def clear_draw_order(self) -> None: ...
    def set_tab_width(self, tab_width: float) -> None: ...
    def clear_tab_width(self) -> None: ...
    def set_glyph_scale(self, glyph_scale: float) -> None: ...
    def clear_glyph_scale(self) -> None: ...
    def set_glyph_shift(self, glyph_shift: float) -> None: ...
    def clear_glyph_shift(self) -> None: ...
    def get_wordwrapped_text(self) -> str: ...
    @overload
    def calc_width(self, line: str) -> float: ...
    @overload
    def calc_width(self, character: int) -> float: ...
    def has_exact_character(self, character: int) -> bool: ...
    def has_character(self, character: int) -> bool: ...
    def is_whitespace(self, character: int) -> bool: ...
    def get_wordwrapped_wtext(self) -> str: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def get_left(self) -> float: ...
    def get_right(self) -> float: ...
    def get_bottom(self) -> float: ...
    def get_top(self) -> float: ...
    def get_height(self) -> float: ...
    def get_width(self) -> float: ...
    def get_upper_left_3d(self) -> LPoint3f: ...
    def get_lower_right_3d(self) -> LPoint3f: ...
    def get_num_rows(self) -> int: ...
    def generate(self) -> PandaNode: ...
    def update(self) -> None: ...
    def force_update(self) -> None: ...
    def get_internal_geom(self) -> PandaNode: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    setTransform = set_transform
    getTransform = get_transform
    setCoordinateSystem = set_coordinate_system
    getCoordinateSystem = get_coordinate_system
    setUsageHint = set_usage_hint
    getUsageHint = get_usage_hint
    setFlattenFlags = set_flatten_flags
    getFlattenFlags = get_flatten_flags
    setFont = set_font
    clearFont = clear_font
    setSmallCaps = set_small_caps
    clearSmallCaps = clear_small_caps
    setSmallCapsScale = set_small_caps_scale
    clearSmallCapsScale = clear_small_caps_scale
    setSlant = set_slant
    clearSlant = clear_slant
    setAlign = set_align
    clearAlign = clear_align
    setIndent = set_indent
    clearIndent = clear_indent
    setWordwrap = set_wordwrap
    clearWordwrap = clear_wordwrap
    setTextColor = set_text_color
    clearTextColor = clear_text_color
    setShadowColor = set_shadow_color
    clearShadowColor = clear_shadow_color
    setShadow = set_shadow
    clearShadow = clear_shadow
    setBin = set_bin
    clearBin = clear_bin
    setDrawOrder = set_draw_order
    clearDrawOrder = clear_draw_order
    setTabWidth = set_tab_width
    clearTabWidth = clear_tab_width
    setGlyphScale = set_glyph_scale
    clearGlyphScale = clear_glyph_scale
    setGlyphShift = set_glyph_shift
    clearGlyphShift = clear_glyph_shift
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
    getClassType = get_class_type
    FFNone = FF_none
    FFLight = FF_light
    FFMedium = FF_medium
    FFStrong = FF_strong
    FFDynamicMerge = FF_dynamic_merge