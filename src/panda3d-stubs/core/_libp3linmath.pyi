from collections.abc import Iterator, Sequence
from typing import Any, ClassVar, Literal, TypeAlias, overload
from panda3d.core import ConfigVariable, Datagram, DatagramIterator, TypeHandle, ostream

_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_Mat4d: TypeAlias = LMatrix4d | UnalignedLMatrix4d
_Mat4f: TypeAlias = LMatrix4f | UnalignedLMatrix4f
_Vec4d: TypeAlias = LVecBase4d | UnalignedLVecBase4d | LMatrix4d.Row | LMatrix4d.CRow
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_Vec3d: TypeAlias = LVecBase3d | LMatrix3d.Row | LMatrix3d.CRow
_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_Vec4i: TypeAlias = LVecBase4i | UnalignedLVecBase4i

class MathNumbers:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: MathNumbers) -> None: ...

class LVecBase2f:
    """This is the base class for all two-component vectors and points."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    x: float
    y: float
    num_components: ClassVar[Literal[2]]
    is_int: ClassVar[Literal[0]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: LVecBase2f) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float) -> None: ...
    @overload
    def __getitem__(self, i: int) -> float: ...
    @overload
    def __getitem__(self, i: int, assign_val: float) -> None: ...
    @staticmethod
    def __len__() -> int: ...
    def __lt__(self, other: LVecBase2f) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __neg__(self) -> LVecBase2f: ...
    def __add__(self, other: LVecBase2f) -> LVecBase2f: ...
    def __sub__(self, other: LVecBase2f) -> LVecBase2f: ...
    def __mul__(self, scalar: float) -> LVecBase2f: ...
    def __truediv__(self, scalar: float) -> LVecBase2f: ...
    def __iadd__(self, other: LVecBase2f) -> LVecBase2f: ...
    def __isub__(self, other: LVecBase2f) -> LVecBase2f: ...
    def __imul__(self, scalar: float) -> LVecBase2f: ...
    def __itruediv__(self, scalar: float) -> LVecBase2f: ...
    def __floordiv__(self, scalar: float) -> LVecBase2f: ...
    def __ifloordiv__(self, scalar: float) -> LVecBase2f: ...
    def __pow__(self, exponent: float) -> LVecBase2f: ...
    def __ipow__(self, exponent: float) -> LVecBase2f: ...
    def __round__(self) -> LVecBase2f: ...
    def __floor__(self) -> LVecBase2f: ...
    def __ceil__(self) -> LVecBase2f: ...
    def __le__(self, other: LVecBase2f) -> bool: ...
    def __iter__(self) -> Iterator[float]: ...
    @overload
    def assign(self, copy: LVecBase2f) -> LVecBase2f: ...
    @overload
    def assign(self, fill_value: float) -> LVecBase2f: ...
    @staticmethod
    def zero() -> LVecBase2f:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVecBase2f:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVecBase2f:
        """Returns a unit Y vector."""
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the vector is not-a-number, false
        otherwise.
        """
        ...
    def get_cell(self, i: int) -> float: ...
    def set_cell(self, i: int, value: float) -> None: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def set_x(self, value: float) -> None: ...
    def set_y(self, value: float) -> None: ...
    def add_to_cell(self, i: int, value: float) -> None:
        """These next functions add to an existing value.  i.e.
        foo.set_x(foo.get_x() + value) These are useful to reduce overhead in
        scripting languages:
        """
        ...
    def add_x(self, value: float) -> None: ...
    def add_y(self, value: float) -> None: ...
    @staticmethod
    def get_num_components() -> int: ...
    def fill(self, fill_value: float) -> None:
        """Sets each element of the vector to the indicated fill_value.  This is
        particularly useful for initializing to zero.
        """
        ...
    def set(self, x: float, y: float) -> None: ...
    def dot(self, other: LVecBase2f) -> float: ...
    def length_squared(self) -> float:
        """Returns the square of the vector's length, cheap and easy."""
        ...
    def length(self) -> float:
        """Returns the length of the vector, by the Pythagorean theorem."""
        ...
    def normalize(self) -> bool:
        """Normalizes the vector in place.  Returns true if the vector was normalized,
        false if it was a zero-length vector.
        """
        ...
    def normalized(self) -> LVecBase2f:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: LVecBase2f) -> LVecBase2f:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    @overload
    def compare_to(self, other: LVecBase2f) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    @overload
    def compare_to(self, other: LVecBase2f, threshold: float) -> int:
        """Sorts vectors lexicographically, componentwise.  Returns a number less than
        0 if this vector sorts before the other one, greater than zero if it sorts
        after, 0 if they are equivalent (within the indicated tolerance).
        """
        ...
    @overload
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def get_hash(self, threshold: float) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    @overload
    def add_hash(self, hash: int, threshold: float) -> int:
        """Adds the vector into the running hash."""
        ...
    def componentwise_mult(self, other: LVecBase2f) -> None: ...
    def fmax(self, other: LVecBase2f) -> LVecBase2f: ...
    def fmin(self, other: LVecBase2f) -> LVecBase2f: ...
    @overload
    def almost_equal(self, other: LVecBase2f) -> bool:
        """Returns true if two vectors are memberwise equal within a default tolerance
        based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: LVecBase2f, threshold: float) -> bool:
        """Returns true if two vectors are memberwise equal within a specified
        tolerance.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the vector, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the vector using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    isNan = is_nan
    getCell = get_cell
    setCell = set_cell
    getX = get_x
    getY = get_y
    setX = set_x
    setY = set_y
    addToCell = add_to_cell
    addX = add_x
    addY = add_y
    getNumComponents = get_num_components
    lengthSquared = length_squared
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    componentwiseMult = componentwise_mult
    Round = __round__
    Floor = __floor__
    Ceil = __ceil__
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type

class LVecBase2d:
    """This is the base class for all two-component vectors and points."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    x: float
    y: float
    num_components: ClassVar[Literal[2]]
    is_int: ClassVar[Literal[0]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: LVecBase2d) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float) -> None: ...
    @overload
    def __getitem__(self, i: int) -> float: ...
    @overload
    def __getitem__(self, i: int, assign_val: float) -> None: ...
    @staticmethod
    def __len__() -> int: ...
    def __lt__(self, other: LVecBase2d) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __neg__(self) -> LVecBase2d: ...
    def __add__(self, other: LVecBase2d) -> LVecBase2d: ...
    def __sub__(self, other: LVecBase2d) -> LVecBase2d: ...
    def __mul__(self, scalar: float) -> LVecBase2d: ...
    def __truediv__(self, scalar: float) -> LVecBase2d: ...
    def __iadd__(self, other: LVecBase2d) -> LVecBase2d: ...
    def __isub__(self, other: LVecBase2d) -> LVecBase2d: ...
    def __imul__(self, scalar: float) -> LVecBase2d: ...
    def __itruediv__(self, scalar: float) -> LVecBase2d: ...
    def __floordiv__(self, scalar: float) -> LVecBase2d: ...
    def __ifloordiv__(self, scalar: float) -> LVecBase2d: ...
    def __pow__(self, exponent: float) -> LVecBase2d: ...
    def __ipow__(self, exponent: float) -> LVecBase2d: ...
    def __round__(self) -> LVecBase2d: ...
    def __floor__(self) -> LVecBase2d: ...
    def __ceil__(self) -> LVecBase2d: ...
    def __le__(self, other: LVecBase2d) -> bool: ...
    def __iter__(self) -> Iterator[float]: ...
    @overload
    def assign(self, copy: LVecBase2d) -> LVecBase2d: ...
    @overload
    def assign(self, fill_value: float) -> LVecBase2d: ...
    @staticmethod
    def zero() -> LVecBase2d:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVecBase2d:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVecBase2d:
        """Returns a unit Y vector."""
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the vector is not-a-number, false
        otherwise.
        """
        ...
    def get_cell(self, i: int) -> float: ...
    def set_cell(self, i: int, value: float) -> None: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def set_x(self, value: float) -> None: ...
    def set_y(self, value: float) -> None: ...
    def add_to_cell(self, i: int, value: float) -> None:
        """These next functions add to an existing value.  i.e.
        foo.set_x(foo.get_x() + value) These are useful to reduce overhead in
        scripting languages:
        """
        ...
    def add_x(self, value: float) -> None: ...
    def add_y(self, value: float) -> None: ...
    @staticmethod
    def get_num_components() -> int: ...
    def fill(self, fill_value: float) -> None:
        """Sets each element of the vector to the indicated fill_value.  This is
        particularly useful for initializing to zero.
        """
        ...
    def set(self, x: float, y: float) -> None: ...
    def dot(self, other: LVecBase2d) -> float: ...
    def length_squared(self) -> float:
        """Returns the square of the vector's length, cheap and easy."""
        ...
    def length(self) -> float:
        """Returns the length of the vector, by the Pythagorean theorem."""
        ...
    def normalize(self) -> bool:
        """Normalizes the vector in place.  Returns true if the vector was normalized,
        false if it was a zero-length vector.
        """
        ...
    def normalized(self) -> LVecBase2d:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: LVecBase2d) -> LVecBase2d:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    @overload
    def compare_to(self, other: LVecBase2d) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    @overload
    def compare_to(self, other: LVecBase2d, threshold: float) -> int:
        """Sorts vectors lexicographically, componentwise.  Returns a number less than
        0 if this vector sorts before the other one, greater than zero if it sorts
        after, 0 if they are equivalent (within the indicated tolerance).
        """
        ...
    @overload
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def get_hash(self, threshold: float) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    @overload
    def add_hash(self, hash: int, threshold: float) -> int:
        """Adds the vector into the running hash."""
        ...
    def componentwise_mult(self, other: LVecBase2d) -> None: ...
    def fmax(self, other: LVecBase2d) -> LVecBase2d: ...
    def fmin(self, other: LVecBase2d) -> LVecBase2d: ...
    @overload
    def almost_equal(self, other: LVecBase2d) -> bool:
        """Returns true if two vectors are memberwise equal within a default tolerance
        based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: LVecBase2d, threshold: float) -> bool:
        """Returns true if two vectors are memberwise equal within a specified
        tolerance.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the vector, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the vector using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    isNan = is_nan
    getCell = get_cell
    setCell = set_cell
    getX = get_x
    getY = get_y
    setX = set_x
    setY = set_y
    addToCell = add_to_cell
    addX = add_x
    addY = add_y
    getNumComponents = get_num_components
    lengthSquared = length_squared
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    componentwiseMult = componentwise_mult
    Round = __round__
    Floor = __floor__
    Ceil = __ceil__
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type

class LVecBase2i:
    """This is the base class for all two-component vectors and points."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    x: int
    y: int
    num_components: ClassVar[Literal[2]]
    is_int: ClassVar[Literal[1]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: LVecBase2i) -> None: ...
    @overload
    def __init__(self, fill_value: int) -> None: ...
    @overload
    def __init__(self, x: int, y: int) -> None: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, i: int, assign_val: int) -> None: ...
    @staticmethod
    def __len__() -> int: ...
    def __lt__(self, other: LVecBase2i) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __neg__(self) -> LVecBase2i: ...
    def __add__(self, other: LVecBase2i) -> LVecBase2i: ...
    def __sub__(self, other: LVecBase2i) -> LVecBase2i: ...
    def __mul__(self, scalar: int) -> LVecBase2i: ...
    def __iadd__(self, other: LVecBase2i) -> LVecBase2i: ...
    def __isub__(self, other: LVecBase2i) -> LVecBase2i: ...
    def __imul__(self, scalar: int) -> LVecBase2i: ...
    def __floordiv__(self, scalar: int) -> LVecBase2i: ...
    def __ifloordiv__(self, scalar: int) -> LVecBase2i: ...
    def __pow__(self, exponent: int) -> LVecBase2i: ...
    def __ipow__(self, exponent: int) -> LVecBase2i: ...
    def __round__(self) -> LVecBase2i: ...
    def __floor__(self) -> LVecBase2i: ...
    def __ceil__(self) -> LVecBase2i: ...
    def __le__(self, other: LVecBase2i) -> bool: ...
    def __iter__(self) -> Iterator[int]: ...
    @overload
    def assign(self, copy: LVecBase2i) -> LVecBase2i: ...
    @overload
    def assign(self, fill_value: int) -> LVecBase2i: ...
    @staticmethod
    def zero() -> LVecBase2i:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVecBase2i:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVecBase2i:
        """Returns a unit Y vector."""
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the vector is not-a-number, false
        otherwise.
        """
        ...
    def get_cell(self, i: int) -> int: ...
    def set_cell(self, i: int, value: int) -> None: ...
    def get_x(self) -> int: ...
    def get_y(self) -> int: ...
    def set_x(self, value: int) -> None: ...
    def set_y(self, value: int) -> None: ...
    def add_to_cell(self, i: int, value: int) -> None:
        """These next functions add to an existing value.  i.e.
        foo.set_x(foo.get_x() + value) These are useful to reduce overhead in
        scripting languages:
        """
        ...
    def add_x(self, value: int) -> None: ...
    def add_y(self, value: int) -> None: ...
    @staticmethod
    def get_num_components() -> int: ...
    def fill(self, fill_value: int) -> None:
        """Sets each element of the vector to the indicated fill_value.  This is
        particularly useful for initializing to zero.
        """
        ...
    def set(self, x: int, y: int) -> None: ...
    def dot(self, other: LVecBase2i) -> int: ...
    def length_squared(self) -> int:
        """Returns the square of the vector's length, cheap and easy."""
        ...
    def compare_to(self, other: LVecBase2i) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    def componentwise_mult(self, other: LVecBase2i) -> None: ...
    def fmax(self, other: LVecBase2i) -> LVecBase2i: ...
    def fmin(self, other: LVecBase2i) -> LVecBase2i: ...
    @overload
    def almost_equal(self, other: LVecBase2i) -> bool:
        """Returns true if two vectors are memberwise equal within a default tolerance
        based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: LVecBase2i, threshold: int) -> bool:
        """Returns true if two vectors are memberwise equal within a specified
        tolerance.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the vector, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the vector using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    isNan = is_nan
    getCell = get_cell
    setCell = set_cell
    getX = get_x
    getY = get_y
    setX = set_x
    setY = set_y
    addToCell = add_to_cell
    addX = add_x
    addY = add_y
    getNumComponents = get_num_components
    lengthSquared = length_squared
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    componentwiseMult = componentwise_mult
    Round = __round__
    Floor = __floor__
    Ceil = __ceil__
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type

class LVector2f(LVecBase2f):
    """This is a two-component vector offset."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2f) -> None:
        """Constructs a new LVector2 from a LVecBase2"""
        ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float) -> None:
        """Constructs a new LVector2 with all components set to the fill value."""
        ...
    def __neg__(self) -> LVector2f: ...
    @overload
    def __add__(self, other: LVector2f) -> LVector2f: ...
    @overload
    def __add__(self, other: LVecBase2f) -> LVecBase2f: ...
    @overload
    def __sub__(self, other: LVector2f) -> LVector2f: ...
    @overload
    def __sub__(self, other: LVecBase2f) -> LVecBase2f: ...
    def __mul__(self, scalar: float) -> LVector2f: ...
    def __truediv__(self, scalar: float) -> LVector2f: ...
    @staticmethod
    def zero() -> LVector2f:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVector2f:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVector2f:
        """Returns a unit Y vector."""
        ...
    def normalized(self) -> LVector2f:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: LVecBase2f) -> LVector2f:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    def signed_angle_rad(self, other: LVecBase2f) -> float:
        """returns the signed angled between two vectors.  normalization is NOT
        necessary
        """
        ...
    def signed_angle_deg(self, other: LVecBase2f) -> float:
        """returns the signed angled between two vectors.  normalization is NOT
        necessary
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    signedAngleRad = signed_angle_rad
    signedAngleDeg = signed_angle_deg
    getClassType = get_class_type

class LVector2d(LVecBase2d):
    """This is a two-component vector offset."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2d) -> None:
        """Constructs a new LVector2 from a LVecBase2"""
        ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float) -> None:
        """Constructs a new LVector2 with all components set to the fill value."""
        ...
    def __neg__(self) -> LVector2d: ...
    @overload
    def __add__(self, other: LVector2d) -> LVector2d: ...
    @overload
    def __add__(self, other: LVecBase2d) -> LVecBase2d: ...
    @overload
    def __sub__(self, other: LVector2d) -> LVector2d: ...
    @overload
    def __sub__(self, other: LVecBase2d) -> LVecBase2d: ...
    def __mul__(self, scalar: float) -> LVector2d: ...
    def __truediv__(self, scalar: float) -> LVector2d: ...
    @staticmethod
    def zero() -> LVector2d:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVector2d:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVector2d:
        """Returns a unit Y vector."""
        ...
    def normalized(self) -> LVector2d:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: LVecBase2d) -> LVector2d:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    def signed_angle_rad(self, other: LVecBase2d) -> float:
        """returns the signed angled between two vectors.  normalization is NOT
        necessary
        """
        ...
    def signed_angle_deg(self, other: LVecBase2d) -> float:
        """returns the signed angled between two vectors.  normalization is NOT
        necessary
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    signedAngleRad = signed_angle_rad
    signedAngleDeg = signed_angle_deg
    getClassType = get_class_type

class LVector2i(LVecBase2i):
    """This is a two-component vector offset."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2i) -> None:
        """Constructs a new LVector2 from a LVecBase2"""
        ...
    @overload
    def __init__(self, fill_value: int) -> None: ...
    @overload
    def __init__(self, x: int, y: int) -> None:
        """Constructs a new LVector2 with all components set to the fill value."""
        ...
    def __neg__(self) -> LVector2i: ...
    @overload
    def __add__(self, other: LVector2i) -> LVector2i: ...
    @overload
    def __add__(self, other: LVecBase2i) -> LVecBase2i: ...
    @overload
    def __sub__(self, other: LVector2i) -> LVector2i: ...
    @overload
    def __sub__(self, other: LVecBase2i) -> LVecBase2i: ...
    def __mul__(self, scalar: int) -> LVector2i: ...
    @staticmethod
    def zero() -> LVector2i:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVector2i:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVector2i:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    getClassType = get_class_type

class LPoint2f(LVecBase2f):
    """This is a two-component point in space."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2f) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None:
        """Constructs a new LPoint2 from a LVecBase2"""
        ...
    @overload
    def __init__(self, x: float, y: float) -> None:
        """Constructs a new LPoint2 all components set to the fill value."""
        ...
    def __neg__(self) -> LPoint2f: ...
    @overload
    def __add__(self, other: LVector2f) -> LPoint2f: ...
    @overload
    def __add__(self, other: LVecBase2f) -> LVecBase2f: ...
    @overload
    def __sub__(self, other: LPoint2f) -> LVector2f: ...
    @overload
    def __sub__(self, other: LVector2f) -> LPoint2f: ...
    @overload
    def __sub__(self, other: LVecBase2f) -> LVecBase2f: ...
    def __mul__(self, scalar: float) -> LPoint2f: ...
    def __truediv__(self, scalar: float) -> LPoint2f: ...
    @staticmethod
    def zero() -> LPoint2f:
        """Returns a zero-length point."""
        ...
    @staticmethod
    def unit_x() -> LPoint2f:
        """Returns a unit X point."""
        ...
    @staticmethod
    def unit_y() -> LPoint2f:
        """Returns a unit Y point."""
        ...
    def normalized(self) -> LPoint2f:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: LVecBase2f) -> LPoint2f:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    getClassType = get_class_type

class LPoint2d(LVecBase2d):
    """This is a two-component point in space."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2d) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None:
        """Constructs a new LPoint2 from a LVecBase2"""
        ...
    @overload
    def __init__(self, x: float, y: float) -> None:
        """Constructs a new LPoint2 all components set to the fill value."""
        ...
    def __neg__(self) -> LPoint2d: ...
    @overload
    def __add__(self, other: LVector2d) -> LPoint2d: ...
    @overload
    def __add__(self, other: LVecBase2d) -> LVecBase2d: ...
    @overload
    def __sub__(self, other: LPoint2d) -> LVector2d: ...
    @overload
    def __sub__(self, other: LVector2d) -> LPoint2d: ...
    @overload
    def __sub__(self, other: LVecBase2d) -> LVecBase2d: ...
    def __mul__(self, scalar: float) -> LPoint2d: ...
    def __truediv__(self, scalar: float) -> LPoint2d: ...
    @staticmethod
    def zero() -> LPoint2d:
        """Returns a zero-length point."""
        ...
    @staticmethod
    def unit_x() -> LPoint2d:
        """Returns a unit X point."""
        ...
    @staticmethod
    def unit_y() -> LPoint2d:
        """Returns a unit Y point."""
        ...
    def normalized(self) -> LPoint2d:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: LVecBase2d) -> LPoint2d:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    getClassType = get_class_type

class LPoint2i(LVecBase2i):
    """This is a two-component point in space."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2i) -> None: ...
    @overload
    def __init__(self, fill_value: int) -> None:
        """Constructs a new LPoint2 from a LVecBase2"""
        ...
    @overload
    def __init__(self, x: int, y: int) -> None:
        """Constructs a new LPoint2 all components set to the fill value."""
        ...
    def __neg__(self) -> LPoint2i: ...
    @overload
    def __add__(self, other: LVector2i) -> LPoint2i: ...
    @overload
    def __add__(self, other: LVecBase2i) -> LVecBase2i: ...
    @overload
    def __sub__(self, other: LPoint2i) -> LVector2i: ...
    @overload
    def __sub__(self, other: LVector2i) -> LPoint2i: ...
    @overload
    def __sub__(self, other: LVecBase2i) -> LVecBase2i: ...
    def __mul__(self, scalar: int) -> LPoint2i: ...
    @staticmethod
    def zero() -> LPoint2i:
        """Returns a zero-length point."""
        ...
    @staticmethod
    def unit_x() -> LPoint2i:
        """Returns a unit X point."""
        ...
    @staticmethod
    def unit_y() -> LPoint2i:
        """Returns a unit Y point."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    getClassType = get_class_type

class LVecBase3f:
    """This is the base class for all three-component vectors and points."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    x: float
    y: float
    z: float
    num_components: ClassVar[Literal[3]]
    is_int: ClassVar[Literal[0]]
    @property
    def xy(self) -> LVecBase2f: ...
    @property
    def xz(self) -> LVecBase2f: ...
    @property
    def yz(self) -> LVecBase2f: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: _Vec3f) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2f, z: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float) -> None: ...
    @overload
    def __getitem__(self, i: int) -> float: ...
    @overload
    def __getitem__(self, i: int, assign_val: float) -> None: ...
    @staticmethod
    def __len__() -> int: ...
    def __lt__(self, other: _Vec3f) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __neg__(self) -> LVecBase3f: ...
    def __add__(self, other: _Vec3f) -> LVecBase3f: ...
    def __sub__(self, other: _Vec3f) -> LVecBase3f: ...
    def __mul__(self, scalar: float) -> LVecBase3f: ...
    def __truediv__(self, scalar: float) -> LVecBase3f: ...
    def __iadd__(self, other: _Vec3f) -> LVecBase3f: ...
    def __isub__(self, other: _Vec3f) -> LVecBase3f: ...
    def __imul__(self, scalar: float) -> LVecBase3f: ...
    def __itruediv__(self, scalar: float) -> LVecBase3f: ...
    def __floordiv__(self, scalar: float) -> LVecBase3f: ...
    def __ifloordiv__(self, scalar: float) -> LVecBase3f: ...
    def __pow__(self, exponent: float) -> LVecBase3f: ...
    def __ipow__(self, exponent: float) -> LVecBase3f: ...
    def __round__(self) -> LVecBase3f: ...
    def __floor__(self) -> LVecBase3f: ...
    def __ceil__(self) -> LVecBase3f: ...
    def __le__(self, other: _Vec3f) -> bool: ...
    def __iter__(self) -> Iterator[float]: ...
    @overload
    def assign(self, copy: _Vec3f) -> LVecBase3f: ...
    @overload
    def assign(self, fill_value: float) -> LVecBase3f: ...
    @staticmethod
    def zero() -> LVecBase3f:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVecBase3f:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVecBase3f:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def unit_z() -> LVecBase3f:
        """Returns a unit Z vector."""
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the vector is not-a-number, false
        otherwise.
        """
        ...
    def get_cell(self, i: int) -> float: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def get_z(self) -> float: ...
    def set_cell(self, i: int, value: float) -> None: ...
    def set_x(self, value: float) -> None: ...
    def set_y(self, value: float) -> None: ...
    def set_z(self, value: float) -> None: ...
    def get_xy(self) -> LVecBase2f:
        """Returns a 2-component vector that shares just the first two components of
        this vector.
        """
        ...
    def get_xz(self) -> LVecBase2f:
        """Returns a 2-component vector that shares just the first and last components
        of this vector.
        """
        ...
    def get_yz(self) -> LVecBase2f:
        """Returns a 2-component vector that shares just the last two components of
        this vector.
        """
        ...
    def add_to_cell(self, i: int, value: float) -> None:
        """These next functions add to an existing value.  i.e.
        foo.set_x(foo.get_x() + value) These are useful to reduce overhead in
        scripting languages:
        """
        ...
    def add_x(self, value: float) -> None: ...
    def add_y(self, value: float) -> None: ...
    def add_z(self, value: float) -> None: ...
    @staticmethod
    def get_num_components() -> int: ...
    def fill(self, fill_value: float) -> None:
        """Sets each element of the vector to the indicated fill_value.  This is
        particularly useful for initializing to zero.
        """
        ...
    def set(self, x: float, y: float, z: float) -> None: ...
    def dot(self, other: _Vec3f) -> float: ...
    def length_squared(self) -> float:
        """Returns the square of the vector's length, cheap and easy."""
        ...
    def length(self) -> float:
        """Returns the length of the vector, by the Pythagorean theorem."""
        ...
    def normalize(self) -> bool:
        """Normalizes the vector in place.  Returns true if the vector was normalized,
        false if it was a zero-length vector.
        """
        ...
    def normalized(self) -> LVecBase3f:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: _Vec3f) -> LVecBase3f:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    def cross(self, other: _Vec3f) -> LVecBase3f: ...
    def get_standardized_hpr(self) -> LVecBase3f:
        """Try to un-spin the hpr to a standard form.  Like all standards, someone
        decides between many arbitrary possible standards.  This function assumes
        that 0 and 360 are the same, as is 720 and -360.  Also 180 and -180 are the
        same.  Another example is -90 and 270. Each element will be in the range
        -180.0 to 179.99999. The original usage of this function is for human
        readable output.
        
        It doesn't work so well for asserting that foo_hpr is roughly equal to
        bar_hpr.  Try using LQuaternionf::is_same_direction() for that.  See Also:
        get_standardized_rotation, LQuaternion::is_same_direction
        """
        ...
    @overload
    def compare_to(self, other: _Vec3f) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    @overload
    def compare_to(self, other: _Vec3f, threshold: float) -> int:
        """Sorts vectors lexicographically, componentwise.  Returns a number less than
        0 if this vector sorts before the other one, greater than zero if it sorts
        after, 0 if they are equivalent (within the indicated tolerance).
        """
        ...
    @overload
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def get_hash(self, threshold: float) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    @overload
    def add_hash(self, hash: int, threshold: float) -> int:
        """Adds the vector into the running hash."""
        ...
    def componentwise_mult(self, other: _Vec3f) -> None: ...
    def fmax(self, other: _Vec3f) -> LVecBase3f: ...
    def fmin(self, other: _Vec3f) -> LVecBase3f: ...
    def cross_into(self, other: _Vec3f) -> None: ...
    @overload
    def almost_equal(self, other: _Vec3f) -> bool:
        """Returns true if two vectors are memberwise equal within a default tolerance
        based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: _Vec3f, threshold: float) -> bool:
        """Returns true if two vectors are memberwise equal within a specified
        tolerance.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the vector, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the vector using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    isNan = is_nan
    getCell = get_cell
    getX = get_x
    getY = get_y
    getZ = get_z
    setCell = set_cell
    setX = set_x
    setY = set_y
    setZ = set_z
    getXy = get_xy
    getXz = get_xz
    getYz = get_yz
    addToCell = add_to_cell
    addX = add_x
    addY = add_y
    addZ = add_z
    getNumComponents = get_num_components
    lengthSquared = length_squared
    getStandardizedHpr = get_standardized_hpr
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    componentwiseMult = componentwise_mult
    Round = __round__
    Floor = __floor__
    Ceil = __ceil__
    crossInto = cross_into
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type

class LVecBase3d:
    """This is the base class for all three-component vectors and points."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    x: float
    y: float
    z: float
    num_components: ClassVar[Literal[3]]
    is_int: ClassVar[Literal[0]]
    @property
    def xy(self) -> LVecBase2d: ...
    @property
    def xz(self) -> LVecBase2d: ...
    @property
    def yz(self) -> LVecBase2d: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: _Vec3d) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2d, z: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float) -> None: ...
    @overload
    def __getitem__(self, i: int) -> float: ...
    @overload
    def __getitem__(self, i: int, assign_val: float) -> None: ...
    @staticmethod
    def __len__() -> int: ...
    def __lt__(self, other: _Vec3d) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __neg__(self) -> LVecBase3d: ...
    def __add__(self, other: _Vec3d) -> LVecBase3d: ...
    def __sub__(self, other: _Vec3d) -> LVecBase3d: ...
    def __mul__(self, scalar: float) -> LVecBase3d: ...
    def __truediv__(self, scalar: float) -> LVecBase3d: ...
    def __iadd__(self, other: _Vec3d) -> LVecBase3d: ...
    def __isub__(self, other: _Vec3d) -> LVecBase3d: ...
    def __imul__(self, scalar: float) -> LVecBase3d: ...
    def __itruediv__(self, scalar: float) -> LVecBase3d: ...
    def __floordiv__(self, scalar: float) -> LVecBase3d: ...
    def __ifloordiv__(self, scalar: float) -> LVecBase3d: ...
    def __pow__(self, exponent: float) -> LVecBase3d: ...
    def __ipow__(self, exponent: float) -> LVecBase3d: ...
    def __round__(self) -> LVecBase3d: ...
    def __floor__(self) -> LVecBase3d: ...
    def __ceil__(self) -> LVecBase3d: ...
    def __le__(self, other: _Vec3d) -> bool: ...
    def __iter__(self) -> Iterator[float]: ...
    @overload
    def assign(self, copy: _Vec3d) -> LVecBase3d: ...
    @overload
    def assign(self, fill_value: float) -> LVecBase3d: ...
    @staticmethod
    def zero() -> LVecBase3d:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVecBase3d:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVecBase3d:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def unit_z() -> LVecBase3d:
        """Returns a unit Z vector."""
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the vector is not-a-number, false
        otherwise.
        """
        ...
    def get_cell(self, i: int) -> float: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def get_z(self) -> float: ...
    def set_cell(self, i: int, value: float) -> None: ...
    def set_x(self, value: float) -> None: ...
    def set_y(self, value: float) -> None: ...
    def set_z(self, value: float) -> None: ...
    def get_xy(self) -> LVecBase2d:
        """Returns a 2-component vector that shares just the first two components of
        this vector.
        """
        ...
    def get_xz(self) -> LVecBase2d:
        """Returns a 2-component vector that shares just the first and last components
        of this vector.
        """
        ...
    def get_yz(self) -> LVecBase2d:
        """Returns a 2-component vector that shares just the last two components of
        this vector.
        """
        ...
    def add_to_cell(self, i: int, value: float) -> None:
        """These next functions add to an existing value.  i.e.
        foo.set_x(foo.get_x() + value) These are useful to reduce overhead in
        scripting languages:
        """
        ...
    def add_x(self, value: float) -> None: ...
    def add_y(self, value: float) -> None: ...
    def add_z(self, value: float) -> None: ...
    @staticmethod
    def get_num_components() -> int: ...
    def fill(self, fill_value: float) -> None:
        """Sets each element of the vector to the indicated fill_value.  This is
        particularly useful for initializing to zero.
        """
        ...
    def set(self, x: float, y: float, z: float) -> None: ...
    def dot(self, other: _Vec3d) -> float: ...
    def length_squared(self) -> float:
        """Returns the square of the vector's length, cheap and easy."""
        ...
    def length(self) -> float:
        """Returns the length of the vector, by the Pythagorean theorem."""
        ...
    def normalize(self) -> bool:
        """Normalizes the vector in place.  Returns true if the vector was normalized,
        false if it was a zero-length vector.
        """
        ...
    def normalized(self) -> LVecBase3d:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: _Vec3d) -> LVecBase3d:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    def cross(self, other: _Vec3d) -> LVecBase3d: ...
    def get_standardized_hpr(self) -> LVecBase3d:
        """Try to un-spin the hpr to a standard form.  Like all standards, someone
        decides between many arbitrary possible standards.  This function assumes
        that 0 and 360 are the same, as is 720 and -360.  Also 180 and -180 are the
        same.  Another example is -90 and 270. Each element will be in the range
        -180.0 to 179.99999. The original usage of this function is for human
        readable output.
        
        It doesn't work so well for asserting that foo_hpr is roughly equal to
        bar_hpr.  Try using LQuaternionf::is_same_direction() for that.  See Also:
        get_standardized_rotation, LQuaternion::is_same_direction
        """
        ...
    @overload
    def compare_to(self, other: _Vec3d) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    @overload
    def compare_to(self, other: _Vec3d, threshold: float) -> int:
        """Sorts vectors lexicographically, componentwise.  Returns a number less than
        0 if this vector sorts before the other one, greater than zero if it sorts
        after, 0 if they are equivalent (within the indicated tolerance).
        """
        ...
    @overload
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def get_hash(self, threshold: float) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    @overload
    def add_hash(self, hash: int, threshold: float) -> int:
        """Adds the vector into the running hash."""
        ...
    def componentwise_mult(self, other: _Vec3d) -> None: ...
    def fmax(self, other: _Vec3d) -> LVecBase3d: ...
    def fmin(self, other: _Vec3d) -> LVecBase3d: ...
    def cross_into(self, other: _Vec3d) -> None: ...
    @overload
    def almost_equal(self, other: _Vec3d) -> bool:
        """Returns true if two vectors are memberwise equal within a default tolerance
        based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: _Vec3d, threshold: float) -> bool:
        """Returns true if two vectors are memberwise equal within a specified
        tolerance.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the vector, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the vector using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    isNan = is_nan
    getCell = get_cell
    getX = get_x
    getY = get_y
    getZ = get_z
    setCell = set_cell
    setX = set_x
    setY = set_y
    setZ = set_z
    getXy = get_xy
    getXz = get_xz
    getYz = get_yz
    addToCell = add_to_cell
    addX = add_x
    addY = add_y
    addZ = add_z
    getNumComponents = get_num_components
    lengthSquared = length_squared
    getStandardizedHpr = get_standardized_hpr
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    componentwiseMult = componentwise_mult
    Round = __round__
    Floor = __floor__
    Ceil = __ceil__
    crossInto = cross_into
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type

class LVecBase3i:
    """This is the base class for all three-component vectors and points."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    x: int
    y: int
    z: int
    num_components: ClassVar[Literal[3]]
    is_int: ClassVar[Literal[1]]
    @property
    def xy(self) -> LVecBase2i: ...
    @property
    def xz(self) -> LVecBase2i: ...
    @property
    def yz(self) -> LVecBase2i: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: LVecBase3i) -> None: ...
    @overload
    def __init__(self, fill_value: int) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2i, z: int) -> None: ...
    @overload
    def __init__(self, x: int, y: int, z: int) -> None: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, i: int, assign_val: int) -> None: ...
    @staticmethod
    def __len__() -> int: ...
    def __lt__(self, other: LVecBase3i) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __neg__(self) -> LVecBase3i: ...
    def __add__(self, other: LVecBase3i) -> LVecBase3i: ...
    def __sub__(self, other: LVecBase3i) -> LVecBase3i: ...
    def __mul__(self, scalar: int) -> LVecBase3i: ...
    def __iadd__(self, other: LVecBase3i) -> LVecBase3i: ...
    def __isub__(self, other: LVecBase3i) -> LVecBase3i: ...
    def __imul__(self, scalar: int) -> LVecBase3i: ...
    def __floordiv__(self, scalar: int) -> LVecBase3i: ...
    def __ifloordiv__(self, scalar: int) -> LVecBase3i: ...
    def __pow__(self, exponent: int) -> LVecBase3i: ...
    def __ipow__(self, exponent: int) -> LVecBase3i: ...
    def __round__(self) -> LVecBase3i: ...
    def __floor__(self) -> LVecBase3i: ...
    def __ceil__(self) -> LVecBase3i: ...
    def __le__(self, other: LVecBase3i) -> bool: ...
    def __iter__(self) -> Iterator[int]: ...
    @overload
    def assign(self, copy: LVecBase3i) -> LVecBase3i: ...
    @overload
    def assign(self, fill_value: int) -> LVecBase3i: ...
    @staticmethod
    def zero() -> LVecBase3i:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVecBase3i:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVecBase3i:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def unit_z() -> LVecBase3i:
        """Returns a unit Z vector."""
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the vector is not-a-number, false
        otherwise.
        """
        ...
    def get_cell(self, i: int) -> int: ...
    def get_x(self) -> int: ...
    def get_y(self) -> int: ...
    def get_z(self) -> int: ...
    def set_cell(self, i: int, value: int) -> None: ...
    def set_x(self, value: int) -> None: ...
    def set_y(self, value: int) -> None: ...
    def set_z(self, value: int) -> None: ...
    def get_xy(self) -> LVecBase2i:
        """Returns a 2-component vector that shares just the first two components of
        this vector.
        """
        ...
    def get_xz(self) -> LVecBase2i:
        """Returns a 2-component vector that shares just the first and last components
        of this vector.
        """
        ...
    def get_yz(self) -> LVecBase2i:
        """Returns a 2-component vector that shares just the last two components of
        this vector.
        """
        ...
    def add_to_cell(self, i: int, value: int) -> None:
        """These next functions add to an existing value.  i.e.
        foo.set_x(foo.get_x() + value) These are useful to reduce overhead in
        scripting languages:
        """
        ...
    def add_x(self, value: int) -> None: ...
    def add_y(self, value: int) -> None: ...
    def add_z(self, value: int) -> None: ...
    @staticmethod
    def get_num_components() -> int: ...
    def fill(self, fill_value: int) -> None:
        """Sets each element of the vector to the indicated fill_value.  This is
        particularly useful for initializing to zero.
        """
        ...
    def set(self, x: int, y: int, z: int) -> None: ...
    def dot(self, other: LVecBase3i) -> int: ...
    def length_squared(self) -> int:
        """Returns the square of the vector's length, cheap and easy."""
        ...
    def cross(self, other: LVecBase3i) -> LVecBase3i: ...
    def compare_to(self, other: LVecBase3i) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    def componentwise_mult(self, other: LVecBase3i) -> None: ...
    def fmax(self, other: LVecBase3i) -> LVecBase3i: ...
    def fmin(self, other: LVecBase3i) -> LVecBase3i: ...
    def cross_into(self, other: LVecBase3i) -> None: ...
    @overload
    def almost_equal(self, other: LVecBase3i) -> bool:
        """Returns true if two vectors are memberwise equal within a default tolerance
        based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: LVecBase3i, threshold: int) -> bool:
        """Returns true if two vectors are memberwise equal within a specified
        tolerance.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the vector, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the vector using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    isNan = is_nan
    getCell = get_cell
    getX = get_x
    getY = get_y
    getZ = get_z
    setCell = set_cell
    setX = set_x
    setY = set_y
    setZ = set_z
    getXy = get_xy
    getXz = get_xz
    getYz = get_yz
    addToCell = add_to_cell
    addX = add_x
    addY = add_y
    addZ = add_z
    getNumComponents = get_num_components
    lengthSquared = length_squared
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    componentwiseMult = componentwise_mult
    Round = __round__
    Floor = __floor__
    Ceil = __ceil__
    crossInto = cross_into
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type

class LVector3f(LVecBase3f):
    """This is a three-component vector distance (as opposed to a three-component
    point, which represents a particular point in space).  Some of the methods
    are slightly different between LPoint3 and LVector3; in particular,
    subtraction of two points yields a vector, while addition of a vector and a
    point yields a point.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def xy(self) -> LVector2f: ...
    @property
    def xz(self) -> LVector2f: ...
    @property
    def yz(self) -> LVector2f: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec3f) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2f, z: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float) -> None: ...
    def __neg__(self) -> LVector3f: ...
    @overload
    def __add__(self, other: LVector3f) -> LVector3f: ...
    @overload
    def __add__(self, other: _Vec3f) -> LVecBase3f: ...
    @overload
    def __sub__(self, other: LVector3f) -> LVector3f: ...
    @overload
    def __sub__(self, other: _Vec3f) -> LVecBase3f: ...
    def __mul__(self, scalar: float) -> LVector3f: ...
    def __truediv__(self, scalar: float) -> LVector3f: ...
    @staticmethod
    def zero() -> LVector3f:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVector3f:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVector3f:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def unit_z() -> LVector3f:
        """Returns a unit Z vector."""
        ...
    def get_xy(self) -> LVector2f:
        """Returns a 2-component vector that shares just the first two components of
        this vector.
        """
        ...
    def get_xz(self) -> LVector2f:
        """Returns a 2-component vector that shares just the first and last components
        of this vector.
        """
        ...
    def get_yz(self) -> LVector2f:
        """Returns a 2-component vector that shares just the last two components of
        this vector.
        """
        ...
    def cross(self, other: _Vec3f) -> LVector3f: ...
    def normalized(self) -> LVector3f:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: _Vec3f) -> LVector3f:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    def angle_rad(self, other: _Vec3f) -> float:
        """Returns the unsigned angle between this vector and the other one, expressed
        in radians.  Both vectors should be initially normalized.
        """
        ...
    def angle_deg(self, other: _Vec3f) -> float:
        """Returns the angle between this vector and the other one, expressed in
        degrees.  Both vectors should be initially normalized.
        """
        ...
    def signed_angle_rad(self, other: _Vec3f, ref: _Vec3f) -> float:
        """returns the signed angle between two vectors.  The angle is positive if the
        rotation from this vector to other is clockwise when looking in the
        direction of the ref vector.
        
        Vectors (except the ref vector) should be initially normalized.
        """
        ...
    def signed_angle_deg(self, other: _Vec3f, ref: _Vec3f) -> float:
        """Returns the signed angle between two vectors.  The angle is positive if the
        rotation from this vector to other is clockwise when looking in the
        direction of the ref vector.
        
        Vectors (except the ref vector) should be initially normalized.
        """
        ...
    def relative_angle_rad(self, other: _Vec3f) -> float:
        """@deprecated Do not use."""
        ...
    def relative_angle_deg(self, other: _Vec3f) -> float:
        """@deprecated Do not use."""
        ...
    @staticmethod
    def up(cs: _CoordinateSystem = ...) -> LVector3f:
        """Returns the up vector for the given coordinate system."""
        ...
    @staticmethod
    def right(cs: _CoordinateSystem = ...) -> LVector3f:
        """Returns the right vector for the given coordinate system."""
        ...
    @staticmethod
    def forward(cs: _CoordinateSystem = ...) -> LVector3f:
        """Returns the forward vector for the given coordinate system."""
        ...
    @staticmethod
    def down(cs: _CoordinateSystem = ...) -> LVector3f:
        """Returns the down vector for the given coordinate system."""
        ...
    @staticmethod
    def left(cs: _CoordinateSystem = ...) -> LVector3f:
        """Returns the left vector for the given coordinate system."""
        ...
    @staticmethod
    def back(cs: _CoordinateSystem = ...) -> LVector3f:
        """Returns the back vector for the given coordinate system."""
        ...
    @staticmethod
    def rfu(right: float, fwd: float, up: float, cs: _CoordinateSystem = ...) -> LVector3f:
        """Returns a vector that is described by its right, forward, and up
        components, in whatever way the coordinate system represents that vector.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    getXy = get_xy
    getXz = get_xz
    getYz = get_yz
    angleRad = angle_rad
    angleDeg = angle_deg
    signedAngleRad = signed_angle_rad
    signedAngleDeg = signed_angle_deg
    relativeAngleRad = relative_angle_rad
    relativeAngleDeg = relative_angle_deg
    getClassType = get_class_type

class LVector3d(LVecBase3d):
    """This is a three-component vector distance (as opposed to a three-component
    point, which represents a particular point in space).  Some of the methods
    are slightly different between LPoint3 and LVector3; in particular,
    subtraction of two points yields a vector, while addition of a vector and a
    point yields a point.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def xy(self) -> LVector2d: ...
    @property
    def xz(self) -> LVector2d: ...
    @property
    def yz(self) -> LVector2d: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec3d) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2d, z: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float) -> None: ...
    def __neg__(self) -> LVector3d: ...
    @overload
    def __add__(self, other: LVector3d) -> LVector3d: ...
    @overload
    def __add__(self, other: _Vec3d) -> LVecBase3d: ...
    @overload
    def __sub__(self, other: LVector3d) -> LVector3d: ...
    @overload
    def __sub__(self, other: _Vec3d) -> LVecBase3d: ...
    def __mul__(self, scalar: float) -> LVector3d: ...
    def __truediv__(self, scalar: float) -> LVector3d: ...
    @staticmethod
    def zero() -> LVector3d:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVector3d:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVector3d:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def unit_z() -> LVector3d:
        """Returns a unit Z vector."""
        ...
    def get_xy(self) -> LVector2d:
        """Returns a 2-component vector that shares just the first two components of
        this vector.
        """
        ...
    def get_xz(self) -> LVector2d:
        """Returns a 2-component vector that shares just the first and last components
        of this vector.
        """
        ...
    def get_yz(self) -> LVector2d:
        """Returns a 2-component vector that shares just the last two components of
        this vector.
        """
        ...
    def cross(self, other: _Vec3d) -> LVector3d: ...
    def normalized(self) -> LVector3d:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: _Vec3d) -> LVector3d:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    def angle_rad(self, other: _Vec3d) -> float:
        """Returns the unsigned angle between this vector and the other one, expressed
        in radians.  Both vectors should be initially normalized.
        """
        ...
    def angle_deg(self, other: _Vec3d) -> float:
        """Returns the angle between this vector and the other one, expressed in
        degrees.  Both vectors should be initially normalized.
        """
        ...
    def signed_angle_rad(self, other: _Vec3d, ref: _Vec3d) -> float:
        """returns the signed angle between two vectors.  The angle is positive if the
        rotation from this vector to other is clockwise when looking in the
        direction of the ref vector.
        
        Vectors (except the ref vector) should be initially normalized.
        """
        ...
    def signed_angle_deg(self, other: _Vec3d, ref: _Vec3d) -> float:
        """Returns the signed angle between two vectors.  The angle is positive if the
        rotation from this vector to other is clockwise when looking in the
        direction of the ref vector.
        
        Vectors (except the ref vector) should be initially normalized.
        """
        ...
    def relative_angle_rad(self, other: _Vec3d) -> float:
        """@deprecated Do not use."""
        ...
    def relative_angle_deg(self, other: _Vec3d) -> float:
        """@deprecated Do not use."""
        ...
    @staticmethod
    def up(cs: _CoordinateSystem = ...) -> LVector3d:
        """Returns the up vector for the given coordinate system."""
        ...
    @staticmethod
    def right(cs: _CoordinateSystem = ...) -> LVector3d:
        """Returns the right vector for the given coordinate system."""
        ...
    @staticmethod
    def forward(cs: _CoordinateSystem = ...) -> LVector3d:
        """Returns the forward vector for the given coordinate system."""
        ...
    @staticmethod
    def down(cs: _CoordinateSystem = ...) -> LVector3d:
        """Returns the down vector for the given coordinate system."""
        ...
    @staticmethod
    def left(cs: _CoordinateSystem = ...) -> LVector3d:
        """Returns the left vector for the given coordinate system."""
        ...
    @staticmethod
    def back(cs: _CoordinateSystem = ...) -> LVector3d:
        """Returns the back vector for the given coordinate system."""
        ...
    @staticmethod
    def rfu(right: float, fwd: float, up: float, cs: _CoordinateSystem = ...) -> LVector3d:
        """Returns a vector that is described by its right, forward, and up
        components, in whatever way the coordinate system represents that vector.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    getXy = get_xy
    getXz = get_xz
    getYz = get_yz
    angleRad = angle_rad
    angleDeg = angle_deg
    signedAngleRad = signed_angle_rad
    signedAngleDeg = signed_angle_deg
    relativeAngleRad = relative_angle_rad
    relativeAngleDeg = relative_angle_deg
    getClassType = get_class_type

class LVector3i(LVecBase3i):
    """This is a three-component vector distance (as opposed to a three-component
    point, which represents a particular point in space).  Some of the methods
    are slightly different between LPoint3 and LVector3; in particular,
    subtraction of two points yields a vector, while addition of a vector and a
    point yields a point.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def xy(self) -> LVector2i: ...
    @property
    def xz(self) -> LVector2i: ...
    @property
    def yz(self) -> LVector2i: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: LVecBase3i) -> None: ...
    @overload
    def __init__(self, fill_value: int) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2i, z: int) -> None: ...
    @overload
    def __init__(self, x: int, y: int, z: int) -> None: ...
    def __neg__(self) -> LVector3i: ...
    @overload
    def __add__(self, other: LVector3i) -> LVector3i: ...
    @overload
    def __add__(self, other: LVecBase3i) -> LVecBase3i: ...
    @overload
    def __sub__(self, other: LVector3i) -> LVector3i: ...
    @overload
    def __sub__(self, other: LVecBase3i) -> LVecBase3i: ...
    def __mul__(self, scalar: int) -> LVector3i: ...
    @staticmethod
    def zero() -> LVector3i:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVector3i:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVector3i:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def unit_z() -> LVector3i:
        """Returns a unit Z vector."""
        ...
    def get_xy(self) -> LVector2i:
        """Returns a 2-component vector that shares just the first two components of
        this vector.
        """
        ...
    def get_xz(self) -> LVector2i:
        """Returns a 2-component vector that shares just the first and last components
        of this vector.
        """
        ...
    def get_yz(self) -> LVector2i:
        """Returns a 2-component vector that shares just the last two components of
        this vector.
        """
        ...
    def cross(self, other: LVecBase3i) -> LVector3i: ...
    @staticmethod
    def up(cs: _CoordinateSystem = ...) -> LVector3i:
        """Returns the up vector for the given coordinate system."""
        ...
    @staticmethod
    def right(cs: _CoordinateSystem = ...) -> LVector3i:
        """Returns the right vector for the given coordinate system."""
        ...
    @staticmethod
    def forward(cs: _CoordinateSystem = ...) -> LVector3i:
        """Returns the forward vector for the given coordinate system."""
        ...
    @staticmethod
    def down(cs: _CoordinateSystem = ...) -> LVector3i:
        """Returns the down vector for the given coordinate system."""
        ...
    @staticmethod
    def left(cs: _CoordinateSystem = ...) -> LVector3i:
        """Returns the left vector for the given coordinate system."""
        ...
    @staticmethod
    def back(cs: _CoordinateSystem = ...) -> LVector3i:
        """Returns the back vector for the given coordinate system."""
        ...
    @staticmethod
    def rfu(right: int, fwd: int, up: int, cs: _CoordinateSystem = ...) -> LVector3i:
        """Returns a vector that is described by its right, forward, and up
        components, in whatever way the coordinate system represents that vector.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    getXy = get_xy
    getXz = get_xz
    getYz = get_yz
    getClassType = get_class_type

class LPoint3f(LVecBase3f):
    """This is a three-component point in space (as opposed to a three-component
    vector, which represents a direction and a distance).  Some of the methods
    are slightly different between LPoint3 and LVector3; in particular,
    subtraction of two points yields a vector, while addition of a vector and a
    point yields a point.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def xy(self) -> LPoint2f: ...
    @property
    def xz(self) -> LPoint2f: ...
    @property
    def yz(self) -> LPoint2f: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec3f) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2f, z: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float) -> None: ...
    def __neg__(self) -> LPoint3f: ...
    @overload
    def __add__(self, other: LVector3f) -> LPoint3f: ...
    @overload
    def __add__(self, other: _Vec3f) -> LVecBase3f: ...
    @overload
    def __sub__(self, other: LPoint3f) -> LVector3f: ...
    @overload
    def __sub__(self, other: LVector3f) -> LPoint3f: ...
    @overload
    def __sub__(self, other: _Vec3f) -> LVecBase3f: ...
    def __mul__(self, scalar: float) -> LPoint3f: ...
    def __truediv__(self, scalar: float) -> LPoint3f: ...
    @staticmethod
    def zero() -> LPoint3f:
        """Returns a zero-length point."""
        ...
    @staticmethod
    def unit_x() -> LPoint3f:
        """Returns a unit X point."""
        ...
    @staticmethod
    def unit_y() -> LPoint3f:
        """Returns a unit Y point."""
        ...
    @staticmethod
    def unit_z() -> LPoint3f:
        """Returns a unit Z point."""
        ...
    def get_xy(self) -> LPoint2f:
        """Returns a 2-component vector that shares just the first two components of
        this vector.
        """
        ...
    def get_xz(self) -> LPoint2f:
        """Returns a 2-component vector that shares just the first and last components
        of this vector.
        """
        ...
    def get_yz(self) -> LPoint2f:
        """Returns a 2-component vector that shares just the last two components of
        this vector.
        """
        ...
    def cross(self, other: _Vec3f) -> LPoint3f: ...
    def normalized(self) -> LPoint3f:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: _Vec3f) -> LPoint3f:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    @staticmethod
    def origin(cs: _CoordinateSystem = ...) -> LPoint3f:
        """Returns the origin of the indicated coordinate system.  This is always 0,
        0, 0 with all of our existing coordinate systems; it's hard to imagine it
        ever being different.
        """
        ...
    @staticmethod
    def rfu(right: float, fwd: float, up: float, cs: _CoordinateSystem = ...) -> LPoint3f:
        """Returns a point described by right, forward, up displacements from the
        origin, wherever that maps to in the given coordinate system.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    getXy = get_xy
    getXz = get_xz
    getYz = get_yz
    getClassType = get_class_type

class LPoint3d(LVecBase3d):
    """This is a three-component point in space (as opposed to a three-component
    vector, which represents a direction and a distance).  Some of the methods
    are slightly different between LPoint3 and LVector3; in particular,
    subtraction of two points yields a vector, while addition of a vector and a
    point yields a point.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def xy(self) -> LPoint2d: ...
    @property
    def xz(self) -> LPoint2d: ...
    @property
    def yz(self) -> LPoint2d: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec3d) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2d, z: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float) -> None: ...
    def __neg__(self) -> LPoint3d: ...
    @overload
    def __add__(self, other: LVector3d) -> LPoint3d: ...
    @overload
    def __add__(self, other: _Vec3d) -> LVecBase3d: ...
    @overload
    def __sub__(self, other: LPoint3d) -> LVector3d: ...
    @overload
    def __sub__(self, other: LVector3d) -> LPoint3d: ...
    @overload
    def __sub__(self, other: _Vec3d) -> LVecBase3d: ...
    def __mul__(self, scalar: float) -> LPoint3d: ...
    def __truediv__(self, scalar: float) -> LPoint3d: ...
    @staticmethod
    def zero() -> LPoint3d:
        """Returns a zero-length point."""
        ...
    @staticmethod
    def unit_x() -> LPoint3d:
        """Returns a unit X point."""
        ...
    @staticmethod
    def unit_y() -> LPoint3d:
        """Returns a unit Y point."""
        ...
    @staticmethod
    def unit_z() -> LPoint3d:
        """Returns a unit Z point."""
        ...
    def get_xy(self) -> LPoint2d:
        """Returns a 2-component vector that shares just the first two components of
        this vector.
        """
        ...
    def get_xz(self) -> LPoint2d:
        """Returns a 2-component vector that shares just the first and last components
        of this vector.
        """
        ...
    def get_yz(self) -> LPoint2d:
        """Returns a 2-component vector that shares just the last two components of
        this vector.
        """
        ...
    def cross(self, other: _Vec3d) -> LPoint3d: ...
    def normalized(self) -> LPoint3d:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: _Vec3d) -> LPoint3d:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    @staticmethod
    def origin(cs: _CoordinateSystem = ...) -> LPoint3d:
        """Returns the origin of the indicated coordinate system.  This is always 0,
        0, 0 with all of our existing coordinate systems; it's hard to imagine it
        ever being different.
        """
        ...
    @staticmethod
    def rfu(right: float, fwd: float, up: float, cs: _CoordinateSystem = ...) -> LPoint3d:
        """Returns a point described by right, forward, up displacements from the
        origin, wherever that maps to in the given coordinate system.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    getXy = get_xy
    getXz = get_xz
    getYz = get_yz
    getClassType = get_class_type

class LPoint3i(LVecBase3i):
    """This is a three-component point in space (as opposed to a three-component
    vector, which represents a direction and a distance).  Some of the methods
    are slightly different between LPoint3 and LVector3; in particular,
    subtraction of two points yields a vector, while addition of a vector and a
    point yields a point.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def xy(self) -> LPoint2i: ...
    @property
    def xz(self) -> LPoint2i: ...
    @property
    def yz(self) -> LPoint2i: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: LVecBase3i) -> None: ...
    @overload
    def __init__(self, fill_value: int) -> None: ...
    @overload
    def __init__(self, copy: LVecBase2i, z: int) -> None: ...
    @overload
    def __init__(self, x: int, y: int, z: int) -> None: ...
    def __neg__(self) -> LPoint3i: ...
    @overload
    def __add__(self, other: LVector3i) -> LPoint3i: ...
    @overload
    def __add__(self, other: LVecBase3i) -> LVecBase3i: ...
    @overload
    def __sub__(self, other: LPoint3i) -> LVector3i: ...
    @overload
    def __sub__(self, other: LVector3i) -> LPoint3i: ...
    @overload
    def __sub__(self, other: LVecBase3i) -> LVecBase3i: ...
    def __mul__(self, scalar: int) -> LPoint3i: ...
    @staticmethod
    def zero() -> LPoint3i:
        """Returns a zero-length point."""
        ...
    @staticmethod
    def unit_x() -> LPoint3i:
        """Returns a unit X point."""
        ...
    @staticmethod
    def unit_y() -> LPoint3i:
        """Returns a unit Y point."""
        ...
    @staticmethod
    def unit_z() -> LPoint3i:
        """Returns a unit Z point."""
        ...
    def get_xy(self) -> LPoint2i:
        """Returns a 2-component vector that shares just the first two components of
        this vector.
        """
        ...
    def get_xz(self) -> LPoint2i:
        """Returns a 2-component vector that shares just the first and last components
        of this vector.
        """
        ...
    def get_yz(self) -> LPoint2i:
        """Returns a 2-component vector that shares just the last two components of
        this vector.
        """
        ...
    def cross(self, other: LVecBase3i) -> LPoint3i: ...
    @staticmethod
    def origin(cs: _CoordinateSystem = ...) -> LPoint3i:
        """Returns the origin of the indicated coordinate system.  This is always 0,
        0, 0 with all of our existing coordinate systems; it's hard to imagine it
        ever being different.
        """
        ...
    @staticmethod
    def rfu(right: int, fwd: int, up: int, cs: _CoordinateSystem = ...) -> LPoint3i:
        """Returns a point described by right, forward, up displacements from the
        origin, wherever that maps to in the given coordinate system.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    getXy = get_xy
    getXz = get_xz
    getYz = get_yz
    getClassType = get_class_type

class LVecBase4f:
    """This is the base class for all three-component vectors and points."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    x: float
    y: float
    z: float
    num_components: ClassVar[Literal[4]]
    is_int: ClassVar[Literal[0]]
    @property
    def xyz(self) -> LVecBase3f: ...
    @property
    def xy(self) -> LVecBase2f: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, point: _Vec3f) -> None:
        """Constructs an LVecBase4 from an LPoint3.  The w coordinate is set to 1.0."""
        ...
    @overload
    def __init__(self, copy: _Vec4f) -> None: ...
    @overload
    def __init__(self, vector: _Vec3f) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None:
        """Constructs an LVecBase4 from an LVector3.  The w coordinate is set to 0.0."""
        ...
    @overload
    def __init__(self, copy: _Vec3f, w: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None: ...
    @overload
    def __getitem__(self, i: int) -> float: ...
    @overload
    def __getitem__(self, i: int, assign_val: float) -> None: ...
    @staticmethod
    def __len__() -> int: ...
    def __lt__(self, other: _Vec4f) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __neg__(self) -> LVecBase4f: ...
    def __add__(self, other: _Vec4f) -> LVecBase4f: ...
    def __sub__(self, other: _Vec4f) -> LVecBase4f: ...
    def __mul__(self, scalar: float) -> LVecBase4f: ...
    def __truediv__(self, scalar: float) -> LVecBase4f: ...
    def __iadd__(self, other: _Vec4f) -> LVecBase4f: ...
    def __isub__(self, other: _Vec4f) -> LVecBase4f: ...
    def __imul__(self, scalar: float) -> LVecBase4f: ...
    def __itruediv__(self, scalar: float) -> LVecBase4f: ...
    def __floordiv__(self, scalar: float) -> LVecBase4f: ...
    def __ifloordiv__(self, scalar: float) -> LVecBase4f: ...
    def __pow__(self, exponent: float) -> LVecBase4f: ...
    def __ipow__(self, exponent: float) -> LVecBase4f: ...
    def __round__(self) -> LVecBase4f: ...
    def __floor__(self) -> LVecBase4f: ...
    def __ceil__(self) -> LVecBase4f: ...
    def __le__(self, other: _Vec4f) -> bool: ...
    def __iter__(self) -> Iterator[float]: ...
    @overload
    def assign(self, copy: _Vec4f) -> LVecBase4f: ...
    @overload
    def assign(self, fill_value: float) -> LVecBase4f: ...
    @staticmethod
    def zero() -> LVecBase4f:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVecBase4f:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVecBase4f:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def unit_z() -> LVecBase4f:
        """Returns a unit Z vector."""
        ...
    @staticmethod
    def unit_w() -> LVecBase4f:
        """Returns a unit W vector."""
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the vector is not-a-number, false
        otherwise.
        """
        ...
    def get_cell(self, i: int) -> float: ...
    def set_cell(self, i: int, value: float) -> None: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def get_z(self) -> float: ...
    def get_w(self) -> float: ...
    def get_xyz(self) -> LVecBase3f:
        """Returns the x, y and z component of this vector"""
        ...
    def get_xy(self) -> LVecBase2f:
        """Returns the x and y component of this vector"""
        ...
    def set_x(self, value: float) -> None: ...
    def set_y(self, value: float) -> None: ...
    def set_z(self, value: float) -> None: ...
    def set_w(self, value: float) -> None: ...
    def add_to_cell(self, i: int, value: float) -> None:
        """These next functions add to an existing value.  i.e.
        foo.set_x(foo.get_x() + value) These are useful to reduce overhead in
        scripting languages:
        """
        ...
    def add_x(self, value: float) -> None: ...
    def add_y(self, value: float) -> None: ...
    def add_z(self, value: float) -> None: ...
    def add_w(self, value: float) -> None: ...
    @staticmethod
    def get_num_components() -> int: ...
    def fill(self, fill_value: float) -> None:
        """Sets each element of the vector to the indicated fill_value.  This is
        particularly useful for initializing to zero.
        """
        ...
    def set(self, x: float, y: float, z: float, w: float) -> None: ...
    def dot(self, other: _Vec4f) -> float: ...
    def length_squared(self) -> float:
        """Returns the square of the vector's length, cheap and easy."""
        ...
    def length(self) -> float:
        """Returns the length of the vector, by the Pythagorean theorem."""
        ...
    def normalize(self) -> bool:
        """Normalizes the vector in place.  Returns true if the vector was normalized,
        false if it was a zero-length vector.
        """
        ...
    def normalized(self) -> LVecBase4f:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: _Vec4f) -> LVecBase4f:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    @overload
    def compare_to(self, other: _Vec4f) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    @overload
    def compare_to(self, other: _Vec4f, threshold: float) -> int:
        """Sorts vectors lexicographically, componentwise.  Returns a number less than
        0 if this vector sorts before the other one, greater than zero if it sorts
        after, 0 if they are equivalent (within the indicated tolerance).
        """
        ...
    @overload
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def get_hash(self, threshold: float) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    @overload
    def add_hash(self, hash: int, threshold: float) -> int:
        """Adds the vector into the running hash."""
        ...
    def componentwise_mult(self, other: _Vec4f) -> None: ...
    def fmax(self, other: _Vec4f) -> LVecBase4f: ...
    def fmin(self, other: _Vec4f) -> LVecBase4f: ...
    @overload
    def almost_equal(self, other: _Vec4f) -> bool:
        """Returns true if two vectors are memberwise equal within a default tolerance
        based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: _Vec4f, threshold: float) -> bool:
        """Returns true if two vectors are memberwise equal within a specified
        tolerance.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the vector, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the vector using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    unitW = unit_w
    isNan = is_nan
    getCell = get_cell
    setCell = set_cell
    getX = get_x
    getY = get_y
    getZ = get_z
    getW = get_w
    getXyz = get_xyz
    getXy = get_xy
    setX = set_x
    setY = set_y
    setZ = set_z
    setW = set_w
    addToCell = add_to_cell
    addX = add_x
    addY = add_y
    addZ = add_z
    addW = add_w
    getNumComponents = get_num_components
    lengthSquared = length_squared
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    componentwiseMult = componentwise_mult
    Round = __round__
    Floor = __floor__
    Ceil = __ceil__
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type

class UnalignedLVecBase4f:
    """This is an "unaligned" LVecBase4.  It has no functionality other than to
    store numbers, and it will pack them in as tightly as possible, avoiding
    any SSE2 alignment requirements shared by the primary LVecBase4 class.
    
    Use it only when you need to pack numbers tightly without respect to
    alignment, and then copy it to a proper LVecBase4 to get actual use from
    it.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    num_components: ClassVar[Literal[4]]
    is_int: ClassVar[Literal[0]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec4f) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None: ...
    @overload
    def __getitem__(self, i: int) -> float: ...
    @overload
    def __getitem__(self, i: int, assign_val: float) -> None: ...
    @staticmethod
    def __len__() -> int: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def fill(self, fill_value: float) -> None:
        """Sets each element of the vector to the indicated fill_value.  This is
        particularly useful for initializing to zero.
        """
        ...
    def set(self, x: float, y: float, z: float, w: float) -> None: ...
    @staticmethod
    def get_num_components() -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNumComponents = get_num_components
    getClassType = get_class_type

class LVecBase4d:
    """This is the base class for all three-component vectors and points."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    x: float
    y: float
    z: float
    num_components: ClassVar[Literal[4]]
    is_int: ClassVar[Literal[0]]
    @property
    def xyz(self) -> LVecBase3d: ...
    @property
    def xy(self) -> LVecBase2d: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, point: _Vec3d) -> None:
        """Constructs an LVecBase4 from an LPoint3.  The w coordinate is set to 1.0."""
        ...
    @overload
    def __init__(self, copy: _Vec4d) -> None: ...
    @overload
    def __init__(self, vector: _Vec3d) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None:
        """Constructs an LVecBase4 from an LVector3.  The w coordinate is set to 0.0."""
        ...
    @overload
    def __init__(self, copy: _Vec3d, w: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None: ...
    @overload
    def __getitem__(self, i: int) -> float: ...
    @overload
    def __getitem__(self, i: int, assign_val: float) -> None: ...
    @staticmethod
    def __len__() -> int: ...
    def __lt__(self, other: _Vec4d) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __neg__(self) -> LVecBase4d: ...
    def __add__(self, other: _Vec4d) -> LVecBase4d: ...
    def __sub__(self, other: _Vec4d) -> LVecBase4d: ...
    def __mul__(self, scalar: float) -> LVecBase4d: ...
    def __truediv__(self, scalar: float) -> LVecBase4d: ...
    def __iadd__(self, other: _Vec4d) -> LVecBase4d: ...
    def __isub__(self, other: _Vec4d) -> LVecBase4d: ...
    def __imul__(self, scalar: float) -> LVecBase4d: ...
    def __itruediv__(self, scalar: float) -> LVecBase4d: ...
    def __floordiv__(self, scalar: float) -> LVecBase4d: ...
    def __ifloordiv__(self, scalar: float) -> LVecBase4d: ...
    def __pow__(self, exponent: float) -> LVecBase4d: ...
    def __ipow__(self, exponent: float) -> LVecBase4d: ...
    def __round__(self) -> LVecBase4d: ...
    def __floor__(self) -> LVecBase4d: ...
    def __ceil__(self) -> LVecBase4d: ...
    def __le__(self, other: _Vec4d) -> bool: ...
    def __iter__(self) -> Iterator[float]: ...
    @overload
    def assign(self, copy: _Vec4d) -> LVecBase4d: ...
    @overload
    def assign(self, fill_value: float) -> LVecBase4d: ...
    @staticmethod
    def zero() -> LVecBase4d:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVecBase4d:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVecBase4d:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def unit_z() -> LVecBase4d:
        """Returns a unit Z vector."""
        ...
    @staticmethod
    def unit_w() -> LVecBase4d:
        """Returns a unit W vector."""
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the vector is not-a-number, false
        otherwise.
        """
        ...
    def get_cell(self, i: int) -> float: ...
    def set_cell(self, i: int, value: float) -> None: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def get_z(self) -> float: ...
    def get_w(self) -> float: ...
    def get_xyz(self) -> LVecBase3d:
        """Returns the x, y and z component of this vector"""
        ...
    def get_xy(self) -> LVecBase2d:
        """Returns the x and y component of this vector"""
        ...
    def set_x(self, value: float) -> None: ...
    def set_y(self, value: float) -> None: ...
    def set_z(self, value: float) -> None: ...
    def set_w(self, value: float) -> None: ...
    def add_to_cell(self, i: int, value: float) -> None:
        """These next functions add to an existing value.  i.e.
        foo.set_x(foo.get_x() + value) These are useful to reduce overhead in
        scripting languages:
        """
        ...
    def add_x(self, value: float) -> None: ...
    def add_y(self, value: float) -> None: ...
    def add_z(self, value: float) -> None: ...
    def add_w(self, value: float) -> None: ...
    @staticmethod
    def get_num_components() -> int: ...
    def fill(self, fill_value: float) -> None:
        """Sets each element of the vector to the indicated fill_value.  This is
        particularly useful for initializing to zero.
        """
        ...
    def set(self, x: float, y: float, z: float, w: float) -> None: ...
    def dot(self, other: _Vec4d) -> float: ...
    def length_squared(self) -> float:
        """Returns the square of the vector's length, cheap and easy."""
        ...
    def length(self) -> float:
        """Returns the length of the vector, by the Pythagorean theorem."""
        ...
    def normalize(self) -> bool:
        """Normalizes the vector in place.  Returns true if the vector was normalized,
        false if it was a zero-length vector.
        """
        ...
    def normalized(self) -> LVecBase4d:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: _Vec4d) -> LVecBase4d:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    @overload
    def compare_to(self, other: _Vec4d) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    @overload
    def compare_to(self, other: _Vec4d, threshold: float) -> int:
        """Sorts vectors lexicographically, componentwise.  Returns a number less than
        0 if this vector sorts before the other one, greater than zero if it sorts
        after, 0 if they are equivalent (within the indicated tolerance).
        """
        ...
    @overload
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def get_hash(self, threshold: float) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    @overload
    def add_hash(self, hash: int, threshold: float) -> int:
        """Adds the vector into the running hash."""
        ...
    def componentwise_mult(self, other: _Vec4d) -> None: ...
    def fmax(self, other: _Vec4d) -> LVecBase4d: ...
    def fmin(self, other: _Vec4d) -> LVecBase4d: ...
    @overload
    def almost_equal(self, other: _Vec4d) -> bool:
        """Returns true if two vectors are memberwise equal within a default tolerance
        based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: _Vec4d, threshold: float) -> bool:
        """Returns true if two vectors are memberwise equal within a specified
        tolerance.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the vector, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the vector using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    unitW = unit_w
    isNan = is_nan
    getCell = get_cell
    setCell = set_cell
    getX = get_x
    getY = get_y
    getZ = get_z
    getW = get_w
    getXyz = get_xyz
    getXy = get_xy
    setX = set_x
    setY = set_y
    setZ = set_z
    setW = set_w
    addToCell = add_to_cell
    addX = add_x
    addY = add_y
    addZ = add_z
    addW = add_w
    getNumComponents = get_num_components
    lengthSquared = length_squared
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    componentwiseMult = componentwise_mult
    Round = __round__
    Floor = __floor__
    Ceil = __ceil__
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type

class UnalignedLVecBase4d:
    """This is an "unaligned" LVecBase4.  It has no functionality other than to
    store numbers, and it will pack them in as tightly as possible, avoiding
    any SSE2 alignment requirements shared by the primary LVecBase4 class.
    
    Use it only when you need to pack numbers tightly without respect to
    alignment, and then copy it to a proper LVecBase4 to get actual use from
    it.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    num_components: ClassVar[Literal[4]]
    is_int: ClassVar[Literal[0]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec4d) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None: ...
    @overload
    def __getitem__(self, i: int) -> float: ...
    @overload
    def __getitem__(self, i: int, assign_val: float) -> None: ...
    @staticmethod
    def __len__() -> int: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def fill(self, fill_value: float) -> None:
        """Sets each element of the vector to the indicated fill_value.  This is
        particularly useful for initializing to zero.
        """
        ...
    def set(self, x: float, y: float, z: float, w: float) -> None: ...
    @staticmethod
    def get_num_components() -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNumComponents = get_num_components
    getClassType = get_class_type

class LVecBase4i:
    """This is the base class for all three-component vectors and points."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    x: int
    y: int
    z: int
    num_components: ClassVar[Literal[4]]
    is_int: ClassVar[Literal[1]]
    @property
    def xyz(self) -> LVecBase3i: ...
    @property
    def xy(self) -> LVecBase2i: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, point: LVecBase3i) -> None:
        """Constructs an LVecBase4 from an LPoint3.  The w coordinate is set to 1.0."""
        ...
    @overload
    def __init__(self, copy: _Vec4i) -> None: ...
    @overload
    def __init__(self, vector: LVecBase3i) -> None: ...
    @overload
    def __init__(self, fill_value: int) -> None:
        """Constructs an LVecBase4 from an LVector3.  The w coordinate is set to 0.0."""
        ...
    @overload
    def __init__(self, copy: LVecBase3i, w: int) -> None: ...
    @overload
    def __init__(self, x: int, y: int, z: int, w: int) -> None: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, i: int, assign_val: int) -> None: ...
    @staticmethod
    def __len__() -> int: ...
    def __lt__(self, other: _Vec4i) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __neg__(self) -> LVecBase4i: ...
    def __add__(self, other: _Vec4i) -> LVecBase4i: ...
    def __sub__(self, other: _Vec4i) -> LVecBase4i: ...
    def __mul__(self, scalar: int) -> LVecBase4i: ...
    def __iadd__(self, other: _Vec4i) -> LVecBase4i: ...
    def __isub__(self, other: _Vec4i) -> LVecBase4i: ...
    def __imul__(self, scalar: int) -> LVecBase4i: ...
    def __floordiv__(self, scalar: int) -> LVecBase4i: ...
    def __ifloordiv__(self, scalar: int) -> LVecBase4i: ...
    def __pow__(self, exponent: int) -> LVecBase4i: ...
    def __ipow__(self, exponent: int) -> LVecBase4i: ...
    def __round__(self) -> LVecBase4i: ...
    def __floor__(self) -> LVecBase4i: ...
    def __ceil__(self) -> LVecBase4i: ...
    def __le__(self, other: _Vec4i) -> bool: ...
    def __iter__(self) -> Iterator[int]: ...
    @overload
    def assign(self, copy: _Vec4i) -> LVecBase4i: ...
    @overload
    def assign(self, fill_value: int) -> LVecBase4i: ...
    @staticmethod
    def zero() -> LVecBase4i:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVecBase4i:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVecBase4i:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def unit_z() -> LVecBase4i:
        """Returns a unit Z vector."""
        ...
    @staticmethod
    def unit_w() -> LVecBase4i:
        """Returns a unit W vector."""
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the vector is not-a-number, false
        otherwise.
        """
        ...
    def get_cell(self, i: int) -> int: ...
    def set_cell(self, i: int, value: int) -> None: ...
    def get_x(self) -> int: ...
    def get_y(self) -> int: ...
    def get_z(self) -> int: ...
    def get_w(self) -> int: ...
    def get_xyz(self) -> LVecBase3i:
        """Returns the x, y and z component of this vector"""
        ...
    def get_xy(self) -> LVecBase2i:
        """Returns the x and y component of this vector"""
        ...
    def set_x(self, value: int) -> None: ...
    def set_y(self, value: int) -> None: ...
    def set_z(self, value: int) -> None: ...
    def set_w(self, value: int) -> None: ...
    def add_to_cell(self, i: int, value: int) -> None:
        """These next functions add to an existing value.  i.e.
        foo.set_x(foo.get_x() + value) These are useful to reduce overhead in
        scripting languages:
        """
        ...
    def add_x(self, value: int) -> None: ...
    def add_y(self, value: int) -> None: ...
    def add_z(self, value: int) -> None: ...
    def add_w(self, value: int) -> None: ...
    @staticmethod
    def get_num_components() -> int: ...
    def fill(self, fill_value: int) -> None:
        """Sets each element of the vector to the indicated fill_value.  This is
        particularly useful for initializing to zero.
        """
        ...
    def set(self, x: int, y: int, z: int, w: int) -> None: ...
    def dot(self, other: _Vec4i) -> int: ...
    def length_squared(self) -> int:
        """Returns the square of the vector's length, cheap and easy."""
        ...
    def compare_to(self, other: _Vec4i) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    def componentwise_mult(self, other: _Vec4i) -> None: ...
    def fmax(self, other: _Vec4i) -> LVecBase4i: ...
    def fmin(self, other: _Vec4i) -> LVecBase4i: ...
    @overload
    def almost_equal(self, other: _Vec4i) -> bool:
        """Returns true if two vectors are memberwise equal within a default tolerance
        based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: _Vec4i, threshold: int) -> bool:
        """Returns true if two vectors are memberwise equal within a specified
        tolerance.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the vector, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the vector to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the vector using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the vector from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    unitW = unit_w
    isNan = is_nan
    getCell = get_cell
    setCell = set_cell
    getX = get_x
    getY = get_y
    getZ = get_z
    getW = get_w
    getXyz = get_xyz
    getXy = get_xy
    setX = set_x
    setY = set_y
    setZ = set_z
    setW = set_w
    addToCell = add_to_cell
    addX = add_x
    addY = add_y
    addZ = add_z
    addW = add_w
    getNumComponents = get_num_components
    lengthSquared = length_squared
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    componentwiseMult = componentwise_mult
    Round = __round__
    Floor = __floor__
    Ceil = __ceil__
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type

class UnalignedLVecBase4i:
    """This is an "unaligned" LVecBase4.  It has no functionality other than to
    store numbers, and it will pack them in as tightly as possible, avoiding
    any SSE2 alignment requirements shared by the primary LVecBase4 class.
    
    Use it only when you need to pack numbers tightly without respect to
    alignment, and then copy it to a proper LVecBase4 to get actual use from
    it.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    num_components: ClassVar[Literal[4]]
    is_int: ClassVar[Literal[1]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec4i) -> None: ...
    @overload
    def __init__(self, fill_value: int) -> None: ...
    @overload
    def __init__(self, x: int, y: int, z: int, w: int) -> None: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, i: int, assign_val: int) -> None: ...
    @staticmethod
    def __len__() -> int: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def fill(self, fill_value: int) -> None:
        """Sets each element of the vector to the indicated fill_value.  This is
        particularly useful for initializing to zero.
        """
        ...
    def set(self, x: int, y: int, z: int, w: int) -> None: ...
    @staticmethod
    def get_num_components() -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNumComponents = get_num_components
    getClassType = get_class_type

class LVector4f(LVecBase4f):
    """This is a four-component vector distance."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def xyz(self) -> LVector3f: ...
    @property
    def xy(self) -> LVector2f: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec4f) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, copy: _Vec3f, w: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None: ...
    def __neg__(self) -> LVector4f: ...
    @overload
    def __add__(self, other: LVector4f) -> LVector4f: ...
    @overload
    def __add__(self, other: _Vec4f) -> LVecBase4f: ...
    @overload
    def __sub__(self, other: LVector4f) -> LVector4f: ...
    @overload
    def __sub__(self, other: _Vec4f) -> LVecBase4f: ...
    def __mul__(self, scalar: float) -> LVector4f: ...
    def __truediv__(self, scalar: float) -> LVector4f: ...
    @staticmethod
    def zero() -> LVector4f:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVector4f:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVector4f:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def unit_z() -> LVector4f:
        """Returns a unit Z vector."""
        ...
    @staticmethod
    def unit_w() -> LVector4f:
        """Returns a unit W vector."""
        ...
    def get_xyz(self) -> LVector3f:
        """Returns the x, y and z component of this vector"""
        ...
    def get_xy(self) -> LVector2f:
        """Returns the x and y component of this vector"""
        ...
    def normalized(self) -> LVector4f:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: _Vec4f) -> LVector4f:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    unitW = unit_w
    getXyz = get_xyz
    getXy = get_xy
    getClassType = get_class_type

class LVector4d(LVecBase4d):
    """This is a four-component vector distance."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def xyz(self) -> LVector3d: ...
    @property
    def xy(self) -> LVector2d: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec4d) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, copy: _Vec3d, w: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None: ...
    def __neg__(self) -> LVector4d: ...
    @overload
    def __add__(self, other: LVector4d) -> LVector4d: ...
    @overload
    def __add__(self, other: _Vec4d) -> LVecBase4d: ...
    @overload
    def __sub__(self, other: LVector4d) -> LVector4d: ...
    @overload
    def __sub__(self, other: _Vec4d) -> LVecBase4d: ...
    def __mul__(self, scalar: float) -> LVector4d: ...
    def __truediv__(self, scalar: float) -> LVector4d: ...
    @staticmethod
    def zero() -> LVector4d:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVector4d:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVector4d:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def unit_z() -> LVector4d:
        """Returns a unit Z vector."""
        ...
    @staticmethod
    def unit_w() -> LVector4d:
        """Returns a unit W vector."""
        ...
    def get_xyz(self) -> LVector3d:
        """Returns the x, y and z component of this vector"""
        ...
    def get_xy(self) -> LVector2d:
        """Returns the x and y component of this vector"""
        ...
    def normalized(self) -> LVector4d:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: _Vec4d) -> LVector4d:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    unitW = unit_w
    getXyz = get_xyz
    getXy = get_xy
    getClassType = get_class_type

class LVector4i(LVecBase4i):
    """This is a four-component vector distance."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def xyz(self) -> LVector3i: ...
    @property
    def xy(self) -> LVector2i: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec4i) -> None: ...
    @overload
    def __init__(self, fill_value: int) -> None: ...
    @overload
    def __init__(self, copy: LVecBase3i, w: int) -> None: ...
    @overload
    def __init__(self, x: int, y: int, z: int, w: int) -> None: ...
    def __neg__(self) -> LVector4i: ...
    @overload
    def __add__(self, other: LVector4i) -> LVector4i: ...
    @overload
    def __add__(self, other: _Vec4i) -> LVecBase4i: ...
    @overload
    def __sub__(self, other: LVector4i) -> LVector4i: ...
    @overload
    def __sub__(self, other: _Vec4i) -> LVecBase4i: ...
    def __mul__(self, scalar: int) -> LVector4i: ...
    @staticmethod
    def zero() -> LVector4i:
        """Returns a zero-length vector."""
        ...
    @staticmethod
    def unit_x() -> LVector4i:
        """Returns a unit X vector."""
        ...
    @staticmethod
    def unit_y() -> LVector4i:
        """Returns a unit Y vector."""
        ...
    @staticmethod
    def unit_z() -> LVector4i:
        """Returns a unit Z vector."""
        ...
    @staticmethod
    def unit_w() -> LVector4i:
        """Returns a unit W vector."""
        ...
    def get_xyz(self) -> LVector3i:
        """Returns the x, y and z component of this vector"""
        ...
    def get_xy(self) -> LVector2i:
        """Returns the x and y component of this vector"""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    unitW = unit_w
    getXyz = get_xyz
    getXy = get_xy
    getClassType = get_class_type

class LPoint4f(LVecBase4f):
    """This is a four-component point in space."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def xyz(self) -> LPoint3f: ...
    @property
    def xy(self) -> LPoint2f: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec4f) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, copy: _Vec3f, w: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None: ...
    def __neg__(self) -> LPoint4f: ...
    @overload
    def __add__(self, other: LVector4f) -> LPoint4f: ...
    @overload
    def __add__(self, other: _Vec4f) -> LVecBase4f: ...
    @overload
    def __sub__(self, other: LPoint4f) -> LVector4f: ...
    @overload
    def __sub__(self, other: LVector4f) -> LPoint4f: ...
    @overload
    def __sub__(self, other: _Vec4f) -> LVecBase4f: ...
    def __mul__(self, scalar: float) -> LPoint4f: ...
    def __truediv__(self, scalar: float) -> LPoint4f: ...
    @staticmethod
    def zero() -> LPoint4f:
        """Returns a zero-length point."""
        ...
    @staticmethod
    def unit_x() -> LPoint4f:
        """Returns a unit X point."""
        ...
    @staticmethod
    def unit_y() -> LPoint4f:
        """Returns a unit Y point."""
        ...
    @staticmethod
    def unit_z() -> LPoint4f:
        """Returns a unit Z point."""
        ...
    @staticmethod
    def unit_w() -> LPoint4f:
        """Returns a unit W point."""
        ...
    def get_xyz(self) -> LPoint3f:
        """Returns the x, y and z component of this vector"""
        ...
    def get_xy(self) -> LPoint2f:
        """Returns the x and y component of this vector"""
        ...
    def normalized(self) -> LPoint4f:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: _Vec4f) -> LPoint4f:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    unitW = unit_w
    getXyz = get_xyz
    getXy = get_xy
    getClassType = get_class_type

class LPoint4d(LVecBase4d):
    """This is a four-component point in space."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def xyz(self) -> LPoint3d: ...
    @property
    def xy(self) -> LPoint2d: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec4d) -> None: ...
    @overload
    def __init__(self, fill_value: float) -> None: ...
    @overload
    def __init__(self, copy: _Vec3d, w: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None: ...
    def __neg__(self) -> LPoint4d: ...
    @overload
    def __add__(self, other: LVector4d) -> LPoint4d: ...
    @overload
    def __add__(self, other: _Vec4d) -> LVecBase4d: ...
    @overload
    def __sub__(self, other: LPoint4d) -> LVector4d: ...
    @overload
    def __sub__(self, other: LVector4d) -> LPoint4d: ...
    @overload
    def __sub__(self, other: _Vec4d) -> LVecBase4d: ...
    def __mul__(self, scalar: float) -> LPoint4d: ...
    def __truediv__(self, scalar: float) -> LPoint4d: ...
    @staticmethod
    def zero() -> LPoint4d:
        """Returns a zero-length point."""
        ...
    @staticmethod
    def unit_x() -> LPoint4d:
        """Returns a unit X point."""
        ...
    @staticmethod
    def unit_y() -> LPoint4d:
        """Returns a unit Y point."""
        ...
    @staticmethod
    def unit_z() -> LPoint4d:
        """Returns a unit Z point."""
        ...
    @staticmethod
    def unit_w() -> LPoint4d:
        """Returns a unit W point."""
        ...
    def get_xyz(self) -> LPoint3d:
        """Returns the x, y and z component of this vector"""
        ...
    def get_xy(self) -> LPoint2d:
        """Returns the x and y component of this vector"""
        ...
    def normalized(self) -> LPoint4d:
        """Normalizes the vector and returns the normalized vector as a copy.  If the
        vector was a zero-length vector, a zero length vector will be returned.
        """
        ...
    def project(self, onto: _Vec4d) -> LPoint4d:
        """Returns a new vector representing the projection of this vector onto
        another one.  The resulting vector will be a scalar multiple of onto.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    unitW = unit_w
    getXyz = get_xyz
    getXy = get_xy
    getClassType = get_class_type

class LPoint4i(LVecBase4i):
    """This is a four-component point in space."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def xyz(self) -> LPoint3i: ...
    @property
    def xy(self) -> LPoint2i: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec4i) -> None: ...
    @overload
    def __init__(self, fill_value: int) -> None: ...
    @overload
    def __init__(self, copy: LVecBase3i, w: int) -> None: ...
    @overload
    def __init__(self, x: int, y: int, z: int, w: int) -> None: ...
    def __neg__(self) -> LPoint4i: ...
    @overload
    def __add__(self, other: LVector4i) -> LPoint4i: ...
    @overload
    def __add__(self, other: _Vec4i) -> LVecBase4i: ...
    @overload
    def __sub__(self, other: LPoint4i) -> LVector4i: ...
    @overload
    def __sub__(self, other: LVector4i) -> LPoint4i: ...
    @overload
    def __sub__(self, other: _Vec4i) -> LVecBase4i: ...
    def __mul__(self, scalar: int) -> LPoint4i: ...
    @staticmethod
    def zero() -> LPoint4i:
        """Returns a zero-length point."""
        ...
    @staticmethod
    def unit_x() -> LPoint4i:
        """Returns a unit X point."""
        ...
    @staticmethod
    def unit_y() -> LPoint4i:
        """Returns a unit Y point."""
        ...
    @staticmethod
    def unit_z() -> LPoint4i:
        """Returns a unit Z point."""
        ...
    @staticmethod
    def unit_w() -> LPoint4i:
        """Returns a unit W point."""
        ...
    def get_xyz(self) -> LPoint3i:
        """Returns the x, y and z component of this vector"""
        ...
    def get_xy(self) -> LPoint2i:
        """Returns the x and y component of this vector"""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    unitX = unit_x
    unitY = unit_y
    unitZ = unit_z
    unitW = unit_w
    getXyz = get_xyz
    getXy = get_xy
    getClassType = get_class_type

class LMatrix3f:
    """This is a 3-by-3 transform matrix.  It typically will represent either a
    rotation-and-scale (no translation) matrix in 3-d, or a full affine matrix
    (rotation, scale, translation) in 2-d, e.g.  for a texture matrix.
    """
    class Row:
        """These helper classes are used to support two-level operator []."""
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: LMatrix3f.Row) -> None: ...
        @overload
        def __getitem__(self, i: int) -> float: ...
        @overload
        def __getitem__(self, i: int, assign_val: float) -> None: ...
        @staticmethod
        def __len__() -> int:
            """Returns 3: the number of columns of a LMatrix3."""
            ...
        def operator_typecast(self) -> LVecBase3f: ...
        operatorTypecast = operator_typecast
    class CRow:
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: LMatrix3f.CRow) -> None: ...
        def __getitem__(self, i: int) -> float: ...
        @staticmethod
        def __len__() -> int:
            """Returns 3: the number of columns of a LMatrix3."""
            ...
        def operator_typecast(self) -> LVecBase3f: ...
        operatorTypecast = operator_typecast
    DtoolClassDict: ClassVar[dict[str, Any]]
    num_components: ClassVar[Literal[9]]
    is_int: ClassVar[Literal[0]]
    @property
    def rows(self) -> Sequence[LVecBase3f]: ...
    @property
    def cols(self) -> Sequence[LVecBase3f]: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: LMatrix3f) -> None: ...
    @overload
    def __init__(self, __param0: _Vec3f, __param1: _Vec3f, __param2: _Vec3f) -> None:
        """Constructs the matrix from three individual rows."""
        ...
    @overload
    def __init__(self, __param0: float, __param1: float, __param2: float, __param3: float, __param4: float, __param5: float, __param6: float, __param7: float, __param8: float) -> None: ...
    def __getitem__(self, i: int) -> LMatrix3f.CRow | LMatrix3f.Row: ...
    @staticmethod
    def __len__() -> int:
        """Returns 3: the number of rows of a LMatrix3."""
        ...
    def __call__(self, row: int, col: int) -> float | None: ...
    def __lt__(self, other: LMatrix3f) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    @overload
    def __mul__(self, other: LMatrix3f) -> LMatrix3f: ...
    @overload
    def __mul__(self, scalar: float) -> LMatrix3f: ...
    def __truediv__(self, scalar: float) -> LMatrix3f: ...
    def __iadd__(self, other: LMatrix3f) -> LMatrix3f:
        """Performs a memberwise addition between two matrices."""
        ...
    def __isub__(self, other: LMatrix3f) -> LMatrix3f:
        """Performs a memberwise subtraction between two matrices."""
        ...
    @overload
    def __imul__(self, other: LMatrix3f) -> LMatrix3f: ...
    @overload
    def __imul__(self, scalar: float) -> LMatrix3f:
        """Performs a memberwise scale."""
        ...
    def __itruediv__(self, scalar: float) -> LMatrix3f:
        """Performs a memberwise scale."""
        ...
    def __le__(self, other: LMatrix3f) -> bool: ...
    @overload
    def assign(self, other: LMatrix3f) -> LMatrix3f: ...
    @overload
    def assign(self, fill_value: float) -> LMatrix3f: ...
    def fill(self, fill_value: float) -> None:
        """Sets each element of the matrix to the indicated fill_value.  This is of
        questionable value, but is sometimes useful when initializing to zero.
        """
        ...
    def set(self, e00: float, e01: float, e02: float, e10: float, e11: float, e12: float, e20: float, e21: float, e22: float) -> None: ...
    def set_row(self, row: int, v: LVecBase2f | _Vec3f) -> None:
        """Replaces the indicated row of the matrix from a two-component vector,
        ignoring the last column.
        """
        ...
    def set_col(self, col: int, v: LVecBase2f | _Vec3f) -> None:
        """Replaces the indicated column of the matrix from a two-component vector,
        ignoring the last row.
        """
        ...
    @overload
    def get_row(self, row: int) -> LVecBase3f:
        """Stores the indicated row of the matrix as a three-component vector."""
        ...
    @overload
    def get_row(self, result_vec: _Vec3f, row: int) -> None:
        """Returns the indicated row of the matrix as a three-component vector."""
        ...
    def get_col(self, col: int) -> LVecBase3f:
        """Returns the indicated column of the matrix as a three-component vector."""
        ...
    def get_row2(self, row: int) -> LVecBase2f:
        """Returns the indicated row of the matrix as a two-component vector, ignoring
        the last column.
        """
        ...
    def get_col2(self, col: int) -> LVecBase2f:
        """Returns the indicated column of the matrix as a two-component vector,
        ignoring the last row.
        """
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the matrix is not-a-number, false
        otherwise.
        """
        ...
    def is_identity(self) -> bool:
        """Returns true if this is (close enough to) the identity matrix, false
        otherwise.
        """
        ...
    def get_cell(self, row: int, col: int) -> float:
        """Returns a particular element of the matrix."""
        ...
    def set_cell(self, row: int, col: int, value: float) -> None:
        """Changes a particular element of the matrix."""
        ...
    def get_num_components(self) -> int:
        """Returns the number of elements in the matrix, nine."""
        ...
    @overload
    def compare_to(self, other: LMatrix3f) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    @overload
    def compare_to(self, other: LMatrix3f, threshold: float) -> int:
        """Sorts matrices lexicographically, componentwise.  Returns a number less
        than 0 if this matrix sorts before the other one, greater than zero if it
        sorts after, 0 if they are equivalent (within the indicated tolerance).
        """
        ...
    @overload
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def get_hash(self, threshold: float) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    @overload
    def add_hash(self, hash: int, threshold: float) -> int:
        """Adds the vector into the running hash."""
        ...
    def xform(self, v: _Vec3f) -> LVecBase3f:
        """3-component vector or point times matrix."""
        ...
    def xform_point(self, v: LVecBase2f) -> LVecBase2f:
        """The matrix transforms a 2-component point (including translation component)
        and returns the result.  This assumes the matrix is an affine transform.
        """
        ...
    @overload
    def xform_vec(self, v: LVecBase2f) -> LVecBase2f:
        """The matrix transforms a 2-component vector (without translation component)
        and returns the result.  This assumes the matrix is an affine transform.
        """
        ...
    @overload
    def xform_vec(self, v: _Vec3f) -> LVecBase3f:
        """The matrix transforms a 3-component vector and returns the result.  This
        assumes the matrix is an orthonormal transform.
        
        In practice, this is the same computation as xform().
        """
        ...
    def xform_vec_general(self, v: _Vec3f) -> LVecBase3f:
        """The matrix transforms a 3-component vector (without translation component)
        and returns the result, as a fully general operation.
        """
        ...
    def xform_in_place(self, v: _Vec3f) -> None:
        """3-component vector or point times matrix."""
        ...
    def xform_point_in_place(self, v: LVecBase2f) -> None:
        """The matrix transforms a 2-component point (including translation
        component).  This assumes the matrix is an affine transform.
        """
        ...
    def xform_vec_in_place(self, v: LVecBase2f | _Vec3f) -> None:
        """The matrix transforms a 2-component vector (without translation component).
        This assumes the matrix is an affine transform.
        """
        ...
    def xform_vec_general_in_place(self, v: _Vec3f) -> None:
        """The matrix transforms a 3-component vector (without translation component),
        as a fully general operation.
        """
        ...
    def multiply(self, other1: LMatrix3f, other2: LMatrix3f) -> None:
        """this = other1 * other2"""
        ...
    def componentwise_mult(self, other: LMatrix3f) -> None: ...
    def determinant(self) -> float:
        """Returns the determinant of the matrix."""
        ...
    def transpose_from(self, other: LMatrix3f) -> None: ...
    def transpose_in_place(self) -> None: ...
    def invert_from(self, other: LMatrix3f) -> bool:
        """Computes the inverse of the other matrix, and stores the result in this
        matrix.  This is a fully general operation and makes no assumptions about
        the type of transform represented by the matrix.
        
        The other matrix must be a different object than this matrix.  However, if
        you need to invert a matrix in place, see invert_in_place.
        
        The return value is true if the matrix was successfully inverted, false if
        there was a singularity.
        """
        ...
    def invert_in_place(self) -> bool:
        """Inverts the current matrix.  Returns true if the inverse is successful,
        false if the matrix was singular.
        """
        ...
    def invert_transpose_from(self, other: LMatrix3f | _Mat4f) -> bool:
        """Simultaneously computes the inverse of the indicated matrix, and then the
        transpose of that inverse.
        """
        ...
    @staticmethod
    def ident_mat() -> LMatrix3f:
        """Returns an identity matrix.
        
        This function definition must appear first, since some inline functions
        below take advantage of it.
        """
        ...
    def set_translate_mat(self, trans: LVecBase2f) -> None:
        """Fills mat with a matrix that applies the indicated translation."""
        ...
    @overload
    def set_rotate_mat(self, angle: float) -> None:
        """Fills mat with a matrix that rotates by the given angle in degrees
        counterclockwise.
        """
        ...
    @overload
    def set_rotate_mat(self, angle: float, axis: _Vec3f, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.
        """
        ...
    def set_scale_mat(self, scale: LVecBase2f | _Vec3f) -> None:
        """Fills mat with a matrix that applies the indicated scale in each of the two
        axes.
        """
        ...
    @overload
    @staticmethod
    def translate_mat(trans: LVecBase2f) -> LMatrix3f:
        """Returns a matrix that applies the indicated translation."""
        ...
    @overload
    @staticmethod
    def translate_mat(tx: float, ty: float) -> LMatrix3f:
        """Returns a matrix that applies the indicated translation."""
        ...
    @overload
    @staticmethod
    def rotate_mat(angle: float) -> LMatrix3f:
        """Returns a matrix that rotates by the given angle in degrees
        counterclockwise.
        """
        ...
    @overload
    @staticmethod
    def rotate_mat(angle: float, axis: _Vec3f, cs: _CoordinateSystem = ...) -> LMatrix3f:
        """Returns a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.
        """
        ...
    @overload
    @staticmethod
    def scale_mat(scale: LVecBase2f | _Vec3f) -> LMatrix3f:
        """Returns a matrix that applies the indicated scale in each of the two axes."""
        ...
    @overload
    @staticmethod
    def scale_mat(sx: float, sy: float) -> LMatrix3f:
        """Returns a matrix that applies the indicated scale in each of the three
        axes.
        """
        ...
    @overload
    @staticmethod
    def scale_mat(sx: float, sy: float, sz: float) -> LMatrix3f:
        """Returns a matrix that applies the indicated scale in each of the two axes."""
        ...
    def set_rotate_mat_normaxis(self, angle: float, axis: _Vec3f, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.  Assumes axis has been
        normalized.
        """
        ...
    @staticmethod
    def rotate_mat_normaxis(angle: float, axis: _Vec3f, cs: _CoordinateSystem = ...) -> LMatrix3f:
        """Returns a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.  Assumes axis has been
        normalized.
        """
        ...
    def set_shear_mat(self, shear: _Vec3f, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that applies the indicated shear in each of the
        three planes.
        """
        ...
    @overload
    @staticmethod
    def shear_mat(shear: _Vec3f, cs: _CoordinateSystem = ...) -> LMatrix3f:
        """Returns a matrix that applies the indicated shear in each of the three
        planes.
        """
        ...
    @overload
    @staticmethod
    def shear_mat(shxy: float, shxz: float, shyz: float, cs: _CoordinateSystem = ...) -> LMatrix3f:
        """Returns a matrix that applies the indicated shear in each of the three
        planes.
        """
        ...
    def set_scale_shear_mat(self, scale: _Vec3f, shear: _Vec3f, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that applies the indicated scale and shear."""
        ...
    @overload
    @staticmethod
    def scale_shear_mat(scale: _Vec3f, shear: _Vec3f, cs: _CoordinateSystem = ...) -> LMatrix3f:
        """Returns a matrix that applies the indicated scale and shear."""
        ...
    @overload
    @staticmethod
    def scale_shear_mat(sx: float, sy: float, sz: float, shxy: float, shxz: float, shyz: float, cs: _CoordinateSystem = ...) -> LMatrix3f:
        """Returns a matrix that applies the indicated scale and shear."""
        ...
    @staticmethod
    def convert_mat(_from: _CoordinateSystem, to: _CoordinateSystem) -> LMatrix3f:
        """Returns a matrix that transforms from the indicated coordinate system to
        the indicated coordinate system.
        """
        ...
    @overload
    def almost_equal(self, other: LMatrix3f) -> bool:
        """Returns true if two matrices are memberwise equal within a default
        tolerance based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: LMatrix3f, threshold: float) -> bool:
        """Returns true if two matrices are memberwise equal within a specified
        tolerance.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the matrix to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the matrix, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, scan: DatagramIterator) -> None:
        """Reads the matrix from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the matrix to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the matrix using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the matrix from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_rows(self) -> tuple[None, ...]: ...
    def get_cols(self) -> tuple[LVecBase3f, ...]: ...
    def get_col2s(self) -> tuple[LVecBase2f, ...]: ...
    def get_row2s(self) -> tuple[LVecBase2f, ...]: ...
    setRow = set_row
    setCol = set_col
    getRow = get_row
    getCol = get_col
    getRow2 = get_row2
    getCol2 = get_col2
    isNan = is_nan
    isIdentity = is_identity
    getCell = get_cell
    setCell = set_cell
    getNumComponents = get_num_components
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    xformPoint = xform_point
    xformVec = xform_vec
    xformVecGeneral = xform_vec_general
    xformInPlace = xform_in_place
    xformPointInPlace = xform_point_in_place
    xformVecInPlace = xform_vec_in_place
    xformVecGeneralInPlace = xform_vec_general_in_place
    componentwiseMult = componentwise_mult
    transposeFrom = transpose_from
    transposeInPlace = transpose_in_place
    invertFrom = invert_from
    invertInPlace = invert_in_place
    invertTransposeFrom = invert_transpose_from
    identMat = ident_mat
    setTranslateMat = set_translate_mat
    setRotateMat = set_rotate_mat
    setScaleMat = set_scale_mat
    translateMat = translate_mat
    rotateMat = rotate_mat
    scaleMat = scale_mat
    setRotateMatNormaxis = set_rotate_mat_normaxis
    rotateMatNormaxis = rotate_mat_normaxis
    setShearMat = set_shear_mat
    shearMat = shear_mat
    setScaleShearMat = set_scale_shear_mat
    scaleShearMat = scale_shear_mat
    convertMat = convert_mat
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type
    getRows = get_rows
    getCols = get_cols
    getCol2s = get_col2s
    getRow2s = get_row2s

class LMatrix4f:
    """This is a 4-by-4 transform matrix."""
    class Row:
        """These helper classes are used to support two-level operator []."""
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: LMatrix4f.Row) -> None: ...
        @overload
        def __getitem__(self, i: int) -> float: ...
        @overload
        def __getitem__(self, i: int, assign_val: float) -> None: ...
        @staticmethod
        def __len__() -> int:
            """Returns 4: the number of columns of a LMatrix4."""
            ...
        def operator_typecast(self) -> LVecBase4f: ...
        operatorTypecast = operator_typecast
    class CRow:
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: LMatrix4f.CRow) -> None: ...
        def __getitem__(self, i: int) -> float: ...
        @staticmethod
        def __len__() -> int:
            """Returns 4: the number of columns of a LMatrix4."""
            ...
        def operator_typecast(self) -> LVecBase4f: ...
        operatorTypecast = operator_typecast
    DtoolClassDict: ClassVar[dict[str, Any]]
    num_components: ClassVar[Literal[16]]
    is_int: ClassVar[Literal[0]]
    @property
    def rows(self) -> Sequence[LVecBase4f]: ...
    @property
    def cols(self) -> Sequence[LVecBase4f]: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, upper3: LMatrix3f) -> None:
        """Construct a 4x4 matrix given a 3x3 rotation matrix and an optional
        translation component.
        """
        ...
    @overload
    def __init__(self, other: _Mat4f) -> None: ...
    @overload
    def __init__(self, upper3: LMatrix3f, trans: _Vec3f) -> None: ...
    @overload
    def __init__(self, __param0: _Vec4f, __param1: _Vec4f, __param2: _Vec4f, __param3: _Vec4f) -> None:
        """Constructs the matrix from four individual rows."""
        ...
    @overload
    def __init__(self, __param0: float, __param1: float, __param2: float, __param3: float, __param4: float, __param5: float, __param6: float, __param7: float, __param8: float, __param9: float, __param10: float, __param11: float, __param12: float, __param13: float, __param14: float, __param15: float) -> None: ...
    def __getitem__(self, i: int) -> LMatrix4f.CRow | LMatrix4f.Row: ...
    @staticmethod
    def __len__() -> int:
        """Returns 4: the number of rows of a LMatrix4."""
        ...
    def __call__(self, row: int, col: int) -> float | None: ...
    def __lt__(self, other: _Mat4f) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    @overload
    def __mul__(self, other: _Mat4f) -> LMatrix4f: ...
    @overload
    def __mul__(self, scalar: float) -> LMatrix4f: ...
    def __truediv__(self, scalar: float) -> LMatrix4f: ...
    def __iadd__(self, other: _Mat4f) -> LMatrix4f:
        """Performs a memberwise addition between two matrices."""
        ...
    def __isub__(self, other: _Mat4f) -> LMatrix4f:
        """Performs a memberwise subtraction between two matrices."""
        ...
    @overload
    def __imul__(self, other: _Mat4f) -> LMatrix4f: ...
    @overload
    def __imul__(self, scalar: float) -> LMatrix4f: ...
    def __itruediv__(self, scalar: float) -> LMatrix4f: ...
    def __le__(self, other: _Mat4f) -> bool: ...
    @overload
    def assign(self, other: _Mat4f) -> LMatrix4f: ...
    @overload
    def assign(self, fill_value: float) -> LMatrix4f: ...
    def fill(self, fill_value: float) -> None:
        """Sets each element of the matrix to the indicated fill_value.  This is of
        questionable value, but is sometimes useful when initializing to zero.
        """
        ...
    def set(self, e00: float, e01: float, e02: float, e03: float, e10: float, e11: float, e12: float, e13: float, e20: float, e21: float, e22: float, e23: float, e30: float, e31: float, e32: float, e33: float) -> None: ...
    def set_upper_3(self, upper3: LMatrix3f) -> None:
        """Get and set the upper 3x3 rotation matrix."""
        ...
    def get_upper_3(self) -> LMatrix3f:
        """Retrieves the upper 3x3 submatrix."""
        ...
    def set_row(self, row: int, v: _Vec3f | _Vec4f) -> None:
        """Replaces the indicated row of the matrix with the indicated 3-component
        vector, ignoring the last column.
        """
        ...
    def set_col(self, col: int, v: _Vec3f | _Vec4f) -> None:
        """Replaces the indicated column of the matrix with the indicated 3-component
        vector, ignoring the last row.
        """
        ...
    @overload
    def get_row(self, row: int) -> LVecBase4f:
        """Stores the indicated row of the matrix as a 4-component vector."""
        ...
    @overload
    def get_row(self, result_vec: _Vec4f, row: int) -> None:
        """Retrieves the indicated row of the matrix as a 4-component vector."""
        ...
    def get_col(self, col: int) -> LVecBase4f:
        """Retrieves the indicated column of the matrix as a 4-component vector."""
        ...
    @overload
    def get_row3(self, row: int) -> LVecBase3f:
        """Stores the row column of the matrix as a 3-component vector, ignoring the
        last column.
        """
        ...
    @overload
    def get_row3(self, result_vec: _Vec3f, row: int) -> None:
        """Retrieves the row column of the matrix as a 3-component vector, ignoring
        the last column.
        """
        ...
    def get_col3(self, col: int) -> LVecBase3f:
        """Retrieves the indicated column of the matrix as a 3-component vector,
        ignoring the last row.
        """
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the matrix is not-a-number, false
        otherwise.
        """
        ...
    def is_identity(self) -> bool:
        """Returns true if this is (close enough to) the identity matrix, false
        otherwise.
        """
        ...
    def get_cell(self, row: int, col: int) -> float:
        """Returns a particular element of the matrix."""
        ...
    def set_cell(self, row: int, col: int, value: float) -> None:
        """Changes a particular element of the matrix."""
        ...
    def get_num_components(self) -> int:
        """Returns the number of elements in the matrix, 16."""
        ...
    @overload
    def compare_to(self, other: _Mat4f) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    @overload
    def compare_to(self, other: _Mat4f, threshold: float) -> int:
        """Sorts matrices lexicographically, componentwise.  Returns a number less
        than 0 if this matrix sorts before the other one, greater than zero if it
        sorts after, 0 if they are equivalent (within the indicated tolerance).
        """
        ...
    @overload
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def get_hash(self, threshold: float) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    @overload
    def add_hash(self, hash: int, threshold: float) -> int:
        """Adds the vector into the running hash."""
        ...
    def xform(self, v: _Vec4f) -> LVecBase4f:
        """4-component vector or point times matrix.  This is a fully general
        operation.
        """
        ...
    def xform_point(self, v: _Vec3f) -> LVecBase3f:
        """The matrix transforms a 3-component point (including translation component)
        and returns the result.  This assumes the matrix is an affine transform.
        """
        ...
    def xform_point_general(self, v: _Vec3f) -> LVecBase3f:
        """The matrix transforms a 3-component point (including translation component)
        and returns the result, as a fully general operation.
        """
        ...
    def xform_vec(self, v: _Vec3f) -> LVecBase3f:
        """The matrix transforms a 3-component vector (without translation component)
        and returns the result.  This assumes the matrix is an orthonormal
        transform.
        """
        ...
    def xform_vec_general(self, v: _Vec3f) -> LVecBase3f:
        """The matrix transforms a 3-component vector (without translation component)
        and returns the result, as a fully general operation.
        """
        ...
    def xform_in_place(self, v: _Vec4f) -> None:
        """4-component vector or point times matrix.  This is a fully general
        operation.
        """
        ...
    def xform_point_in_place(self, v: _Vec3f) -> None:
        """The matrix transforms a 3-component point (including translation
        component).  This assumes the matrix is an affine transform.
        """
        ...
    def xform_point_general_in_place(self, v: _Vec3f) -> None:
        """The matrix transforms a 3-component point (including translation
        component), as a fully general operation.
        """
        ...
    def xform_vec_in_place(self, v: _Vec3f) -> None:
        """The matrix transforms a 3-component vector (without translation component).
        This assumes the matrix is an orthonormal transform.
        """
        ...
    def xform_vec_general_in_place(self, v: _Vec3f) -> None:
        """The matrix transforms a 3-component vector (without translation component),
        as a fully general operation.
        """
        ...
    def multiply(self, other1: _Mat4f, other2: _Mat4f) -> None:
        """this = other1 * other2"""
        ...
    def componentwise_mult(self, other: _Mat4f) -> None: ...
    def transpose_from(self, other: _Mat4f) -> None: ...
    def transpose_in_place(self) -> None: ...
    def invert_from(self, other: _Mat4f) -> bool:
        """Computes the inverse of the other matrix, and stores the result in this
        matrix.  This is a fully general operation and makes no assumptions about
        the type of transform represented by the matrix.
        
        The other matrix must be a different object than this matrix.  However, if
        you need to invert a matrix in place, see invert_in_place.
        
        The return value is true if the matrix was successfully inverted, false if
        the was a singularity.
        """
        ...
    def invert_affine_from(self, other: _Mat4f) -> bool:
        """bugbug: we could optimize this for rotationscaletranslation matrices
        (transpose upper 3x3 and take negative of translation component)
        """
        ...
    def invert_in_place(self) -> bool:
        """Inverts the current matrix.  Returns true if the inverse is successful,
        false if the matrix was singular.
        """
        ...
    def accumulate(self, other: _Mat4f, weight: float) -> None:
        """Computes `(*this) += other * weight`."""
        ...
    @staticmethod
    def ident_mat() -> LMatrix4f:
        """Returns an identity matrix.
        
        This function definition must appear first, since some inline functions
        below take advantage of it.
        """
        ...
    @staticmethod
    def ones_mat() -> LMatrix4f:
        """Returns an matrix filled with ones."""
        ...
    @staticmethod
    def zeros_mat() -> LMatrix4f:
        """Returns an matrix filled with zeros."""
        ...
    def set_translate_mat(self, trans: _Vec3f) -> None:
        """Fills mat with a matrix that applies the indicated translation."""
        ...
    def set_rotate_mat(self, angle: float, axis: _Vec3f, cs: _CoordinateSystem = ...) -> None:
        """Sets mat to a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.
        """
        ...
    def set_rotate_mat_normaxis(self, angle: float, axis: _Vec3f, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.  Assumes axis has been
        prenormalized.
        """
        ...
    def set_scale_mat(self, scale: _Vec3f) -> None:
        """Fills mat with a matrix that applies the indicated scale in each of the
        three axes.
        """
        ...
    def set_shear_mat(self, shear: _Vec3f, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that applies the indicated shear in each of the
        three planes.
        """
        ...
    def set_scale_shear_mat(self, scale: _Vec3f, shear: _Vec3f, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that applies the indicated scale and shear."""
        ...
    @overload
    @staticmethod
    def translate_mat(trans: _Vec3f) -> LMatrix4f:
        """Returns a matrix that applies the indicated translation."""
        ...
    @overload
    @staticmethod
    def translate_mat(tx: float, ty: float, tz: float) -> LMatrix4f:
        """Returns a matrix that applies the indicated translation."""
        ...
    @staticmethod
    def rotate_mat(angle: float, axis: _Vec3f, cs: _CoordinateSystem = ...) -> LMatrix4f:
        """Returns a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.
        """
        ...
    @staticmethod
    def rotate_mat_normaxis(angle: float, axis: _Vec3f, cs: _CoordinateSystem = ...) -> LMatrix4f:
        """Returns a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.  Assumes axis has been
        prenormalized.
        """
        ...
    @overload
    @staticmethod
    def scale_mat(scale: _Vec3f | float) -> LMatrix4f:
        """Returns a matrix that applies the indicated scale in each of the three
        axes.
        """
        ...
    @overload
    @staticmethod
    def scale_mat(sx: float, sy: float, sz: float) -> LMatrix4f:
        """Returns a matrix that applies the indicated uniform scale."""
        ...
    @overload
    @staticmethod
    def shear_mat(shear: _Vec3f, cs: _CoordinateSystem = ...) -> LMatrix4f:
        """Returns a matrix that applies the indicated shear in each of the three
        planes.
        """
        ...
    @overload
    @staticmethod
    def shear_mat(shxy: float, shxz: float, shyz: float, cs: _CoordinateSystem = ...) -> LMatrix4f:
        """Returns a matrix that applies the indicated shear in each of the three
        planes.
        """
        ...
    @overload
    @staticmethod
    def scale_shear_mat(scale: _Vec3f, shear: _Vec3f, cs: _CoordinateSystem = ...) -> LMatrix4f:
        """Returns a matrix that applies the indicated scale and shear."""
        ...
    @overload
    @staticmethod
    def scale_shear_mat(sx: float, sy: float, sz: float, shxy: float, shxz: float, shyz: float, cs: _CoordinateSystem = ...) -> LMatrix4f:
        """Returns a matrix that applies the indicated scale and shear."""
        ...
    @staticmethod
    def y_to_z_up_mat() -> LMatrix4f:
        """Returns a matrix that transforms from the Y-up coordinate system to the
        Z-up coordinate system.
        """
        ...
    @staticmethod
    def z_to_y_up_mat() -> LMatrix4f:
        """Returns a matrix that transforms from the Y-up coordinate system to the
        Z-up coordinate system.
        """
        ...
    @staticmethod
    def convert_mat(_from: _CoordinateSystem, to: _CoordinateSystem) -> LMatrix4f:
        """Returns a matrix that transforms from the indicated coordinate system to
        the indicated coordinate system.
        """
        ...
    @overload
    def almost_equal(self, other: _Mat4f) -> bool:
        """Returns true if two matrices are memberwise equal within a default
        tolerance based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: _Mat4f, threshold: float) -> bool:
        """Returns true if two matrices are memberwise equal within a specified
        tolerance.  This is faster than the equivalence operator as this doesn't
        have to guarantee that it is transitive.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the matrix to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the matrix, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, scan: DatagramIterator) -> None:
        """Reads the matrix from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the matrix to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the matrix using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the matrix from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_rows(self) -> tuple[None, ...]: ...
    def get_cols(self) -> tuple[LVecBase4f, ...]: ...
    def get_row3s(self) -> tuple[None, ...]: ...
    setUpper3 = set_upper_3
    getUpper3 = get_upper_3
    setRow = set_row
    setCol = set_col
    getRow = get_row
    getCol = get_col
    getRow3 = get_row3
    getCol3 = get_col3
    isNan = is_nan
    isIdentity = is_identity
    getCell = get_cell
    setCell = set_cell
    getNumComponents = get_num_components
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    xformPoint = xform_point
    xformPointGeneral = xform_point_general
    xformVec = xform_vec
    xformVecGeneral = xform_vec_general
    xformInPlace = xform_in_place
    xformPointInPlace = xform_point_in_place
    xformPointGeneralInPlace = xform_point_general_in_place
    xformVecInPlace = xform_vec_in_place
    xformVecGeneralInPlace = xform_vec_general_in_place
    componentwiseMult = componentwise_mult
    transposeFrom = transpose_from
    transposeInPlace = transpose_in_place
    invertFrom = invert_from
    invertAffineFrom = invert_affine_from
    invertInPlace = invert_in_place
    identMat = ident_mat
    onesMat = ones_mat
    zerosMat = zeros_mat
    setTranslateMat = set_translate_mat
    setRotateMat = set_rotate_mat
    setRotateMatNormaxis = set_rotate_mat_normaxis
    setScaleMat = set_scale_mat
    setShearMat = set_shear_mat
    setScaleShearMat = set_scale_shear_mat
    translateMat = translate_mat
    rotateMat = rotate_mat
    rotateMatNormaxis = rotate_mat_normaxis
    scaleMat = scale_mat
    shearMat = shear_mat
    scaleShearMat = scale_shear_mat
    yToZUpMat = y_to_z_up_mat
    zToYUpMat = z_to_y_up_mat
    convertMat = convert_mat
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type
    getRows = get_rows
    getCols = get_cols
    getRow3s = get_row3s

class UnalignedLMatrix4f:
    """This is an "unaligned" LMatrix4.  It has no functionality other than to
    store numbers, and it will pack them in as tightly as possible, avoiding
    any SSE2 alignment requirements shared by the primary LMatrix4 class.
    
    Use it only when you need to pack numbers tightly without respect to
    alignment, and then copy it to a proper LMatrix4 to get actual use from it.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    num_components: ClassVar[Literal[16]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Mat4f) -> None: ...
    @overload
    def __init__(self, e00: float, e01: float, e02: float, e03: float, e10: float, e11: float, e12: float, e13: float, e20: float, e21: float, e22: float, e23: float, e30: float, e31: float, e32: float, e33: float) -> None: ...
    def __call__(self, row: int, col: int) -> float | None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def assign(self, copy: _Mat4f) -> UnalignedLMatrix4f: ...
    def set(self, e00: float, e01: float, e02: float, e03: float, e10: float, e11: float, e12: float, e13: float, e20: float, e21: float, e22: float, e23: float, e30: float, e31: float, e32: float, e33: float) -> None: ...
    def get_num_components(self) -> int:
        """Returns the number of elements in the matrix, sixteen."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNumComponents = get_num_components
    getClassType = get_class_type

class LMatrix3d:
    """This is a 3-by-3 transform matrix.  It typically will represent either a
    rotation-and-scale (no translation) matrix in 3-d, or a full affine matrix
    (rotation, scale, translation) in 2-d, e.g.  for a texture matrix.
    """
    class Row:
        """These helper classes are used to support two-level operator []."""
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: LMatrix3d.Row) -> None: ...
        @overload
        def __getitem__(self, i: int) -> float: ...
        @overload
        def __getitem__(self, i: int, assign_val: float) -> None: ...
        @staticmethod
        def __len__() -> int:
            """Returns 3: the number of columns of a LMatrix3."""
            ...
        def operator_typecast(self) -> LVecBase3d: ...
        operatorTypecast = operator_typecast
    class CRow:
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: LMatrix3d.CRow) -> None: ...
        def __getitem__(self, i: int) -> float: ...
        @staticmethod
        def __len__() -> int:
            """Returns 3: the number of columns of a LMatrix3."""
            ...
        def operator_typecast(self) -> LVecBase3d: ...
        operatorTypecast = operator_typecast
    DtoolClassDict: ClassVar[dict[str, Any]]
    num_components: ClassVar[Literal[9]]
    is_int: ClassVar[Literal[0]]
    @property
    def rows(self) -> Sequence[LVecBase3d]: ...
    @property
    def cols(self) -> Sequence[LVecBase3d]: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: LMatrix3d) -> None: ...
    @overload
    def __init__(self, __param0: _Vec3d, __param1: _Vec3d, __param2: _Vec3d) -> None:
        """Constructs the matrix from three individual rows."""
        ...
    @overload
    def __init__(self, __param0: float, __param1: float, __param2: float, __param3: float, __param4: float, __param5: float, __param6: float, __param7: float, __param8: float) -> None: ...
    def __getitem__(self, i: int) -> LMatrix3d.CRow | LMatrix3d.Row: ...
    @staticmethod
    def __len__() -> int:
        """Returns 3: the number of rows of a LMatrix3."""
        ...
    def __call__(self, row: int, col: int) -> float | None: ...
    def __lt__(self, other: LMatrix3d) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    @overload
    def __mul__(self, other: LMatrix3d) -> LMatrix3d: ...
    @overload
    def __mul__(self, scalar: float) -> LMatrix3d: ...
    def __truediv__(self, scalar: float) -> LMatrix3d: ...
    def __iadd__(self, other: LMatrix3d) -> LMatrix3d:
        """Performs a memberwise addition between two matrices."""
        ...
    def __isub__(self, other: LMatrix3d) -> LMatrix3d:
        """Performs a memberwise subtraction between two matrices."""
        ...
    @overload
    def __imul__(self, other: LMatrix3d) -> LMatrix3d: ...
    @overload
    def __imul__(self, scalar: float) -> LMatrix3d:
        """Performs a memberwise scale."""
        ...
    def __itruediv__(self, scalar: float) -> LMatrix3d:
        """Performs a memberwise scale."""
        ...
    def __le__(self, other: LMatrix3d) -> bool: ...
    @overload
    def assign(self, other: LMatrix3d) -> LMatrix3d: ...
    @overload
    def assign(self, fill_value: float) -> LMatrix3d: ...
    def fill(self, fill_value: float) -> None:
        """Sets each element of the matrix to the indicated fill_value.  This is of
        questionable value, but is sometimes useful when initializing to zero.
        """
        ...
    def set(self, e00: float, e01: float, e02: float, e10: float, e11: float, e12: float, e20: float, e21: float, e22: float) -> None: ...
    def set_row(self, row: int, v: LVecBase2d | _Vec3d) -> None:
        """Replaces the indicated row of the matrix from a two-component vector,
        ignoring the last column.
        """
        ...
    def set_col(self, col: int, v: LVecBase2d | _Vec3d) -> None:
        """Replaces the indicated column of the matrix from a two-component vector,
        ignoring the last row.
        """
        ...
    @overload
    def get_row(self, row: int) -> LVecBase3d:
        """Stores the indicated row of the matrix as a three-component vector."""
        ...
    @overload
    def get_row(self, result_vec: _Vec3d, row: int) -> None:
        """Returns the indicated row of the matrix as a three-component vector."""
        ...
    def get_col(self, col: int) -> LVecBase3d:
        """Returns the indicated column of the matrix as a three-component vector."""
        ...
    def get_row2(self, row: int) -> LVecBase2d:
        """Returns the indicated row of the matrix as a two-component vector, ignoring
        the last column.
        """
        ...
    def get_col2(self, col: int) -> LVecBase2d:
        """Returns the indicated column of the matrix as a two-component vector,
        ignoring the last row.
        """
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the matrix is not-a-number, false
        otherwise.
        """
        ...
    def is_identity(self) -> bool:
        """Returns true if this is (close enough to) the identity matrix, false
        otherwise.
        """
        ...
    def get_cell(self, row: int, col: int) -> float:
        """Returns a particular element of the matrix."""
        ...
    def set_cell(self, row: int, col: int, value: float) -> None:
        """Changes a particular element of the matrix."""
        ...
    def get_num_components(self) -> int:
        """Returns the number of elements in the matrix, nine."""
        ...
    @overload
    def compare_to(self, other: LMatrix3d) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    @overload
    def compare_to(self, other: LMatrix3d, threshold: float) -> int:
        """Sorts matrices lexicographically, componentwise.  Returns a number less
        than 0 if this matrix sorts before the other one, greater than zero if it
        sorts after, 0 if they are equivalent (within the indicated tolerance).
        """
        ...
    @overload
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def get_hash(self, threshold: float) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    @overload
    def add_hash(self, hash: int, threshold: float) -> int:
        """Adds the vector into the running hash."""
        ...
    def xform(self, v: _Vec3d) -> LVecBase3d:
        """3-component vector or point times matrix."""
        ...
    def xform_point(self, v: LVecBase2d) -> LVecBase2d:
        """The matrix transforms a 2-component point (including translation component)
        and returns the result.  This assumes the matrix is an affine transform.
        """
        ...
    @overload
    def xform_vec(self, v: LVecBase2d) -> LVecBase2d:
        """The matrix transforms a 2-component vector (without translation component)
        and returns the result.  This assumes the matrix is an affine transform.
        """
        ...
    @overload
    def xform_vec(self, v: _Vec3d) -> LVecBase3d:
        """The matrix transforms a 3-component vector and returns the result.  This
        assumes the matrix is an orthonormal transform.
        
        In practice, this is the same computation as xform().
        """
        ...
    def xform_vec_general(self, v: _Vec3d) -> LVecBase3d:
        """The matrix transforms a 3-component vector (without translation component)
        and returns the result, as a fully general operation.
        """
        ...
    def xform_in_place(self, v: _Vec3d) -> None:
        """3-component vector or point times matrix."""
        ...
    def xform_point_in_place(self, v: LVecBase2d) -> None:
        """The matrix transforms a 2-component point (including translation
        component).  This assumes the matrix is an affine transform.
        """
        ...
    def xform_vec_in_place(self, v: LVecBase2d | _Vec3d) -> None:
        """The matrix transforms a 2-component vector (without translation component).
        This assumes the matrix is an affine transform.
        """
        ...
    def xform_vec_general_in_place(self, v: _Vec3d) -> None:
        """The matrix transforms a 3-component vector (without translation component),
        as a fully general operation.
        """
        ...
    def multiply(self, other1: LMatrix3d, other2: LMatrix3d) -> None:
        """this = other1 * other2"""
        ...
    def componentwise_mult(self, other: LMatrix3d) -> None: ...
    def determinant(self) -> float:
        """Returns the determinant of the matrix."""
        ...
    def transpose_from(self, other: LMatrix3d) -> None: ...
    def transpose_in_place(self) -> None: ...
    def invert_from(self, other: LMatrix3d) -> bool:
        """Computes the inverse of the other matrix, and stores the result in this
        matrix.  This is a fully general operation and makes no assumptions about
        the type of transform represented by the matrix.
        
        The other matrix must be a different object than this matrix.  However, if
        you need to invert a matrix in place, see invert_in_place.
        
        The return value is true if the matrix was successfully inverted, false if
        there was a singularity.
        """
        ...
    def invert_in_place(self) -> bool:
        """Inverts the current matrix.  Returns true if the inverse is successful,
        false if the matrix was singular.
        """
        ...
    def invert_transpose_from(self, other: LMatrix3d | _Mat4d) -> bool:
        """Simultaneously computes the inverse of the indicated matrix, and then the
        transpose of that inverse.
        """
        ...
    @staticmethod
    def ident_mat() -> LMatrix3d:
        """Returns an identity matrix.
        
        This function definition must appear first, since some inline functions
        below take advantage of it.
        """
        ...
    def set_translate_mat(self, trans: LVecBase2d) -> None:
        """Fills mat with a matrix that applies the indicated translation."""
        ...
    @overload
    def set_rotate_mat(self, angle: float) -> None:
        """Fills mat with a matrix that rotates by the given angle in degrees
        counterclockwise.
        """
        ...
    @overload
    def set_rotate_mat(self, angle: float, axis: _Vec3d, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.
        """
        ...
    def set_scale_mat(self, scale: LVecBase2d | _Vec3d) -> None:
        """Fills mat with a matrix that applies the indicated scale in each of the two
        axes.
        """
        ...
    @overload
    @staticmethod
    def translate_mat(trans: LVecBase2d) -> LMatrix3d:
        """Returns a matrix that applies the indicated translation."""
        ...
    @overload
    @staticmethod
    def translate_mat(tx: float, ty: float) -> LMatrix3d:
        """Returns a matrix that applies the indicated translation."""
        ...
    @overload
    @staticmethod
    def rotate_mat(angle: float) -> LMatrix3d:
        """Returns a matrix that rotates by the given angle in degrees
        counterclockwise.
        """
        ...
    @overload
    @staticmethod
    def rotate_mat(angle: float, axis: _Vec3d, cs: _CoordinateSystem = ...) -> LMatrix3d:
        """Returns a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.
        """
        ...
    @overload
    @staticmethod
    def scale_mat(scale: LVecBase2d | _Vec3d) -> LMatrix3d:
        """Returns a matrix that applies the indicated scale in each of the two axes."""
        ...
    @overload
    @staticmethod
    def scale_mat(sx: float, sy: float) -> LMatrix3d:
        """Returns a matrix that applies the indicated scale in each of the three
        axes.
        """
        ...
    @overload
    @staticmethod
    def scale_mat(sx: float, sy: float, sz: float) -> LMatrix3d:
        """Returns a matrix that applies the indicated scale in each of the two axes."""
        ...
    def set_rotate_mat_normaxis(self, angle: float, axis: _Vec3d, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.  Assumes axis has been
        normalized.
        """
        ...
    @staticmethod
    def rotate_mat_normaxis(angle: float, axis: _Vec3d, cs: _CoordinateSystem = ...) -> LMatrix3d:
        """Returns a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.  Assumes axis has been
        normalized.
        """
        ...
    def set_shear_mat(self, shear: _Vec3d, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that applies the indicated shear in each of the
        three planes.
        """
        ...
    @overload
    @staticmethod
    def shear_mat(shear: _Vec3d, cs: _CoordinateSystem = ...) -> LMatrix3d:
        """Returns a matrix that applies the indicated shear in each of the three
        planes.
        """
        ...
    @overload
    @staticmethod
    def shear_mat(shxy: float, shxz: float, shyz: float, cs: _CoordinateSystem = ...) -> LMatrix3d:
        """Returns a matrix that applies the indicated shear in each of the three
        planes.
        """
        ...
    def set_scale_shear_mat(self, scale: _Vec3d, shear: _Vec3d, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that applies the indicated scale and shear."""
        ...
    @overload
    @staticmethod
    def scale_shear_mat(scale: _Vec3d, shear: _Vec3d, cs: _CoordinateSystem = ...) -> LMatrix3d:
        """Returns a matrix that applies the indicated scale and shear."""
        ...
    @overload
    @staticmethod
    def scale_shear_mat(sx: float, sy: float, sz: float, shxy: float, shxz: float, shyz: float, cs: _CoordinateSystem = ...) -> LMatrix3d:
        """Returns a matrix that applies the indicated scale and shear."""
        ...
    @staticmethod
    def convert_mat(_from: _CoordinateSystem, to: _CoordinateSystem) -> LMatrix3d:
        """Returns a matrix that transforms from the indicated coordinate system to
        the indicated coordinate system.
        """
        ...
    @overload
    def almost_equal(self, other: LMatrix3d) -> bool:
        """Returns true if two matrices are memberwise equal within a default
        tolerance based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: LMatrix3d, threshold: float) -> bool:
        """Returns true if two matrices are memberwise equal within a specified
        tolerance.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the matrix to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the matrix, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, scan: DatagramIterator) -> None:
        """Reads the matrix from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the matrix to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the matrix using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the matrix from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_rows(self) -> tuple[None, ...]: ...
    def get_cols(self) -> tuple[LVecBase3d, ...]: ...
    def get_col2s(self) -> tuple[LVecBase2d, ...]: ...
    def get_row2s(self) -> tuple[LVecBase2d, ...]: ...
    setRow = set_row
    setCol = set_col
    getRow = get_row
    getCol = get_col
    getRow2 = get_row2
    getCol2 = get_col2
    isNan = is_nan
    isIdentity = is_identity
    getCell = get_cell
    setCell = set_cell
    getNumComponents = get_num_components
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    xformPoint = xform_point
    xformVec = xform_vec
    xformVecGeneral = xform_vec_general
    xformInPlace = xform_in_place
    xformPointInPlace = xform_point_in_place
    xformVecInPlace = xform_vec_in_place
    xformVecGeneralInPlace = xform_vec_general_in_place
    componentwiseMult = componentwise_mult
    transposeFrom = transpose_from
    transposeInPlace = transpose_in_place
    invertFrom = invert_from
    invertInPlace = invert_in_place
    invertTransposeFrom = invert_transpose_from
    identMat = ident_mat
    setTranslateMat = set_translate_mat
    setRotateMat = set_rotate_mat
    setScaleMat = set_scale_mat
    translateMat = translate_mat
    rotateMat = rotate_mat
    scaleMat = scale_mat
    setRotateMatNormaxis = set_rotate_mat_normaxis
    rotateMatNormaxis = rotate_mat_normaxis
    setShearMat = set_shear_mat
    shearMat = shear_mat
    setScaleShearMat = set_scale_shear_mat
    scaleShearMat = scale_shear_mat
    convertMat = convert_mat
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type
    getRows = get_rows
    getCols = get_cols
    getCol2s = get_col2s
    getRow2s = get_row2s

class LMatrix4d:
    """This is a 4-by-4 transform matrix."""
    class Row:
        """These helper classes are used to support two-level operator []."""
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: LMatrix4d.Row) -> None: ...
        @overload
        def __getitem__(self, i: int) -> float: ...
        @overload
        def __getitem__(self, i: int, assign_val: float) -> None: ...
        @staticmethod
        def __len__() -> int:
            """Returns 4: the number of columns of a LMatrix4."""
            ...
        def operator_typecast(self) -> LVecBase4d: ...
        operatorTypecast = operator_typecast
    class CRow:
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: LMatrix4d.CRow) -> None: ...
        def __getitem__(self, i: int) -> float: ...
        @staticmethod
        def __len__() -> int:
            """Returns 4: the number of columns of a LMatrix4."""
            ...
        def operator_typecast(self) -> LVecBase4d: ...
        operatorTypecast = operator_typecast
    DtoolClassDict: ClassVar[dict[str, Any]]
    num_components: ClassVar[Literal[16]]
    is_int: ClassVar[Literal[0]]
    @property
    def rows(self) -> Sequence[LVecBase4d]: ...
    @property
    def cols(self) -> Sequence[LVecBase4d]: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, upper3: LMatrix3d) -> None:
        """Construct a 4x4 matrix given a 3x3 rotation matrix and an optional
        translation component.
        """
        ...
    @overload
    def __init__(self, other: _Mat4d) -> None: ...
    @overload
    def __init__(self, upper3: LMatrix3d, trans: _Vec3d) -> None: ...
    @overload
    def __init__(self, __param0: _Vec4d, __param1: _Vec4d, __param2: _Vec4d, __param3: _Vec4d) -> None:
        """Constructs the matrix from four individual rows."""
        ...
    @overload
    def __init__(self, __param0: float, __param1: float, __param2: float, __param3: float, __param4: float, __param5: float, __param6: float, __param7: float, __param8: float, __param9: float, __param10: float, __param11: float, __param12: float, __param13: float, __param14: float, __param15: float) -> None: ...
    def __getitem__(self, i: int) -> LMatrix4d.CRow | LMatrix4d.Row: ...
    @staticmethod
    def __len__() -> int:
        """Returns 4: the number of rows of a LMatrix4."""
        ...
    def __call__(self, row: int, col: int) -> float | None: ...
    def __lt__(self, other: _Mat4d) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    @overload
    def __mul__(self, other: _Mat4d) -> LMatrix4d: ...
    @overload
    def __mul__(self, scalar: float) -> LMatrix4d: ...
    def __truediv__(self, scalar: float) -> LMatrix4d: ...
    def __iadd__(self, other: _Mat4d) -> LMatrix4d:
        """Performs a memberwise addition between two matrices."""
        ...
    def __isub__(self, other: _Mat4d) -> LMatrix4d:
        """Performs a memberwise subtraction between two matrices."""
        ...
    @overload
    def __imul__(self, other: _Mat4d) -> LMatrix4d: ...
    @overload
    def __imul__(self, scalar: float) -> LMatrix4d: ...
    def __itruediv__(self, scalar: float) -> LMatrix4d: ...
    def __le__(self, other: _Mat4d) -> bool: ...
    @overload
    def assign(self, other: _Mat4d) -> LMatrix4d: ...
    @overload
    def assign(self, fill_value: float) -> LMatrix4d: ...
    def fill(self, fill_value: float) -> None:
        """Sets each element of the matrix to the indicated fill_value.  This is of
        questionable value, but is sometimes useful when initializing to zero.
        """
        ...
    def set(self, e00: float, e01: float, e02: float, e03: float, e10: float, e11: float, e12: float, e13: float, e20: float, e21: float, e22: float, e23: float, e30: float, e31: float, e32: float, e33: float) -> None: ...
    def set_upper_3(self, upper3: LMatrix3d) -> None:
        """Get and set the upper 3x3 rotation matrix."""
        ...
    def get_upper_3(self) -> LMatrix3d:
        """Retrieves the upper 3x3 submatrix."""
        ...
    def set_row(self, row: int, v: _Vec3d | _Vec4d) -> None:
        """Replaces the indicated row of the matrix with the indicated 3-component
        vector, ignoring the last column.
        """
        ...
    def set_col(self, col: int, v: _Vec3d | _Vec4d) -> None:
        """Replaces the indicated column of the matrix with the indicated 3-component
        vector, ignoring the last row.
        """
        ...
    @overload
    def get_row(self, row: int) -> LVecBase4d:
        """Stores the indicated row of the matrix as a 4-component vector."""
        ...
    @overload
    def get_row(self, result_vec: _Vec4d, row: int) -> None:
        """Retrieves the indicated row of the matrix as a 4-component vector."""
        ...
    def get_col(self, col: int) -> LVecBase4d:
        """Retrieves the indicated column of the matrix as a 4-component vector."""
        ...
    @overload
    def get_row3(self, row: int) -> LVecBase3d:
        """Stores the row column of the matrix as a 3-component vector, ignoring the
        last column.
        """
        ...
    @overload
    def get_row3(self, result_vec: _Vec3d, row: int) -> None:
        """Retrieves the row column of the matrix as a 3-component vector, ignoring
        the last column.
        """
        ...
    def get_col3(self, col: int) -> LVecBase3d:
        """Retrieves the indicated column of the matrix as a 3-component vector,
        ignoring the last row.
        """
        ...
    def is_nan(self) -> bool:
        """Returns true if any component of the matrix is not-a-number, false
        otherwise.
        """
        ...
    def is_identity(self) -> bool:
        """Returns true if this is (close enough to) the identity matrix, false
        otherwise.
        """
        ...
    def get_cell(self, row: int, col: int) -> float:
        """Returns a particular element of the matrix."""
        ...
    def set_cell(self, row: int, col: int, value: float) -> None:
        """Changes a particular element of the matrix."""
        ...
    def get_num_components(self) -> int:
        """Returns the number of elements in the matrix, 16."""
        ...
    @overload
    def compare_to(self, other: _Mat4d) -> int:
        """This flavor of compare_to uses a default threshold value based on the
        numeric type.
        """
        ...
    @overload
    def compare_to(self, other: _Mat4d, threshold: float) -> int:
        """Sorts matrices lexicographically, componentwise.  Returns a number less
        than 0 if this matrix sorts before the other one, greater than zero if it
        sorts after, 0 if they are equivalent (within the indicated tolerance).
        """
        ...
    @overload
    def get_hash(self) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def get_hash(self, threshold: float) -> int:
        """Returns a suitable hash for phash_map."""
        ...
    @overload
    def add_hash(self, hash: int) -> int:
        """Adds the vector into the running hash."""
        ...
    @overload
    def add_hash(self, hash: int, threshold: float) -> int:
        """Adds the vector into the running hash."""
        ...
    def xform(self, v: _Vec4d) -> LVecBase4d:
        """4-component vector or point times matrix.  This is a fully general
        operation.
        """
        ...
    def xform_point(self, v: _Vec3d) -> LVecBase3d:
        """The matrix transforms a 3-component point (including translation component)
        and returns the result.  This assumes the matrix is an affine transform.
        """
        ...
    def xform_point_general(self, v: _Vec3d) -> LVecBase3d:
        """The matrix transforms a 3-component point (including translation component)
        and returns the result, as a fully general operation.
        """
        ...
    def xform_vec(self, v: _Vec3d) -> LVecBase3d:
        """The matrix transforms a 3-component vector (without translation component)
        and returns the result.  This assumes the matrix is an orthonormal
        transform.
        """
        ...
    def xform_vec_general(self, v: _Vec3d) -> LVecBase3d:
        """The matrix transforms a 3-component vector (without translation component)
        and returns the result, as a fully general operation.
        """
        ...
    def xform_in_place(self, v: _Vec4d) -> None:
        """4-component vector or point times matrix.  This is a fully general
        operation.
        """
        ...
    def xform_point_in_place(self, v: _Vec3d) -> None:
        """The matrix transforms a 3-component point (including translation
        component).  This assumes the matrix is an affine transform.
        """
        ...
    def xform_point_general_in_place(self, v: _Vec3d) -> None:
        """The matrix transforms a 3-component point (including translation
        component), as a fully general operation.
        """
        ...
    def xform_vec_in_place(self, v: _Vec3d) -> None:
        """The matrix transforms a 3-component vector (without translation component).
        This assumes the matrix is an orthonormal transform.
        """
        ...
    def xform_vec_general_in_place(self, v: _Vec3d) -> None:
        """The matrix transforms a 3-component vector (without translation component),
        as a fully general operation.
        """
        ...
    def multiply(self, other1: _Mat4d, other2: _Mat4d) -> None:
        """this = other1 * other2"""
        ...
    def componentwise_mult(self, other: _Mat4d) -> None: ...
    def transpose_from(self, other: _Mat4d) -> None: ...
    def transpose_in_place(self) -> None: ...
    def invert_from(self, other: _Mat4d) -> bool:
        """Computes the inverse of the other matrix, and stores the result in this
        matrix.  This is a fully general operation and makes no assumptions about
        the type of transform represented by the matrix.
        
        The other matrix must be a different object than this matrix.  However, if
        you need to invert a matrix in place, see invert_in_place.
        
        The return value is true if the matrix was successfully inverted, false if
        the was a singularity.
        """
        ...
    def invert_affine_from(self, other: _Mat4d) -> bool:
        """bugbug: we could optimize this for rotationscaletranslation matrices
        (transpose upper 3x3 and take negative of translation component)
        """
        ...
    def invert_in_place(self) -> bool:
        """Inverts the current matrix.  Returns true if the inverse is successful,
        false if the matrix was singular.
        """
        ...
    def accumulate(self, other: _Mat4d, weight: float) -> None:
        """Computes `(*this) += other * weight`."""
        ...
    @staticmethod
    def ident_mat() -> LMatrix4d:
        """Returns an identity matrix.
        
        This function definition must appear first, since some inline functions
        below take advantage of it.
        """
        ...
    @staticmethod
    def ones_mat() -> LMatrix4d:
        """Returns an matrix filled with ones."""
        ...
    @staticmethod
    def zeros_mat() -> LMatrix4d:
        """Returns an matrix filled with zeros."""
        ...
    def set_translate_mat(self, trans: _Vec3d) -> None:
        """Fills mat with a matrix that applies the indicated translation."""
        ...
    def set_rotate_mat(self, angle: float, axis: _Vec3d, cs: _CoordinateSystem = ...) -> None:
        """Sets mat to a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.
        """
        ...
    def set_rotate_mat_normaxis(self, angle: float, axis: _Vec3d, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.  Assumes axis has been
        prenormalized.
        """
        ...
    def set_scale_mat(self, scale: _Vec3d) -> None:
        """Fills mat with a matrix that applies the indicated scale in each of the
        three axes.
        """
        ...
    def set_shear_mat(self, shear: _Vec3d, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that applies the indicated shear in each of the
        three planes.
        """
        ...
    def set_scale_shear_mat(self, scale: _Vec3d, shear: _Vec3d, cs: _CoordinateSystem = ...) -> None:
        """Fills mat with a matrix that applies the indicated scale and shear."""
        ...
    @overload
    @staticmethod
    def translate_mat(trans: _Vec3d) -> LMatrix4d:
        """Returns a matrix that applies the indicated translation."""
        ...
    @overload
    @staticmethod
    def translate_mat(tx: float, ty: float, tz: float) -> LMatrix4d:
        """Returns a matrix that applies the indicated translation."""
        ...
    @staticmethod
    def rotate_mat(angle: float, axis: _Vec3d, cs: _CoordinateSystem = ...) -> LMatrix4d:
        """Returns a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.
        """
        ...
    @staticmethod
    def rotate_mat_normaxis(angle: float, axis: _Vec3d, cs: _CoordinateSystem = ...) -> LMatrix4d:
        """Returns a matrix that rotates by the given angle in degrees
        counterclockwise about the indicated vector.  Assumes axis has been
        prenormalized.
        """
        ...
    @overload
    @staticmethod
    def scale_mat(scale: _Vec3d | float) -> LMatrix4d:
        """Returns a matrix that applies the indicated scale in each of the three
        axes.
        """
        ...
    @overload
    @staticmethod
    def scale_mat(sx: float, sy: float, sz: float) -> LMatrix4d:
        """Returns a matrix that applies the indicated uniform scale."""
        ...
    @overload
    @staticmethod
    def shear_mat(shear: _Vec3d, cs: _CoordinateSystem = ...) -> LMatrix4d:
        """Returns a matrix that applies the indicated shear in each of the three
        planes.
        """
        ...
    @overload
    @staticmethod
    def shear_mat(shxy: float, shxz: float, shyz: float, cs: _CoordinateSystem = ...) -> LMatrix4d:
        """Returns a matrix that applies the indicated shear in each of the three
        planes.
        """
        ...
    @overload
    @staticmethod
    def scale_shear_mat(scale: _Vec3d, shear: _Vec3d, cs: _CoordinateSystem = ...) -> LMatrix4d:
        """Returns a matrix that applies the indicated scale and shear."""
        ...
    @overload
    @staticmethod
    def scale_shear_mat(sx: float, sy: float, sz: float, shxy: float, shxz: float, shyz: float, cs: _CoordinateSystem = ...) -> LMatrix4d:
        """Returns a matrix that applies the indicated scale and shear."""
        ...
    @staticmethod
    def y_to_z_up_mat() -> LMatrix4d:
        """Returns a matrix that transforms from the Y-up coordinate system to the
        Z-up coordinate system.
        """
        ...
    @staticmethod
    def z_to_y_up_mat() -> LMatrix4d:
        """Returns a matrix that transforms from the Y-up coordinate system to the
        Z-up coordinate system.
        """
        ...
    @staticmethod
    def convert_mat(_from: _CoordinateSystem, to: _CoordinateSystem) -> LMatrix4d:
        """Returns a matrix that transforms from the indicated coordinate system to
        the indicated coordinate system.
        """
        ...
    @overload
    def almost_equal(self, other: _Mat4d) -> bool:
        """Returns true if two matrices are memberwise equal within a default
        tolerance based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: _Mat4d, threshold: float) -> bool:
        """Returns true if two matrices are memberwise equal within a specified
        tolerance.  This is faster than the equivalence operator as this doesn't
        have to guarantee that it is transitive.
        """
        ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the matrix to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the matrix, regardless of the setting of
        Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
        ...
    def read_datagram_fixed(self, scan: DatagramIterator) -> None:
        """Reads the matrix from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
        ...
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the matrix to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the matrix using the standard width
        setting, especially when you are writing a bam file.
        """
        ...
    def read_datagram(self, source: DatagramIterator) -> None:
        """Reads the matrix from the Datagram using get_stdfloat()."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_rows(self) -> tuple[None, ...]: ...
    def get_cols(self) -> tuple[LVecBase4d, ...]: ...
    def get_row3s(self) -> tuple[None, ...]: ...
    setUpper3 = set_upper_3
    getUpper3 = get_upper_3
    setRow = set_row
    setCol = set_col
    getRow = get_row
    getCol = get_col
    getRow3 = get_row3
    getCol3 = get_col3
    isNan = is_nan
    isIdentity = is_identity
    getCell = get_cell
    setCell = set_cell
    getNumComponents = get_num_components
    compareTo = compare_to
    getHash = get_hash
    addHash = add_hash
    xformPoint = xform_point
    xformPointGeneral = xform_point_general
    xformVec = xform_vec
    xformVecGeneral = xform_vec_general
    xformInPlace = xform_in_place
    xformPointInPlace = xform_point_in_place
    xformPointGeneralInPlace = xform_point_general_in_place
    xformVecInPlace = xform_vec_in_place
    xformVecGeneralInPlace = xform_vec_general_in_place
    componentwiseMult = componentwise_mult
    transposeFrom = transpose_from
    transposeInPlace = transpose_in_place
    invertFrom = invert_from
    invertAffineFrom = invert_affine_from
    invertInPlace = invert_in_place
    identMat = ident_mat
    onesMat = ones_mat
    zerosMat = zeros_mat
    setTranslateMat = set_translate_mat
    setRotateMat = set_rotate_mat
    setRotateMatNormaxis = set_rotate_mat_normaxis
    setScaleMat = set_scale_mat
    setShearMat = set_shear_mat
    setScaleShearMat = set_scale_shear_mat
    translateMat = translate_mat
    rotateMat = rotate_mat
    rotateMatNormaxis = rotate_mat_normaxis
    scaleMat = scale_mat
    shearMat = shear_mat
    scaleShearMat = scale_shear_mat
    yToZUpMat = y_to_z_up_mat
    zToYUpMat = z_to_y_up_mat
    convertMat = convert_mat
    almostEqual = almost_equal
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram
    getClassType = get_class_type
    getRows = get_rows
    getCols = get_cols
    getRow3s = get_row3s

class UnalignedLMatrix4d:
    """This is an "unaligned" LMatrix4.  It has no functionality other than to
    store numbers, and it will pack them in as tightly as possible, avoiding
    any SSE2 alignment requirements shared by the primary LMatrix4 class.
    
    Use it only when you need to pack numbers tightly without respect to
    alignment, and then copy it to a proper LMatrix4 to get actual use from it.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    num_components: ClassVar[Literal[16]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Mat4d) -> None: ...
    @overload
    def __init__(self, e00: float, e01: float, e02: float, e03: float, e10: float, e11: float, e12: float, e13: float, e20: float, e21: float, e22: float, e23: float, e30: float, e31: float, e32: float, e33: float) -> None: ...
    def __call__(self, row: int, col: int) -> float | None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def assign(self, copy: _Mat4d) -> UnalignedLMatrix4d: ...
    def set(self, e00: float, e01: float, e02: float, e03: float, e10: float, e11: float, e12: float, e13: float, e20: float, e21: float, e22: float, e23: float, e30: float, e31: float, e32: float, e33: float) -> None: ...
    def get_num_components(self) -> int:
        """Returns the number of elements in the matrix, sixteen."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getNumComponents = get_num_components
    getClassType = get_class_type

class LQuaternionf(LVecBase4f):
    """This is the base quaternion class"""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec4f) -> None: ...
    @overload
    def __init__(self, r: float, copy: _Vec3f) -> None: ...
    @overload
    def __init__(self, r: float, i: float, j: float, k: float) -> None: ...
    def __neg__(self) -> LQuaternionf: ...
    def __add__(self, other: _Vec4f) -> LQuaternionf: ...
    def __sub__(self, other: _Vec4f) -> LQuaternionf: ...
    @overload
    def __mul__(self, __param0: LMatrix3f) -> LMatrix3f: ...
    @overload
    def __mul__(self, __param0: _Mat4f) -> LMatrix4f: ...
    @overload
    def __mul__(self, __param0: _Vec4f) -> LQuaternionf: ...
    @overload
    def __mul__(self, scalar: float) -> LQuaternionf: ...
    def __truediv__(self, scalar: float) -> LQuaternionf: ...
    def __imul__(self, __param0: _Vec4f) -> LQuaternionf: ...
    def __pow__(self, __param0: float) -> LQuaternionf:
        """Returns a new quaternion that represents this quaternion raised to the
        given power.
        """
        ...
    @staticmethod
    def pure_imaginary(v: _Vec3f) -> LQuaternionf: ...
    def conjugate(self) -> LQuaternionf:
        """Returns the complex conjugate of this quat."""
        ...
    @overload
    def xform(self, v: _Vec3f) -> LVecBase3f:
        """Transforms a 3-d vector by the indicated rotation"""
        ...
    @overload
    def xform(self, v: _Vec4f) -> LVecBase4f:
        """Transforms a 4-d vector by the indicated rotation"""
        ...
    def multiply(self, rhs: _Vec4f) -> LQuaternionf:
        """actual multiply call (non virtual)"""
        ...
    def angle_rad(self, other: _Vec4f) -> float:
        """Returns the angle between the orientation represented by this quaternion
        and the other one, expressed in radians.
        """
        ...
    def angle_deg(self, other: _Vec4f) -> float:
        """Returns the angle between the orientation represented by this quaternion
        and the other one, expressed in degrees.
        """
        ...
    @overload
    def almost_equal(self, other: _Vec4f) -> bool:
        """Returns true if two quaternions are memberwise equal within a default
        tolerance based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: _Vec4f, threshold: float) -> bool:
        """Returns true if two quaternions are memberwise equal within a specified
        tolerance.
        """
        ...
    def is_same_direction(self, other: _Vec4f) -> bool:
        """Returns true if two quaternions represent the same rotation within a
        default tolerance based on the numeric type.
        """
        ...
    def almost_same_direction(self, other: _Vec4f, threshold: float) -> bool:
        """Returns true if two quaternions represent the same rotation within a
        specified tolerance.
        """
        ...
    def output(self, __param0: ostream) -> None: ...
    def extract_to_matrix(self, m: LMatrix3f | _Mat4f) -> None:
        """Based on the quat lib from VRPN."""
        ...
    def set_from_matrix(self, m: LMatrix3f | _Mat4f) -> None:
        """Sets the quaternion according to the rotation represented by the matrix.
        Originally we tried an algorithm presented by Do-While Jones, but that
        turned out to be broken.  This is based on the quat lib from UNC.
        """
        ...
    def set_hpr(self, hpr: _Vec3f, cs: _CoordinateSystem = ...) -> None:
        """Sets the quaternion as the unit quaternion that is equivalent to these
        Euler angles.  (from Real-time Rendering, p.49)
        """
        ...
    def get_hpr(self, cs: _CoordinateSystem = ...) -> LVecBase3f:
        """Extracts the equivalent Euler angles from the unit quaternion."""
        ...
    def get_axis(self) -> LVector3f:
        """This, along with get_angle(), returns the rotation represented by the
        quaternion as an angle about an arbitrary axis.  This returns the axis; it
        is not normalized.
        """
        ...
    def get_axis_normalized(self) -> LVector3f:
        """This, along with get_angle(), returns the rotation represented by the
        quaternion as an angle about an arbitrary axis.  This returns the
        normalized axis.
        """
        ...
    def get_angle_rad(self) -> float:
        """This, along with get_axis(), returns the rotation represented by the
        quaternion as an angle about an arbitrary axis.  This returns the angle, in
        radians counterclockwise about the axis.
        
        It is necessary to ensure the quaternion has been normalized (for instance,
        with a call to normalize()) before calling this method.
        """
        ...
    def get_angle(self) -> float:
        """This, along with get_axis(), returns the rotation represented by the
        quaternion as an angle about an arbitrary axis.  This returns the angle, in
        degrees counterclockwise about the axis.
        
        It is necessary to ensure the quaternion has been normalized (for instance,
        with a call to normalize()) before calling this method.
        """
        ...
    def set_from_axis_angle_rad(self, angle_rad: float, axis: _Vec3f) -> None:
        """angle_rad is the angle about the axis in radians.  axis must be normalized."""
        ...
    def set_from_axis_angle(self, angle_deg: float, axis: _Vec3f) -> None:
        """angle_deg is the angle about the axis in degrees.  axis must be normalized."""
        ...
    def get_up(self, cs: _CoordinateSystem = ...) -> LVector3f:
        """Returns the orientation represented by this quaternion, expressed as an up
        vector.
        """
        ...
    def get_right(self, cs: _CoordinateSystem = ...) -> LVector3f:
        """Returns the orientation represented by this quaternion, expressed as a
        right vector.
        """
        ...
    def get_forward(self, cs: _CoordinateSystem = ...) -> LVector3f:
        """Returns the orientation represented by this quaternion, expressed as a
        forward vector.
        """
        ...
    def get_r(self) -> float: ...
    def get_i(self) -> float: ...
    def get_j(self) -> float: ...
    def get_k(self) -> float: ...
    def set_r(self, r: float) -> None: ...
    def set_i(self, i: float) -> None: ...
    def set_j(self, j: float) -> None: ...
    def set_k(self, k: float) -> None: ...
    def normalize(self) -> bool: ...
    def conjugate_from(self, other: _Vec4f) -> bool:
        """Computes the conjugate of the other quat, and stores the result in this
        quat.  This is a fully general operation and makes no assumptions about the
        type of transform represented by the quat.
        
        The other quat must be a different object than this quat.  However, if you
        need to get a conjugate of a quat in place, see conjugate_in_place.
        
        The return value is true if the quat was successfully inverted, false if
        there was a singularity.
        """
        ...
    def conjugate_in_place(self) -> bool:
        """Sets this to be the conjugate of the current quat.  Returns true if the
        successful, false if the quat was singular.
        """
        ...
    def invert_from(self, other: _Vec4f) -> bool:
        """Computes the inverse of the other quat, and stores the result in this quat.
        This is a fully general operation and makes no assumptions about the type
        of transform represented by the quat.
        
        The other quat must be a different object than this quat.  However, if you
        need to invert a quat in place, see invert_in_place.
        
        The return value is true if the quat was successfully inverted, false if
        there was a singularity.
        """
        ...
    def invert_in_place(self) -> bool:
        """Inverts the current quat.  Returns true if the inverse is successful, false
        if the quat was singular.
        """
        ...
    def is_identity(self) -> bool:
        """Returns true if this quaternion represents the identity transformation: no
        rotation.
        """
        ...
    def is_almost_identity(self, tolerance: float) -> bool:
        """Returns true if this quaternion represents the identity transformation
        within a given tolerance.
        """
        ...
    @staticmethod
    def ident_quat() -> LQuaternionf:
        """Returns an identity quaternion."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    pureImaginary = pure_imaginary
    angleRad = angle_rad
    angleDeg = angle_deg
    almostEqual = almost_equal
    isSameDirection = is_same_direction
    almostSameDirection = almost_same_direction
    extractToMatrix = extract_to_matrix
    setFromMatrix = set_from_matrix
    setHpr = set_hpr
    getHpr = get_hpr
    getAxis = get_axis
    getAxisNormalized = get_axis_normalized
    getAngleRad = get_angle_rad
    getAngle = get_angle
    setFromAxisAngleRad = set_from_axis_angle_rad
    setFromAxisAngle = set_from_axis_angle
    getUp = get_up
    getRight = get_right
    getForward = get_forward
    getR = get_r
    getI = get_i
    getJ = get_j
    getK = get_k
    setR = set_r
    setI = set_i
    setJ = set_j
    setK = set_k
    conjugateFrom = conjugate_from
    conjugateInPlace = conjugate_in_place
    invertFrom = invert_from
    invertInPlace = invert_in_place
    isIdentity = is_identity
    isAlmostIdentity = is_almost_identity
    identQuat = ident_quat
    getClassType = get_class_type

class LQuaterniond(LVecBase4d):
    """This is the base quaternion class"""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: _Vec4d) -> None: ...
    @overload
    def __init__(self, r: float, copy: _Vec3d) -> None: ...
    @overload
    def __init__(self, r: float, i: float, j: float, k: float) -> None: ...
    def __neg__(self) -> LQuaterniond: ...
    def __add__(self, other: _Vec4d) -> LQuaterniond: ...
    def __sub__(self, other: _Vec4d) -> LQuaterniond: ...
    @overload
    def __mul__(self, __param0: LMatrix3d) -> LMatrix3d: ...
    @overload
    def __mul__(self, __param0: _Mat4d) -> LMatrix4d: ...
    @overload
    def __mul__(self, __param0: _Vec4d) -> LQuaterniond: ...
    @overload
    def __mul__(self, scalar: float) -> LQuaterniond: ...
    def __truediv__(self, scalar: float) -> LQuaterniond: ...
    def __imul__(self, __param0: _Vec4d) -> LQuaterniond: ...
    def __pow__(self, __param0: float) -> LQuaterniond:
        """Returns a new quaternion that represents this quaternion raised to the
        given power.
        """
        ...
    @staticmethod
    def pure_imaginary(v: _Vec3d) -> LQuaterniond: ...
    def conjugate(self) -> LQuaterniond:
        """Returns the complex conjugate of this quat."""
        ...
    @overload
    def xform(self, v: _Vec3d) -> LVecBase3d:
        """Transforms a 3-d vector by the indicated rotation"""
        ...
    @overload
    def xform(self, v: _Vec4d) -> LVecBase4d:
        """Transforms a 4-d vector by the indicated rotation"""
        ...
    def multiply(self, rhs: _Vec4d) -> LQuaterniond:
        """actual multiply call (non virtual)"""
        ...
    def angle_rad(self, other: _Vec4d) -> float:
        """Returns the angle between the orientation represented by this quaternion
        and the other one, expressed in radians.
        """
        ...
    def angle_deg(self, other: _Vec4d) -> float:
        """Returns the angle between the orientation represented by this quaternion
        and the other one, expressed in degrees.
        """
        ...
    @overload
    def almost_equal(self, other: _Vec4d) -> bool:
        """Returns true if two quaternions are memberwise equal within a default
        tolerance based on the numeric type.
        """
        ...
    @overload
    def almost_equal(self, other: _Vec4d, threshold: float) -> bool:
        """Returns true if two quaternions are memberwise equal within a specified
        tolerance.
        """
        ...
    def is_same_direction(self, other: _Vec4d) -> bool:
        """Returns true if two quaternions represent the same rotation within a
        default tolerance based on the numeric type.
        """
        ...
    def almost_same_direction(self, other: _Vec4d, threshold: float) -> bool:
        """Returns true if two quaternions represent the same rotation within a
        specified tolerance.
        """
        ...
    def output(self, __param0: ostream) -> None: ...
    def extract_to_matrix(self, m: LMatrix3d | _Mat4d) -> None:
        """Based on the quat lib from VRPN."""
        ...
    def set_from_matrix(self, m: LMatrix3d | _Mat4d) -> None:
        """Sets the quaternion according to the rotation represented by the matrix.
        Originally we tried an algorithm presented by Do-While Jones, but that
        turned out to be broken.  This is based on the quat lib from UNC.
        """
        ...
    def set_hpr(self, hpr: _Vec3d, cs: _CoordinateSystem = ...) -> None:
        """Sets the quaternion as the unit quaternion that is equivalent to these
        Euler angles.  (from Real-time Rendering, p.49)
        """
        ...
    def get_hpr(self, cs: _CoordinateSystem = ...) -> LVecBase3d:
        """Extracts the equivalent Euler angles from the unit quaternion."""
        ...
    def get_axis(self) -> LVector3d:
        """This, along with get_angle(), returns the rotation represented by the
        quaternion as an angle about an arbitrary axis.  This returns the axis; it
        is not normalized.
        """
        ...
    def get_axis_normalized(self) -> LVector3d:
        """This, along with get_angle(), returns the rotation represented by the
        quaternion as an angle about an arbitrary axis.  This returns the
        normalized axis.
        """
        ...
    def get_angle_rad(self) -> float:
        """This, along with get_axis(), returns the rotation represented by the
        quaternion as an angle about an arbitrary axis.  This returns the angle, in
        radians counterclockwise about the axis.
        
        It is necessary to ensure the quaternion has been normalized (for instance,
        with a call to normalize()) before calling this method.
        """
        ...
    def get_angle(self) -> float:
        """This, along with get_axis(), returns the rotation represented by the
        quaternion as an angle about an arbitrary axis.  This returns the angle, in
        degrees counterclockwise about the axis.
        
        It is necessary to ensure the quaternion has been normalized (for instance,
        with a call to normalize()) before calling this method.
        """
        ...
    def set_from_axis_angle_rad(self, angle_rad: float, axis: _Vec3d) -> None:
        """angle_rad is the angle about the axis in radians.  axis must be normalized."""
        ...
    def set_from_axis_angle(self, angle_deg: float, axis: _Vec3d) -> None:
        """angle_deg is the angle about the axis in degrees.  axis must be normalized."""
        ...
    def get_up(self, cs: _CoordinateSystem = ...) -> LVector3d:
        """Returns the orientation represented by this quaternion, expressed as an up
        vector.
        """
        ...
    def get_right(self, cs: _CoordinateSystem = ...) -> LVector3d:
        """Returns the orientation represented by this quaternion, expressed as a
        right vector.
        """
        ...
    def get_forward(self, cs: _CoordinateSystem = ...) -> LVector3d:
        """Returns the orientation represented by this quaternion, expressed as a
        forward vector.
        """
        ...
    def get_r(self) -> float: ...
    def get_i(self) -> float: ...
    def get_j(self) -> float: ...
    def get_k(self) -> float: ...
    def set_r(self, r: float) -> None: ...
    def set_i(self, i: float) -> None: ...
    def set_j(self, j: float) -> None: ...
    def set_k(self, k: float) -> None: ...
    def normalize(self) -> bool: ...
    def conjugate_from(self, other: _Vec4d) -> bool:
        """Computes the conjugate of the other quat, and stores the result in this
        quat.  This is a fully general operation and makes no assumptions about the
        type of transform represented by the quat.
        
        The other quat must be a different object than this quat.  However, if you
        need to get a conjugate of a quat in place, see conjugate_in_place.
        
        The return value is true if the quat was successfully inverted, false if
        there was a singularity.
        """
        ...
    def conjugate_in_place(self) -> bool:
        """Sets this to be the conjugate of the current quat.  Returns true if the
        successful, false if the quat was singular.
        """
        ...
    def invert_from(self, other: _Vec4d) -> bool:
        """Computes the inverse of the other quat, and stores the result in this quat.
        This is a fully general operation and makes no assumptions about the type
        of transform represented by the quat.
        
        The other quat must be a different object than this quat.  However, if you
        need to invert a quat in place, see invert_in_place.
        
        The return value is true if the quat was successfully inverted, false if
        there was a singularity.
        """
        ...
    def invert_in_place(self) -> bool:
        """Inverts the current quat.  Returns true if the inverse is successful, false
        if the quat was singular.
        """
        ...
    def is_identity(self) -> bool:
        """Returns true if this quaternion represents the identity transformation: no
        rotation.
        """
        ...
    def is_almost_identity(self, tolerance: float) -> bool:
        """Returns true if this quaternion represents the identity transformation
        within a given tolerance.
        """
        ...
    @staticmethod
    def ident_quat() -> LQuaterniond:
        """Returns an identity quaternion."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    pureImaginary = pure_imaginary
    angleRad = angle_rad
    angleDeg = angle_deg
    almostEqual = almost_equal
    isSameDirection = is_same_direction
    almostSameDirection = almost_same_direction
    extractToMatrix = extract_to_matrix
    setFromMatrix = set_from_matrix
    setHpr = set_hpr
    getHpr = get_hpr
    getAxis = get_axis
    getAxisNormalized = get_axis_normalized
    getAngleRad = get_angle_rad
    getAngle = get_angle
    setFromAxisAngleRad = set_from_axis_angle_rad
    setFromAxisAngle = set_from_axis_angle
    getUp = get_up
    getRight = get_right
    getForward = get_forward
    getR = get_r
    getI = get_i
    getJ = get_j
    getK = get_k
    setR = set_r
    setI = set_i
    setJ = set_j
    setK = set_k
    conjugateFrom = conjugate_from
    conjugateInPlace = conjugate_in_place
    invertFrom = invert_from
    invertInPlace = invert_in_place
    isIdentity = is_identity
    isAlmostIdentity = is_almost_identity
    identQuat = ident_quat
    getClassType = get_class_type

class LRotationf(LQuaternionf):
    """This is a unit quaternion representing a rotation."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, c: LQuaternionf) -> None:
        """lmatrix3"""
        ...
    @overload
    def __init__(self, m: LMatrix3f | _Mat4f) -> None:
        """lmatrix4"""
        ...
    @overload
    def __init__(self, copy: _Vec4f) -> None: ...
    @overload
    def __init__(self, axis: _Vec3f, angle: float) -> None: ...
    @overload
    def __init__(self, h: float, p: float, r: float) -> None: ...
    @overload
    def __init__(self, r: float, i: float, j: float, k: float) -> None:
        """axis + angle (in degrees)"""
        ...
    @overload
    def __mul__(self, other: LRotationf) -> LRotationf: ...
    @overload
    def __mul__(self, other: _Vec4f) -> LQuaternionf: ...
    @overload
    def __mul__(self, scalar: float) -> LRotationf: ...
    def __truediv__(self, scalar: float) -> LRotationf: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class LRotationd(LQuaterniond):
    """This is a unit quaternion representing a rotation."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, c: LQuaterniond) -> None:
        """lmatrix3"""
        ...
    @overload
    def __init__(self, m: LMatrix3d | _Mat4d) -> None:
        """lmatrix4"""
        ...
    @overload
    def __init__(self, copy: _Vec4d) -> None: ...
    @overload
    def __init__(self, axis: _Vec3d, angle: float) -> None: ...
    @overload
    def __init__(self, h: float, p: float, r: float) -> None: ...
    @overload
    def __init__(self, r: float, i: float, j: float, k: float) -> None:
        """axis + angle (in degrees)"""
        ...
    @overload
    def __mul__(self, other: LRotationd) -> LRotationd: ...
    @overload
    def __mul__(self, other: _Vec4d) -> LQuaterniond: ...
    @overload
    def __mul__(self, scalar: float) -> LRotationd: ...
    def __truediv__(self, scalar: float) -> LRotationd: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class LOrientationf(LQuaternionf):
    """This is a unit quaternion representing an orientation."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, c: _Vec4f) -> None:
        """matrix3"""
        ...
    @overload
    def __init__(self, m: LMatrix3f | _Mat4f) -> None:
        """matrix4"""
        ...
    @overload
    def __init__(self, point_at: _Vec3f, twist: float) -> None: ...
    @overload
    def __init__(self, r: float, i: float, j: float, k: float) -> None: ...
    def __mul__(self, other: _Vec4f) -> LOrientationf: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class LOrientationd(LQuaterniond):
    """This is a unit quaternion representing an orientation."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, c: _Vec4d) -> None:
        """matrix3"""
        ...
    @overload
    def __init__(self, m: LMatrix3d | _Mat4d) -> None:
        """matrix4"""
        ...
    @overload
    def __init__(self, point_at: _Vec3d, twist: float) -> None: ...
    @overload
    def __init__(self, r: float, i: float, j: float, k: float) -> None: ...
    def __mul__(self, other: _Vec4d) -> LOrientationd: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class ConfigVariableColor(ConfigVariable):
    """This is a convenience class to specialize ConfigVariable as a set of
    floating-point types representing a color value.
    
    It interprets the color differently depending on how many words were
    specified: if only one, it is interpreted as a shade of gray with alpha 1.
    If two values were specified, a grayscale and alpha pair.  If three, a set
    of R, G, B values with alpha 1, and if four, a complete RGBA color.
    
    This isn't defined in dtool because it relies on the LColor class, which is
    defined in linmath.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: ConfigVariableColor) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, name: str, default_value: _Vec4f | str, description: str = ..., flags: int = ...) -> None: ...
    def __getitem__(self, n: int) -> float: ...
    def operator_typecast(self) -> LVecBase4f: ...
    def assign(self, value: _Vec4f) -> ConfigVariableColor: ...
    def set_value(self, value: _Vec4f) -> None:
        """Reassigns the variable's local value."""
        ...
    def get_value(self) -> LVecBase4f:
        """Returns the variable's value."""
        ...
    def get_default_value(self) -> LVecBase4f:
        """Returns the variable's default value."""
        ...
    operatorTypecast = operator_typecast
    setValue = set_value
    getValue = get_value
    getDefaultValue = get_default_value

CS_default: Literal[0]
CS_zup_right: Literal[1]
CS_yup_right: Literal[2]
CS_zup_left: Literal[3]
CS_yup_left: Literal[4]
CS_invalid: Literal[5]
@overload
def __mul__(v: LPoint3d, m: LMatrix3d) -> LPoint3d: ...
@overload
def __mul__(v: LPoint3f, m: LMatrix3f) -> LPoint3f: ...
@overload
def __mul__(v: LPoint4d, m: LMatrix4d) -> LPoint4d: ...
@overload
def __mul__(v: LPoint4f, m: LMatrix4f) -> LPoint4f: ...
@overload
def __mul__(v: LVector3d, m: LMatrix3d) -> LVector3d: ...
@overload
def __mul__(v: LVector3f, m: LMatrix3f) -> LVector3f: ...
@overload
def __mul__(v: LVector4d, m: LMatrix4d) -> LVector4d: ...
@overload
def __mul__(v: LVector4f, m: LMatrix4f) -> LVector4f: ...
@overload
def __mul__(m: LMatrix3d, q: _Vec4d) -> LMatrix3d: ...
@overload
def __mul__(m: LMatrix3f, q: _Vec4f) -> LMatrix3f: ...
@overload
def __mul__(m: _Mat4d, q: _Vec4d) -> LMatrix4d: ...
@overload
def __mul__(m: _Mat4f, q: _Vec4f) -> LMatrix4f: ...
@overload
def __mul__(v: LVecBase2d, m: LMatrix3d) -> LPoint2d | LVector2d: ...
@overload
def __mul__(v: LVecBase2f, m: LMatrix3f) -> LPoint2f | LVector2f: ...
@overload
def __mul__(v: _Vec3d, m: _Mat4d) -> LPoint3d | LVector3d: ...
@overload
def __mul__(v: _Vec3f, m: _Mat4f) -> LPoint3f | LVector3f: ...
@overload
def __mul__(v: _Vec3d, m: LMatrix3d) -> LVecBase3d: ...
@overload
def __mul__(v: _Vec3f, m: LMatrix3f) -> LVecBase3f: ...
@overload
def __mul__(v: _Vec4d, m: _Mat4d) -> LVecBase4d: ...
@overload
def __mul__(v: _Vec4f, m: _Mat4f) -> LVecBase4f: ...
@overload
def __imul__(v: LPoint3d | LVecBase2d | LVector3d | _Vec3d, m: LMatrix3d) -> None: ...
@overload
def __imul__(v: LPoint3f | LVecBase2f | LVector3f | _Vec3f, m: LMatrix3f) -> None: ...
@overload
def __imul__(v: _Vec3d | _Vec4d, m: _Mat4d) -> None: ...
@overload
def __imul__(v: _Vec3f | _Vec4f, m: _Mat4f) -> None: ...
def deg_2_rad(f: float) -> float: ...
def rad_2_deg(f: float) -> float: ...
def get_default_coordinate_system() -> _CoordinateSystem: ...
def parse_coordinate_system_string(str: str) -> _CoordinateSystem: ...
def format_coordinate_system(cs: _CoordinateSystem) -> str: ...
def is_right_handed(cs: _CoordinateSystem = ...) -> bool: ...
@overload
def transpose(a: LMatrix3d) -> LMatrix3d: ...
@overload
def transpose(a: LMatrix3f) -> LMatrix3f: ...
@overload
def transpose(a: _Mat4d) -> LMatrix4d: ...
@overload
def transpose(a: _Mat4f) -> LMatrix4f: ...
@overload
def invert(a: LMatrix3d) -> LMatrix3d: ...
@overload
def invert(a: LMatrix3f) -> LMatrix3f: ...
@overload
def invert(a: _Mat4d) -> LMatrix4d: ...
@overload
def invert(a: _Mat4f) -> LMatrix4f: ...
@overload
def invert(a: _Vec4d) -> LQuaterniond: ...
@overload
def invert(a: _Vec4f) -> LQuaternionf: ...
def generic_write_datagram(dest: Datagram, value: LMatrix3d | LMatrix3f | _Mat4d | _Mat4f) -> None: ...
def generic_read_datagram(result: LMatrix3d | LMatrix3f | _Mat4d | _Mat4f, source: DatagramIterator) -> None: ...
@overload
def compose_matrix(mat: LMatrix3d, scale: _Vec3d, hpr: _Vec3d, cs: _CoordinateSystem = ...) -> None: ...
@overload
def compose_matrix(mat: LMatrix3f, scale: _Vec3f, hpr: _Vec3f, cs: _CoordinateSystem = ...) -> None: ...
@overload
def compose_matrix(mat: LMatrix3d, scale: _Vec3d, shear: _Vec3d, hpr: _Vec3d, cs: _CoordinateSystem = ...) -> None: ...
@overload
def compose_matrix(mat: LMatrix3f, scale: _Vec3f, shear: _Vec3f, hpr: _Vec3f, cs: _CoordinateSystem = ...) -> None: ...
@overload
def compose_matrix(mat: _Mat4d, scale: _Vec3d, hpr: _Vec3d, translate: _Vec3d, cs: _CoordinateSystem = ...) -> None: ...
@overload
def compose_matrix(mat: _Mat4f, scale: _Vec3f, hpr: _Vec3f, translate: _Vec3f, cs: _CoordinateSystem = ...) -> None: ...
@overload
def compose_matrix(mat: _Mat4d, scale: _Vec3d, shear: _Vec3d, hpr: _Vec3d, translate: _Vec3d, cs: _CoordinateSystem = ...) -> None: ...
@overload
def compose_matrix(mat: _Mat4f, scale: _Vec3f, shear: _Vec3f, hpr: _Vec3f, translate: _Vec3f, cs: _CoordinateSystem = ...) -> None: ...
@overload
def decompose_matrix(mat: LMatrix3d, scale: _Vec3d, hpr: _Vec3d, cs: _CoordinateSystem = ...) -> bool: ...
@overload
def decompose_matrix(mat: LMatrix3f, scale: _Vec3f, hpr: _Vec3f, cs: _CoordinateSystem = ...) -> bool: ...
@overload
def decompose_matrix(mat: LMatrix3d, scale: _Vec3d, shear: _Vec3d, hpr: _Vec3d, cs: _CoordinateSystem = ...) -> bool: ...
@overload
def decompose_matrix(mat: LMatrix3f, scale: _Vec3f, shear: _Vec3f, hpr: _Vec3f, cs: _CoordinateSystem = ...) -> bool: ...
@overload
def decompose_matrix(mat: _Mat4d, scale: _Vec3d, hpr: _Vec3d, translate: _Vec3d, cs: _CoordinateSystem = ...) -> bool: ...
@overload
def decompose_matrix(mat: _Mat4f, scale: _Vec3f, hpr: _Vec3f, translate: _Vec3f, cs: _CoordinateSystem = ...) -> bool: ...
@overload
def decompose_matrix(mat: _Mat4d, scale: _Vec3d, shear: _Vec3d, hpr: _Vec3d, translate: _Vec3d, cs: _CoordinateSystem = ...) -> bool: ...
@overload
def decompose_matrix(mat: _Mat4f, scale: _Vec3f, shear: _Vec3f, hpr: _Vec3f, translate: _Vec3f, cs: _CoordinateSystem = ...) -> bool: ...
@overload
def decompose_matrix_old_hpr(mat: LMatrix3d, scale: _Vec3d, shear: _Vec3d, hpr: _Vec3d, cs: _CoordinateSystem = ...) -> bool: ...
@overload
def decompose_matrix_old_hpr(mat: LMatrix3f, scale: _Vec3f, shear: _Vec3f, hpr: _Vec3f, cs: _CoordinateSystem = ...) -> bool: ...
@overload
def old_to_new_hpr(old_hpr: _Vec3d) -> LVecBase3d: ...
@overload
def old_to_new_hpr(old_hpr: _Vec3f) -> LVecBase3f: ...
deg2Rad = deg_2_rad
rad2Deg = rad_2_deg
getDefaultCoordinateSystem = get_default_coordinate_system
parseCoordinateSystemString = parse_coordinate_system_string
formatCoordinateSystem = format_coordinate_system
isRightHanded = is_right_handed
genericWriteDatagram = generic_write_datagram
genericReadDatagram = generic_read_datagram
composeMatrix = compose_matrix
decomposeMatrix = decompose_matrix
decomposeMatrixOldHpr = decompose_matrix_old_hpr
oldToNewHpr = old_to_new_hpr
CSDefault = CS_default
CSZupRight = CS_zup_right
CSYupRight = CS_yup_right
CSZupLeft = CS_zup_left
CSYupLeft = CS_yup_left
CSInvalid = CS_invalid
LVertexf = LPoint3f
LNormalf = LVector3f
LTexCoordf = LPoint2f
LTexCoord3f = LPoint3f
LColorf = LVecBase4f
LRGBColorf = LVecBase3f
LVertexd = LPoint3d
LNormald = LVector3d
LTexCoordd = LPoint2d
LTexCoord3d = LPoint3d
LColord = LVecBase4d
LRGBColord = LVecBase3d
Mat4F = LMatrix4f
Mat3F = LMatrix3f
VBase4F = LVecBase4f
Vec4F = LVector4f
Point4F = LPoint4f
VBase3F = LVecBase3f
Vec3F = LVector3f
Point3F = LPoint3f
VBase2F = LVecBase2f
Vec2F = LVector2f
Point2F = LPoint2f
QuatF = LQuaternionf
Mat4D = LMatrix4d
Mat3D = LMatrix3d
VBase4D = LVecBase4d
Vec4D = LVector4d
Point4D = LPoint4d
VBase3D = LVecBase3d
Vec3D = LVector3d
Point3D = LPoint3d
VBase2D = LVecBase2d
Vec2D = LVector2d
Point2D = LPoint2d
QuatD = LQuaterniond
LVecBase2 = LVecBase2f
LPoint2 = LPoint2f
LVector2 = LVector2f
LVecBase3 = LVecBase3f
LPoint3 = LPoint3f
LVector3 = LVector3f
LVecBase4 = LVecBase4f
LPoint4 = LPoint4f
LVector4 = LVector4f
LQuaternion = LQuaternionf
LRotation = LRotationf
LOrientation = LOrientationf
LMatrix3 = LMatrix3f
LMatrix4 = LMatrix4f
LVertex = LPoint3f
LNormal = LVector3f
LTexCoord = LPoint2f
LTexCoord3 = LPoint3f
LColor = LVecBase4f
LRGBColor = LVecBase3f
UnalignedLVecBase4 = UnalignedLVecBase4f
UnalignedLMatrix4 = UnalignedLMatrix4f
Mat4 = LMatrix4f
Mat3 = LMatrix3f
VBase4 = LVecBase4f
Vec4 = LVector4f
Point4 = LPoint4f
VBase3 = LVecBase3f
Vec3 = LVector3f
Point3 = LPoint3f
VBase2 = LVecBase2f
Vec2 = LVector2f
Point2 = LPoint2f
Quat = LQuaternionf
