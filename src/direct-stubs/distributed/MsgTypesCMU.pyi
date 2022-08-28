MsgName2Id: dict[str, int]
MsgId2Names: dict[int, list[str]]

# The source file uses `globals().update(MsgName2Id)`
def __getattr__(name: str) -> int: ...
