from collections.abc import Iterator, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import (
    DoubleMat4Like,
    DoubleVec2Like,
    DoubleVec3Like,
    DoubleVec4Like,
    IntVec2Like,
    IntVec3Like,
    IntVec4Like,
    Mat4Like,
    Vec2Like,
    Vec3Like,
    Vec4Like,
)
from panda3d.core._dtoolbase import TypeHandle
from panda3d.core._dtoolutil import ostream
from panda3d.core._express import Datagram, DatagramIterator, PointerToVoid, TypedReferenceCount
from panda3d.core._linmath import (
    LMatrix3d,
    LMatrix3f,
    LMatrix4d,
    LMatrix4f,
    LPoint2d,
    LPoint3,
    LPoint3d,
    LPoint3f,
    LVecBase2d,
    LVecBase2f,
    LVecBase2i,
    LVecBase3d,
    LVecBase3f,
    LVecBase3i,
    LVecBase4d,
    LVecBase4f,
    LVector3d,
    LVector3f,
    UnalignedLMatrix4d,
    UnalignedLMatrix4f,
    UnalignedLVecBase4d,
    UnalignedLVecBase4f,
    UnalignedLVecBase4i,
)

_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]

class PointerToBase_ReferenceCountedVector_LMatrix3d(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_LMatrix3d(PointerToBase_ReferenceCountedVector_LMatrix3d):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_LMatrix3d(PointerToArrayBase_LMatrix3d):
    def __init__(self, copy: ConstPointerToArray_LMatrix3d | PointerToArray_LMatrix3d) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LMatrix3d: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_LMatrix3d: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LMatrix3d]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> LMatrix3d: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: LMatrix3d) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_LMatrix3f(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_LMatrix3f(PointerToBase_ReferenceCountedVector_LMatrix3f):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_LMatrix3f(PointerToArrayBase_LMatrix3f):
    def __init__(self, copy: ConstPointerToArray_LMatrix3f | PointerToArray_LMatrix3f) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LMatrix3f: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_LMatrix3f: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LMatrix3f]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> LMatrix3f: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: LMatrix3f) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_LVecBase2d(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_LVecBase2d(PointerToBase_ReferenceCountedVector_LVecBase2d):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_LVecBase2d(PointerToArrayBase_LVecBase2d):
    def __init__(self, copy: ConstPointerToArray_LVecBase2d | PointerToArray_LVecBase2d) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LVecBase2d: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_LVecBase2d: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LVecBase2d]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> LVecBase2d: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: DoubleVec2Like) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_LVecBase2f(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_LVecBase2f(PointerToBase_ReferenceCountedVector_LVecBase2f):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_LVecBase2f(PointerToArrayBase_LVecBase2f):
    def __init__(self, copy: ConstPointerToArray_LVecBase2f | PointerToArray_LVecBase2f) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LVecBase2f: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_LVecBase2f: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LVecBase2f]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> LVecBase2f: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: Vec2Like) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_LVecBase2i(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_LVecBase2i(PointerToBase_ReferenceCountedVector_LVecBase2i):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_LVecBase2i(PointerToArrayBase_LVecBase2i):
    def __init__(self, copy: ConstPointerToArray_LVecBase2i | PointerToArray_LVecBase2i) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LVecBase2i: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_LVecBase2i: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LVecBase2i]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> LVecBase2i: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: IntVec2Like) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_LVecBase3d(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_LVecBase3d(PointerToBase_ReferenceCountedVector_LVecBase3d):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_LVecBase3d(PointerToArrayBase_LVecBase3d):
    def __init__(self, copy: ConstPointerToArray_LVecBase3d | PointerToArray_LVecBase3d) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LVecBase3d: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_LVecBase3d: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LVecBase3d]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> LVecBase3d: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: DoubleVec3Like) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_LVecBase3f(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_LVecBase3f(PointerToBase_ReferenceCountedVector_LVecBase3f):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_LVecBase3f(PointerToArrayBase_LVecBase3f):
    def __init__(self, copy: ConstPointerToArray_LVecBase3f | PointerToArray_LVecBase3f) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LVecBase3f: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_LVecBase3f: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LVecBase3f]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> LVecBase3f: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: Vec3Like) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_LVecBase3i(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_LVecBase3i(PointerToBase_ReferenceCountedVector_LVecBase3i):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_LVecBase3i(PointerToArrayBase_LVecBase3i):
    def __init__(self, copy: ConstPointerToArray_LVecBase3i | PointerToArray_LVecBase3i) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LVecBase3i: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_LVecBase3i: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LVecBase3i]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> LVecBase3i: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: IntVec3Like) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_UnalignedLMatrix4d(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_UnalignedLMatrix4d(PointerToBase_ReferenceCountedVector_UnalignedLMatrix4d):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_UnalignedLMatrix4d(PointerToArrayBase_UnalignedLMatrix4d):
    def __init__(self, copy: ConstPointerToArray_UnalignedLMatrix4d | PointerToArray_UnalignedLMatrix4d) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> UnalignedLMatrix4d: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_UnalignedLMatrix4d: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[UnalignedLMatrix4d]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> UnalignedLMatrix4d: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: LMatrix4d | UnalignedLMatrix4d) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_UnalignedLMatrix4f(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_UnalignedLMatrix4f(PointerToBase_ReferenceCountedVector_UnalignedLMatrix4f):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_UnalignedLMatrix4f(PointerToArrayBase_UnalignedLMatrix4f):
    def __init__(self, copy: ConstPointerToArray_UnalignedLMatrix4f | PointerToArray_UnalignedLMatrix4f) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> UnalignedLMatrix4f: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_UnalignedLMatrix4f: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[UnalignedLMatrix4f]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> UnalignedLMatrix4f: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: LMatrix4f | UnalignedLMatrix4f) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_UnalignedLVecBase4d(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_UnalignedLVecBase4d(PointerToBase_ReferenceCountedVector_UnalignedLVecBase4d):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_UnalignedLVecBase4d(PointerToArrayBase_UnalignedLVecBase4d):
    def __init__(self, copy: ConstPointerToArray_UnalignedLVecBase4d | PointerToArray_UnalignedLVecBase4d) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> UnalignedLVecBase4d: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_UnalignedLVecBase4d: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[UnalignedLVecBase4d]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> UnalignedLVecBase4d: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: DoubleVec4Like | UnalignedLVecBase4d) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_UnalignedLVecBase4f(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_UnalignedLVecBase4f(PointerToBase_ReferenceCountedVector_UnalignedLVecBase4f):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_UnalignedLVecBase4f(PointerToArrayBase_UnalignedLVecBase4f):
    def __init__(self, copy: ConstPointerToArray_UnalignedLVecBase4f | PointerToArray_UnalignedLVecBase4f) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> UnalignedLVecBase4f: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_UnalignedLVecBase4f: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[UnalignedLVecBase4f]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> UnalignedLVecBase4f: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: UnalignedLVecBase4f | Vec4Like) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToBase_ReferenceCountedVector_UnalignedLVecBase4i(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_UnalignedLVecBase4i(PointerToBase_ReferenceCountedVector_UnalignedLVecBase4i):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_UnalignedLVecBase4i(PointerToArrayBase_UnalignedLVecBase4i):
    def __init__(self, copy: ConstPointerToArray_UnalignedLVecBase4i | PointerToArray_UnalignedLVecBase4i) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> UnalignedLVecBase4i: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_UnalignedLVecBase4i: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[UnalignedLVecBase4i]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> UnalignedLVecBase4i: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: IntVec4Like | UnalignedLVecBase4i) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToArray_LMatrix3d(PointerToArrayBase_LMatrix3d):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_LMatrix3d) -> None: ...
    @overload
    def __init__(self, source: Sequence[LMatrix3d]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LMatrix3d: ...
    def __setitem__(self, n: int, value: LMatrix3d) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_LMatrix3d: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LMatrix3d]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_LMatrix3d: ...
    def push_back(self, x: LMatrix3d) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> LMatrix3d: ...
    def set_element(self, n: int, value: LMatrix3d) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: LMatrix3d) -> int: ...
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

class PointerToArray_LMatrix3f(PointerToArrayBase_LMatrix3f):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_LMatrix3f) -> None: ...
    @overload
    def __init__(self, source: Sequence[LMatrix3f]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LMatrix3f: ...
    def __setitem__(self, n: int, value: LMatrix3f) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_LMatrix3f: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LMatrix3f]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_LMatrix3f: ...
    def push_back(self, x: LMatrix3f) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> LMatrix3f: ...
    def set_element(self, n: int, value: LMatrix3f) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: LMatrix3f) -> int: ...
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

class PointerToArray_LVecBase2d(PointerToArrayBase_LVecBase2d):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_LVecBase2d) -> None: ...
    @overload
    def __init__(self, source: Sequence[LVecBase2d]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LVecBase2d: ...
    def __setitem__(self, n: int, value: DoubleVec2Like) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_LVecBase2d: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LVecBase2d]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_LVecBase2d: ...
    def push_back(self, x: DoubleVec2Like) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> LVecBase2d: ...
    def set_element(self, n: int, value: DoubleVec2Like) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: DoubleVec2Like) -> int: ...
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

class PointerToArray_LVecBase2f(PointerToArrayBase_LVecBase2f):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_LVecBase2f) -> None: ...
    @overload
    def __init__(self, source: Sequence[LVecBase2f]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LVecBase2f: ...
    def __setitem__(self, n: int, value: Vec2Like) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_LVecBase2f: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LVecBase2f]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_LVecBase2f: ...
    def push_back(self, x: Vec2Like) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> LVecBase2f: ...
    def set_element(self, n: int, value: Vec2Like) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: Vec2Like) -> int: ...
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

class PointerToArray_LVecBase2i(PointerToArrayBase_LVecBase2i):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_LVecBase2i) -> None: ...
    @overload
    def __init__(self, source: Sequence[LVecBase2i]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LVecBase2i: ...
    def __setitem__(self, n: int, value: IntVec2Like) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_LVecBase2i: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LVecBase2i]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_LVecBase2i: ...
    def push_back(self, x: IntVec2Like) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> LVecBase2i: ...
    def set_element(self, n: int, value: IntVec2Like) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: IntVec2Like) -> int: ...
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

class PointerToArray_LVecBase3d(PointerToArrayBase_LVecBase3d):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_LVecBase3d) -> None: ...
    @overload
    def __init__(self, source: Sequence[LVecBase3d]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LVecBase3d: ...
    def __setitem__(self, n: int, value: DoubleVec3Like) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_LVecBase3d: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LVecBase3d]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_LVecBase3d: ...
    def push_back(self, x: DoubleVec3Like) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> LVecBase3d: ...
    def set_element(self, n: int, value: DoubleVec3Like) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: DoubleVec3Like) -> int: ...
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

class PointerToArray_LVecBase3f(PointerToArrayBase_LVecBase3f):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_LVecBase3f) -> None: ...
    @overload
    def __init__(self, source: Sequence[LVecBase3f]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LVecBase3f: ...
    def __setitem__(self, n: int, value: Vec3Like) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_LVecBase3f: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LVecBase3f]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_LVecBase3f: ...
    def push_back(self, x: Vec3Like) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> LVecBase3f: ...
    def set_element(self, n: int, value: Vec3Like) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: Vec3Like) -> int: ...
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

class PointerToArray_LVecBase3i(PointerToArrayBase_LVecBase3i):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_LVecBase3i) -> None: ...
    @overload
    def __init__(self, source: Sequence[LVecBase3i]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> LVecBase3i: ...
    def __setitem__(self, n: int, value: IntVec3Like) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_LVecBase3i: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[LVecBase3i]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_LVecBase3i: ...
    def push_back(self, x: IntVec3Like) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> LVecBase3i: ...
    def set_element(self, n: int, value: IntVec3Like) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: IntVec3Like) -> int: ...
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

class PointerToArray_UnalignedLMatrix4d(PointerToArrayBase_UnalignedLMatrix4d):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_UnalignedLMatrix4d) -> None: ...
    @overload
    def __init__(self, source: Sequence[UnalignedLMatrix4d]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> UnalignedLMatrix4d: ...
    def __setitem__(self, n: int, value: LMatrix4d | UnalignedLMatrix4d) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_UnalignedLMatrix4d: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[UnalignedLMatrix4d]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_UnalignedLMatrix4d: ...
    def push_back(self, x: LMatrix4d | UnalignedLMatrix4d) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> UnalignedLMatrix4d: ...
    def set_element(self, n: int, value: LMatrix4d | UnalignedLMatrix4d) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: LMatrix4d | UnalignedLMatrix4d) -> int: ...
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

class PointerToArray_UnalignedLMatrix4f(PointerToArrayBase_UnalignedLMatrix4f):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_UnalignedLMatrix4f) -> None: ...
    @overload
    def __init__(self, source: Sequence[UnalignedLMatrix4f]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> UnalignedLMatrix4f: ...
    def __setitem__(self, n: int, value: LMatrix4f | UnalignedLMatrix4f) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_UnalignedLMatrix4f: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[UnalignedLMatrix4f]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_UnalignedLMatrix4f: ...
    def push_back(self, x: LMatrix4f | UnalignedLMatrix4f) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> UnalignedLMatrix4f: ...
    def set_element(self, n: int, value: LMatrix4f | UnalignedLMatrix4f) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: LMatrix4f | UnalignedLMatrix4f) -> int: ...
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

class PointerToArray_UnalignedLVecBase4d(PointerToArrayBase_UnalignedLVecBase4d):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_UnalignedLVecBase4d) -> None: ...
    @overload
    def __init__(self, source: Sequence[UnalignedLVecBase4d]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> UnalignedLVecBase4d: ...
    def __setitem__(self, n: int, value: DoubleVec4Like | UnalignedLVecBase4d) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_UnalignedLVecBase4d: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[UnalignedLVecBase4d]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_UnalignedLVecBase4d: ...
    def push_back(self, x: DoubleVec4Like | UnalignedLVecBase4d) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> UnalignedLVecBase4d: ...
    def set_element(self, n: int, value: DoubleVec4Like | UnalignedLVecBase4d) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: DoubleVec4Like | UnalignedLVecBase4d) -> int: ...
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

class PointerToArray_UnalignedLVecBase4f(PointerToArrayBase_UnalignedLVecBase4f):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_UnalignedLVecBase4f) -> None: ...
    @overload
    def __init__(self, source: Sequence[UnalignedLVecBase4f]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> UnalignedLVecBase4f: ...
    def __setitem__(self, n: int, value: UnalignedLVecBase4f | Vec4Like) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_UnalignedLVecBase4f: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[UnalignedLVecBase4f]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_UnalignedLVecBase4f: ...
    def push_back(self, x: UnalignedLVecBase4f | Vec4Like) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> UnalignedLVecBase4f: ...
    def set_element(self, n: int, value: UnalignedLVecBase4f | Vec4Like) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: UnalignedLVecBase4f | Vec4Like) -> int: ...
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

class PointerToArray_UnalignedLVecBase4i(PointerToArrayBase_UnalignedLVecBase4i):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_UnalignedLVecBase4i) -> None: ...
    @overload
    def __init__(self, source: Sequence[UnalignedLVecBase4i]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> UnalignedLVecBase4i: ...
    def __setitem__(self, n: int, value: IntVec4Like | UnalignedLVecBase4i) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_UnalignedLVecBase4i: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[UnalignedLVecBase4i]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_UnalignedLVecBase4i: ...
    def push_back(self, x: IntVec4Like | UnalignedLVecBase4i) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> UnalignedLVecBase4i: ...
    def set_element(self, n: int, value: IntVec4Like | UnalignedLVecBase4i) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: IntVec4Like | UnalignedLVecBase4i) -> int: ...
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

class BoundingVolume(TypedReferenceCount):
    """This is an abstract class for any volume in any sense which can be said to
    define the locality of reference of a node in a graph, along with all of
    its descendants.  It is not necessarily a geometric volume (although see
    GeometricBoundingVolume); this is simply an abstract interface for bounds
    of any sort.
    """

    IF_no_intersection: Final = 0
    IFNoIntersection: Final = 0
    IF_possible: Final = 1
    IFPossible: Final = 1
    IF_some: Final = 2
    IFSome: Final = 2
    IF_all: Final = 4
    IFAll: Final = 4
    IF_dont_understand: Final = 8
    IFDontUnderstand: Final = 8
    BT_default: Final = 0
    BTDefault: Final = 0
    BT_best: Final = 1
    BTBest: Final = 1
    BT_sphere: Final = 2
    BTSphere: Final = 2
    BT_box: Final = 3
    BTBox: Final = 3
    BT_fastest: Final = 4
    BTFastest: Final = 4
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def make_copy(self) -> BoundingVolume: ...
    def is_empty(self) -> bool:
        """Any kind of volume might be empty.  This is a degenerate volume that
        contains no points; it's not the same as, for instance, a sphere with
        radius zero, since that contains one point (the center).  It intersects
        with no other volumes.
        """
    def is_infinite(self) -> bool:
        """The other side of the empty coin is an infinite volume.  This is a
        degenerate state of a normally finite volume that contains all points.
        (Note that some kinds of infinite bounding volumes, like binary separating
        planes, do not contain all points and thus correctly return is_infinite()
        == false, even though they are technically infinite.  This is a special
        case of the word 'infinite' meaning the volume covers all points in space.)

        It completely intersects with all other volumes except empty volumes.
        """
    def set_infinite(self) -> None:
        """Marks the volume as infinite, even if it is normally finite.  You can think
        of this as an infinite extend_by() operation.
        """
    def extend_by(self, vol: BoundingVolume) -> bool:
        """Increases the size of the volume to include the given volume."""
    def contains(self, vol: BoundingVolume) -> int:
        """Returns the appropriate set of IntersectionFlags to indicate the amount of
        intersection with the indicated volume.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    makeCopy = make_copy
    isEmpty = is_empty
    isInfinite = is_infinite
    setInfinite = set_infinite
    extendBy = extend_by

class GeometricBoundingVolume(BoundingVolume):
    """This is another abstract class, for a general class of bounding volumes
    that actually enclose points in 3-d space, such as BSP's and bounding
    spheres.
    """

    @overload  # type: ignore[override]
    def extend_by(self, vol: GeometricBoundingVolume) -> bool:
        """`(self, vol: GeometricBoundingVolume)`:
        Increases the size of the volume to include the given volume.

        `(self, point: LPoint3)`:
        Increases the size of the volume to include the given point.
        """
    @overload
    def extend_by(self, point: Vec3Like) -> bool: ...
    @overload  # type: ignore[override]
    def contains(self, vol: GeometricBoundingVolume) -> int:
        """`(self, vol: GeometricBoundingVolume)`:
        Returns the appropriate set of IntersectionFlags to indicate the amount of
        intersection with the indicated volume.

        `(self, point: LPoint3)`:
        Returns the appropriate set of IntersectionFlags to indicate the amount of
        intersection with the indicated point.

        `(self, a: LPoint3, b: LPoint3)`:
        Returns the appropriate set of IntersectionFlags to indicate the amount of
        intersection with the indicated line segment.
        """
    @overload
    def contains(self, point: Vec3Like) -> int: ...
    @overload
    def contains(self, a: Vec3Like, b: Vec3Like) -> int: ...
    def get_approx_center(self) -> LPoint3: ...
    def xform(self, mat: Mat4Like) -> None: ...
    extendBy = extend_by  # type: ignore[assignment]
    getApproxCenter = get_approx_center

class FiniteBoundingVolume(GeometricBoundingVolume):
    """A special kind of GeometricBoundingVolume that is known to be finite.  It
    is possible to query this kind of volume for its minimum and maximum
    extents.
    """

    @property
    def min(self) -> LPoint3: ...
    @property
    def max(self) -> LPoint3: ...
    @property
    def volume(self) -> float: ...
    def get_min(self) -> LPoint3: ...
    def get_max(self) -> LPoint3: ...
    def get_volume(self) -> float: ...
    getMin = get_min
    getMax = get_max
    getVolume = get_volume

class LParabolaf:
    """An abstract mathematical description of a parabola, particularly useful for
    describing arcs of projectiles.

    The parabolic equation, given parametrically here, is P = At^2 + Bt + C.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: LParabolaf = ...) -> None:
        """`(self)`:
        Constructs a meaningless degenerate parabola.

        `(self, a: LVecBase3f, b: LVecBase3f, c: LVecBase3f)`:
        Constructs a parabola given the three points of the parametric equation:
        the acceleration, initial velocity, and start point.
        """
    @overload
    def __init__(self, a: Vec3Like, b: Vec3Like, c: Vec3Like) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def xform(self, mat: Mat4Like) -> None:
        """Transforms the parabola by the indicated matrix."""
    def get_a(self) -> LVecBase3f:
        """Returns the first point of the parabola's parametric equation: the
        acceleration.
        """
    def get_b(self) -> LVecBase3f:
        """Returns the second point of the parabola's parametric equation: the initial
        velocity.
        """
    def get_c(self) -> LVecBase3f:
        """Returns the third point of the parabola's parametric equation: the start
        point.
        """
    def calc_point(self, t: float) -> LPoint3f:
        """Computes the point on the parabola at time t."""
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the parabola to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the parabola, regardless of the setting
        of Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
    def read_datagram_fixed(self, source: Datagram | DatagramIterator) -> None:
        """Reads the parabola from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the parabola to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the vector using the standard width
        setting, especially when you are writing a bam file.
        """
    def read_datagram(self, source: Datagram | DatagramIterator) -> None:
        """Reads the parabola from the Datagram using get_stdfloat()."""
    getA = get_a
    getB = get_b
    getC = get_c
    calcPoint = calc_point
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram

class LParabolad:
    """An abstract mathematical description of a parabola, particularly useful for
    describing arcs of projectiles.

    The parabolic equation, given parametrically here, is P = At^2 + Bt + C.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: LParabolad = ...) -> None:
        """`(self)`:
        Constructs a meaningless degenerate parabola.

        `(self, a: LVecBase3d, b: LVecBase3d, c: LVecBase3d)`:
        Constructs a parabola given the three points of the parametric equation:
        the acceleration, initial velocity, and start point.
        """
    @overload
    def __init__(self, a: DoubleVec3Like, b: DoubleVec3Like, c: DoubleVec3Like) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def xform(self, mat: DoubleMat4Like) -> None:
        """Transforms the parabola by the indicated matrix."""
    def get_a(self) -> LVecBase3d:
        """Returns the first point of the parabola's parametric equation: the
        acceleration.
        """
    def get_b(self) -> LVecBase3d:
        """Returns the second point of the parabola's parametric equation: the initial
        velocity.
        """
    def get_c(self) -> LVecBase3d:
        """Returns the third point of the parabola's parametric equation: the start
        point.
        """
    def calc_point(self, t: float) -> LPoint3d:
        """Computes the point on the parabola at time t."""
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def write_datagram_fixed(self, destination: Datagram) -> None:
        """Writes the parabola to the Datagram using add_float32() or add_float64(),
        depending on the type of floats in the parabola, regardless of the setting
        of Datagram::set_stdfloat_double().  This is appropriate when you want to
        write a fixed-width value to the datagram, especially when you are not
        writing a bam file.
        """
    def read_datagram_fixed(self, source: Datagram | DatagramIterator) -> None:
        """Reads the parabola from the Datagram using get_float32() or get_float64().
        See write_datagram_fixed().
        """
    def write_datagram(self, destination: Datagram) -> None:
        """Writes the parabola to the Datagram using add_stdfloat().  This is
        appropriate when you want to write the vector using the standard width
        setting, especially when you are writing a bam file.
        """
    def read_datagram(self, source: Datagram | DatagramIterator) -> None:
        """Reads the parabola from the Datagram using get_stdfloat()."""
    getA = get_a
    getB = get_b
    getC = get_c
    calcPoint = calc_point
    writeDatagramFixed = write_datagram_fixed
    readDatagramFixed = read_datagram_fixed
    writeDatagram = write_datagram
    readDatagram = read_datagram

class LPlanef(LVecBase4f):
    """An abstract mathematical description of a plane.  A plane is defined by the
    equation Ax + By + Cz + D = 0.
    """

    @overload
    def __init__(self, copy: Vec4Like = ...) -> None:
        """`(self)`:
        Creates a default plane.  This plane happens to intersect the origin,
        perpendicular to the Z axis.  It's not clear how useful a default plane is.

        `(self, a: LPoint3f, b: LPoint3f, c: LPoint3f)`:
        Constructs a plane given three counter-clockwise points, as seen from the
        front of the plane (that is, viewed from the end of the normal vector,
        looking down).

        `(self, normal: LVector3f, point: LPoint3f)`:
        Constructs a plane given a surface normal vector and a point within the
        plane.

        `(self, a: float, b: float, c: float, d: float)`:
        Constructs a plane given the four terms of the plane equation.
        """
    @overload
    def __init__(self, normal: Vec3Like, point: Vec3Like) -> None: ...
    @overload
    def __init__(self, a: Vec3Like, b: Vec3Like, c: Vec3Like) -> None: ...
    @overload
    def __init__(self, a: float, b: float, c: float, d: float) -> None: ...
    def __mul__(self, mat: Mat4Like) -> LPlanef: ...  # type: ignore[override]
    def __imul__(self, mat: Mat4Like) -> Self: ...  # type: ignore[override]
    def __neg__(self) -> LPlanef: ...
    def xform(self, mat: Mat4Like) -> None:
        """Transforms the plane by the indicated matrix."""
    def get_reflection_mat(self) -> LMatrix4f:
        """This computes a transform matrix that reflects the universe to the other
        side of the plane, as in a mirror.
        """
    def get_normal(self) -> LVector3f:
        """Returns the surface normal of the plane."""
    def get_point(self) -> LPoint3f:
        """Returns an arbitrary point in the plane.  This can be used along with the
        normal returned by get_normal() to reconstruct the plane.
        """
    def dist_to_plane(self, point: Vec3Like) -> float:
        """Returns the straight-line shortest distance from the point to the plane.
        The returned value is positive if the point is in front of the plane (on
        the side with the normal), or negative in the point is behind the plane (on
        the opposite side from the normal). It's zero if the point is exactly in
        the plane.
        """
    def normalize(self) -> bool:
        """Normalizes the plane in place.  Returns true if the plane was normalized,
        false if the plane had a zero-length normal vector.
        """
    def normalized(self) -> LPlanef:
        """Normalizes the plane and returns the normalized plane as a copy.  If the
        plane's normal was a zero-length vector, the same plane is returned.
        """
    def project(self, point: Vec3Like) -> LPoint3f:  # type: ignore[override]
        """Returns the point within the plane nearest to the indicated point in space."""
    def flip(self) -> None:
        """Convenience method that flips the plane in-place.  This is done by simply
        flipping the normal vector.
        """
    def intersects_line(self, intersection_point: Vec3Like, p1: Vec3Like, p2: Vec3Like) -> bool:
        """Returns true if the plane intersects the infinite line passing through
        points p1 and p2, false if the line is parallel.  The points p1 and p2 are
        used only to define the Euclidean line; they have no other bearing on the
        intersection test.  If true, sets intersection_point to the point of
        intersection.
        """
    def intersects_plane(self, _from: Vec3Like, delta: Vec3Like, other: Vec4Like) -> bool:
        """Returns true if the two planes intersect, false if they do not.  If they do
        intersect, then from and delta are filled in with the parametric
        representation of the line of intersection: that is, from is a point on
        that line, and delta is a vector showing the direction of the line.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    getReflectionMat = get_reflection_mat
    getNormal = get_normal
    getPoint = get_point
    distToPlane = dist_to_plane
    intersectsLine = intersects_line
    intersectsPlane = intersects_plane

class LPlaned(LVecBase4d):
    """An abstract mathematical description of a plane.  A plane is defined by the
    equation Ax + By + Cz + D = 0.
    """

    @overload
    def __init__(self, copy: DoubleVec4Like = ...) -> None:
        """`(self)`:
        Creates a default plane.  This plane happens to intersect the origin,
        perpendicular to the Z axis.  It's not clear how useful a default plane is.

        `(self, a: LPoint3d, b: LPoint3d, c: LPoint3d)`:
        Constructs a plane given three counter-clockwise points, as seen from the
        front of the plane (that is, viewed from the end of the normal vector,
        looking down).

        `(self, normal: LVector3d, point: LPoint3d)`:
        Constructs a plane given a surface normal vector and a point within the
        plane.

        `(self, a: float, b: float, c: float, d: float)`:
        Constructs a plane given the four terms of the plane equation.
        """
    @overload
    def __init__(self, normal: DoubleVec3Like, point: DoubleVec3Like) -> None: ...
    @overload
    def __init__(self, a: DoubleVec3Like, b: DoubleVec3Like, c: DoubleVec3Like) -> None: ...
    @overload
    def __init__(self, a: float, b: float, c: float, d: float) -> None: ...
    def __mul__(self, mat: DoubleMat4Like) -> LPlaned: ...  # type: ignore[override]
    def __imul__(self, mat: DoubleMat4Like) -> Self: ...  # type: ignore[override]
    def __neg__(self) -> LPlaned: ...
    def xform(self, mat: DoubleMat4Like) -> None:
        """Transforms the plane by the indicated matrix."""
    def get_reflection_mat(self) -> LMatrix4d:
        """This computes a transform matrix that reflects the universe to the other
        side of the plane, as in a mirror.
        """
    def get_normal(self) -> LVector3d:
        """Returns the surface normal of the plane."""
    def get_point(self) -> LPoint3d:
        """Returns an arbitrary point in the plane.  This can be used along with the
        normal returned by get_normal() to reconstruct the plane.
        """
    def dist_to_plane(self, point: DoubleVec3Like) -> float:
        """Returns the straight-line shortest distance from the point to the plane.
        The returned value is positive if the point is in front of the plane (on
        the side with the normal), or negative in the point is behind the plane (on
        the opposite side from the normal). It's zero if the point is exactly in
        the plane.
        """
    def normalize(self) -> bool:
        """Normalizes the plane in place.  Returns true if the plane was normalized,
        false if the plane had a zero-length normal vector.
        """
    def normalized(self) -> LPlaned:
        """Normalizes the plane and returns the normalized plane as a copy.  If the
        plane's normal was a zero-length vector, the same plane is returned.
        """
    def project(self, point: DoubleVec3Like) -> LPoint3d:  # type: ignore[override]
        """Returns the point within the plane nearest to the indicated point in space."""
    def flip(self) -> None:
        """Convenience method that flips the plane in-place.  This is done by simply
        flipping the normal vector.
        """
    def intersects_line(self, intersection_point: DoubleVec3Like, p1: DoubleVec3Like, p2: DoubleVec3Like) -> bool:
        """Returns true if the plane intersects the infinite line passing through
        points p1 and p2, false if the line is parallel.  The points p1 and p2 are
        used only to define the Euclidean line; they have no other bearing on the
        intersection test.  If true, sets intersection_point to the point of
        intersection.
        """
    def intersects_plane(self, _from: DoubleVec3Like, delta: DoubleVec3Like, other: DoubleVec4Like) -> bool:
        """Returns true if the two planes intersect, false if they do not.  If they do
        intersect, then from and delta are filled in with the parametric
        representation of the line of intersection: that is, from is a point on
        that line, and delta is a vector showing the direction of the line.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    getReflectionMat = get_reflection_mat
    getNormal = get_normal
    getPoint = get_point
    distToPlane = dist_to_plane
    intersectsLine = intersects_line
    intersectsPlane = intersects_plane

class BoundingBox(FiniteBoundingVolume):
    """An axis-aligned bounding box; that is, a minimum and maximum coordinate
    triple.

    This box is always axis-aligned.  If you need a more general bounding box,
    try BoundingHexahedron.
    """

    @property
    def points(self) -> Sequence[LPoint3]: ...
    @property
    def planes(self) -> Sequence[LPlane]: ...
    @overload
    def __init__(self) -> None:
        """`(self)`:
        Constructs an empty box object.

        `(self, min: LPoint3, max: LPoint3)`:
        Constructs a specific box object.
        """
    @overload
    def __init__(self, min: Vec3Like, max: Vec3Like) -> None: ...
    def get_num_points(self) -> int:
        """Returns 8: the number of vertices of a rectangular solid."""
    def get_point(self, n: int) -> LPoint3:
        """Returns the nth vertex of the rectangular solid."""
    def get_num_planes(self) -> int:
        """Returns 6: the number of faces of a rectangular solid."""
    def get_plane(self, n: int) -> LPlane:
        """Returns the nth face of the rectangular solid."""
    def set_min_max(self, min: Vec3Like, max: Vec3Like) -> None:
        """Sets the min and max point of the rectangular solid."""
    def get_points(self) -> tuple[LPoint3, ...]: ...
    def get_planes(self) -> tuple[LPlane, ...]: ...
    getNumPoints = get_num_points
    getPoint = get_point
    getNumPlanes = get_num_planes
    getPlane = get_plane
    setMinMax = set_min_max
    getPoints = get_points
    getPlanes = get_planes

class LFrustumf:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: LFrustumf = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @overload
    def make_ortho_2D(self) -> None:
        """Sets up a two-dimensional orthographic frustum"""
    @overload
    def make_ortho_2D(self, l: float, r: float, t: float, b: float) -> None: ...
    @overload
    def make_ortho(self, fnear: float, ffar: float) -> None:
        """Behaves like gluOrtho"""
    @overload
    def make_ortho(self, fnear: float, ffar: float, l: float, r: float, t: float, b: float) -> None: ...
    def make_perspective_hfov(self, xfov: float, aspect: float, fnear: float, ffar: float) -> None:
        """Behaves like gluPerspective (Aspect = width/height, Yfov in degrees)"""
    def make_perspective_vfov(self, yfov: float, aspect: float, fnear: float, ffar: float) -> None: ...
    def make_perspective(self, xfov: float, yfov: float, fnear: float, ffar: float) -> None: ...
    makeOrtho2D = make_ortho_2D
    makeOrtho = make_ortho
    makePerspectiveHfov = make_perspective_hfov
    makePerspectiveVfov = make_perspective_vfov
    makePerspective = make_perspective

class LFrustumd:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: LFrustumd = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @overload
    def make_ortho_2D(self) -> None:
        """Sets up a two-dimensional orthographic frustum"""
    @overload
    def make_ortho_2D(self, l: float, r: float, t: float, b: float) -> None: ...
    @overload
    def make_ortho(self, fnear: float, ffar: float) -> None:
        """Behaves like gluOrtho"""
    @overload
    def make_ortho(self, fnear: float, ffar: float, l: float, r: float, t: float, b: float) -> None: ...
    def make_perspective_hfov(self, xfov: float, aspect: float, fnear: float, ffar: float) -> None:
        """Behaves like gluPerspective (Aspect = width/height, Yfov in degrees)"""
    def make_perspective_vfov(self, yfov: float, aspect: float, fnear: float, ffar: float) -> None: ...
    def make_perspective(self, xfov: float, yfov: float, fnear: float, ffar: float) -> None: ...
    makeOrtho2D = make_ortho_2D
    makeOrtho = make_ortho
    makePerspectiveHfov = make_perspective_hfov
    makePerspectiveVfov = make_perspective_vfov
    makePerspective = make_perspective

class BoundingHexahedron(FiniteBoundingVolume):
    """This defines a bounding convex hexahedron.  It is typically used to
    represent a frustum, but may represent any enclosing convex hexahedron,
    including simple boxes.  However, if all you want is an axis-aligned
    bounding box, you may be better off with the simpler BoundingBox class.
    """

    @property
    def points(self) -> Sequence[LPoint3]: ...
    @property
    def planes(self) -> Sequence[LPlane]: ...
    @overload
    def __init__(self, frustum: LFrustum, is_ortho: bool, cs: _CoordinateSystem = ...) -> None: ...
    @overload
    def __init__(
        self,
        fll: Vec3Like,
        flr: Vec3Like,
        fur: Vec3Like,
        ful: Vec3Like,
        nll: Vec3Like,
        nlr: Vec3Like,
        nur: Vec3Like,
        nul: Vec3Like,
    ) -> None: ...
    def get_num_points(self) -> int:
        """Returns 8: the number of vertices of a hexahedron."""
    def get_point(self, n: int) -> LPoint3:
        """Returns the nth vertex of the hexahedron."""
    def get_num_planes(self) -> int:
        """Returns 6: the number of faces of a hexahedron."""
    def get_plane(self, n: int) -> LPlane:
        """Returns the nth face of the hexahedron."""
    def get_points(self) -> tuple[LPoint3, ...]: ...
    def get_planes(self) -> tuple[LPlane, ...]: ...
    getNumPoints = get_num_points
    getPoint = get_point
    getNumPlanes = get_num_planes
    getPlane = get_plane
    getPoints = get_points
    getPlanes = get_planes

class BoundingLine(GeometricBoundingVolume):
    """This funny bounding volume is an infinite line with no thickness and
    extending to infinity in both directions.

    Note that it *always* extends in both directions, despite the fact that you
    specify two points to the constructor.  These are not endpoints, they are
    two arbitrary points on the line.
    """

    def __init__(self, a: Vec3Like, b: Vec3Like) -> None: ...
    def get_point_a(self) -> LPoint3:
        """Returns the first point that defines the line."""
    def get_point_b(self) -> LPoint3:
        """Returns the second point that defines the line."""
    getPointA = get_point_a
    getPointB = get_point_b

class BoundingPlane(GeometricBoundingVolume):
    """This funny bounding volume is an infinite plane that divides space into two
    regions: the part behind the normal, which is "inside" the bounding volume,
    and the part in front of the normal, which is "outside" the bounding
    volume.
    """

    @property
    def plane(self) -> LPlane: ...
    def __init__(self, plane: Vec4Like = ...) -> None:
        """Constructs an empty "plane" that has no intersections."""
    def get_plane(self) -> LPlane: ...
    getPlane = get_plane

class BoundingSphere(FiniteBoundingVolume):
    """This defines a bounding sphere, consisting of a center and a radius.  It is
    always a sphere, and never an ellipsoid or other quadric.
    """

    center: LPoint3
    radius: float
    @overload
    def __init__(self) -> None:
        """`(self)`:
        Constructs an empty sphere.

        `(self, center: LPoint3, radius: float)`:
        Constructs a specific sphere.
        """
    @overload
    def __init__(self, center: Vec3Like, radius: float) -> None: ...
    def get_center(self) -> LPoint3: ...
    def get_radius(self) -> float: ...
    def set_center(self, center: Vec3Like) -> None:
        """Sets the center point of the sphere."""
    def set_radius(self, radius: float) -> None:
        """Sets the radius of the sphere."""
    getCenter = get_center
    getRadius = get_radius
    setCenter = set_center
    setRadius = set_radius

class IntersectionBoundingVolume(GeometricBoundingVolume):
    """This special bounding volume is the intersection of all of its constituent
    bounding volumes.

    A point is defined to be within an IntersectionBoundingVolume if it is
    within all of its component bounding volumes.
    """

    @property
    def components(self) -> Sequence[GeometricBoundingVolume]: ...
    def __init__(self) -> None:
        """Constructs an empty intersection."""
    def get_num_components(self) -> int:
        """Returns the number of components in the intersection."""
    def get_component(self, n: int) -> GeometricBoundingVolume:
        """Returns the nth component in the intersection."""
    def clear_components(self) -> None:
        """Removes all components from the volume."""
    def add_component(self, component: GeometricBoundingVolume) -> None:
        """Adds a new component to the volume.  This does not necessarily increase the
        total number of components by one, and you may or may not be able to find
        this component in the volume by a subsequent call to get_component();
        certain optimizations may prevent the component from being added, or have
        other unexpected effects on the total set of components.
        """
    def get_components(self) -> tuple[GeometricBoundingVolume, ...]: ...
    getNumComponents = get_num_components
    getComponent = get_component
    clearComponents = clear_components
    addComponent = add_component
    getComponents = get_components

class Mersenne:
    max_value: Final = 2147483647
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: Mersenne) -> None:
        """initializes mt[N] with a seed"""
    @overload
    def __init__(self, seed: int) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_uint31(self) -> int:
        """generates a random number on [0,0x7fffffff]-interval"""
    getUint31 = get_uint31

class OmniBoundingVolume(GeometricBoundingVolume):
    """This is a special kind of GeometricBoundingVolume that fills all of space."""

    def __init__(self) -> None: ...

class UnionBoundingVolume(GeometricBoundingVolume):
    """This special bounding volume is the union of all of its constituent
    bounding volumes.

    A point is defined to be within a UnionBoundingVolume if it is within any
    one or more of its component bounding volumes.
    """

    @property
    def components(self) -> Sequence[GeometricBoundingVolume]: ...
    def __init__(self) -> None:
        """Constructs an empty union."""
    def get_num_components(self) -> int:
        """Returns the number of components in the union."""
    def get_component(self, n: int) -> GeometricBoundingVolume:
        """Returns the nth component in the union."""
    def clear_components(self) -> None:
        """Removes all components from the volume."""
    def add_component(self, component: GeometricBoundingVolume) -> None:
        """Adds a new component to the volume.  This does not necessarily increase the
        total number of components by one, and you may or may not be able to find
        this component in the volume by a subsequent call to get_component();
        certain optimizations may prevent the component from being added, or have
        other unexpected effects on the total set of components.
        """
    def filter_intersection(self, volume: BoundingVolume) -> None:
        """Removes from the union any components that have no intersection with the
        indicated volume.
        """
    def get_components(self) -> tuple[GeometricBoundingVolume, ...]: ...
    getNumComponents = get_num_components
    getComponent = get_component
    clearComponents = clear_components
    addComponent = add_component
    filterIntersection = filter_intersection
    getComponents = get_components

class Randomizer:
    """A handy class to return random numbers."""

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, seed: int = ...) -> None:
        """If seed is nonzero, it is used to define the tables; if it is zero a random
        seed is generated.
        """
    @overload
    def __init__(self, copy: Randomizer) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def random_int(self, range: int) -> int:
        """Returns a random integer in the range [0, range)."""
    def random_real(self, range: float) -> float:
        """Returns a random double in the range [0, range)."""
    def random_real_unit(self) -> float:
        """Returns a random double in the range [-0.5, 0.5)."""
    @staticmethod
    def get_next_seed() -> int:
        """Returns a random seed value for the next global Randomizer object."""
    def get_seed(self) -> int:
        """Returns a unique seed value based on the seed value passed to this
        Randomizer object (and on its current state).
        """
    randomInt = random_int
    randomReal = random_real
    randomRealUnit = random_real_unit
    getNextSeed = get_next_seed
    getSeed = get_seed

class PerlinNoise:
    """This is the base class for PerlinNoise2 and PerlinNoise3, different
    dimensions of Perlin noise implementation.  The base class just collects
    the common functionality.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_seed(self) -> int:
        """Returns a unique seed value based on the seed value passed to this
        PerlinNoise object (and on its current state).
        """
    getSeed = get_seed

class PerlinNoise2(PerlinNoise):
    """This class provides an implementation of Perlin noise for 2 variables.
    This code is loosely based on the reference implementation at
    https://mrl.nyu.edu/~perlin/noise/ .
    """

    @overload
    def __init__(self, copy: PerlinNoise2 = ...) -> None:
        """`(self)`:
        Randomizes the tables to make a unique noise function.  Uses a default
        scale (noise frequency), table size, and seed.

        `(self, copy: PerlinNoise2)`:
        Makes an exact copy of the existing PerlinNoise object, including its
        random seed.

        `(self, sx: float, sy: float, table_size: int = ..., seed: int = ...)`:
        Randomizes the tables to make a unique noise function.

        If seed is nonzero, it is used to define the tables; if it is zero a random
        seed is generated.
        """
    @overload
    def __init__(self, sx: float, sy: float, table_size: int = ..., seed: int = ...) -> None: ...
    @overload
    def __call__(self, value: DoubleVec2Like | Vec2Like) -> float: ...
    @overload
    def __call__(self, x: float, y: float) -> float: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    @overload
    def set_scale(self, scale: DoubleVec2Like | Vec2Like | float) -> None:
        """Changes the scale (frequency) of the noise."""
    @overload
    def set_scale(self, sx: float, sy: float) -> None: ...
    @overload
    def noise(self, value: DoubleVec2Like | Vec2Like) -> float:
        """Returns the noise function of the three inputs."""
    @overload
    def noise(self, x: float, y: float) -> float: ...
    setScale = set_scale

class PerlinNoise3(PerlinNoise):
    """This class provides an implementation of Perlin noise for 3 variables.
    This code is loosely based on the reference implementation at
    http://mrl.nyu.edu/~perlin/noise/ .
    """

    @overload
    def __init__(self, copy: PerlinNoise3 = ...) -> None:
        """`(self)`:
        Randomizes the tables to make a unique noise function.  Uses a default
        scale (noise frequency), table size, and seed.

        `(self, copy: PerlinNoise3)`:
        Makes an exact copy of the existing PerlinNoise object, including its
        random seed.

        `(self, sx: float, sy: float, sz: float, table_size: int = ..., seed: int = ...)`:
        Randomizes the tables to make a unique noise function.

        If seed is nonzero, it is used to define the tables; if it is zero a random
        seed is generated.
        """
    @overload
    def __init__(self, sx: float, sy: float, sz: float, table_size: int = ..., seed: int = ...) -> None: ...
    @overload
    def __call__(self, value: DoubleVec3Like | Vec3Like) -> float: ...
    @overload
    def __call__(self, x: float, y: float, z: float) -> float: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    @overload
    def set_scale(self, scale: DoubleVec3Like | Vec3Like | float) -> None:
        """Changes the scale (frequency) of the noise."""
    @overload
    def set_scale(self, sx: float, sy: float, sz: float) -> None: ...
    @overload
    def noise(self, value: DoubleVec3Like | Vec3Like) -> float:
        """Returns the noise function of the three inputs."""
    @overload
    def noise(self, x: float, y: float, z: float) -> float: ...
    setScale = set_scale

class StackedPerlinNoise2:
    """Implements a multi-layer PerlinNoise, with one or more high-frequency noise
    functions added to a lower-frequency base noise function.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: StackedPerlinNoise2 = ...) -> None:
        """`(self)`:
        Creates a StackedPerlinNoise2 object with no levels.  You should call
        add_level() to add each level by hand.

        `(self, copy: StackedPerlinNoise2)`:
        Creates an exact duplicate of the existing StackedPerlinNoise2 object,
        including the random seed.

        `(self, sx: float, sy: float, num_levels: int = ..., scale_factor: float = ..., amp_scale: float = ..., table_size: int = ..., seed: int = ...)`:
        Creates num_levels nested PerlinNoise2 objects.  Each stacked Perlin object
        will have a scale of 1 scale_factor times the previous object (so that it
        is higher-frequency, if scale_factor > 1), and an amplitude of amp_scale
        times the previous object (so that it is less important, if amp_scale < 1).
        """
    @overload
    def __init__(
        self,
        sx: float,
        sy: float,
        num_levels: int = ...,
        scale_factor: float = ...,
        amp_scale: float = ...,
        table_size: int = ...,
        seed: int = ...,
    ) -> None: ...
    @overload
    def __call__(self, value: DoubleVec2Like | Vec2Like) -> float: ...
    @overload
    def __call__(self, x: float, y: float) -> float: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def add_level(self, level: PerlinNoise2, amp: float = ...) -> None:
        """Adds an arbitrary PerlinNoise2 object, and an associated amplitude, to the
        stack.
        """
    def clear(self) -> None:
        """Removes all levels from the stack.  You must call add_level() again to
        restore them.
        """
    @overload
    def noise(self, value: DoubleVec2Like | Vec2Like) -> float:
        """Returns the noise function of the three inputs."""
    @overload
    def noise(self, x: float, y: float) -> float: ...
    addLevel = add_level

class StackedPerlinNoise3:
    """Implements a multi-layer PerlinNoise, with one or more high-frequency noise
    functions added to a lower-frequency base noise function.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: StackedPerlinNoise3 = ...) -> None:
        """`(self)`:
        Creates a StackedPerlinNoise3 object with no levels.  You should call
        add_level() to add each level by hand.

        `(self, copy: StackedPerlinNoise3)`:
        Creates an exact duplicate of the existing StackedPerlinNoise3 object,
        including the random seed.

        `(self, sx: float, sy: float, sz: float, num_levels: int = ..., scale_factor: float = ..., amp_scale: float = ..., table_size: int = ..., seed: int = ...)`:
        Creates num_levels nested PerlinNoise3 objects.  Each stacked Perlin object
        will have a scale of 1 scale_factor times the previous object (so that it
        is higher-frequency, if scale_factor > 1), and an amplitude of amp_scale
        times the previous object (so that it is less important, if amp_scale < 1).
        """
    @overload
    def __init__(
        self,
        sx: float,
        sy: float,
        sz: float,
        num_levels: int = ...,
        scale_factor: float = ...,
        amp_scale: float = ...,
        table_size: int = ...,
        seed: int = ...,
    ) -> None: ...
    @overload
    def __call__(self, value: DoubleVec3Like | Vec3Like) -> float: ...
    @overload
    def __call__(self, x: float, y: float, z: float) -> float: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def add_level(self, level: PerlinNoise3, amp: float = ...) -> None:
        """Adds an arbitrary PerlinNoise3 object, and an associated amplitude, to the
        stack.
        """
    def clear(self) -> None:
        """Removes all levels from the stack.  You must call add_level() again to
        restore them.
        """
    @overload
    def noise(self, value: DoubleVec3Like | Vec3Like) -> float:
        """Returns the noise function of the three inputs."""
    @overload
    def noise(self, x: float, y: float, z: float) -> float: ...
    addLevel = add_level

class Triangulator:
    """This class can triangulate a convex or concave polygon, even one with
    holes.  It is adapted from an algorithm published as:

    Narkhede A. and Manocha D., Fast polygon triangulation algorithm based on
    Seidel's Algorithm, UNC-CH, 1994.

    http://www.cs.unc.edu/~dm/CODE/GEM/chapter.html

    It works strictly on 2-d points.  See Triangulator3 for 3-d points.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def vertices(self) -> Sequence[LPoint2d]: ...
    def __init__(self, __param0: Triangulator = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def clear(self) -> None:
        """Removes all vertices and polygon specifications from the Triangulator, and
        prepares it to start over.
        """
    @overload
    def add_vertex(self, point: DoubleVec2Like) -> int:
        """Adds a new vertex to the vertex pool.  Returns the vertex index number."""
    @overload
    def add_vertex(self, x: float, y: float) -> int: ...
    def get_num_vertices(self) -> int:
        """Returns the number of vertices in the pool.  Note that the Triangulator
        might append new vertices, in addition to those added by the user, if any
        of the polygon is self-intersecting, or if any of the holes intersect some
        part of the polygon edges.
        """
    def get_vertex(self, n: int) -> LPoint2d:
        """Returns the nth vertex."""
    def clear_polygon(self) -> None:
        """Removes the current polygon definition (and its set of holes), but does not
        clear the vertex pool.
        """
    def add_polygon_vertex(self, index: int) -> None:
        """Adds the next consecutive vertex of the polygon.  This vertex should index
        into the vertex pool established by repeated calls to add_vertex().

        The vertices may be listed in either clockwise or counterclockwise order.
        Vertices should not be repeated.  In particular, do not repeat the first
        vertex at the end.
        """
    def is_left_winding(self) -> bool:
        """Returns true if the polygon vertices are listed in counterclockwise order,
        or false if they appear to be listed in clockwise order.
        """
    def begin_hole(self) -> None:
        """Finishes the previous hole, if any, and prepares to add a new hole."""
    def add_hole_vertex(self, index: int) -> None:
        """Adds the next consecutive vertex of the current hole.  This vertex should
        index into the vertex pool established by repeated calls to add_vertex().

        The vertices may be listed in either clockwise or counterclockwise order.
        Vertices should not be repeated.
        """
    def triangulate(self) -> None:
        """Does the work of triangulating the specified polygon.  After this call, you
        may retrieve the new triangles one at a time by iterating through
        get_triangle_v0/1/2().
        """
    def get_num_triangles(self) -> int:
        """Returns the number of triangles generated by the previous call to
        triangulate().
        """
    def get_triangle_v0(self, n: int) -> int:
        """Returns vertex 0 of the nth triangle generated by the previous call to
        triangulate().

        This is a zero-based index into the vertices added by repeated calls to
        add_vertex().
        """
    def get_triangle_v1(self, n: int) -> int:
        """Returns vertex 1 of the nth triangle generated by the previous call to
        triangulate().

        This is a zero-based index into the vertices added by repeated calls to
        add_vertex().
        """
    def get_triangle_v2(self, n: int) -> int:
        """Returns vertex 2 of the nth triangle generated by the previous call to
        triangulate().

        This is a zero-based index into the vertices added by repeated calls to
        add_vertex().
        """
    def get_vertices(self) -> tuple[LPoint2d, ...]: ...
    addVertex = add_vertex
    getNumVertices = get_num_vertices
    getVertex = get_vertex
    clearPolygon = clear_polygon
    addPolygonVertex = add_polygon_vertex
    isLeftWinding = is_left_winding
    beginHole = begin_hole
    addHoleVertex = add_hole_vertex
    getNumTriangles = get_num_triangles
    getTriangleV0 = get_triangle_v0
    getTriangleV1 = get_triangle_v1
    getTriangleV2 = get_triangle_v2
    getVertices = get_vertices

class Triangulator3(Triangulator):
    """This is an extension of Triangulator to handle polygons with three-
    dimensional points.  It assumes all of the points lie in a single plane,
    and internally projects the supplied points into 2-D for passing to the
    underlying Triangulator object.
    """

    @property
    def vertices(self) -> Sequence[LPoint3d]: ...  # type: ignore[override]
    @property
    def plane(self) -> LPlaned: ...
    def __init__(self, __param0: Triangulator3 = ...) -> None: ...
    @overload  # type: ignore[override]
    def add_vertex(self, point: DoubleVec3Like) -> int:
        """Adds a new vertex to the vertex pool.  Returns the vertex index number."""
    @overload
    def add_vertex(self, x: float, y: float, z: float) -> int: ...
    def get_vertex(self, n: int) -> LPoint3d:  # type: ignore[override]
        """Returns the nth vertex."""
    def get_plane(self) -> LPlaned:
        """Returns the plane of the polygon.  This is only available after calling
        triangulate().
        """
    def get_vertices(self) -> tuple[LPoint3d, ...]: ...  # type: ignore[override]
    addVertex = add_vertex  # type: ignore[assignment]
    getVertex = get_vertex  # type: ignore[assignment]
    getPlane = get_plane
    getVertices = get_vertices  # type: ignore[assignment]

@overload
def heads_up(mat: DoubleMat4Like, fwd: DoubleVec3Like, up: DoubleVec3Like = ..., cs: _CoordinateSystem = ...) -> None: ...
@overload
def heads_up(mat: Mat4Like, fwd: Vec3Like, up: Vec3Like = ..., cs: _CoordinateSystem = ...) -> None: ...
@overload
def heads_up(quat: DoubleVec4Like, fwd: DoubleVec3Like, up: DoubleVec3Like = ..., cs: _CoordinateSystem = ...) -> None: ...
@overload
def heads_up(quat: Vec4Like, fwd: Vec3Like, up: Vec3Like = ..., cs: _CoordinateSystem = ...) -> None: ...
@overload
def heads_up(mat: DoubleMat4Like, fwd: DoubleVec3Like, cs: _CoordinateSystem) -> None: ...
@overload
def heads_up(mat: Mat4Like, fwd: Vec3Like, cs: _CoordinateSystem) -> None: ...
@overload
def heads_up(quat: DoubleVec4Like, fwd: DoubleVec3Like, cs: _CoordinateSystem) -> None: ...
@overload
def heads_up(quat: Vec4Like, fwd: Vec3Like, cs: _CoordinateSystem) -> None: ...
@overload
def look_at(mat: DoubleMat4Like, fwd: DoubleVec3Like, up: DoubleVec3Like = ..., cs: _CoordinateSystem = ...) -> None: ...
@overload
def look_at(mat: Mat4Like, fwd: Vec3Like, up: Vec3Like = ..., cs: _CoordinateSystem = ...) -> None: ...
@overload
def look_at(quat: DoubleVec4Like, fwd: DoubleVec3Like, up: DoubleVec3Like = ..., cs: _CoordinateSystem = ...) -> None: ...
@overload
def look_at(quat: Vec4Like, fwd: Vec3Like, up: Vec3Like = ..., cs: _CoordinateSystem = ...) -> None: ...
@overload
def look_at(mat: DoubleMat4Like, fwd: DoubleVec3Like, cs: _CoordinateSystem) -> None: ...
@overload
def look_at(mat: Mat4Like, fwd: Vec3Like, cs: _CoordinateSystem) -> None: ...
@overload
def look_at(quat: DoubleVec4Like, fwd: DoubleVec3Like, cs: _CoordinateSystem) -> None: ...
@overload
def look_at(quat: Vec4Like, fwd: Vec3Like, cs: _CoordinateSystem) -> None: ...
@overload
def rotate_to(mat: DoubleMat4Like, a: DoubleVec3Like, b: DoubleVec3Like) -> None: ...
@overload
def rotate_to(mat: Mat4Like, a: Vec3Like, b: Vec3Like) -> None: ...

headsUp = heads_up
lookAt = look_at
rotateTo = rotate_to
ConstPointerToArrayLMatrix3d = ConstPointerToArray_LMatrix3d
PointerToArrayBaseLMatrix3d = PointerToArrayBase_LMatrix3d
PointerToBaseReferenceCountedVectorLMatrix3d = PointerToBase_ReferenceCountedVector_LMatrix3d
ConstPointerToArrayLMatrix3f = ConstPointerToArray_LMatrix3f
PointerToArrayBaseLMatrix3f = PointerToArrayBase_LMatrix3f
PointerToBaseReferenceCountedVectorLMatrix3f = PointerToBase_ReferenceCountedVector_LMatrix3f
ConstPointerToArrayLVecBase2d = ConstPointerToArray_LVecBase2d
PointerToArrayBaseLVecBase2d = PointerToArrayBase_LVecBase2d
PointerToBaseReferenceCountedVectorLVecBase2d = PointerToBase_ReferenceCountedVector_LVecBase2d
ConstPointerToArrayLVecBase2f = ConstPointerToArray_LVecBase2f
PointerToArrayBaseLVecBase2f = PointerToArrayBase_LVecBase2f
PointerToBaseReferenceCountedVectorLVecBase2f = PointerToBase_ReferenceCountedVector_LVecBase2f
ConstPointerToArrayLVecBase2i = ConstPointerToArray_LVecBase2i
PointerToArrayBaseLVecBase2i = PointerToArrayBase_LVecBase2i
PointerToBaseReferenceCountedVectorLVecBase2i = PointerToBase_ReferenceCountedVector_LVecBase2i
ConstPointerToArrayLVecBase3d = ConstPointerToArray_LVecBase3d
PointerToArrayBaseLVecBase3d = PointerToArrayBase_LVecBase3d
PointerToBaseReferenceCountedVectorLVecBase3d = PointerToBase_ReferenceCountedVector_LVecBase3d
ConstPointerToArrayLVecBase3f = ConstPointerToArray_LVecBase3f
PointerToArrayBaseLVecBase3f = PointerToArrayBase_LVecBase3f
PointerToBaseReferenceCountedVectorLVecBase3f = PointerToBase_ReferenceCountedVector_LVecBase3f
ConstPointerToArrayLVecBase3i = ConstPointerToArray_LVecBase3i
PointerToArrayBaseLVecBase3i = PointerToArrayBase_LVecBase3i
PointerToBaseReferenceCountedVectorLVecBase3i = PointerToBase_ReferenceCountedVector_LVecBase3i
ConstPointerToArrayUnalignedLMatrix4d = ConstPointerToArray_UnalignedLMatrix4d
PointerToArrayBaseUnalignedLMatrix4d = PointerToArrayBase_UnalignedLMatrix4d
PointerToBaseReferenceCountedVectorUnalignedLMatrix4d = PointerToBase_ReferenceCountedVector_UnalignedLMatrix4d
ConstPointerToArrayUnalignedLMatrix4f = ConstPointerToArray_UnalignedLMatrix4f
PointerToArrayBaseUnalignedLMatrix4f = PointerToArrayBase_UnalignedLMatrix4f
PointerToBaseReferenceCountedVectorUnalignedLMatrix4f = PointerToBase_ReferenceCountedVector_UnalignedLMatrix4f
ConstPointerToArrayUnalignedLVecBase4d = ConstPointerToArray_UnalignedLVecBase4d
PointerToArrayBaseUnalignedLVecBase4d = PointerToArrayBase_UnalignedLVecBase4d
PointerToBaseReferenceCountedVectorUnalignedLVecBase4d = PointerToBase_ReferenceCountedVector_UnalignedLVecBase4d
ConstPointerToArrayUnalignedLVecBase4f = ConstPointerToArray_UnalignedLVecBase4f
PointerToArrayBaseUnalignedLVecBase4f = PointerToArrayBase_UnalignedLVecBase4f
PointerToBaseReferenceCountedVectorUnalignedLVecBase4f = PointerToBase_ReferenceCountedVector_UnalignedLVecBase4f
ConstPointerToArrayUnalignedLVecBase4i = ConstPointerToArray_UnalignedLVecBase4i
PointerToArrayBaseUnalignedLVecBase4i = PointerToArrayBase_UnalignedLVecBase4i
PointerToBaseReferenceCountedVectorUnalignedLVecBase4i = PointerToBase_ReferenceCountedVector_UnalignedLVecBase4i
PointerToArrayLMatrix3d = PointerToArray_LMatrix3d
PointerToArrayLMatrix3f = PointerToArray_LMatrix3f
PointerToArrayLVecBase2d = PointerToArray_LVecBase2d
PointerToArrayLVecBase2f = PointerToArray_LVecBase2f
PointerToArrayLVecBase2i = PointerToArray_LVecBase2i
PointerToArrayLVecBase3d = PointerToArray_LVecBase3d
PointerToArrayLVecBase3f = PointerToArray_LVecBase3f
PointerToArrayLVecBase3i = PointerToArray_LVecBase3i
PointerToArrayUnalignedLMatrix4d = PointerToArray_UnalignedLMatrix4d
PointerToArrayUnalignedLMatrix4f = PointerToArray_UnalignedLMatrix4f
PointerToArrayUnalignedLVecBase4d = PointerToArray_UnalignedLVecBase4d
PointerToArrayUnalignedLVecBase4f = PointerToArray_UnalignedLVecBase4f
PointerToArrayUnalignedLVecBase4i = PointerToArray_UnalignedLVecBase4i
LParabola = LParabolaf
LPlane = LPlanef
PlaneF = LPlanef
PlaneD = LPlaned
Plane = LPlanef
LFrustum = LFrustumf
FrustumF = LFrustumf
FrustumD = LFrustumd
Frustum = LFrustumf
PTA_LMatrix4f = PointerToArray_UnalignedLMatrix4f
PTALMatrix4f = PTA_LMatrix4f
CPTA_LMatrix4f = ConstPointerToArray_UnalignedLMatrix4f
CPTALMatrix4f = CPTA_LMatrix4f
PTA_LMatrix4d = PointerToArray_UnalignedLMatrix4d
PTALMatrix4d = PTA_LMatrix4d
CPTA_LMatrix4d = ConstPointerToArray_UnalignedLMatrix4d
CPTALMatrix4d = CPTA_LMatrix4d
PTA_LMatrix4 = PTA_LMatrix4f
PTALMatrix4 = PTA_LMatrix4
CPTA_LMatrix4 = CPTA_LMatrix4f
CPTALMatrix4 = CPTA_LMatrix4
PTAMat4 = PTA_LMatrix4
CPTAMat4 = CPTA_LMatrix4
PTAMat4d = PTA_LMatrix4d
CPTAMat4d = CPTA_LMatrix4d
PTA_LMatrix3f = PointerToArray_LMatrix3f
PTALMatrix3f = PTA_LMatrix3f
CPTA_LMatrix3f = ConstPointerToArray_LMatrix3f
CPTALMatrix3f = CPTA_LMatrix3f
PTA_LMatrix3d = PointerToArray_LMatrix3d
PTALMatrix3d = PTA_LMatrix3d
CPTA_LMatrix3d = ConstPointerToArray_LMatrix3d
CPTALMatrix3d = CPTA_LMatrix3d
PTA_LMatrix3 = PTA_LMatrix3f
PTALMatrix3 = PTA_LMatrix3
CPTA_LMatrix3 = CPTA_LMatrix3f
CPTALMatrix3 = CPTA_LMatrix3
PTAMat3 = PTA_LMatrix3
CPTAMat3 = CPTA_LMatrix3
PTAMat3d = PTA_LMatrix3d
CPTAMat3d = CPTA_LMatrix3d
PTA_LVecBase4f = PointerToArray_UnalignedLVecBase4f
PTALVecBase4f = PTA_LVecBase4f
CPTA_LVecBase4f = ConstPointerToArray_UnalignedLVecBase4f
CPTALVecBase4f = CPTA_LVecBase4f
PTA_LVecBase4d = PointerToArray_UnalignedLVecBase4d
PTALVecBase4d = PTA_LVecBase4d
CPTA_LVecBase4d = ConstPointerToArray_UnalignedLVecBase4d
CPTALVecBase4d = CPTA_LVecBase4d
PTA_LVecBase4i = PointerToArray_UnalignedLVecBase4i
PTALVecBase4i = PTA_LVecBase4i
CPTA_LVecBase4i = ConstPointerToArray_UnalignedLVecBase4i
CPTALVecBase4i = CPTA_LVecBase4i
PTA_LVecBase4 = PTA_LVecBase4f
PTALVecBase4 = PTA_LVecBase4
CPTA_LVecBase4 = CPTA_LVecBase4f
CPTALVecBase4 = CPTA_LVecBase4
PTAVecBase4f = PTA_LVecBase4f
CPTAVecBase4f = CPTA_LVecBase4f
PTAVecBase4d = PTA_LVecBase4d
CPTAVecBase4d = CPTA_LVecBase4d
PTA_LVecBase3f = PointerToArray_LVecBase3f
PTALVecBase3f = PTA_LVecBase3f
CPTA_LVecBase3f = ConstPointerToArray_LVecBase3f
CPTALVecBase3f = CPTA_LVecBase3f
PTA_LVecBase3d = PointerToArray_LVecBase3d
PTALVecBase3d = PTA_LVecBase3d
CPTA_LVecBase3d = ConstPointerToArray_LVecBase3d
CPTALVecBase3d = CPTA_LVecBase3d
PTA_LVecBase3i = PointerToArray_LVecBase3i
PTALVecBase3i = PTA_LVecBase3i
CPTA_LVecBase3i = ConstPointerToArray_LVecBase3i
CPTALVecBase3i = CPTA_LVecBase3i
PTA_LVecBase3 = PTA_LVecBase3f
PTALVecBase3 = PTA_LVecBase3
CPTA_LVecBase3 = CPTA_LVecBase3f
CPTALVecBase3 = CPTA_LVecBase3
PTAVecBase3f = PTA_LVecBase3f
CPTAVecBase3f = CPTA_LVecBase3f
PTAVecBase3d = PTA_LVecBase3d
CPTAVecBase3d = CPTA_LVecBase3d
PTA_LVecBase2f = PointerToArray_LVecBase2f
PTALVecBase2f = PTA_LVecBase2f
CPTA_LVecBase2f = ConstPointerToArray_LVecBase2f
CPTALVecBase2f = CPTA_LVecBase2f
PTA_LVecBase2d = PointerToArray_LVecBase2d
PTALVecBase2d = PTA_LVecBase2d
CPTA_LVecBase2d = ConstPointerToArray_LVecBase2d
CPTALVecBase2d = CPTA_LVecBase2d
PTA_LVecBase2i = PointerToArray_LVecBase2i
PTALVecBase2i = PTA_LVecBase2i
CPTA_LVecBase2i = ConstPointerToArray_LVecBase2i
CPTALVecBase2i = CPTA_LVecBase2i
PTA_LVecBase2 = PTA_LVecBase2f
PTALVecBase2 = PTA_LVecBase2
CPTA_LVecBase2 = CPTA_LVecBase2f
CPTALVecBase2 = CPTA_LVecBase2
PTAVecBase2f = PTA_LVecBase2f
CPTAVecBase2f = CPTA_LVecBase2f
PTAVecBase2d = PTA_LVecBase2d
CPTAVecBase2d = CPTA_LVecBase2d
