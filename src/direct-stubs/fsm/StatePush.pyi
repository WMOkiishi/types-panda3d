__all__ = ['EnterExit', 'EventArgument', 'EventPulse', 'FunctionCall', 'Pulse', 'StateVar']

from collections.abc import Callable
from typing import Any, Generic, TypeVar
from typing_extensions import Self

from direct.showbase.DirectObject import DirectObject

_T = TypeVar('_T')

class PushesStateChanges(Generic[_T]):
    def __init__(self, value: _T) -> None: ...
    def destroy(self) -> None: ...
    def getState(self) -> _T: ...
    def pushCurrentState(self) -> Self: ...

class ReceivesStateChanges(Generic[_T]):
    def __init__(self, source: PushesStateChanges[_T]) -> None: ...
    def destroy(self) -> None: ...

class StateVar(PushesStateChanges[_T]):
    def set(self, value: _T) -> None: ...
    def get(self) -> _T: ...

class StateChangeNode(PushesStateChanges[_T], ReceivesStateChanges[_T]):
    def __init__(self, source: PushesStateChanges[_T]) -> None: ...

class ReceivesMultipleStateChanges:
    def __init__(self) -> None: ...
    def destroy(self) -> None: ...

class FunctionCall(ReceivesMultipleStateChanges, PushesStateChanges[Any]):
    def __init__(self, func: Callable[..., object], *args: Any, **kArgs: Any) -> None: ...
    def getState(self) -> tuple[tuple[Any, ...], dict[str, Any]]: ...

class EnterExit(StateChangeNode[bool]):
    def __init__(
        self, source: PushesStateChanges[bool], enterFunc: Callable[[], object], exitFunc: Callable[[], object]
    ) -> None: ...

class Pulse(PushesStateChanges[bool]):
    def __init__(self) -> None: ...
    def sendPulse(self) -> None: ...

class EventPulse(Pulse, DirectObject):
    def __init__(self, event: str) -> None: ...

class EventArgument(PushesStateChanges[Any], DirectObject):
    def __init__(self, event: str, index: int = 0) -> None: ...

class AttrSetter(StateChangeNode[_T]):
    def __init__(self, source: PushesStateChanges[_T], object: Any, attrName: str) -> None: ...
