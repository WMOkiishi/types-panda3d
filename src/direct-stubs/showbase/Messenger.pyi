__all__ = ['Messenger']

from collections.abc import Callable, Sequence
from typing import Any, ClassVar
from typing_extensions import TypeAlias

from panda3d.core import AsyncFuture
from ..directnotify.Notifier import Notifier
from ..stdpy.threading import Lock
from .DirectObject import DirectObject

# Ideally, this should just be Sequence[Any], but the code specifically checks
# for one of these types.
_Args: TypeAlias = tuple[Any, ...] | list[Any] | set[Any]
class Messenger:
    notify: ClassVar[Notifier]
    lock: Lock
    quieting: dict[str, bool]
    def __init__(self) -> None: ...
    def future(self, event: str) -> AsyncFuture: ...
    def accept(
        self,
        event: str,
        object: DirectObject,
        method: Callable[..., object],
        extraArgs: _Args = ...,
        persistent: bool = True,
    ) -> None: ...
    def ignore(self, event: str, object: DirectObject) -> None: ...
    def ignore_all(self, object: DirectObject) -> None: ...
    def get_all_accepting(self, object: DirectObject): ...
    def is_accepting(self, event: str, object: DirectObject) -> bool: ...
    def who_accepts(self, event: str): ...
    def is_ignoring(self, event: str, object: DirectObject) -> bool: ...
    def send(self, event: str, sentArgs: Sequence[Any] = ..., taskChain: str | None = None) -> None: ...
    def clear(self) -> None: ...
    def is_empty(self) -> bool: ...
    def get_events(self): ...
    def replace_method(self, oldMethod: Callable[..., object], newFunction: Callable[..., object]) -> int: ...
    def toggle_verbose(self) -> None: ...
    def find(self, needle: str): ...
    def find_all(self, needle: str, limit: int | None = None): ...
    def detailed_repr(self) -> str: ...
    ignoreAll = ignore_all
    getAllAccepting = get_all_accepting
    isAccepting = is_accepting
    whoAccepts = who_accepts
    isIgnoring = is_ignoring
    isEmpty = is_empty
    getEvents = get_events
    replaceMethod = replace_method
    toggleVerbose = toggle_verbose
    findAll = find_all
    detailedRepr = detailed_repr