import ast
import itertools
import logging
from collections.abc import Iterable, Iterator
from typing import Final

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
