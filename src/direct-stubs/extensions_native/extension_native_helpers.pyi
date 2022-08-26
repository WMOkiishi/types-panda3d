__all__ = ['Dtool_ObjectToDict', 'Dtool_funcToMethod']

from collections.abc import Callable
from typing import Any

def Dtool_ObjectToDict(clas: Any, name, obj) -> None: ...

def Dtool_funcToMethod(func: Callable[..., Any], cls: Any, method_name: str | None = None) -> None: ...
