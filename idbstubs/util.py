import ast
import itertools
import logging
from collections.abc import Iterable, Iterator, Mapping, Set
from typing import Final, TypeVar, cast

T = TypeVar('T')
KT = TypeVar('KT')
VT = TypeVar('VT', covariant=True)

_logger: Final = logging.getLogger(__name__)

flatten = itertools.chain.from_iterable


def is_dunder(s: str, /) -> bool:
    """Return whether a given string starts and ends with "__"."""
    return s.startswith('__') and s.endswith('__')


def is_sunder(s: str, /) -> bool:
    """Return whether a given string starts and ends with exactly one underscore."""
    return s.startswith('_') and s.endswith('_') and not is_dunder(s)


def indent_lines(lines: Iterable[str], *, level: int = 4) -> Iterator[str]:
    """Yield each string from the iterable with four spaces prepended.
    Empty strings are yielded unchanged. The number of spaces prepended
    can be changed by passing a keyword-only `level` argument.
    """
    indentation = ' ' * level
    for line in lines:
        yield (indentation + line) if line else ''


def docstring_lines(doc: str) -> Iterator[str]:
    """Yield the lines of a docstring (including quotes)
    with the given contents (excluding quotes).
    """
    if not doc:
        return
    elif '\n' in doc:
        yield from f'"""{doc}\n"""'.splitlines()
    else:
        yield f'"""{doc}"""'


def names_within(s: str, /) -> Iterator[str]:
    """Yield the identifiers referenced by an expression."""
    if s.isalnum():
        yield s
        return
    try:
        parsed = ast.parse(s)
    except SyntaxError:
        _logger.exception(f'Could not parse {s!r}')
        return
    for node in ast.walk(parsed):
        if isinstance(node, ast.Name):
            yield node.id


def unpack_union(s: str, /) -> list[str]:
    """Return a list of the individual types within
    a string representation of a type union.
    """
    if '|' not in s:
        return [s]
    try:
        parsed = ast.parse(s)
    except SyntaxError:
        _logger.exception(f'Could not parse {s!r}')
        return []

    def iter_ast_union(u: ast.BinOp, /) -> Iterator[str]:
        for expr in u.left, u.right:
            match expr:
                case ast.BinOp(op=ast.BitOr()):
                    yield from iter_ast_union(expr)
                case _:
                    yield ast.unparse(expr)

    type_list: list[str] = []
    match parsed.body:
        case [ast.Expr(value=ast.BinOp(op=ast.BitOr()) as op)]:
            type_list += iter_ast_union(op)
        case _:
            type_list.append(s)

    return type_list


class TrackingSet(Set[T]):
    __slots__ = '_mapping'
    _mapping: dict[T, bool]

    def __init__(self, iterable: Iterable[T]) -> None:
        self._mapping = dict.fromkeys(iterable, False)

    def __len__(self) -> int:
        return len(self._mapping)

    def __contains__(self, item: object) -> bool:
        result = item in self._mapping
        if result:
            self._mapping[cast(T, item)] = True
        return result

    def __iter__(self) -> Iterator[T]:
        return iter(self._mapping)

    def used_items(self) -> set[T]:
        return {k for k, v in self._mapping.items() if v}

    def unused_items(self) -> set[T]:
        return {k for k, v in self._mapping.items() if not v}


class TrackingMap(Mapping[KT, VT]):
    __slots__ = '_mapping'
    _mapping: dict[KT, tuple[VT, bool]]

    def __init__(self, mapping: Mapping[KT, VT]) -> None:
        self._mapping = {k: (v, False) for k, v in mapping.items()}

    def __len__(self) -> int:
        return len(self._mapping)

    def __getitem__(self, key: KT) -> VT:
        value, used = self._mapping[key]
        if not used:
            self._mapping[key] = value, True
        return value

    def __iter__(self) -> Iterator[KT]:
        return iter(self._mapping)

    def used_keys(self) -> set[KT]:
        return {k for k, (_, used) in self._mapping.items() if used}

    def unused_keys(self) -> set[KT]:
        return {k for k, (_, used) in self._mapping.items() if not used}
