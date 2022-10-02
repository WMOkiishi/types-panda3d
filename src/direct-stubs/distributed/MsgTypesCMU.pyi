from typing_extensions import Final, Literal

MsgName2Id: Final[dict[str, int]]
MsgId2Names: Final[dict[int, list[str]]]

SET_DOID_RANGE_CMU: Final[Literal[9001]]
CLIENT_OBJECT_GENERATE_CMU: Final[Literal[9002]]
OBJECT_GENERATE_CMU: Final[Literal[9003]]
OBJECT_UPDATE_FIELD_CMU: Final[Literal[9004]]
OBJECT_DISABLE_CMU: Final[Literal[9005]]
OBJECT_DELETE_CMU: Final[Literal[9006]]
REQUEST_GENERATES_CMU: Final[Literal[9007]]
CLIENT_DISCONNECT_CMU: Final[Literal[9008]]
CLIENT_SET_INTEREST_CMU: Final[Literal[9009]]
OBJECT_SET_ZONE_CMU: Final[Literal[9010]]
CLIENT_HEARTBEAT_CMU: Final[Literal[9011]]
CLIENT_OBJECT_UPDATE_FIELD_TARGETED_CMU: Final[Literal[9011]]
CLIENT_OBJECT_UPDATE_FIELD: Final[Literal[120]]
