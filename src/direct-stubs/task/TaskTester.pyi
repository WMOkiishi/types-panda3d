# undocumented
__all__: list[str] = []

from _typeshed import Unused
from typing import Literal

numTasks: int
maxDelay: int
counter: int

def spawnNewTask() -> None: ...
def taskCallback(task: Unused) -> Literal[0]: ...
