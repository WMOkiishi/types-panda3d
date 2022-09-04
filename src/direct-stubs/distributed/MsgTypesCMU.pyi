from typing_extensions import Final

MsgName2Id: Final[dict[str, int]]
MsgId2Names: Final[dict[int, list[str]]]

# The source file uses `globals().update(MsgName2Id)`
def __getattr__(name: str) -> int: ...
