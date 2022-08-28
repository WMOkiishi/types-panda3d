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

def setprofile(func) -> None: ...
def settrace(func) -> None: ...

def RLock(verbose: bool | None = None) -> _RLock: ...

class _RLock:
    def __init__(self, verbose: bool | None = None) -> None: ...
    acquire = __enter__
    def __enter__(self, blocking=1) -> bool: ...
    def release(self) -> None: ...
    def __exit__(self, t: object, v: object, tb: object) -> None: ...

def Condition(lock=None, verbose: bool | None = None) -> _Condition: ...

class _Condition:
    def __init__(self, lock=None, verbose: bool | None = None) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, t: object, v: object, tb: object, /) -> None: ...
    def wait(self, timeout: float | None = None) -> None: ...
    def notify(self, n: int = 1) -> None: ...
    def notifyAll(self) -> None: ...

def Semaphore(value: int = 1, verbose: bool | None = None) -> _Semaphore: ...

class _Semaphore:
    def __init__(self, value: int = 1, verbose: bool | None = None) -> None: ...
    acquire = __enter__
    def __enter__(self, blocking: bool = True) -> bool: ...
    def release(self) -> None: ...
    def __exit__(self, t: object, v: object, tb: object) -> None: ...

def BoundedSemaphore(value: int = 1, verbose: bool | None = None) -> _BoundedSemaphore: ...

class _BoundedSemaphore:
    def __init__(self, value: int = 1, verbose: bool | None = None) -> None: ...
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
        args: Iterable[Any] = (),
        kwargs: Mapping[str, Any] | None = None,
        verbose: bool | None = None,
        daemon: bool | None = None,
    ) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def join(self, timeout: float | None) -> None: ...
    def getName(self) -> str: ...
    def setName(self, name: str) -> None: ...
    def is_alive(self) -> bool: ...
    isAlive = is_alive
    def isDaemon(self) -> bool: ...
    def setDaemon(self, daemonic: bool) -> None: ...

def Timer(interval, function, args=..., kwargs=...) -> _Timer: ...

class _Timer(Thread):
    def __init__(self, interval, function, args=..., kwargs=...) -> None: ...
    def cancel(self) -> None: ...

def current_thread(): ...
currentThread = current_thread
def active_count() -> int: ...
activeCount = active_count
def enumerate(): ...
def main_thread(): ...
