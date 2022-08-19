from typing_extensions import Literal

from panda3d.core import BitMask_uint32_t_32, LPoint3f, LVector3f, NodePath

UNPICKABLE: list[str]

X_AXIS: LVector3f
Y_AXIS: LVector3f
Z_AXIS: LVector3f
NEG_X_AXIS: LVector3f
NEG_Y_AXIS: LVector3f
NEG_Z_AXIS: LVector3f
ZERO_VEC: LVector3f
ORIGIN: LVector3f
UNIT_VEC: LVector3f
ZERO_POINT: LPoint3f

DIRECT_FLASH_DURATION: float
MANIPULATION_MOVE_DELAY: float
Q_EPSILON: float

DIRECT_NO_MOD: Literal[0b000]
DIRECT_SHIFT_MOD: Literal[0b001]
DIRECT_CONTROL_MOD: Literal[0b010]
DIRECT_ALT_MOD: Literal[0b100]

SKIP_NONE: Literal[0b00000]
SKIP_HIDDEN: Literal[0b00001]
SKIP_BACKFACE: Literal[0b00010]
SKIP_CAMERA: Literal[0b00100]
SKIP_UNPICKABLE: Literal[0b01000]
SKIP_WIDGET: Literal[0b10000]
SKIP_ALL: Literal[0b11111]

EDIT_TYPE_UNMOVABLE: Literal[0b001]
EDIT_TYPE_UNSCALABLE: Literal[0b010]
EDIT_TYPE_UNROTATABLE: Literal[0b100]
EDIT_TYPE_UNEDITABLE: Literal[0b111]

LE_TOP_CAM_MASK: BitMask_uint32_t_32
LE_FRONT_CAM_MASK: BitMask_uint32_t_32
LE_LEFT_CAM_MASK: BitMask_uint32_t_32
LE_PERSP_CAM_MASK: BitMask_uint32_t_32
LE_CAM_MASKS: dict[Literal['persp', 'left', 'front', 'top'], BitMask_uint32_t_32]

def LE_showInAllCam(nodePath: NodePath) -> None: ...
def LE_showInOneCam(nodePath: NodePath, thisCamName: str) -> None: ...
