__all__ = []

def GetBool(sym: str, default: bool = False) -> bool: ...
def GetInt(sym: str, default: int = 0) -> int: ...
def GetDouble(sym: str, default: float = 0.0) -> float: ...
def GetString(sym: str, default: str = '') -> str: ...
GetFloat = GetDouble