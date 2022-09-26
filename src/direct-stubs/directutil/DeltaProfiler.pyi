class DeltaProfiler:
    name: str
    priorLabel: str
    priorTime: float
    active: bool
    def __init__(self, name: str = ...) -> None: ...
    def printDeltaTime(self, label: str) -> None: ...
