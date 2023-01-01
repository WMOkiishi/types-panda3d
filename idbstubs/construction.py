import itertools
import logging
from collections import defaultdict
from collections.abc import Iterable, Iterator, Sequence
from typing import Final, Protocol, TypeVar, cast

from attrs import evolve

from .idb_interface import (
    IDBElement,
    IDBFunction,
    IDBFunctionWrapper,
    IDBMakeSeq,
    IDBType,
    get_global_functions,
    get_global_types,
    get_globals,
    get_manifests,
)
from .idbutil import (
    element_is_exposed,
    function_is_exposed,
    type_has_copy_constructor,
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
    comment_to_docstring,
    make_class_name,
    make_method_name,
    snake_to_camel,
)
from .typedata import TYPE_ALIASES, get_type_name
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


def get_function_name(function: IDBFunction) -> str:
    """Return the Python name for a function."""
    if function.is_operator_typecast:
        if len(function.wrappers) != 1:
            scoped_name = function.scoped_name
            _logger.warning(f'Typecast {scoped_name!r} has multiple wrappers')
        return_type = unwrap_type(function.wrappers[0].return_type)
        if return_type.is_atomic:
            return f'__{get_type_name(return_type)}__'
    if function.is_unary_op:
        rename_dict = UNARY_METHOD_RENAMES
    else:
        rename_dict = METHOD_RENAMES
    if (special_rename := rename_dict.get(function.name)) is not None:
        return special_rename
    else:
        return make_method_name(function.name)


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


def make_manifest_reps() -> Iterator[Attribute]:
    """Yield representations of all manifests known to interrogate."""
    for manifest in get_manifests():
        type_name = 'Final[int]' if manifest.has_int_value else 'Final[str]'
        yield Attribute(manifest.name, type_name, namespace=('panda3d', 'core'))


def get_type_methods(idb_type: IDBType) -> Iterator[Function]:
    """Yield representations of all exposed methods
    for a type known to interrogate.
    """
    got_copy = got_deepcopy = False
    for idb_function in itertools.chain(
        idb_type.constructors,
        idb_type.casts,
        idb_type.up_down_casts,
        idb_type.methods,
    ):
        if not function_is_exposed(idb_function):
            continue
        method = make_function_rep(idb_function)
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
        elif method.name == '__len__' and idb_type.name in SIZE_NOT_LEN:
            method.name = 'size'
        elif method.name == '__copy__':
            got_copy = True
        elif method.name == '__deepcopy__':
            got_deepcopy = True
        yield method
    if type_has_copy_constructor(idb_type):
        if not got_copy:
            yield Function(
                '__copy__',
                [Signature([Parameter('self', 'Self')], 'Self')],
            )
        if not got_deepcopy:
            yield Function(
                '__deepcopy__',
                [Signature(
                    [
                        Parameter('self', 'Self'),
                        Parameter('memo', 'object', named=False),
                    ],
                    'Self',
                )],
            )
    for make_seq in idb_type.make_seqs:
        yield make_make_seq_rep(make_seq)


def make_typedef_rep(idb_type: IDBType) -> Alias:
    """Return a representation of a typedef known to interrogate."""
    wrapped_type = idb_type.wrapped_type
    name = make_class_name(idb_type.name)
    typedef_of = get_type_name(wrapped_type)
    of_local = idb_type.library_name == wrapped_type.library_name
    return Alias(name, typedef_of, of_local=of_local)


def make_attribute_rep(
        element: IDBElement,
        namespace: Sequence[str] = ()) -> Attribute:
    """Return an attribute representation of an element known to interrogate."""
    type_name = get_type_name(element.type)
    if element.is_sequence:
        if element.has_setter:
            seq_type = 'MutableSequence'
        else:
            seq_type = 'Sequence'
        type_name = f'{seq_type}[{type_name}]' if type_name else seq_type
        read_only = True
    elif element.is_mapping:
        getter_wrapper = element.getter.wrappers[0]
        if getter_wrapper.parameters[0].is_this:
            t = getter_wrapper.parameters[1].type
        else:
            t = getter_wrapper.parameters[0].type
        from_type = get_type_name(t) or 'Any'
        to_type = type_name or 'Any'
        if element.has_setter:
            map_type = 'MutableMapping'
        else:
            map_type = 'Mapping'
        type_name = f'{map_type}[{from_type}, {to_type}]'
        read_only = True
    else:
        read_only = not element.has_setter
    if not is_dunder(element.name):
        doc = comment_to_docstring(element.comment)
    else:
        doc = ''
    return Attribute(
        check_keyword(element.name),
        type_name,
        read_only=read_only,
        namespace=namespace,
        doc=doc,
        comment=get_comment(element.name, namespace),
    )


def make_signature_rep(
        wrapper: IDBFunctionWrapper,
        *, is_constructor: bool = False,
        ensure_self_param: bool = False) -> Signature:
    """Return a representation of the signature
    of a function wrapper known to interrogate.
    """
    ensure_self_param = ensure_self_param or is_constructor
    if is_constructor:
        return_type = 'None'
    else:
        return_type = get_type_name(wrapper.return_type)
    params: list[Parameter] = []
    if ensure_self_param:
        params.append(Parameter('self'))
    for param in wrapper.parameters:
        if param.is_this:
            if not ensure_self_param:
                params.append(Parameter('self'))
            continue
        params.append(Parameter(
            check_keyword(param.name),
            get_type_name(param.type),
            is_optional=param.is_optional,
            named=param.has_name,
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


def make_function_rep(function: IDBFunction) -> Function:
    """Return a representation of a function known to interrogate."""
    is_constructor = function.is_constructor
    name = '__init__' if is_constructor else get_function_name(function)
    scoped_name = function.scoped_name
    namespace = (
        function.module_name,
        *(make_class_name(s) for s in scoped_name.split('::')[:-1])
    )
    is_static_method = (
        function.is_method and not is_dunder(name)
        and not function.wrappers[0].parameters[0].is_this
    )
    omit_docstring = is_dunder(name) and name != '__init__'
    signatures: list[Signature] = []
    sigs_by_doc = defaultdict[str, list[str]](list)
    for wrapper in function.wrappers:
        if not wrapper_is_exposed(wrapper):
            continue
        signature = make_signature_rep(
            wrapper,
            is_constructor=function.is_constructor,
            ensure_self_param=function.is_method and not is_static_method,
        )
        signatures.append(signature)
        if not omit_docstring:
            sig_doc = comment_to_docstring(wrapper.comment)
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
        is_static=is_static_method,
        namespace=namespace,
        doc=doc,
        comment=get_comment(name, namespace),
    )


def make_type_reps(
        idb_type: IDBType,
        namespace: Sequence[str] = ()) -> Iterable[StubRep]:
    if idb_type.is_enum:
        if idb_type.is_scoped_enum:
            return make_scoped_enum_rep(idb_type, namespace),
        else:
            value_reps = make_enum_value_reps(idb_type, namespace)
            if idb_type.name:
                return flatten(with_alias(v, True) for v in value_reps)
            else:
                return value_reps
    if idb_type.is_typedef:
        class_ = make_typedef_rep(idb_type)
    else:
        class_ = make_class_rep(idb_type, namespace)
        if class_.name == 'BitMaskNative':
            return ()
    return with_alias(class_, True)


def make_make_seq_rep(make_seq: IDBMakeSeq) -> Function:
    """Return a representation of a MakeSeq known to interrogate."""
    element_getter = make_seq.element_getter
    namespace = (
        element_getter.module_name,
        *(make_class_name(s) for s in make_seq.scoped_name.split('::')[:-1])
    )
    return_type = get_type_name(element_getter.wrappers[0].return_type)
    signature = Signature([Parameter('self')], f'tuple[{return_type}, ...]')
    return Function(
        make_seq.seq_name,
        [signature],
        namespace=namespace,
        doc=comment_to_docstring(make_seq.comment),
        comment=get_comment(make_seq.seq_name, namespace),
    )


def make_enum_alias_rep(idb_type: IDBType) -> Alias:
    """Return a representation of a type alias
    for an enum type known to interrogate.
    """
    values = sorted(e.value for e in idb_type.enum_values)
    values_str = ', '.join(str(v) for v in values)
    definition = f'Literal[{values_str}]' if values else 'int'
    return Alias(idb_type.name, definition, is_type_alias=True)


def make_enum_value_reps(
        idb_type: IDBType,
        namespace: Sequence[str] = ()) -> list[Attribute]:
    """Return variable representations for an enum type known to interrogate."""
    value_reps: list[Attribute] = []
    for enum_value in idb_type.enum_values:
        if enum_value.scoped_name in NOT_EXPOSED:
            continue
        value_name = enum_value.name
        type_string = f'Final[Literal[{enum_value.value}]]'
        value_reps.append(Attribute(value_name, type_string, namespace=namespace))
    return value_reps


def make_scoped_enum_rep(
        idb_type: IDBType,
        namespace: Sequence[str] = ()) -> Class:
    """Return a representation of a scoped enum known to interrogate."""
    name = make_class_name(idb_type.name)
    this_namespace = (*namespace, name)
    values = {
        value.name: Attribute(value.name, 'int', namespace=this_namespace)
        for value in idb_type.enum_values
    }
    return Class(name, ['Enum'], values, is_final=idb_type.is_final, namespace=namespace)


def make_class_rep(
        idb_type: IDBType,
        namespace: Sequence[str] = ()) -> Class:
    """Return a representation of a class known to interrogate."""
    name = make_class_name(idb_type.name)
    class_body: dict[str, StubRep] = {}
    this_namespace = (*namespace, name)
    derivations = [
        get_type_name(derivation)
        for derivation in idb_type.derivations
        if type_is_exposed(derivation)
    ]
    if (type_vars := GENERIC.get(name)) is not None:
        derivations.append(f'Generic[{type_vars}]')
    # Attributes
    class_body['DtoolClassDict'] = Attribute(
        'DtoolClassDict', 'ClassVar[dict[str, Any]]', namespace=this_namespace
    )
    for elem in idb_type.elements:
        if element_is_exposed(elem) and elem.name not in NO_STUBS:
            attribute = make_attribute_rep(elem, this_namespace)
            class_body[attribute.name] = attribute
    if name.startswith('ParamValue_'):
        value = name[11:]
        if value in ('string', 'wstring'):
            value = 'str'
        class_body['value'] = Attribute('value', value, namespace=this_namespace)
    # Methods
    for method in get_type_methods(idb_type):
        if method.name in class_body:
            _logger.info(f'Discarding {method}; its name is already in use')
            continue
        class_body |= {rep.name: rep for rep in with_alias(method)}
    # Nested types
    for nested_type in idb_type.nested_types:
        if not type_is_exposed(nested_type):
            continue
        type_reps = make_type_reps(nested_type, this_namespace)
        class_body |= {rep.name: rep for rep in type_reps}
    scoped_name = '.'.join(this_namespace)
    return Class(
        name, derivations, class_body,
        is_final=idb_type.is_final,
        conditional=CONDITIONALS.get(scoped_name, ''),
        namespace=namespace,
        doc=comment_to_docstring(idb_type.comment),
        comment=get_comment(scoped_name),
    )


def make_package_rep(package_name: str = 'panda3d') -> Package:
    nested_by_mod_by_lib = defaultdict[str, defaultdict[str, list[StubRep]]](lambda: defaultdict(list))
    # Gather global functions
    for idb_function in itertools.chain(
        get_global_functions(),
        (g.getter for g in get_globals()),
    ):
        if not function_is_exposed(idb_function):
            continue
        function_rep = make_function_rep(idb_function)
        mod_name = idb_function.module_name
        lib_name = '_' + idb_function.library_name.removeprefix('libp3')
        nested_by_mod_by_lib[mod_name][lib_name] += with_alias(function_rep)

    # Gather global types
    for idb_type in get_global_types():
        if idb_type.is_nested:
            continue
        mod_name = idb_type.module_name
        lib_name = '_' + idb_type.library_name.removeprefix('libp3')
        nested_by_mod_by_lib[mod_name][lib_name] += make_type_reps(
            idb_type, mod_name.split('.')
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
