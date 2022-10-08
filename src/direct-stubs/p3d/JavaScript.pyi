__all__ = ['BrowserObject', 'ConcreteStruct', 'MethodWrapper', 'UndefinedObject', 'Undefined']

from typing import Any
from typing_extensions import Final, Literal

class UndefinedObject:
    def __bool__(self) -> Literal[False]: ...
    __nonzero__ = __bool__

Undefined: Final[UndefinedObject]

class ConcreteStruct:
    def __init__(self) -> None: ...
    def getConcreteProperties(self) -> list[Any]: ...

class BrowserObject:
    def __init__(self, runner, objectId) -> None: ...
    def __del__(self) -> None: ...
    def __bool__(self) -> Literal[True]: ...
    __nonzero__ = __bool__
    def __call__(self, *args, needsResponse: bool = ...): ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...

class MethodWrapper:
    def __init__(self, runner, parentObj, objectId) -> None: ...
    def __call__(self, *args, needsResponse: bool = ...) -> None: ...
    def __bool__(self) -> Literal[True]: ...
    __nonzero__ = __bool__
