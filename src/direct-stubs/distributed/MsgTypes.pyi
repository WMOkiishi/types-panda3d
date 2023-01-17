from typing_extensions import Final, Never

MsgName2Id: Final[dict[str, int]]
MsgId2Names: Final[dict[int, list[str]]]

CLIENT_HELLO: Final = 1
CLIENT_HELLO_RESP: Final = 2
CLIENT_DISCONNECT: Final = 3
CLIENT_EJECT: Final = 4
CLIENT_HEARTBEAT: Final = 5

CLIENT_OBJECT_SET_FIELD: Final = 120
CLIENT_OBJECT_SET_FIELDS: Final = 121
CLIENT_OBJECT_LEAVING: Final = 132
CLIENT_OBJECT_LEAVING_OWNER: Final = 161
CLIENT_ENTER_OBJECT_REQUIRED: Final = 142
CLIENT_ENTER_OBJECT_REQUIRED_OTHER: Final = 143
CLIENT_ENTER_OBJECT_REQUIRED_OWNER: Final = 172
CLIENT_ENTER_OBJECT_REQUIRED_OTHER_OWNER: Final = 173

CLIENT_DONE_INTEREST_RESP: Final = 204
CLIENT_ADD_INTEREST: Final = 200
CLIENT_ADD_INTEREST_MULTIPLE: Final = 201
CLIENT_REMOVE_INTEREST: Final = 203
CLIENT_OBJECT_LOCATION: Final = 140

CONTROL_CHANNEL: Final = 1
CONTROL_ADD_CHANNEL: Final = 9000
CONTROL_REMOVE_CHANNEL: Final = 9001
CONTROL_ADD_RANGE: Final = 9002
CONTROL_REMOVE_RANGE: Final = 9003
CONTROL_ADD_POST_REMOVE: Final = 9010
CONTROL_CLEAR_POST_REMOVES: Final = 9011

STATESERVER_CREATE_OBJECT_WITH_REQUIRED: Final = 2000
STATESERVER_CREATE_OBJECT_WITH_REQUIRED_OTHER: Final = 2001
STATESERVER_DELETE_AI_OBJECTS: Final = 2009
STATESERVER_OBJECT_GET_FIELD: Final = 2010
STATESERVER_OBJECT_GET_FIELD_RESP: Final = 2011
STATESERVER_OBJECT_GET_FIELDS: Final = 2012
STATESERVER_OBJECT_GET_FIELDS_RESP: Final = 2013
STATESERVER_OBJECT_GET_ALL: Final = 2014
STATESERVER_OBJECT_GET_ALL_RESP: Final = 2015
STATESERVER_OBJECT_SET_FIELD: Final = 2020
STATESERVER_OBJECT_SET_FIELDS: Final = 2021
STATESERVER_OBJECT_DELETE_FIELD_RAM: Final = 2030
STATESERVER_OBJECT_DELETE_FIELDS_RAM: Final = 2031
STATESERVER_OBJECT_DELETE_RAM: Final = 2032
STATESERVER_OBJECT_SET_LOCATION: Final = 2040
STATESERVER_OBJECT_CHANGING_LOCATION: Final = 2041
STATESERVER_OBJECT_ENTER_LOCATION_WITH_REQUIRED: Final = 2042
STATESERVER_OBJECT_ENTER_LOCATION_WITH_REQUIRED_OTHER: Final = 2043
STATESERVER_OBJECT_GET_LOCATION: Final = 2044
STATESERVER_OBJECT_GET_LOCATION_RESP: Final = 2045
STATESERVER_OBJECT_SET_AI: Final = 2050
STATESERVER_OBJECT_CHANGING_AI: Final = 2051
STATESERVER_OBJECT_ENTER_AI_WITH_REQUIRED: Final = 2052
STATESERVER_OBJECT_ENTER_AI_WITH_REQUIRED_OTHER: Final = 2053
STATESERVER_OBJECT_GET_AI: Final = 2054
STATESERVER_OBJECT_GET_AI_RESP: Final = 2055
STATESERVER_OBJECT_SET_OWNER: Final = 2060
STATESERVER_OBJECT_CHANGING_OWNER: Final = 2061
STATESERVER_OBJECT_ENTER_OWNER_WITH_REQUIRED: Final = 2062
STATESERVER_OBJECT_ENTER_OWNER_WITH_REQUIRED_OTHER: Final = 2063
STATESERVER_OBJECT_GET_OWNER: Final = 2064
STATESERVER_OBJECT_GET_OWNER_RESP: Final = 2065
STATESERVER_OBJECT_GET_ZONE_OBJECTS: Final = 2100
STATESERVER_OBJECT_GET_ZONES_OBJECTS: Final = 2102
STATESERVER_OBJECT_GET_CHILDREN: Final = 2104
STATESERVER_OBJECT_GET_ZONE_COUNT: Final = 2110
STATESERVER_OBJECT_GET_ZONE_COUNT_RESP: Final = 2111
STATESERVER_OBJECT_GET_ZONES_COUNT: Final = 2112
STATESERVER_OBJECT_GET_ZONES_COUNT_RESP: Final = 2113
STATESERVER_OBJECT_GET_CHILD_COUNT: Final = 2114
STATESERVER_OBJECT_GET_CHILD_COUNT_RESP: Final = 2115
STATESERVER_OBJECT_DELETE_ZONE: Final = 2120
STATESERVER_OBJECT_DELETE_ZONES: Final = 2122
STATESERVER_OBJECT_DELETE_CHILDREN: Final = 2124

DBSS_OBJECT_ACTIVATE_WITH_DEFAULTS: Final = 2200
DBSS_OBJECT_ACTIVATE_WITH_DEFAULTS_OTHER: Final = 2201
DBSS_OBJECT_GET_ACTIVATED: Final = 2207
DBSS_OBJECT_GET_ACTIVATED_RESP: Final = 2208
DBSS_OBJECT_DELETE_FIELD_DISK: Final = 2230
DBSS_OBJECT_DELETE_FIELDS_DISK: Final = 2231
DBSS_OBJECT_DELETE_DISK: Final = 2232

DBSERVER_CREATE_OBJECT: Final = 3000
DBSERVER_CREATE_OBJECT_RESP: Final = 3001
DBSERVER_OBJECT_GET_FIELD: Final = 3010
DBSERVER_OBJECT_GET_FIELD_RESP: Final = 3011
DBSERVER_OBJECT_GET_FIELDS: Final = 3012
DBSERVER_OBJECT_GET_FIELDS_RESP: Final = 3013
DBSERVER_OBJECT_GET_ALL: Final = 3014
DBSERVER_OBJECT_GET_ALL_RESP: Final = 3015
DBSERVER_OBJECT_SET_FIELD: Final = 3020
DBSERVER_OBJECT_SET_FIELDS: Final = 3021
DBSERVER_OBJECT_SET_FIELD_IF_EQUALS: Final = 3022
DBSERVER_OBJECT_SET_FIELD_IF_EQUALS_RESP: Final = 3023
DBSERVER_OBJECT_SET_FIELDS_IF_EQUALS: Final = 3024
DBSERVER_OBJECT_SET_FIELDS_IF_EQUALS_RESP: Final = 3025
DBSERVER_OBJECT_SET_FIELD_IF_EMPTY: Final = 3026
DBSERVER_OBJECT_SET_FIELD_IF_EMPTY_RESP: Final = 3027
DBSERVER_OBJECT_DELETE_FIELD: Final = 3030
DBSERVER_OBJECT_DELETE_FIELDS: Final = 3031
DBSERVER_OBJECT_DELETE: Final = 3032

CLIENTAGENT_SET_STATE: Final = 1000
CLIENTAGENT_SET_CLIENT_ID: Final = 1001
CLIENTAGENT_SEND_DATAGRAM: Final = 1002
CLIENTAGENT_EJECT: Final = 1004
CLIENTAGENT_DROP: Final = 1005
CLIENTAGENT_GET_NETWORK_ADDRESS: Final = 1006
CLIENTAGENT_GET_NETWORK_ADDRESS_RESP: Final = 1007
CLIENTAGENT_DECLARE_OBJECT: Final = 1010
CLIENTAGENT_UNDECLARE_OBJECT: Final = 1011
CLIENTAGENT_ADD_SESSION_OBJECT: Final = 1012
CLIENTAGENT_REMOVE_SESSION_OBJECT: Final = 1013
CLIENTAGENT_SET_FIELDS_SENDABLE: Final = 1014
CLIENTAGENT_OPEN_CHANNEL: Final = 1100
CLIENTAGENT_CLOSE_CHANNEL: Final = 1101
CLIENTAGENT_ADD_POST_REMOVE: Final = 1110
CLIENTAGENT_CLEAR_POST_REMOVES: Final = 1111
CLIENTAGENT_ADD_INTEREST: Final = 1200
CLIENTAGENT_ADD_INTEREST_MULTIPLE: Final = 1201
CLIENTAGENT_REMOVE_INTEREST: Final = 1203

QUIET_ZONE_IGNORED_LIST: Final[list[Never]]

CLIENT_LOGIN_2_GREEN: Final = 1
CLIENT_LOGIN_2_PLAY_TOKEN: Final = 2
CLIENT_LOGIN_2_BLUE: Final = 3
CLIENT_LOGIN_3_DISL_TOKEN: Final = 4
