import logging
from collections import defaultdict
from collections.abc import Iterable, Iterator, Sequence
from typing import Final, Protocol, TypeVar, cast

import panda3d.interrogatedb as idb
from attrs import evolve

from .idbutil import (
    ElementIndex,
    FunctionIndex,
    FunctionWrapperIndex,
    MakeSeqIndex,
    TypeIndex,
    element_is_exposed,
    function_is_exposed,
    get_all_methods,
    get_derivations,
    get_elements,
    get_global_functions,
    get_global_types,
    get_nested_types,
    get_python_wrappers,
    type_is_exposed,
    unwrap_type,
    wrapper_is_exposed,
)
from .reps import (
    Alias,
    Attribute,
    Class,
    Function,
    Module,
    Package,
    Parameter,
    Signature,
    StubRep,
)
from .special_cases import (
    CONDITIONALS,
    GENERIC,
    IGNORE_ERRORS,
    METHOD_RENAMES,
    NO_MANGLING,
    NO_STUBS,
    NOT_EXPOSED,
    SIZE_NOT_LEN,
    UNARY_METHOD_RENAMES,
)
from .translation import (
    check_keyword,
    class_name_from_cpp_name,
    comment_to_docstring,
    method_name_from_cpp_name,
    snake_to_camel,
)
from .typedata import TYPE_ALIASES, get_direct_type_name, get_type_name
from .util import flatten, is_dunder

_logger: Final = logging.getLogger(__name__)


class NamespacedStubRep(StubRep, Protocol):
    namespace: Sequence[str]


SR = TypeVar('SR', bound=NamespacedStubRep)


def get_comment(name: str, namespace: Iterable[str] = ()) -> str:
    scoped_name = '.'.join((*namespace, name))
    # Sneak in some "noqa" comments
    if scoped_name == 'panda3d.core.StreamWrapper.iostream':
        return 'noqa: F811'
    elif (
        scoped_name.startswith('panda3d.core.CallbackGraphicsWindow')
        and scoped_name.endswith((
            'EventsCallbackData',
            'PropertiesCallbackData',
            'RenderCallbackData',
        ))
    ):
        return 'noqa: F821'
    ignored_errors = IGNORE_ERRORS.get(scoped_name)
    if ignored_errors is None:
        return ''
    return f'type: ignore[{ignored_errors}]'


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
        rename_dict = UNARY_METHOD_RENAMES
    else:
        rename_dict = METHOD_RENAMES
    if (special_rename := rename_dict.get(name)) is not None:
        return special_rename
    else:
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
                return rep, Alias(
                    alias_name,
                    name,
                    of_local=True,
                    comment=get_comment(alias_name, rep.namespace),
                )
    return rep,


def get_all_manifests() -> Iterator[Attribute]:
    """Yield representations of all manifests known to interrogate."""
    for n in range(idb.interrogate_number_of_manifests()):
        m = idb.interrogate_get_manifest(n)
        name = idb.interrogate_manifest_name(m)
        type_name = 'int' if idb.interrogate_manifest_has_int_value(m) else 'str'
        yield Attribute(name, f'Final[{type_name}]', namespace=('panda3d', 'core'))


def get_type_methods(t: TypeIndex, /) -> Iterator[Function]:
    """Yield representations of all exposed methods
    for a type known to interrogate.
    """
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
        yield method
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
    type_name = get_type_name(idb.interrogate_element_type(e))
    if idb.interrogate_element_is_sequence(e):
        if idb.interrogate_element_has_setter(e):
            seq_type = 'MutableSequence'
        else:
            seq_type = 'Sequence'
        type_name = f'{seq_type}[{type_name}]' if type_name else seq_type
        read_only = True
    elif idb.interrogate_element_is_mapping(e):
        getter = idb.interrogate_element_getter(e)
        wrapper = idb.interrogate_function_python_wrapper(getter, 0)
        if idb.interrogate_wrapper_parameter_is_this(wrapper, 0):
            t = idb.interrogate_wrapper_parameter_type(wrapper, 1)
        else:
            t = idb.interrogate_wrapper_parameter_type(wrapper, 0)
        from_type = get_type_name(t) or 'Any'
        to_type = type_name or 'Any'
        if idb.interrogate_element_has_setter(e):
            map_type = 'MutableMapping'
        else:
            map_type = 'Mapping'
        type_name = f'{map_type}[{from_type}, {to_type}]'
        read_only = True
    else:
        read_only = not idb.interrogate_element_has_setter(e)
    if idb.interrogate_element_has_comment(e) and not is_dunder(name):
        doc = comment_to_docstring(idb.interrogate_element_comment(e))
    else:
        doc = ''
    return Attribute(
        check_keyword(name),
        type_name,
        read_only=read_only,
        namespace=namespace,
        doc=doc,
        comment=get_comment(name, namespace),
    )


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
        params.append(Parameter('self'))
    for n in range(idb.interrogate_wrapper_number_of_parameters(w)):
        if idb.interrogate_wrapper_parameter_is_this(w, n):
            if not ensure_self_param:
                params.append(Parameter('self'))
            continue
        params.append(Parameter(
            check_keyword(idb.interrogate_wrapper_parameter_name(w, n)),
            get_type_name(idb.interrogate_wrapper_parameter_type(w, n)),
            is_optional=idb.interrogate_wrapper_parameter_is_optional(w, n),
            named=idb.interrogate_wrapper_parameter_has_name(w, n),
        ))
    match params:
        case [Parameter(name='args') as args]:
            args.name = '*' + args.name
        case [
            *_,
            Parameter(name='args') as args,
            Parameter(name='kwargs' | 'kwds') as kwargs,
        ]:
            args.name = '*' + args.name
            kwargs.name = '**' + kwargs.name
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
    omit_docstring = is_dunder(name) and name != '__init__'
    signatures: list[Signature] = []
    sigs_by_doc = defaultdict[str, list[str]](list)
    for w in get_python_wrappers(f):
        if not wrapper_is_exposed(w):
            continue
        signature = make_signature_rep(w, is_constructor=is_constructor,
                                       ensure_self_param=not_static)
        signatures.append(signature)
        if idb.interrogate_wrapper_has_comment(w) and not omit_docstring:
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
        comment=get_comment(name, namespace),
    )


def make_type_reps(
        t: TypeIndex, /,
        namespace: Sequence[str] = ()) -> Iterable[StubRep]:
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
        class_ = make_class_rep(t, namespace)
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
    signature = Signature([Parameter('self')], f'tuple[{return_type}, ...]')
    if idb.interrogate_make_seq_has_comment(ms):
        doc = comment_to_docstring(idb.interrogate_make_seq_comment(ms))
    else:
        doc = ''
    return Function(
        name,
        [signature],
        is_method=True,
        namespace=namespace,
        doc=doc,
        comment=get_comment(name, namespace),
    )


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
        namespace: Sequence[str] = ()) -> Class:
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
    for e in get_elements(t):
        if element_is_exposed(e) and idb.interrogate_element_name(e) not in NO_STUBS:
            element = make_element_rep(e, this_namespace)
            class_body[element.name] = element
    if name.startswith('ParamValue_'):
        value = name[11:]
        if value in ('string', 'wstring'):
            value = 'str'
        class_body['value'] = Attribute('value', value, namespace=this_namespace)
    # Methods
    for method in get_type_methods(t):
        if method.name in class_body:
            _logger.info(f'Discarding {method}; its name is already in use')
            continue
        class_body |= {rep.name: rep for rep in with_alias(method)}
    # Nested types
    for s in get_nested_types(t):
        if not type_is_exposed(s):
            continue
        type_reps = make_type_reps(s, this_namespace)
        class_body |= {rep.name: rep for rep in type_reps}
    # Docstring
    if idb.interrogate_type_has_comment(t):
        doc = comment_to_docstring(idb.interrogate_type_comment(t))
    else:
        doc = ''
    scoped_name = '.'.join(this_namespace)
    return Class(
        name, derivations, class_body,
        is_final=idb.interrogate_type_is_final(t),
        conditional=CONDITIONALS.get(scoped_name, ''),
        namespace=namespace,
        doc=doc,
        comment=get_comment(scoped_name),
    )


def make_package_rep(package_name: str = 'panda3d') -> Package:
    nested_by_mod_by_lib = defaultdict[str, defaultdict[str, list[StubRep]]](lambda: defaultdict(list))
    # Gather global functions
    for f in get_global_functions():
        if not function_is_exposed(f):
            continue
        function = make_function_rep(f)
        mod_name = idb.interrogate_function_module_name(f)
        lib_name = '_' + idb.interrogate_function_library_name(f).removeprefix('libp3')
        nested_by_mod_by_lib[mod_name][lib_name] += with_alias(function)

    # Gather global types
    for t in get_global_types():
        mod_name = idb.interrogate_type_module_name(t)
        lib_name = '_' + idb.interrogate_type_library_name(t).removeprefix('libp3')
        nested_by_mod_by_lib[mod_name][lib_name] += make_type_reps(
            t, mod_name.split('.')
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


def make_typing_module() -> Module:
    aliases = [
        Alias(name, definition, is_type_alias=True)
        for name, definition in TYPE_ALIASES.items()
    ]
    return Module('_typing', {'typing': aliases}, namespace=('panda3d',))
