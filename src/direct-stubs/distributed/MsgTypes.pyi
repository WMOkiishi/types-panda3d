from typing_extensions import Final, Literal, Never

MsgName2Id: Final[dict[str, int]]
MsgId2Names: Final[dict[int, list[str]]]
QUIET_ZONE_IGNORED_LIST: Final[list[Never]]
CLIENT_LOGIN_2_GREEN: Final[Literal[1]]
CLIENT_LOGIN_2_PLAY_TOKEN: Final[Literal[2]]
CLIENT_LOGIN_2_BLUE: Final[Literal[3]]
CLIENT_LOGIN_3_DISL_TOKEN: Final[Literal[4]]

# The source file uses `globals().update(MsgName2Id)`
def __getattr__(name: str) -> int: ...
