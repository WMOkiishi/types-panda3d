__all__ = [
    'BoundedSemaphore',
    'Condition',
    'Event',
    'Lock',
    'RLock',
    'Semaphore',
    'TIMEOUT_MAX',
    'Thread',
    'ThreadError',
    'Timer',
    'active_count',
    'current_thread',
    'enumerate',
    'get_ident',
    'local',
    'main_thread',
    'setprofile',
    'settrace',
    'stack_size',
]

from collections.abc import Callable, Iterable, Mapping
from typing import Any
from typing_extensions import TypeAlias

from .thread import (
    allocate_lock as Lock,
    error as ThreadError,
    get_ident as get_ident,
    TIMEOUT_MAX as TIMEOUT_MAX,
)
from .threading import (
    local as local,
    stack_size as stack_size,
)

_Unused: TypeAlias = object

def setprofile(func: Callable[..., Any]) -> None: ...
def settrace(func: Callable[..., Any]) -> None: ...

def RLock(verbose: bool | None = None) -> _RLock: ...

class _RLock:
    def __init__(self, verbose: bool | None = None) -> None: ...
    def __enter__(self, blocking: bool = True) -> bool: ...
    def release(self) -> None: ...
    def __exit__(self, t: _Unused, v: _Unused, tb: _Unused) -> None: ...
    acquire = __enter__

def Condition(lock: _RLock | None = None, verbose: bool | None = None) -> _Condition: ...

class _Condition:
    def __init__(self, lock: _RLock | None = None, verbose: bool | None = None) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, __t: _Unused, __v: _Unused, __tb: _Unused) -> None: ...
    def wait(self, timeout: float | None = None) -> None: ...
    def notify(self, n: int = ...) -> None: ...
    def notifyAll(self) -> None: ...

def Semaphore(value: int = ..., verbose: bool | None = None) -> _Semaphore: ...

class _Semaphore:
    def __init__(self, value: int = ..., verbose: bool | None = None) -> None: ...
    def __enter__(self, blocking: bool = True) -> bool: ...
    def release(self) -> None: ...
    def __exit__(self, t: _Unused, v: _Unused, tb: _Unused) -> None: ...
    acquire = __enter__

def BoundedSemaphore(value: int = ..., verbose: bool | None = None) -> _BoundedSemaphore: ...

class _BoundedSemaphore:
    def __init__(self, value: int = ..., verbose: bool | None = None) -> None: ...
    def release(self) -> None: ...

def Event(verbose: bool | None = None) -> _Event: ...

class _Event:
    def __init__(self, verbose: bool | None = None) -> None: ...
    def isSet(self) -> bool: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    def wait(self, timeout: float | None = None) -> None: ...

class Thread:
    name: str
    daemon: bool
    def __init__(
        self,
        group: None = None,
        target: Callable[..., object] | None = None,
        name: object = None,
        args: Iterable[Any] = ...,
        kwargs: Mapping[str, Any] | None = None,
        verbose: bool | None = None,
        daemon: bool | None = None,
    ) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def join(self, timeout: float | None = None) -> None: ...
    def getName(self) -> str: ...
    def setName(self, name: str) -> None: ...
    def is_alive(self) -> bool: ...
    isAlive = is_alive
    def isDaemon(self) -> bool: ...
    def setDaemon(self, daemonic: bool) -> None: ...

def Timer(
    interval: float | None,
    function: Callable[..., Any],
    args: Iterable[Any] = ...,
    kwargs: Mapping[str, Any] = ...,
) -> _Timer: ...

class _Timer(Thread):
    def __init__(
        self,
        interval: float | None,
        function: Callable[..., Any],
        args: Iterable[Any] = ...,
        kwargs: Mapping[str, Any] = ...,
    ) -> None: ...
    def cancel(self) -> None: ...

def current_thread() -> Thread: ...
currentThread = current_thread
def active_count() -> int: ...
activeCount = active_count
def enumerate() -> list[Thread]: ...
def main_thread() -> Thread: ...
