import ast
import itertools
import logging
from collections.abc import Iterator
from typing import Final, ParamSpec, TypeVar

_logger: Final = logging.getLogger(__name__)

P = ParamSpec('P')
T = TypeVar('T')

flatten = itertools.chain.from_iterable


def is_dunder(s: str, /) -> bool:
    """Return whether a given string starts and ends with "__"."""
    return s.startswith('__') and s.endswith('__')


def is_sunder(s: str, /) -> bool:
    """Return whether a given string starts and ends with exactly one underscore."""
    return s.startswith('_') and s.endswith('_') and not is_dunder(s)


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


# def print_stats(f: Callable[P, T], /) -> Callable[P, T]:
#     @wraps(f)
#     def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
#         with cProfile.Profile() as prof:
#             result = f(*args, **kwargs)
#         stats = pstats.Stats(prof)
#         stats.sort_stats(pstats.SortKey.TIME)
#         stats.print_stats()
#         return result
#
#     return wrapper
