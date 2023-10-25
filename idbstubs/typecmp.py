from __future__ import annotations

import abc
import itertools
import logging
from collections.abc import Collection, Container, Iterable, Iterator, Sequence
from typing import Final

import attrs

from .util import unpack_union

_logger: Final = logging.getLogger(__name__)
_type_cache: Final[dict[str, Type]] = {}


class Type(metaclass=abc.ABCMeta):
    def check_subclass(self, subclass: Type) -> bool:
        return self == subclass

    def check_superclass(self, superclass: Type) -> bool:
        return self == superclass

    def __ge__(self, other: Type) -> bool:
        return self.check_subclass(other) or other.check_superclass(self)

    def __le__(self, other: Type) -> bool:
        return self.check_superclass(other) or other.check_subclass(self)

    def __gt__(self, other: Type) -> bool:
        return self >= other and not self <= other

    def __lt__(self, other: Type) -> bool:
        return self <= other and not self >= other

    def __or__(self, other: Type) -> Type:
        return unify_types((self, other))

    def __sub__(self, other: Type) -> Type:
        return BottomType() if self <= other else self


@attrs.frozen
class BasicType(Type):
    name: str

    def __str__(self) -> str:
        return self.name


@attrs.frozen
class ClassType(Type):
    name: str
    bases: Sequence[ClassType] = attrs.field(default=(), converter=tuple)

    def __str__(self) -> str:
        return self.name

    def check_superclass(self, superclass: Type) -> bool:
        if self == superclass:
            return True
        for base in self.bases:
            if base <= superclass:
                return True
        return False


@attrs.frozen
class AliasType(Type):
    name: str
    alias_of: Type

    def __str__(self) -> str:
        return self.name

    def check_subclass(self, subclass: Type) -> bool:
        return self.alias_of >= subclass

    def check_superclass(self, superclass: Type) -> bool:
        return self.alias_of <= superclass

    def __sub__(self, other: Type) -> Type:
        result = self.alias_of - other
        if result == self.alias_of:
            return self
        return result


@attrs.frozen
class UnionType(Type):
    parts: Collection[Type] = attrs.field(converter=tuple)

    def __str__(self) -> str:
        return ' | '.join(str(part) for part in self.parts)

    def check_subclass(self, subclass: Type) -> bool:
        return any(part >= subclass for part in self.parts)

    def check_superclass(self, superclass: Type) -> bool:
        return all(part <= superclass for part in self.parts)

    def __sub__(self, other: Type) -> Type:
        return unify_types(part - other for part in self.parts)


@attrs.frozen
class ProtocolType(Type):
    name: str
    matches: Container[Type]

    def __str__(self) -> str:
        return self.name

    def check_subclass(self, subclass: Type) -> bool:
        return subclass == self or subclass in self.matches


@attrs.frozen
class BottomType(Type):
    name: str = 'Never'

    def __str__(self) -> str:
        return self.name

    def check_superclass(self, superclass: Type) -> bool:
        return True


@attrs.frozen
class MissingType(Type):
    def __str__(self) -> str:
        return ''

    def __bool__(self) -> bool:
        return False


def atomize(*types: Type, follow_aliases: bool = True) -> Iterator[Type]:
    for typ in types:
        if follow_aliases and isinstance(typ, AliasType):
            yield from atomize(typ.alias_of, follow_aliases=True)
        elif isinstance(typ, UnionType):
            yield from atomize(*typ.parts, follow_aliases=follow_aliases)
        else:
            yield typ


def _union_sort_key(typ: Type) -> tuple[bool, str]:
    string = str(typ)
    return string == 'None', string


def unify_types(types: Iterable[Type]) -> Type:
    """Return a type equivalent to the union of the given types."""
    unique_types = set(atomize(*types, follow_aliases=False))
    for a, b in itertools.combinations(unique_types, 2):
        if a <= b:
            unique_types.discard(a)
        elif b <= a:
            unique_types.discard(b)
    if not unique_types:
        return BottomType()
    elif len(unique_types) == 1:
        return unique_types.pop()
    else:
        return UnionType(sorted(unique_types, key=_union_sort_key))


def types_intersect(a: Type, b: Type, /) -> bool:
    """Return whether the given types have any intersection."""
    for t, u in itertools.product(atomize(a), atomize(b)):
        if t <= u or u <= t:
            return True
    return False


def soft_difference(a: Type, b: Type, /) -> Type:
    return unify_types(
        t for t in atomize(a, follow_aliases=False)
        if not t <= b
    )


def register(typ: Type) -> None:
    key = str(typ)
    if key in _type_cache:
        raise ValueError(f'Attempt to re-register a type as {key!r}')
    _type_cache[key] = typ


def get(key: str) -> Type:
    if (registered := _type_cache.get(key)) is not None:
        return registered
    parts = list(unpack_union(key))
    if len(parts) == 1:
        typ = BasicType(key)
        _type_cache[key] = typ
        return typ
    return unify_types(get(part) for part in parts)


register(BottomType())
register(MissingType())
register(ProtocolType('float', frozenset({BasicType('int')})))
