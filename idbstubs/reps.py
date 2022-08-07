from collections import defaultdict
from collections.abc import Iterable, Iterator, Sequence
from itertools import chain
from pathlib import Path
from typing import Any, Protocol

from attrs import Factory, define, evolve, field

from .util import flatten, is_dunder, names_within


class StubRep(Protocol):
    name: str
    def sort(self) -> tuple[int, int]: ...
    def get_dependencies(self) -> Iterator[str]: ...
    def definition(self) -> Iterator[str]: ...


@define
class TypeVariable:
    name: str
    bounds: Sequence[str] = field(default=(), converter=tuple)

    def __str__(self) -> str:
        if not self.bounds:
            definition = f'TypeVar({self.name!r})'
        elif len(self.bounds) == 1:
            definition = f'TypeVar({self.name!r}, bound={self.bounds[0]})'
        else:
            constraints = ', '.join(self.bounds)
            definition = f'TypeVar({self.name!r}, {constraints})'
        return f'{self.name} = {definition}'

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
            s += ' = ...'
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

    @property
    def is_static(self) -> bool:
        return not (self.parameters and self.parameters[0].is_self)

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
    namespace: Sequence[str] = field(default=(), converter=tuple, kw_only=True)
    doc: str = field(default='', kw_only=True)

    @property
    def scoped_name(self) -> str:
        return '.'.join((*self.namespace, self.name))

    @property
    def is_overloaded(self) -> bool:
        """Whether the function should be decorated with @typing.overload."""
        return len(self.signatures) > 1

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
            ('overload',) if self.is_overloaded else (),
        )

    def definition(self) -> Iterator[str]:
        is_method = self.is_method
        is_overloaded = self.is_overloaded
        doc_printed = False
        for signature in self.signatures:
            if is_overloaded:
                yield '@overload'
            if is_method and signature.is_static:
                yield '@staticmethod'
            if self.doc and not doc_printed:
                yield f'def {self.name}{signature}:'
                if '\n' in self.doc:
                    for line in f'"""{self.doc}\n"""'.splitlines():
                        yield '    ' + line
                else:
                    yield f'    """{self.doc}"""'
                yield '    ...'  # This isn't really necessary
                doc_printed = True
            else:
                yield f'def {self.name}{signature}: ...'


@define
class Element:
    name: str
    type: str
    read_only: bool = field(default=False, kw_only=True)
    namespace: Sequence[str] = field(default=(), converter=tuple, kw_only=True)
    doc: str = field(default='', kw_only=True)

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
            if self.doc:
                yield function_def
                if '\n' in self.doc:
                    for line in f'"""{self.doc}\n"""'.splitlines():
                        yield '    ' + line
                else:
                    yield f'    """{self.doc}"""'
                yield '    ...'  # This isn't really necessary
            else:
                yield function_def + ' ...'
        elif self.type:
            yield f'{self.name}: {self.type}'
        else:
            yield f'{self.name} = ...'
        # if self.doc:
        #     one_line_doc = self.doc.strip('"\n').replace('\n', ' ')
        #     yield f'{definition}  # {one_line_doc}'


@define
class Class:
    name: str
    derivations: Sequence[str] = field(default=(), converter=tuple)
    nested: Sequence[StubRep] = Factory(list)
    is_final: bool = field(default=False, kw_only=True)
    namespace: Sequence[str] = field(default=(), converter=tuple, kw_only=True)
    doc: str = field(default='', kw_only=True)

    @property
    def scoped_name(self) -> str:
        return '.'.join((*self.namespace, self.name))

    def __str__(self) -> str:
        return f'Class {self.scoped_name!r}'

    def sort(self) -> tuple[int, int]:
        return 0, 1

    def get_dependencies(self) -> Iterator[str]:
        return chain(
            ('final',) if self.is_final else (),
            flatten(names_within(d) for d in self.derivations),
            flatten(i.get_dependencies() for i in self.nested),
        )

    def definition(self) -> Iterator[str]:
        if self.is_final:
            yield '@final'
        declaration = f'class {self.name}'
        if self.derivations:
            declaration += f"({', '.join(self.derivations)})"
        declaration += ':'
        if not (self.nested or self.doc):
            yield declaration + ' ...'
            return
        yield declaration
        if self.doc:
            if '\n' in self.doc:
                for line in f'"""{self.doc}\n"""'.splitlines():
                    yield '    ' + line
            else:
                yield f'    """{self.doc}"""'
        sorted_nested = sorted(self.nested, key=lambda i: i.sort())
        for line in flatten(i.definition() for i in sorted_nested):
            yield '    ' + line


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
        if self.namespace:
            modules = sorted(
                self.imports,
                key=lambda m: (m.startswith(self.namespace[0]), m)
            )
        else:
            modules = sorted(self.imports)
        for module in modules:
            imported_names = sorted(self.imports[module])
            if len(module) + sum(len(n)+2 for n in imported_names) < 115:
                yield f"from {module} import {', '.join(imported_names)}"
            else:
                yield f'from {module} import ('
                for name in imported_names:
                    yield f'    {name},'
                yield ')'

    def lines(self) -> Iterator[str]:
        yield from self.import_lines()
        if self.imports and self.nested:
            yield ''
        prev_was_class = False
        first_item = True
        for item in self.nested:
            is_class = isinstance(item, Class)
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
    modules: Iterable[Module] = field(default=(), converter=tuple)

    def __str__(self) -> str:
        return f'Package {self.name!r}'

    def __iter__(self) -> Iterator[Module]:
        return iter(self.modules)
