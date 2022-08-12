from typing_extensions import Literal, TypeAlias

_OldBool: TypeAlias = Literal[0, 1]

class RotatingLog:
    path: str
    timeInterval: float | None
    timeLimit: float | None
    sizeLimit: float | None
    def __init__(self, path: str = './log_file', hourInterval: float | None = 24, megabyteLimit: float | None = 1024) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def shouldRotate(self) -> _OldBool: ...
    def filePath(self) -> str: ...
    def rotate(self) -> None: ...
    def write(self, data): ...
    def flush(self) -> None: ...
    def fileno(self) -> int: ...
    def isatty(self) -> bool: ...
    def __next__(self): ...
    def next(self): ...
    def read(self, size): ...
    def readline(self, size): ...
    def readlines(self, sizehint): ...
    def xreadlines(self): ...
    def seek(self, offset, whence = 0): ...
    def tell(self) -> int: ...
    def truncate(self, size) -> int: ...
    def writelines(self, sequence) -> None: ...
