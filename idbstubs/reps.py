from __future__ import annotations

import builtins
import sys
from collections import defaultdict
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from pathlib import Path
from typing import Any, Protocol

from attrs import Factory, define, evolve, field

from . import typecmp as tc
from .util import (
    docstring_lines,
    flatten,
    get_indent,
    is_dunder,
    names_within,
    with_comment,
)


def _convert_type(t: tc.Type | str) -> tc.Type:
    if isinstance(t, str):
        return tc.BasicType(t)
    return t


class StubRep(Protocol):
    name: str
    def get_dependencies(self) -> Iterator[str]: ...
    def definition(self, *, indent_level: int = 0) -> Iterator[str]: ...


@define
class TypeVariable(StubRep):
    name: str
    parameters: Iterable[str] = field(default=(), converter=tuple)

    def __str__(self) -> str:
        parameters = [repr(self.name), *self.parameters]
        return f"TypeVar({', '.join(parameters)})"

    def get_dependencies(self) -> Iterator[str]:
        yield from names_within(str(self))

    def definition(self, *, indent_level: int = 0) -> Iterator[str]:
        yield f'{get_indent(indent_level)}{self.name} = {self}'


@define
class TypeAlias(StubRep):
    name: str
    alias_of: str

    def __str__(self) -> str:
        return f'{self.name}: TypeAlias = {self.alias_of}'

    def get_dependencies(self) -> Iterator[str]:
        yield 'TypeAlias'
        yield from names_within(self.alias_of)

    def definition(self, *, indent_level: int = 0) -> Iterator[str]:
        yield get_indent(indent_level) + str(self)


@define
class Alias(StubRep):
    name: str
    alias_of: str
    of_local: bool = field(default=False, kw_only=True)
    comment: str = field(default='', kw_only=True, eq=False)

    def __str__(self) -> str:
        return f'{self.name} = {self.alias_of}'

    def get_dependencies(self) -> Iterator[str]:
        """Yield the names of types referenced by the alias."""
        if not self.of_local:
            yield from names_within(self.alias_of)

    def definition(self, *, indent_level: int = 0) -> Iterator[str]:
        line = get_indent(indent_level) + str(self)
        yield with_comment(line, self.comment)


@define
class Constant(StubRep):
    name: str
    value: int | float | complex | str | bytes | None

    def __str__(self) -> str:
        return f'{self.name}: Final = {self.value!r}'

    def get_dependencies(self) -> Iterator[str]:
        yield 'Final'

    def definition(self, *, indent_level: int = 0) -> Iterator[str]:
        yield get_indent(indent_level) + str(self)


@define
class Parameter:
    name: str
    type: tc.Type = field(default=tc.MissingType(), converter=_convert_type)
    is_optional: bool = field(default=False, kw_only=True)
    named: bool = field(default=True, kw_only=True)

    def __str__(self) -> str:
        s = self.name
        if not self.named:
            s = '__' + s.lstrip('_')
        if self.type:
            s += f': {self.type}'
        if self.is_optional:
            s += ' = ...' if self.type else '=...'
        return s

    def get_dependencies(self) -> Iterator[str]:
        return names_within(str(self.type))


@define
class Signature:
    parameters: Sequence[Parameter] = field(converter=tuple)
    return_type: tc.Type = field(converter=_convert_type)
    doc: str = field(default='', kw_only=True, eq=False)

    @property
    def param_string(self) -> str:
        return ', '.join(str(p) for p in self.parameters)

    def __str__(self) -> str:
        if self.return_type:
            return f'({self.param_string}) -> {self.return_type}'
        else:
            return f'({self.param_string})'

    def copy(self, **changes: Any) -> Signature:
        if 'parameters' not in changes:
            changes['parameters'] = tuple((evolve(p) for p in self.parameters))
        return evolve(self, **changes)

    def has_arity_overlap(self, other: Signature) -> bool:
        return not (
            self.min_arity() > other.max_arity()
            or self.max_arity() < other.min_arity()
        )

    def min_arity(self) -> int:
        """Return the minimum number of arguments the signature will accept."""
        return sum(not p.is_optional for p in self.parameters)

    def max_arity(self) -> int:
        """Return the maximum number of arguments the signature will accept."""
        return len(self.parameters)

    def get_dependencies(self) -> Iterator[str]:
        yield from names_within(str(self.return_type))
        for parameter in self.parameters:
            yield from parameter.get_dependencies()

    def definition(
            self,
            *, prefix: str = '',
            indent_level: int = 0,
            decorators: Iterable[str] = ()) -> Iterator[str]:
        postfix = '' if self.doc else ' ...'
        indent = get_indent(indent_level)
        next_indent = get_indent(indent_level + 1)
        for decorator in decorators:
            yield f'{indent}@{decorator}'
        sig_def = f'{indent}{prefix}{self}:{postfix}'
        if len(sig_def) <= 130:
            yield sig_def
        else:
            yield f'{indent}{prefix}('
            for param in self.parameters:
                yield f'{next_indent}{param},'
            yield f'{indent}) -> {self.return_type}:{postfix}'
        yield from docstring_lines(self.doc, indent_level=indent_level + 1)


@define
class Function(StubRep):
    name: str
    signatures: Sequence[Signature] = field(converter=tuple)
    decorators: Sequence[str] = field(default=(), kw_only=True, converter=tuple)
    comment: str = field(default='', kw_only=True, eq=False)

    def __str__(self) -> str:
        return f'Function {self.name!r}'

    def get_dependencies(self) -> Iterator[str]:
        if len(self.signatures) > 1:
            yield 'overload'
        yield from self.decorators
        for signature in self.signatures:
            yield from signature.get_dependencies()

    def definition(self, *, indent_level: int = 0) -> Iterator[str]:
        decorators = self.decorators
        if len(self.signatures) > 1:
            decorators = ('overload', *decorators)
        comment_needed = bool(self.comment)
        for signature in self.signatures:
            definition_lines = signature.definition(
                prefix=f'def {self.name}',
                indent_level=indent_level,
                decorators=decorators,
            )
            if comment_needed:
                first_line = next(definition_lines)
                yield with_comment(first_line, self.comment)
                comment_needed = False
            yield from definition_lines


@define
class Attribute(StubRep):
    name: str
    type: tc.Type = field(converter=_convert_type)
    read_only: bool = field(default=False, kw_only=True)
    doc: str = field(default='', kw_only=True, eq=False)
    comment: str = field(default='', kw_only=True, eq=False)

    def __str__(self) -> str:
        return f'Attribute {self.name!r} ({self.type})'

    def get_dependencies(self) -> Iterator[str]:
        return names_within(str(self.type))

    def definition(self, *, indent_level: int = 0) -> Iterator[str]:
        indent = get_indent(indent_level)
        if self.read_only:
            yield indent + '@property'
            if self.type:
                function_def = f'{indent}def {self.name}(self) -> {self.type}:'
            else:
                function_def = f'{indent}def {self.name}(self):'
            if not self.doc:
                function_def += ' ...'
            yield with_comment(function_def, self.comment)
            doc_indent_level = indent_level + 1
        else:
            if self.type:
                attribute_def = f'{indent}{self.name}: {self.type}'
            else:
                attribute_def = f'{indent}{self.name} = ...'
            yield with_comment(attribute_def, self.comment)
            doc_indent_level = indent_level
        yield from docstring_lines(self.doc, indent_level=doc_indent_level)


@define
class Class(StubRep):
    name: str
    bases: Sequence[str] = field(default=(), converter=tuple)
    body: Mapping[str, StubRep] = Factory(dict)
    is_final: bool = field(default=False, kw_only=True)
    conditional: str = field(default='', kw_only=True, eq=False)
    doc: str = field(default='', kw_only=True, eq=False)
    comment: str = field(default='', kw_only=True, eq=False)

    def __str__(self) -> str:
        return f'Class {self.name!r}'

    def get_base_dependencies(self) -> Iterator[str]:
        for base in self.bases:
            yield from names_within(base)

    def get_dependencies(self) -> Iterator[str]:
        yield from names_within(self.conditional)
        if self.is_final:
            yield 'final'
        yield from self.get_base_dependencies()
        for item in self.body.values():
            yield from item.get_dependencies()

    def definition(self, *, indent_level: int = 0) -> Iterator[str]:
        if self.conditional:
            yield f'{get_indent(indent_level)}if {self.conditional}:'
            indent_level += 1
        indent = get_indent(indent_level)
        if self.is_final:
            yield indent + '@final'
        declaration = f'{indent}class {self.name}'
        if self.bases:
            declaration += f"({', '.join(self.bases)})"
        declaration += ':'
        if not (self.doc or self.body):
            declaration += ' ...'
            yield with_comment(declaration, self.comment)
            return
        yield with_comment(declaration, self.comment)
        yield from docstring_lines(self.doc, indent_level=indent_level+1)
        sorted_nested = sorted(self.body.values(), key=_sort_rep)
        if self.doc and sorted_nested:
            yield ''
        yield from definitions(sorted_nested, indent_level=indent_level+1)


@define
class File:
    path: Path = field(converter=Path)
    nested: list[StubRep] = field(factory=list, converter=list)
    imports: defaultdict[str, list[str]] = field(
        factory=lambda: defaultdict(list), kw_only=True)

    def stub_path(self) -> Path:
        parts = self.path.parts
        return Path(parts[0] + '-stubs', *parts[1:])

    def __str__(self) -> str:
        return f'Stub File {self.path!r}'

    def sort_items(self) -> None:
        seen = set(dir(builtins))
        seen.update(flatten(self.imports.values()))
        queued_subclasses = defaultdict[str, list[Class]](list)
        sorted_nested: list[StubRep] = []

        for item in sorted(self.nested, key=_sort_rep):
            if isinstance(item, Class):
                queued = False
                for dep in item.get_base_dependencies():
                    if dep not in seen:
                        queued_subclasses[dep].append(item)
                        queued = True
                if queued:
                    continue
            seen.add(item.name)
            sorted_nested.append(item)

            new_names = [item.name]
            for name in new_names:
                for subclass in queued_subclasses[name]:
                    for dep in subclass.get_base_dependencies():
                        if dep not in seen:
                            break
                    else:
                        seen.add(subclass.name)
                        sorted_nested.append(subclass)
                        new_names.append(subclass.name)
        self.nested = sorted_nested

    def import_lines(self) -> Iterator[str]:
        this_package = self.path.parts[0] if self.path.parts else None
        extended_stdlib = sys.stdlib_module_names | {'_typeshed', 'typing_extensions'}

        stdlib_modules, other_modules, local_modules = set[str](), set[str](), set[str]()
        for module in self.imports:
            if not module or module.split('.')[0] in extended_stdlib:
                stdlib_modules.add(module)
            elif this_package and module.startswith(this_package):
                local_modules.add(module)
            else:
                other_modules.add(module)

        def import_sort_key(name: str) -> tuple[int, str]:
            if name.isupper():
                return 0, name.casefold()
            elif name[0:1].isupper():
                return 1, name.casefold()
            else:
                return 2, name.casefold()

        need_blank_line = False
        for modules in (stdlib_modules, other_modules, local_modules):
            if modules:
                if need_blank_line:
                    yield ''
                need_blank_line = True
            for module in sorted(modules):
                imported_names = sorted(self.imports[module], key=import_sort_key)
                if not module:
                    for name in imported_names:
                        yield f'import {name}'
                    continue
                single_line = f"from {module} import {', '.join(imported_names)}"
                if len(single_line) <= 130:
                    yield single_line
                else:
                    yield f'from {module} import ('
                    for name in imported_names:
                        yield f'    {name},'
                    yield ')'

    def lines(self) -> Iterator[str]:
        yield from self.import_lines()
        if self.imports and self.nested:
            yield ''
        yield from definitions(self.nested)

    def get_dependencies(self) -> Iterator[str]:
        for item in self.nested:
            yield from item.get_dependencies()


_rep_matchers: list[Callable[[StubRep], bool]] = [
    lambda r: isinstance(r, TypeVariable),
    lambda r: isinstance(r, TypeAlias),
    lambda r: isinstance(r, Constant),
    lambda r: isinstance(r, Class),
    lambda r: isinstance(r, Alias) and not r.of_local,
    lambda r: isinstance(r, Attribute) and not r.read_only,
    lambda r: isinstance(r, Attribute),
    lambda r: isinstance(r, Function) and is_dunder(r.name),
    lambda r: isinstance(r, Function),
    lambda r: isinstance(r, Alias),
]


def _sort_rep(rep: StubRep) -> int:
    for i, f in enumerate(_rep_matchers):
        if f(rep):
            return i
    return len(_rep_matchers)


def need_space_between(first: StubRep, second: StubRep) -> bool:
    TypingConstruct = TypeVariable | TypeAlias
    if isinstance(first, Class) or isinstance(second, Class):
        return True
    elif isinstance(first, TypingConstruct) != isinstance(second, TypingConstruct):
        return True
    else:
        return False


def definitions(reps: Iterable[StubRep], *, indent_level: int = 0) -> Iterator[str]:
    previous: StubRep | None = None
    for item in reps:
        if previous is not None and need_space_between(previous, item):
            yield ''
        yield from item.definition(indent_level=indent_level)
        previous = item
