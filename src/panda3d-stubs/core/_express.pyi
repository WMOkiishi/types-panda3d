import sys
from _typeshed import StrOrBytesPath
from collections.abc import Iterator, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import SearchPathLike
from panda3d.core._dtoolbase import TypedObject, TypeHandle
from panda3d.core._dtoolutil import DSearchPath, Filename, iostream, istream, ostream
from panda3d.core._prc import ConfigVariableFilename, IStreamWrapper, OStreamWrapper, StreamReader, StreamWrapper, StreamWriter

_ErrorUtilCode: TypeAlias = int
_WindowsRegistry_RegLevel: TypeAlias = Literal[0, 1]
_WindowsRegistry_Type: TypeAlias = Literal[0, 1, 2]

class PointerToVoid:
    """This is the non-template part of the base class for PointerTo and
    ConstPointerTo.  It is necessary so we can keep a pointer to a non-template
    class within the ReferenceCount object, to implement weak reference
    pointers--we need to have something to clean up when the ReferenceCount
    object destructs.

    This is the base class for PointerToBase<T>.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def is_null(self) -> bool:
        """Returns true if the PointerTo is a NULL pointer, false otherwise.  (Direct
        comparison to a NULL pointer also works.)
        """
    def get_hash(self) -> int: ...
    isNull = is_null
    getHash = get_hash

class PointerToBase_ReferenceCountedVector_double(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_double(PointerToBase_ReferenceCountedVector_double):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_double(PointerToArrayBase_double):
    def __init__(self, copy: ConstPointerToArray_double | PointerToArray_double) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> float: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_double: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[float]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> float: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: float) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_float(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_float(PointerToBase_ReferenceCountedVector_float):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_float(PointerToArrayBase_float):
    def __init__(self, copy: ConstPointerToArray_float | PointerToArray_float) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> float: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_float: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[float]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> float: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: float) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_int(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_int(PointerToBase_ReferenceCountedVector_int):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_int(PointerToArrayBase_int):
    def __init__(self, copy: ConstPointerToArray_int | PointerToArray_int) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> int: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_int: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[int]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> int: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: int) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_unsigned_char(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_unsigned_char(PointerToBase_ReferenceCountedVector_unsigned_char):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_unsigned_char(PointerToArrayBase_unsigned_char):
    def __init__(self, copy: ConstPointerToArray_unsigned_char | PointerToArray_unsigned_char) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> str: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_unsigned_char: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[str]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> str: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: str) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToArray_double(PointerToArrayBase_double):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_double) -> None: ...
    @overload
    def __init__(self, source: Sequence[float]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> float: ...
    def __setitem__(self, n: int, value: float) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_double: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[float]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_double: ...
    def push_back(self, x: float) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> float: ...
    def set_element(self, n: int, value: float) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: float) -> int: ...
    emptyArray = empty_array
    pushBack = push_back
    popBack = pop_back
    getElement = get_element
    setElement = set_element
    getData = get_data
    setData = set_data
    getSubdata = get_subdata
    setSubdata = set_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToArray_float(PointerToArrayBase_float):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_float) -> None: ...
    @overload
    def __init__(self, source: Sequence[float]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> float: ...
    def __setitem__(self, n: int, value: float) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_float: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[float]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_float: ...
    def push_back(self, x: float) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> float: ...
    def set_element(self, n: int, value: float) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: float) -> int: ...
    emptyArray = empty_array
    pushBack = push_back
    popBack = pop_back
    getElement = get_element
    setElement = set_element
    getData = get_data
    setData = set_data
    getSubdata = get_subdata
    setSubdata = set_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToArray_int(PointerToArrayBase_int):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_int) -> None: ...
    @overload
    def __init__(self, source: Sequence[int]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> int: ...
    def __setitem__(self, n: int, value: int) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_int: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[int]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_int: ...
    def push_back(self, x: int) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> int: ...
    def set_element(self, n: int, value: int) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: int) -> int: ...
    emptyArray = empty_array
    pushBack = push_back
    popBack = pop_back
    getElement = get_element
    setElement = set_element
    getData = get_data
    setData = set_data
    getSubdata = get_subdata
    setSubdata = set_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToArray_unsigned_char(PointerToArrayBase_unsigned_char):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_unsigned_char) -> None: ...
    @overload
    def __init__(self, source: Sequence[str]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> str: ...
    def __setitem__(self, n: int, value: str) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_unsigned_char: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[str]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_unsigned_char: ...
    def push_back(self, x: str) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> str: ...
    def set_element(self, n: int, value: str) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: str) -> int: ...
    emptyArray = empty_array
    pushBack = push_back
    popBack = pop_back
    getElement = get_element
    setElement = set_element
    getData = get_data
    setData = set_data
    getSubdata = get_subdata
    setSubdata = set_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class MemoryUsage:
    """This class is used strictly for debugging purposes, specifically for
    tracking memory leaks of reference-counted objects: it keeps a record of
    every such object currently allocated.

    When compiled with NDEBUG set, this entire class does nothing and compiles
    to a stub.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def tracking(self) -> bool: ...
    @property
    def counting(self) -> bool: ...
    @property
    def current_cpp_size(self) -> int: ...
    @property
    def total_cpp_size(self) -> int: ...
    @property
    def panda_heap_single_size(self) -> int: ...
    @property
    def panda_heap_array_size(self) -> int: ...
    @property
    def panda_heap_overhead(self) -> int: ...
    @property
    def panda_mmap_size(self) -> int: ...
    @property
    def external_size(self) -> int: ...
    @property
    def total_size(self) -> int: ...
    def __init__(self, __param0: MemoryUsage) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def is_tracking() -> bool:
        """Returns true if the MemoryUsage object is currently tracking memory (e.g.
        track-memory-usage is configured #t).
        """
    @staticmethod
    def is_counting() -> bool:
        """Returns true if the MemoryUsage object is currently at least counting
        memory (e.g.  this is a Windows debug build), even if it's not fully
        tracking it.
        """
    @staticmethod
    def get_current_cpp_size() -> int:
        """Returns the total number of bytes of allocated memory consumed by C++
        objects, not including the memory previously frozen.
        """
    @staticmethod
    def get_total_cpp_size() -> int:
        """Returns the total number of bytes of allocated memory consumed by C++
        objects, including the memory previously frozen.
        """
    @staticmethod
    def get_panda_heap_single_size() -> int:
        """Returns the total number of bytes allocated from the heap from code within
        Panda, for individual objects.
        """
    @staticmethod
    def get_panda_heap_array_size() -> int:
        """Returns the total number of bytes allocated from the heap from code within
        Panda, for arrays.
        """
    @staticmethod
    def get_panda_heap_overhead() -> int:
        """Returns the extra bytes allocated from the system that are not immediately
        used for holding allocated objects.  This can only be determined if
        ALTERNATIVE_MALLOC is enabled.
        """
    @staticmethod
    def get_panda_mmap_size() -> int:
        """Returns the total number of bytes allocated from the virtual memory pool
        from code within Panda.
        """
    @staticmethod
    def get_external_size() -> int:
        """Returns the total number of bytes of allocated memory in the heap that
        Panda didn't seem to be responsible for.  This includes a few bytes for
        very low-level objects (like ConfigVariables) that cannot use Panda memory
        tracking because they are so very low-level.

        This also includes all of the memory that might have been allocated by a
        high-level interpreter, like Python.

        This number is only available if Panda is able to hook into the actual heap
        callback.
        """
    @staticmethod
    def get_total_size() -> int:
        """Returns the total size of allocated memory consumed by the process, as
        nearly as can be determined.
        """
    @staticmethod
    def get_num_pointers() -> int:
        """Returns the number of pointers currently active."""
    @staticmethod
    def get_pointers(result: MemoryUsagePointers) -> None:
        """Fills the indicated MemoryUsagePointers with the set of all pointers
        currently active.
        """
    @staticmethod
    def get_pointers_of_type(result: MemoryUsagePointers, type: TypeHandle | type) -> None:
        """Fills the indicated MemoryUsagePointers with the set of all pointers of the
        indicated type currently active.
        """
    @staticmethod
    def get_pointers_of_age(result: MemoryUsagePointers, _from: float, to: float) -> None:
        """Fills the indicated MemoryUsagePointers with the set of all pointers that
        were allocated within the range of the indicated number of seconds ago.
        """
    @staticmethod
    def get_pointers_with_zero_count(result: MemoryUsagePointers) -> None:
        """Fills the indicated MemoryUsagePointers with the set of all currently
        active pointers (that is, pointers allocated since the last call to
        freeze(), and not yet freed) that have a zero reference count.

        Generally, an undeleted pointer with a zero reference count means its
        reference count has never been incremented beyond zero (since once it has
        been incremented, the only way it can return to zero would free the
        pointer).  This may include objects that are allocated statically or on the
        stack, which are never intended to be deleted.  Or, it might represent a
        programmer or compiler error.

        This function has the side-effect of incrementing each of their reference
        counts by one, thus preventing them from ever being freed--but since they
        hadn't been freed anyway, probably no additional harm is done.
        """
    @staticmethod
    def freeze() -> None:
        """'Freezes' all pointers currently stored so that they are no longer
        reported; only newly allocate pointers from this point on will appear in
        future information requests.  This makes it easier to differentiate between
        continuous leaks and one-time memory allocations.
        """
    @staticmethod
    def show_current_types() -> None:
        """Shows the breakdown of types of all of the active pointers."""
    @staticmethod
    def show_trend_types() -> None:
        """Shows the breakdown of types of all of the pointers allocated and freed
        since the last call to freeze().
        """
    @staticmethod
    def show_current_ages() -> None:
        """Shows the breakdown of ages of all of the active pointers."""
    @staticmethod
    def show_trend_ages() -> None:
        """Shows the breakdown of ages of all of the pointers allocated and freed
        since the last call to freeze().
        """
    isTracking = is_tracking
    isCounting = is_counting
    getCurrentCppSize = get_current_cpp_size
    getTotalCppSize = get_total_cpp_size
    getPandaHeapSingleSize = get_panda_heap_single_size
    getPandaHeapArraySize = get_panda_heap_array_size
    getPandaHeapOverhead = get_panda_heap_overhead
    getPandaMmapSize = get_panda_mmap_size
    getExternalSize = get_external_size
    getTotalSize = get_total_size
    getNumPointers = get_num_pointers
    getPointers = get_pointers
    getPointersOfType = get_pointers_of_type
    getPointersOfAge = get_pointers_of_age
    getPointersWithZeroCount = get_pointers_with_zero_count
    showCurrentTypes = show_current_types
    showTrendTypes = show_trend_types
    showCurrentAges = show_current_ages
    showTrendAges = show_trend_ages

class ReferenceCount:
    """A base class for all things that want to be reference-counted.
    ReferenceCount works in conjunction with PointerTo to automatically delete
    objects when the last pointer to them goes away.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def ref_count(self) -> int:
        """The current reference count."""
    def get_ref_count(self) -> int:
        """Returns the current reference count."""
    def ref(self) -> None:
        """Explicitly increments the reference count.  User code should avoid using
        ref() and unref() directly, which can result in missed reference counts.
        Instead, let a PointerTo object manage the reference counting
        automatically.

        This function is const, even though it changes the object, because
        generally fiddling with an object's reference count isn't considered part
        of fiddling with the object.  An object might be const in other ways, but
        we still need to accurately count the number of references to it.
        """
    def unref(self) -> bool:
        """Explicitly decrements the reference count.  Note that the object will not
        be implicitly deleted by unref() simply because the reference count drops
        to zero.  (Having a member function delete itself is problematic.) However,
        see the helper function unref_delete().

        User code should avoid using ref() and unref() directly, which can result
        in missed reference counts.  Instead, let a PointerTo object manage the
        reference counting automatically.

        This function is const, even though it changes the object, because
        generally fiddling with an object's reference count isn't considered part
        of fiddling with the object.  An object might be const in other ways, but
        we still need to accurately count the number of references to it.

        The return value is true if the new reference count is nonzero, false if it
        is zero.
        """
    def test_ref_count_integrity(self) -> bool:
        """Does some easy checks to make sure that the reference count isn't
        completely bogus.  Returns true if ok, false otherwise.
        """
    def test_ref_count_nonzero(self) -> bool:
        """Does some easy checks to make sure that the reference count isn't zero, or
        completely bogus.  Returns true if ok, false otherwise.
        """
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getRefCount = get_ref_count
    testRefCountIntegrity = test_ref_count_integrity
    testRefCountNonzero = test_ref_count_nonzero
    getClassType = get_class_type

class Buffer(ReferenceCount):
    def __init__(self, __param0: Buffer) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_length(self) -> int: ...
    getLength = get_length

class PStatCollectorForwardBase(ReferenceCount):
    """This class serves as a cheap forward reference to a PStatCollector, which
    is defined in the pstatclient module (and is not directly accessible here
    in the express module).

    This is subclassed as PStatCollectorForward, which defines the actual
    functionality.
    """

    def add_level(self, level: float) -> None: ...
    addLevel = add_level

class NodeReferenceCount(ReferenceCount):
    """This class specializes ReferenceCount to add an additional counter, called
    node_ref_count, for the purposes of counting the number of times the object
    is referenced by a "node", whatever that may mean in context.

    The new methods node_ref() and node_unref() automatically increment and
    decrement the primary reference count as well.  There also exists a
    NodePointerTo<> class to maintain the node_ref counters automatically.

    See also CachedTypedWritableReferenceCount, which is similar in principle,
    as well as NodeCachedReferenceCount, which combines both of these.
    """

    def get_node_ref_count(self) -> int:
        """Returns the current reference count."""
    def node_ref(self) -> None:
        """Explicitly increments the node reference count and the normal reference
        count simultaneously.
        """
    def node_unref(self) -> bool:
        """Explicitly decrements the node reference count and the normal reference
        count simultaneously.

        The return value is true if the new reference count is nonzero, false if it
        is zero.
        """
    def test_ref_count_integrity(self) -> bool:
        """Does some easy checks to make sure that the reference count isn't
        completely bogus.
        """
    def node_unref_only(self) -> None:
        """Decrements the node reference count without affecting the normal reference
        count.  Intended to be called by derived classes only, presumably to
        reimplement node_unref().
        """
    getNodeRefCount = get_node_ref_count
    nodeRef = node_ref
    nodeUnref = node_unref
    testRefCountIntegrity = test_ref_count_integrity
    nodeUnrefOnly = node_unref_only

class Datagram(TypedObject):
    """An ordered list of data elements, formatted in memory for transmission over
    a socket or writing to a data file.

    Data elements should be added one at a time, in order, to the Datagram.
    The nature and contents of the data elements are totally up to the user.
    When a Datagram has been transmitted and received, its data elements may be
    extracted using a DatagramIterator; it is up to the caller to know the
    correct type of each data element in order.

    A Datagram is itself headerless; it is simply a collection of data
    elements.
    """

    @overload
    def __init__(self, copy: Datagram = ...) -> None:
        """Constructs a datagram from an existing block of data."""
    @overload
    def __init__(self, data: bytes) -> None: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: Datagram) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def clear(self) -> None:
        """Resets the datagram to empty, in preparation for building up a new
        datagram.
        """
    def dump_hex(self, out: ostream, indent: int = ...) -> None:
        """Writes a representation of the entire datagram contents, as a sequence of
        hex (and ASCII) values.
        """
    def add_bool(self, value: bool) -> None:
        """Adds a boolean value to the datagram."""
    def add_int8(self, value: str) -> None:
        """Adds a signed 8-bit integer to the datagram."""
    def add_uint8(self, value: str) -> None:
        """Adds an unsigned 8-bit integer to the datagram."""
    def add_int16(self, value: int) -> None:
        """Adds a signed 16-bit integer to the datagram."""
    def add_int32(self, value: int) -> None:
        """Adds a signed 32-bit integer to the datagram."""
    def add_int64(self, value: int) -> None:
        """Adds a signed 64-bit integer to the datagram."""
    def add_uint16(self, value: int) -> None:
        """Adds an unsigned 16-bit integer to the datagram."""
    def add_uint32(self, value: int) -> None:
        """Adds an unsigned 32-bit integer to the datagram."""
    def add_uint64(self, value: int) -> None:
        """Adds an unsigned 64-bit integer to the datagram."""
    def add_float32(self, value: float) -> None:
        """Adds a 32-bit single-precision floating-point number to the datagram.
        Since this kind of float is not necessarily portable across different
        architectures, special care is required.
        """
    def add_float64(self, value: float) -> None:
        """Adds a 64-bit floating-point number to the datagram."""
    def add_stdfloat(self, value: float) -> None:
        """Adds either a 32-bit or a 64-bit floating-point number, according to
        set_stdfloat_double().
        """
    def add_be_int16(self, value: int) -> None:
        """These functions pack numbers big-endian, in case that's desired."""
    def add_be_int32(self, value: int) -> None:
        """Adds a signed 32-bit big-endian integer to the datagram."""
    def add_be_int64(self, value: int) -> None:
        """Adds a signed 64-bit big-endian integer to the datagram."""
    def add_be_uint16(self, value: int) -> None:
        """Adds an unsigned 16-bit big-endian integer to the datagram."""
    def add_be_uint32(self, value: int) -> None:
        """Adds an unsigned 32-bit big-endian integer to the datagram."""
    def add_be_uint64(self, value: int) -> None:
        """Adds an unsigned 64-bit big-endian integer to the datagram."""
    def add_be_float32(self, value: float) -> None:
        """Adds a 32-bit single-precision big-endian floating-point number to the
        datagram.
        """
    def add_be_float64(self, value: float) -> None:
        """Adds a 64-bit big-endian floating-point number to the datagram."""
    def add_string(self, str: str) -> None:
        """Adds a variable-length string to the datagram.  This actually adds a count
        followed by n bytes.
        """
    def add_string32(self, str: str) -> None:
        """Adds a variable-length string to the datagram, using a 32-bit length field
        to allow very long strings.
        """
    def add_z_string(self, str: str) -> None:
        """Adds a variable-length string to the datagram, as a NULL-terminated string."""
    def add_fixed_string(self, str: str, size: int) -> None:
        """Adds a fixed-length string to the datagram.  If the string given is less
        than the requested size, this will pad the string out with zeroes; if it is
        greater than the requested size, this will silently truncate the string.
        """
    def add_wstring(self, str: str) -> None:
        """Adds a variable-length wstring to the datagram."""
    def add_blob(self, __param0: bytes) -> None:
        """Adds a variable-length binary blob to the datagram.  This actually adds a
        count followed by n bytes.
        """
    def add_blob32(self, __param0: bytes) -> None:
        """Adds a variable-length binary blob to the datagram, using a 32-bit length
        field to allow very long blobs.
        """
    def pad_bytes(self, size: int) -> None:
        """Adds the indicated number of zero bytes to the datagram."""
    def append_data(self, data: bytes) -> None:
        """Appends some more raw data to the end of the datagram."""
    def get_message(self) -> bytes:
        """Returns the datagram's data as a string."""
    def get_length(self) -> int:
        """Returns the number of bytes in the datagram."""
    def set_array(self, data: PTA_uchar) -> None:
        """Replaces the data in the Datagram with the data in the indicated PTA_uchar.
        This is assignment by reference: subsequent changes to the Datagram will
        also change the source PTA_uchar.
        """
    def copy_array(self, data: CPTA_uchar | PointerToArray_unsigned_char) -> None:
        """Replaces the data in the Datagram with a copy of the data in the indicated
        CPTA_uchar.  Unlike set_array(), a complete copy is made of the data;
        subsequent changes to the Datagram will *not* change the source CPTA_uchar.
        """
    def get_array(self) -> CPTA_uchar:
        """Returns a const pointer to the actual data in the Datagram."""
    def modify_array(self) -> PTA_uchar:
        """Returns a modifiable pointer to the actual data in the Datagram."""
    def set_stdfloat_double(self, stdfloat_double: bool) -> None:
        """Changes the stdfloat_double flag, which defines the operation performed by
        add_stdfloat() and DatagramIterator::get_stdfloat().  When this is true,
        add_stdfloat() adds a 64-bit floating-point number; when it is false, it
        adds a 32-bit floating-point number.  The default is based on the
        STDFLOAT_DOUBLE compilation flag.
        """
    def get_stdfloat_double(self) -> bool:
        """Returns the stdfloat_double flag.  See set_stdfloat_double()."""
    def output(self, out: ostream) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    dumpHex = dump_hex
    addBool = add_bool
    addInt8 = add_int8
    addUint8 = add_uint8
    addInt16 = add_int16
    addInt32 = add_int32
    addInt64 = add_int64
    addUint16 = add_uint16
    addUint32 = add_uint32
    addUint64 = add_uint64
    addFloat32 = add_float32
    addFloat64 = add_float64
    addStdfloat = add_stdfloat
    addBeInt16 = add_be_int16
    addBeInt32 = add_be_int32
    addBeInt64 = add_be_int64
    addBeUint16 = add_be_uint16
    addBeUint32 = add_be_uint32
    addBeUint64 = add_be_uint64
    addBeFloat32 = add_be_float32
    addBeFloat64 = add_be_float64
    addString = add_string
    addString32 = add_string32
    addZString = add_z_string
    addFixedString = add_fixed_string
    addWstring = add_wstring
    addBlob = add_blob
    addBlob32 = add_blob32
    padBytes = pad_bytes
    appendData = append_data
    getMessage = get_message
    Bytes = __bytes__
    getLength = get_length
    setArray = set_array
    copyArray = copy_array
    getArray = get_array
    modifyArray = modify_array
    setStdfloatDouble = set_stdfloat_double
    getStdfloatDouble = get_stdfloat_double

class DatagramGenerator:
    """This class defines the abstract interace to any source of datagrams,
    whether it be from a file or from the net.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_datagram(self, data: Datagram) -> bool: ...
    def save_datagram(self, info: SubfileInfo) -> bool:
        """Skips over the next datagram without extracting it, but saves the relevant
        file information in the SubfileInfo object so that its data may be read
        later.  For non-file-based datagram generators, this may mean creating a
        temporary file and copying the contents of the datagram to disk.

        Returns true on success, false on failure or if this method is
        unimplemented.
        """
    def is_eof(self) -> bool: ...
    def is_error(self) -> bool: ...
    def get_filename(self) -> Filename:
        """Returns the filename that provides the source for these datagrams, if any,
        or empty string if the datagrams do not originate from a file on disk.
        """
    def get_timestamp(self) -> int:
        """Returns the on-disk timestamp of the file that was read, at the time it was
        opened, if that is available, or 0 if it is not.
        """
    def get_file(self) -> FileReference:
        """Returns the FileReference that provides the source for these datagrams, if
        any, or NULL if the datagrams do not originate from a file on disk.
        """
    def get_vfile(self) -> VirtualFile:
        """Returns the VirtualFile that provides the source for these datagrams, if
        any, or NULL if the datagrams do not originate from a VirtualFile.
        """
    def get_file_pos(self) -> int:
        """Returns the current file position within the data stream, if any, or 0 if
        the file position is not meaningful or cannot be determined.

        For DatagramGenerators that return a meaningful file position, this will be
        pointing to the first byte following the datagram returned after a call to
        get_datagram().
        """
    getDatagram = get_datagram
    saveDatagram = save_datagram
    isEof = is_eof
    isError = is_error
    getFilename = get_filename
    getTimestamp = get_timestamp
    getFile = get_file
    getVfile = get_vfile
    getFilePos = get_file_pos

class DatagramIterator:
    """A class to retrieve the individual data elements previously stored in a
    Datagram.  Elements may be retrieved one at a time; it is up to the caller
    to know the correct type and order of each element.

    Note that it is the responsibility of the caller to ensure that the datagram
    object is not destructed while this DatagramIterator is in use.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: DatagramIterator = ...) -> None: ...
    @overload
    def __init__(self, datagram: Datagram, offset: int = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_bool(self) -> bool:
        """Extracts a boolean value."""
    def get_int8(self) -> str:
        """Extracts a signed 8-bit integer."""
    def get_uint8(self) -> str:
        """Extracts an unsigned 8-bit integer."""
    def get_int16(self) -> int:
        """Extracts a signed 16-bit integer."""
    def get_int32(self) -> int:
        """Extracts a signed 32-bit integer."""
    def get_int64(self) -> int:
        """Extracts a signed 64-bit integer."""
    def get_uint16(self) -> int:
        """Extracts an unsigned 16-bit integer."""
    def get_uint32(self) -> int:
        """Extracts an unsigned 32-bit integer."""
    def get_uint64(self) -> int:
        """Extracts an unsigned 64-bit integer."""
    def get_float32(self) -> float:
        """Extracts a 32-bit single-precision floating-point number."""
    def get_float64(self) -> float:
        """Extracts a 64-bit floating-point number."""
    def get_stdfloat(self) -> float:
        """Extracts either a 32-bit or a 64-bit floating-point number, according to
        Datagram::set_stdfloat_double().
        """
    def get_be_int16(self) -> int:
        """Extracts a signed 16-bit big-endian integer."""
    def get_be_int32(self) -> int:
        """Extracts a signed 32-bit big-endian integer."""
    def get_be_int64(self) -> int:
        """Extracts a signed 64-bit big-endian integer."""
    def get_be_uint16(self) -> int:
        """Extracts an unsigned 16-bit big-endian integer."""
    def get_be_uint32(self) -> int:
        """Extracts an unsigned 32-bit big-endian integer."""
    def get_be_uint64(self) -> int:
        """Extracts an unsigned 64-bit big-endian integer."""
    def get_be_float32(self) -> float:
        """Extracts a 32-bit big-endian single-precision floating-point number."""
    def get_be_float64(self) -> float:
        """Extracts a 64-bit big-endian floating-point number."""
    def get_string(self) -> str:
        """Extracts a variable-length string."""
    def get_string32(self) -> str:
        """Extracts a variable-length string with a 32-bit length field."""
    def get_z_string(self) -> str:
        """Extracts a variable-length string, as a NULL-terminated string."""
    def get_fixed_string(self, size: int) -> str:
        """Extracts a fixed-length string.  However, if a zero byte occurs within the
        string, it marks the end of the string.
        """
    def get_wstring(self) -> str:
        """Extracts a variable-length wstring (with a 32-bit length field)."""
    def get_blob(self) -> bytes:
        """Extracts a variable-length binary blob."""
    def get_blob32(self) -> bytes:
        """Extracts a variable-length binary blob with a 32-bit size field."""
    def skip_bytes(self, size: int) -> None:
        """Skips over the indicated number of bytes in the datagram."""
    def extract_bytes(self, size: int) -> bytes:
        """Extracts the indicated number of bytes in the datagram and returns them as
        a string.
        """
    def get_remaining_bytes(self) -> bytes:
        """Returns the remaining bytes in the datagram as a string, but does not
        extract them from the iterator.
        """
    def get_remaining_size(self) -> int:
        """Return the bytes left in the datagram."""
    def get_datagram(self) -> Datagram:
        """Return the datagram of this iterator."""
    def get_current_index(self) -> int:
        """Returns the current position within the datagram of the next piece of data
        to extract.
        """
    def output(self, out: ostream) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream, indent: int = ...) -> None:
        """Write a string representation of this instance to <out>."""
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getBool = get_bool
    getInt8 = get_int8
    getUint8 = get_uint8
    getInt16 = get_int16
    getInt32 = get_int32
    getInt64 = get_int64
    getUint16 = get_uint16
    getUint32 = get_uint32
    getUint64 = get_uint64
    getFloat32 = get_float32
    getFloat64 = get_float64
    getStdfloat = get_stdfloat
    getBeInt16 = get_be_int16
    getBeInt32 = get_be_int32
    getBeInt64 = get_be_int64
    getBeUint16 = get_be_uint16
    getBeUint32 = get_be_uint32
    getBeUint64 = get_be_uint64
    getBeFloat32 = get_be_float32
    getBeFloat64 = get_be_float64
    getString = get_string
    getString32 = get_string32
    getZString = get_z_string
    getFixedString = get_fixed_string
    getWstring = get_wstring
    getBlob = get_blob
    getBlob32 = get_blob32
    skipBytes = skip_bytes
    extractBytes = extract_bytes
    getRemainingBytes = get_remaining_bytes
    getRemainingSize = get_remaining_size
    getDatagram = get_datagram
    getCurrentIndex = get_current_index
    getClassType = get_class_type

class DatagramSink:
    """This class defines the abstract interface to sending datagrams to any
    target, whether it be into a file or across the net
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def filename(self) -> Filename: ...
    @property
    def file(self) -> FileReference: ...
    @property
    def file_pos(self) -> int: ...
    def put_datagram(self, data: Datagram) -> bool: ...
    @overload
    def copy_datagram(self, result: SubfileInfo, filename: StrOrBytesPath) -> bool:
        """`(self, result: SubfileInfo, filename: Filename)`:
        Copies the file data from the entire indicated file (via the vfs) as the
        next datagram.  This is intended to support potentially very large
        datagrams.

        Returns true on success, false on failure or if this method is
        unimplemented.  On true, fills "result" with the information that
        references the copied file, if possible.

        `(self, result: SubfileInfo, source: SubfileInfo)`:
        Copies the file data from the range of the indicated file (outside of the
        vfs) as the next datagram.  This is intended to support potentially very
        large datagrams.

        Returns true on success, false on failure or if this method is
        unimplemented.  On true, fills "result" with the information that
        references the copied file, if possible.
        """
    @overload
    def copy_datagram(self, result: SubfileInfo, source: SubfileInfo) -> bool: ...
    def is_error(self) -> bool: ...
    def flush(self) -> None: ...
    def get_filename(self) -> Filename:
        """Returns the filename that provides the target for these datagrams, if any,
        or empty string if the datagrams do not get written to a file on disk.
        """
    def get_file(self) -> FileReference:
        """Returns the FileReference that provides the target for these datagrams, if
        any, or NULL if the datagrams do not written to a file on disk.
        """
    def get_file_pos(self) -> int:
        """Returns the current file position within the data stream, if any, or 0 if
        the file position is not meaningful or cannot be determined.

        For DatagramSinks that return a meaningful file position, this will be
        pointing to the first byte following the datagram returned after a call to
        put_datagram().
        """
    putDatagram = put_datagram
    copyDatagram = copy_datagram
    isError = is_error
    getFilename = get_filename
    getFile = get_file
    getFilePos = get_file_pos

class TypedReferenceCount(TypedObject, ReferenceCount):  # type: ignore[misc]
    """A base class for things which need to inherit from both TypedObject and
    from ReferenceCount.  It's convenient to define this intermediate base
    class instead of multiply inheriting from the two classes each time they
    are needed, so that we can sensibly pass around pointers to things which
    are both TypedObjects and ReferenceCounters.

    See also TypedObject for detailed instructions.
    """

    def upcast_to_TypedObject(self) -> TypedObject: ...
    def upcast_to_ReferenceCount(self) -> ReferenceCount: ...
    upcastToTypedObject = upcast_to_TypedObject
    upcastToReferenceCount = upcast_to_ReferenceCount

class FileReference(TypedReferenceCount):
    """Keeps a reference-counted pointer to a file on disk.  As long as the
    FileReference is held, someone presumably has a use for this file.
    """

    @overload
    def __init__(self, __param0: ConfigVariableFilename | FileReference) -> None: ...
    @overload
    def __init__(self, filename: StrOrBytesPath) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_filename(self) -> Filename:
        """Returns the filename of the reference."""
    getFilename = get_filename

class Ramfile:
    """An in-memory buffer specifically designed for downloading files to memory."""

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: Ramfile = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def seek(self, pos: int) -> None:
        """Moves the data pointer to the indicated byte position.  It is not an error
        to move the pointer past the end of data.
        """
    def tell(self) -> int:
        """Returns the current data pointer position as a byte offset from the
        beginning of the stream.
        """
    def read(self, length: int) -> bytes:
        """Extracts and returns the indicated number of characters from the current
        data pointer, and advances the data pointer.  If the data pointer exceeds
        the end of the buffer, returns empty string.

        The interface here is intentionally designed to be similar to that for
        Python's file.read() function.
        """
    def readline(self) -> bytes:
        """Assumes the stream represents a text file, and extracts one line up to and
        including the trailing newline character.  Returns empty string when the
        end of file is reached.

        The interface here is intentionally designed to be similar to that for
        Python's file.readline() function.
        """
    def readlines(self) -> list[bytes]: ...
    def get_data(self) -> bytes:
        """Returns the entire buffer contents as a string, regardless of the current
        data pointer.
        """
    def get_data_size(self) -> int:
        """Returns the size of the entire buffer contents."""
    def clear(self) -> None:
        """Empties the current buffer contents."""
    getData = get_data
    getDataSize = get_data_size

class HashVal:
    """Stores a 128-bit value that represents the hashed contents (typically MD5)
    of a file or buffer.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: HashVal = ...) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: HashVal) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def compare_to(self, other: HashVal) -> int: ...
    def merge_with(self, other: HashVal) -> None:
        """Generates a new HashVal representing the xor of this one and the other one."""
    def output_dec(self, out: ostream) -> None:
        """Outputs the HashVal as four unsigned decimal integers."""
    def input_dec(self, _in: istream) -> None:
        """Inputs the HashVal as four unsigned decimal integers."""
    def output_hex(self, out: ostream) -> None:
        """Outputs the HashVal as a 32-digit hexadecimal number."""
    def input_hex(self, _in: istream) -> None:
        """Inputs the HashVal as a 32-digit hexadecimal number."""
    def output_binary(self, out: ostream) -> None:
        """Outputs the HashVal as a binary stream of bytes in order.  This is not the
        same order generated by write_stream().
        """
    def input_binary(self, _in: istream) -> None:
        """Inputs the HashVal as a binary stream of bytes in order.  This is not the
        same order expected by read_stream().
        """
    def output(self, out: ostream) -> None: ...
    def as_dec(self) -> str:
        """Returns the HashVal as a string with four decimal numbers."""
    def set_from_dec(self, text: str) -> bool:
        """Sets the HashVal from a string with four decimal numbers.  Returns true if
        valid, false otherwise.
        """
    def as_hex(self) -> str:
        """Returns the HashVal as a 32-byte hexadecimal string."""
    def set_from_hex(self, text: str) -> bool:
        """Sets the HashVal from a 32-byte hexademical string.  Returns true if
        successful, false otherwise.
        """
    def as_bin(self) -> bytes:
        """Returns the HashVal as a 16-byte binary string."""
    def set_from_bin(self, text: bytes) -> bool:
        """Sets the HashVal from a 16-byte binary string.  Returns true if successful,
        false otherwise.
        """
    def write_datagram(self, destination: Datagram) -> None: ...
    def read_datagram(self, source: Datagram | DatagramIterator) -> None: ...
    def write_stream(self, destination: StreamWriter) -> None: ...
    def read_stream(self, source: StreamReader) -> None: ...
    def hash_file(self, filename: StrOrBytesPath) -> bool:
        """Generates the hash value from the indicated file.  Returns true on success,
        false if the file cannot be read.  This method is only defined if we have
        the OpenSSL library (which provides md5 functionality) available.
        """
    def hash_stream(self, stream: istream) -> bool:
        """Generates the hash value from the indicated file.  Returns true on success,
        false if the file cannot be read.  This method is only defined if we have
        the OpenSSL library (which provides md5 functionality) available.
        """
    def hash_ramfile(self, ramfile: Ramfile) -> None:
        """Generates the hash value by hashing the indicated data.  This method is
        only defined if we have the OpenSSL library (which provides md5
        functionality) available.
        """
    def hash_string(self, data: str) -> None:
        """Generates the hash value by hashing the indicated data.  This method is
        only defined if we have the OpenSSL library (which provides md5
        functionality) available.
        """
    def hash_bytes(self, data: bytes) -> None:
        """Generates the hash value by hashing the indicated data.  This method is
        only defined if we have the OpenSSL library (which provides md5
        functionality) available.
        """
    def hash_buffer(self, buffer: str, length: int) -> None:
        """Generates the hash value by hashing the indicated data.  This method is
        only defined if we have the OpenSSL library (which provides md5
        functionality) available.
        """
    compareTo = compare_to
    mergeWith = merge_with
    outputDec = output_dec
    inputDec = input_dec
    outputHex = output_hex
    inputHex = input_hex
    outputBinary = output_binary
    inputBinary = input_binary
    asDec = as_dec
    setFromDec = set_from_dec
    asHex = as_hex
    setFromHex = set_from_hex
    asBin = as_bin
    setFromBin = set_from_bin
    writeDatagram = write_datagram
    readDatagram = read_datagram
    writeStream = write_stream
    readStream = read_stream
    hashFile = hash_file
    hashStream = hash_stream
    hashRamfile = hash_ramfile
    hashString = hash_string
    hashBytes = hash_bytes
    hashBuffer = hash_buffer

class MemoryUsagePointers:
    """This is a list of pointers returned by a MemoryUsage object in response to
    some query.

    Warning: once pointers are stored in a MemoryUsagePointers object, they are
    reference-counted, and will not be freed until the MemoryUsagePointers
    object is freed (or clear() is called on the object).  However, they may
    not even be freed then; pointers may leak once they have been added to this
    structure.  This is because we don't store enough information in this
    structure to correctly free the pointers that have been added.  Since this
    is intended primarily as a debugging tool, this is not a major issue.

    This class is just a user interface to talk about pointers stored in a
    MemoryUsage object.  It doesn't even exist when compiled with NDEBUG.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: MemoryUsagePointers = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_num_pointers(self) -> int:
        """Returns the number of pointers in the set."""
    def get_pointer(self, n: int) -> ReferenceCount:
        """Returns the nth pointer of the set."""
    def get_typed_pointer(self, n: int) -> TypedObject:
        """Returns the nth pointer of the set, typecast to a TypedObject if possible.
        If the pointer is not a TypedObject or if the cast cannot be made, returns
        nullptr.
        """
    def get_type(self, n: int) -> TypeHandle:
        """Returns the actual type of the nth pointer, if it is known."""
    def get_type_name(self, n: int) -> str:
        """Returns the type name of the nth pointer, if it is known."""
    def get_age(self, n: int) -> float:
        """Returns the age of the nth pointer: the number of seconds elapsed between
        the time it was allocated and the time it was added to this set via a call
        to MemoryUsage::get_pointers().
        """
    def get_python_pointer(self, n: int): ...
    def clear(self) -> None:
        """Empties the set of pointers."""
    def output(self, out: ostream) -> None: ...
    def get_pointers(self) -> tuple[ReferenceCount, ...]: ...
    def get_typed_pointers(self) -> tuple[TypedObject, ...]: ...
    getNumPointers = get_num_pointers
    getPointer = get_pointer
    getTypedPointer = get_typed_pointer
    getType = get_type
    getTypeName = get_type_name
    getAge = get_age
    getPythonPointer = get_python_pointer
    getPointers = get_pointers
    getTypedPointers = get_typed_pointers

class ISubStream(istream):
    """An istream object that presents a subwindow into another istream.  The
    first character read from this stream will be the "start" character from
    the source istream; just before the file pointer reaches the "end"
    character, eof is returned.

    The source stream must be one that we can randomly seek within.  The
    resulting ISubStream will also support arbitrary seeks.
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, source: IStreamWrapper, start: int, end: int) -> None: ...
    def open(self, source: IStreamWrapper, start: int, end: int) -> ISubStream:
        """Starts the SubStream reading from the indicated source, with the first
        character being the character at position "start" within the source, for
        end - start total characters.  The character at "end" within the source
        will never be read; this will appear to be EOF.

        If end is zero, it indicates that the ISubStream will continue until the
        end of the source stream.
        """
    def close(self) -> ISubStream:
        """Resets the SubStream to empty, but does not actually close the source
        istream.
        """

class OSubStream(ostream):
    """An ostream object that presents a subwindow into another ostream.  The
    first character written to this stream will be the "start" character in the
    dest istream; no characters may be written to character "end" or later
    (unless end is zero).

    The dest stream must be one that we can randomly seek within.  The
    resulting OSubStream will also support arbitrary seeks.
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, dest: OStreamWrapper, start: int, end: int, append: bool = ...) -> None: ...
    def open(self, dest: OStreamWrapper, start: int, end: int, append: bool = ...) -> OSubStream:
        """Starts the SubStream reading from the indicated dest, with the first
        character being the character at position "start" within the dest, for end
        - start total characters.  The character at "end" within the dest will
        never be read; this will appear to be EOF.

        If end is zero, it indicates that the OSubStream will continue until the
        end of the dest stream.
        """
    def close(self) -> OSubStream:
        """Resets the SubStream to empty, but does not actually close the dest
        ostream.
        """

class SubStream(iostream):
    """Combined ISubStream and OSubStream for bidirectional I/O."""

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, nested: StreamWrapper, start: int, end: int, append: bool = ...) -> None: ...
    def open(self, nested: StreamWrapper, start: int, end: int, append: bool = ...) -> SubStream:
        """Starts the SubStream reading and writing from the indicated nested stream,
        within the indicated range.  "end" is the first character outside of the
        range.

        If end is zero, it indicates that the SubStream will continue until the end
        of the nested stream.
        """
    def close(self) -> SubStream:
        """Resets the SubStream to empty, but does not actually close the nested
        ostream.
        """

class Multifile(ReferenceCount):
    """A file that contains a set of files."""

    @property
    def magic_number(self) -> str: ...
    def __init__(self) -> None: ...
    @overload
    def open_read(self, multifile_name: StrOrBytesPath, offset: int = ...) -> bool:
        """`(self, multifile_name: Filename, offset: int = ...)`:
        Opens the named Multifile on disk for reading.  The Multifile index is read
        in, and the list of subfiles becomes available; individual subfiles may
        then be extracted or read, but the list of subfiles may not be modified.

        Also see the version of open_read() which accepts an istream.  Returns true
        on success, false on failure.

        `(self, multifile_stream: IStreamWrapper, owns_pointer: bool = ..., offset: int = ...)`:
        Opens an anonymous Multifile for reading using an istream.  There must be
        seek functionality via seekg() and tellg() on the istream.

        If owns_pointer is true, then the Multifile assumes ownership of the stream
        pointer and will delete it when the multifile is closed, including if this
        function returns false.
        """
    @overload
    def open_read(self, multifile_stream: IStreamWrapper, owns_pointer: bool = ..., offset: int = ...) -> bool: ...
    @overload
    def open_write(self, multifile_name: StrOrBytesPath) -> bool:
        """`(self, multifile_name: Filename)`:
        Opens the named Multifile on disk for writing.  If there already exists a
        file by that name, it is truncated.  The Multifile is then prepared for
        accepting a brand new set of subfiles, which will be written to the
        indicated filename.  Individual subfiles may not be extracted or read.

        Also see the version of open_write() which accepts an ostream.  Returns
        true on success, false on failure.

        `(self, multifile_stream: ostream, owns_pointer: bool = ...)`:
        Opens an anonymous Multifile for writing using an ostream.  There must be
        seek functionality via seekp() and tellp() on the pstream.

        If owns_pointer is true, then the Multifile assumes ownership of the stream
        pointer and will delete it when the multifile is closed, including if this
        function returns false.
        """
    @overload
    def open_write(self, multifile_stream: ostream, owns_pointer: bool = ...) -> bool: ...
    @overload
    def open_read_write(self, multifile_name: StrOrBytesPath) -> bool:
        """`(self, multifile_name: Filename)`:
        Opens the named Multifile on disk for reading and writing.  If there
        already exists a file by that name, its index is read.  Subfiles may be
        added or removed, and the resulting changes will be written to the named
        file.

        Also see the version of open_read_write() which accepts an iostream.
        Returns true on success, false on failure.

        `(self, multifile_stream: iostream, owns_pointer: bool = ...)`:
        Opens an anonymous Multifile for reading and writing using an iostream.
        There must be seek functionality via seekg()/seekp() and tellg()/tellp() on
        the iostream.

        If owns_pointer is true, then the Multifile assumes ownership of the stream
        pointer and will delete it when the multifile is closed, including if this
        function returns false.
        """
    @overload
    def open_read_write(self, multifile_stream: iostream, owns_pointer: bool = ...) -> bool: ...
    def close(self) -> None:
        """Closes the Multifile if it is open.  All changes are flushed to disk, and
        the file becomes invalid for further operations until the next call to
        open().
        """
    def get_multifile_name(self) -> Filename:
        """Returns the filename of the Multifile, if it is available."""
    def set_multifile_name(self, multifile_name: StrOrBytesPath) -> None:
        """Replaces the filename of the Multifile.  This is primarily used for
        documentation purposes only; changing this name does not open the indicated
        file.  See open_read() or open_write() for that.
        """
    def is_read_valid(self) -> bool:
        """Returns true if the Multifile has been opened for read mode and there have
        been no errors, and individual Subfile contents may be extracted.
        """
    def is_write_valid(self) -> bool:
        """Returns true if the Multifile has been opened for write mode and there have
        been no errors, and Subfiles may be added or removed from the Multifile.
        """
    def needs_repack(self) -> bool:
        """Returns true if the Multifile index is suboptimal and should be repacked.
        Call repack() to achieve this.
        """
    def get_timestamp(self) -> int:
        """Returns the modification timestamp of the overall Multifile.  This
        indicates the most recent date at which subfiles were added or removed from
        the Multifile.  Note that it is logically possible for an individual
        subfile to have a more recent timestamp than the overall timestamp.
        """
    def set_timestamp(self, timestamp: int) -> None:
        """Changes the overall mudification timestamp of the multifile.  Note that this
        will be reset to the current time every time you modify a subfile.
        Only set this if you know what you are doing!
        """
    def set_record_timestamp(self, record_timestamp: bool) -> None:
        """Sets the flag indicating whether timestamps should be recorded within the
        Multifile or not.  The default is true, indicating the Multifile will
        record timestamps for the overall file and also for each subfile.

        If this is false, the Multifile will not record timestamps internally.  In
        this case, the return value from get_timestamp() or get_subfile_timestamp()
        will be estimations.

        You may want to set this false to minimize the bitwise difference between
        independently-generated Multifiles.
        """
    def get_record_timestamp(self) -> bool:
        """Returns the flag indicating whether timestamps should be recorded within
        the Multifile or not.  See set_record_timestamp().
        """
    def set_scale_factor(self, scale_factor: int) -> None:
        """Changes the internal scale factor for this Multifile.

        This is normally 1, but it may be set to any arbitrary value (greater than
        zero) to support Multifile archives that exceed 4GB, if necessary.
        (Individual subfiles may still not exceed 4GB.)

        All addresses within the file are rounded up to the next multiple of
        _scale_factor, and zeros are written to the file to fill the resulting
        gaps.  Then the address is divided by _scale_factor and written out as a
        32-bit integer.  Thus, setting a scale factor of 2 supports up to 8GB
        files, 3 supports 12GB files, etc.

        Calling this function on an already-existing Multifile will have no
        immediate effect until a future call to repack() or close() (or until the
        Multifile is destructed).
        """
    def get_scale_factor(self) -> int:
        """Returns the internal scale factor for this Multifile.  See
        set_scale_factor().
        """
    def set_encryption_flag(self, flag: bool) -> None:
        """Sets the flag indicating whether subsequently-added subfiles should be
        encrypted before writing them to the multifile.  If true, subfiles will be
        encrypted; if false (the default), they will be written without encryption.

        When true, subfiles will be encrypted with the password specified by
        set_encryption_password().  It is possible to apply a different password to
        different files, but the resulting file can't be mounted via VFS.
        """
    def get_encryption_flag(self) -> bool:
        """Returns the flag indicating whether subsequently-added subfiles should be
        encrypted before writing them to the multifile.  See set_encryption_flag().
        """
    def set_encryption_password(self, encryption_password: str) -> None:
        """Specifies the password that will be used to encrypt subfiles subsequently
        added to the multifile, if the encryption flag is also set true (see
        set_encryption_flag()).

        It is possible to apply a different password to different files, but the
        resulting file can't be mounted via VFS.  Changing this value may cause an
        implicit call to flush().
        """
    def get_encryption_password(self) -> str:
        """Returns the password that will be used to encrypt subfiles subsequently
        added to the multifile.  See set_encryption_password().
        """
    def set_encryption_algorithm(self, encryption_algorithm: str) -> None:
        """Specifies the encryption algorithm that should be used for future calls to
        add_subfile().  The default is whatever is specified by the encryption-
        algorithm config variable.  The complete set of available algorithms is
        defined by the current version of OpenSSL.

        If an invalid algorithm is specified, there is no immediate error return
        code, but flush() will fail and the file will be invalid.

        It is possible to apply a different encryption algorithm to different
        files, and unlike the password, this does not interfere with mounting the
        multifile via VFS.  Changing this value may cause an implicit call to
        flush().
        """
    def get_encryption_algorithm(self) -> str:
        """Returns the encryption algorithm that was specified by
        set_encryption_algorithm().
        """
    def set_encryption_key_length(self, encryption_key_length: int) -> None:
        """Specifies the length of the key, in bits, that should be used to encrypt
        the stream in future calls to add_subfile().  The default is whatever is
        specified by the encryption-key-length config variable.

        If an invalid key_length for the chosen algorithm is specified, there is no
        immediate error return code, but flush() will fail and the file will be
        invalid.

        It is possible to apply a different key length to different files, and
        unlike the password, this does not interfere with mounting the multifile
        via VFS. Changing this value may cause an implicit call to flush().
        """
    def get_encryption_key_length(self) -> int:
        """Returns the encryption key length, in bits, that was specified by
        set_encryption_key_length().
        """
    def set_encryption_iteration_count(self, encryption_iteration_count: int) -> None:
        """Specifies the number of times to repeatedly hash the key before writing it
        to the stream in future calls to add_subfile().  Its purpose is to make it
        computationally more expensive for an attacker to search the key space
        exhaustively.  This should be a multiple of 1,000 and should not exceed
        about 65 million; the value 0 indicates just one application of the hashing
        algorithm.

        The default is whatever is specified by the multifile-encryption-iteration-
        count config variable.

        It is possible to apply a different iteration count to different files, and
        unlike the password, this does not interfere with mounting the multifile
        via VFS.  Changing this value causes an implicit call to flush().
        """
    def get_encryption_iteration_count(self) -> int:
        """Returns the value that was specified by set_encryption_iteration_count()."""
    @overload
    def add_subfile(self, subfile_name: str, filename: StrOrBytesPath, compression_level: int) -> str:
        """`(self, subfile_name: str, filename: Filename, compression_level: int)`:
        Adds a file on disk as a subfile to the Multifile.  The file named by
        filename will be read and added to the Multifile at the next call to
        flush().  If there already exists a subfile with the indicated name, it is
        replaced without examining its contents (but see also update_subfile).

        Either Filename:::set_binary() or set_text() must have been called
        previously to specify the nature of the source file.  If set_text() was
        called, the text flag will be set on the subfile.

        Returns the subfile name on success (it might have been modified slightly),
        or empty string on failure.

        `(self, subfile_name: str, subfile_data: istream, compression_level: int)`:
        Adds a file from a stream as a subfile to the Multifile.  The indicated
        istream will be read and its contents added to the Multifile at the next
        call to flush(). The file will be added as a binary subfile.

        Note that the istream must remain untouched and unused by any other code
        until flush() is called.  At that time, the Multifile will read the entire
        contents of the istream from the current file position to the end of the
        file.  Subsequently, the Multifile will *not* close or delete the istream.
        It is the caller's responsibility to ensure that the istream pointer does
        not destruct during the lifetime of the Multifile.

        Returns the subfile name on success (it might have been modified slightly),
        or empty string on failure.
        """
    @overload
    def add_subfile(self, subfile_name: str, subfile_data: istream, compression_level: int) -> str: ...
    def update_subfile(self, subfile_name: str, filename: StrOrBytesPath, compression_level: int) -> str:
        """Adds a file on disk to the subfile.  If a subfile already exists with the
        same name, its contents are compared byte-for-byte to the disk file, and it
        is replaced only if it is different; otherwise, the multifile is left
        unchanged.

        Either Filename:::set_binary() or set_text() must have been called
        previously to specify the nature of the source file.  If set_text() was
        called, the text flag will be set on the subfile.
        """
    @overload
    def add_signature(self, composite: StrOrBytesPath, password: str = ...) -> bool:
        """`(self, certificate: Filename, chain: Filename, pkey: Filename, password: str = ...)`:
        Adds a new signature to the Multifile.  This signature associates the
        indicated certificate with the current contents of the Multifile.  When the
        Multifile is read later, the signature will still be present only if the
        Multifile is unchanged; any subsequent changes to the Multifile will
        automatically invalidate and remove the signature.

        The chain filename may be empty if the certificate does not require an
        authenticating certificate chain (e.g.  because it is self-signed).

        The specified private key must match the certificate, and the Multifile
        must be open in read-write mode.  The private key is only used for
        generating the signature; it is not written to the Multifile and cannot be
        retrieved from the Multifile later.  (However, the certificate *can* be
        retrieved from the Multifile later, to identify the entity that created the
        signature.)

        This implicitly causes a repack() operation if one is needed.  Returns true
        on success, false on failure.

        This flavor of add_signature() reads the certificate and private key from a
        PEM-formatted file, for instance as generated by the openssl command.  If
        the private key file is password-encrypted, the third parameter will be
        used as the password to decrypt it.

        `(self, composite: Filename, password: str = ...)`:
        Adds a new signature to the Multifile.  This signature associates the
        indicated certificate with the current contents of the Multifile.  When the
        Multifile is read later, the signature will still be present only if the
        Multifile is unchanged; any subsequent changes to the Multifile will
        automatically invalidate and remove the signature.

        This flavor of add_signature() reads the certificate, private key, and
        certificate chain from the same PEM-formatted file.  It takes the first
        private key found as the intended key, and then uses the first certificate
        found that matches that key as the signing certificate.  Any other
        certificates in the file are taken to be part of the chain.
        """
    @overload
    def add_signature(
        self, certificate: StrOrBytesPath, chain: StrOrBytesPath, pkey: StrOrBytesPath, password: str = ...
    ) -> bool: ...
    def get_num_signatures(self) -> int:
        """Returns the number of matching signatures found on the Multifile.  These
        signatures may be iterated via get_signature() and related methods.

        A signature on this list is guaranteed to match the Multifile contents,
        proving that the Multifile has been unmodified since the signature was
        applied.  However, this does not guarantee that the certificate itself is
        actually from who it says it is from; only that it matches the Multifile
        contents.  See validate_signature_certificate() to authenticate a
        particular certificate.
        """
    def get_signature_subject_name(self, n: int) -> str:
        """Returns the "subject name" for the nth signature found on the Multifile.
        This is a string formatted according to RFC2253 that should more-or-less
        identify a particular certificate; when paired with the public key (see
        get_signature_public_key()), it can uniquely identify a certificate.  See
        the comments in get_num_signatures().
        """
    def get_signature_friendly_name(self, n: int) -> str:
        """Returns a "friendly name" for the nth signature found on the Multifile.
        This attempts to extract out the most meaningful part of the subject name.
        It returns the emailAddress, if it is defined; otherwise, it returns the
        commonName.

        See the comments in get_num_signatures().
        """
    def get_signature_public_key(self, n: int) -> str:
        """Returns the public key used for the nth signature found on the Multifile.
        This is encoded in DER form and returned as a string of hex digits.

        This can be used, in conjunction with the subject name (see
        get_signature_subject_name()), to uniquely identify a particular
        certificate and its subsequent reissues.  See the comments in
        get_num_signatures().
        """
    def print_signature_certificate(self, n: int, out: ostream) -> None:
        """Writes the certificate for the nth signature, in user-readable verbose
        form, to the indicated stream.  See the comments in get_num_signatures().
        """
    def write_signature_certificate(self, n: int, out: ostream) -> None:
        """Writes the certificate for the nth signature, in PEM form, to the indicated
        stream.  See the comments in get_num_signatures().
        """
    def validate_signature_certificate(self, n: int) -> int:
        """Checks that the certificate used for the nth signature is a valid,
        authorized certificate with some known certificate authority.  Returns 0 if
        it is valid, -1 if there is some error, or the corresponding OpenSSL error
        code if it is invalid, out-of-date, or self-signed.
        """
    def flush(self) -> bool:
        """Writes all contents of the Multifile to disk.  Until flush() is called,
        add_subfile() and remove_subfile() do not actually do anything to disk.  At
        this point, all of the recently-added subfiles are read and their contents
        are added to the end of the Multifile, and the recently-removed subfiles
        are marked gone from the Multifile.

        This may result in a suboptimal index.  To guarantee that the index is
        written at the beginning of the file, call repack() instead of flush().

        It is not necessary to call flush() explicitly unless you are concerned
        about reading the recently-added subfiles immediately.

        Returns true on success, false on failure.
        """
    def repack(self) -> bool:
        """Forces a complete rewrite of the Multifile and all of its contents, so that
        its index will appear at the beginning of the file with all of the subfiles
        listed in alphabetical order.  This is considered optimal for reading, and
        is the standard configuration; but it is not essential to do this.

        It is only valid to call this if the Multifile was opened using
        open_read_write() and an explicit filename, rather than an iostream.  Also,
        we must have write permission to the directory containing the Multifile.

        Returns true on success, false on failure.
        """
    def get_num_subfiles(self) -> int:
        """Returns the number of subfiles within the Multifile.  The subfiles may be
        accessed in alphabetical order by iterating through [0 ..
        get_num_subfiles()).
        """
    def find_subfile(self, subfile_name: str) -> int:
        """Returns the index of the subfile with the indicated name, or -1 if the
        named subfile is not within the Multifile.
        """
    def has_directory(self, subfile_name: str) -> bool:
        """Returns true if the indicated subfile name is the directory prefix to one
        or more files within the Multifile.  That is, the Multifile contains at
        least one file named "subfile_name/...".
        """
    @overload
    def remove_subfile(self, index: int) -> None:
        """`(self, index: int)`:
        Removes the nth subfile from the Multifile.  This will cause all subsequent
        index numbers to decrease by one.  The file will not actually be removed
        from the disk until the next call to flush().

        Note that this does not actually remove the data from the indicated
        subfile; it simply removes it from the index.  The Multifile will not be
        reduced in size after this operation, until the next call to repack().

        `(self, subfile_name: str)`:
        Removes the named subfile from the Multifile, if it exists; returns true if
        successfully removed, or false if it did not exist in the first place.  The
        file will not actually be removed from the disk until the next call to
        flush().

        Note that this does not actually remove the data from the indicated
        subfile; it simply removes it from the index.  The Multifile will not be
        reduced in size after this operation, until the next call to repack().
        """
    @overload
    def remove_subfile(self, subfile_name: str) -> bool: ...
    def get_subfile_name(self, index: int) -> str:
        """Returns the name of the nth subfile."""
    def get_subfile_length(self, index: int) -> int:
        """Returns the uncompressed data length of the nth subfile.  This might return
        0 if the subfile has recently been added and flush() has not yet been
        called.
        """
    def get_subfile_timestamp(self, index: int) -> int:
        """Returns the modification time of the nth subfile.  If this is called on an
        older .mf file, which did not store individual timestamps in the file (or
        if get_record_timestamp() is false), this will return the modification time
        of the overall multifile.
        """
    def is_subfile_compressed(self, index: int) -> bool:
        """Returns true if the indicated subfile has been compressed when stored
        within the archive, false otherwise.
        """
    def is_subfile_encrypted(self, index: int) -> bool:
        """Returns true if the indicated subfile has been encrypted when stored within
        the archive, false otherwise.
        """
    def is_subfile_text(self, index: int) -> bool:
        """Returns true if the indicated subfile represents text data, or false if it
        represents binary data.  If the file is text data, it may have been
        processed by end-of-line conversion when it was added.  (But the actual
        bits in the multifile will represent the standard Unix end-of-line
        convention, e.g.  \\n instead of \\r\\n.)
        """
    def get_index_end(self) -> int:
        """Returns the first byte that is guaranteed to follow any index byte already
        written to disk in the Multifile.

        This number is largely meaningless in many cases, but if needs_repack() is
        false, and the file is flushed, this will indicate the number of bytes in
        the header + index.  Everything at this byte position and later will be
        actual data.
        """
    def get_subfile_internal_start(self, index: int) -> int:
        """Returns the starting byte position within the Multifile at which the
        indicated subfile begins.  This may be used, with
        get_subfile_internal_length(), for low-level access to the subfile, but
        usually it is better to use open_read_subfile() instead (which
        automatically decrypts and/or uncompresses the subfile data).
        """
    def get_subfile_internal_length(self, index: int) -> int:
        """Returns the number of bytes the indicated subfile consumes within the
        archive.  For compressed subfiles, this will generally be smaller than
        get_subfile_length(); for encrypted (but noncompressed) subfiles, it may be
        slightly different, for noncompressed and nonencrypted subfiles, it will be
        equal.
        """
    def read_subfile(self, index: int) -> bytes:
        """Returns a vector_uchar that contains the entire contents of the indicated
        subfile.
        """
    def open_read_subfile(self, index: int) -> istream:
        """Returns an istream that may be used to read the indicated subfile.  You may
        seek() within this istream to your heart's content; even though it will be
        a reference to the already-opened pfstream of the Multifile itself, byte 0
        appears to be the beginning of the subfile and EOF appears to be the end of
        the subfile.

        The returned istream will have been allocated via new; you should pass the
        pointer to close_read_subfile() when you are finished with it to delete it
        and release its resources.

        Any future calls to repack() or close() (or the Multifile destructor) will
        invalidate all currently open subfile pointers.

        The return value will be NULL if the stream cannot be opened for some
        reason.
        """
    @staticmethod
    def close_read_subfile(stream: istream) -> None:
        """Closes a file opened by a previous call to open_read_subfile().  This
        really just deletes the istream pointer, but it is recommended to use this
        interface instead of deleting it explicitly, to help work around compiler
        issues.
        """
    def extract_subfile(self, index: int, filename: StrOrBytesPath) -> bool:
        """Extracts the nth subfile into a file with the given name."""
    def extract_subfile_to(self, index: int, out: ostream) -> bool:
        """Extracts the nth subfile to the indicated ostream."""
    def compare_subfile(self, index: int, filename: StrOrBytesPath) -> bool:
        """Performs a byte-for-byte comparison of the indicated file on disk with the
        nth subfile.  Returns true if the files are equivalent, or false if they
        are different (or the file is missing).

        If Filename::set_binary() or set_text() has already been called, it
        specifies the nature of the source file.  If this is different from the
        text flag of the subfile, the comparison will always return false.  If this
        has not been specified, it will be set from the text flag of the subfile.
        """
    def output(self, out: ostream) -> None: ...
    def ls(self, out: ostream = ...) -> None:
        """Shows a list of all subfiles within the Multifile."""
    @staticmethod
    def get_magic_number() -> str:
        """Returns a string with the first n bytes written to a Multifile, to identify
        it as a Multifile.
        """
    def set_header_prefix(self, header_prefix: str) -> None:
        """Sets the string which is written to the Multifile before the Multifile
        header.  This string must begin with a hash mark and end with a newline
        character; and if it includes embedded newline characters, each one must be
        followed by a hash mark.  If these conditions are not initially true, the
        string will be modified as necessary to make it so.

        This is primarily useful as a simple hack to allow p3d applications to be
        run directly from the command line on Unix-like systems.

        The return value is true if successful, or false on failure (for instance,
        because the header prefix violates the above rules).
        """
    def get_header_prefix(self) -> str:
        """Returns the string that preceded the Multifile header on the file, if any.
        See set_header_prefix().
        """
    def get_subfile_names(self) -> tuple[str, ...]: ...
    openRead = open_read
    openWrite = open_write
    openReadWrite = open_read_write
    getMultifileName = get_multifile_name
    setMultifileName = set_multifile_name
    isReadValid = is_read_valid
    isWriteValid = is_write_valid
    needsRepack = needs_repack
    getTimestamp = get_timestamp
    setTimestamp = set_timestamp
    setRecordTimestamp = set_record_timestamp
    getRecordTimestamp = get_record_timestamp
    setScaleFactor = set_scale_factor
    getScaleFactor = get_scale_factor
    setEncryptionFlag = set_encryption_flag
    getEncryptionFlag = get_encryption_flag
    setEncryptionPassword = set_encryption_password
    getEncryptionPassword = get_encryption_password
    setEncryptionAlgorithm = set_encryption_algorithm
    getEncryptionAlgorithm = get_encryption_algorithm
    setEncryptionKeyLength = set_encryption_key_length
    getEncryptionKeyLength = get_encryption_key_length
    setEncryptionIterationCount = set_encryption_iteration_count
    getEncryptionIterationCount = get_encryption_iteration_count
    addSubfile = add_subfile
    updateSubfile = update_subfile
    addSignature = add_signature
    getNumSignatures = get_num_signatures
    getSignatureSubjectName = get_signature_subject_name
    getSignatureFriendlyName = get_signature_friendly_name
    getSignaturePublicKey = get_signature_public_key
    printSignatureCertificate = print_signature_certificate
    writeSignatureCertificate = write_signature_certificate
    validateSignatureCertificate = validate_signature_certificate
    getNumSubfiles = get_num_subfiles
    findSubfile = find_subfile
    hasDirectory = has_directory
    removeSubfile = remove_subfile
    getSubfileName = get_subfile_name
    getSubfileLength = get_subfile_length
    getSubfileTimestamp = get_subfile_timestamp
    isSubfileCompressed = is_subfile_compressed
    isSubfileEncrypted = is_subfile_encrypted
    isSubfileText = is_subfile_text
    getIndexEnd = get_index_end
    getSubfileInternalStart = get_subfile_internal_start
    getSubfileInternalLength = get_subfile_internal_length
    readSubfile = read_subfile
    openReadSubfile = open_read_subfile
    closeReadSubfile = close_read_subfile
    extractSubfile = extract_subfile
    extractSubfileTo = extract_subfile_to
    compareSubfile = compare_subfile
    getMagicNumber = get_magic_number
    setHeaderPrefix = set_header_prefix
    getHeaderPrefix = get_header_prefix
    getSubfileNames = get_subfile_names

class Namable:
    """A base class for all things which can have a name.  The name is either
    empty or nonempty, but it is never NULL.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    name: str
    @overload
    def __init__(self, initial_name: str = ...) -> None: ...
    @overload
    def __init__(self, __param0: Namable) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_name(self, name: str) -> None: ...
    def clear_name(self) -> None:
        """Resets the Namable's name to empty."""
    def has_name(self) -> bool:
        """Returns true if the Namable has a nonempty name set, false if the name is
        empty.
        """
    def get_name(self) -> str: ...
    def output(self, out: ostream) -> None:
        """Outputs the Namable.  This function simply writes the name to the output
        stream; most Namable derivatives will probably redefine this.
        """
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setName = set_name
    clearName = clear_name
    hasName = has_name
    getName = get_name
    getClassType = get_class_type

class OpenSSLWrapper:
    """Provides an interface wrapper around the OpenSSL library, to ensure that
    the library is properly initialized in the application, and to provide some
    hooks into global OpenSSL context data.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def clear_certificates(self) -> None:
        """Removes all the certificates from the global store, including the compiled-
        in certificates loaded from ca_bundle_data.c.  You can add new certificates
        by calling load_certificates().
        """
    def load_certificates(self, filename: StrOrBytesPath) -> int:
        """Reads the PEM-formatted certificate(s) (delimited by -----BEGIN
        CERTIFICATE----- and -----END CERTIFICATE-----) from the indicated file and
        adds them to the global store object, retrieved via get_x509_store().

        Returns the number of certificates read on success, or 0 on failure.

        You should call this only with trusted, locally-stored certificates; not
        with certificates received from an untrusted source.
        """
    def load_certificates_from_pem_ram(self, data: str, data_size: int = ...) -> int:
        """Reads a chain of trusted certificates from the indicated data buffer and
        adds them to the X509_STORE object.  The data buffer should be PEM-
        formatted.  Returns the number of certificates read on success, or 0 on
        failure.

        You should call this only with trusted, locally-stored certificates; not
        with certificates received from an untrusted source.
        """
    def load_certificates_from_der_ram(self, data: str, data_size: int = ...) -> int:
        """Reads a chain of trusted certificates from the indicated data buffer and
        adds them to the X509_STORE object.  The data buffer should be DER-
        formatted.  Returns the number of certificates read on success, or 0 on
        failure.

        You should call this only with trusted, locally-stored certificates; not
        with certificates received from an untrusted source.
        """
    def notify_ssl_errors(self) -> None:
        """A convenience function that is itself a wrapper around the OpenSSL
        convenience function to output the recent OpenSSL errors.  This function
        sends the error string to express_cat.warning().  If REPORT_OPENSSL_ERRORS
        is not defined, the function does nothing.
        """
    def notify_debug_ssl_errors(self) -> None:
        """As notify_ssl_errors(), but sends the output to debug instead of warning."""
    @staticmethod
    def get_global_ptr() -> OpenSSLWrapper: ...
    clearCertificates = clear_certificates
    loadCertificates = load_certificates
    loadCertificatesFromPemRam = load_certificates_from_pem_ram
    loadCertificatesFromDerRam = load_certificates_from_der_ram
    notifySslErrors = notify_ssl_errors
    notifyDebugSslErrors = notify_debug_ssl_errors
    getGlobalPtr = get_global_ptr

class SubfileInfo:
    """This class records a particular byte sub-range within an existing file on
    disk.  Generally, the filename is understood as a physical file on disk,
    and not to be looked up via the vfs.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: SubfileInfo = ...) -> None: ...
    @overload
    def __init__(self, file: ConfigVariableFilename | FileReference, start: int, size: int) -> None: ...
    @overload
    def __init__(self, filename: StrOrBytesPath, start: int, size: int) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def is_empty(self) -> bool:
        """Returns true if this SubfileInfo doesn't define any file, false if it has
        real data.
        """
    def get_file(self) -> FileReference:
        """Returns the FileReference that represents this file."""
    def get_filename(self) -> Filename:
        """A shortcut to the filename."""
    def get_start(self) -> int:
        """Returns the offset within the file at which this file data begins."""
    def get_size(self) -> int:
        """Returns the number of consecutive bytes, beginning at get_start(), that
        correspond to this file data.
        """
    def output(self, out: ostream) -> None: ...
    isEmpty = is_empty
    getFile = get_file
    getFilename = get_filename
    getStart = get_start
    getSize = get_size

class VirtualFile(TypedReferenceCount):
    """The abstract base class for a file or directory within the
    VirtualFileSystem.
    """

    def get_file_system(self) -> VirtualFileSystem: ...
    def get_filename(self) -> Filename: ...
    def get_original_filename(self) -> Filename:
        """Returns the original filename as it was used to locate this VirtualFile.
        This is usually, but not always, the same string returned by
        get_filename().
        """
    def has_file(self) -> bool:
        """Returns true if this file exists, false otherwise."""
    def is_directory(self) -> bool:
        """Returns true if this file represents a directory (and scan_directory() may
        be called), false otherwise.
        """
    def is_regular_file(self) -> bool:
        """Returns true if this file represents a regular file (and read_file() may be
        called), false otherwise.
        """
    def is_writable(self) -> bool:
        """Returns true if this file may be written to, which implies write_file() may
        be called (unless it is a directory instead of a regular file).
        """
    def delete_file(self) -> bool:
        """Attempts to delete this file or directory.  This can remove a single file
        or an empty directory.  It will not remove a nonempty directory.  Returns
        true on success, false on failure.
        """
    def rename_file(self, new_file: VirtualFile) -> bool:
        """Attempts to move or rename this file or directory.  If the original file is
        an ordinary file, it will quietly replace any already-existing file in the
        new filename (but not a directory).  If the original file is a directory,
        the new filename must not already exist.

        If the file is a directory, the new filename must be within the same mount
        point.  If the file is an ordinary file, the new filename may be anywhere;
        but if it is not within the same mount point then the rename operation is
        automatically performed as a two-step copy-and-delete operation.
        """
    def copy_file(self, new_file: VirtualFile) -> bool:
        """Attempts to copy the contents of this file to the indicated file.  Returns
        true on success, false on failure.
        """
    def scan_directory(self) -> VirtualFileList:
        """If the file represents a directory (that is, is_directory() returns true),
        this returns the list of files within the directory at the current time.
        Returns NULL if the file is not a directory or if the directory cannot be
        read.
        """
    def output(self, out: ostream) -> None: ...
    def ls(self, out: ostream = ...) -> None:
        """If the file represents a directory, lists its contents."""
    def ls_all(self, out: ostream = ...) -> None:
        """If the file represents a directory, recursively lists its contents and
        those of all subdirectories.
        """
    def read_file(self, auto_unwrap: bool) -> bytes:
        """Returns the entire contents of the file as a string."""
    def open_read_file(self, auto_unwrap: bool) -> istream:
        """Opens the file for reading.  Returns a newly allocated istream on success
        (which you should eventually delete when you are done reading). Returns
        NULL on failure.
        """
    def close_read_file(self, stream: istream) -> None:
        """Closes a file opened by a previous call to open_read_file().  This really
        just deletes the istream pointer, but it is recommended to use this
        interface instead of deleting it explicitly, to help work around compiler
        issues.
        """
    def was_read_successful(self) -> bool:
        """Call this method after a reading the istream returned by open_read_file()
        to completion.  If it returns true, the file was read completely and
        without error; if it returns false, there may have been some errors or a
        truncated file read.  This is particularly likely if the stream is a
        VirtualFileHTTP.
        """
    def write_file(self, data, auto_wrap: bool): ...
    def open_write_file(self, auto_wrap: bool, truncate: bool) -> ostream:
        """Opens the file for writing.  Returns a newly allocated ostream on success
        (which you should eventually delete when you are done writing). Returns
        NULL on failure.
        """
    def open_append_file(self) -> ostream:
        """Works like open_write_file(), but the file is opened in append mode.  Like
        open_write_file, the returned pointer should eventually be passed to
        close_write_file().
        """
    def close_write_file(self, stream: ostream) -> None:
        """Closes a file opened by a previous call to open_write_file().  This really
        just deletes the ostream pointer, but it is recommended to use this
        interface instead of deleting it explicitly, to help work around compiler
        issues.
        """
    def open_read_write_file(self, truncate: bool) -> iostream:
        """Opens the file for writing.  Returns a newly allocated iostream on success
        (which you should eventually delete when you are done writing). Returns
        NULL on failure.
        """
    def open_read_append_file(self) -> iostream:
        """Works like open_read_write_file(), but the file is opened in append mode.
        Like open_read_write_file, the returned pointer should eventually be passed
        to close_read_write_file().
        """
    def close_read_write_file(self, stream: iostream) -> None:
        """Closes a file opened by a previous call to open_read_write_file().  This
        really just deletes the iostream pointer, but it is recommended to use this
        interface instead of deleting it explicitly, to help work around compiler
        issues.
        """
    def get_file_size(self, stream: istream = ...) -> int:
        """`(self)`:
        Returns the current size on disk (or wherever it is) of the file before it
        has been opened.

        `(self, stream: istream)`:
        Returns the current size on disk (or wherever it is) of the already-open
        file.  Pass in the stream that was returned by open_read_file(); some
        implementations may require this stream to determine the size.
        """
    def get_timestamp(self) -> int:
        """Returns a time_t value that represents the time the file was last modified,
        to within whatever precision the operating system records this information
        (on a Windows95 system, for instance, this may only be accurate to within 2
        seconds).

        If the timestamp cannot be determined, either because it is not supported
        by the operating system or because there is some error (such as file not
        found), returns 0.
        """
    def get_system_info(self, info: SubfileInfo) -> bool:
        """Populates the SubfileInfo structure with the data representing where the
        file actually resides on disk, if this is knowable.  Returns true if the
        file might reside on disk, and the info is populated, or false if it does
        not (or it is not known where the file resides), in which case the info is
        meaningless.
        """
    getFileSystem = get_file_system
    getFilename = get_filename
    getOriginalFilename = get_original_filename
    hasFile = has_file
    isDirectory = is_directory
    isRegularFile = is_regular_file
    isWritable = is_writable
    deleteFile = delete_file
    renameFile = rename_file
    copyFile = copy_file
    scanDirectory = scan_directory
    lsAll = ls_all
    readFile = read_file
    openReadFile = open_read_file
    closeReadFile = close_read_file
    wasReadSuccessful = was_read_successful
    writeFile = write_file
    openWriteFile = open_write_file
    openAppendFile = open_append_file
    closeWriteFile = close_write_file
    openReadWriteFile = open_read_write_file
    openReadAppendFile = open_read_append_file
    closeReadWriteFile = close_read_write_file
    getFileSize = get_file_size
    getTimestamp = get_timestamp
    getSystemInfo = get_system_info

class VirtualFileComposite(VirtualFile):
    """A composite directory within the VirtualFileSystem: this maps to more than
    one directory on different mount points.  The resulting directory appears
    to be the union of all the individual simple directories.
    """

class VirtualFileMount(TypedReferenceCount):
    """The abstract base class for a mount definition used within a
    VirtualFileSystem.  Normally users don't need to monkey with this class
    directly.
    """

    def get_file_system(self) -> VirtualFileSystem:
        """Returns the file system this mount object is attached to."""
    def get_mount_point(self) -> Filename:
        """Returns the name of the directory within the virtual file system that this
        mount object is attached to.  This directory name will end with a slash.
        """
    def get_mount_flags(self) -> int:
        """Returns the set of flags passed by the user to the
        VirtualFileSystem::mount() command.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    getFileSystem = get_file_system
    getMountPoint = get_mount_point
    getMountFlags = get_mount_flags

class VirtualFileMountMultifile(VirtualFileMount):
    """Maps a Multifile's contents into the VirtualFileSystem."""

    def __init__(self, multifile: Multifile) -> None: ...
    def get_multifile(self) -> Multifile:
        """Returns the Multifile pointer that this mount object is based on."""
    getMultifile = get_multifile

class VirtualFileMountRamdisk(VirtualFileMount):
    """Simulates an actual directory on disk with in-memory storage.  This is
    useful mainly for performing high level functions that expect disk I/O
    without actually writing files to disk.  Naturally, there are significant
    limits to the size of the files that may be written with this system; and
    "files" written here are not automatically persistent between sessions.
    """

    def __init__(self) -> None: ...

class VirtualFileMountSystem(VirtualFileMount):
    """Maps an actual OS directory into the VirtualFileSystem."""

    def __init__(self, physical_filename: StrOrBytesPath) -> None: ...
    def get_physical_filename(self) -> Filename:
        """Returns the name of the source file on the OS filesystem of the directory
        or file that is mounted.
        """
    getPhysicalFilename = get_physical_filename

class VirtualFileSimple(VirtualFile):
    """A simple file or directory within the VirtualFileSystem: this maps to
    exactly one file on one mount point.  Most directories, and all regular
    files, are of this kind.
    """

    def get_mount(self) -> VirtualFileMount:
        """Returns the VirtualFileMount this file is associated with."""
    def is_implicit_pz_file(self) -> bool:
        """Returns true if this file is a .pz file that should be implicitly
        decompressed on load, or false if it is not a .pz file or if it should not
        be decompressed.
        """
    getMount = get_mount
    isImplicitPzFile = is_implicit_pz_file

class TemporaryFile(FileReference):
    """This is a special kind of FileReference class that automatically deletes
    the file in question when it is deleted.  It is not responsible for
    creating, opening, or closing the file, however.
    """

    @overload
    def __init__(self, filename: StrOrBytesPath) -> None: ...
    @overload
    def __init__(self, __param0: TemporaryFile) -> None: ...

class IDecompressStream(istream):
    """An input stream object that uses zlib to decompress (inflate) the input
    from another source stream on-the-fly.

    Attach an IDecompressStream to an existing istream that provides compressed
    data, and read the corresponding uncompressed data from the
    IDecompressStream.

    Seeking is not supported.
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, source: istream, owns_source: bool) -> None: ...
    def open(self, source: istream, owns_source: bool) -> IDecompressStream: ...
    def close(self) -> IDecompressStream:
        """Resets the ZStream to empty, but does not actually close the source istream
        unless owns_source was true.
        """

class OCompressStream(ostream):
    """An input stream object that uses zlib to compress (deflate) data to another
    destination stream on-the-fly.

    Attach an OCompressStream to an existing ostream that will accept
    compressed data, and write your uncompressed source data to the
    OCompressStream.

    Seeking is not supported.
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, dest: ostream, owns_dest: bool, compression_level: int = ...) -> None: ...
    def open(self, dest: ostream, owns_dest: bool, compression_level: int = ...) -> OCompressStream: ...
    def close(self) -> OCompressStream:
        """Resets the ZStream to empty, but does not actually close the dest ostream
        unless owns_dest was true.
        """

class VirtualFileList(ReferenceCount):
    """A list of VirtualFiles, as returned by VirtualFile::scan_directory()."""

    def __init__(self, __param0: VirtualFileList) -> None: ...
    def __getitem__(self, n: int) -> VirtualFile:
        """Returns the nth file in the list."""
    def __len__(self) -> int:
        """Returns the number of files in the list."""
    def __iadd__(self, other: VirtualFileList) -> Self: ...
    def __add__(self, other: VirtualFileList) -> VirtualFileList: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def __iter__(self) -> Iterator[VirtualFile]: ...  # Doesn't actually exist
    def get_num_files(self) -> int:
        """Returns the number of files in the list."""
    def get_file(self, n: int) -> VirtualFile:
        """Returns the nth file in the list."""
    def get_files(self) -> tuple[VirtualFile, ...]: ...
    getNumFiles = get_num_files
    getFile = get_file
    getFiles = get_files

class VirtualFileSystem:
    """A hierarchy of directories and files that appears to be one continuous file
    system, even though the files may originate from several different sources
    that may not be related to the actual OS's file system.

    For instance, a VirtualFileSystem can transparently mount one or more
    Multifiles as their own subdirectory hierarchies.
    """

    MF_read_only: Final = 2
    MFReadOnly: Final = 2
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def mounts(self) -> Sequence[PointerTo_VirtualFileMount]: ...
    def __init__(self) -> None: ...
    @overload
    def mount(self, multifile: Multifile, mount_point: StrOrBytesPath, flags: int) -> bool:
        """`(self, physical_filename: Filename, mount_point: Filename, flags: int, password: str = ...)`:
        Mounts the indicated system file or directory at the given mount point.  If
        the named file is a directory, mounts the directory.  If the named file is
        a Multifile, mounts it as a Multifile.  Returns true on success, false on
        failure.

        A given system directory may be mounted to multiple different mount point,
        and the same mount point may share multiple system directories.  In the
        case of ambiguities (that is, two different files with exactly the same
        full pathname), the most-recently mounted system wins.

        The filename specified as the first parameter must refer to a real,
        physical filename on disk; it cannot be a virtual file already appearing
        within the vfs filespace.  However, it is possible to mount such a file;
        see mount_loop() for this.

        Note that a mounted VirtualFileSystem directory is fully case-sensitive,
        unlike the native Windows file system, so you must refer to files within
        the virtual file system with exactly the right case.

        `(self, multifile: Multifile, mount_point: Filename, flags: int)`:
        Mounts the indicated Multifile at the given mount point.

        `(self, mount: VirtualFileMount, mount_point: Filename, flags: int)`:
        Adds the given VirtualFileMount object to the mount list.  This is a lower-
        level function than the other flavors of mount(); it requires you to create
        a VirtualFileMount object specifically.
        """
    @overload
    def mount(self, mount: VirtualFileMount, mount_point: StrOrBytesPath, flags: int) -> bool: ...
    @overload
    def mount(self, physical_filename: StrOrBytesPath, mount_point: StrOrBytesPath, flags: int, password: str = ...) -> bool: ...
    def mount_loop(self, virtual_filename: StrOrBytesPath, mount_point: StrOrBytesPath, flags: int, password: str = ...) -> bool:
        """This is similar to mount(), but it receives the name of a Multifile that
        already appears within the virtual file system.  It can be used to mount a
        Multifile that is itself hosted within a virtually-mounted Multifile.

        This interface can also be used to mount physical files (that appear within
        the virtual filespace), but it cannot be used to mount directories.  Use
        mount() if you need to mount a directory.

        Note that there is additional overhead, in the form of additional buffer
        copies of the data, for recursively mounting a multifile like this.
        """
    @overload
    def unmount(self, physical_filename: StrOrBytesPath) -> int:
        """`(self, physical_filename: Filename)`:
        Unmounts all appearances of the indicated directory name or multifile name
        from the file system.  Returns the number of appearances unmounted.

        `(self, multifile: Multifile)`:
        Unmounts all appearances of the indicated Multifile from the file system.
        Returns the number of appearances unmounted.

        `(self, mount: VirtualFileMount)`:
        Unmounts the indicated VirtualFileMount object from the file system.
        Returns the number of appearances unmounted.
        """
    @overload
    def unmount(self, multifile: Multifile) -> int: ...
    @overload
    def unmount(self, mount: VirtualFileMount) -> int: ...
    def unmount_point(self, mount_point: StrOrBytesPath) -> int:
        """Unmounts all systems attached to the given mount point from the file
        system.  Returns the number of appearances unmounted.
        """
    def unmount_all(self) -> int:
        """Unmounts all files from the file system.  Returns the number of systems
        unmounted.
        """
    def get_num_mounts(self) -> int:
        """Returns the number of individual mounts in the system."""
    def get_mount(self, n: int) -> VirtualFileMount:
        """Returns the nth mount in the system."""
    def chdir(self, new_directory: StrOrBytesPath) -> bool:
        """Changes the current directory.  This is used to resolve relative pathnames
        in get_file() and/or find_file().  Returns true if successful, false
        otherwise.
        """
    def get_cwd(self) -> Filename:
        """Returns the current directory name.  See chdir()."""
    def make_directory(self, filename: StrOrBytesPath) -> bool:
        """Attempts to create a directory within the file system.  Returns true on
        success, false on failure (for instance, because the parent directory does
        not exist, or is read-only).  If the directory already existed prior to
        this call, returns true.
        """
    def make_directory_full(self, filename: StrOrBytesPath) -> bool:
        """Attempts to create a directory within the file system.  Will also create
        any intervening directories needed.  Returns true on success, false on
        failure.
        """
    def get_file(self, filename: StrOrBytesPath, status_only: bool = ...) -> VirtualFile:
        """Looks up the file by the indicated name in the file system.  Returns a
        VirtualFile pointer representing the file if it is found, or NULL if it is
        not.

        If status_only is true, the file will be checked for existence and length
        and so on, but the returned file's contents cannot be read.  This is an
        optimization which is especially important for certain mount types, for
        instance HTTP, for which opening a file to determine its status is
        substantially less expensive than opening it to read its contents.
        """
    def create_file(self, filename: StrOrBytesPath) -> VirtualFile:
        """Attempts to create a file by the indicated name in the filesystem, if
        possible, and returns it.  If a file by this name already exists, returns
        the same thing as get_file().  If the filename is located within a read-
        only directory, or the directory doesn't exist, returns NULL.
        """
    def find_file(self, filename: StrOrBytesPath, searchpath: SearchPathLike, status_only: bool = ...) -> VirtualFile:
        """Uses the indicated search path to find the file within the file system.
        Returns the first occurrence of the file found, or NULL if the file cannot
        be found.
        """
    def delete_file(self, filename: StrOrBytesPath) -> bool:
        """Attempts to delete the indicated file or directory.  This can remove a
        single file or an empty directory.  It will not remove a nonempty
        directory.  Returns true on success, false on failure.
        """
    def rename_file(self, orig_filename: StrOrBytesPath, new_filename: StrOrBytesPath) -> bool:
        """Attempts to move or rename the indicated file or directory.  If the
        original file is an ordinary file, it will quietly replace any already-
        existing file in the new filename (but not a directory).  If the original
        file is a directory, the new filename must not already exist.

        If the file is a directory, the new filename must be within the same mount
        point.  If the file is an ordinary file, the new filename may be anywhere;
        but if it is not within the same mount point then the rename operation is
        automatically performed as a two-step copy-and-delete operation.
        """
    def copy_file(self, orig_filename: StrOrBytesPath, new_filename: StrOrBytesPath) -> bool:
        """Attempts to copy the contents of the indicated file to the indicated file.
        Returns true on success, false on failure.
        """
    def resolve_filename(self, filename: StrOrBytesPath, searchpath: SearchPathLike, default_extension: str = ...) -> bool:
        """Searches the given search path for the filename.  If it is found, updates
        the filename to the full pathname found and returns true; otherwise,
        returns false.
        """
    def find_all_files(self, filename: StrOrBytesPath, searchpath: SearchPathLike, results: DSearchPath.Results) -> int:
        """Searches all the directories in the search list for the indicated file, in
        order.  Fills up the results list with *all* of the matching filenames
        found, if any.  Returns the number of matches found.

        It is the responsibility of the the caller to clear the results list first;
        otherwise, the newly-found files will be appended to the list.
        """
    def exists(self, filename: StrOrBytesPath) -> bool:
        """Convenience function; returns true if the named file exists."""
    def is_directory(self, filename: StrOrBytesPath) -> bool:
        """Convenience function; returns true if the named file exists and is a
        directory.
        """
    def is_regular_file(self, filename: StrOrBytesPath) -> bool:
        """Convenience function; returns true if the named file exists and is a
        regular file.
        """
    def scan_directory(self, filename: StrOrBytesPath) -> VirtualFileList:
        """If the file represents a directory (that is, is_directory() returns true),
        this returns the list of files within the directory at the current time.
        Returns NULL if the file is not a directory or if the directory cannot be
        read.
        """
    def ls(self, filename: StrOrBytesPath) -> None:
        """Convenience function; lists the files within the indicated directory."""
    def ls_all(self, filename: StrOrBytesPath) -> None:
        """Convenience function; lists the files within the indicated directory, and
        all files below, recursively.
        """
    def write(self, out: ostream) -> None:
        """Print debugging information.  (e.g.  from Python or gdb prompt)."""
    @staticmethod
    def get_global_ptr() -> VirtualFileSystem:
        """Returns the default global VirtualFileSystem.  You may create your own
        personal VirtualFileSystem objects and use them for whatever you like, but
        Panda will attempt to load models and stuff from this default object.

        Initially, the global VirtualFileSystem is set up to mount the OS
        filesystem to root; i.e.  it is equivalent to the OS filesystem.  This may
        be subsequently adjusted by the user.
        """
    def read_file(self, filename: StrOrBytesPath, auto_unwrap: bool):
        """Convenience function; returns the entire contents of the indicated file as
        a string.

        If auto_unwrap is true, an explicitly-named .pz/.gz file is automatically
        decompressed and the decompressed contents are returned.  This is different
        than vfs-implicit-pz, which will automatically decompress a file if the
        extension .pz is *not* given.
        """
    def open_read_file(self, filename: StrOrBytesPath, auto_unwrap: bool) -> istream:
        """Convenience function; returns a newly allocated istream if the file exists
        and can be read, or NULL otherwise.  Does not return an invalid istream.

        If auto_unwrap is true, an explicitly-named .pz file is automatically
        decompressed and the decompressed contents are returned.  This is different
        than vfs-implicit-pz, which will automatically decompress a file if the
        extension .pz is *not* given.
        """
    @staticmethod
    def close_read_file(stream: istream) -> None:
        """Closes a file opened by a previous call to open_read_file().  This really
        just deletes the istream pointer, but it is recommended to use this
        interface instead of deleting it explicitly, to help work around compiler
        issues.
        """
    def write_file(self, filename: StrOrBytesPath, data, auto_wrap: bool): ...
    def open_write_file(self, filename: StrOrBytesPath, auto_wrap: bool, truncate: bool) -> ostream:
        """Convenience function; returns a newly allocated ostream if the file exists
        and can be written, or NULL otherwise.  Does not return an invalid ostream.

        If auto_wrap is true, an explicitly-named .pz file is automatically
        compressed while writing.  If truncate is true, the file is truncated to
        zero length before writing.
        """
    def open_append_file(self, filename: StrOrBytesPath) -> ostream:
        """Works like open_write_file(), but the file is opened in append mode.  Like
        open_write_file, the returned pointer should eventually be passed to
        close_write_file().
        """
    @staticmethod
    def close_write_file(stream: ostream) -> None:
        """Closes a file opened by a previous call to open_write_file().  This really
        just deletes the ostream pointer, but it is recommended to use this
        interface instead of deleting it explicitly, to help work around compiler
        issues.
        """
    def open_read_write_file(self, filename: StrOrBytesPath, truncate: bool) -> iostream:
        """Convenience function; returns a newly allocated iostream if the file exists
        and can be written, or NULL otherwise.  Does not return an invalid
        iostream.
        """
    def open_read_append_file(self, filename: StrOrBytesPath) -> iostream:
        """Works like open_read_write_file(), but the file is opened in append mode.
        Like open_read_write_file, the returned pointer should eventually be passed
        to close_read_write_file().
        """
    @staticmethod
    def close_read_write_file(stream: iostream) -> None:
        """Closes a file opened by a previous call to open_read_write_file().  This
        really just deletes the iostream pointer, but it is recommended to use this
        interface instead of deleting it explicitly, to help work around compiler
        issues.
        """
    def get_mounts(self) -> tuple[VirtualFileMount, ...]: ...
    mountLoop = mount_loop
    unmountPoint = unmount_point
    unmountAll = unmount_all
    getNumMounts = get_num_mounts
    getMount = get_mount
    getCwd = get_cwd
    makeDirectory = make_directory
    makeDirectoryFull = make_directory_full
    getFile = get_file
    createFile = create_file
    findFile = find_file
    deleteFile = delete_file
    renameFile = rename_file
    copyFile = copy_file
    resolveFilename = resolve_filename
    findAllFiles = find_all_files
    isDirectory = is_directory
    isRegularFile = is_regular_file
    scanDirectory = scan_directory
    lsAll = ls_all
    getGlobalPtr = get_global_ptr
    readFile = read_file
    openReadFile = open_read_file
    closeReadFile = close_read_file
    writeFile = write_file
    openWriteFile = open_write_file
    openAppendFile = open_append_file
    closeWriteFile = close_write_file
    openReadWriteFile = open_read_write_file
    openReadAppendFile = open_read_append_file
    closeReadWriteFile = close_read_write_file
    getMounts = get_mounts

class PointerToBase_VirtualFileMount(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerTo_VirtualFileMount(PointerToBase_VirtualFileMount):
    @overload
    def __init__(self, copy: VirtualFileMount = ...) -> None: ...
    @overload
    def __init__(self, ptr: VirtualFileMount) -> None: ...
    @overload
    def __init__(self, __param0: None) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def p(self) -> VirtualFileMount:
        """If your base class is a derivative of TypedObject, you might want to use
        the DCAST macro defined in typedObject.h instead, e.g.  DCAST(MyType,
        ptr).  This provides a clean downcast that doesn't require .p() or any
        double-casting, and it can be run-time checked for correctness.
        """
    @overload
    def assign(self, copy: VirtualFileMount) -> Self: ...
    @overload
    def assign(self, ptr: VirtualFileMount) -> Self: ...

class TrueClock:
    """An interface to whatever real-time clock we might have available in the
    current environment.  There is only one TrueClock in existence, and it
    constructs itself.

    The TrueClock returns elapsed real time in seconds since some undefined
    epoch.  Since it is not defined at what time precisely the clock indicates
    zero, this value can only be meaningfully used to measure elapsed time, by
    sampling it at two different times and subtracting.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def long_time(self) -> float:
        """get_long_time() returns the most accurate timer we have over a long
        interval.  It may not be very precise for measuring short intervals, but
        it should not drift substantially over the long haul.
        """
    @property
    def short_time(self) -> float:
        """get_short_time() returns the most precise timer we have over a short
        interval.  It may tend to drift over the long haul, but it should have
        lots of digits to measure short intervals very precisely.
        """
    @property
    def short_raw_time(self) -> float:
        """get_short_raw_time() is like get_short_time(), but does not apply any
        corrections (e.g.  paranoid-clock) to the result returned by the OS.
        """
    @property
    def error_count(self) -> int: ...
    def get_long_time(self) -> float:
        """get_long_time() returns the most accurate timer we have over a long
        interval.  It may not be very precise for measuring short intervals, but
        it should not drift substantially over the long haul.
        """
    def get_short_time(self) -> float:
        """get_short_time() returns the most precise timer we have over a short
        interval.  It may tend to drift over the long haul, but it should have
        lots of digits to measure short intervals very precisely.
        """
    def get_short_raw_time(self) -> float:
        """get_short_raw_time() is like get_short_time(), but does not apply any
        corrections (e.g.  paranoid-clock) to the result returned by the OS.
        """
    def get_error_count(self) -> int:
        """Returns the number of clock errors that have been detected.  Each time a
        clock error is detected, in which the value returned by either of the above
        methods is suspect, the value returned by this method will be incremented.
        Applications can monitor this value and react, for instance, by
        resynchronizing their clocks each time this value changes.
        """
    @staticmethod
    def get_global_ptr() -> TrueClock:
        """Returns a pointer to the one TrueClock object in the world."""
    def set_cpu_affinity(self, mask: int) -> bool: ...
    getLongTime = get_long_time
    getShortTime = get_short_time
    getShortRawTime = get_short_raw_time
    getErrorCount = get_error_count
    getGlobalPtr = get_global_ptr
    setCpuAffinity = set_cpu_affinity

class Patchfile:
    DtoolClassDict: ClassVar[dict[str, Any]]
    allow_multifile: bool
    footprint_length: int
    @property
    def progress(self) -> float: ...
    @property
    def source_hash(self) -> HashVal: ...
    @property
    def result_hash(self) -> HashVal: ...
    def __init__(self, buffer: Buffer = ...) -> None:
        """`(self)`:
        Create a patch file and initializes internal data

        `(self, buffer: Buffer)`:
        Create patch file with buffer to patch
        """
    def build(self, file_orig: StrOrBytesPath, file_new: StrOrBytesPath, patch_name: StrOrBytesPath) -> bool:
        """This implementation uses the "greedy differencing algorithm" described in
        the masters thesis "Differential Compression: A Generalized Solution for
        Binary Files" by Randal C. Burns (p.13). For an original file of size M and
        a new file of size N, this algorithm is O(M) in space and O(M*N) (worst-
        case) in time.  return false on error
        """
    def read_header(self, patch_file: StrOrBytesPath) -> int:
        """Opens the patch file for reading, and gets the header information from the
        file but does not begin to do any real work.  This can be used to query the
        data stored in the patch.
        """
    @overload
    def initiate(self, patch_file: StrOrBytesPath, file: StrOrBytesPath) -> int:
        """`(self, patch_file: Filename, file: Filename)`:
        Set up to apply the patch to the file (original file and patch are
        destroyed in the process).

        `(self, patch_file: Filename, orig_file: Filename, target_file: Filename)`:
        Set up to apply the patch to the file.  In this form, neither the original
        file nor the patch file are destroyed.
        """
    @overload
    def initiate(self, patch_file: StrOrBytesPath, orig_file: StrOrBytesPath, target_file: StrOrBytesPath) -> int: ...
    def run(self) -> int:
        """Perform one buffer's worth of patching.
        Returns one of the following values:
        @li @c EU_ok : while patching
        @li @c EU_success : when done
        @li @c EU_error_abort : Patching has not been initiated
        @li @c EU_error_file_invalid : file is corrupted
        @li @c EU_error_invalid_checksum : incompatible patch file
        @li @c EU_error_write_file_rename : could not rename file
        """
    @overload
    def apply(self, patch_file: StrOrBytesPath, file: StrOrBytesPath) -> bool:
        """`(self, patch_file: Filename, file: Filename)`:
        Patches the entire file in one call returns true on success and false on
        error

        This version will delete the patch file and overwrite the original file.

        `(self, patch_file: Filename, orig_file: Filename, target_file: Filename)`:
        Patches the entire file in one call returns true on success and false on
        error

        This version will not delete any files.
        """
    @overload
    def apply(self, patch_file: StrOrBytesPath, orig_file: StrOrBytesPath, target_file: StrOrBytesPath) -> bool: ...
    def get_progress(self) -> float:
        """Returns a value in the range 0..1, representing the amount of progress
        through the patchfile, during a session.
        """
    def set_allow_multifile(self, allow_multifile: bool) -> None:
        """If this flag is set true, the Patchfile will make a special case for
        patching Panda Multifiles, if detected, and attempt to patch them on a
        subfile-by-subfile basis.  If this flag is false, the Patchfile will always
        patch the file on a full-file basis.

        This has effect only when building patches; it is not used for applying
        patches.
        """
    def get_allow_multifile(self) -> bool:
        """See set_allow_multifile()."""
    def set_footprint_length(self, length: int) -> None: ...
    def get_footprint_length(self) -> int: ...
    def reset_footprint_length(self) -> None: ...
    def has_source_hash(self) -> bool:
        """Returns true if the MD5 hash for the source file is known.  (Some early
        versions of the patch file did not store this information.)
        """
    def get_source_hash(self) -> HashVal:
        """Returns the MD5 hash for the source file."""
    def get_result_hash(self) -> HashVal:
        """Returns the MD5 hash for the file after the patch has been applied."""
    readHeader = read_header
    getProgress = get_progress
    setAllowMultifile = set_allow_multifile
    getAllowMultifile = get_allow_multifile
    setFootprintLength = set_footprint_length
    getFootprintLength = get_footprint_length
    resetFootprintLength = reset_footprint_length
    hasSourceHash = has_source_hash
    getSourceHash = get_source_hash
    getResultHash = get_result_hash

class ProfileTimer:
    """ProfileTimer

    HowTo:
      Create a ProfileTimer and hold onto it.
      Call init() whenever you like (the timer doesn't
        start yet).
      Call on() to start the timer.
      While the timer is on, call mark() at each point of interest,
        in the code you are timing.
      You can turn the timer off() and on() to skip things you
        don't want to time.
      When your timing is finished, call printTo() to see the
        results (e.g. myTimer.printTo(cerr)).

    Notes:
      You should be able to time things down to the millisecond
      well enough, but if you call on() and off() within micro-
      seconds of each other, I don't think you'll get very good
      results.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, name: str = ..., maxEntries: int = ...) -> None: ...
    @overload
    def __init__(self, other: ProfileTimer) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def init(self, name: str, maxEntries: int = ...) -> None: ...
    def on(self) -> None: ...
    def mark(self, tag: str) -> None: ...
    def off(self, tag: str = ...) -> None: ...
    def getTotalTime(self) -> float:
        """Don't call any of the following during timing: (Because they are slow,
        not because anything will break).
        """
    @staticmethod
    def consolidateAllTo(out: ostream = ...) -> None: ...
    def consolidateTo(self, out: ostream = ...) -> None: ...
    @staticmethod
    def printAllTo(out: ostream = ...) -> None: ...
    def printTo(self, out: ostream = ...) -> None: ...

class WeakPointerToVoid(PointerToVoid):
    """This is the specialization of PointerToVoid for weak pointers.  It needs an
    additional flag to indicate that the pointer has been deleted.
    """

    def was_deleted(self) -> bool:
        """Returns true if the object we are pointing to has been deleted, false
        otherwise.  If this returns true, it means that the pointer can not yet be
        reused, but it does not guarantee that it can be safely accessed.  See the
        lock() method for a safe way to access the underlying pointer.

        This will always return true for a null pointer, unlike is_valid_pointer().
        """
    def is_valid_pointer(self) -> bool:
        """Returns true if the pointer is not null and the object has not been
        deleted.  See was_deleted() for caveats.
        """
    wasDeleted = was_deleted
    isValidPointer = is_valid_pointer

if sys.platform == 'win32':
    class WindowsRegistry:
        """This class provides a hook to Python to read and write strings and integers
        to the windows registry.  It automatically converts strings from utf-8
        encoding and stores them in Unicode (and conversely reconverts them on
        retrieval).
        """

        rl_machine: Final = 0
        RlMachine: Final = 0
        rl_user: Final = 1
        RlUser: Final = 1
        T_none: Final = 0
        TNone: Final = 0
        T_int: Final = 1
        TInt: Final = 1
        T_string: Final = 2
        TString: Final = 2
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: WindowsRegistry = ...) -> None: ...
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...
        @staticmethod
        def set_string_value(key: str, name: str, value: str, rl: _WindowsRegistry_RegLevel = ...) -> bool:
            """Sets the registry key to the indicated value as a string.  The supplied
            string value is automatically converted from whatever encoding is set by
            TextEncoder::set_default_encoding() and written as a Unicode string.  The
            registry key must already exist prior to calling this function.
            """
        @staticmethod
        def set_int_value(key: str, name: str, value: int, rl: _WindowsRegistry_RegLevel = ...) -> bool:
            """Sets the registry key to the indicated value as an integer.  The registry
            key must already exist prior to calling this function.
            """
        @staticmethod
        def get_key_type(key: str, name: str, rl: _WindowsRegistry_RegLevel = ...) -> _WindowsRegistry_Type:
            """Returns the type of the indicated key, or T_none if the key is not known or
            is some unsupported type.
            """
        @staticmethod
        def get_string_value(key: str, name: str, default_value: str, rl: _WindowsRegistry_RegLevel = ...) -> str:
            """Returns the value associated with the indicated registry key, assuming it
            is a string value.  The string value is automatically encoded using
            TextEncoder::get_default_encoding().  If the key is not defined or is not a
            string type value, default_value is returned instead.
            """
        @staticmethod
        def get_int_value(key: str, name: str, default_value: int, rl: _WindowsRegistry_RegLevel = ...) -> int:
            """Returns the value associated with the indicated registry key, assuming it
            is an integer value.  If the key is not defined or is not an integer type
            value, default_value is returned instead.
            """
        setStringValue = set_string_value
        setIntValue = set_int_value
        getKeyType = get_key_type
        getStringValue = get_string_value
        getIntValue = get_int_value

EU_http_redirect: Final = 7
EUHttpRedirect: Final = 7
EU_eof: Final = 6
EUEof: Final = 6
EU_network_no_data: Final = 5
EUNetworkNoData: Final = 5
EU_write_ram: Final = 4
EUWriteRam: Final = 4
EU_write: Final = 3
EUWrite: Final = 3
EU_ok: Final = 2
EUOk: Final = 2
EU_success: Final = 1
EUSuccess: Final = 1
EU_error_abort: Final = -1
EUErrorAbort: Final = -1
EU_error_file_empty: Final = -2
EUErrorFileEmpty: Final = -2
EU_error_file_invalid: Final = -3
EUErrorFileInvalid: Final = -3
EU_error_invalid_checksum: Final = -4
EUErrorInvalidChecksum: Final = -4
EU_error_network_dead: Final = -30
EUErrorNetworkDead: Final = -30
EU_error_network_unreachable: Final = -31
EUErrorNetworkUnreachable: Final = -31
EU_error_network_disconnected: Final = -32
EUErrorNetworkDisconnected: Final = -32
EU_error_network_timeout: Final = -33
EUErrorNetworkTimeout: Final = -33
EU_error_network_no_data: Final = -34
EUErrorNetworkNoData: Final = -34
EU_error_network_disconnected_locally: Final = -40
EUErrorNetworkDisconnectedLocally: Final = -40
EU_error_network_buffer_overflow: Final = -41
EUErrorNetworkBufferOverflow: Final = -41
EU_error_network_disk_quota_exceeded: Final = -42
EUErrorNetworkDiskQuotaExceeded: Final = -42
EU_error_network_remote_host_disconnected: Final = -50
EUErrorNetworkRemoteHostDisconnected: Final = -50
EU_error_network_remote_host_down: Final = -51
EUErrorNetworkRemoteHostDown: Final = -51
EU_error_network_remote_host_unreachable: Final = -52
EUErrorNetworkRemoteHostUnreachable: Final = -52
EU_error_network_remote_host_not_found: Final = -53
EUErrorNetworkRemoteHostNotFound: Final = -53
EU_error_network_remote_host_no_response: Final = -54
EUErrorNetworkRemoteHostNoResponse: Final = -54
EU_error_write_out_of_files: Final = -60
EUErrorWriteOutOfFiles: Final = -60
EU_error_write_out_of_memory: Final = -61
EUErrorWriteOutOfMemory: Final = -61
EU_error_write_sharing_violation: Final = -62
EUErrorWriteSharingViolation: Final = -62
EU_error_write_disk_full: Final = -63
EUErrorWriteDiskFull: Final = -63
EU_error_write_disk_not_found: Final = -64
EUErrorWriteDiskNotFound: Final = -64
EU_error_write_disk_sector_not_found: Final = -65
EUErrorWriteDiskSectorNotFound: Final = -65
EU_error_write_disk_fault: Final = -66
EUErrorWriteDiskFault: Final = -66
EU_error_write_file_rename: Final = -67
EUErrorWriteFileRename: Final = -67
EU_error_http_server_timeout: Final = -70
EUErrorHttpServerTimeout: Final = -70
EU_error_http_gateway_timeout: Final = -71
EUErrorHttpGatewayTimeout: Final = -71
EU_error_http_service_unavailable: Final = -72
EUErrorHttpServiceUnavailable: Final = -72
EU_error_http_proxy_authentication: Final = -73
EUErrorHttpProxyAuthentication: Final = -73
EU_error_zlib: Final = -80
EUErrorZlib: Final = -80

def compress_string(source: str, compression_level: int) -> str: ...
def decompress_string(source: str) -> str: ...
def compress_file(source: StrOrBytesPath, dest: StrOrBytesPath, compression_level: int) -> bool: ...
def decompress_file(source: StrOrBytesPath, dest: StrOrBytesPath) -> bool: ...
def compress_stream(source: istream, dest: ostream, compression_level: int) -> bool: ...
def decompress_stream(source: istream, dest: ostream) -> bool: ...
def copy_stream(source: istream, dest: ostream) -> bool: ...
def encrypt_string(
    source: str, password: str, algorithm: str = ..., key_length: int = ..., iteration_count: int = ...
) -> str: ...
def decrypt_string(source: str, password: str) -> str: ...
def encrypt_file(
    source: StrOrBytesPath,
    dest: StrOrBytesPath,
    password: str,
    algorithm: str = ...,
    key_length: int = ...,
    iteration_count: int = ...,
) -> bool: ...
def decrypt_file(source: StrOrBytesPath, dest: StrOrBytesPath, password: str) -> bool: ...
def encrypt_stream(
    source: istream, dest: ostream, password: str, algorithm: str = ..., key_length: int = ..., iteration_count: int = ...
) -> bool: ...
def decrypt_stream(source: istream, dest: ostream, password: str) -> bool: ...
def error_to_text(err: _ErrorUtilCode) -> str: ...
def get_write_error() -> int: ...
def handle_socket_error() -> str: ...
def get_network_error() -> int: ...
def password_hash(password: str, salt: str, iters: int, keylen: int) -> str: ...

compressString = compress_string
decompressString = decompress_string
compressFile = compress_file
decompressFile = decompress_file
compressStream = compress_stream
decompressStream = decompress_stream
copyStream = copy_stream
encryptString = encrypt_string
decryptString = decrypt_string
encryptFile = encrypt_file
decryptFile = decrypt_file
encryptStream = encrypt_stream
decryptStream = decrypt_stream
errorToText = error_to_text
getWriteError = get_write_error
handleSocketError = handle_socket_error
getNetworkError = get_network_error
passwordHash = password_hash
CPTA_double = ConstPointerToArray_double
CPTADouble = CPTA_double
ConstPointerToArrayDouble = ConstPointerToArray_double
PointerToArrayBaseDouble = PointerToArrayBase_double
PointerToBaseReferenceCountedVectorDouble = PointerToBase_ReferenceCountedVector_double
CPTA_float = ConstPointerToArray_float
CPTAFloat = CPTA_float
ConstPointerToArrayFloat = ConstPointerToArray_float
PointerToArrayBaseFloat = PointerToArrayBase_float
PointerToBaseReferenceCountedVectorFloat = PointerToBase_ReferenceCountedVector_float
CPTA_int = ConstPointerToArray_int
CPTAInt = CPTA_int
ConstPointerToArrayInt = ConstPointerToArray_int
PointerToArrayBaseInt = PointerToArrayBase_int
PointerToBaseReferenceCountedVectorInt = PointerToBase_ReferenceCountedVector_int
CPTA_uchar = ConstPointerToArray_unsigned_char
CPTAUchar = CPTA_uchar
ConstPointerToArrayUnsignedChar = ConstPointerToArray_unsigned_char
PointerToArrayBaseUnsignedChar = PointerToArrayBase_unsigned_char
PointerToBaseReferenceCountedVectorUnsignedChar = PointerToBase_ReferenceCountedVector_unsigned_char
PTA_double = PointerToArray_double
PTADouble = PTA_double
PointerToArrayDouble = PointerToArray_double
PTA_float = PointerToArray_float
PTAFloat = PTA_float
PointerToArrayFloat = PointerToArray_float
PTA_int = PointerToArray_int
PTAInt = PTA_int
PointerToArrayInt = PointerToArray_int
PTA_uchar = PointerToArray_unsigned_char
PTAUchar = PTA_uchar
PointerToArrayUnsignedChar = PointerToArray_unsigned_char
PointerToVirtualFileMount = PointerTo_VirtualFileMount
PointerToBaseVirtualFileMount = PointerToBase_VirtualFileMount
PTA_stdfloat = PTA_float
PTAStdfloat = PTA_stdfloat
CPTA_stdfloat = CPTA_float
CPTAStdfloat = CPTA_stdfloat
