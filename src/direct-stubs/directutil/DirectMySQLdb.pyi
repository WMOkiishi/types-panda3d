from typing import Any

from .DirectMySQLdbConnection import DirectMySQLdbConnection

def connect(*args: Any, **kwargs: Any) -> DirectMySQLdbConnection: ...

Connect = connect
Connection = connect
