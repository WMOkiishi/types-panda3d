__all__ = []

from typing_extensions import Literal

defaultFont = ...
defaultFontFunc = ...
defaultClickSound = ...
defaultRolloverSound = ...
defaultDialogGeom = ...
defaultDialogRelief: Literal[0, 1, 2, 3, 4, 5, 6]
drawOrder: int
panel = ...

INITOPT: list[Literal['initopt']]

LMB: Literal[0]
MMB: Literal[1]
RMB: Literal[2]

NORMAL: Literal['normal']
DISABLED: Literal['disabled']

FLAT: Literal[1]
RAISED: Literal[2]
SUNKEN: Literal[3]
GROOVE: Literal[4]
RIDGE: Literal[5]
TEXTUREBORDER: Literal[6]
FrameStyleDict: dict[Literal['flat', 'raised', 'sunken', 'groove', 'ridge', 'texture_border'], Literal[1, 2, 3, 4, 5, 6]]

HORIZONTAL: Literal['horizontal']
VERTICAL: Literal['vertical']
VERTICAL_INVERTED: Literal['vertical_inverted']

DIALOG_NO: Literal[0]
DIALOG_OK: Literal[1]
DIALOG_YES: Literal[1]
DIALOG_RETRY: Literal[1]
DIALOG_CANCEL: Literal[-1]

DESTROY: Literal['destroy-']
PRINT: Literal['print-']
ENTER: str
EXIT: str
WITHIN: str
WITHOUT: str
B1CLICK: str
B2CLICK: str
B3CLICK: str
B1PRESS: str
B2PRESS: str
B3PRESS: str
B1RELEASE: str
B2RELEASE: str
B3RELEASE: str
OVERFLOW: str
ACCEPT: str
ACCEPTFAILED: str
TYPE: str
ERASE: str
CURSORMOVE: str
ADJUST: str

IMAGE_SORT_INDEX: Literal[10]
GEOM_SORT_INDEX: Literal[20]
TEXT_SORT_INDEX: Literal[30]
FADE_SORT_INDEX: Literal[1000]
NO_FADE_SORT_INDEX: Literal[2000]
BACKGROUND_SORT_INDEX: Literal[-100]
MIDGROUND_SORT_INDEX: Literal[0]
FOREGROUND_SORT_INDEX: Literal[100]

BUTTON_READY_STATE: Literal[0]
BUTTON_DEPRESSED_STATE: Literal[1]
BUTTON_ROLLOVER_STATE: Literal[2]
BUTTON_INACTIVE_STATE: Literal[3]

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
