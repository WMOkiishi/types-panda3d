from collections.abc import Callable, Mapping, Sequence
from typing import Any, NoReturn
from typing_extensions import Final

TIMEOUT_MAX: Final[float]
def force_yield() -> None: ...
def consider_yield() -> None: ...
forceYield = force_yield
considerYield = consider_yield
class error(Exception): ...

class LockType:
    def __init__(self) -> None: ...
    def release(self) -> None: ...
    def locked(self) -> bool: ...
    def __enter__(self, waitflag: bool = True, timeout: float = -1) -> bool: ...
    def __exit__(self, t: object, v: object, tb: object) -> None: ...
    acquire = __enter__

def start_new_thread(function: Callable[..., object], args: Sequence[Any], kwargs: Mapping[str, Any] = ..., name: str | None = None) -> int: ...
def interrupt_main() -> None: ...
def exit() -> NoReturn: ...
def allocate_lock() -> LockType: ...
def get_ident(): ...
def stack_size(size: object = 0) -> NoReturn: ...
