from __future__ import annotations

from collections.abc import Iterator
from typing import Literal, TypeAlias

import attrs
import panda3d.interrogatedb as idb

TypeIndex: TypeAlias = int
ElementIndex: TypeAlias = int
FunctionIndex: TypeAlias = int
FunctionWrapperIndex: TypeAlias = int
MakeSeqIndex: TypeAlias = int
ManifestIndex: TypeAlias = int
AtomicToken: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


@attrs.define
class IDBManifest:
    index: ManifestIndex

    @property
    def name(self) -> str:
        return idb.interrogate_manifest_name(self.index)

    @property
    def has_int_value(self) -> bool:
        return idb.interrogate_manifest_has_int_value(self.index)


@attrs.define
class IDBParameter:
    index: int
    wrapper_index: FunctionWrapperIndex

    @property
    def has_name(self) -> bool:
        return idb.interrogate_wrapper_parameter_has_name(self.wrapper_index, self.index)

    @property
    def name(self) -> str:
        return idb.interrogate_wrapper_parameter_name(self.wrapper_index, self.index)

    @property
    def type(self) -> IDBType:
        return IDBType(idb.interrogate_wrapper_parameter_type(self.wrapper_index, self.index))

    @property
    def is_this(self) -> bool:
        return idb.interrogate_wrapper_parameter_is_this(self.wrapper_index, self.index)

    @property
    def is_optional(self) -> bool:
        return idb.interrogate_wrapper_parameter_is_optional(self.wrapper_index, self.index)


@attrs.define
class IDBFunctionWrapper:
    index: FunctionWrapperIndex

    @attrs.define
    class ParameterList:
        wrapper_index: FunctionWrapperIndex

        def __len__(self) -> int:
            return idb.interrogate_wrapper_number_of_parameters(self.wrapper_index)

        def __getitem__(self, item: int) -> IDBParameter:
            return IDBParameter(item, self.wrapper_index)

        def __iter__(self) -> Iterator[IDBParameter]:
            for n in range(len(self)):
                yield self[n]

    @property
    def comment(self) -> str:
        return idb.interrogate_wrapper_comment(self.index)

    @property
    def parameters(self) -> ParameterList:
        return IDBFunctionWrapper.ParameterList(self.index)

    @property
    def return_type(self) -> IDBType:
        return IDBType(idb.interrogate_wrapper_return_type(self.index))


@attrs.define
class IDBFunction:
    index: FunctionIndex

    @attrs.define
    class WrapperList:
        function_index: FunctionIndex

        def __len__(self) -> int:
            return idb.interrogate_function_number_of_python_wrappers(self.function_index)

        def __getitem__(self, item: int) -> IDBFunctionWrapper:
            w = idb.interrogate_function_python_wrapper(self.function_index, item)
            return IDBFunctionWrapper(w)

        def __iter__(self) -> Iterator[IDBFunctionWrapper]:
            for n in range(len(self)):
                yield self[n]

    @property
    def name(self) -> str:
        return idb.interrogate_function_name(self.index)

    @property
    def scoped_name(self) -> str:
        return idb.interrogate_function_scoped_name(self.index)

    @property
    def module_name(self) -> str:
        return idb.interrogate_function_module_name(self.index)

    @property
    def library_name(self) -> str:
        return idb.interrogate_function_library_name(self.index)

    @property
    def is_method(self) -> bool:
        return idb.interrogate_function_is_method(self.index)

    @property
    def is_constructor(self) -> bool:
        return idb.interrogate_function_is_constructor(self.index)

    @property
    def is_unary_op(self) -> bool:
        return idb.interrogate_function_is_unary_op(self.index)

    @property
    def is_operator_typecast(self) -> bool:
        return idb.interrogate_function_is_operator_typecast(self.index)

    @property
    def wrappers(self) -> WrapperList:
        return IDBFunction.WrapperList(self.index)


@attrs.define
class IDBMakeSeq:
    index: MakeSeqIndex

    @property
    def seq_name(self) -> str:
        return idb.interrogate_make_seq_seq_name(self.index)

    @property
    def scoped_name(self) -> str:
        return idb.interrogate_make_seq_scoped_name(self.index)

    @property
    def comment(self) -> str:
        return idb.interrogate_make_seq_comment(self.index)

    @property
    def element_getter(self) -> IDBFunction:
        return IDBFunction(idb.interrogate_make_seq_element_getter(self.index))


@attrs.define
class IDBElement:
    index: ElementIndex

    @property
    def name(self) -> str:
        return idb.interrogate_element_name(self.index)

    @property
    def scoped_name(self) -> str:
        return idb.interrogate_element_scoped_name(self.index)

    @property
    def comment(self) -> str:
        return idb.interrogate_element_comment(self.index)

    @property
    def type(self) -> IDBType:
        return IDBType(idb.interrogate_element_type(self.index))

    @property
    def getter(self) -> IDBFunction:
        return IDBFunction(idb.interrogate_element_getter(self.index))

    @property
    def has_setter(self) -> bool:
        return idb.interrogate_element_has_setter(self.index)

    @property
    def is_sequence(self) -> bool:
        return idb.interrogate_element_is_sequence(self.index)

    @property
    def is_mapping(self) -> bool:
        return idb.interrogate_element_is_mapping(self.index)


@attrs.define
class IDBEnumValue:
    index: int
    type_index: TypeIndex

    @property
    def name(self) -> str:
        return idb.interrogate_type_enum_value_name(self.type_index, self.index)

    @property
    def scoped_name(self) -> str:
        return idb.interrogate_type_enum_value_scoped_name(self.type_index, self.index)

    @property
    def value(self) -> int:
        return idb.interrogate_type_enum_value(self.type_index, self.index)


@attrs.define(frozen=True)
class IDBType:
    index: TypeIndex

    @attrs.define
    class EnumValueList:
        type_index: FunctionWrapperIndex

        def __len__(self) -> int:
            return idb.interrogate_type_number_of_enum_values(self.type_index)

        def __getitem__(self, item: int) -> IDBEnumValue:
            return IDBEnumValue(item, self.type_index)

        def __iter__(self) -> Iterator[IDBEnumValue]:
            for n in range(len(self)):
                yield self[n]

    def __str__(self) -> str:
        return f'{self.name!r} ({self.index})'

    @property
    def name(self) -> str:
        return idb.interrogate_type_name(self.index)

    @property
    def scoped_name(self) -> str:
        return idb.interrogate_type_scoped_name(self.index)

    @property
    def comment(self) -> str:
        return idb.interrogate_type_comment(self.index)

    @property
    def module_name(self) -> str:
        return idb.interrogate_type_module_name(self.index)

    @property
    def library_name(self) -> str:
        return idb.interrogate_type_library_name(self.index)

    @property
    def is_global(self) -> bool:
        return idb.interrogate_type_is_global(self.index)

    @property
    def is_nested(self) -> bool:
        return idb.interrogate_type_is_nested(self.index)

    @property
    def is_atomic(self) -> bool:
        return idb.interrogate_type_is_atomic(self.index)

    @property
    def atomic_token(self) -> AtomicToken:
        return idb.interrogate_type_atomic_token(self.index)

    @property
    def is_wrapped(self) -> bool:
        return idb.interrogate_type_is_wrapped(self.index)

    @property
    def is_typedef(self) -> bool:
        return idb.interrogate_type_is_typedef(self.index)

    @property
    def wrapped_type(self) -> IDBType:
        return IDBType(idb.interrogate_type_wrapped_type(self.index))

    @property
    def is_array(self) -> bool:
        return idb.interrogate_type_is_array(self.index)

    @property
    def is_enum(self) -> bool:
        return idb.interrogate_type_is_enum(self.index)

    @property
    def is_scoped_enum(self) -> bool:
        return idb.interrogate_type_is_scoped_enum(self.index)

    @property
    def enum_values(self) -> EnumValueList:
        return IDBType.EnumValueList(self.index)

    @property
    def is_fully_defined(self) -> bool:
        return idb.interrogate_type_is_fully_defined(self.index)

    @property
    def is_unpublished(self) -> bool:
        return idb.interrogate_type_is_unpublished(self.index)

    @property
    def is_final(self) -> bool:
        return idb.interrogate_type_is_final(self.index)

    @property
    def derivations(self) -> Iterator[IDBType]:
        for n in range(idb.interrogate_type_number_of_derivations(self.index)):
            yield IDBType(idb.interrogate_type_get_derivation(self.index, n))

    @property
    def constructors(self) -> Iterator[IDBFunction]:
        for n in range(idb.interrogate_type_number_of_constructors(self.index)):
            yield IDBFunction(idb.interrogate_type_get_constructor(self.index, n))

    @property
    def elements(self) -> Iterator[IDBElement]:
        for n in range(idb.interrogate_type_number_of_elements(self.index)):
            yield IDBElement(idb.interrogate_type_get_element(self.index, n))

    @property
    def methods(self) -> Iterator[IDBFunction]:
        for n in range(idb.interrogate_type_number_of_methods(self.index)):
            yield IDBFunction(idb.interrogate_type_get_method(self.index, n))

    @property
    def make_seqs(self) -> Iterator[IDBMakeSeq]:
        for n in range(idb.interrogate_type_number_of_make_seqs(self.index)):
            yield IDBMakeSeq(idb.interrogate_type_get_make_seq(self.index, n))

    @property
    def casts(self) -> Iterator[IDBFunction]:
        for n in range(idb.interrogate_type_number_of_casts(self.index)):
            yield IDBFunction(idb.interrogate_type_get_cast(self.index, n))

    @property
    def up_down_casts(self) -> Iterator[IDBFunction]:
        for n in range(idb.interrogate_type_number_of_derivations(self.index)):
            if idb.interrogate_type_derivation_has_upcast(self.index, n):
                yield IDBFunction(idb.interrogate_type_get_upcast(self.index, n))
            if idb.interrogate_type_derivation_has_downcast(self.index, n):
                yield IDBFunction(idb.interrogate_type_get_downcast(self.index, n))

    @property
    def nested_types(self) -> Iterator[IDBType]:
        for n in range(idb.interrogate_type_number_of_nested_types(self.index)):
            yield IDBType(idb.interrogate_type_get_nested_type(self.index, n))


def get_manifests() -> Iterator[IDBManifest]:
    """Yield all manifests known to interrogate."""
    for n in range(idb.interrogate_number_of_manifests()):
        yield IDBManifest(idb.interrogate_get_manifest(n))


def get_globals() -> Iterator[IDBElement]:
    """Yield all globals known to interrogate."""
    for n in range(idb.interrogate_number_of_globals()):
        yield IDBElement(idb.interrogate_get_global(n))


def get_all_types() -> Iterator[IDBType]:
    """Yield all types known to interrogate."""
    for n in range(idb.interrogate_number_of_types()):
        yield IDBType(idb.interrogate_get_type(n))


def get_global_types() -> Iterator[IDBType]:
    """Yield all global types known to interrogate."""
    for n in range(idb.interrogate_number_of_global_types()):
        yield IDBType(idb.interrogate_get_global_type(n))


def get_global_functions() -> Iterator[IDBFunction]:
    """Yield all global functions known to interrogate."""
    for n in range(idb.interrogate_number_of_global_functions()):
        yield IDBFunction(idb.interrogate_get_global_function(n))
