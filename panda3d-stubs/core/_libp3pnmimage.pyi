from collections.abc import Sequence
from os import PathLike
from typing import Any, ClassVar, Literal, TypeAlias, overload

_ColorSpace: TypeAlias = Literal[0, 1, 2, 3]
_PNMImageHeader_ColorType: TypeAlias = Literal[0, 1, 2, 3, 4]
_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_Vec3d: TypeAlias = LVecBase3d | LMatrix3d.Row | LMatrix3d.CRow
_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_Vec4d: TypeAlias = LVecBase4d | UnalignedLVecBase4d | LMatrix4d.Row | LMatrix4d.CRow
_Mat4d: TypeAlias = LMatrix4d | UnalignedLMatrix4d
_Mat4f: TypeAlias = LMatrix4f | UnalignedLMatrix4f
_PNMBrush_BrushEffect: TypeAlias = Literal[0, 1, 2, 3]

class pixel:
    DtoolClassDict: ClassVar[dict[str, Any]]
    b: int
    g: int
    r: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, fill: int) -> None: ...
    @overload
    def __init__(self, __param0: pixel) -> None: ...
    @overload
    def __init__(self, r: int, g: int, b: int) -> None: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, i: int, assign_val: int) -> None: ...
    def __add__(self, other: pixel) -> pixel: ...
    def __sub__(self, other: pixel) -> pixel: ...
    def __mul__(self, mult: float) -> pixel: ...
    def __iadd__(self, other: pixel) -> pixel: ...
    def __isub__(self, other: pixel) -> pixel: ...
    def __imul__(self, mult: float) -> pixel: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: pixel) -> bool: ...
    @staticmethod
    def __len__() -> int: ...
    def __le__(self, other: pixel) -> bool: ...
    def output(self, out: ostream) -> None: ...

class PNMFileType(TypedWritable):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def name(self) -> str: ...
    @property
    def extensions(self) -> Sequence[str]: ...
    @property
    def suggested_extension(self) -> str: ...
    def get_name(self) -> str: ...
    def get_num_extensions(self) -> int: ...
    def get_extension(self, n: int) -> str: ...
    def get_suggested_extension(self) -> str: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_extensions(self) -> tuple[str, ...]: ...
    getName = get_name
    getNumExtensions = get_num_extensions
    getExtension = get_extension
    getSuggestedExtension = get_suggested_extension
    getClassType = get_class_type
    getExtensions = get_extensions

class PNMFileTypeRegistry:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def types(self) -> Sequence[PNMFileType]: ...
    def __init__(self, __param0: PNMFileTypeRegistry) -> None: ...
    def get_num_types(self) -> int: ...
    def get_type(self, n: int) -> PNMFileType: ...
    def get_type_from_extension(self, filename: str) -> PNMFileType: ...
    def get_type_from_magic_number(self, magic_number: str) -> PNMFileType: ...
    def get_type_by_handle(self, handle: TypeHandle) -> PNMFileType: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    @staticmethod
    def get_global_ptr() -> PNMFileTypeRegistry: ...
    def get_types(self) -> tuple[PNMFileType, ...]: ...
    getNumTypes = get_num_types
    getType = get_type
    getTypeFromExtension = get_type_from_extension
    getTypeFromMagicNumber = get_type_from_magic_number
    getTypeByHandle = get_type_by_handle
    getGlobalPtr = get_global_ptr
    getTypes = get_types

class PNMImageHeader:
    class PixelSpec:
        DtoolClassDict: ClassVar[dict[str, Any]]
        @overload
        def __init__(self, __param0: PNMImageHeader.PixelSpec) -> None: ...
        @overload
        def __init__(self, rgb: pixel) -> None: ...
        @overload
        def __init__(self, gray_value: int) -> None: ...
        @overload
        def __init__(self, rgb: pixel, alpha: int) -> None: ...
        @overload
        def __init__(self, gray_value: int, alpha: int) -> None: ...
        @overload
        def __init__(self, red: int, green: int, blue: int) -> None: ...
        @overload
        def __init__(self, red: int, green: int, blue: int, alpha: int) -> None: ...
        def __lt__(self, other: PNMImageHeader.PixelSpec) -> bool: ...
        def __eq__(self, __other: object) -> bool: ...
        def __ne__(self, __other: object) -> bool: ...
        def __getitem__(self, n: int) -> int: ...
        @staticmethod
        def __len__() -> int: ...
        def __le__(self, other: PNMImageHeader.PixelSpec) -> bool: ...
        def compare_to(self, other: PNMImageHeader.PixelSpec) -> int: ...
        def get_red(self) -> int: ...
        def get_green(self) -> int: ...
        def get_blue(self) -> int: ...
        def get_alpha(self) -> int: ...
        def set_red(self, red: int) -> None: ...
        def set_green(self, green: int) -> None: ...
        def set_blue(self, blue: int) -> None: ...
        def set_alpha(self, alpha: int) -> None: ...
        def output(self, out: ostream) -> None: ...
        compareTo = compare_to
        getRed = get_red
        getGreen = get_green
        getBlue = get_blue
        getAlpha = get_alpha
        setRed = set_red
        setGreen = set_green
        setBlue = set_blue
        setAlpha = set_alpha
    class PixelSpecCount:
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: PNMImageHeader.PixelSpecCount) -> None: ...
    class Histogram:
        DtoolClassDict: ClassVar[dict[str, Any]]
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, __param0: PNMImageHeader.Histogram) -> None: ...
        def get_num_pixels(self) -> int: ...
        def get_pixel(self, n: int) -> PNMImageHeader.PixelSpec: ...
        @overload
        def get_count(self, pixel: PNMImageHeader.PixelSpec) -> int: ...
        @overload
        def get_count(self, n: int) -> int: ...
        def write(self, out: ostream) -> None: ...
        def get_pixels(self) -> tuple[PNMImageHeader.PixelSpec, ...]: ...
        getNumPixels = get_num_pixels
        getPixel = get_pixel
        getCount = get_count
        getPixels = get_pixels
    DtoolClassDict: ClassVar[dict[str, Any]]
    comment: str
    CT_invalid: ClassVar[Literal[0]]
    CT_grayscale: ClassVar[Literal[1]]
    CT_two_channel: ClassVar[Literal[2]]
    CT_color: ClassVar[Literal[3]]
    CT_four_channel: ClassVar[Literal[4]]
    @property
    def num_channels(self) -> int: ...
    @property
    def maxval(self) -> int: ...
    @property
    def color_space(self) -> _ColorSpace: ...
    @property
    def size(self) -> LVecBase2i: ...
    @property
    def type(self) -> PNMFileType: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: PNMImageHeader) -> None: ...
    def assign(self, copy: PNMImageHeader) -> PNMImageHeader: ...
    def get_color_type(self) -> _PNMImageHeader_ColorType: ...
    def get_num_channels(self) -> int: ...
    @overload
    def is_grayscale(self) -> bool: ...
    @overload
    def is_grayscale(self, color_type: _PNMImageHeader_ColorType) -> bool: ...
    @overload
    def has_alpha(self) -> bool: ...
    @overload
    def has_alpha(self, color_type: _PNMImageHeader_ColorType) -> bool: ...
    def get_maxval(self) -> int: ...
    def get_color_space(self) -> _ColorSpace: ...
    def get_x_size(self) -> int: ...
    def get_y_size(self) -> int: ...
    def get_size(self) -> LVecBase2i: ...
    def get_comment(self) -> str: ...
    def set_comment(self, comment: str) -> None: ...
    def has_type(self) -> bool: ...
    def get_type(self) -> PNMFileType: ...
    def set_type(self, type: PNMFileType) -> None: ...
    @overload
    def read_header(self, filename: _Filename, type: PNMFileType = ..., report_unknown_type: bool = ...) -> bool: ...
    @overload
    def read_header(self, data: istream, filename: str = ..., type: PNMFileType = ..., report_unknown_type: bool = ...) -> bool: ...
    def output(self, out: ostream) -> None: ...
    getColorType = get_color_type
    getNumChannels = get_num_channels
    isGrayscale = is_grayscale
    hasAlpha = has_alpha
    getMaxval = get_maxval
    getColorSpace = get_color_space
    getXSize = get_x_size
    getYSize = get_y_size
    getSize = get_size
    getComment = get_comment
    setComment = set_comment
    hasType = has_type
    getType = get_type
    setType = set_type
    readHeader = read_header
    CTInvalid = CT_invalid
    CTGrayscale = CT_grayscale
    CTTwoChannel = CT_two_channel
    CTColor = CT_color
    CTFourChannel = CT_four_channel

class PfmFile(PNMImageHeader):
    DtoolClassDict: ClassVar[dict[str, Any]]
    scale: float
    @property
    def valid(self) -> bool: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: PfmFile) -> None: ...
    def __imul__(self, multiplier: float) -> PfmFile: ...
    def assign(self, copy: PfmFile) -> PfmFile: ...
    @overload
    def clear(self) -> None: ...
    @overload
    def clear(self, x_size: int, y_size: int, num_channels: int) -> None: ...
    @overload
    def read(self, fullpath: _Filename) -> bool: ...
    @overload
    def read(self, _in: istream, fullpath: _Filename = ...) -> bool: ...
    @overload
    def write(self, fullpath: _Filename) -> bool: ...
    @overload
    def write(self, out: ostream, fullpath: _Filename = ...) -> bool: ...
    def load(self, pnmimage: PNMImage) -> bool: ...
    def store(self, pnmimage: PNMImage) -> bool: ...
    @overload
    def store_mask(self, pnmimage: PNMImage) -> bool: ...
    @overload
    def store_mask(self, pnmimage: PNMImage, min_point: _Vec4f, max_point: _Vec4f) -> bool: ...
    def is_valid(self) -> bool: ...
    def get_scale(self) -> float: ...
    def set_scale(self, scale: float) -> None: ...
    def has_point(self, x: int, y: int) -> bool: ...
    def get_channel(self, x: int, y: int, c: int) -> float: ...
    def set_channel(self, x: int, y: int, c: int, value: float) -> None: ...
    def get_point1(self, x: int, y: int) -> float: ...
    def set_point1(self, x: int, y: int, point: float) -> None: ...
    def get_point2(self, x: int, y: int) -> LPoint2f: ...
    def set_point2(self, x: int, y: int, point: LVecBase2d | LVecBase2f) -> None: ...
    def modify_point2(self, x: int, y: int) -> LPoint2f: ...
    def get_point(self, x: int, y: int) -> LPoint3f: ...
    def set_point(self, x: int, y: int, point: _Vec3d | _Vec3f) -> None: ...
    def modify_point(self, x: int, y: int) -> LPoint3f: ...
    def get_point3(self, x: int, y: int) -> LPoint3f: ...
    def set_point3(self, x: int, y: int, point: _Vec3d | _Vec3f) -> None: ...
    def modify_point3(self, x: int, y: int) -> LPoint3f: ...
    def get_point4(self, x: int, y: int) -> LPoint4f: ...
    def set_point4(self, x: int, y: int, point: _Vec4d | _Vec4f) -> None: ...
    def modify_point4(self, x: int, y: int) -> LPoint4f: ...
    def fill(self, value: LVecBase2f | _Vec3f | _Vec4f | float) -> None: ...
    def fill_nan(self) -> None: ...
    def fill_no_data_value(self) -> None: ...
    def fill_channel(self, channel: int, value: float) -> None: ...
    def fill_channel_nan(self, channel: int) -> None: ...
    def fill_channel_masked(self, channel: int, value: float) -> None: ...
    def fill_channel_masked_nan(self, channel: int) -> None: ...
    def calc_average_point(self, result: _Vec3f, x: float, y: float, radius: float) -> bool: ...
    def calc_bilinear_point(self, result: _Vec3f, x: float, y: float) -> bool: ...
    def calc_min_max(self, min_points: _Vec3f, max_points: _Vec3f) -> bool: ...
    def calc_autocrop(self, range: _Vec4d | _Vec4f) -> bool: ...
    def is_row_empty(self, y: int, x_begin: int, x_end: int) -> bool: ...
    def is_column_empty(self, x: int, y_begin: int, y_end: int) -> bool: ...
    def set_zero_special(self, zero_special: bool) -> None: ...
    def set_no_data_chan4(self, chan4: bool) -> None: ...
    def set_no_data_nan(self, num_channels: int) -> None: ...
    def set_no_data_value(self, no_data_value: _Vec4d | _Vec4f) -> None: ...
    def set_no_data_threshold(self, no_data_value: _Vec4d | _Vec4f) -> None: ...
    def clear_no_data_value(self) -> None: ...
    def has_no_data_value(self) -> bool: ...
    def has_no_data_threshold(self) -> bool: ...
    def get_no_data_value(self) -> LPoint4f: ...
    def resize(self, new_x_size: int, new_y_size: int) -> None: ...
    def box_filter_from(self, radius: float, copy: PfmFile) -> None: ...
    def gaussian_filter_from(self, radius: float, copy: PfmFile) -> None: ...
    def quick_filter_from(self, copy: PfmFile) -> None: ...
    def reverse_rows(self) -> None: ...
    def flip(self, flip_x: bool, flip_y: bool, transpose: bool) -> None: ...
    def xform(self, transform: _Mat4d | _Mat4f) -> None: ...
    def forward_distort(self, dist: PfmFile, scale_factor: float = ...) -> None: ...
    def reverse_distort(self, dist: PfmFile, scale_factor: float = ...) -> None: ...
    def apply_1d_lut(self, channel: int, lut: PfmFile, x_scale: float = ...) -> None: ...
    def merge(self, other: PfmFile) -> None: ...
    def apply_mask(self, other: PfmFile) -> None: ...
    def copy_channel(self, to_channel: int, other: PfmFile, from_channel: int) -> None: ...
    def copy_channel_masked(self, to_channel: int, other: PfmFile, from_channel: int) -> None: ...
    def apply_crop(self, x_begin: int, x_end: int, y_begin: int, y_end: int) -> None: ...
    def clear_to_texcoords(self, x_size: int, y_size: int) -> None: ...
    def pull_spot(self, delta: _Vec4f, xc: float, yc: float, xr: float, yr: float, exponent: float) -> int: ...
    def calc_tight_bounds(self, min_point: _Vec3f, max_point: _Vec3f) -> bool: ...
    def compute_planar_bounds(self, center: LVecBase2d | LVecBase2f, point_dist: float, sample_radius: float, points_only: bool) -> BoundingHexahedron: ...
    def compute_sample_point(self, result: _Vec3f, x: float, y: float, sample_radius: float) -> None: ...
    def copy_sub_image(self, copy: PfmFile, xto: int, yto: int, xfrom: int = ..., yfrom: int = ..., x_size: int = ..., y_size: int = ...) -> None: ...
    def add_sub_image(self, copy: PfmFile, xto: int, yto: int, xfrom: int = ..., yfrom: int = ..., x_size: int = ..., y_size: int = ..., pixel_scale: float = ...) -> None: ...
    def mult_sub_image(self, copy: PfmFile, xto: int, yto: int, xfrom: int = ..., yfrom: int = ..., x_size: int = ..., y_size: int = ..., pixel_scale: float = ...) -> None: ...
    def divide_sub_image(self, copy: PfmFile, xto: int, yto: int, xfrom: int = ..., yfrom: int = ..., x_size: int = ..., y_size: int = ..., pixel_scale: float = ...) -> None: ...
    def indirect_1d_lookup(self, index_image: PfmFile, channel: int, pixel_values: PfmFile) -> None: ...
    def gamma_correct(self, from_gamma: float, to_gamma: float) -> None: ...
    def gamma_correct_alpha(self, from_gamma: float, to_gamma: float) -> None: ...
    @overload
    def apply_exponent(self, gray_exponent: float) -> None: ...
    @overload
    def apply_exponent(self, gray_exponent: float, alpha_exponent: float) -> None: ...
    @overload
    def apply_exponent(self, c0_exponent: float, c1_exponent: float, c2_exponent: float) -> None: ...
    @overload
    def apply_exponent(self, c0_exponent: float, c1_exponent: float, c2_exponent: float, c3_exponent: float) -> None: ...
    def output(self, out: ostream) -> None: ...
    def get_points(self) -> Any: ...
    storeMask = store_mask
    isValid = is_valid
    getScale = get_scale
    setScale = set_scale
    hasPoint = has_point
    getChannel = get_channel
    setChannel = set_channel
    getPoint1 = get_point1
    setPoint1 = set_point1
    getPoint2 = get_point2
    setPoint2 = set_point2
    modifyPoint2 = modify_point2
    getPoint = get_point
    setPoint = set_point
    modifyPoint = modify_point
    getPoint3 = get_point3
    setPoint3 = set_point3
    modifyPoint3 = modify_point3
    getPoint4 = get_point4
    setPoint4 = set_point4
    modifyPoint4 = modify_point4
    fillNan = fill_nan
    fillNoDataValue = fill_no_data_value
    fillChannel = fill_channel
    fillChannelNan = fill_channel_nan
    fillChannelMasked = fill_channel_masked
    fillChannelMaskedNan = fill_channel_masked_nan
    calcAveragePoint = calc_average_point
    calcBilinearPoint = calc_bilinear_point
    calcMinMax = calc_min_max
    calcAutocrop = calc_autocrop
    isRowEmpty = is_row_empty
    isColumnEmpty = is_column_empty
    setZeroSpecial = set_zero_special
    setNoDataChan4 = set_no_data_chan4
    setNoDataNan = set_no_data_nan
    setNoDataValue = set_no_data_value
    setNoDataThreshold = set_no_data_threshold
    clearNoDataValue = clear_no_data_value
    hasNoDataValue = has_no_data_value
    hasNoDataThreshold = has_no_data_threshold
    getNoDataValue = get_no_data_value
    boxFilterFrom = box_filter_from
    gaussianFilterFrom = gaussian_filter_from
    quickFilterFrom = quick_filter_from
    reverseRows = reverse_rows
    forwardDistort = forward_distort
    reverseDistort = reverse_distort
    apply1dLut = apply_1d_lut
    applyMask = apply_mask
    copyChannel = copy_channel
    copyChannelMasked = copy_channel_masked
    applyCrop = apply_crop
    clearToTexcoords = clear_to_texcoords
    pullSpot = pull_spot
    calcTightBounds = calc_tight_bounds
    computePlanarBounds = compute_planar_bounds
    computeSamplePoint = compute_sample_point
    copySubImage = copy_sub_image
    addSubImage = add_sub_image
    multSubImage = mult_sub_image
    divideSubImage = divide_sub_image
    indirect1dLookup = indirect_1d_lookup
    gammaCorrect = gamma_correct
    gammaCorrectAlpha = gamma_correct_alpha
    applyExponent = apply_exponent
    getPoints = get_points

class PNMBrush(ReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    BE_set: ClassVar[Literal[0]]
    BE_blend: ClassVar[Literal[1]]
    BE_darken: ClassVar[Literal[2]]
    BE_lighten: ClassVar[Literal[3]]
    @staticmethod
    def make_transparent() -> PNMBrush: ...
    @staticmethod
    def make_pixel(color: _Vec4f, effect: _PNMBrush_BrushEffect = ...) -> PNMBrush: ...
    @staticmethod
    def make_spot(color: _Vec4f, radius: float, fuzzy: bool, effect: _PNMBrush_BrushEffect = ...) -> PNMBrush: ...
    @staticmethod
    def make_image(image: PNMImage, xc: float, yc: float, effect: _PNMBrush_BrushEffect = ...) -> PNMBrush: ...
    makeTransparent = make_transparent
    makePixel = make_pixel
    makeSpot = make_spot
    makeImage = make_image
    BESet = BE_set
    BEBlend = BE_blend
    BEDarken = BE_darken
    BELighten = BE_lighten

class PNMImage(PNMImageHeader):
    class Row:
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: PNMImage.Row) -> None: ...
        def __len__(self) -> int: ...
        def __getitem__(self, x: int) -> LVecBase4f: ...
        def __setitem__(self, x: int, v: _Vec4f) -> None: ...
        def get_xel_val(self, x: int) -> pixel: ...
        def set_xel_val(self, x: int, v: pixel) -> None: ...
        def get_alpha_val(self, x: int) -> int: ...
        def set_alpha_val(self, x: int, v: int) -> None: ...
        getXelVal = get_xel_val
        setXelVal = set_xel_val
        getAlphaVal = get_alpha_val
        setAlphaVal = set_alpha_val
    class CRow:
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: PNMImage.CRow) -> None: ...
        def __len__(self) -> int: ...
        def __getitem__(self, x: int) -> LVecBase4f: ...
        def get_xel_val(self, x: int) -> pixel: ...
        def get_alpha_val(self, x: int) -> int: ...
        getXelVal = get_xel_val
        getAlphaVal = get_alpha_val
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: PNMImage) -> None: ...
    @overload
    def __init__(self, filename: _Filename, type: PNMFileType = ...) -> None: ...
    @overload
    def __init__(self, x_size: int, y_size: int, num_channels: int = ..., maxval: int = ..., type: PNMFileType = ..., color_space: _ColorSpace = ...) -> None: ...
    def __getitem__(self, y: int) -> PNMImage.CRow | PNMImage.Row: ...
    def __invert__(self) -> PNMImage: ...
    def __add__(self, other: PNMImage | _Vec4f) -> PNMImage: ...
    def __sub__(self, other: PNMImage | _Vec4f) -> PNMImage: ...
    @overload
    def __mul__(self, other: PNMImage | _Vec4f) -> PNMImage: ...
    @overload
    def __mul__(self, multiplier: float) -> PNMImage: ...
    def __iadd__(self, other: PNMImage | _Vec4f) -> PNMImage: ...
    def __isub__(self, other: PNMImage | _Vec4f) -> PNMImage: ...
    @overload
    def __imul__(self, other: PNMImage | _Vec4f) -> PNMImage: ...
    @overload
    def __imul__(self, multiplier: float) -> PNMImage: ...
    def assign(self, copy: PNMImage) -> PNMImage: ...
    def clamp_val(self, input_value: int) -> int: ...
    @overload
    def to_val(self, input_value: _Vec3f) -> pixel: ...
    @overload
    def to_val(self, input_value: float) -> int: ...
    def to_alpha_val(self, input_value: float) -> int: ...
    @overload
    def from_val(self, input_value: pixel) -> LVecBase3f: ...
    @overload
    def from_val(self, input_value: int) -> float: ...
    def from_alpha_val(self, input_value: int) -> float: ...
    @overload
    def clear(self) -> None: ...
    @overload
    def clear(self, x_size: int, y_size: int, num_channels: int = ..., maxval: int = ..., type: PNMFileType = ..., color_space: _ColorSpace = ...) -> None: ...
    def copy_from(self, copy: PNMImage) -> None: ...
    @overload
    def copy_channel(self, copy: PNMImage, src_channel: int, dest_channel: int) -> None: ...
    @overload
    def copy_channel(self, copy: PNMImage, xto: int, yto: int, cto: int, xfrom: int = ..., yfrom: int = ..., cfrom: int = ..., x_size: int = ..., y_size: int = ...) -> None: ...
    def copy_channel_bits(self, copy: PNMImage, src_channel: int, dest_channel: int, src_mask: int, right_shift: int) -> None: ...
    def copy_header_from(self, header: PNMImageHeader) -> None: ...
    def take_from(self, orig: PNMImage) -> None: ...
    @overload
    def fill(self, gray: float = ...) -> None: ...
    @overload
    def fill(self, red: float, green: float, blue: float) -> None: ...
    @overload
    def fill_val(self, gray: int = ...) -> None: ...
    @overload
    def fill_val(self, red: int, green: int, blue: int) -> None: ...
    def alpha_fill(self, alpha: float = ...) -> None: ...
    def alpha_fill_val(self, alpha: int = ...) -> None: ...
    def set_read_size(self, x_size: int, y_size: int) -> None: ...
    def clear_read_size(self) -> None: ...
    def has_read_size(self) -> bool: ...
    def get_read_x_size(self) -> int: ...
    def get_read_y_size(self) -> int: ...
    def get_color_space(self) -> _ColorSpace: ...
    @overload
    def read(self, filename: _Filename, type: PNMFileType = ..., report_unknown_type: bool = ...) -> bool: ...
    @overload
    def read(self, data: istream, filename: str = ..., type: PNMFileType = ..., report_unknown_type: bool = ...) -> bool: ...
    @overload
    def write(self, filename: _Filename, type: PNMFileType = ...) -> bool: ...
    @overload
    def write(self, data: ostream, filename: str = ..., type: PNMFileType = ...) -> bool: ...
    def is_valid(self) -> bool: ...
    def set_num_channels(self, num_channels: int) -> None: ...
    def set_color_type(self, color_type: _PNMImageHeader_ColorType) -> None: ...
    def set_color_space(self, color_space: _ColorSpace) -> None: ...
    def add_alpha(self) -> None: ...
    def remove_alpha(self) -> None: ...
    @overload
    def make_grayscale(self) -> None: ...
    @overload
    def make_grayscale(self, rc: float, gc: float, bc: float) -> None: ...
    def make_rgb(self) -> None: ...
    def premultiply_alpha(self) -> None: ...
    def unpremultiply_alpha(self) -> None: ...
    def reverse_rows(self) -> None: ...
    def flip(self, flip_x: bool, flip_y: bool, transpose: bool) -> None: ...
    def set_maxval(self, maxval: int) -> None: ...
    def get_xel_val(self, x: int, y: int) -> pixel: ...
    @overload
    def set_xel_val(self, x: int, y: int, value: pixel) -> None: ...
    @overload
    def set_xel_val(self, x: int, y: int, gray: int) -> None: ...
    @overload
    def set_xel_val(self, x: int, y: int, r: int, g: int, b: int) -> None: ...
    def get_red_val(self, x: int, y: int) -> int: ...
    def get_green_val(self, x: int, y: int) -> int: ...
    def get_blue_val(self, x: int, y: int) -> int: ...
    def get_gray_val(self, x: int, y: int) -> int: ...
    def get_alpha_val(self, x: int, y: int) -> int: ...
    def set_red_val(self, x: int, y: int, r: int) -> None: ...
    def set_green_val(self, x: int, y: int, g: int) -> None: ...
    def set_blue_val(self, x: int, y: int, b: int) -> None: ...
    def set_gray_val(self, x: int, y: int, gray: int) -> None: ...
    def set_alpha_val(self, x: int, y: int, a: int) -> None: ...
    def get_channel_val(self, x: int, y: int, channel: int) -> int: ...
    def set_channel_val(self, x: int, y: int, channel: int, value: int) -> None: ...
    def get_channel(self, x: int, y: int, channel: int) -> float: ...
    def set_channel(self, x: int, y: int, channel: int, value: float) -> None: ...
    def get_pixel(self, x: int, y: int) -> PNMImageHeader.PixelSpec: ...
    def set_pixel(self, x: int, y: int, pixel: PNMImageHeader.PixelSpec) -> None: ...
    def get_xel(self, x: int, y: int) -> LVecBase3f: ...
    @overload
    def set_xel(self, x: int, y: int, value: _Vec3f) -> None: ...
    @overload
    def set_xel(self, x: int, y: int, gray: float) -> None: ...
    @overload
    def set_xel(self, x: int, y: int, r: float, g: float, b: float) -> None: ...
    def get_xel_a(self, x: int, y: int) -> LVecBase4f: ...
    @overload
    def set_xel_a(self, x: int, y: int, value: _Vec4f) -> None: ...
    @overload
    def set_xel_a(self, x: int, y: int, r: float, g: float, b: float, a: float) -> None: ...
    def get_red(self, x: int, y: int) -> float: ...
    def get_green(self, x: int, y: int) -> float: ...
    def get_blue(self, x: int, y: int) -> float: ...
    def get_gray(self, x: int, y: int) -> float: ...
    def get_alpha(self, x: int, y: int) -> float: ...
    def set_red(self, x: int, y: int, r: float) -> None: ...
    def set_green(self, x: int, y: int, g: float) -> None: ...
    def set_blue(self, x: int, y: int, b: float) -> None: ...
    def set_gray(self, x: int, y: int, gray: float) -> None: ...
    def set_alpha(self, x: int, y: int, a: float) -> None: ...
    @overload
    def get_bright(self, x: int, y: int) -> float: ...
    @overload
    def get_bright(self, x: int, y: int, rc: float, gc: float, bc: float) -> float: ...
    @overload
    def get_bright(self, x: int, y: int, rc: float, gc: float, bc: float, ac: float) -> float: ...
    @overload
    def blend(self, x: int, y: int, val: _Vec3f, alpha: float) -> None: ...
    @overload
    def blend(self, x: int, y: int, r: float, g: float, b: float, alpha: float) -> None: ...
    def copy_sub_image(self, copy: PNMImage, xto: int, yto: int, xfrom: int = ..., yfrom: int = ..., x_size: int = ..., y_size: int = ...) -> None: ...
    def blend_sub_image(self, copy: PNMImage, xto: int, yto: int, xfrom: int = ..., yfrom: int = ..., x_size: int = ..., y_size: int = ..., pixel_scale: float = ...) -> None: ...
    def add_sub_image(self, copy: PNMImage, xto: int, yto: int, xfrom: int = ..., yfrom: int = ..., x_size: int = ..., y_size: int = ..., pixel_scale: float = ...) -> None: ...
    def mult_sub_image(self, copy: PNMImage, xto: int, yto: int, xfrom: int = ..., yfrom: int = ..., x_size: int = ..., y_size: int = ..., pixel_scale: float = ...) -> None: ...
    def darken_sub_image(self, copy: PNMImage, xto: int, yto: int, xfrom: int = ..., yfrom: int = ..., x_size: int = ..., y_size: int = ..., pixel_scale: float = ...) -> None: ...
    def lighten_sub_image(self, copy: PNMImage, xto: int, yto: int, xfrom: int = ..., yfrom: int = ..., x_size: int = ..., y_size: int = ..., pixel_scale: float = ...) -> None: ...
    def threshold(self, select_image: PNMImage, channel: int, threshold: float, lt: PNMImage, ge: PNMImage) -> None: ...
    def fill_distance_inside(self, mask: PNMImage, threshold: float, radius: int, shrink_from_border: bool) -> None: ...
    def fill_distance_outside(self, mask: PNMImage, threshold: float, radius: int) -> None: ...
    def indirect_1d_lookup(self, index_image: PNMImage, channel: int, pixel_values: PNMImage) -> None: ...
    def rescale(self, min_val: float, max_val: float) -> None: ...
    def render_spot(self, fg: _Vec4f, bg: _Vec4f, min_radius: float, max_radius: float) -> None: ...
    def expand_border(self, left: int, right: int, bottom: int, top: int, color: _Vec4f) -> None: ...
    def box_filter(self, radius: float = ...) -> None: ...
    def gaussian_filter(self, radius: float = ...) -> None: ...
    def unfiltered_stretch_from(self, copy: PNMImage) -> None: ...
    def box_filter_from(self, radius: float, copy: PNMImage) -> None: ...
    def gaussian_filter_from(self, radius: float, copy: PNMImage) -> None: ...
    def quick_filter_from(self, copy: PNMImage, xborder: int = ..., yborder: int = ...) -> None: ...
    def make_histogram(self, hist: PNMImageHeader.Histogram) -> None: ...
    def quantize(self, max_colors: int) -> None: ...
    @overload
    def perlin_noise_fill(self, perlin: StackedPerlinNoise2) -> None: ...
    @overload
    def perlin_noise_fill(self, sx: float, sy: float, table_size: int = ..., seed: int = ...) -> None: ...
    def remix_channels(self, conv: _Mat4f) -> None: ...
    def gamma_correct(self, from_gamma: float, to_gamma: float) -> None: ...
    def gamma_correct_alpha(self, from_gamma: float, to_gamma: float) -> None: ...
    @overload
    def apply_exponent(self, gray_exponent: float) -> None: ...
    @overload
    def apply_exponent(self, gray_exponent: float, alpha_exponent: float) -> None: ...
    @overload
    def apply_exponent(self, red_exponent: float, green_exponent: float, blue_exponent: float) -> None: ...
    @overload
    def apply_exponent(self, red_exponent: float, green_exponent: float, blue_exponent: float, alpha_exponent: float) -> None: ...
    def get_average_xel(self) -> LVecBase3f: ...
    def get_average_xel_a(self) -> LVecBase4f: ...
    def get_average_gray(self) -> float: ...
    def do_fill_distance(self, xi: int, yi: int, d: int) -> None: ...
    clampVal = clamp_val
    toVal = to_val
    toAlphaVal = to_alpha_val
    fromVal = from_val
    fromAlphaVal = from_alpha_val
    copyFrom = copy_from
    copyChannel = copy_channel
    copyChannelBits = copy_channel_bits
    copyHeaderFrom = copy_header_from
    takeFrom = take_from
    fillVal = fill_val
    alphaFill = alpha_fill
    alphaFillVal = alpha_fill_val
    setReadSize = set_read_size
    clearReadSize = clear_read_size
    hasReadSize = has_read_size
    getReadXSize = get_read_x_size
    getReadYSize = get_read_y_size
    getColorSpace = get_color_space
    isValid = is_valid
    setNumChannels = set_num_channels
    setColorType = set_color_type
    setColorSpace = set_color_space
    addAlpha = add_alpha
    removeAlpha = remove_alpha
    makeGrayscale = make_grayscale
    makeRgb = make_rgb
    premultiplyAlpha = premultiply_alpha
    unpremultiplyAlpha = unpremultiply_alpha
    reverseRows = reverse_rows
    setMaxval = set_maxval
    getXelVal = get_xel_val
    setXelVal = set_xel_val
    getRedVal = get_red_val
    getGreenVal = get_green_val
    getBlueVal = get_blue_val
    getGrayVal = get_gray_val
    getAlphaVal = get_alpha_val
    setRedVal = set_red_val
    setGreenVal = set_green_val
    setBlueVal = set_blue_val
    setGrayVal = set_gray_val
    setAlphaVal = set_alpha_val
    getChannelVal = get_channel_val
    setChannelVal = set_channel_val
    getChannel = get_channel
    setChannel = set_channel
    getPixel = get_pixel
    setPixel = set_pixel
    getXel = get_xel
    setXel = set_xel
    getXelA = get_xel_a
    setXelA = set_xel_a
    getRed = get_red
    getGreen = get_green
    getBlue = get_blue
    getGray = get_gray
    getAlpha = get_alpha
    setRed = set_red
    setGreen = set_green
    setBlue = set_blue
    setGray = set_gray
    setAlpha = set_alpha
    getBright = get_bright
    copySubImage = copy_sub_image
    blendSubImage = blend_sub_image
    addSubImage = add_sub_image
    multSubImage = mult_sub_image
    darkenSubImage = darken_sub_image
    lightenSubImage = lighten_sub_image
    fillDistanceInside = fill_distance_inside
    fillDistanceOutside = fill_distance_outside
    indirect1dLookup = indirect_1d_lookup
    renderSpot = render_spot
    expandBorder = expand_border
    boxFilter = box_filter
    gaussianFilter = gaussian_filter
    unfilteredStretchFrom = unfiltered_stretch_from
    boxFilterFrom = box_filter_from
    gaussianFilterFrom = gaussian_filter_from
    quickFilterFrom = quick_filter_from
    makeHistogram = make_histogram
    perlinNoiseFill = perlin_noise_fill
    remixChannels = remix_channels
    gammaCorrect = gamma_correct
    gammaCorrectAlpha = gamma_correct_alpha
    applyExponent = apply_exponent
    getAverageXel = get_average_xel
    getAverageXelA = get_average_xel_a
    getAverageGray = get_average_gray
    doFillDistance = do_fill_distance

class PNMPainter:
    DtoolClassDict: ClassVar[dict[str, Any]]
    pen: PNMBrush
    fill: PNMBrush
    @overload
    def __init__(self, __param0: PNMPainter) -> None: ...
    @overload
    def __init__(self, image: PNMImage, xo: int = ..., yo: int = ...) -> None: ...
    def set_pen(self, pen: PNMBrush) -> None: ...
    def get_pen(self) -> PNMBrush: ...
    def set_fill(self, fill: PNMBrush) -> None: ...
    def get_fill(self) -> PNMBrush: ...
    def draw_point(self, x: float, y: float) -> None: ...
    def draw_line(self, xa: float, ya: float, xb: float, yb: float) -> None: ...
    def draw_rectangle(self, xa: float, ya: float, xb: float, yb: float) -> None: ...
    setPen = set_pen
    getPen = get_pen
    setFill = set_fill
    getFill = get_fill
    drawPoint = draw_point
    drawLine = draw_line
    drawRectangle = draw_rectangle

def decode_sRGB_float(val: float | str) -> float: ...
def decode_sRGB_uchar(val: float | str) -> str: ...
def encode_sRGB_float(val: float | str) -> float: ...
def encode_sRGB_uchar(val: float | str) -> str: ...
decodeSRGBFloat = decode_sRGB_float
decodeSRGBUchar = decode_sRGB_uchar
encodeSRGBFloat = encode_sRGB_float
encodeSRGBUchar = encode_sRGB_uchar
Pixel = pixel
xel = pixel
Xel = xel
