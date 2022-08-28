from .DirectMySQLdbConnection import DirectMySQLdbConnection

def connect(*args, **kwargs) -> DirectMySQLdbConnection: ...
Connect = connect
Connection = connect
