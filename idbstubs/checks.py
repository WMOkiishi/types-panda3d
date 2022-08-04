import importlib
import logging
from typing import Final

from .reps import Alias, Class, Module, StubRep
from .special_cases import ITERABLE, NO_STUBS
from .util import flatten, is_sunder

_logger: Final = logging.getLogger(__name__)

ignored_type_attrs: Final = NO_STUBS | {
    '__new__', '__init__', '__hash__',
    '__doc__', '__module__',
    '__copy__', '__deepcopy__',
    '__radd__', '__rsub__', '__rmul__',
    '__rtruediv__', '__rfloordiv__',
    '__rand__', '__ror__', '__rxor__',
    '__rlshift__', '__rrshift__',
    '__rpow__', '__rmod__',
}
ignored_mod_attrs: Final = frozenset((
    '__doc__', '__file__', '__loader__',
    '__name__', '__package__', '__spec__',
    'Dtool_BorrowThisReference',
    'Dtool_PyNativeInterface',
))
_comparisons: Final = frozenset(('__lt__', '__le__', '__ge__', '__gt__'))
_equality: Final = frozenset(('__eq__', '__ne__'))


def is_stub_only(rep: StubRep) -> bool:
    if isinstance(rep, Alias):
        return rep.is_type_alias
    return False


def check_class(rep: Class, runtime: object) -> None:
    rep_attrs = {i.name for i in rep.nested if not is_stub_only(i)}
    runtime_attrs = {i for i in runtime.__dict__ if not is_sunder(i)}
    no_stub = runtime_attrs - rep_attrs - ignored_type_attrs
    no_runtime = rep_attrs - runtime_attrs
    if '__setitem__' in rep_attrs:
        # __delitem__ shares a slot with __setitem__, even if it can't be used
        no_stub.discard('__delitem__')
    if no_stub >= _equality:
        # If both are missing, they're probably just equivalent to object.__eq__ / __ne__
        no_stub -= _equality
    elif '__eq__' in rep_attrs:
        no_stub.discard('__ne__')
    if no_stub >= _comparisons:
        # If all four are missing, they probably all just return NotImplemented
        no_stub -= _comparisons
    else:
        if '__lt__' in rep_attrs:
            no_stub.discard('__gt__')
        if '__le__' in rep_attrs:
            no_stub.discard('__ge__')
    if rep.name in ITERABLE:
        no_runtime.discard('__iter__')
    if no_stub:
        _logger.warning(f'No stubs for attributes {no_stub} in {rep}')
    if no_runtime:
        _logger.warning(f'Attributes {no_runtime} in {rep} do not exist at runtime')
    for i in rep.nested:
        if isinstance(i, Class):
            name = i.name
            if name not in no_runtime:
                check_class(i, getattr(runtime, name))


def check_module(mod_rep: Module) -> None:
    try:
        module = importlib.import_module(mod_rep.scoped_name)
    except ModuleNotFoundError:
        _logger.error(f'Could not find {mod_rep}')
        return
    all_nested = list(flatten(mod_rep.nested.values()))
    rep_attrs = {i.name for i in all_nested if not is_stub_only(i)}
    runtime_attrs = set(module.__dict__)
    no_stub = runtime_attrs - rep_attrs - ignored_mod_attrs
    no_runtime = rep_attrs - runtime_attrs
    if no_stub:
        _logger.warning(f'No stubs for attributes {no_stub} in {mod_rep}')
    if no_runtime:
        _logger.warning(f'Attributes {no_runtime} in {mod_rep} do not exist at runtime')
    for i in all_nested:
        if isinstance(i, Class):
            name = i.name
            if name not in no_runtime:
                check_class(i, getattr(module, name))
    _logger.debug(f'Finished checking {mod_rep}')
