import itertools
import logging
from collections import defaultdict
from collections.abc import Iterator, Sequence
from typing import Final, cast

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
    type_is_exposed,
    wrapper_is_exposed,
)
from .reps import (
    Alias,
    Attribute,
    Class,
    Constant,
    Function,
    Module,
    Package,
    Parameter,
    Signature,
    StubRep,
    TypeAlias,
)
from .special_cases import (
    ATTR_TYPE_OVERRIDES,
    CONDITIONALS,
    DEFAULT_RETURNS,
    GENERIC,
    IGNORE_ERRORS,
    METHOD_RENAMES,
    NO_ALIAS,
    NO_STUBS,
    NOT_EXPOSED,
    PARAM_TYPE_OVERRIDES,
    RETURN_SELF,
    RETURN_TYPE_OVERRIDES,
    UNARY_METHOD_RENAMES,
)
from .translation import (
    check_keyword,
    comment_to_docstring,
    make_alias_name,
    make_class_name,
    make_method_name,
)
from .typedata import TYPE_ALIASES, get_type_name
from .util import is_dunder

_logger: Final = logging.getLogger(__name__)


def get_comment(scoped_name: str) -> str:
    # Sneak in some "noqa" comments
    if scoped_name == 'StreamWrapper::iostream':
        return 'noqa: F811'
    elif (
        scoped_name.startswith('CallbackGraphicsWindow')
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
    if function.is_constructor:
        return '__init__'
    if function.is_operator_typecast:
        if len(function.wrappers) != 1:
            scoped_name = function.scoped_name
            _logger.warning(f'Typecast {scoped_name!r} has multiple wrappers')
        return_type = function.wrappers[0].return_type.unwrap()
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


def make_manifest_reps() -> Iterator[Attribute]:
    """Yield representations of all manifests known to interrogate."""
    for manifest in get_manifests():
        type_name = 'Final[int]' if manifest.has_int_value else 'Final[str]'
        yield Attribute(manifest.name, type_name)
        alias_name = make_alias_name(manifest.name)
        if alias_name != manifest.name:
            yield Attribute(alias_name, type_name)


def get_type_methods(idb_type: IDBType) -> Iterator[Function]:
    """Yield representations of all exposed methods
    for a type known to interrogate.
    """
    method_names = {method.name for method in idb_type.methods}
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
        elif method.name == '__len__' and (
            'operator []' not in method_names
            and '__getitem__' not in method_names
        ):
            method.name = 'size'
        yield method
    if idb_type.check_for_copy_constructor() or 'make_copy' in method_names:
        if '__copy__' not in method_names:
            yield Function('__copy__', [Signature([Parameter('self')], 'Self')])
        if '__deepcopy__' not in method_names:
            yield Function(
                '__deepcopy__',
                [Signature(
                    [Parameter('self'), Parameter('memo', 'object', named=False)],
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


def make_attribute_rep(element: IDBElement) -> Attribute:
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
        if element.has_has_function:
            type_name += ' | None'
    doc = comment_to_docstring(element.comment)
    return Attribute(
        check_keyword(element.name),
        ATTR_TYPE_OVERRIDES.get(element.scoped_name, type_name),
        read_only=read_only,
        doc=doc,
        comment=get_comment(element.scoped_name),
    )


def make_signature_rep(
        wrapper: IDBFunctionWrapper,
        function: IDBFunction | None = None,
        *, ensure_self_param: bool = False) -> Signature:
    """Return a representation of the signature
    of a function wrapper known to interrogate.
    """
    if function is not None and function.is_constructor:
        return_type = 'None'
    elif function is not None and function.is_method and function.name in RETURN_SELF:
        return_type = 'Self'
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
        case [Parameter('args') as args]:
            args.name = '*' + args.name
        case [
            *_,
            Parameter('args') as args,
            Parameter('kwargs' | 'kwds') as kwargs,
        ]:
            args.name = '*' + args.name
            kwargs.name = '**' + kwargs.name
    return Signature(params, return_type)


def make_function_rep(function: IDBFunction) -> Function:
    """Return a representation of a function known to interrogate."""
    name = get_function_name(function)
    is_static_method = (
        function.is_method and not is_dunder(name)
        and not function.wrappers[0].parameters[0].is_this
    )
    signatures: list[Signature] = []
    sigs_by_doc = defaultdict[str, list[str]](list)
    param_overrides = PARAM_TYPE_OVERRIDES.get(function.scoped_name)
    return_overrides = RETURN_TYPE_OVERRIDES.get(function.scoped_name, {})
    if isinstance(return_overrides, str):
        return_overrides = {i: return_overrides for i in range(len(function.wrappers))}
    for i, wrapper in enumerate(function.wrappers):
        if not wrapper_is_exposed(wrapper):
            continue
        signature = make_signature_rep(
            wrapper, function,
            ensure_self_param=function.is_method and not is_static_method,
        )
        if sig_doc := comment_to_docstring(wrapper.comment):
            sigs_by_doc[sig_doc].append(f'`({signature.param_string})`')
        if param_overrides:
            for j, param in enumerate(signature.parameters):
                param_override = param_overrides.get((i, j))
                if param_override is not None:
                    param.type = param_override
        return_override = return_overrides.get(i)
        if return_override is None and not signature.return_type:
            return_override = DEFAULT_RETURNS.get(function.name)
        if return_override is not None:
            signature.return_type = return_override
        signatures.append(signature)
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
        decorators=('staticmethod',) if is_static_method else (),
        doc=doc,
        comment=get_comment(function.scoped_name),
    )


def make_type_reps(idb_type: IDBType) -> Iterator[StubRep]:
    if idb_type.is_enum:
        if idb_type.is_scoped_enum:
            yield make_scoped_enum_rep(idb_type)
        else:
            yield from make_enum_value_reps(idb_type)
        return
    if idb_type.is_typedef:
        class_ = make_typedef_rep(idb_type)
    else:
        class_ = make_class_rep(idb_type)
        if class_.name == 'BitMaskNative':
            return
    yield class_
    alias_name = make_alias_name(class_.name, capitalize=True)
    if alias_name != class_.name:
        yield Alias(alias_name, class_.name, of_local=True)


def make_make_seq_rep(make_seq: IDBMakeSeq) -> Function:
    """Return a representation of a MakeSeq known to interrogate."""
    element_getter = make_seq.element_getter
    return_type = get_type_name(element_getter.wrappers[0].return_type)
    signature = Signature([Parameter('self')], f'tuple[{return_type}, ...]')
    return Function(
        make_seq.seq_name,
        [signature],
        doc=comment_to_docstring(make_seq.comment),
        comment=get_comment(make_seq.scoped_name),
    )


def make_enum_value_reps(idb_type: IDBType) -> Iterator[Constant]:
    """Return variable representations for an enum type known to interrogate."""
    for enum_value in idb_type.enum_values:
        if enum_value.scoped_name in NOT_EXPOSED:
            continue
        value_name = enum_value.name
        yield Constant(value_name, enum_value.value)
        alias_name = make_alias_name(value_name, capitalize=True)
        if idb_type.name and alias_name != value_name:
            yield Constant(alias_name, enum_value.value)


def make_scoped_enum_rep(idb_type: IDBType) -> Class:
    """Return a representation of a scoped enum known to interrogate."""
    name = make_class_name(idb_type.name)
    values = {
        value.name: Attribute(value.name, 'int')
        for value in idb_type.enum_values
    }
    return Class(name, ['Enum'], values, is_final=idb_type.is_final)


def make_class_rep(idb_type: IDBType) -> Class:
    """Return a representation of a class known to interrogate."""
    name = make_class_name(idb_type.name)
    class_body: dict[str, StubRep] = {}
    bases = [
        get_type_name(derivation)
        for derivation in idb_type.derivations
        if type_is_exposed(derivation)
    ]
    if (type_vars := GENERIC.get(name)) is not None:
        bases.append(f'Generic[{type_vars}]')
    # Attributes
    class_body['DtoolClassDict'] = Attribute(
        'DtoolClassDict', 'ClassVar[dict[str, Any]]'
    )
    for elem in idb_type.elements:
        if element_is_exposed(elem) and elem.name not in NO_STUBS:
            attribute = make_attribute_rep(elem)
            class_body[attribute.name] = attribute
    if name.startswith('ParamValue_'):
        value = name[11:]
        if value in ('string', 'wstring'):
            value = 'str'
        class_body['value'] = Attribute('value', value)
    # Methods
    for method in get_type_methods(idb_type):
        if method.name in class_body:
            _logger.info(f'Discarding {method}; its name is already in use')
            continue
        class_body[method.name] = method
        if method.name not in NO_ALIAS:
            alias_name = make_alias_name(method.name)
            if alias_name != method.name:
                if (
                    method.comment == 'type: ignore[override]'
                    # It is unclear why Mypy takes issue with these two.
                    or (name, method.name) in (
                        ('Character', 'get_bundle'),
                        ('GeomVertexRewriter', 'set_column'),
                    )
                ):
                    comment = 'type: ignore[assignment]'
                else:
                    comment = ''
                class_body[alias_name] = Alias(
                    alias_name,
                    method.name,
                    of_local=True,
                    comment=comment,
                )
    # Nested types
    for nested_type in idb_type.nested_types:
        if not type_is_exposed(nested_type):
            continue
        type_reps = make_type_reps(nested_type)
        class_body |= {rep.name: rep for rep in type_reps}
    return Class(
        name, bases, class_body,
        is_final=idb_type.is_final,
        conditional=CONDITIONALS.get(idb_type.scoped_name, ''),
        doc=comment_to_docstring(idb_type.comment),
        comment=get_comment(idb_type.scoped_name),
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
        nested_by_mod_by_lib[mod_name][lib_name].append(function_rep)
        if function_rep.name not in NO_ALIAS:
            alias_name = make_alias_name(function_rep.name)
            if alias_name != function_rep.name:
                nested_by_mod_by_lib[mod_name][lib_name].append(
                    Alias(alias_name, function_rep.name, of_local=True)
                )

    # Gather global types
    for idb_type in get_global_types():
        if idb_type.is_nested:
            continue
        mod_name = idb_type.module_name
        lib_name = '_' + idb_type.library_name.removeprefix('libp3')
        nested_by_mod_by_lib[mod_name][lib_name] += make_type_reps(idb_type)

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
        TypeAlias(name, definition)
        for name, definition in TYPE_ALIASES.items()
    ]
    return Module('_typing', {'typing': aliases}, namespace=('panda3d',))
