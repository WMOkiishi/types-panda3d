__all__ = ['Messenger']

from collections.abc import Callable
from typing import Any, ClassVar
from typing_extensions import TypeAlias

from direct.directnotify.Notifier import Notifier
from direct.stdpy.threading import Lock
from panda3d.core import AsyncFuture

from .DirectObject import DirectObject

# Ideally, this should just be Sequence[Any], but the code here and in DirectObject
# means that it has to be one of these.
_Args: TypeAlias = tuple[Any, ...] | list[Any]
_EventDict: TypeAlias = dict[tuple[str, int], tuple[Callable[..., Any], _Args, bool]]

class Messenger:
    notify: ClassVar[Notifier]
    lock: Lock
    quieting: dict[str, bool]
    def __init__(self) -> None: ...
    def future(self, event: str) -> AsyncFuture: ...
    def accept(
        self, event: str, object: DirectObject, method: Callable[..., object], extraArgs: _Args = ..., persistent: bool = ...
    ) -> None: ...
    def ignore(self, event: str, object: DirectObject) -> None: ...
    def ignore_all(self, object: DirectObject) -> None: ...
    def get_all_accepting(self, object: DirectObject) -> list[str]: ...
    def is_accepting(self, event: str, object: DirectObject) -> bool: ...
    def who_accepts(self, event: str) -> _EventDict | None: ...
    def is_ignoring(self, event: str, object: DirectObject) -> bool: ...
    def send(self, event: str, sentArgs: _Args = ..., taskChain: str | None = ...) -> None: ...
    def clear(self) -> None: ...
    def is_empty(self) -> bool: ...
    def get_events(self) -> list[str]: ...
    def replace_method(self, oldMethod: Callable[..., object], newFunction: Callable[..., object]) -> int: ...
    def toggle_verbose(self) -> None: ...
    def find(self, needle: str) -> dict[str, _EventDict]: ...
    def find_all(self, needle: str, limit: int | None = ...) -> dict[str, _EventDict]: ...
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
