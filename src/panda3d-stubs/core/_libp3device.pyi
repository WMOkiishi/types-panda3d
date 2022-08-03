from collections.abc import Sequence
from enum import Enum
from typing import Any, ClassVar, Literal, TypeAlias, overload

_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]

class TrackerData:
    DtoolClassDict: ClassVar[dict[str, Any]]
    time: float
    pos: LPoint3f
    orient: LOrientationf
    dt: float

class InputDevice(TypedReferenceCount):
    class DeviceClass(Enum):
        unknown: int
        virtual_device: int
        keyboard: int
        mouse: int
        touch: int
        gamepad: int
        flight_stick: int
        steering_wheel: int
        dance_pad: int
        hmd: int
        spatial_mouse: int
        digitizer: int
    class Feature(Enum):
        pointer: int
        keyboard: int
        tracker: int
        vibration: int
        battery: int
    class Axis(Enum):
        none: int
        x: int
        y: int
        z: int
        yaw: int
        pitch: int
        roll: int
        left_x: int
        left_y: int
        left_trigger: int
        right_x: int
        right_y: int
        right_trigger: int
        throttle: int
        rudder: int
        wheel: int
        accelerator: int
        brake: int
        pressure: int
    class ButtonState:
        DtoolClassDict: ClassVar[dict[str, Any]]
        @property
        def known(self) -> bool: ...
        @property
        def pressed(self) -> bool: ...
        @property
        def handle(self) -> ButtonHandle: ...
        def __init__(self, __param0: InputDevice.ButtonState) -> None: ...
        def __bool__(self) -> bool: ...
    class AxisState:
        DtoolClassDict: ClassVar[dict[str, Any]]
        axis: InputDevice.Axis
        value: float
        known: bool
        def __init__(self, __param0: InputDevice.AxisState) -> None: ...
        def __bool__(self) -> bool: ...
    class BatteryData:
        DtoolClassDict: ClassVar[dict[str, Any]]
        level: int
        max_level: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, __param0: InputDevice.BatteryData) -> None: ...
    DtoolClassDict: ClassVar[dict[str, Any]]
    S_unknown: ClassVar[Literal[0]]
    S_up: ClassVar[Literal[1]]
    S_down: ClassVar[Literal[2]]
    @property
    def name(self) -> str: ...
    @property
    def manufacturer(self) -> str: ...
    @property
    def serial_number(self) -> str: ...
    @property
    def vendor_id(self) -> int: ...
    @property
    def product_id(self) -> int: ...
    @property
    def connected(self) -> bool: ...
    @property
    def device_class(self) -> InputDevice.DeviceClass: ...
    @property
    def tracker(self) -> TrackerData: ...
    @property
    def battery(self) -> InputDevice.BatteryData: ...
    @property
    def buttons(self) -> Sequence[InputDevice.ButtonState]: ...
    @property
    def axes(self) -> Sequence[InputDevice.AxisState]: ...
    @property
    def _pointer_data(self) -> PointerData: ...
    @property
    def _battery_data(self) -> InputDevice.BatteryData: ...
    @property
    def _tracker_data(self) -> TrackerData: ...
    def has_feature(self, feature: InputDevice.Feature) -> bool: ...
    def map_button(self, index: int, handle: ButtonHandle) -> None: ...
    def map_axis(self, index: int, axis: InputDevice.Axis) -> None: ...
    def find_button(self, handle: ButtonHandle) -> InputDevice.ButtonState: ...
    def find_axis(self, axis: InputDevice.Axis) -> InputDevice.AxisState: ...
    def set_vibration(self, strong: float, weak: float) -> None: ...
    def enable_pointer_events(self) -> None: ...
    def disable_pointer_events(self) -> None: ...
    def poll(self) -> None: ...
    def has_button_event(self) -> bool: ...
    def get_button_events(self) -> ButtonEventList: ...
    def has_pointer_event(self) -> bool: ...
    def get_pointer_events(self) -> PointerEventList: ...
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    hasFeature = has_feature
    mapButton = map_button
    mapAxis = map_axis
    findButton = find_button
    findAxis = find_axis
    setVibration = set_vibration
    enablePointerEvents = enable_pointer_events
    disablePointerEvents = disable_pointer_events
    hasButtonEvent = has_button_event
    getButtonEvents = get_button_events
    hasPointerEvent = has_pointer_event
    getPointerEvents = get_pointer_events
    getClassType = get_class_type
    SUnknown = S_unknown
    SUp = S_up
    SDown = S_down

class ClientBase(TypedReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def fork_asynchronous_thread(self, poll_time: float) -> bool: ...
    def is_forked(self) -> bool: ...
    def poll(self) -> bool: ...
    def get_last_poll_time(self) -> float: ...
    def set_coordinate_system(self, cs: _CoordinateSystem) -> None: ...
    def get_coordinate_system(self) -> _CoordinateSystem: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    forkAsynchronousThread = fork_asynchronous_thread
    isForked = is_forked
    getLastPollTime = get_last_poll_time
    setCoordinateSystem = set_coordinate_system
    getCoordinateSystem = get_coordinate_system
    getClassType = get_class_type

class AnalogNode(DataNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: AnalogNode) -> None: ...
    @overload
    def __init__(self, device: InputDevice) -> None: ...
    @overload
    def __init__(self, client: ClientBase, device_name: str) -> None: ...
    def is_valid(self) -> bool: ...
    def get_num_controls(self) -> int: ...
    def get_control_state(self, index: int) -> float: ...
    def is_control_known(self, index: int) -> bool: ...
    def set_output(self, channel: int, index: int, flip: bool) -> None: ...
    def clear_output(self, channel: int) -> None: ...
    def get_output(self, channel: int) -> int: ...
    def is_output_flipped(self, channel: int) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    isValid = is_valid
    getNumControls = get_num_controls
    getControlState = get_control_state
    isControlKnown = is_control_known
    setOutput = set_output
    clearOutput = clear_output
    getOutput = get_output
    isOutputFlipped = is_output_flipped
    getClassType = get_class_type

class ButtonNode(DataNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: ButtonNode) -> None: ...
    @overload
    def __init__(self, device: InputDevice) -> None: ...
    @overload
    def __init__(self, client: ClientBase, device_name: str) -> None: ...
    def is_valid(self) -> bool: ...
    def get_num_buttons(self) -> int: ...
    def set_button_map(self, index: int, button: ButtonHandle) -> None: ...
    def get_button_map(self, index: int) -> ButtonHandle: ...
    def get_button_state(self, index: int) -> bool: ...
    def is_button_known(self, index: int) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    isValid = is_valid
    getNumButtons = get_num_buttons
    setButtonMap = set_button_map
    getButtonMap = get_button_map
    getButtonState = get_button_state
    isButtonKnown = is_button_known
    getClassType = get_class_type

class DialNode(DataNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: DialNode) -> None: ...
    @overload
    def __init__(self, client: ClientBase, device_name: str) -> None: ...
    def is_valid(self) -> bool: ...
    def get_num_dials(self) -> int: ...
    def read_dial(self, index: int) -> float: ...
    def is_dial_known(self, index: int) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    isValid = is_valid
    getNumDials = get_num_dials
    readDial = read_dial
    isDialKnown = is_dial_known
    getClassType = get_class_type

class InputDeviceSet:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: InputDeviceSet) -> None: ...
    def __getitem__(self, index: int) -> InputDevice: ...
    def __len__(self) -> int: ...
    def assign(self, copy: InputDeviceSet) -> InputDeviceSet: ...
    def clear(self) -> None: ...
    def reserve(self, num: int) -> None: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...

class InputDeviceManager:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def get_devices(self) -> InputDeviceSet: ...
    @overload
    def get_devices(self, device_class: InputDevice.DeviceClass) -> InputDeviceSet: ...
    def add_device(self, device: InputDevice) -> None: ...
    def remove_device(self, device: InputDevice) -> None: ...
    def update(self) -> None: ...
    @staticmethod
    def get_global_ptr() -> InputDeviceManager: ...
    getDevices = get_devices
    addDevice = add_device
    removeDevice = remove_device
    getGlobalPtr = get_global_ptr

class InputDeviceNode(DataNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    device: InputDevice
    @overload
    def __init__(self, __param0: InputDeviceNode) -> None: ...
    @overload
    def __init__(self, device: InputDevice, name: str) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class TrackerNode(DataNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, device: InputDevice) -> None: ...
    @overload
    def __init__(self, __param0: TrackerNode) -> None: ...
    @overload
    def __init__(self, client: ClientBase, device_name: str) -> None: ...
    def is_valid(self) -> bool: ...
    def get_pos(self) -> LPoint3f: ...
    def get_orient(self) -> LOrientationf: ...
    def get_transform(self) -> LMatrix4f: ...
    def get_time(self) -> float: ...
    def has_time(self) -> bool: ...
    def set_tracker_coordinate_system(self, cs: _CoordinateSystem) -> None: ...
    def get_tracker_coordinate_system(self) -> _CoordinateSystem: ...
    def set_graph_coordinate_system(self, cs: _CoordinateSystem) -> None: ...
    def get_graph_coordinate_system(self) -> _CoordinateSystem: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    isValid = is_valid
    getPos = get_pos
    getOrient = get_orient
    getTransform = get_transform
    getTime = get_time
    hasTime = has_time
    setTrackerCoordinateSystem = set_tracker_coordinate_system
    getTrackerCoordinateSystem = get_tracker_coordinate_system
    setGraphCoordinateSystem = set_graph_coordinate_system
    getGraphCoordinateSystem = get_graph_coordinate_system
    getClassType = get_class_type

class VirtualMouse(DataNode):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: VirtualMouse) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def set_mouse_pos(self, x: int, y: int) -> None: ...
    def set_window_size(self, width: int, height: int) -> None: ...
    def set_mouse_on(self, flag: bool) -> None: ...
    def press_button(self, button: ButtonHandle) -> None: ...
    def release_button(self, button: ButtonHandle) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setMousePos = set_mouse_pos
    setWindowSize = set_window_size
    setMouseOn = set_mouse_on
    pressButton = press_button
    releaseButton = release_button
    getClassType = get_class_type