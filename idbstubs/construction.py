import logging
from collections import defaultdict
from collections.abc import Iterable, Iterator, Sequence
from itertools import chain
from typing import Final, TypeVar, cast

import panda3d.interrogatedb as idb
from attrs import evolve

from .idbutil import (
    ElementIndex, FunctionIndex, FunctionWrapperIndex, MakeSeqIndex, TypeIndex,
    element_is_exposed, function_is_exposed, get_all_methods, get_derivations,
    get_global_functions, get_global_getters, get_python_wrappers,
    type_is_exposed, unwrap_type, wrapper_is_exposed
)
from .processors import process_function
from .reps import (
    Alias, Attribute, Class, Function, Module, Package, Parameter, Signature,
    StubRep
)
from .special_cases import (
    ATTR_TYPE_OVERRIDES, GENERIC, IGNORE_ERRORS, ITERABLE, NO_MANGLING,
    NO_STUBS, NOT_EXPOSED
)
from .translation import (
    check_keyword, class_name_from_cpp_name, comment_to_docstring,
    method_name_from_cpp_name, snake_to_camel
)
from .typedata import (
    TYPE_ALIASES, get_direct_type_name, get_linear_superclasses, get_type_name
)
from .util import flatten, is_dunder

_logger: Final = logging.getLogger(__name__)
_class_bodies: Final[dict[str, dict[str, StubRep]]] = {}

# Don't replace `size` with `__len__` for these
SIZE_NOT_LEN: Final = ('EggGroupNode', 'WindowProperties')

SR = TypeVar('SR', bound=StubRep)


def get_function_name(f: FunctionIndex, /) -> str:
    """Return the Python name for a function."""
    if idb.interrogate_function_is_operator_typecast(f):
        if idb.interrogate_function_number_of_python_wrappers(f) != 1:
            scoped_name = idb.interrogate_function_scoped_name(f)
            _logger.warning(f'Typecast {scoped_name!r} has multiple wrappers')
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
        capitalize: bool = False) -> tuple[SR] | tuple[SR, SR | Alias]:
    """Return a tuple of the given `StubRep` and,
    if it would be unique, a camel-case alias.
    """
    name = rep.name
    if name not in NO_MANGLING:
        alias_name = check_keyword(snake_to_camel(name, capitalize))
        if alias_name != name:
            if isinstance(rep, Attribute) and not rep.read_only:
                return rep, evolve(rep, name=alias_name)
            else:
                return rep, Alias(alias_name, name, of_local=True,
                                  namespace=rep.namespace)
    return rep,


def get_all_manifests() -> Iterator[Attribute]:
    """Yield representations of all manifests known to interrogate."""
    for n in range(idb.interrogate_number_of_manifests()):
        m = idb.interrogate_get_manifest(n)
        if idb.interrogate_manifest_has_int_value(m):
            value = idb.interrogate_manifest_get_int_value(m)
        else:
            value = idb.interrogate_manifest_definition(m)
        name = idb.interrogate_manifest_name(m)
        yield Attribute(name, f'Final[{type(value).__name__}]', namespace=('panda3d', 'core'))


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
        elif method.name == '__getitem__':
            # Sometimes, the signatures for '__setitem__' are mixed in
            # with those for '__getitem__'. I'm not entirely sure why.
            getitem_sigs: list[Signature] = []
            setitem_sigs: list[Signature] = []
            for sig in method.signatures:
                if len(sig.parameters) <= 2:
                    getitem_sigs.append(sig)
                else:
                    setitem_sigs.append(sig)
            if getitem_sigs:
                yield evolve(method, signatures=getitem_sigs)
            if setitem_sigs:
                yield evolve(method, name='__setitem__', signatures=setitem_sigs)
            continue
        elif method.name == '__len__':
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
        yield evolve(lt_function, name='__le__')
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
        namespace: Sequence[str] = ()) -> Attribute:
    """Return a representation of an element known to interrogate."""
    name = idb.interrogate_element_name(e)
    type_name = ATTR_TYPE_OVERRIDES.get(idb.interrogate_element_scoped_name(e))
    if type_name is None:
        type_name = get_type_name(idb.interrogate_element_type(e))
    if idb.interrogate_element_is_sequence(e):
        type_name = f'Sequence[{type_name}]' if type_name else 'Sequence'
    elif idb.interrogate_element_is_mapping(e):
        type_name = f'Mapping[Any, {type_name}]' if type_name else 'Mapping'
    read_only = not idb.interrogate_element_setter(e)
    if idb.interrogate_element_has_comment(e):
        doc = comment_to_docstring(idb.interrogate_element_comment(e))
    else:
        doc = ''
    return Attribute(check_keyword(name), type_name, read_only=read_only,
                     namespace=namespace, doc=doc)


def make_signature_rep(
        w: FunctionWrapperIndex, /,
        *, is_constructor: bool = False,
        ensure_self_param: bool = False) -> Signature:
    """Return a representation of the signature
    of a function wrapper known to interrogate.
    """
    ensure_self_param = ensure_self_param or is_constructor
    if is_constructor:
        return_type = 'None'
    else:
        return_type_index = idb.interrogate_wrapper_return_type(w)
        return_type = get_type_name(return_type_index)
    params: list[Parameter] = []
    if ensure_self_param:
        params.append(Parameter.as_self())
    for n in range(idb.interrogate_wrapper_number_of_parameters(w)):
        if idb.interrogate_wrapper_parameter_is_this(w, n):
            if not ensure_self_param:
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
    not_static = (
        is_method and is_dunder(name)
        or idb.interrogate_wrapper_parameter_is_this(first_wrapper, 0)
    )
    signatures: list[Signature] = []
    sigs_by_doc = defaultdict[str, list[str]](list)
    for w in get_python_wrappers(f):
        if not wrapper_is_exposed(w):
            continue
        signature = make_signature_rep(w, is_constructor=is_constructor,
                                       ensure_self_param=not_static)
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
    return Function(
        name,
        signatures,
        is_method=is_method,
        is_static=not not_static,
        namespace=namespace,
        doc=doc,
    )


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
        if not idb.interrogate_type_is_nested(t):
            _class_bodies[class_.name] = dict(class_.body)
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
        namespace: Sequence[str] = ()) -> list[Attribute]:
    """Return variable representations for an enum type known to interrogate."""
    value_reps: list[Attribute] = []
    for n in range(idb.interrogate_type_number_of_enum_values(t)):
        if idb.interrogate_type_enum_value_scoped_name(t, n) in NOT_EXPOSED:
            continue
        value = idb.interrogate_type_enum_value(t, n)
        value_name = idb.interrogate_type_enum_value_name(t, n)
        type_string = f'Final[Literal[{value}]]'
        value_reps.append(Attribute(value_name, type_string, namespace=namespace))
    return value_reps


def make_scoped_enum_rep(t: TypeIndex, /, namespace: Sequence[str] = ()) -> Class:
    """Return a representation of a scoped enum known to interrogate."""
    name = get_direct_type_name(t)
    this_namespace = (*namespace, name)
    value_elements: dict[str, Attribute] = {}
    for n in range(idb.interrogate_type_number_of_enum_values(t)):
        value_name = idb.interrogate_type_enum_value_name(t, n)
        value_elements[value_name] = Attribute(
            value_name, 'int', namespace=this_namespace
        )
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
    class_body: dict[str, StubRep] = {}
    this_namespace = (*namespace, name)
    derivations = [
        get_type_name(j)
        for j in get_derivations(t)
        if type_is_exposed(j)
    ]
    if (type_vars := GENERIC.get(name)) is not None:
        derivations.append(f'Generic[{type_vars}]')
    # Elements
    class_body['DtoolClassDict'] = Attribute(
        'DtoolClassDict', 'ClassVar[dict[str, Any]]', namespace=this_namespace
    )
    for n in range(idb.interrogate_type_number_of_elements(t)):
        e = idb.interrogate_type_get_element(t, n)
        if element_is_exposed(e) and not idb.interrogate_element_name(e) in NO_STUBS:
            element = make_element_rep(e, this_namespace)
            class_body[element.name] = element
    if name.startswith('ParamValue_'):
        value = name[11:]
        if value in ('string', 'wstring'):
            value = 'str'
        class_body['value'] = Attribute('value', value, namespace=this_namespace)
    # Methods
    for method in get_type_methods(t):
        method = process_function(
            method,
            infer_opt_params=infer_opt_params,
            ignore_coercion=ignore_coercion,
        )
        if method.name in class_body:
            _logger.info(f'Discarding {method}; its name is already in use')
            continue
        class_body |= {rep.name: rep for rep in with_alias(method)}
    if (iterable_of := ITERABLE.get(name)) is not None:
        class_body['__iter__'] = Function(
            '__iter__',
            [Signature([Parameter.as_self()], f'Iterator[{iterable_of}]')],
            is_method=True, namespace=this_namespace,
        )
    # Nested types
    for n in range(idb.interrogate_type_number_of_nested_types(t)):
        s = idb.interrogate_type_get_nested_type(t, n)
        if idb.interrogate_type_is_typedef(s):
            # Nested typedefs are not exposed to Python.
            # We can't lump this into `type_is_exposed` because it only matters for definitions.
            continue
        if not type_is_exposed(s):
            continue
        type_reps = make_type_reps(
            s, this_namespace,
            infer_opt_params=infer_opt_params,
            ignore_coercion=ignore_coercion,
        )
        class_body |= {rep.name: rep for rep in type_reps}
    # "type: ignore" comments
    for rep in class_body.values():
        if (ignored_errors := IGNORE_ERRORS.get(rep.scoped_name)) is not None:
            rep.comment = f'type: ignore[{ignored_errors}]'
    # Docstring
    if idb.interrogate_type_has_comment(t):
        doc = comment_to_docstring(idb.interrogate_type_comment(t))
    else:
        doc = ''
    return Class(
        name, derivations, class_body,
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
        lib_name = '_' + idb.interrogate_function_library_name(f).removeprefix('libp3')
        nested_by_mod_by_lib[mod_name][lib_name] += with_alias(function)

    # Gather global types
    for n in range(idb.interrogate_number_of_global_types()):
        t = idb.interrogate_get_global_type(n)
        if idb.interrogate_type_is_nested(t):
            continue
        mod_name = idb.interrogate_type_module_name(t)
        lib_name = '_' + idb.interrogate_type_library_name(t).removeprefix('libp3')
        nested_by_mod_by_lib[mod_name][lib_name] += make_type_reps(
            t, mod_name.split('.'),
            infer_opt_params=infer_opt_params,
            ignore_coercion=ignore_coercion,
        )

    # Make package
    modules: list[Module] = []
    for mod_name, nested_by_lib in nested_by_mod_by_lib.items():
        for rep in flatten(nested_by_lib.values()):
            if (ignored_errors := IGNORE_ERRORS.get(rep.scoped_name)) is not None:
                rep.comment = f'type: ignore[{ignored_errors}]'
            if isinstance(rep, Class):
                process_class(rep)
        nested_by_lib = cast(dict[str, Sequence[StubRep]], nested_by_lib)
        modules.append(Module(
            mod_name.removeprefix(package_name + '.'),
            nested_by_lib, namespace=(package_name,)
        ))
    return Package(package_name, modules)


def process_class(class_: Class) -> None:
    class_body = _class_bodies.get(class_.name)
    if class_body is None:
        return
    nested_names = set(class_body.keys())
    for base_class in get_linear_superclasses(class_.name):
        base_class_body = _class_bodies.get(base_class)
        if base_class_body is None:
            continue
        for name in nested_names & base_class_body.keys():
            match class_body[name], base_class_body[name]:
                case Class() | Alias(of_local=True), _:
                    continue
                case (
                    Function(doc=doc_1),
                    Function(doc=doc_2)
                ) if doc_1 and doc_1 != doc_2:
                    continue
                case (
                    Attribute(doc=doc_1, read_only=True),
                    Attribute(doc=doc_2, read_only=True)
                ) if doc_1 and doc_1 != doc_2:
                    continue
                case a, b if a == b:
                    del class_body[name]
                    nested_names.remove(name)
    new_nested: dict[str, StubRep] = {}
    for rep in class_.body.values():
        if isinstance(rep, Alias) and rep.of_local:
            name_to_check = rep.alias_of
        else:
            name_to_check = rep.name
        if name_to_check in nested_names:
            new_nested[rep.name] = rep
    class_.body = new_nested


def make_typing_module() -> Module:
    aliases = [
        Alias(name, definition, is_type_alias=True)
        for name, definition in TYPE_ALIASES.items()
    ]
    return Module('_typing', {'typing': aliases}, namespace=('panda3d',))
