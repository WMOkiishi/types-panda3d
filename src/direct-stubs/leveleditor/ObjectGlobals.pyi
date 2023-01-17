from typing_extensions import Final, Literal

OBJ_UID: Final = 0
OBJ_NP: Final = 1
OBJ_DEF: Final = 2
OBJ_MODEL: Final = 3
OBJ_ANIM: Final = 4
OBJ_PROP: Final = 5
OBJ_RGBA: Final = 6

PROP_UI_ENTRY: Final[str]
PROP_UI_COMBO: Final[str]
PROP_UI_RADIO: Final[str]
PROP_UI_CHECK: Final[str]
PROP_UI_SLIDE: Final[str]
PROP_UI_SPIN: Final[str]
PROP_UI_BLIND: Final[str]
PROP_UI_COMBO_DYNAMIC: Final[str]
PROP_UI_TIME: Final[str]

PROP_TYPE: Final = 0
PROP_DATATYPE: Final = 1
PROP_FUNC: Final = 2
PROP_DEFAULT: Final = 3
PROP_RANGE: Final = 4
PROP_DYNAMIC_KEY: Final = 5

PROP_MODEL: Final[str]

RANGE_MIN: Final = 0
RANGE_MAX: Final = 1
RANGE_RATE: Final = 2
FUNC_NAME: Final = 0
FUNC_ARGS: Final = 1
PROP_INT: Final = 0
PROP_BOOL: Final = 1
PROP_FLOAT: Final = 2
PROP_STR: Final = 3
PROP_BLIND: Final = 4

TYPE_CONV: Final[dict[Literal[0, 1, 2, 3], type]]

ARG_NAME: Final[str]
ARG_VAL: Final[str]
ARG_OBJ: Final[str]
ARG_NOLOADING: Final[str]
ARG_PARENT: Final[str]
