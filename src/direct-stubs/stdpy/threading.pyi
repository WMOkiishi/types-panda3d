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
    'local',
    'main_thread',
    'setprofile',
    'settrace',
    'stack_size',
]

from collections.abc import Callable, Iterable, Mapping
from typing import Any, NoReturn
from typing_extensions import Final, Never

from direct._typing import Unused
from panda3d import core
from .thread import error as ThreadError

TIMEOUT_MAX: Final[float]

class local:
    def __del__(self) -> None: ...
    def __setattr__(self, key: str, value: Any) -> None: ...
    def __getattr__(self, key: str) -> Any: ...

class ThreadBase:
    name: str
    daemon: bool
    ident: Never
    def __init__(self) -> None: ...
    def getName(self) -> str: ...
    def isDaemon(self) -> bool: ...
    def setDaemon(self, daemon: bool) -> None: ...
    def __setattr__(self, key: str, value: Any) -> None: ...
    forceYield = core.Thread.forceYield
    considerYield = core.Thread.considerYield

class Thread(ThreadBase):
    def __init__(
        self,
        group: None = None,
        target: Callable[..., object] | None = None,
        name: str | None = None,
        args: Iterable[Any] = ...,
        kwargs: Mapping[str, Any] = ...,
        daemon: bool | None = None,
    ) -> None: ...
    def __del__(self) -> None: ...
    def is_alive(self) -> bool: ...
    isAlive = is_alive
    def start(self) -> None: ...
    def run(self) -> None: ...
    def join(self, timeout: None = None) -> None: ...
    def setName(self, name: str) -> None: ...

class ExternalThread(ThreadBase):
    def __init__(self, extThread: ExternalThread, threadId: int) -> None: ...
    def is_alive(self) -> bool: ...
    def isAlive(self) -> bool: ...
    def start(self) -> NoReturn: ...
    def run(self) -> NoReturn: ...
    def join(self, timeout: Unused = None) -> NoReturn: ...
    def setDaemon(self, daemon: Unused) -> NoReturn: ...

class MainThread(ExternalThread): ...

class Lock(core.Mutex):
    def __init__(self, name: str = ...) -> None: ...
    def __enter__(self, blocking: bool = True) -> bool: ...
    def __exit__(self, t: Unused, v: Unused, tb: Unused) -> None: ...  # noqa: Y036
    acquire = __enter__  # type: ignore[assignment]

class RLock(core.ReMutex):
    def __init__(self, name: str = ...) -> None: ...
    def __enter__(self, blocking: bool = True) -> bool: ...
    def __exit__(self, t: Unused, v: Unused, tb: Unused) -> None: ...  # noqa: Y036
    acquire = __enter__  # type: ignore[assignment]

class Condition(core.ConditionVarFull):
    def __init__(self, lock: Lock | None = None) -> None: ...
    def acquire(self, blocking: bool = True) -> bool: ...
    def release(self) -> None: ...
    def wait(self, timeout: float | None = None) -> None: ...
    def __enter__(self, blocking: bool = True) -> bool: ...
    def __exit__(self, t: Unused, v: Unused, tb: Unused) -> None: ...  # noqa: Y036

class Semaphore(core.Semaphore):
    def __init__(self, value: int = ...) -> None: ...
    def __enter__(self, blocking: bool = True) -> bool: ...
    def __exit__(self, t: Unused, v: Unused, tb: Unused) -> None: ...  # noqa: Y036
    acquire = __enter__  # type: ignore[assignment]

class BoundedSemaphore(Semaphore): ...

class Event:
    def __init__(self) -> None: ...
    def is_set(self) -> bool: ...
    isSet = is_set
    def set(self) -> None: ...
    def clear(self) -> None: ...
    def wait(self, timeout: float | None = None) -> None: ...

class Timer(Thread):
    interval: float
    function: Callable[..., object]
    args: Iterable[Any]
    kwargs: Mapping[str, Any]
    finished: Event
    def __init__(
        self,
        interval: float,
        function: Callable[..., object],
        args: Iterable[Any] = ...,
        kwargs: Mapping[str, Any] = ...,
    ) -> None: ...
    def cancel(self) -> None: ...

def current_thread() -> ExternalThread: ...
def main_thread() -> MainThread: ...
currentThread = current_thread
def enumerate() -> list: ...
def active_count() -> int: ...
activeCount = active_count
def settrace(func: Callable[..., Any]) -> None: ...
def setprofile(func: Callable[..., Any]) -> None: ...
def stack_size(size: Unused = None) -> NoReturn: ...
