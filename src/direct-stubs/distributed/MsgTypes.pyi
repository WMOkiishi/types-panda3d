from typing_extensions import Literal, Never

MsgName2Id: dict[str, int]
MsgId2Names: dict[int, list[str]]
QUIET_ZONE_IGNORED_LIST: list[Never]
CLIENT_LOGIN_2_GREEN: Literal[1]
CLIENT_LOGIN_2_PLAY_TOKEN: Literal[2]
CLIENT_LOGIN_2_BLUE: Literal[3]
CLIENT_LOGIN_3_DISL_TOKEN: Literal[4]

# The source file uses `globals().update(MsgName2Id)`
def __getattr__(name: str) -> int: ...
