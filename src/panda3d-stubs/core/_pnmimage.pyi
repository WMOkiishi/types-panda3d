from _typeshed import StrOrBytesPath
from collections.abc import Iterator, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import DoubleMat4Like, DoubleVec2Like, DoubleVec3Like, DoubleVec4Like, Mat4Like, Vec2Like, Vec3Like, Vec4Like
from panda3d.core._dtoolbase import TypeHandle
from panda3d.core._dtoolutil import istream, ostream
from panda3d.core._express import ReferenceCount
from panda3d.core._linmath import LColorf, LPoint2f, LPoint3f, LPoint4f, LRGBColorf, LVecBase2i
from panda3d.core._mathutil import BoundingHexahedron, StackedPerlinNoise2
from panda3d.core._putil import TypedWritable

_ColorSpace: TypeAlias = Literal[0, 1, 2, 3]
_PNMImageHeader_ColorType: TypeAlias = Literal[0, 1, 2, 3, 4]
_PNMBrush_BrushEffect: TypeAlias = Literal[0, 1, 2, 3]

class pixel:
    DtoolClassDict: ClassVar[dict[str, Any]]
    b: int
    g: int
    r: int
    @overload
    def __init__(self, fill: int = ...) -> None: ...
    @overload
    def __init__(self, __param0: pixel) -> None: ...
    @overload
    def __init__(self, r: int, g: int, b: int) -> None: ...
    def __getitem__(self, i: int) -> int: ...
    def __setitem__(self, i: int, assign_val: int) -> None: ...
    def __add__(self, other: pixel) -> pixel: ...
    def __sub__(self, other: pixel) -> pixel: ...
    def __mul__(self, mult: float) -> pixel: ...
    def __iadd__(self, other: pixel) -> Self: ...
    def __isub__(self, other: pixel) -> Self: ...
    def __imul__(self, mult: float) -> Self: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: pixel) -> bool: ...
    def __len__(self) -> int: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def __iter__(self) -> Iterator[int]: ...  # Doesn't actually exist
    def output(self, out: ostream) -> None: ...

class PNMFileType(TypedWritable):
    """This is the base class of a family of classes that represent particular
    image file types that PNMImage supports.
    """

    @property
    def name(self) -> str: ...
    @property
    def extensions(self) -> Sequence[str]: ...
    @property
    def suggested_extension(self) -> str: ...
    def get_name(self) -> str: ...
    def get_num_extensions(self) -> int:
        """Returns the number of different possible filename extensions associated
        with this particular file type.
        """
    def get_extension(self, n: int) -> str:
        """Returns the nth possible filename extension associated with this particular
        file type, without a leading dot.
        """
    def get_suggested_extension(self) -> str:
        """Returns a suitable filename extension (without a leading dot) to suggest
        for files of this type, or empty string if no suggestions are available.
        """
    def get_extensions(self) -> tuple[str, ...]: ...
    getName = get_name
    getNumExtensions = get_num_extensions
    getExtension = get_extension
    getSuggestedExtension = get_suggested_extension
    getExtensions = get_extensions

class PNMFileTypeRegistry:
    """This class maintains the set of all known PNMFileTypes in the universe."""

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def types(self) -> Sequence[PNMFileType]: ...
    def __init__(self, __param0: PNMFileTypeRegistry) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_num_types(self) -> int:
        """Returns the total number of types registered."""
    def get_type(self, n: int) -> PNMFileType:
        """Returns the nth type registered."""
    def get_type_from_extension(self, filename: str) -> PNMFileType:
        """Tries to determine what the PNMFileType is likely to be for a particular
        image file based on its extension.  Returns a suitable PNMFileType pointer,
        or NULL if no type can be determined.
        """
    def get_type_from_magic_number(self, magic_number: str) -> PNMFileType:
        """Tries to determine what the PNMFileType is likely to be for a particular
        image file based on its magic number, the first two bytes read from the
        file.  Returns a suitable PNMFileType pointer, or NULL if no type can be
        determined.
        """
    def get_type_by_handle(self, handle: TypeHandle | type) -> PNMFileType:
        """Returns the PNMFileType instance stored in the registry for the given
        TypeHandle, e.g.  as retrieved by a previous call to get_type() on the type
        instance.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes a list of supported image file types to the indicated output stream,
        one per line.
        """
    @staticmethod
    def get_global_ptr() -> PNMFileTypeRegistry:
        """Returns a pointer to the global PNMFileTypeRegistry object."""
    def get_types(self) -> tuple[PNMFileType, ...]: ...
    getNumTypes = get_num_types
    getType = get_type
    getTypeFromExtension = get_type_from_extension
    getTypeFromMagicNumber = get_type_from_magic_number
    getTypeByHandle = get_type_by_handle
    getGlobalPtr = get_global_ptr
    getTypes = get_types

class PNMImageHeader:
    """This is the base class of PNMImage, PNMReader, and PNMWriter.  It
    encapsulates all the information associated with an image that describes
    its size, number of channels, etc; that is, all the information about the
    image except the image data itself.  It's the sort of information you
    typically read from the image file's header.
    """

    class PixelSpec:
        """Contains a single pixel specification used in compute_histogram() and
        make_histogram().  Note that pixels are stored by integer value, not by
        floating-point scaled value.
        """

        DtoolClassDict: ClassVar[dict[str, Any]]
        @overload
        def __init__(self, __param0: PNMImageHeader.PixelSpec) -> None: ...
        @overload
        def __init__(self, rgb: xel, alpha: int = ...) -> None: ...
        @overload
        def __init__(self, gray_value: int, alpha: int = ...) -> None: ...
        @overload
        def __init__(self, red: int, green: int, blue: int, alpha: int = ...) -> None: ...
        def __lt__(self, other: PNMImageHeader.PixelSpec | pixel) -> bool: ...
        def __eq__(self, __other: object) -> bool: ...
        def __ne__(self, __other: object) -> bool: ...
        def __getitem__(self, n: int) -> int: ...
        def __len__(self) -> int:
            """Specifies the number of components in the PixelSpec; this is always 4,
            regardless of the type of image it was taken from.
            """
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...
        def __iter__(self) -> Iterator[int]: ...  # Doesn't actually exist
        def compare_to(self, other: PNMImageHeader.PixelSpec | pixel) -> int: ...
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
        """Associates a pixel specification with an appearance count, for use in
        Histogram, below.
        """

        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: PNMImageHeader.PixelSpecCount) -> None: ...
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...

    class Histogram:
        """Used to return a pixel histogram in PNMImage::get_histogram()."""

        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: PNMImageHeader.Histogram = ...) -> None: ...
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...
        def get_num_pixels(self) -> int:
            """Returns the number of unique pixel colors in the histogram."""
        def get_pixel(self, n: int) -> PNMImageHeader.PixelSpec:
            """Returns the nth unique pixel color in the histogram.  These are ordered by
            default from most common to least common.
            """
        @overload
        def get_count(self, pixel: PNMImageHeader.PixelSpec | pixel) -> int:
            """`(self, pixel: PNMImageHeader.PixelSpec)`:
            Returns the number of occurrences in the image of the indicated pixel
            color.

            `(self, n: int)`:
            Returns the number of occurrences in the image of the nth unique pixel
            color in the histogram.
            """
        @overload
        def get_count(self, n: int) -> int: ...
        def write(self, out: ostream) -> None: ...
        def get_pixels(self) -> tuple[PNMImageHeader.PixelSpec, ...]: ...
        getNumPixels = get_num_pixels
        getPixel = get_pixel
        getCount = get_count
        getPixels = get_pixels

    CT_invalid: Final = 0
    CTInvalid: Final = 0
    CT_grayscale: Final = 1
    CTGrayscale: Final = 1
    CT_two_channel: Final = 2
    CTTwoChannel: Final = 2
    CT_color: Final = 3
    CTColor: Final = 3
    CT_four_channel: Final = 4
    CTFourChannel: Final = 4
    DtoolClassDict: ClassVar[dict[str, Any]]
    comment: str
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
    def __init__(self, copy: PNMImageHeader = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def get_color_type(self) -> _PNMImageHeader_ColorType:
        """Returns the image type of the image, as an enumerated value.  This is
        really just the number of channels cast to the enumerated type.
        """
    def get_num_channels(self) -> int:
        """Returns the number of channels in the image."""
    def is_grayscale(self, color_type: _PNMImageHeader_ColorType = ...) -> bool:
        """`(self)`:
        Returns false if the image is a full-color image, and has red, green, and
        blue components; true if it is a grayscale image and has only a gray
        component.  (The gray color is actually stored in the blue channel, and the
        red and green channels are ignored.)

        `(self, color_type: _PNMImageHeader_ColorType)`:
        This static variant of is_grayscale() returns true if the indicated image
        type represents a grayscale image, false otherwise.
        """
    def has_alpha(self, color_type: _PNMImageHeader_ColorType = ...) -> bool:
        """`(self)`:
        Returns true if the image includes an alpha channel, false otherwise.
        Unlike is_grayscale(), if this returns false it is an error to call any of
        the functions accessing the alpha channel.

        `(self, color_type: _PNMImageHeader_ColorType)`:
        This static variant of has_alpha() returns true if the indicated image type
        includes an alpha channel, false otherwise.
        """
    def get_maxval(self) -> int:
        """Returns the maximum channel value allowable for any pixel in this image;
        for instance, 255 for a typical 8-bit-per-channel image.  A pixel with this
        value is full on.
        """
    def get_color_space(self) -> _ColorSpace:
        """Returns the color space that the image is encoded in, or CS_unspecified if
        unknown.
        """
    def get_x_size(self) -> int:
        """Returns the number of pixels in the X direction.  This is one more than the
        largest allowable X coordinate.
        """
    def get_y_size(self) -> int:
        """Returns the number of pixels in the Y direction.  This is one more than the
        largest allowable Y coordinate.
        """
    def get_size(self) -> LVecBase2i:
        """Returns the number of pixels in each direction.  This is one more than the
        largest allowable coordinates.
        """
    def get_comment(self) -> str:
        """Gets the user comment from the file."""
    def set_comment(self, comment: str) -> None:
        """Writes a user comment string to the image (header)."""
    def has_type(self) -> bool:
        """Returns true if the PNMImageHeader knows what type it is, false otherwise."""
    def get_type(self) -> PNMFileType:
        """If the file type is known (e.g.  has_type() returns true), returns its
        PNMFileType pointer; otherwise, returns NULL.
        """
    def set_type(self, type: PNMFileType) -> None:
        """Sets the file type of this PNMImage.  This will be the default type used
        when an image is read, if the type cannot be determined by magic number or
        inferred by extension, or the type used when the image is written, if the
        type cannot be inferred from the filename extension.
        """
    @overload
    def read_header(self, filename: StrOrBytesPath, type: PNMFileType = ..., report_unknown_type: bool = ...) -> bool:
        """`(self, filename: Filename, type: PNMFileType = ..., report_unknown_type: bool = ...)`:
        Opens up the image file and tries to read its header information to
        determine its size, number of channels, etc.  If successful, updates the
        header information and returns true; otherwise, returns false.

        `(self, data: istream, filename: str = ..., type: PNMFileType = ..., report_unknown_type: bool = ...)`:
        Reads the image header information only from the indicated stream.

        The filename is advisory only, and may be used to suggest a type if it has
        a known extension.

        If type is non-NULL, it is a suggestion for the type of file it is (and a
        non-NULL type will override any magic number test or filename extension
        lookup).

        Returns true if successful, false on error.
        """
    @overload
    def read_header(
        self, data: istream, filename: str = ..., type: PNMFileType = ..., report_unknown_type: bool = ...
    ) -> bool: ...
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

class PfmFile(PNMImageHeader):
    """Defines a pfm file, a 2-d table of floating-point numbers, either
    3-component or 1-component, or with a special extension, 2- or 4-component.
    """

    scale: float
    @property
    def valid(self) -> bool: ...
    def __init__(self, copy: PfmFile = ...) -> None: ...
    def __imul__(self, multiplier: float) -> Self: ...
    @overload
    def clear(self) -> None:
        """`(self)`:
        Eliminates all data in the file.

        `(self, x_size: int, y_size: int, num_channels: int)`:
        Resets to an empty table with a specific size.  The case of num_channels ==
        0 is allowed only in the case that x_size and y_size are also == 0; and
        this makes an empty (and invalid) PfmFile.
        """
    @overload
    def clear(self, x_size: int, y_size: int, num_channels: int) -> None: ...
    @overload
    def read(self, fullpath: StrOrBytesPath) -> bool:
        """`(self, fullpath: Filename)`:
        Reads the PFM data from the indicated file, returning true on success,
        false on failure.

        This can also handle reading a standard image file supported by PNMImage;
        it will be quietly converted to a floating-point type.

        `(self, _in: istream, fullpath: Filename = ...)`:
        Reads the PFM data from the indicated stream, returning true on success,
        false on failure.

        This can also handle reading a standard image file supported by PNMImage;
        it will be quietly converted to a floating-point type.
        """
    @overload
    def read(self, _in: istream, fullpath: StrOrBytesPath = ...) -> bool: ...
    @overload
    def write(self, fullpath: StrOrBytesPath) -> bool:
        """`(self, fullpath: Filename)`:
        Writes the PFM data to the indicated file, returning true on success, false
        on failure.

        If the type implied by the filename extension supports floating-point, the
        data will be written directly; otherwise, the floating-point data will be
        quietly converted to the appropriate integer type.

        `(self, out: ostream, fullpath: Filename = ...)`:
        Writes the PFM data to the indicated stream, returning true on success,
        false on failure.
        """
    @overload
    def write(self, out: ostream, fullpath: StrOrBytesPath = ...) -> bool: ...
    def load(self, pnmimage: PNMImage) -> bool:
        """Fills the PfmFile with the data from the indicated PNMImage, converted to
        floating-point values.
        """
    def store(self, pnmimage: PNMImage) -> bool:
        """Copies the data to the indicated PNMImage, converting to RGB values."""
    @overload
    def store_mask(self, pnmimage: PNMImage) -> bool:
        """`(self, pnmimage: PNMImage)`:
        Stores 1 or 0 values into the indicated PNMImage, according to has_point()
        for each pixel.  Each valid point gets a 1 value; each nonexistent point
        gets a 0 value.

        `(self, pnmimage: PNMImage, min_point: LVecBase4f, max_point: LVecBase4f)`:
        Stores 1 or 0 values into the indicated PNMImage, according to has_point()
        for each pixel.  Each valid point gets a 1 value; each nonexistent point
        gets a 0 value.

        This flavor of store_mask also checks whether the valid points are within
        the specified min/max range.  Any valid points without the condition
        min_point[c] <= value[c] <= max_point[c], for any c, are stored with a 0 in
        the mask.
        """
    @overload
    def store_mask(self, pnmimage: PNMImage, min_point: Vec4Like, max_point: Vec4Like) -> bool: ...
    def is_valid(self) -> bool: ...
    def get_scale(self) -> float:
        """The "scale" is reported in the pfm header and is probably meaningless."""
    def set_scale(self, scale: float) -> None:
        """The "scale" is reported in the pfm header and is probably meaningless."""
    def has_point(self, x: int, y: int) -> bool:
        """Returns true if there is a valid point at x, y.  This always returns true
        unless a "no data" value has been set, in which case it returns false if
        the point at x, y is the "no data" value.
        """
    def get_channel(self, x: int, y: int, c: int) -> float:
        """Returns the cth channel of the point value at the indicated point."""
    def set_channel(self, x: int, y: int, c: int, value: float) -> None:
        """Replaces the cth channel of the point value at the indicated point."""
    def get_point1(self, x: int, y: int) -> float:
        """Returns the 1-component point value at the indicated point."""
    def set_point1(self, x: int, y: int, point: float) -> None:
        """Replaces the 1-component point value at the indicated point."""
    def get_point2(self, x: int, y: int) -> LPoint2f:
        """Returns the 2-component point value at the indicated point.  In a 1-channel
        image, the channel value is in the x component.
        """
    def set_point2(self, x: int, y: int, point: DoubleVec2Like | Vec2Like) -> None:
        """Replaces the 2-component point value at the indicated point.  In a
        1-channel image, the channel value is in the x component.
        """
    def modify_point2(self, x: int, y: int) -> LPoint2f:
        """Returns a modifiable 2-component point value at the indicated point."""
    def get_point(self, x: int, y: int) -> LPoint3f:
        """Returns the 3-component point value at the indicated point.  In a 1-channel
        image, the channel value is in the x component.
        """
    def set_point(self, x: int, y: int, point: DoubleVec3Like | Vec3Like) -> None:
        """Replaces the 3-component point value at the indicated point.  In a
        1-channel image, the channel value is in the x component.
        """
    def modify_point(self, x: int, y: int) -> LPoint3f:
        """Returns a modifiable 3-component point value at the indicated point."""
    def get_point3(self, x: int, y: int) -> LPoint3f:
        """Returns the 3-component point value at the indicated point.  In a 1-channel
        image, the channel value is in the x component.
        """
    def set_point3(self, x: int, y: int, point: DoubleVec3Like | Vec3Like) -> None:
        """Replaces the 3-component point value at the indicated point.  In a
        1-channel image, the channel value is in the x component.
        """
    def modify_point3(self, x: int, y: int) -> LPoint3f:
        """Returns a modifiable 3-component point value at the indicated point."""
    def get_point4(self, x: int, y: int) -> LPoint4f:
        """Returns the 4-component point value at the indicated point.  In a 1-channel
        image, the channel value is in the x component.
        """
    def set_point4(self, x: int, y: int, point: DoubleVec4Like | Vec4Like) -> None:
        """Replaces the 4-component point value at the indicated point.  In a
        1-channel image, the channel value is in the x component.
        """
    def modify_point4(self, x: int, y: int) -> LPoint4f:
        """Returns a modifiable 4-component point value at the indicated point."""
    def fill(self, value: Vec2Like | Vec3Like | Vec4Like | float) -> None:
        """Fills the table with all of the same value."""
    def fill_nan(self) -> None:
        """Fills the table with all NaN."""
    def fill_no_data_value(self) -> None:
        """Fills the table with the current no_data value, so that the table is empty."""
    def fill_channel(self, channel: int, value: float) -> None:
        """Fills the indicated channel with all of the same value, leaving the other
        channels unchanged.
        """
    def fill_channel_nan(self, channel: int) -> None:
        """Fills the indicated channel with NaN, leaving the other channels unchanged."""
    def fill_channel_masked(self, channel: int, value: float) -> None:
        """Fills the indicated channel with all of the same value, but only where the
        table already has a data point.  Leaves empty points unchanged.
        """
    def fill_channel_masked_nan(self, channel: int) -> None:
        """Fills the indicated channel with NaN, but only where the table already has
        a data point.  Leaves empty points unchanged.
        """
    def calc_average_point(self, result: Vec3Like, x: float, y: float, radius: float) -> bool:
        """Computes the unweighted average point of all points within the box centered
        at (x, y) with the indicated Manhattan-distance radius.  Missing points are
        assigned the value of their nearest neighbor.  Returns true if successful,
        or false if the point value cannot be determined.
        """
    def calc_bilinear_point(self, result: Vec3Like, x: float, y: float) -> bool:
        """Computes the weighted average of the four nearest points to the floating-
        point index (x, y).  Returns true if the point has any contributors, false
        if the point is unknown.
        """
    def calc_min_max(self, min_points: Vec3Like, max_points: Vec3Like) -> bool:
        """Calculates the minimum and maximum x, y, and z depth component values,
        representing the bounding box of depth values, and places them in the
        indicated vectors.  Returns true if successful, false if the mesh contains
        no points.
        """
    def calc_autocrop(self, range: DoubleVec4Like | Vec4Like) -> bool:
        """Computes the minimum range of x and y across the PFM file that include all
        points.  If there are no points with no_data_value in the grid--that is,
        all points are included--then this will return (0, get_x_size(), 0,
        get_y_size()).
        """
    def is_row_empty(self, y: int, x_begin: int, x_end: int) -> bool:
        """Returns true if all of the points on row y, in the range [x_begin, x_end),
        are the no_data value, or false if any one of these points has a value.
        """
    def is_column_empty(self, x: int, y_begin: int, y_end: int) -> bool:
        """Returns true if all of the points on column x, from [y_begin, y_end), are
        the no_data value, or false if any one of these points has a value.
        """
    def set_zero_special(self, zero_special: bool) -> None:
        """Sets the zero_special flag.  When this flag is true, values of (0, 0, 0) in
        the pfm file are treated as a special case, and are not processed.

        This is a special case of set_no_data_value().
        """
    def set_no_data_chan4(self, chan4: bool) -> None:
        """Sets the no_data_chan4 flag.  When this flag is true, and the pfm file has
        4 channels, then a negative value in the fourth channel indicates no data.
        When it is false, all points are valid.

        This is a special case of set_no_data_value().
        """
    def set_no_data_nan(self, num_channels: int) -> None:
        """Sets the no_data_nan flag.  When num_channels is nonzero, then a NaN value
        in any of the first num_channels channels indicates no data for that point.
        If num_channels is zero, then all points are valid.

        This is a special case of set_no_data_value().
        """
    def set_no_data_value(self, no_data_value: DoubleVec4Like | Vec4Like) -> None:
        """Sets the special value that means "no data" when it appears in the pfm
        file.
        """
    def set_no_data_threshold(self, no_data_value: DoubleVec4Like | Vec4Like) -> None:
        """Sets the special threshold value.  Points that are below this value in all
        components are considered "no value".
        """
    def clear_no_data_value(self) -> None:
        """Removes the special value that means "no data" when it appears in the pfm
        file.  All points will thus be considered valid.
        """
    def has_no_data_value(self) -> bool:
        """Returns whether a "no data" value has been established by
        set_no_data_value().
        """
    def has_no_data_threshold(self) -> bool:
        """Returns whether a "no data" threshold value has been established by
        set_no_data_threshold().
        """
    def get_no_data_value(self) -> LPoint4f:
        """If has_no_data_value() returns true, this returns the particular "no data"
        value.
        """
    def resize(self, new_x_size: int, new_y_size: int) -> None:
        """Applies a simple filter to resample the pfm file in-place to the indicated
        size.  Don't confuse this with applying a scale to all of the points via
        xform().
        """
    def box_filter_from(self, radius: float, copy: PfmFile) -> None:
        """Makes a resized copy of the indicated image into this one using the
        indicated filter.  The image to be copied is squashed and stretched to
        match the dimensions of the current image, applying the appropriate filter
        to perform the stretching.
        """
    def gaussian_filter_from(self, radius: float, copy: PfmFile) -> None:
        """Makes a resized copy of the indicated image into this one using the
        indicated filter.  The image to be copied is squashed and stretched to
        match the dimensions of the current image, applying the appropriate filter
        to perform the stretching.
        """
    def quick_filter_from(self, copy: PfmFile) -> None:
        """Resizes from the given image, with a fixed radius of 0.5. This is a very
        specialized and simple algorithm that doesn't handle dropping below the
        Nyquist rate very well, but is quite a bit faster than the more general
        box_filter(), above.
        """
    def reverse_rows(self) -> None:
        """Performs an in-place reversal of the row (y) data."""
    def flip(self, flip_x: bool, flip_y: bool, transpose: bool) -> None:
        """Reverses, transposes, and/or rotates the table in-place according to the
        specified parameters.  If flip_x is true, the x axis is reversed; if flip_y
        is true, the y axis is reversed.  Then, if transpose is true, the x and y
        axes are exchanged.  These parameters can be used to select any combination
        of 90-degree or 180-degree rotations and flips.
        """
    def xform(self, transform: DoubleMat4Like | Mat4Like) -> None:
        """Applies the indicated transform matrix to all points in-place."""
    def forward_distort(self, dist: PfmFile, scale_factor: float = ...) -> None:
        """Applies the distortion indicated in the supplied dist map to the current
        map.  The dist map is understood to be a mapping of points in the range
        0..1 in the first two dimensions.

        The operation can be expressed symbolically as:

        this(u, v) = this(dist(u, v))

        If scale_factor is not 1, it should be a value > 1, and it specifies the
        factor to upscale the working table while processing, to reduce artifacts
        from integer truncation.

        By convention, the y axis is inverted in the distortion map relative to the
        coordinates here.  A y value of 0 in the distortion map corresponds with a
        v value of 1 in this file.
        """
    def reverse_distort(self, dist: PfmFile, scale_factor: float = ...) -> None:
        """Applies the distortion indicated in the supplied dist map to the current
        map.  The dist map is understood to be a mapping of points in the range
        0..1 in the first two dimensions.

        The operation can be expressed symbolically as:

        this(u, v) = dist(this(u, v))

        If scale_factor is not 1, it should be a value > 1, and it specifies the
        factor to upscale the working table while processing, to reduce artifacts
        from integer truncation.

        By convention, the y axis in inverted in the distortion map relative to the
        coordinates here.  A y value of 0 in the distortion map corresponds with a
        v value of 1 in this file.
        """
    def apply_1d_lut(self, channel: int, lut: PfmFile, x_scale: float = ...) -> None:
        """Assumes that lut is an X by 1, 1-component PfmFile whose X axis maps points
        to target points.  For each point in this pfm file, computes: p(u,
        v)[channel] = lut(p(u, v)[channel] * x_scale, 0)[0]
        """
    def merge(self, other: PfmFile) -> None:
        """Wherever there is missing data in this PfmFile (that is, wherever
        has_point() returns false), copy data from the other PfmFile, which must be
        exactly the same dimensions as this one.
        """
    def apply_mask(self, other: PfmFile) -> None:
        """Wherever there is missing data in the other PfmFile, set this the
        corresponding point in this PfmFile to missing as well, so that this
        PfmFile has only points where both files have points.

        The point is set to "missing" by setting it the no_data_value.
        """
    def copy_channel(self, to_channel: int, other: PfmFile, from_channel: int) -> None:
        """Copies just the specified channel values from the indicated PfmFile (which
        could be same as this PfmFile) into the specified channel of this one.
        """
    def copy_channel_masked(self, to_channel: int, other: PfmFile, from_channel: int) -> None:
        """Copies just the specified channel values from the indicated PfmFile, but
        only where the other file has a data point.
        """
    def apply_crop(self, x_begin: int, x_end: int, y_begin: int, y_end: int) -> None:
        """Reduces the PFM file to the cells in the rectangle bounded by (x_begin,
        x_end, y_begin, y_end), where the _end cells are not included.
        """
    def clear_to_texcoords(self, x_size: int, y_size: int) -> None:
        """Replaces this PfmFile with a new PfmFile of size x_size x y_size x 3,
        containing the x y 0 values in the range 0 .. 1 according to the x y index.
        """
    def pull_spot(self, delta: Vec4Like, xc: float, yc: float, xr: float, yr: float, exponent: float) -> int:
        """Applies delta * t to the point values within radius (xr, yr) distance of
        (xc, yc).  The t value is scaled from 1.0 at the center to 0.0 at radius
        (xr, yr), and this scale follows the specified exponent.  Returns the
        number of points affected.
        """
    def calc_tight_bounds(self, min_point: Vec3Like, max_point: Vec3Like) -> bool:
        """Calculates the minimum and maximum vertices of all points within the table.
        Assumes the table contains 3-D points.

        The return value is true if any points in the table, or false if none are.
        """
    def compute_planar_bounds(
        self, center: DoubleVec2Like | Vec2Like, point_dist: float, sample_radius: float, points_only: bool
    ) -> BoundingHexahedron:
        """Computes the minmax bounding volume of the points in 3-D space, assuming
        the points represent a mostly-planar surface.

        This algorithm works by sampling the (square) sample_radius pixels at the
        four point_dist corners around the center (cx - pd, cx + pd) and so on, to
        approximate the plane of the surface.  Then all of the points are projected
        into that plane and the bounding volume of the entire mesh within that
        plane is determined.  If points_only is true, the bounding volume of only
        those four points is determined.

        center, point_dist and sample_radius are in UV space, i.e.  in the range
        0..1.
        """
    def compute_sample_point(self, result: Vec3Like, x: float, y: float, sample_radius: float) -> None:
        """Computes the average of all the point within sample_radius (manhattan
        distance) and the indicated point.

        The point coordinates are given in UV space, in the range 0..1.
        """
    def copy_sub_image(
        self, copy: PfmFile, xto: int, yto: int, xfrom: int = ..., yfrom: int = ..., x_size: int = ..., y_size: int = ...
    ) -> None:
        """Copies a rectangular area of another image into a rectangular area of this
        image.  Both images must already have been initialized.  The upper-left
        corner of the region in both images is specified, and the size of the area;
        if the size is omitted, it defaults to the entire other image, or the
        largest piece that will fit.
        """
    def add_sub_image(
        self,
        copy: PfmFile,
        xto: int,
        yto: int,
        xfrom: int = ...,
        yfrom: int = ...,
        x_size: int = ...,
        y_size: int = ...,
        pixel_scale: float = ...,
    ) -> None:
        """Behaves like copy_sub_image(), except the copy pixels are added to the
        pixels of the destination, after scaling by the specified pixel_scale.
        """
    def mult_sub_image(
        self,
        copy: PfmFile,
        xto: int,
        yto: int,
        xfrom: int = ...,
        yfrom: int = ...,
        x_size: int = ...,
        y_size: int = ...,
        pixel_scale: float = ...,
    ) -> None:
        """Behaves like copy_sub_image(), except the copy pixels are multiplied to the
        pixels of the destination, after scaling by the specified pixel_scale.
        """
    def divide_sub_image(
        self,
        copy: PfmFile,
        xto: int,
        yto: int,
        xfrom: int = ...,
        yfrom: int = ...,
        x_size: int = ...,
        y_size: int = ...,
        pixel_scale: float = ...,
    ) -> None:
        """Behaves like copy_sub_image(), except the copy pixels are divided into the
        pixels of the destination, after scaling by the specified pixel_scale.
        dest(x, y) = dest(x, y) / (copy(x, y) * pixel_scale).
        """
    def indirect_1d_lookup(self, index_image: PfmFile, channel: int, pixel_values: PfmFile) -> None:
        """index_image is a WxH 1-channel image, while pixel_values is an Nx1
        image with any number of channels.  Typically pixel_values will be
        a 256x1 image.

        Fills the PfmFile with a new image the same width and height as
        index_image, with the same number of channels as pixel_values.

        Each pixel of the new image is computed with the formula:

        new_image(x, y) = pixel_values(index_image(x, y)[channel], 0)

        At present, no interpolation is performed; the nearest value in
        pixel_values is discovered.  This may change in the future.
        """
    def gamma_correct(self, from_gamma: float, to_gamma: float) -> None:
        """Assuming the image was constructed with a gamma curve of from_gamma in the
        RGB channels, converts it to an image with a gamma curve of to_gamma in the
        RGB channels.  Does not affect the alpha channel.
        """
    def gamma_correct_alpha(self, from_gamma: float, to_gamma: float) -> None:
        """Assuming the image was constructed with a gamma curve of from_gamma in the
        alpha channel, converts it to an image with a gamma curve of to_gamma in
        the alpha channel.  Does not affect the RGB channels.
        """
    @overload
    def apply_exponent(self, gray_exponent: float, alpha_exponent: float = ...) -> None:
        """`(self, gray_exponent: float)`; `(self, gray_exponent: float, alpha_exponent: float)`; `(self, c0_exponent: float, c1_exponent: float, c2_exponent: float, c3_exponent: float)`:
        Adjusts each channel of the image by raising the corresponding component
        value to the indicated exponent, such that L' = L ^ exponent.

        `(self, c0_exponent: float, c1_exponent: float, c2_exponent: float)`:
        Adjusts each channel of the image by raising the corresponding component
        value to the indicated exponent, such that L' = L ^ exponent.  For a
        grayscale image, the blue_exponent value is used for the grayscale value,
        and red_exponent and green_exponent are unused.
        """
    @overload
    def apply_exponent(self, c0_exponent: float, c1_exponent: float, c2_exponent: float, c3_exponent: float = ...) -> None: ...
    def get_points(self): ...
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
    """This class is used to control the shape and color of the drawing operations
    performed by a PNMPainter object.

    Normally, you don't create a PNMBrush directly; instead, use one of the
    static PNMBrush::make_*() methods provided here.

    A PNMBrush is used to draw the border of a polygon or rectangle, as well as
    for filling its interior.  When it is used to draw a border, the brush is
    "smeared" over the border; when it is used to fill the interior, it is
    tiled through the interior.
    """

    BE_set: Final = 0
    BESet: Final = 0
    BE_blend: Final = 1
    BEBlend: Final = 1
    BE_darken: Final = 2
    BEDarken: Final = 2
    BE_lighten: Final = 3
    BELighten: Final = 3
    @staticmethod
    def make_transparent() -> PNMBrush:
        """Returns a new brush that does not paint anything.  Can be used as either a
        pen or a fill brush to make borderless or unfilled shapes, respectively.
        """
    @staticmethod
    def make_pixel(color: Vec4Like, effect: _PNMBrush_BrushEffect = ...) -> PNMBrush:
        """Returns a new brush that paints a single pixel of the indicated color on a
        border, or paints a solid color in an interior.
        """
    @staticmethod
    def make_spot(color: Vec4Like, radius: float, fuzzy: bool, effect: _PNMBrush_BrushEffect = ...) -> PNMBrush:
        """Returns a new brush that paints a spot of the indicated color and radius.
        If fuzzy is true, the spot is fuzzy; otherwise, it is hard-edged.
        """
    @staticmethod
    def make_image(image: PNMImage, xc: float, yc: float, effect: _PNMBrush_BrushEffect = ...) -> PNMBrush:
        """Returns a new brush that paints with the indicated image.  xc and yc
        indicate the pixel in the center of the brush.

        The brush makes a copy of the image; it is safe to deallocate or modify the
        image after making this call.
        """
    makeTransparent = make_transparent
    makePixel = make_pixel
    makeSpot = make_spot
    makeImage = make_image

class PNMImage(PNMImageHeader):
    """The name of this class derives from the fact that we originally implemented
    it as a layer on top of the "pnm library", based on netpbm, which was built
    to implement pbm, pgm, and pbm files, and is the underlying support of a
    number of public-domain image file converters.  Nowadays we are no longer
    derived directly from the pnm library, mainly to allow support of C++
    iostreams instead of the C stdio FILE interface.

    Conceptually, a PNMImage is a two-dimensional array of xels, which are the
    PNM-defined generic pixel type.  Each xel may have a red, green, and blue
    component, or (if the image is grayscale) a gray component.  The image may
    be read in, the individual xels manipulated, and written out again, or a
    black image may be constructed from scratch.

    A PNMImage has a color space and a maxval, the combination of which defines
    how a floating-point linear color value is encoded as an integer value in
    memory.  The functions ending in _val operate on encoded colors, whereas
    the regular ones work with linear floating-point values.  All operations
    are color space correct unless otherwise specified.

    The image is of size XSize() by YSize() xels, numbered from top to bottom,
    left to right, beginning at zero.

    Files can be specified by filename, or by an iostream pointer.  The
    filename "-" refers to stdin or stdout.

    This class is not inherently thread-safe; use it from a single thread or
    protect access using a mutex.
    """

    class Row:
        """Provides an accessor for reading or writing the contents of one row of
        the image in-place.
        """

        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: PNMImage.Row) -> None: ...
        def __len__(self) -> int:
            """Get the number of pixels in the row."""
        def __getitem__(self, x: int) -> LColorf: ...
        def __setitem__(self, x: int, v: Vec4Like) -> None:
            """Set the pixel at the given column in the row.  If the image has no alpha
            channel, the alpha component is ignored.
            """
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...
        def __iter__(self) -> Iterator[LColorf]: ...  # Doesn't actually exist
        def get_xel_val(self, x: int) -> xel:
            """Fetch the pixel at the given column in the row."""
        def set_xel_val(self, x: int, v: xel) -> None:
            """Set the pixel at the given column in the row."""
        def get_alpha_val(self, x: int) -> int:
            """Fetch the alpha value at the given column in the row."""
        def set_alpha_val(self, x: int, v: int) -> None:
            """Set the alpha value at the given column in the row."""
        getXelVal = get_xel_val
        setXelVal = set_xel_val
        getAlphaVal = get_alpha_val
        setAlphaVal = set_alpha_val

    class CRow:
        """Provides an accessor for reading the contents of one row of the image in-
        place.
        """

        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: PNMImage.CRow) -> None: ...
        def __len__(self) -> int:
            """Get the number of pixels in the row."""
        def __getitem__(self, x: int) -> LColorf: ...
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...
        def __iter__(self) -> Iterator[LColorf]: ...  # Doesn't actually exist
        def get_xel_val(self, x: int) -> xel:
            """Fetch the pixel at the given column in the row."""
        def get_alpha_val(self, x: int) -> int:
            """Fetch the alpha value at the given column in the row."""
        getXelVal = get_xel_val
        getAlphaVal = get_alpha_val

    @overload
    def __init__(self, copy: PNMImage = ...) -> None: ...
    @overload
    def __init__(self, filename: StrOrBytesPath, type: PNMFileType = ...) -> None: ...
    @overload
    def __init__(
        self,
        x_size: int,
        y_size: int,
        num_channels: int = ...,
        maxval: int = ...,
        type: PNMFileType = ...,
        color_space: _ColorSpace = ...,
    ) -> None: ...
    def __getitem__(self, y: int) -> PNMImage.CRow | PNMImage.Row: ...
    def __invert__(self) -> PNMImage: ...
    def __add__(self, other: PNMImage | Vec4Like) -> PNMImage: ...
    def __sub__(self, other: PNMImage | Vec4Like) -> PNMImage: ...
    @overload
    def __mul__(self, other: PNMImage | Vec4Like) -> PNMImage: ...
    @overload
    def __mul__(self, multiplier: float) -> PNMImage: ...
    def __iadd__(self, other: PNMImage | Vec4Like) -> Self: ...
    def __isub__(self, other: PNMImage | Vec4Like) -> Self: ...
    @overload
    def __imul__(self, other: PNMImage | Vec4Like) -> Self: ...
    @overload
    def __imul__(self, multiplier: float) -> Self: ...
    def clamp_val(self, input_value: int) -> int:
        """A handy function to clamp values to [0..get_maxval()]."""
    @overload
    def to_val(self, input_value: Vec3Like) -> xel:
        """A handy function to scale non-alpha values from [0..1] to
        [0..get_maxval()].  Do not use this for alpha values, see to_alpha_val.
        """
    @overload
    def to_val(self, input_value: float) -> int: ...
    def to_alpha_val(self, input_value: float) -> int:
        """A handy function to scale alpha values from [0..1] to [0..get_maxval()]."""
    @overload
    def from_val(self, input_value: xel) -> LRGBColorf:
        """A handy function to scale non-alpha values from [0..get_maxval()] to
        [0..1].  Do not use this for alpha values, see from_alpha_val.
        """
    @overload
    def from_val(self, input_value: int) -> float: ...
    def from_alpha_val(self, input_value: int) -> float:
        """A handy function to scale alpha values from [0..get_maxval()] to [0..1]."""
    @overload
    def clear(self) -> None:
        """`(self)`:
        Frees all memory allocated for the image, and clears all its parameters
        (size, color, type, etc).

        `(self, x_size: int, y_size: int, num_channels: int = ..., maxval: int = ..., type: PNMFileType = ..., color_space: _ColorSpace = ...)`:
        This flavor of clear() reinitializes the image to an empty (black) image
        with the given dimensions.
        """
    @overload
    def clear(
        self,
        x_size: int,
        y_size: int,
        num_channels: int = ...,
        maxval: int = ...,
        type: PNMFileType = ...,
        color_space: _ColorSpace = ...,
    ) -> None: ...
    def copy_from(self, copy: PNMImage) -> None:
        """Makes this image become a copy of the other image."""
    @overload
    def copy_channel(self, copy: PNMImage, src_channel: int, dest_channel: int) -> None:
        """`(self, copy: PNMImage, src_channel: int, dest_channel: int)`:
        Copies a channel from one image into another.  Images must be the same size

        `(self, copy: PNMImage, xto: int, yto: int, cto: int, xfrom: int = ..., yfrom: int = ..., cfrom: int = ..., x_size: int = ..., y_size: int = ...)`:
        Copies just a single channel from the source image into a single channel of
        this image, leaving the remaining channels alone.
        """
    @overload
    def copy_channel(
        self,
        copy: PNMImage,
        xto: int,
        yto: int,
        cto: int,
        xfrom: int = ...,
        yfrom: int = ...,
        cfrom: int = ...,
        x_size: int = ...,
        y_size: int = ...,
    ) -> None: ...
    def copy_channel_bits(self, copy: PNMImage, src_channel: int, dest_channel: int, src_mask: int, right_shift: int) -> None:
        """Copies some subset of the bits of the specified channel from one image into
        some subset of the bits of the specified channel in another image.  Images
        must be the same size.

        If right_shift is negative, it means a left shift.
        """
    def copy_header_from(self, header: PNMImageHeader) -> None:
        """Copies just the header information into this image.  This will blow away
        any image data stored in the image.  The new image data will be allocated,
        but left unitialized.
        """
    def take_from(self, orig: PNMImage) -> None:
        """Move the contents of the other image into this one, and empty the other
        image.
        """
    @overload
    def fill(self, gray: float = ...) -> None:
        """`(self, gray: float = ...)`:
        Sets the entire image (except the alpha channel) to the given grayscale
        level.

        `(self, red: float, green: float, blue: float)`:
        Sets the entire image (except the alpha channel) to the given color.
        """
    @overload
    def fill(self, red: float, green: float, blue: float) -> None: ...
    @overload
    def fill_val(self, gray: int = ...) -> None:
        """`(self, gray: int = ...)`:
        Sets the entire image (except the alpha channel) to the given grayscale
        level.

        `(self, red: int, green: int, blue: int)`:
        Sets the entire image (except the alpha channel) to the given color.
        """
    @overload
    def fill_val(self, red: int, green: int, blue: int) -> None: ...
    def alpha_fill(self, alpha: float = ...) -> None:
        """Sets the entire alpha channel to the given level."""
    def alpha_fill_val(self, alpha: int = ...) -> None:
        """Sets the entire alpha channel to the given level."""
    def set_read_size(self, x_size: int, y_size: int) -> None:
        """Specifies the size to we'd like to scale the image upon reading it.  This
        will affect the next call to read().  This is usually used to reduce the
        image size, e.g.  for a thumbnail.

        If the file type reader supports it (e.g.  JPEG), then this will scale the
        image during the read operation, consequently reducing memory and CPU
        utilization.  If the file type reader does not support it, this will load
        the image normally, and them perform a linear scale after it has been
        loaded.
        """
    def clear_read_size(self) -> None:
        """Undoes the effect of a previous call to set_read_size()."""
    def has_read_size(self) -> bool:
        """Returns true if set_read_size() has been called."""
    def get_read_x_size(self) -> int:
        """Returns the requested x_size of the image if set_read_size() has been
        called, or the image x_size otherwise (if it is known).
        """
    def get_read_y_size(self) -> int:
        """Returns the requested y_size of the image if set_read_size() has been
        called, or the image y_size otherwise (if it is known).
        """
    def get_color_space(self) -> _ColorSpace:
        """Returns the color space in which the image is encoded."""
    @overload
    def read(self, filename: StrOrBytesPath, type: PNMFileType = ..., report_unknown_type: bool = ...) -> bool:
        """`(self, filename: Filename, type: PNMFileType = ..., report_unknown_type: bool = ...)`:
        Reads the indicated image filename.  If type is non-NULL, it is a
        suggestion for the type of file it is.  Returns true if successful, false
        on error.

        `(self, data: istream, filename: str = ..., type: PNMFileType = ..., report_unknown_type: bool = ...)`:
        Reads the image data from the indicated stream.

        The filename is advisory only, and may be used to suggest a type if it has
        a known extension.

        If type is non-NULL, it is a suggestion for the type of file it is (and a
        non-NULL type will override any magic number test or filename extension
        lookup).

        Returns true if successful, false on error.
        """
    @overload
    def read(self, data: istream, filename: str = ..., type: PNMFileType = ..., report_unknown_type: bool = ...) -> bool: ...
    @overload
    def write(self, filename: StrOrBytesPath, type: PNMFileType = ...) -> bool:
        """`(self, filename: Filename, type: PNMFileType = ...)`:
        Writes the image to the indicated filename.  If type is non-NULL, it is a
        suggestion for the type of image file to write.

        `(self, data: ostream, filename: str = ..., type: PNMFileType = ...)`:
        Writes the image to the indicated ostream.

        The filename is advisory only, and may be used suggest a type if it has a
        known extension.

        If type is non-NULL, it is a suggestion for the type of image file to
        write.
        """
    @overload
    def write(self, data: ostream, filename: str = ..., type: PNMFileType = ...) -> bool: ...
    def is_valid(self) -> bool:
        """Returns true if the image has been read in or correctly initialized with a
        height and width.  If this returns false, virtually all member functions
        except clear() and read() are invalid function calls.
        """
    def set_num_channels(self, num_channels: int) -> None:
        """Changes the number of channels associated with the image.  The new number
        of channels must be an integer in the range 1 through 4, inclusive.  This
        will allocate and/or deallocate memory as necessary to accommodate; see
        set_color_type().
        """
    def set_color_type(self, color_type: _PNMImageHeader_ColorType) -> None:
        """Translates the image to or from grayscale, color, or four-color mode.
        Grayscale images are converted to full-color images with R, G, B set to the
        original gray level; color images are converted to grayscale according to
        the value of Bright().  The alpha channel, if added, is initialized to
        zero.
        """
    def set_color_space(self, color_space: _ColorSpace) -> None:
        """Converts the colors in the image to the indicated color space.  This may be
        a lossy operation, in particular when going from sRGB to linear.  The alpha
        channel remains untouched.

        Note that, because functions like get_xel() and set_xel() work on
        linearized floating-point values, this conversion won't affect those values
        (aside from some minor discrepancies due to storage precision).  It does
        affect the values used by get_xel_val() and set_xel_val(), though, since
        those operate on encoded colors.

        Some color spaces, particularly scRGB, may enforce the use of a particular
        maxval setting.
        """
    def add_alpha(self) -> None:
        """Adds an alpha channel to the image, if it does not already have one.  The
        alpha channel is initialized to zeros.
        """
    def remove_alpha(self) -> None:
        """Removes the image's alpha channel, if it exists."""
    @overload
    def make_grayscale(self) -> None:
        """`(self)`:
        Converts the image from RGB to grayscale.  Any alpha channel, if present,
        is left undisturbed.

        `(self, rc: float, gc: float, bc: float)`:
        Converts the image from RGB to grayscale.  Any alpha channel, if present,
        is left undisturbed.  The optional rc, gc, bc values represent the relative
        weights to apply to each channel to convert it to grayscale.
        """
    @overload
    def make_grayscale(self, rc: float, gc: float, bc: float) -> None: ...
    def make_rgb(self) -> None:
        """Converts the image from grayscale to RGB.  Any alpha channel, if present,
        is left undisturbed.
        """
    def premultiply_alpha(self) -> None:
        """Converts an image in-place to its "premultiplied" form, where, for every
        pixel in the image, the red, green, and blue components are multiplied by
        that pixel's alpha value.

        This does not modify any alpha values.
        """
    def unpremultiply_alpha(self) -> None:
        """Converts an image in-place to its "straight alpha" form (presumably from a
        "premultiplied" form), where, for every pixel in the image, the red, green,
        and blue components are divided by that pixel's alpha value.

        This does not modify any alpha values.
        """
    def reverse_rows(self) -> None:
        """Performs an in-place reversal of the row (y) data."""
    def flip(self, flip_x: bool, flip_y: bool, transpose: bool) -> None:
        """Reverses, transposes, and/or rotates the image in-place according to the
        specified parameters.  If flip_x is true, the x axis is reversed; if flip_y
        is true, the y axis is reversed.  Then, if transpose is true, the x and y
        axes are exchanged.  These parameters can be used to select any combination
        of 90-degree or 180-degree rotations and flips.
        """
    def set_maxval(self, maxval: int) -> None:
        """Rescales the image to the indicated maxval."""
    def get_xel_val(self, x: int, y: int) -> xel:
        """Returns the RGB color at the indicated pixel.  Each component is in the
        range 0..maxval.
        """
    @overload
    def set_xel_val(self, x: int, y: int, value: xel) -> None:
        """`(self, x: int, y: int, value: xel)`; `(self, x: int, y: int, r: int, g: int, b: int)`:
        Changes the RGB color at the indicated pixel.  Each component is in the
        range 0..maxval, encoded in the configured color space.  See set_xel if you
        instead have a linearized and normalized floating-point value.

        `(self, x: int, y: int, gray: int)`:
        Changes all three color components at the indicated pixel to the same
        value.  The value is in the range component is in the range 0..maxval,
        encoded in the configured color space.  See set_xel if you instead have a
        linearized and normalized floating-point value.
        """
    @overload
    def set_xel_val(self, x: int, y: int, gray: int) -> None: ...
    @overload
    def set_xel_val(self, x: int, y: int, r: int, g: int, b: int) -> None: ...
    def get_red_val(self, x: int, y: int) -> int:
        """Returns the red component color at the indicated pixel.  The value returned
        is in the range 0..maxval and encoded in the configured color space.
        """
    def get_green_val(self, x: int, y: int) -> int:
        """Returns the green component color at the indicated pixel.  The value
        returned is in the range 0..maxval and encoded in the configured color
        space.
        """
    def get_blue_val(self, x: int, y: int) -> int:
        """Returns the blue component color at the indicated pixel.  The value
        returned is in the range 0..maxval and encoded in the configured color
        space.
        """
    def get_gray_val(self, x: int, y: int) -> int:
        """Returns the gray component color at the indicated pixel.  This only has a
        meaningful value for grayscale images; for other image types, this returns
        the value of the blue channel only.  However, also see the get_bright()
        function.  The value returned is in the range 0..maxval and encoded in the
        configured color space.
        """
    def get_alpha_val(self, x: int, y: int) -> int:
        """Returns the alpha component color at the indicated pixel.  It is an error
        to call this unless has_alpha() is true.  The value returned is in the
        range 0..maxval and always linear.
        """
    def set_red_val(self, x: int, y: int, r: int) -> None:
        """Sets the red component color only at the indicated pixel.  The value given
        should be in the range 0..maxval, encoded in the configured color space.
        See set_red if you instead have a linearized and normalized floating-point
        value.
        """
    def set_green_val(self, x: int, y: int, g: int) -> None:
        """Sets the green component color only at the indicated pixel.  The value
        given should be in the range 0..maxval, encoded in the configured color
        space.  See set_green if you instead have a linearized and normalized
        floating-point value.
        """
    def set_blue_val(self, x: int, y: int, b: int) -> None:
        """Sets the blue component color only at the indicated pixel.  The value given
        should be in the range 0..maxval, encoded in the configured color space.
        See set_blue if you instead have a linearized and normalized floating-point
        value.
        """
    def set_gray_val(self, x: int, y: int, gray: int) -> None:
        """Sets the gray component color at the indicated pixel.  This is only
        meaningful for grayscale images; for other image types, this simply sets
        the blue component color.  However, also see set_xel_val(), which can set
        all the component colors to the same grayscale level, and hence works
        correctly both for grayscale and color images.  The value given should be
        in the range 0..maxval, encoded in the configured color space.  See
        set_gray if you instead have a linearized normalized floating-point value.
        """
    def set_alpha_val(self, x: int, y: int, a: int) -> None:
        """Sets the alpha component color only at the indicated pixel.  It is an error
        to call this unless has_alpha() is true.  The value given should be in the
        range 0..maxval.

        This value is always linearly encoded, even if the image is set to the sRGB
        color space.
        """
    def get_channel_val(self, x: int, y: int, channel: int) -> int:
        """Returns the nth component color at the indicated pixel.  The channel index
        should be in the range 0..(get_num_channels()-1).  The channels are ordered
        B, G, R, A.  This is slightly less optimal than accessing the component
        values directly by named methods.  The value returned is in the range
        0..maxval.
        """
    def set_channel_val(self, x: int, y: int, channel: int, value: int) -> None:
        """Sets the nth component color at the indicated pixel.  The channel index
        should be in the range 0..(get_num_channels()-1).  The channels are ordered
        B, G, R, A.  This is slightly less optimal than setting the component
        values directly by named methods.  The value given should be in the range
        0..maxval.
        """
    def get_channel(self, x: int, y: int, channel: int) -> float:
        """Returns the nth component color at the indicated pixel.  The channel index
        should be in the range 0..(get_num_channels()-1).  The channels are ordered
        B, G, R, A.  This is slightly less optimal than accessing the component
        values directly by named methods.  The value returned is a float in the
        range 0..1.
        """
    def set_channel(self, x: int, y: int, channel: int, value: float) -> None:
        """Sets the nth component color at the indicated pixel.  The channel index
        should be in the range 0..(get_num_channels()-1).  The channels are ordered
        B, G, R, A.  This is slightly less optimal than setting the component
        values directly by named methods.  The value given should be a float in the
        range 0..1.
        """
    def get_pixel(self, x: int, y: int) -> PNMImageHeader.PixelSpec:
        """Returns the (r, g, b, a) pixel value at the indicated pixel, using a
        PixelSpec object.
        """
    def set_pixel(self, x: int, y: int, pixel: PNMImageHeader.PixelSpec | pixel) -> None:
        """Sets the (r, g, b, a) pixel value at the indicated pixel, using a PixelSpec
        object.
        """
    def get_xel(self, x: int, y: int) -> LRGBColorf:
        """Returns the RGB color at the indicated pixel.  Each component is a
        linearized float in the range 0..1.
        """
    @overload
    def set_xel(self, x: int, y: int, value: Vec3Like) -> None:
        """`(self, x: int, y: int, value: LRGBColorf)`; `(self, x: int, y: int, r: float, g: float, b: float)`:
        Changes the RGB color at the indicated pixel.  Each component is a
        linearized float in the range 0..1.

        `(self, x: int, y: int, gray: float)`:
        Changes all three color components at the indicated pixel to the same
        value.  The value is a linearized float in the range 0..1.
        """
    @overload
    def set_xel(self, x: int, y: int, gray: float) -> None: ...
    @overload
    def set_xel(self, x: int, y: int, r: float, g: float, b: float) -> None: ...
    def get_xel_a(self, x: int, y: int) -> LColorf:
        """Returns the RGBA color at the indicated pixel.  Each component is a
        linearized float in the range 0..1.
        """
    @overload
    def set_xel_a(self, x: int, y: int, value: Vec4Like) -> None:
        """Changes the RGBA color at the indicated pixel.  Each component is a
        linearized float in the range 0..1.
        """
    @overload
    def set_xel_a(self, x: int, y: int, r: float, g: float, b: float, a: float) -> None: ...
    def get_red(self, x: int, y: int) -> float:
        """Returns the red component color at the indicated pixel.  The value returned
        is a linearized float in the range 0..1.
        """
    def get_green(self, x: int, y: int) -> float:
        """Returns the green component color at the indicated pixel.  The value
        returned is a linearized float in the range 0..1.
        """
    def get_blue(self, x: int, y: int) -> float:
        """Returns the blue component color at the indicated pixel.  The value
        returned is a linearized float in the range 0..1.
        """
    def get_gray(self, x: int, y: int) -> float:
        """Returns the gray component color at the indicated pixel.  This only has a
        meaningful value for grayscale images; for other image types, this returns
        the value of the blue channel only.  However, also see the get_bright()
        function.  The value returned is a linearized float in the range 0..1.
        """
    def get_alpha(self, x: int, y: int) -> float:
        """Returns the alpha component color at the indicated pixel.  It is an error
        to call this unless has_alpha() is true.  The value returned is a float in
        the range 0..1.
        """
    def set_red(self, x: int, y: int, r: float) -> None:
        """Sets the red component color only at the indicated pixel.  The value given
        should be a linearized float in the range 0..1.
        """
    def set_green(self, x: int, y: int, g: float) -> None:
        """Sets the green component color only at the indicated pixel.  The value
        given should be a linearized float in the range 0..1.
        """
    def set_blue(self, x: int, y: int, b: float) -> None:
        """Sets the blue component color only at the indicated pixel.  The value given
        should be a linearized float in the range 0..1.
        """
    def set_gray(self, x: int, y: int, gray: float) -> None:
        """Sets the gray component color at the indicated pixel.  This is only
        meaningful for grayscale images; for other image types, this simply sets
        the blue component color.  However, also see set_xel(), which can set all
        the component colors to the same grayscale level, and hence works correctly
        both for grayscale and color images.  The value given should be a
        linearized float in the range 0..1.
        """
    def set_alpha(self, x: int, y: int, a: float) -> None:
        """Sets the alpha component color only at the indicated pixel.  It is an error
        to call this unless has_alpha() is true.  The value given should be in the
        range 0..1.
        """
    @overload
    def get_bright(self, x: int, y: int) -> float:
        """`(self, x: int, y: int)`:
        Returns the linear brightness of the given xel, as a linearized float in
        the range 0..1.  This flavor of get_bright() returns the correct grayscale
        brightness level for both full-color and grayscale images.

        `(self, x: int, y: int, rc: float, gc: float, bc: float)`:
        This flavor of get_bright() works correctly only for color images.  It
        returns a single brightness value for the RGB color at the indicated pixel,
        based on the supplied weights for each component.

        `(self, x: int, y: int, rc: float, gc: float, bc: float, ac: float)`:
        This flavor of get_bright() works correctly only for four-channel images.
        It returns a single brightness value for the RGBA color at the indicated
        pixel, based on the supplied weights for each component.
        """
    @overload
    def get_bright(self, x: int, y: int, rc: float, gc: float, bc: float, ac: float = ...) -> float: ...
    @overload
    def blend(self, x: int, y: int, val: Vec3Like, alpha: float) -> None:
        """Smoothly blends the indicated pixel value in with whatever was already in
        the image, based on the given alpha value.  An alpha of 1.0 is fully opaque
        and completely replaces whatever was there previously; alpha of 0.0 is
        fully transparent and does nothing.
        """
    @overload
    def blend(self, x: int, y: int, r: float, g: float, b: float, alpha: float) -> None: ...
    def copy_sub_image(
        self, copy: PNMImage, xto: int, yto: int, xfrom: int = ..., yfrom: int = ..., x_size: int = ..., y_size: int = ...
    ) -> None:
        """Copies a rectangular area of another image into a rectangular area of this
        image.  Both images must already have been initialized.  The upper-left
        corner of the region in both images is specified, and the size of the area;
        if the size is omitted, it defaults to the entire other image, or the
        largest piece that will fit.
        """
    def blend_sub_image(
        self,
        copy: PNMImage,
        xto: int,
        yto: int,
        xfrom: int = ...,
        yfrom: int = ...,
        x_size: int = ...,
        y_size: int = ...,
        pixel_scale: float = ...,
    ) -> None:
        """Behaves like copy_sub_image(), except the alpha channel of the copy is used
        to blend the copy into the destination image, instead of overwriting pixels
        unconditionally.

        If pixel_scale is not 1.0, it specifies an amount to scale each *alpha*
        value of the source image before applying it to the target image.

        If pixel_scale is 1.0 and the copy has no alpha channel, this degenerates
        into copy_sub_image().
        """
    def add_sub_image(
        self,
        copy: PNMImage,
        xto: int,
        yto: int,
        xfrom: int = ...,
        yfrom: int = ...,
        x_size: int = ...,
        y_size: int = ...,
        pixel_scale: float = ...,
    ) -> None:
        """Behaves like copy_sub_image(), except the copy pixels are added to the
        pixels of the destination, after scaling by the specified pixel_scale.
        Unlike blend_sub_image(), the alpha channel is not treated specially.
        """
    def mult_sub_image(
        self,
        copy: PNMImage,
        xto: int,
        yto: int,
        xfrom: int = ...,
        yfrom: int = ...,
        x_size: int = ...,
        y_size: int = ...,
        pixel_scale: float = ...,
    ) -> None:
        """Behaves like copy_sub_image(), except the copy pixels are multiplied to the
        pixels of the destination, after scaling by the specified pixel_scale.
        Unlike blend_sub_image(), the alpha channel is not treated specially.
        """
    def darken_sub_image(
        self,
        copy: PNMImage,
        xto: int,
        yto: int,
        xfrom: int = ...,
        yfrom: int = ...,
        x_size: int = ...,
        y_size: int = ...,
        pixel_scale: float = ...,
    ) -> None:
        """Behaves like copy_sub_image(), but the resulting color will be the darker
        of the source and destination colors at each pixel (and at each R, G, B, A
        component value).

        If pixel_scale is not 1.0, it specifies an amount to scale each pixel value
        of the source image before applying it to the target image.  The scale is
        applied with the center at 1.0: scaling the pixel value smaller brings it
        closer to 1.0.
        """
    def lighten_sub_image(
        self,
        copy: PNMImage,
        xto: int,
        yto: int,
        xfrom: int = ...,
        yfrom: int = ...,
        x_size: int = ...,
        y_size: int = ...,
        pixel_scale: float = ...,
    ) -> None:
        """Behaves like copy_sub_image(), but the resulting color will be the lighter
        of the source and destination colors at each pixel (and at each R, G, B, A
        component value).

        If pixel_scale is not 1.0, it specifies an amount to scale each pixel value
        of the source image before applying it to the target image.
        """
    def threshold(self, select_image: PNMImage, channel: int, threshold: float, lt: PNMImage, ge: PNMImage) -> None:
        """Selectively copies each pixel from either one source or another source,
        depending on the pixel value of the indicated channel of select_image.

        For each pixel (x, y):

        s = select_image.get_channel(x, y, channel). Set this image's (x, y) to:

        lt.get_xel(x, y) if s < threshold, or

        ge.get_xel(x, y) if s >= threshold

        Any of select_image, lt, or ge may be the same PNMImge object as this
        image, or the same as each other; or they may all be different.  All images
        must be the same size.  As a special case, lt and ge may both be 1x1 images
        instead of the source image size.
        """
    def fill_distance_inside(self, mask: PNMImage, threshold: float, radius: int, shrink_from_border: bool) -> None:
        """Replaces this image with a grayscale image whose gray channel represents
        the linear Manhattan distance from the nearest dark pixel in the given mask
        image, up to the specified radius value (which also becomes the new
        maxval).  radius may range from 0 to maxmaxval; smaller values will compute
        faster.  A dark pixel is defined as one whose pixel value is < threshold.

        If shrink_from_border is true, then the mask image is considered to be
        surrounded by a border of dark pixels; otherwise, the border isn't
        considered.

        This can be used, in conjunction with threshold, to shrink a mask image
        inwards by a certain number of pixels.

        The mask image may be the same image as this one, in which case it is
        destructively modified by this process.
        """
    def fill_distance_outside(self, mask: PNMImage, threshold: float, radius: int) -> None:
        """Replaces this image with a grayscale image whose gray channel represents
        the linear Manhattan distance from the nearest white pixel in the given
        mask image, up to the specified radius value (which also becomes the new
        maxval).  radius may range from 0 to maxmaxval; smaller values will compute
        faster.  A white pixel is defined as one whose pixel value is >= threshold.

        This can be used, in conjunction with threshold, to grow a mask image
        outwards by a certain number of pixels.

        The mask image may be the same image as this one, in which case it is
        destructively modified by this process.
        """
    def indirect_1d_lookup(self, index_image: PNMImage, channel: int, pixel_values: PNMImage) -> None:
        """index_image is a WxH grayscale image, while pixel_values is an Nx1 color
        (or grayscale) image.  Typically pixel_values will be a 256x1 image.

        Fills the PNMImage with a new image the same width and height as
        index_image, with the same number of channels as pixel_values.

        Each pixel of the new image is computed with the formula:

        new_image(x, y) = pixel_values(index_image(x, y)[channel], 0)

        At present, no interpolation is performed; the nearest value in
        pixel_values is discovered.  This may change in the future.
        """
    def rescale(self, min_val: float, max_val: float) -> None:
        """Rescales the RGB channel values so that any values in the original image
        between min_val and max_val are expanded to the range 0 .. 1.  Values below
        min_val are set to 0, and values above max_val are set to 1. Does not
        affect the alpha channel, if any.
        """
    def render_spot(self, fg: Vec4Like, bg: Vec4Like, min_radius: float, max_radius: float) -> None:
        """Renders a solid-color circle, with a fuzzy edge, into the center of the
        PNMImage.  If the PNMImage is non-square, this actually renders an ellipse.

        The min_radius and max_radius are in the scale 0..1, where 1.0 means the
        full width of the image.  If min_radius == max_radius, the edge is sharp
        (but still antialiased); otherwise, the pixels between min_radius and
        max_radius are smoothly blended between fg and bg colors.
        """
    def expand_border(self, left: int, right: int, bottom: int, top: int, color: Vec4Like) -> None:
        """Expands the image by the indicated number of pixels on each edge.  The new
        pixels are set to the indicated color.

        If any of the values is negative, this actually crops the image.
        """
    def box_filter(self, radius: float = ...) -> None:
        """This flavor of box_filter() will apply the filter over the entire image
        without resizing or copying; the effect is that of a blur operation.
        """
    def gaussian_filter(self, radius: float = ...) -> None:
        """This flavor of gaussian_filter() will apply the filter over the entire
        image without resizing or copying; the effect is that of a blur operation.
        """
    def unfiltered_stretch_from(self, copy: PNMImage) -> None:
        """Resizes from the indicated image into this one by performing a nearest-
        point sample.
        """
    def box_filter_from(self, radius: float, copy: PNMImage) -> None:
        """Makes a resized copy of the indicated image into this one using the
        indicated filter.  The image to be copied is squashed and stretched to
        match the dimensions of the current image, applying the appropriate filter
        to perform the stretching.
        """
    def gaussian_filter_from(self, radius: float, copy: PNMImage) -> None:
        """Makes a resized copy of the indicated image into this one using the
        indicated filter.  The image to be copied is squashed and stretched to
        match the dimensions of the current image, applying the appropriate filter
        to perform the stretching.
        """
    def quick_filter_from(self, copy: PNMImage, xborder: int = ..., yborder: int = ...) -> None:
        """Resizes from the given image, with a fixed radius of 0.5. This is a very
        specialized and simple algorithm that doesn't handle dropping below the
        Nyquist rate very well, but is quite a bit faster than the more general
        box_filter(), above.  If borders are specified, they will further restrict
        the size of the resulting image.  There's no point in using
        quick_box_filter() on a single image.
        """
    def make_histogram(self, hist: PNMImageHeader.Histogram) -> None:
        """Computes a histogram of the colors used in the image."""
    def quantize(self, max_colors: int) -> None:
        """Reduces the number of unique colors in the image to (at most) the given
        count.  Fewer colors than requested may be left in the image after this
        operation, but never more.

        At present, this is only supported on images without an alpha channel.

        @since 1.10.5
        """
    @overload
    def perlin_noise_fill(self, perlin: StackedPerlinNoise2) -> None:
        """`(self, perlin: StackedPerlinNoise2)`:
        Variant of perlin_noise_fill that uses an existing StackedPerlinNoise2
        object.

        `(self, sx: float, sy: float, table_size: int = ..., seed: int = ...)`:
        Fills the image with a grayscale perlin noise pattern based on the
        indicated parameters.  Uses set_xel to set the grayscale values.  The sx
        and sy parameters are in multiples of the size of this image.  See also the
        PerlinNoise2 class in mathutil.
        """
    @overload
    def perlin_noise_fill(self, sx: float, sy: float, table_size: int = ..., seed: int = ...) -> None: ...
    def remix_channels(self, conv: Mat4Like) -> None:
        """Transforms every pixel using the operation (Ro,Go,Bo) =
        conv.xform_point(Ri,Gi,Bi); Input must be a color image.
        """
    def gamma_correct(self, from_gamma: float, to_gamma: float) -> None:
        """Assuming the image was constructed with a gamma curve of from_gamma in the
        RGB channels, converts it to an image with a gamma curve of to_gamma in the
        RGB channels.  Does not affect the alpha channel.
        """
    def gamma_correct_alpha(self, from_gamma: float, to_gamma: float) -> None:
        """Assuming the image was constructed with a gamma curve of from_gamma in the
        alpha channel, converts it to an image with a gamma curve of to_gamma in
        the alpha channel.  Does not affect the RGB channels.
        """
    @overload
    def apply_exponent(self, gray_exponent: float, alpha_exponent: float = ...) -> None:
        """`(self, gray_exponent: float)`; `(self, gray_exponent: float, alpha_exponent: float)`:
        Adjusts each channel of the image by raising the corresponding component
        value to the indicated exponent, such that L' = L ^ exponent.

        `(self, red_exponent: float, green_exponent: float, blue_exponent: float)`; `(self, red_exponent: float, green_exponent: float, blue_exponent: float, alpha_exponent: float)`:
        Adjusts each channel of the image by raising the corresponding component
        value to the indicated exponent, such that L' = L ^ exponent.  For a
        grayscale image, the blue_exponent value is used for the grayscale value,
        and red_exponent and green_exponent are unused.
        """
    @overload
    def apply_exponent(
        self, red_exponent: float, green_exponent: float, blue_exponent: float, alpha_exponent: float = ...
    ) -> None: ...
    def get_average_xel(self) -> LRGBColorf:
        """Returns the average color of all of the pixels in the image."""
    def get_average_xel_a(self) -> LColorf:
        """Returns the average color of all of the pixels in the image, including the
        alpha channel.
        """
    def get_average_gray(self) -> float:
        """Returns the average grayscale component of all of the pixels in the image."""
    def do_fill_distance(self, xi: int, yi: int, d: int) -> None:
        """Recursively fills in the minimum distance measured from a certain set of
        points into the gray channel.
        """
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
    """This class provides a number of convenient methods for painting drawings
    directly into a PNMImage.

    It stores a pointer to the PNMImage you pass it, but it does not take
    ownership of the object; you are responsible for ensuring that the PNMImage
    does not destruct during the lifetime of the PNMPainter object.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    pen: PNMBrush
    fill: PNMBrush
    @overload
    def __init__(self, __param0: PNMPainter) -> None:
        """The constructor stores a pointer to the PNMImage you pass it, but it does
        not take ownership of the object; you are responsible for ensuring that the
        PNMImage does not destruct during the lifetime of the PNMPainter object.

        The xo, yo coordinates specify an optional offset for fill coordinates.  If
        you are painting with a pattern fill, these specify the virtual coordinates
        of the upper-left corner of the image, which can allow you to adjust the
        pattern to line up with nested images, if necessary.
        """
    @overload
    def __init__(self, image: PNMImage, xo: int = ..., yo: int = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_pen(self, pen: PNMBrush) -> None:
        """Specifies a PNMBrush that will be used for drawing lines and edges.  If the
        brush is a bitmap brush, its image will be smeared pixelwise along the
        line.

        Unlike the PNMImage passed to the constructor, the PNMPainter will take
        ownership of the pen.  It is not necessary to keep a separate pointer to
        it.
        """
    def get_pen(self) -> PNMBrush:
        """Returns the current pen.  See set_pen()."""
    def set_fill(self, fill: PNMBrush) -> None:
        """Specifies a PNMBrush that will be used for filling in the interiors of
        objects.  If the brush is a bitmap brush, its image will be tiled
        throughout the space.

        Unlike the PNMImage passed to the constructor, the PNMPainter will take
        ownership of the fill brush.  It is not necessary to keep a separate
        pointer to it.
        """
    def get_fill(self) -> PNMBrush:
        """Returns the current fill brush.  See set_fill()."""
    def draw_point(self, x: float, y: float) -> None:
        """Draws an antialiased point on the PNMImage, using the current pen."""
    def draw_line(self, xa: float, ya: float, xb: float, yb: float) -> None:
        """Draws an antialiased line on the PNMImage, using the current pen."""
    def draw_rectangle(self, xa: float, ya: float, xb: float, yb: float) -> None:
        """Draws a filled rectangule on the PNMImage, using the current pen for the
        outline, and the current fill brush for the interior.

        The two coordinates specify any two diagonally opposite corners.
        """
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
