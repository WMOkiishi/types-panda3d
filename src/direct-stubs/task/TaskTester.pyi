# undocumented
__all__: list[str] = []

from typing import Literal

from direct._typing import Unused

numTasks: int
maxDelay: int
counter: int

def spawnNewTask() -> None: ...
def taskCallback(task: Unused) -> Literal[0]: ...
