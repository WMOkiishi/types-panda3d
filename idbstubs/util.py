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


def get_indent(level: int = 1, tab: str = '    ') -> str:
    return tab * level


def with_comment(line: str, comment: str) -> str:
    """Return `line` with `comment` appended as a comment.
    If `comment` is empty, return `line` unchanged.
    """
    if comment:
        return f'{line}  # {comment}'
    else:
        return line


def docstring_lines(doc: str, *, indent_level: int = 0) -> Iterator[str]:
    """Yield the lines of a docstring (including quotes)
    with the given contents (excluding quotes).
    """
    indent = get_indent(indent_level)
    if not doc:
        return
    elif '\n' in doc:
        for line in f'"""{doc}\n"""'.splitlines():
            if line:
                line = indent + line
            yield line
    else:
        yield f'{indent}"""{doc}"""'


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


def unpack_union(s: str, /) -> Iterator[str]:
    """Yield the individual types within
    a string representation of a type union.
    """
    if '|' not in s:
        yield s
        return
    try:
        parsed = ast.parse(s, mode='eval')
    except SyntaxError:
        _logger.exception(f'Could not parse {s!r}')
        return
    stack = [parsed.body]
    for expr in stack:
        match expr:
            case ast.BinOp(op=ast.BitOr()):
                stack += expr.left, expr.right
            case _:
                yield ast.unparse(expr)


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
