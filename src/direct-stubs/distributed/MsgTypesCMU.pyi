from typing import Final

MsgName2Id: Final[dict[str, int]]
MsgId2Names: Final[dict[int, list[str]]]

SET_DOID_RANGE_CMU: Final = 9001
CLIENT_OBJECT_GENERATE_CMU: Final = 9002
OBJECT_GENERATE_CMU: Final = 9003
OBJECT_UPDATE_FIELD_CMU: Final = 9004
OBJECT_DISABLE_CMU: Final = 9005
OBJECT_DELETE_CMU: Final = 9006
REQUEST_GENERATES_CMU: Final = 9007
CLIENT_DISCONNECT_CMU: Final = 9008
CLIENT_SET_INTEREST_CMU: Final = 9009
OBJECT_SET_ZONE_CMU: Final = 9010
CLIENT_HEARTBEAT_CMU: Final = 9011
CLIENT_OBJECT_UPDATE_FIELD_TARGETED_CMU: Final = 9011
CLIENT_OBJECT_UPDATE_FIELD: Final = 120
