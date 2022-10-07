from collections import defaultdict
from collections.abc import Iterator, Mapping, Sequence
from itertools import chain
from pathlib import Path
from sys import stdlib_module_names
from typing import Any, Protocol

from attrs import Factory, define, evolve, field

from .util import (
    docstring_lines, flatten, indent_lines, is_dunder, names_within
)


class StubRep(Protocol):
    @property
    def name(self) -> str: ...
    def sort(self) -> tuple[int, int]: ...
    def get_dependencies(self) -> Iterator[str]: ...
    def definition(self) -> Iterator[str]: ...


@define
class TypeVariable:
    name: str
    bounds: Sequence[str] = field(default=(), converter=tuple)
    variance: str = ''

    def __str__(self) -> str:
        parameters = [repr(self.name)]
        if self.bounds:
            if len(self.bounds) == 1:
                parameters.append(f'bound={self.bounds[0]}')
            else:
                parameters += self.bounds
        if self.variance and self.variance != 'invariant':
            parameters.append(f'{self.variance}=True')
        return f"{self.name} = TypeVar({', '.join(parameters)})"

    def sort(self) -> tuple[int, int]:
        return 0, 0

    def get_dependencies(self) -> Iterator[str]:
        yield 'TypeVar'
        yield from flatten(names_within(i) for i in self.bounds)

    def definition(self) -> Iterator[str]:
        yield str(self)


@define
class Alias:
    name: str
    alias_of: str
    is_type_alias: bool = field(default=False, kw_only=True)
    of_local: bool = field(default=False, kw_only=True)
    namespace: Sequence[str] = field(
        default=(), converter=tuple, kw_only=True, eq=False)
    comment: str = field(default='', kw_only=True, eq=False)

    @property
    def scoped_name(self) -> str:
        return '.'.join((*self.namespace, self.name))

    def __str__(self) -> str:
        if self.is_type_alias:
            return f'{self.name}: TypeAlias = {self.alias_of}'
        else:
            return f'{self.name} = {self.alias_of}'

    def sort(self) -> tuple[int, int]:
        if self.of_local:
            return 2, 1
        if self.is_type_alias:
            return 0, 0
        return 0, 2

    def get_dependencies(self) -> Iterator[str]:
        """Yield the names of types referenced by the alias."""
        return chain(
            () if self.of_local else names_within(self.alias_of),
            ('TypeAlias',) if self.is_type_alias else (),
        )

    def definition(self) -> Iterator[str]:
        if self.comment:
            yield f'{self}  # {self.comment}'
        else:
            yield str(self)


@define
class Parameter:
    name: str
    type: str = ''
    is_optional: bool = field(default=False, kw_only=True)
    named: bool = field(default=True, kw_only=True)
    is_self: bool = field(default=False, kw_only=True)

    @classmethod
    def as_self(cls) -> 'Parameter':
        """Construct a representation of a `self` parameter."""
        return cls('self', is_self=True)

    def __str__(self) -> str:
        s = self.name
        if not self.named:
            s = '__' + s.lstrip('_')
        if self.type:
            s += ': ' + self.type
        if self.is_optional:
            s += ' = ...' if self.type else '=...'
        return s

    def get_dependencies(self) -> Iterator[str]:
        return names_within(self.type)


@define
class Signature:
    parameters: Sequence[Parameter] = field(converter=tuple)
    return_type: str

    def __str__(self) -> str:
        param_string = ', '.join(map(str, self.parameters))
        if self.return_type:
            return f'({param_string}) -> {self.return_type}'
        else:
            return f'({param_string})'

    def copy(self, **changes: Any) -> 'Signature':
        if 'parameters' not in changes:
            changes['parameters'] = tuple((evolve(p) for p in self.parameters))
        return evolve(self, **changes)

    def min_arity(self) -> int:
        """Return the minimum number of arguments the signature will accept."""
        return sum(not p.is_optional for p in self.parameters)

    def max_arity(self) -> int:
        """Return the maximum number of arguments the signature will accept."""
        return len(self.parameters)

    def get_arity(self) -> tuple[int, int]:
        """Return the minimum and maximum number
        of arguments the signature will accept.
        """
        min_arity = sum(not p.is_optional for p in self.parameters)
        max_arity = len(self.parameters)
        return min_arity, max_arity

    def get_dependencies(self) -> Iterator[str]:
        return chain(
            names_within(self.return_type),
            flatten(p.get_dependencies() for p in self.parameters),
        )


@define
class Function:
    name: str
    signatures: Sequence[Signature] = field(converter=tuple)
    is_method: bool = field(default=False, kw_only=True)
    is_static: bool = field(default=False, kw_only=True)
    namespace: Sequence[str] = field(
        default=(), converter=tuple, kw_only=True, eq=False)
    doc: str = field(default='', kw_only=True, eq=False)
    comment: str = field(default='', kw_only=True, eq=False)

    @property
    def scoped_name(self) -> str:
        return '.'.join((*self.namespace, self.name))

    def decorators(self) -> list[str]:
        """Return a list of the names of the decorators that should be
        applied to this function's signatures.
        """
        decorators: list[str] = []
        if len(self.signatures) > 1:
            decorators.append('overload')
        if self.is_method and self.is_static:
            decorators.append('staticmethod')
        return decorators

    def __str__(self) -> str:
        kind = 'Method' if self.is_method else 'Function'
        return f'{kind} {self.scoped_name!r}'

    def sort(self) -> tuple[int, int]:
        if is_dunder(self.name):
            return 1, 0
        return 1, 1

    def get_dependencies(self) -> Iterator[str]:
        return chain(
            flatten(s.get_dependencies() for s in self.signatures),
            self.decorators(),
        )

    def definition(self) -> Iterator[str]:
        decorators = self.decorators()
        doc_printed = False
        comment_printed = False
        for signature in self.signatures:
            for decorator in decorators:
                if self.comment and not comment_printed:
                    yield f'@{decorator}  # {self.comment}'
                    comment_printed = True
                else:
                    yield '@' + decorator
            sig_def = f'def {self.name}{signature}:'
            if doc_printed or not self.doc:
                sig_def += ' ...'
            if self.comment and not comment_printed:
                sig_def += f'  # {self.comment}'
                comment_printed = True
            yield sig_def
            if not doc_printed:
                yield from indent_lines(docstring_lines(self.doc))
                doc_printed = True


@define
class Attribute:
    name: str
    type: str
    read_only: bool = field(default=False, kw_only=True)
    namespace: Sequence[str] = field(
        default=(), converter=tuple, kw_only=True, eq=False)
    doc: str = field(default='', kw_only=True, eq=False)
    comment: str = field(default='', kw_only=True, eq=False)

    @property
    def scoped_name(self) -> str:
        return '.'.join((*self.namespace, self.name))

    def __str__(self) -> str:
        return f'Element {self.name!r} ({self.type})'

    def sort(self) -> tuple[int, int]:
        return (0, 4) if self.read_only else (0, 3)

    def get_dependencies(self) -> Iterator[str]:
        return names_within(self.type)

    def definition(self) -> Iterator[str]:
        if self.read_only:
            yield '@property'
            if self.type:
                function_def = f'def {self.name}(self) -> {self.type}:'
            else:
                function_def = f'def {self.name}(self):'
            if not self.doc:
                function_def += ' ...'
            if self.comment:
                function_def += '  # ' + self.comment
            yield function_def
            doc_indent_level = 4
        else:
            if self.type:
                attribute_def = f'{self.name}: {self.type}'
            else:
                attribute_def = f'{self.name} = ...'
            if self.comment:
                attribute_def += '  # ' + self.comment
            yield attribute_def
            doc_indent_level = 0
        yield from indent_lines(docstring_lines(self.doc),
                                level=doc_indent_level)


@define
class Class:
    name: str
    derivations: Sequence[str] = field(default=(), converter=tuple)
    body: Mapping[str, StubRep] = Factory(dict)
    is_final: bool = field(default=False, kw_only=True)
    namespace: Sequence[str] = field(
        default=(), converter=tuple, kw_only=True, eq=False)
    conditional: str = field(default='', kw_only=True, eq=False)
    doc: str = field(default='', kw_only=True, eq=False)
    comment: str = field(default='', kw_only=True, eq=False)

    @property
    def scoped_name(self) -> str:
        return '.'.join((*self.namespace, self.name))

    def __str__(self) -> str:
        return f'Class {self.scoped_name!r}'

    def is_empty(self) -> bool:
        """Return whether the class has any body (including a docstring)."""
        return not (self.doc or self.body)

    def sort(self) -> tuple[int, int]:
        return 0, 1

    def get_dependencies(self) -> Iterator[str]:
        return chain(
            names_within(self.conditional),
            ('final',) if self.is_final else (),
            flatten(names_within(d) for d in self.derivations),
            flatten(i.get_dependencies() for i in self.body.values()),
        )

    def definition(self) -> Iterator[str]:
        if self.conditional:
            yield f'if {self.conditional}:'
            yield from indent_lines(evolve(self, conditional='').definition())
            return
        if self.is_final:
            yield '@final'
        declaration = f'class {self.name}'
        if self.derivations:
            declaration += f"({', '.join(self.derivations)})"
        declaration += ':'
        if self.is_empty():
            if self.comment:
                yield f'{declaration} ...  # {self.comment}'
            else:
                yield declaration + ' ...'
            return
        if self.comment:
            declaration += f'  # {self.comment}'
        yield declaration
        yield from indent_lines(docstring_lines(self.doc))
        sorted_nested = sorted(self.body.values(), key=lambda i: i.sort())
        prev_was_class = False
        for item in sorted_nested:
            is_class = isinstance(item, Class) and not item.is_empty()
            if is_class or prev_was_class:
                yield ''
            prev_was_class = is_class
            yield from indent_lines(item.definition())


@define
class File:
    name: str
    nested: list[StubRep] = field(factory=list, converter=list)
    namespace: Sequence[str] = field(default=(), converter=tuple, kw_only=True)
    imports: defaultdict[str, list[str]] = field(
        factory=lambda: defaultdict(list), kw_only=True)

    @property
    def scoped_name(self) -> str:
        return '.'.join((*self.namespace, self.name))

    def this_namespace(self) -> tuple[str, ...]:
        return *self.namespace, self.name

    def stub_path(self) -> Path:
        parts = self.this_namespace()
        return Path(parts[0] + '-stubs', *parts[1:])

    def __str__(self) -> str:
        return f'Stub File {self.scoped_name!r}'

    def sort_items(self) -> None:
        self.nested.sort(key=lambda x: x.sort())

    def import_lines(self) -> Iterator[str]:
        this_package = self.namespace[0] if self.namespace else None
        extended_stdlib = stdlib_module_names | {'_typeshed', 'typing_extensions'}

        def grouping_function(module: str) -> int:
            if not module or module.split('.')[0] in extended_stdlib:
                return 0
            elif this_package and module.startswith(this_package):
                return 2
            else:
                return 1

        keyed_modules = sorted((grouping_function(m), m) for m in self.imports)
        prev_key = None
        for key, module in keyed_modules:
            if prev_key not in (None, key):
                yield ''
            imported_names = sorted(
                self.imports[module], key=lambda s: s[0:1] + s[1:].lower()
            )
            if not module:
                for name in imported_names:
                    yield f'import {name}'
                continue
            if len(module) + sum(len(n)+2 for n in imported_names) < 117:
                yield f"from {module} import {', '.join(imported_names)}"
            else:
                yield f'from {module} import ('
                for name in imported_names:
                    yield f'    {name},'
                yield ')'
            prev_key = key

    def lines(self) -> Iterator[str]:
        yield from self.import_lines()
        if self.imports and self.nested:
            yield ''
        prev_was_class = False
        first_item = True
        for item in self.nested:
            is_class = isinstance(item, Class) and not item.is_empty()
            if (is_class or prev_was_class) and not first_item:
                yield ''
            prev_was_class = is_class
            yield from item.definition()
            if first_item:
                first_item = False

    def get_dependencies(self) -> Iterator[str]:
        return flatten(i.get_dependencies() for i in self.nested)


@define
class Module:
    name: str
    nested: dict[str, Sequence[StubRep]] = Factory(dict)
    namespace: Sequence[str] = field(default=(), converter=tuple, kw_only=True)

    @property
    def scoped_name(self) -> str:
        return '.'.join((*self.namespace, self.name))

    def __str__(self) -> str:
        return f'Module {self.scoped_name!r}'

    def __iter__(self) -> Iterator[File]:
        if len(self.nested) == 1:
            nested = tuple(self.nested.values())[0]
            # Convert to a list because the type checker doesn't know about
            # attrs field converters.
            nested = list(nested)
            yield File(self.name, nested, namespace=self.namespace)
            return
        this_namespace = (*self.namespace, self.name)
        for file_name, nested in self.nested.items():
            # See previous comment.
            nested = list(nested)
            yield File(file_name, nested, namespace=this_namespace)


@define
class Package:
    name: str
    modules: list[Module] = Factory(list)

    def __str__(self) -> str:
        return f'Package {self.name!r}'

    def __iter__(self) -> Iterator[Module]:
        return iter(self.modules)

    def add_module(self, module: Module) -> None:
        self.modules.append(module)
