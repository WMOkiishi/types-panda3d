from typing_extensions import Final, Literal

class StagedObject:
    UNKNOWN: Final[Literal[-1]]
    OFF: Final[Literal[0]]
    ON: Final[Literal[1]]
    def __init__(self, initState: Literal[-1, 0, 1] = ...) -> None: ...
    def goOnStage(self) -> None: ...
    def handleOnStage(self) -> None: ...
    def goOffStage(self) -> None: ...
    def handleOffStage(self) -> None: ...
    def isOnStage(self) -> bool: ...
    def isOffStage(self) -> bool: ...
