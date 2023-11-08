__all__: list[str] = []

from typing_extensions import deprecated

@deprecated('')
def GetBool(sym: str, default: bool = False) -> bool: ...
@deprecated('')
def GetInt(sym: str, default: int = 0) -> int: ...
@deprecated('')
def GetDouble(sym: str, default: float = 0.0) -> float: ...
@deprecated('')
def GetString(sym: str, default: str = '') -> str: ...

GetFloat = GetDouble
