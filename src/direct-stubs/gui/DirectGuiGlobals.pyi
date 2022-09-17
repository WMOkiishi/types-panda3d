__all__: list[str] = []

from typing_extensions import Final, Literal

defaultFont = ...
defaultFontFunc = ...
defaultClickSound = ...
defaultRolloverSound = ...
defaultDialogGeom = ...
defaultDialogRelief: Literal[0, 1, 2, 3, 4, 5, 6]
drawOrder: int
panel = ...

INITOPT: Final[list[Literal['initopt']]]

LMB: Final[Literal[0]]
MMB: Final[Literal[1]]
RMB: Final[Literal[2]]

NORMAL: Final[Literal['normal']]
DISABLED: Final[Literal['disabled']]

FLAT: Final[Literal[1]]
RAISED: Final[Literal[2]]
SUNKEN: Final[Literal[3]]
GROOVE: Final[Literal[4]]
RIDGE: Final[Literal[5]]
TEXTUREBORDER: Final[Literal[6]]
FrameStyleDict: Final[dict[Literal['flat', 'raised', 'sunken', 'groove', 'ridge', 'texture_border'], Literal[1, 2, 3, 4, 5, 6]]]

HORIZONTAL: Final[Literal['horizontal']]
VERTICAL: Final[Literal['vertical']]
VERTICAL_INVERTED: Final[Literal['vertical_inverted']]

DIALOG_NO: Final[Literal[0]]
DIALOG_OK: Final[Literal[1]]
DIALOG_YES: Final[Literal[1]]
DIALOG_RETRY: Final[Literal[1]]
DIALOG_CANCEL: Final[Literal[-1]]

DESTROY: Final[Literal['destroy-']]
PRINT: Final[Literal['print-']]
ENTER: Final[str]
EXIT: Final[str]
WITHIN: Final[str]
WITHOUT: Final[str]
B1CLICK: Final[str]
B2CLICK: Final[str]
B3CLICK: Final[str]
B1PRESS: Final[str]
B2PRESS: Final[str]
B3PRESS: Final[str]
B1RELEASE: Final[str]
B2RELEASE: Final[str]
B3RELEASE: Final[str]
OVERFLOW: Final[str]
ACCEPT: Final[str]
ACCEPTFAILED: Final[str]
TYPE: Final[str]
ERASE: Final[str]
CURSORMOVE: Final[str]
ADJUST: Final[str]

IMAGE_SORT_INDEX: Final[Literal[10]]
GEOM_SORT_INDEX: Final[Literal[20]]
TEXT_SORT_INDEX: Final[Literal[30]]
FADE_SORT_INDEX: Final[Literal[1000]]
NO_FADE_SORT_INDEX: Final[Literal[2000]]
BACKGROUND_SORT_INDEX: Final[Literal[-100]]
MIDGROUND_SORT_INDEX: Final[Literal[0]]
FOREGROUND_SORT_INDEX: Final[Literal[100]]

BUTTON_READY_STATE: Final[Literal[0]]
BUTTON_DEPRESSED_STATE: Final[Literal[1]]
BUTTON_ROLLOVER_STATE: Final[Literal[2]]
BUTTON_INACTIVE_STATE: Final[Literal[3]]

def get_default_rolloverSound(): ...
def set_default_rolloverSound(newSound) -> None: ...
def get_default_click_sound(): ...
def set_default_click_sound(newSound) -> None: ...
def get_default_font(): ...
def set_default_font(newFont) -> None: ...
def set_default_font_func(newFontFunc) -> None: ...
def get_default_dialog_geom(): ...
def get_default_dialog_relief(): ...
def set_default_dialog_geom(newDialogGeom, relief=None) -> None: ...
def get_default_draw_order() -> int: ...
def set_default_draw_order(newDrawOrder: int) -> None: ...
def get_default_panel(): ...
def set_default_panel(newPanel): ...

getDefaultRolloverSound = get_default_rolloverSound
setDefaultRolloverSound = set_default_rolloverSound
getDefaultClickSound = get_default_click_sound
setDefaultClickSound = set_default_click_sound
getDefaultFont = get_default_font
setDefaultFont = set_default_font
setDefaultFontFunc = set_default_font_func
getDefaultDialogGeom = get_default_dialog_geom
getDefaultDialogRelief = get_default_dialog_relief
setDefaultDialogGeom = set_default_dialog_geom
getDefaultDrawOrder = get_default_draw_order
setDefaultDrawOrder = set_default_draw_order
getDefaultPanel = get_default_panel
setDefaultPanel = set_default_panel
