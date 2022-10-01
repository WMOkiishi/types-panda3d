__all__ = ['Dtool_ObjectToDict', 'Dtool_funcToMethod']

from collections.abc import Callable, MutableMapping
from typing import Any, ClassVar, Protocol

class _DtoolClass(Protocol):
    DtoolClassDict: ClassVar[MutableMapping[str, Any]]

def Dtool_ObjectToDict(cls: _DtoolClass, name: str, obj: Any) -> None: ...
def Dtool_funcToMethod(func: Callable[..., Any], cls: _DtoolClass, method_name: str | None = None) -> None: ...
