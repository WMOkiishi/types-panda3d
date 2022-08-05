import logging
from collections import defaultdict
from collections.abc import Iterable, Iterator, Sequence
from itertools import chain
from typing import Final, TypeVar, cast

import attrs
import panda3d.interrogatedb as idb

from .idbutil import (
    ElementIndex, FunctionIndex, FunctionWrapperIndex, MakeSeqIndex, TypeIndex,
    element_is_exposed, function_is_exposed, get_all_methods, get_derivations,
    get_global_functions, get_global_getters, get_python_wrappers,
    type_is_exposed, unwrap_type, wrapper_is_exposed
)
from .processors import process_function
from .reps import (
    Alias, Class, Element, Function, Module, Package, Parameter, Signature,
    StubRep
)
from .special_cases import ITERABLE, NO_MANGLING, NO_STUBS, NOT_EXPOSED
from .translation import (
    check_keyword, class_name_from_cpp_name, comment_to_docstring,
    method_name_from_cpp_name, snake_to_camel
)
from .typedata import get_direct_type_name, get_type_name
from .util import flatten

_logger: Final = logging.getLogger(__name__)

# Don't replace `size` with `__len__` for these
SIZE_NOT_LEN: Final = ('EggGroupNode', 'WindowProperties')

SR = TypeVar('SR', bound=StubRep)


def get_function_name(f: FunctionIndex, /) -> str:
    """Return the Python name for a function."""
    if idb.interrogate_function_is_operator_typecast(f):
        if idb.interrogate_function_number_of_python_wrappers(f) != 1:
            scoped_name = idb.interrogate_function_scoped_name(f)
            _logger.warning(f"Typecast '{scoped_name}' has multiple wrappers")
        w = idb.interrogate_function_python_wrapper(f, 0)
        return_type = unwrap_type(idb.interrogate_wrapper_return_type(w))
        if idb.interrogate_type_is_atomic(return_type):
            return f'__{get_type_name(return_type)}__'
    name = idb.interrogate_function_name(f)
    if idb.interrogate_function_is_unary_op(f):
        name += 'unary'
    return method_name_from_cpp_name(name)


def with_alias(
        rep: SR, /,
        capitalize: bool = False) -> tuple[SR] | tuple[SR, Alias]:
    """Return a tuple of the given `StubRep` and,
    if it would be unique, a camel-case alias.
    """
    name = rep.name
    if name not in NO_MANGLING:
        alias_name = check_keyword(snake_to_camel(name, capitalize))
        if alias_name != name:
            return (rep, Alias(alias_name, name, of_local=True))
    return (rep,)


def get_all_manifests() -> Iterator[Element]:
    """Yield representations of all manifests known to interrogate."""
    for n in range(idb.interrogate_number_of_manifests()):
        m = idb.interrogate_get_manifest(n)
        if idb.interrogate_manifest_has_int_value(m):
            value = idb.interrogate_manifest_get_int_value(m)
        else:
            value = idb.interrogate_manifest_definition(m)
        name = idb.interrogate_manifest_name(m)
        yield Element(name, f'Literal[{value!r}]', namespace=('panda3d', 'core'))


def get_type_methods(t: TypeIndex, /) -> Iterator[Function]:
    """Yield representations of all exposed methods
    for a type known to interrogate.
    """
    lt_function: Function | None = None
    seen_eq = False
    seen_le = False
    for f in get_all_methods(t):
        if not function_is_exposed(f):
            continue
        method = make_function_rep(f)
        if method.name in NO_STUBS:
            continue
        if method.name == '__len__':
            if idb.interrogate_type_name(t) in SIZE_NOT_LEN:
                method.name = 'size'
        elif method.name == '__lt__':
            lt_function = method
        elif method.name == '__eq__':
            seen_eq = True
        elif method.name == '__le__':
            seen_le = True
        yield method
    if lt_function is not None and seen_eq and not seen_le:
        yield attrs.evolve(lt_function, name='__le__')
    for n in range(idb.interrogate_type_number_of_make_seqs(t)):
        yield make_make_seq_rep(idb.interrogate_type_get_make_seq(t, n))


def make_typedef_rep(t: TypeIndex, /) -> Alias:
    """Return a representation of a typedef known to interrogate."""
    s = idb.interrogate_type_wrapped_type(t)
    name = get_direct_type_name(t)
    typedef_of = get_type_name(s)
    of_local = (
        idb.interrogate_type_library_name(t)
        ==
        idb.interrogate_type_library_name(s)
    )
    return Alias(name, typedef_of, of_local=of_local)


def make_element_rep(
        e: ElementIndex, /,
        namespace: Sequence[str] = ()) -> Element:
    """Return a representation of an element known to interrogate."""
    name = idb.interrogate_element_name(e)
    type_name = get_type_name(idb.interrogate_element_type(e))
    if idb.interrogate_element_is_sequence(e):
        type_name = f'Sequence[{type_name}]'
    elif idb.interrogate_element_is_mapping(e):
        type_name = f'Mapping[Any, {type_name}]'
    read_only = not idb.interrogate_element_setter(e)
    if idb.interrogate_element_has_comment(e):
        doc = comment_to_docstring(idb.interrogate_element_comment(e))
    else:
        doc = ''
    return Element(check_keyword(name), type_name, read_only=read_only,
                   namespace=namespace, doc=doc)


def make_signature_rep(
        w: FunctionWrapperIndex, /,
        is_constructor: bool = False) -> Signature:
    """Return a representation of the signature
    of a function wrapper known to interrogate.
    """
    if is_constructor:
        return_type = 'None'
        params = [Parameter.as_self()]
    else:
        return_type_index = idb.interrogate_wrapper_return_type(w)
        return_type = get_type_name(return_type_index)
        params: list[Parameter] = []
    for n in range(idb.interrogate_wrapper_number_of_parameters(w)):
        if idb.interrogate_wrapper_parameter_is_this(w, n):
            params.append(Parameter.as_self())
            continue
        params.append(Parameter(
            check_keyword(idb.interrogate_wrapper_parameter_name(w, n)),
            get_type_name(idb.interrogate_wrapper_parameter_type(w, n)),
            is_optional=idb.interrogate_wrapper_parameter_is_optional(w, n),
            named=idb.interrogate_wrapper_parameter_has_name(w, n),
        ))
    return Signature(params, return_type)


def make_function_rep(f: FunctionIndex, /) -> Function:
    """Return a representation of a function known to interrogate."""
    is_constructor = idb.interrogate_function_is_constructor(f)
    is_method = idb.interrogate_function_is_method(f)
    name = '__init__' if is_constructor else get_function_name(f)
    scoped_name = idb.interrogate_function_scoped_name(f)
    namespace = (
        idb.interrogate_function_module_name(f),
        *(class_name_from_cpp_name(s) for s in scoped_name.split('::')[:-1])
    )
    first_wrapper = idb.interrogate_function_python_wrapper(f, 0)
    not_static = idb.interrogate_wrapper_parameter_is_this(first_wrapper, 0)
    signatures: list[Signature] = []
    sigs_by_doc = defaultdict[str, list[str]](list)
    for w in get_python_wrappers(f):
        if not wrapper_is_exposed(w):
            continue
        signature = make_signature_rep(w, is_constructor)
        if not_static and (
            not signature.parameters
            or not signature.parameters[0].is_self
        ):
            signature.parameters = [Parameter.as_self(), *signature.parameters]
        signatures.append(signature)
        if idb.interrogate_wrapper_has_comment(w):
            sig_doc = comment_to_docstring(idb.interrogate_wrapper_comment(w))
            if sig_doc:
                param_string = f"`({', '.join(str(p) for p in signature.parameters)})`"
                sigs_by_doc[sig_doc].append(param_string)
    if len(sigs_by_doc) <= 1:
        doc = ''.join(sigs_by_doc)
    else:
        doc = '\n\n'.join(
            f"{'; '.join(p)}:\n{d}"
            for d, p in sigs_by_doc.items()
        )
    return Function(name, signatures, is_method=is_method,
                    namespace=namespace, doc=doc)


def make_type_reps(
        t: TypeIndex, /,
        namespace: Sequence[str] = (),
        *, infer_opt_params: bool = True,
        ignore_coercion: bool = False) -> Iterable[StubRep]:
    if idb.interrogate_type_is_enum(t):
        if idb.interrogate_type_is_scoped_enum(t):
            return make_scoped_enum_rep(t, namespace),
        else:
            value_reps = make_enum_value_reps(t, namespace)
            if idb.interrogate_type_name(t):
                return flatten(with_alias(v, True) for v in value_reps)
            else:
                return value_reps
    if idb.interrogate_type_is_typedef(t):
        class_ = make_typedef_rep(t)
    else:
        class_ = make_class_rep(
            t, namespace,
            infer_opt_params=infer_opt_params,
            ignore_coercion=ignore_coercion
        )
        if class_.name == 'BitMaskNative':
            return ()
    return with_alias(class_, True)


def make_make_seq_rep(ms: MakeSeqIndex, /) -> Function:
    """Return a representation of a MakeSeq known to interrogate."""
    name = idb.interrogate_make_seq_seq_name(ms)
    element_getter = idb.interrogate_make_seq_element_getter(ms)
    namespace = (
        idb.interrogate_function_module_name(element_getter),
        *(class_name_from_cpp_name(s) for s in
          idb.interrogate_make_seq_scoped_name(ms).split('::')[:-1])
    )
    element_getter_wrapper = idb.interrogate_function_python_wrapper(element_getter, 0)
    return_type_index = idb.interrogate_wrapper_return_type(element_getter_wrapper)
    return_type = get_type_name(return_type_index)
    signature = Signature([Parameter.as_self()], f'tuple[{return_type}, ...]')
    if idb.interrogate_make_seq_has_comment(ms):
        doc = comment_to_docstring(idb.interrogate_make_seq_comment(ms))
    else:
        doc = ''
    return Function(name, [signature], is_method=True, namespace=namespace, doc=doc)


def make_enum_alias_rep(t: TypeIndex, /) -> Alias:
    """Return a representation of a type alias
    for an enum type known to interrogate.
    """
    name = get_type_name(t)
    values = sorted(
        idb.interrogate_type_enum_value(t, n)
        for n in range(idb.interrogate_type_number_of_enum_values(t))
    )
    values_str = ', '.join(str(v) for v in values)
    definition = f'Literal[{values_str}]' if values else 'int'
    return Alias(name, definition, is_type_alias=True)


def make_enum_value_reps(
        t: TypeIndex, /,
        namespace: Sequence[str] = ()) -> list[Element]:
    """Return variable representations for an enum type known to interrogate."""
    is_nested = idb.interrogate_type_is_nested(t)
    value_reps: list[Element] = []
    for n in range(idb.interrogate_type_number_of_enum_values(t)):
        if idb.interrogate_type_enum_value_scoped_name(t, n) in NOT_EXPOSED:
            continue
        value = idb.interrogate_type_enum_value(t, n)
        value_name = idb.interrogate_type_enum_value_name(t, n)
        type = f'ClassVar[Literal[{value}]]' if is_nested else f'Literal[{value}]'
        value_reps.append(Element(value_name, type, namespace=namespace))
    return value_reps


def make_scoped_enum_rep(t: TypeIndex, /, namespace: Sequence[str] = ()) -> Class:
    """Return a representation of a scoped enum known to interrogate."""
    name = get_direct_type_name(t)
    this_namespace = (*namespace, name)
    value_elements = [
        Element(
            idb.interrogate_type_enum_value_name(t, n),
            'int', namespace=this_namespace
        )
        for n in range(idb.interrogate_type_number_of_enum_values(t))
    ]
    is_final = idb.interrogate_type_is_final(t)
    return Class(name, ['Enum'], value_elements,
                 is_final=is_final, namespace=namespace)


def make_class_rep(
        t: TypeIndex, /,
        namespace: Sequence[str] = (),
        *, infer_opt_params: bool = True,
        ignore_coercion: bool = False) -> Class:
    """Return a representation of a class known to interrogate."""
    name = get_direct_type_name(t)
    nested: list[StubRep] = []
    this_namespace = (*namespace, name)
    derivations = [
        get_type_name(j)
        for j in get_derivations(t)
        if type_is_exposed(j)
    ]
    # Elements
    nested.append(
        Element('DtoolClassDict', 'ClassVar[dict[str, Any]]',
                namespace=namespace)
    )
    for n in range(idb.interrogate_type_number_of_elements(t)):
        e = idb.interrogate_type_get_element(t, n)
        if element_is_exposed(e):
            nested.append(make_element_rep(e, namespace))
    if name.startswith('ParamValue_'):
        value = name[11:]
        if value in ('string', 'wstring'):
            value = 'str'
        nested.append(Element('value', value, namespace=namespace))
    # Methods
    for method in get_type_methods(t):
        method = process_function(
            method,
            infer_opt_params=infer_opt_params,
            ignore_coercion=ignore_coercion,
        )
        nested += with_alias(method)
    if (iterable_of := ITERABLE.get(name)) is not None:
        nested.append(Function(
            '__iter__',
            [Signature([Parameter.as_self()], f'Iterator[{iterable_of}]')],
            is_method=True, namespace=this_namespace,
        ))
    # Nested types
    for n in range(idb.interrogate_type_number_of_nested_types(t)):
        s = idb.interrogate_type_get_nested_type(t, n)
        if idb.interrogate_type_is_typedef(s):
            # Nested typedefs are not exposed to Python.
            # We can't lump this into `type_is_exposed` because it only matters for definitions.
            continue
        if not type_is_exposed(s):
            continue
        nested += make_type_reps(
            s, this_namespace,
            infer_opt_params=infer_opt_params,
            ignore_coercion=ignore_coercion
        )
    # Docstring
    if idb.interrogate_type_has_comment(t):
        doc = comment_to_docstring(idb.interrogate_type_comment(t))
    else:
        doc = ''
    return Class(
        name, derivations, nested,
        is_final=idb.interrogate_type_is_final(t),
        namespace=namespace,
        doc=doc,
    )


def make_package_rep(
        package_name: str = 'panda3d',
        *, infer_opt_params: bool = False,
        ignore_coercion: bool = False) -> Package:
    nested_by_mod_by_lib = defaultdict[str, defaultdict[str, list[StubRep]]](lambda: defaultdict(list))
    # Gather global functions
    for f in chain(get_global_functions(), get_global_getters()):
        if not function_is_exposed(f):
            continue
        function = process_function(
            make_function_rep(f),
            infer_opt_params=infer_opt_params,
            ignore_coercion=ignore_coercion,
        )
        mod_name = idb.interrogate_function_module_name(f)
        lib_name = '_' + idb.interrogate_function_library_name(f)
        nested_by_mod_by_lib[mod_name][lib_name] += with_alias(function)

    # Gather global types
    for n in range(idb.interrogate_number_of_global_types()):
        t = idb.interrogate_get_global_type(n)
        if idb.interrogate_type_is_nested(t):
            continue
        mod_name = idb.interrogate_type_module_name(t)
        lib_name = '_' + idb.interrogate_type_library_name(t)
        nested_by_mod_by_lib[mod_name][lib_name] += make_type_reps(
            t, mod_name.split('.'),
            infer_opt_params=infer_opt_params,
            ignore_coercion=ignore_coercion,
        )

    # Make package
    modules: list[Module] = []
    for mod_name, nested_by_lib in nested_by_mod_by_lib.items():
        nested_by_lib = cast(dict[str, Sequence[StubRep]], nested_by_lib)
        modules.append(Module(
            mod_name.removeprefix(package_name + '.'),
            nested_by_lib, namespace=(package_name,)
        ))
    return Package(package_name, modules)
