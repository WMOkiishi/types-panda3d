from _typeshed import StrOrBytesPath
from collections.abc import Callable, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias, final

from panda3d._typing import IntVec2Like, IntVec3Like, Vec4Like
from panda3d.core._device import InputDevice
from panda3d.core._dgraph import DataNode
from panda3d.core._dtoolbase import TypeHandle
from panda3d.core._dtoolutil import Filename, ostream
from panda3d.core._event import AsyncFuture
from panda3d.core._express import ReferenceCount, TypedReferenceCount
from panda3d.core._gobj import PreparedGraphicsObjects, Shader, Texture, TextureStage
from panda3d.core._gsgbase import GraphicsOutputBase, GraphicsStateGuardianBase
from panda3d.core._linmath import LColor, LPoint2i, LVecBase2i, LVecBase4, LVector2i
from panda3d.core._pgraph import CullResult, CullTraverser, Loader, NodePath, PandaNode, SceneSetup, ShaderAttrib, TextureAttrib
from panda3d.core._pgraphnodes import ShaderGenerator
from panda3d.core._pipeline import ReMutex, Thread
from panda3d.core._pnmimage import PNMImage
from panda3d.core._putil import ButtonHandle, ButtonMap, CallbackData, CallbackObject, DrawMask, MouseData, PointerData

_GraphicsStateGuardian_ShaderModel: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
_WindowProperties_MouseMode: TypeAlias = Literal[0, 1, 2]
_WindowProperties_ZOrder: TypeAlias = Literal[0, 1, 2]
_Lens_StereoChannel: TypeAlias = Literal[0, 1, 2, 3]
_DrawableRegion_RenderTexturePlane: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
_GraphicsOutput_RenderTextureMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_Texture_QualityLevel: TypeAlias = Literal[0, 1, 2, 3]
_CallbackGraphicsWindow_RenderCallbackType: TypeAlias = Literal[0, 1, 2, 3]
_GraphicsOutput_FrameMode: TypeAlias = Literal[0, 1, 2]

class GraphicsDevice(TypedReferenceCount):
    """An abstract device object that is part of Graphics Pipe.  This device is
    set to NULL for OpenGL. But DirectX uses it to take control of multiple
    windows under single device or multiple devices (i.e.  more than one
    adapters in the machine).
    """

    def get_pipe(self) -> GraphicsPipe:
        """Returns the GraphicsPipe that this device is associated with."""
    getPipe = get_pipe

class GraphicsPipe(TypedReferenceCount):
    """An object to create GraphicsOutputs that share a particular 3-D API.
    Normally, there will only be one GraphicsPipe in an application, although
    it is possible to have multiple of these at once if there are multiple
    different API's available in the same machine.

    Often, the GraphicsPipe corresponds to a physical output device, hence the
    term "pipe", but this is not necessarily the case.

    The GraphicsPipe is used by the GraphicsEngine object to create and destroy
    windows; it keeps ownership of the windows it creates.

    M. Asad added new/interim functionality where GraphicsPipe now contains a
    device interface to directx/opengl which will be used to handle multiple
    windows from same device.
    """

    OT_window: Final = 1
    OTWindow: Final = 1
    OT_fullscreen_window: Final = 2
    OTFullscreenWindow: Final = 2
    OT_buffer: Final = 4
    OTBuffer: Final = 4
    OT_texture_buffer: Final = 8
    OTTextureBuffer: Final = 8
    BF_refuse_parasite: Final = 1
    BFRefuseParasite: Final = 1
    BF_require_parasite: Final = 2
    BFRequireParasite: Final = 2
    BF_refuse_window: Final = 4
    BFRefuseWindow: Final = 4
    BF_require_window: Final = 8
    BFRequireWindow: Final = 8
    BF_require_callback_window: Final = 16
    BFRequireCallbackWindow: Final = 16
    BF_can_bind_color: Final = 64
    BFCanBindColor: Final = 64
    BF_can_bind_every: Final = 128
    BFCanBindEvery: Final = 128
    BF_resizeable: Final = 256
    BFResizeable: Final = 256
    BF_size_track_host: Final = 512
    BFSizeTrackHost: Final = 512
    BF_rtt_cumulative: Final = 1024
    BFRttCumulative: Final = 1024
    BF_fb_props_optional: Final = 2048
    BFFbPropsOptional: Final = 2048
    BF_size_square: Final = 4096
    BFSizeSquare: Final = 4096
    BF_size_power_2: Final = 8192
    BFSizePower2: Final = 8192
    BF_can_bind_layered: Final = 16384
    BFCanBindLayered: Final = 16384
    @property
    def display_width(self) -> int: ...
    @property
    def display_height(self) -> int: ...
    @property
    def display_zoom(self) -> float: ...
    @property
    def display_information(self) -> DisplayInformation: ...
    @property
    def interface_name(self) -> str: ...
    def is_valid(self) -> bool:
        """Returns false if this pipe is known to be invalid, meaning that an attempt
        to create a GraphicsWindow with the pipe will certainly fail.  Returns true
        if the pipe is probably valid (is this case, an attempt to create a
        GraphicsWindow should succeed, but might still fail).

        Use the GraphicsEngine class to create a GraphicsWindow on a particular
        pipe.
        """
    def get_supported_types(self) -> int:
        """Returns the mask of bits that represents the kinds of GraphicsOutput
        objects this pipe might be able to successfully create.  The return value
        is the union of bits in GraphicsPipe::OutputTypes that represents the set
        of GraphicsOutput types.

        A 1 bit in a particular position is not a guarantee of success, but a 0 bit
        is a guarantee of failure.
        """
    def supports_type(self, flags: int) -> bool:
        """A convenience function to ask if a particular type or types of
        GraphicsObjects are supported.  The parameter is a union of one or more
        bits defined in GrpahicsPipe::OutputTypes.

        Returns true if all of the requested types are listed in the
        supported_types mask, false if any one of them is not.  This is not a
        guarantee that the indicated output type will successfully be created when
        it is attempted.
        """
    def get_display_width(self) -> int:
        """Returns the width of the entire display, if it is known.  This may return
        0.  This is not a guarantee that windows (particularly fullscreen windows)
        may not be created larger than this width, but it is intended to provide a
        hint to the application.
        """
    def get_display_height(self) -> int:
        """Returns the height of the entire display, if it is known.  This may return
        0.  See the caveats for get_display_width().
        """
    def get_display_zoom(self) -> float:
        """Returns the display zoom factor configured in the operating system.  If the
        operating system automatically scales windows to match the DPI (such as when
        dpi-aware is set to false), this will be 1.0.  Otherwise, this will be set to
        a value approximating the density of the monitor divided by the standard
        density of the operating system (usually 96), yielding a value like 1.5 or
        2.0.

        @since 1.10.8
        """
    def get_display_information(self) -> DisplayInformation:
        """Gets the pipe's DisplayInformation."""
    def lookup_cpu_data(self) -> None:
        """Looks up the detailed CPU information and stores it in
        _display_information, if supported by the OS. This may take a second or
        two.
        """
    def get_interface_name(self) -> str: ...
    isValid = is_valid
    getSupportedTypes = get_supported_types
    supportsType = supports_type
    getDisplayWidth = get_display_width
    getDisplayHeight = get_display_height
    getDisplayZoom = get_display_zoom
    getDisplayInformation = get_display_information
    lookupCpuData = lookup_cpu_data
    getInterfaceName = get_interface_name

class DisplayInformation:
    """This class contains various display information."""

    DS_unknown: Final = 0
    DSUnknown: Final = 0
    DS_success: Final = 1
    DSSuccess: Final = 1
    DS_direct_3d_create_error: Final = 2
    DSDirect3dCreateError: Final = 2
    DS_create_window_error: Final = 3
    DSCreateWindowError: Final = 3
    DS_create_device_error: Final = 4
    DSCreateDeviceError: Final = 4
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: DisplayInformation = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_display_state(self) -> int: ...
    def get_maximum_window_width(self) -> int: ...
    def get_maximum_window_height(self) -> int: ...
    def get_window_bits_per_pixel(self) -> int: ...
    def get_total_display_modes(self) -> int: ...
    def get_display_mode(self, display_index: int) -> DisplayMode: ...
    def get_display_mode_width(self, display_index: int) -> int:
        """Older interface for display modes."""
    def get_display_mode_height(self, display_index: int) -> int: ...
    def get_display_mode_bits_per_pixel(self, display_index: int) -> int: ...
    def get_display_mode_refresh_rate(self, display_index: int) -> int: ...
    def get_display_mode_fullscreen_only(self, display_index: int) -> int: ...
    def get_shader_model(self) -> _GraphicsStateGuardian_ShaderModel: ...
    def get_video_memory(self) -> int: ...
    def get_texture_memory(self) -> int: ...
    def update_memory_information(self) -> None: ...
    def get_physical_memory(self) -> int: ...
    def get_available_physical_memory(self) -> int: ...
    def get_page_file_size(self) -> int: ...
    def get_available_page_file_size(self) -> int: ...
    def get_process_virtual_memory(self) -> int: ...
    def get_available_process_virtual_memory(self) -> int: ...
    def get_memory_load(self) -> int: ...
    def get_page_fault_count(self) -> int: ...
    def get_process_memory(self) -> int: ...
    def get_peak_process_memory(self) -> int: ...
    def get_page_file_usage(self) -> int: ...
    def get_peak_page_file_usage(self) -> int: ...
    def get_vendor_id(self) -> int: ...
    def get_device_id(self) -> int: ...
    def get_driver_product(self) -> int: ...
    def get_driver_version(self) -> int: ...
    def get_driver_sub_version(self) -> int: ...
    def get_driver_build(self) -> int: ...
    def get_driver_date_month(self) -> int: ...
    def get_driver_date_day(self) -> int: ...
    def get_driver_date_year(self) -> int: ...
    def get_cpu_vendor_string(self) -> str: ...
    def get_cpu_brand_string(self) -> str: ...
    def get_cpu_version_information(self) -> int: ...
    def get_cpu_brand_index(self) -> int: ...
    def get_cpu_frequency(self) -> int: ...
    @staticmethod
    def get_cpu_time() -> int:
        """Equivalent to the rdtsc processor instruction."""
    def get_maximum_cpu_frequency(self) -> int: ...
    def get_current_cpu_frequency(self) -> int: ...
    def update_cpu_frequency(self, processor_number: int) -> None: ...
    def get_num_cpu_cores(self) -> int:
        """Returns the number of individual CPU cores in the system, or 0 if this
        number is not available.  A hyperthreaded CPU counts once here.
        """
    def get_num_logical_cpus(self) -> int:
        """Returns the number of logical CPU's in the system, or 0 if this number is
        not available.  A hyperthreaded CPU counts as two or more here.
        """
    def get_os_version_major(self) -> int:
        """Returns -1 if not set."""
    def get_os_version_minor(self) -> int:
        """Returns -1 if not set."""
    def get_os_version_build(self) -> int:
        """Returns -1 if not set."""
    def get_os_platform_id(self) -> int:
        """Returns -1 if not set."""
    def get_display_modes(self) -> tuple[DisplayMode, ...]: ...
    getDisplayState = get_display_state
    getMaximumWindowWidth = get_maximum_window_width
    getMaximumWindowHeight = get_maximum_window_height
    getWindowBitsPerPixel = get_window_bits_per_pixel
    getTotalDisplayModes = get_total_display_modes
    getDisplayMode = get_display_mode
    getDisplayModeWidth = get_display_mode_width
    getDisplayModeHeight = get_display_mode_height
    getDisplayModeBitsPerPixel = get_display_mode_bits_per_pixel
    getDisplayModeRefreshRate = get_display_mode_refresh_rate
    getDisplayModeFullscreenOnly = get_display_mode_fullscreen_only
    getShaderModel = get_shader_model
    getVideoMemory = get_video_memory
    getTextureMemory = get_texture_memory
    updateMemoryInformation = update_memory_information
    getPhysicalMemory = get_physical_memory
    getAvailablePhysicalMemory = get_available_physical_memory
    getPageFileSize = get_page_file_size
    getAvailablePageFileSize = get_available_page_file_size
    getProcessVirtualMemory = get_process_virtual_memory
    getAvailableProcessVirtualMemory = get_available_process_virtual_memory
    getMemoryLoad = get_memory_load
    getPageFaultCount = get_page_fault_count
    getProcessMemory = get_process_memory
    getPeakProcessMemory = get_peak_process_memory
    getPageFileUsage = get_page_file_usage
    getPeakPageFileUsage = get_peak_page_file_usage
    getVendorId = get_vendor_id
    getDeviceId = get_device_id
    getDriverProduct = get_driver_product
    getDriverVersion = get_driver_version
    getDriverSubVersion = get_driver_sub_version
    getDriverBuild = get_driver_build
    getDriverDateMonth = get_driver_date_month
    getDriverDateDay = get_driver_date_day
    getDriverDateYear = get_driver_date_year
    getCpuVendorString = get_cpu_vendor_string
    getCpuBrandString = get_cpu_brand_string
    getCpuVersionInformation = get_cpu_version_information
    getCpuBrandIndex = get_cpu_brand_index
    getCpuFrequency = get_cpu_frequency
    getCpuTime = get_cpu_time
    getMaximumCpuFrequency = get_maximum_cpu_frequency
    getCurrentCpuFrequency = get_current_cpu_frequency
    updateCpuFrequency = update_cpu_frequency
    getNumCpuCores = get_num_cpu_cores
    getNumLogicalCpus = get_num_logical_cpus
    getOsVersionMajor = get_os_version_major
    getOsVersionMinor = get_os_version_minor
    getOsVersionBuild = get_os_version_build
    getOsPlatformId = get_os_platform_id
    getDisplayModes = get_display_modes

class DrawableRegion:
    """This is a base class for GraphicsWindow (actually, GraphicsOutput) and
    DisplayRegion, both of which are conceptually rectangular regions into
    which drawing commands may be issued.  Sometimes you want to deal with a
    single display region, and sometimes you want to deal with the whole window
    at once, particularly for issuing clear commands and capturing screenshots.
    """

    RTP_stencil: Final = 0
    RTPStencil: Final = 0
    RTP_depth_stencil: Final = 1
    RTPDepthStencil: Final = 1
    RTP_color: Final = 2
    RTPColor: Final = 2
    RTP_aux_rgba_0: Final = 3
    RTPAuxRgba0: Final = 3
    RTP_aux_rgba_1: Final = 4
    RTPAuxRgba1: Final = 4
    RTP_aux_rgba_2: Final = 5
    RTPAuxRgba2: Final = 5
    RTP_aux_rgba_3: Final = 6
    RTPAuxRgba3: Final = 6
    RTP_aux_hrgba_0: Final = 7
    RTPAuxHrgba0: Final = 7
    RTP_aux_hrgba_1: Final = 8
    RTPAuxHrgba1: Final = 8
    RTP_aux_hrgba_2: Final = 9
    RTPAuxHrgba2: Final = 9
    RTP_aux_hrgba_3: Final = 10
    RTPAuxHrgba3: Final = 10
    RTP_aux_float_0: Final = 11
    RTPAuxFloat0: Final = 11
    RTP_aux_float_1: Final = 12
    RTPAuxFloat1: Final = 12
    RTP_aux_float_2: Final = 13
    RTPAuxFloat2: Final = 13
    RTP_aux_float_3: Final = 14
    RTPAuxFloat3: Final = 14
    RTP_depth: Final = 15
    RTPDepth: Final = 15
    RTP_COUNT: Final = 16
    RTPCOUNT: Final = 16
    DtoolClassDict: ClassVar[dict[str, Any]]
    clear_color: LColor
    clear_depth: float
    clear_stencil: int
    pixel_zoom: float
    @property
    def pixel_factor(self) -> float: ...
    def set_clear_color_active(self, clear_color_active: bool) -> None:
        """Toggles the flag that indicates whether the color buffer should be cleared
        every frame.  If this is true, the color buffer will be cleared to the
        color indicated by set_clear_color(); otherwise, it will be left alone.
        """
    def get_clear_color_active(self) -> bool:
        """Returns the current setting of the flag that indicates whether the color
        buffer should be cleared every frame.  See set_clear_color_active().
        """
    def set_clear_depth_active(self, clear_depth_active: bool) -> None:
        """Toggles the flag that indicates whether the depth buffer should be cleared
        every frame.  If this is true, the depth buffer will be cleared to the
        depth value indicated by set_clear_depth(); otherwise, it will be left
        alone.
        """
    def get_clear_depth_active(self) -> bool:
        """Returns the current setting of the flag that indicates whether the depth
        buffer should be cleared every frame.  See set_clear_depth_active().
        """
    def set_clear_stencil_active(self, clear_stencil_active: bool) -> None:
        """Toggles the flag that indicates whether the stencil buffer should be
        cleared every frame.  If this is true, the stencil buffer will be cleared
        to the value indicated by set_clear_stencil(); otherwise, it will be left
        alone.
        """
    def get_clear_stencil_active(self) -> bool:
        """Returns the current setting of the flag that indicates whether the color
        buffer should be cleared every frame.  See set_clear_stencil_active().
        """
    def set_clear_color(self, color: Vec4Like) -> None:
        """Sets the clear color to the indicated value.  This is the value that will
        be used to clear the color buffer every frame, but only if
        get_clear_color_active() returns true.  If get_clear_color_active() returns
        false, this is meaningless.
        """
    def get_clear_color(self) -> LColor:
        """Returns the current clear color value.  This is the value that will be used
        to clear the color buffer every frame, but only if get_clear_color_active()
        returns true.  If get_clear_color_active() returns false, this is
        meaningless.
        """
    def set_clear_depth(self, depth: float) -> None:
        """Sets the clear depth to the indicated value.  This is the value that will
        be used to clear the depth buffer every frame, but only if
        get_clear_depth_active() returns true.  If get_clear_depth_active() returns
        false, this is meaningless.
        """
    def get_clear_depth(self) -> float:
        """Returns the current clear depth value.  This is the value that will be used
        to clear the depth buffer every frame, but only if get_clear_depth_active()
        returns true.  If get_clear_depth_active() returns false, this is
        meaningless.
        """
    def set_clear_stencil(self, stencil: int) -> None: ...
    def get_clear_stencil(self) -> int:
        """Returns the current clear stencil value.  This is the value that will be
        used to clear the stencil buffer every frame, but only if
        get_clear_stencil_active() returns true.  If get_clear_stencil_active()
        returns false, this is meaningless.
        """
    def set_clear_active(self, n: int, clear_aux_active: bool) -> None:
        """Sets the clear-active flag for any bitplane."""
    def get_clear_active(self, n: int) -> bool:
        """Gets the clear-active flag for any bitplane."""
    def set_clear_value(self, n: int, clear_value: Vec4Like) -> None:
        """Sets the clear value for any bitplane."""
    def get_clear_value(self, n: int) -> LColor:
        """Returns the clear value for any bitplane."""
    def disable_clears(self) -> None:
        """Disables both the color and depth clear.  See set_clear_color_active and
        set_clear_depth_active.
        """
    def is_any_clear_active(self) -> bool:
        """Returns true if any of the clear types (so far there are just color or
        depth) have been set active, or false if none of them are active and there
        is no need to clear.
        """
    def set_pixel_zoom(self, pixel_zoom: float) -> None:
        """Sets the amount by which the pixels of the region are scaled internally
        when filling the image interally.  Setting this number larger makes the
        pixels blockier, but may make the rendering faster, particularly for
        software renderers.  Setting this number to 2.0 reduces the number of
        pixels that have to be filled by the renderer by a factor of 2.0.  It
        doesn't make sense to set this lower than 1.0.

        It is possible to set this on either individual DisplayRegions or on
        overall GraphicsWindows, but you will get better performance for setting it
        on the window rather than its individual DisplayRegions.  Also, you may not
        set it on a DisplayRegion that doesn't have both clear_color() and
        clear_depth() enabled.

        This property is only supported on renderers for which it is particularly
        useful--currently, this is the tinydisplay software renderer.  Other kinds
        of renderers allow you to set this property, but ignore it.
        """
    def get_pixel_zoom(self) -> float:
        """Returns the value set by set_pixel_zoom(), regardless of whether it is
        being respected or not.  Also see get_pixel_factor().
        """
    def get_pixel_factor(self) -> float:
        """Returns the amount by which the height and width of the region will be
        scaled internally, based on the zoom factor set by set_pixel_zoom().  This
        will return 1.0 if the pixel_zoom was not set or if it is not being
        respected (for instance, because the underlying renderer doesn't support it
        --see supports_pixel_zoom).
        """
    def supports_pixel_zoom(self) -> bool:
        """Returns true if a call to set_pixel_zoom() will be respected, false if it
        will be ignored.  If this returns false, then get_pixel_factor() will
        always return 1.0, regardless of what value you specify for
        set_pixel_zoom().

        This may return false if the underlying renderer doesn't support pixel
        zooming, or if you have called this on a DisplayRegion that doesn't have
        both set_clear_color() and set_clear_depth() enabled.
        """
    @staticmethod
    def get_renderbuffer_type(plane: int) -> int:
        """Returns the RenderBuffer::Type that corresponds to a RenderTexturePlane."""
    setClearColorActive = set_clear_color_active
    getClearColorActive = get_clear_color_active
    setClearDepthActive = set_clear_depth_active
    getClearDepthActive = get_clear_depth_active
    setClearStencilActive = set_clear_stencil_active
    getClearStencilActive = get_clear_stencil_active
    setClearColor = set_clear_color
    getClearColor = get_clear_color
    setClearDepth = set_clear_depth
    getClearDepth = get_clear_depth
    setClearStencil = set_clear_stencil
    getClearStencil = get_clear_stencil
    setClearActive = set_clear_active
    getClearActive = get_clear_active
    setClearValue = set_clear_value
    getClearValue = get_clear_value
    disableClears = disable_clears
    isAnyClearActive = is_any_clear_active
    setPixelZoom = set_pixel_zoom
    getPixelZoom = get_pixel_zoom
    getPixelFactor = get_pixel_factor
    supportsPixelZoom = supports_pixel_zoom
    getRenderbufferType = get_renderbuffer_type

class WindowHandle(TypedReferenceCount):
    """This object represents a window on the desktop, not necessarily a Panda
    window.  This structure can be assigned to a WindowProperties to indicate a
    parent window.

    It also has callbacks so the Panda window can communicate with its parent
    window, which is particularly important when running embedded in a browser.

    To create a WindowHandle, you would usually call one of the
    NativeWindowHandle::make_*() methods, depending on the kind of native
    window handle object you already have.
    """

    class OSHandle(TypedReferenceCount):
        """This internal pointer within WindowHandle stores the actual OS-specific
        window handle type, whatever type that is.  It is subclassed for each OS.
        """

        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: WindowHandle.OSHandle) -> None: ...
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...
        def get_int_handle(self) -> int:
            """Returns the OS-specific handle converted to an integer, if this is possible
            for the particular representation.  Returns 0 if it is not.
            """
        def output(self, out: ostream) -> None: ...
        @staticmethod
        def get_class_type() -> TypeHandle: ...
        getIntHandle = get_int_handle
        getClassType = get_class_type

    os_handle: WindowHandle.OSHandle
    @overload
    def __init__(self, copy: WindowHandle) -> None: ...
    @overload
    def __init__(self, os_handle: WindowHandle.OSHandle) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_os_handle(self) -> WindowHandle.OSHandle:
        """Returns the OS-specific handle stored internally to the WindowHandle
        wrapper.
        """
    def set_os_handle(self, os_handle: WindowHandle.OSHandle) -> None:
        """Changes the OS-specific handle stored internally to the WindowHandle
        wrapper.
        """
    def send_windows_message(self, msg: int, wparam: int, lparam: int) -> None:
        """Call this method on a parent WindowHandle to deliver a Windows message to
        the current child window, if any.  This is used in the web plugin system to
        deliver button events detected directly by the browser system into Panda,
        which is particularly necessary on Vista.
        """
    def get_int_handle(self) -> int:
        """Returns the OS-specific handle converted to an integer, if this is possible
        for the particular representation.  Returns 0 if it is not.
        """
    def output(self, out: ostream) -> None: ...
    getOsHandle = get_os_handle
    setOsHandle = set_os_handle
    sendWindowsMessage = send_windows_message
    getIntHandle = get_int_handle

class WindowProperties:
    """A container for the various kinds of properties we might ask to have on a
    graphics window before we open it.  This also serves to hold the current
    properties for a window after it has been opened.
    """

    Z_bottom: Final = 0
    ZBottom: Final = 0
    Z_normal: Final = 1
    ZNormal: Final = 1
    Z_top: Final = 2
    ZTop: Final = 2
    M_absolute: Final = 0
    MAbsolute: Final = 0
    M_relative: Final = 1
    MRelative: Final = 1
    M_confined: Final = 2
    MConfined: Final = 2
    DtoolClassDict: ClassVar[dict[str, Any]]
    default: WindowProperties
    origin: LPoint2i
    size: LVector2i
    mouse_mode: _WindowProperties_MouseMode
    title: str
    undecorated: bool
    fixed_size: bool
    fullscreen: bool
    foreground: bool
    minimized: bool
    open: bool
    cursor_hidden: bool
    icon_filename: Filename
    cursor_filename: Filename
    z_order: _WindowProperties_ZOrder
    parent_window: WindowHandle
    @property
    def config_properties(self) -> WindowProperties: ...
    def __init__(self, *args, **kwds) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def assign(self, copy: Self) -> Self: ...
    @staticmethod
    def get_config_properties() -> WindowProperties:
        """Returns a WindowProperties structure with all of the default values filled
        in according to the user's config file.
        """
    @staticmethod
    def get_default() -> WindowProperties:
        """Returns the "default" WindowProperties.  If set_default() has been called,
        this returns that WindowProperties structure; otherwise, this returns
        get_config_properties().
        """
    @staticmethod
    def set_default(default_properties: WindowProperties) -> None:
        """Replaces the "default" WindowProperties with the specified structure.  The
        specified WindowProperties will be returned by future calls to
        get_default(), until clear_default() is called.

        Note that this completely replaces the default properties; it is not
        additive.
        """
    @staticmethod
    def clear_default() -> None:
        """Returns the "default" WindowProperties to whatever is specified in the
        user's config file.
        """
    def clear(self) -> None:
        """Unsets all properties that have been specified so far, and resets the
        WindowProperties structure to its initial empty state.
        """
    def is_any_specified(self) -> bool:
        """Returns true if any properties have been specified, false otherwise."""
    @overload
    def set_origin(self, origin: IntVec2Like) -> None:
        """Specifies the origin on the screen (in pixels, relative to the top-left
        corner) at which the window should appear.  This is the origin of the top-
        left corner of the useful part of the window, not including decorations.
        """
    @overload
    def set_origin(self, x_origin: int, y_origin: int) -> None: ...
    def get_origin(self) -> LPoint2i:
        """Returns the coordinates of the window's top-left corner, not including
        decorations.
        """
    def get_x_origin(self) -> int:
        """Returns the x coordinate of the window's top-left corner, not including
        decorations.
        """
    def get_y_origin(self) -> int:
        """Returns the y coordinate of the window's top-left corner, not including
        decorations.
        """
    def has_origin(self) -> bool:
        """Returns true if the window origin has been specified, false otherwise."""
    def clear_origin(self) -> None:
        """Removes the origin specification from the properties."""
    @overload
    def set_size(self, size: IntVec2Like) -> None:
        """Specifies the requested size of the window, in pixels.  This is the size of
        the useful part of the window, not including decorations.
        """
    @overload
    def set_size(self, x_size: int, y_size: int) -> None: ...
    def get_size(self) -> LVector2i:
        """Returns size in pixels of the useful part of the window, not including
        decorations.
        """
    def get_x_size(self) -> int:
        """Returns size in pixels in the x dimension of the useful part of the window,
        not including decorations.  That is, this is the window's width.
        """
    def get_y_size(self) -> int:
        """Returns size in pixels in the y dimension of the useful part of the window,
        not including decorations.  That is, this is the window's height.
        """
    def has_size(self) -> bool:
        """Returns true if the window size has been specified, false otherwise."""
    def clear_size(self) -> None:
        """Removes the size specification from the properties."""
    def has_mouse_mode(self) -> bool: ...
    def set_mouse_mode(self, mode: _WindowProperties_MouseMode) -> None:
        """Specifies the mode in which the window is to operate its mouse pointer.

        M_absolute: the normal mode in which a mouse pointer operates, where the
        mouse can move outside the window and the mouse coordinates are relative to
        its position in the window.

        M_relative (OSX or Unix/X11 only): a mode where only relative movements are
        reported; particularly useful for FPS-style mouse movements where you have
        hidden the mouse pointer and are are more interested in how fast the mouse
        is moving, rather than precisely where the pointer is hovering.

        This has no effect on Windows.  On Unix/X11, this requires the Xxf86dga
        extension to be available.

        M_confined: this mode reports absolute mouse positions, but confines the
        mouse pointer to the window boundary.  It can portably replace M_relative
        for an FPS, but you need to periodically move the pointer to the center of
        the window and track movement deltas.
        """
    def get_mouse_mode(self) -> _WindowProperties_MouseMode:
        """See set_mouse_mode()."""
    def clear_mouse_mode(self) -> None:
        """Removes the mouse_mode specification from the properties."""
    def set_title(self, title: str) -> None:
        """Specifies the title that should be assigned to the window."""
    def get_title(self) -> str:
        """Returns the window's title."""
    def has_title(self) -> bool:
        """Returns true if the window title has been specified, false otherwise."""
    def clear_title(self) -> None:
        """Removes the title specification from the properties."""
    def set_undecorated(self, undecorated: bool) -> None:
        """Specifies whether the window should be created with a visible title and
        border (false, the default) or not (true).
        """
    def get_undecorated(self) -> bool:
        """Returns true if the window has no border."""
    def has_undecorated(self) -> bool:
        """Returns true if set_undecorated() has been specified."""
    def clear_undecorated(self) -> None:
        """Removes the undecorated specification from the properties."""
    def set_fixed_size(self, fixed_size: bool) -> None:
        """Specifies whether the window should be resizable by the user."""
    def get_fixed_size(self) -> bool:
        """Returns true if the window cannot be resized by the user, false otherwise."""
    def has_fixed_size(self) -> bool:
        """Returns true if set_fixed_size() has been specified."""
    def clear_fixed_size(self) -> None:
        """Removes the fixed_size specification from the properties."""
    def set_fullscreen(self, fullscreen: bool) -> None:
        """Specifies whether the window should be opened in fullscreen mode (true) or
        normal windowed mode (false, the default).
        """
    def get_fullscreen(self) -> bool:
        """Returns true if the window is in fullscreen mode."""
    def has_fullscreen(self) -> bool:
        """Returns true if set_fullscreen() has been specified."""
    def clear_fullscreen(self) -> None:
        """Removes the fullscreen specification from the properties."""
    def set_foreground(self, foreground: bool) -> None:
        """Specifies whether the window should be opened in the foreground (true), or
        left in the background (false).
        """
    def get_foreground(self) -> bool:
        """Returns true if the window is in the foreground."""
    def has_foreground(self) -> bool:
        """Returns true if set_foreground() has been specified."""
    def clear_foreground(self) -> None:
        """Removes the foreground specification from the properties."""
    def set_minimized(self, minimized: bool) -> None:
        """Specifies whether the window should be created minimized (true), or normal
        (false).
        """
    def get_minimized(self) -> bool:
        """Returns true if the window is minimized."""
    def has_minimized(self) -> bool:
        """Returns true if set_minimized() has been specified."""
    def clear_minimized(self) -> None:
        """Removes the minimized specification from the properties."""
    def set_raw_mice(self, raw_mice: bool) -> None:
        """Specifies whether the window should read the raw mouse devices."""
    def get_raw_mice(self) -> bool:
        """Returns true if the window reads the raw mice."""
    def has_raw_mice(self) -> bool:
        """Returns true if set_raw_mice() has been specified."""
    def clear_raw_mice(self) -> None:
        """Removes the raw_mice specification from the properties."""
    def set_open(self, open: bool) -> None:
        """Specifies whether the window should be open.  It is legal to create a
        GraphicsWindow in the closed state, and later request it to open by
        changing this flag.
        """
    def get_open(self) -> bool:
        """Returns true if the window is open."""
    def has_open(self) -> bool:
        """Returns true if set_open() has been specified."""
    def clear_open(self) -> None:
        """Removes the open specification from the properties."""
    def set_cursor_hidden(self, cursor_hidden: bool) -> None:
        """Specifies whether the mouse cursor should be visible."""
    def get_cursor_hidden(self) -> bool:
        """Returns true if the mouse cursor is invisible."""
    def has_cursor_hidden(self) -> bool:
        """Returns true if set_cursor_hidden() has been specified."""
    def clear_cursor_hidden(self) -> None:
        """Removes the cursor_hidden specification from the properties."""
    def set_icon_filename(self, icon_filename: StrOrBytesPath) -> None:
        """Specifies the file that contains the icon to associate with the window when
        it is minimized.
        """
    def get_icon_filename(self) -> Filename:
        """Returns the icon filename associated with the window."""
    def has_icon_filename(self) -> bool:
        """Returns true if set_icon_filename() has been specified."""
    def clear_icon_filename(self) -> None:
        """Removes the icon_filename specification from the properties."""
    def set_cursor_filename(self, cursor_filename: StrOrBytesPath) -> None:
        """Specifies the file that contains the icon to associate with the mouse
        cursor when it is within the window (and visible).
        """
    def get_cursor_filename(self) -> Filename:
        """Returns the icon filename associated with the mouse cursor."""
    def has_cursor_filename(self) -> bool:
        """Returns true if set_cursor_filename() has been specified."""
    def clear_cursor_filename(self) -> None:
        """Removes the cursor_filename specification from the properties."""
    def set_z_order(self, z_order: _WindowProperties_ZOrder) -> None:
        """Specifies the relative ordering of the window with respect to other
        windows.  If the z_order is Z_top, the window will always be on top of
        other windows; if it is Z_bottom, it will always be below other windows.
        Most windows will want to be Z_normal, which allows the user to control the
        order.
        """
    def get_z_order(self) -> _WindowProperties_ZOrder:
        """Returns the window's z_order."""
    def has_z_order(self) -> bool:
        """Returns true if the window z_order has been specified, false otherwise."""
    def clear_z_order(self) -> None:
        """Removes the z_order specification from the properties."""
    @overload
    def set_parent_window(self, parent_window: WindowHandle | WindowHandle.OSHandle = ...) -> None:
        """`(self, parent_window: WindowHandle = ...)`:
        Specifies the window that this window should be attached to.  If this is
        NULL or unspecified, the window will be created as a toplevel window on the
        desktop; if this is non-NULL, the window will be bound as a child window to
        the indicated parent window.

        You should use GraphicsPipe::make_window_handle() to create an instance of
        a WindowHandle object given an appropriate OS-specific window handle
        representation.  Each OS-specific GraphicsPipe class defines a
        make_window_handle() method that returns an appropriate WindowHandle object
        to wrap the particular OS-specific representation.

        `(self, parent: int)`:
        Specifies the window that this window should be attached to.

        This is a deprecated variant on this method, and exists only for backward
        compatibility.  Future code should use the version of set_parent_window()
        below that receives a WindowHandle object; that interface is much more
        robust.

        In this deprecated variant, the actual value for "parent" is platform-
        specific.  On Windows, it is the HWND of the parent window, cast to an
        unsigned integer.  On X11, it is the Window pointer of the parent window,
        similarly cast.  On OSX, this is the NSWindow pointer, which doesn't appear
        to work at all.
        """
    @overload
    def set_parent_window(self, parent: int) -> None: ...
    def get_parent_window(self) -> WindowHandle:
        """Returns the parent window specification, or NULL if there is no parent
        window specified.
        """
    def has_parent_window(self) -> bool:
        """Checks the S_parent_window specification from the properties."""
    def clear_parent_window(self) -> None:
        """Removes the S_parent_window specification from the properties."""
    def add_properties(self, other: WindowProperties) -> None:
        """Sets any properties that are explicitly specified in other on this object.
        Leaves other properties unchanged.
        """
    def output(self, out: ostream) -> None:
        """Sets any properties that are explicitly specified in other on this object.
        Leaves other properties unchanged.
        """
    getConfigProperties = get_config_properties
    getDefault = get_default
    setDefault = set_default
    clearDefault = clear_default
    isAnySpecified = is_any_specified
    setOrigin = set_origin
    getOrigin = get_origin
    getXOrigin = get_x_origin
    getYOrigin = get_y_origin
    hasOrigin = has_origin
    clearOrigin = clear_origin
    setSize = set_size
    getSize = get_size
    getXSize = get_x_size
    getYSize = get_y_size
    hasSize = has_size
    clearSize = clear_size
    hasMouseMode = has_mouse_mode
    setMouseMode = set_mouse_mode
    getMouseMode = get_mouse_mode
    clearMouseMode = clear_mouse_mode
    setTitle = set_title
    getTitle = get_title
    hasTitle = has_title
    clearTitle = clear_title
    setUndecorated = set_undecorated
    getUndecorated = get_undecorated
    hasUndecorated = has_undecorated
    clearUndecorated = clear_undecorated
    setFixedSize = set_fixed_size
    getFixedSize = get_fixed_size
    hasFixedSize = has_fixed_size
    clearFixedSize = clear_fixed_size
    setFullscreen = set_fullscreen
    getFullscreen = get_fullscreen
    hasFullscreen = has_fullscreen
    clearFullscreen = clear_fullscreen
    setForeground = set_foreground
    getForeground = get_foreground
    hasForeground = has_foreground
    clearForeground = clear_foreground
    setMinimized = set_minimized
    getMinimized = get_minimized
    hasMinimized = has_minimized
    clearMinimized = clear_minimized
    setRawMice = set_raw_mice
    getRawMice = get_raw_mice
    hasRawMice = has_raw_mice
    clearRawMice = clear_raw_mice
    setOpen = set_open
    getOpen = get_open
    hasOpen = has_open
    clearOpen = clear_open
    setCursorHidden = set_cursor_hidden
    getCursorHidden = get_cursor_hidden
    hasCursorHidden = has_cursor_hidden
    clearCursorHidden = clear_cursor_hidden
    setIconFilename = set_icon_filename
    getIconFilename = get_icon_filename
    hasIconFilename = has_icon_filename
    clearIconFilename = clear_icon_filename
    setCursorFilename = set_cursor_filename
    getCursorFilename = get_cursor_filename
    hasCursorFilename = has_cursor_filename
    clearCursorFilename = clear_cursor_filename
    setZOrder = set_z_order
    getZOrder = get_z_order
    hasZOrder = has_z_order
    clearZOrder = clear_z_order
    setParentWindow = set_parent_window
    getParentWindow = get_parent_window
    hasParentWindow = has_parent_window
    clearParentWindow = clear_parent_window
    addProperties = add_properties

class DisplayRegion(TypedReferenceCount, DrawableRegion):
    """A rectangular subregion within a window for rendering into.  Typically,
    there is one DisplayRegion that covers the whole window, but you may also
    create smaller DisplayRegions for having different regions within the
    window that represent different scenes.  You may also stack up
    DisplayRegions like panes of glass, usually for layering 2-d interfaces on
    top of a 3-d scene.
    """

    dimensions: LVecBase4
    camera: NodePath
    active: bool
    sort: int
    stereo_channel: _Lens_StereoChannel
    tex_view_offset: int
    incomplete_render: bool
    texture_reload_priority: int
    lens_index: int
    cull_traverser: CullTraverser
    target_tex_page: int
    scissor_enabled: bool
    cull_callback: CallbackObject
    draw_callback: CallbackObject
    @property
    def window(self) -> GraphicsOutput: ...
    @property
    def pipe(self) -> GraphicsPipe: ...
    @property
    def stereo(self) -> bool: ...
    @property
    def pixel_size(self) -> LVecBase2i: ...
    def upcast_to_TypedReferenceCount(self) -> TypedReferenceCount: ...
    def upcast_to_DrawableRegion(self) -> DrawableRegion: ...
    def get_num_regions(self) -> int:
        """Returns the number of regions, see set_num_regions."""
    def set_num_regions(self, i: int) -> None:
        """Sets the number of regions that this DisplayRegion indicates.  Usually,
        this number is 1 (and it is always at least 1), and only the first is used
        for rendering.  However, if more than one is provided, you may select which
        one to render into using a geometry shader (gl_ViewportIndex in GLSL).
        """
    def get_dimensions(self, i: int = ...) -> LVecBase4:
        """Retrieves the coordinates of the DisplayRegion's rectangle within its
        GraphicsOutput.  These numbers will be in the range [0..1].
        """
    def get_left(self, i: int = ...) -> float:
        """Retrieves the x coordinate of the left edge of the rectangle within its
        GraphicsOutput.  This number will be in the range [0..1].
        """
    def get_right(self, i: int = ...) -> float:
        """Retrieves the x coordinate of the right edge of the rectangle within its
        GraphicsOutput.  This number will be in the range [0..1].
        """
    def get_bottom(self, i: int = ...) -> float:
        """Retrieves the y coordinate of the bottom edge of the rectangle within its
        GraphicsOutput.  This number will be in the range [0..1].
        """
    def get_top(self, i: int = ...) -> float:
        """Retrieves the y coordinate of the top edge of the rectangle within its
        GraphicsOutput.  This number will be in the range [0..1].
        """
    @overload
    def set_dimensions(self, dimensions: Vec4Like) -> None:
        """`(self, dimensions: LVecBase4)`; `(self, l: float, r: float, b: float, t: float)`; `(self, i: int, l: float, r: float, b: float, t: float)`:
        Changes the portion of the framebuffer this DisplayRegion corresponds to.
        The parameters range from 0 to 1, where 0,0 is the lower left corner and
        1,1 is the upper right; (0, 1, 0, 1) represents the whole screen.

        `(self, i: int, dimensions: LVecBase4)`:
        Changes the portion of the framebuffer this DisplayRegion corresponds to.
        The parameters range from 0 to 1, where 0,0 is the lower left corner and
        1,1 is the upper right; (0, 1, 0, 1) represents the whole screen.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    @overload
    def set_dimensions(self, i: int, dimensions: Vec4Like) -> None: ...
    @overload
    def set_dimensions(self, l: float, r: float, b: float, t: float) -> None: ...
    @overload
    def set_dimensions(self, i: int, l: float, r: float, b: float, t: float) -> None: ...
    def get_window(self) -> GraphicsOutput:
        """Returns the GraphicsOutput that this DisplayRegion is ultimately associated
        with, or NULL if no window is associated.
        """
    def get_pipe(self) -> GraphicsPipe:
        """Returns the GraphicsPipe that this DisplayRegion is ultimately associated
        with, or NULL if no pipe is associated.
        """
    def is_stereo(self) -> bool:
        """Returns true if this is a StereoDisplayRegion, false otherwise."""
    def set_camera(self, camera: NodePath) -> None:
        """Sets the camera that is associated with this DisplayRegion.  There is a
        one-to-many association between cameras and DisplayRegions; one camera may
        be shared by multiple DisplayRegions.

        The camera is actually set via a NodePath, which clarifies which instance
        of the camera (if there happen to be multiple instances) we should use.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_camera(self, current_thread: Thread = ...) -> NodePath:
        """Returns the camera associated with this DisplayRegion, or an empty NodePath
        if no camera is associated.
        """
    def set_active(self, active: bool) -> None:
        """Sets the active flag associated with the DisplayRegion.  If the
        DisplayRegion is marked inactive, nothing is rendered.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def is_active(self) -> bool:
        """Returns the active flag associated with the DisplayRegion."""
    def set_sort(self, sort: int) -> None:
        """Sets the sort value associated with the DisplayRegion.  Within a window,
        DisplayRegions will be rendered in order from the lowest sort value to the
        highest.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_sort(self) -> int:
        """Returns the sort value associated with the DisplayRegion."""
    def set_stereo_channel(self, stereo_channel: _Lens_StereoChannel) -> None:
        """Specifies whether the DisplayRegion represents the left or right channel of
        a stereo pair, or whether it is a normal, monocular image.  This
        automatically adjusts the lens that is used to render to this DisplayRegion
        to its left or right eye, according to the lens's stereo properties.

        When the DisplayRegion is attached to a stereo window (one for which
        is_stereo() returns true), this also specifies which physical channel the
        DisplayRegion renders to.

        Normally you would create at least two DisplayRegions for a stereo window,
        one for each of the left and right channels.  The two DisplayRegions may
        share the same camera (and thus the same lens); this parameter is used to
        control the exact properties of the lens when it is used to render into
        this DisplayRegion.

        Also see the StereoDisplayRegion, which automates managing a pair of
        left/right DisplayRegions.

        An ordinary DisplayRegion may be set to SC_mono, SC_left, or SC_right.  You
        may set SC_stereo only on a StereoDisplayRegion.

        This call also resets tex_view_offset to its default value, which is 0 for
        the left eye or 1 for the right eye of a stereo display region, or 0 for a
        mono display region.
        """
    def get_stereo_channel(self) -> _Lens_StereoChannel:
        """Returns whether the DisplayRegion is specified as the left or right channel
        of a stereo pair, or whether it is a normal, monocular image.  See
        set_stereo_channel().
        """
    def set_tex_view_offset(self, tex_view_offset: int) -> None:
        """Sets the current texture view offset for this DisplayRegion.  This is
        normally set to zero.  If nonzero, it is used to select a particular view
        of any multiview textures that are rendered within this DisplayRegion.

        For a StereoDisplayRegion, this is normally 0 for the left eye, and 1 for
        the right eye, to support stereo textures.  This is set automatically when
        you call set_stereo_channel().
        """
    def get_tex_view_offset(self) -> int:
        """Returns the current texture view offset for this DisplayRegion.  This is
        normally set to zero.  If nonzero, it is used to select a particular view
        of any multiview textures that are rendered within this DisplayRegion.

        For a StereoDisplayRegion, this is normally 0 for the left eye, and 1 for
        the right eye, to support stereo textures.
        """
    def set_incomplete_render(self, incomplete_render: bool) -> None:
        """Sets the incomplete_render flag.  When this is true, the frame will be
        rendered even if some of the geometry or textures in the scene are not
        available (e.g.  they have been temporarily paged out).  When this is
        false, the frame will be held up while this data is reloaded.

        This flag may also be set on the GraphicsStateGuardian.  It will be
        considered true for a given DisplayRegion only if it is true on both the
        GSG and on the DisplayRegion.

        See GraphicsStateGuardian::set_incomplete_render() for more detail.
        """
    def get_incomplete_render(self) -> bool:
        """Returns the incomplete_render flag.  See set_incomplete_render()."""
    def set_texture_reload_priority(self, texture_reload_priority: int) -> None:
        """Specifies an integer priority which is assigned to any asynchronous texture
        reload requests spawned while processing this DisplayRegion.  This controls
        which textures are loaded first when multiple textures need to be reloaded
        at once; it also controls the relative priority between asynchronous
        texture loads and asynchronous model or animation loads.

        Specifying a larger number here makes the textures rendered by this
        DisplayRegion load up first.  This may be particularly useful to do, for
        instance, for the DisplayRegion that renders the gui.
        """
    def get_texture_reload_priority(self) -> int:
        """Returns the priority which is assigned to asynchronous texture reload
        requests.  See set_texture_reload_priority().
        """
    def set_lens_index(self, index: int) -> None:
        """Sets the lens index, allows for multiple lenses to be attached to a camera.
        This is useful for a variety of setups, such as fish eye rendering.  The
        default is 0.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_lens_index(self) -> int:
        """Returns the specific lens of the associated Camera that will be used for
        rendering this scene.  Most Cameras hold only one lens, but for multiple
        lenses this method may be used to selected between them.
        """
    def set_cull_traverser(self, trav: CullTraverser) -> None:
        """Specifies the CullTraverser that will be used to draw the contents of this
        DisplayRegion.  Normally the default CullTraverser is sufficient, but this
        may be changed to change the default cull behavior.
        """
    def get_cull_traverser(self) -> CullTraverser:
        """Returns the CullTraverser that will be used to draw the contents of this
        DisplayRegion.
        """
    def set_cube_map_index(self, cube_map_index: int) -> None:
        """Deprecated; replaced by set_target_tex_page()."""
    def set_target_tex_page(self, page: int) -> None:
        """This is a special parameter that is only used when rendering the faces of a
        cube map or multipage and/or multiview texture.

        This sets up the DisplayRegion to render to the ith page and jth view of
        its associated texture(s); the value must be consistent with the range of
        values availble to the texture.  A normal DisplayRegion that is not
        associated with any particular page should be set to page -1 and view 0.

        This is particularly useful when rendering cube maps and/or stereo
        textures.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_target_tex_page(self) -> int:
        """Returns the target page number associated with this particular
        DisplayRegion, or -1 if it is not associated with a page.  See
        set_target_tex_page().
        """
    def set_scissor_enabled(self, scissor_enabled: bool) -> None:
        """Sets whether or not scissor testing is enabled for this region.  The
        default is true, except for the overlay display region.
        """
    def get_scissor_enabled(self) -> bool:
        """Returns whether or not scissor testing is enabled for this region.  The
        default is true, except for the overlay display region.
        """
    def set_cull_callback(self, object: Callable | CallbackObject) -> None:
        """Sets the CallbackObject that will be notified when the DisplayRegion is
        visited during the cull traversal.  This callback will be made during the
        cull thread.

        The cull traversal is responsible for determining which nodes are visible
        and within the view frustum, and for accumulating state and transform, and
        generally building up the list of CullableObjects that are to be eventually
        passed to the draw traversal for rendering.

        At the time the cull traversal callback is made, the traversal for this
        DisplayRegion has not yet started.

        The callback is passed an instance of a DisplayRegionCullCallbackData,
        which contains pointers to the current scene information, as well as the
        current DisplayRegion and GSG.  The callback *replaces* the normal cull
        behavior, so if your callback does nothing, the scene graph will not be
        traversed and therefore nothing will be drawn.  If you wish the normal cull
        traversal to be performed for this DisplayRegion, you must call
        cbdata->upcall() from your callback.
        """
    def clear_cull_callback(self) -> None:
        """Removes the callback set by an earlier call to set_cull_callback()."""
    def get_cull_callback(self) -> CallbackObject:
        """Returns the CallbackObject set by set_cull_callback()."""
    def set_draw_callback(self, object: Callable | CallbackObject) -> None:
        """Sets the CallbackObject that will be notified when the contents of
        DisplayRegion is drawn during the draw traversal.  This callback will be
        made during the draw thread.

        The draw traversal is responsible for actually issuing the commands to the
        graphics engine to draw primitives.  Its job is to walk through the list of
        CullableObjects build up by the cull traversal, as quickly as possible,
        issuing the appropriate commands to draw each one.

        At the time the draw traversal callback is made, the graphics state is in
        the initial state, and no projection matrix or modelview matrix is in
        effect.  begin_scene() has not yet been called, and no objects have yet
        been drawn.  However, the viewport has already been set to the appropriate
        part of the window, and the clear commands for this DisplayRegion (if any)
        have been issued.

        The callback is passed an instance of a DisplayRegionDrawCallbackData,
        which contains pointers to the current scene information, as well as the
        current DisplayRegion and GSG.  The callback *replaces* the normal draw
        behavior, so if your callback does nothing, nothing in the DisplayRegion
        will be drawn.  If you wish the draw traversal to continue to draw the
        contents of this DisplayRegion, you must call cbdata->upcall() from your
        callback.
        """
    def clear_draw_callback(self) -> None:
        """Removes the callback set by an earlier call to set_draw_callback()."""
    def get_draw_callback(self) -> CallbackObject:
        """Returns the CallbackObject set by set_draw_callback()."""
    def get_pixel_width(self, i: int = ...) -> int:
        """Returns the width of the DisplayRegion in pixels."""
    def get_pixel_height(self, i: int = ...) -> int:
        """Returns the height of the DisplayRegion in pixels."""
    def get_pixel_size(self, i: int = ...) -> LVecBase2i:
        """Returns the size of the DisplayRegion in pixels."""
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def make_screenshot_filename(prefix: str = ...) -> Filename:
        """Synthesizes a suitable default filename for passing to save_screenshot().

        The default filename is generated from the supplied prefix and from the
        Config variable screenshot-filename, which contains the following strings:

        %~p - the supplied prefix %~f - the frame count %~e - the value of
        screenshot-extension All other % strings in strftime().
        """
    def save_screenshot_default(self, prefix: str = ...) -> Filename:
        """Saves a screenshot of the region to a default filename, and returns the
        filename, or empty string if the screenshot failed.  The filename is
        generated by make_screenshot_filename().
        """
    def save_screenshot(self, filename: StrOrBytesPath, image_comment: str = ...) -> bool:
        """Saves a screenshot of the region to the indicated filename.  Returns true
        on success, false on failure.
        """
    @overload
    def get_screenshot(self) -> Texture:
        """`(self)`:
        Captures the most-recently rendered image from the framebuffer and returns
        it as a Texture, or NULL on failure.

        `(self, image: PNMImage)`:
        Captures the most-recently rendered image from the framebuffer into the
        indicated PNMImage.  Returns true on success, false on failure.
        """
    @overload
    def get_screenshot(self, image: PNMImage) -> bool: ...
    def clear_cull_result(self) -> None: ...
    def make_cull_result_graph(self) -> PandaNode:
        """Returns a special scene graph constructed to represent the results of the
        last frame's cull operation.

        This will be a hierarchy of nodes, one node for each bin, each of which
        will in term be a parent of a number of GeomNodes, representing the
        geometry drawn in each bin.

        This is useful mainly for high-level debugging and abstraction tools; it
        should not be mistaken for the low-level cull result itself, which is
        constructed and maintained internally.  No such scene graph is normally
        constructed during the rendering of a frame; this is an artificial
        construct created for the purpose of making it easy to analyze the results
        of the cull operation.
        """
    upcastToTypedReferenceCount = upcast_to_TypedReferenceCount
    upcastToDrawableRegion = upcast_to_DrawableRegion
    getNumRegions = get_num_regions
    setNumRegions = set_num_regions
    getDimensions = get_dimensions
    getLeft = get_left
    getRight = get_right
    getBottom = get_bottom
    getTop = get_top
    setDimensions = set_dimensions
    getWindow = get_window
    getPipe = get_pipe
    isStereo = is_stereo
    setCamera = set_camera
    getCamera = get_camera
    setActive = set_active
    isActive = is_active
    setSort = set_sort
    getSort = get_sort
    setStereoChannel = set_stereo_channel
    getStereoChannel = get_stereo_channel
    setTexViewOffset = set_tex_view_offset
    getTexViewOffset = get_tex_view_offset
    setIncompleteRender = set_incomplete_render
    getIncompleteRender = get_incomplete_render
    setTextureReloadPriority = set_texture_reload_priority
    getTextureReloadPriority = get_texture_reload_priority
    setLensIndex = set_lens_index
    getLensIndex = get_lens_index
    setCullTraverser = set_cull_traverser
    getCullTraverser = get_cull_traverser
    setCubeMapIndex = set_cube_map_index
    setTargetTexPage = set_target_tex_page
    getTargetTexPage = get_target_tex_page
    setScissorEnabled = set_scissor_enabled
    getScissorEnabled = get_scissor_enabled
    setCullCallback = set_cull_callback
    clearCullCallback = clear_cull_callback
    getCullCallback = get_cull_callback
    setDrawCallback = set_draw_callback
    clearDrawCallback = clear_draw_callback
    getDrawCallback = get_draw_callback
    getPixelWidth = get_pixel_width
    getPixelHeight = get_pixel_height
    getPixelSize = get_pixel_size
    makeScreenshotFilename = make_screenshot_filename
    saveScreenshotDefault = save_screenshot_default
    saveScreenshot = save_screenshot
    getScreenshot = get_screenshot
    clearCullResult = clear_cull_result
    makeCullResultGraph = make_cull_result_graph

class GraphicsOutput(GraphicsOutputBase, DrawableRegion):
    """This is a base class for the various different classes that represent the
    result of a frame of rendering.  The most common kind of GraphicsOutput is
    a GraphicsWindow, which is a real-time window on the desktop, but another
    example is GraphicsBuffer, which is an offscreen buffer.

    The actual rendering, and anything associated with the graphics context
    itself, is managed by the associated GraphicsStateGuardian (which might
    output to multiple GraphicsOutput objects).

    GraphicsOutputs are not actually writable to bam files, of course, but they
    may be passed as event parameters, so they inherit from
    TypedWritableReferenceCount instead of TypedReferenceCount for that
    convenience.
    """

    RTM_none: Final = 0
    RTMNone: Final = 0
    RTM_bind_or_copy: Final = 1
    RTMBindOrCopy: Final = 1
    RTM_copy_texture: Final = 2
    RTMCopyTexture: Final = 2
    RTM_copy_ram: Final = 3
    RTMCopyRam: Final = 3
    RTM_triggered_copy_texture: Final = 4
    RTMTriggeredCopyTexture: Final = 4
    RTM_triggered_copy_ram: Final = 5
    RTMTriggeredCopyRam: Final = 5
    RTM_bind_layered: Final = 6
    RTMBindLayered: Final = 6
    FM_render: Final = 0
    FMRender: Final = 0
    FM_parasite: Final = 1
    FMParasite: Final = 1
    FM_refresh: Final = 2
    FMRefresh: Final = 2
    active: bool
    one_shot: bool
    inverted: bool
    swap_eyes: bool
    sort: int
    child_sort: int
    @property
    def gsg(self) -> GraphicsStateGuardian: ...
    @property
    def pipe(self) -> GraphicsPipe: ...
    @property
    def engine(self) -> GraphicsEngine: ...
    @property
    def name(self) -> str: ...
    @property
    def size(self) -> LVecBase2i: ...
    @property
    def fb_size(self) -> LVecBase2i: ...
    @property
    def sbs_left_size(self) -> LVecBase2i: ...
    @property
    def sbs_right_size(self) -> LVecBase2i: ...
    @property
    def display_regions(self) -> Sequence[DisplayRegion]: ...
    @property
    def active_display_regions(self) -> Sequence[DisplayRegion]: ...
    @property
    def supports_render_texture(self) -> bool: ...
    def upcast_to_GraphicsOutputBase(self) -> GraphicsOutputBase: ...
    def upcast_to_DrawableRegion(self) -> DrawableRegion: ...
    def get_gsg(self) -> GraphicsStateGuardian:
        """Returns the GSG that is associated with this window.  There is a one-to-one
        association between windows and GSG's.

        This may return NULL if the graphics context has not yet been created for
        the window, e.g.  before the first frame has rendered; or after the window
        has been closed.
        """
    def get_pipe(self) -> GraphicsPipe:
        """Returns the GraphicsPipe that this window is associated with.  It is
        possible that the GraphicsPipe might have been deleted while an outstanding
        PT(GraphicsOutput) prevented all of its children windows from also being
        deleted; in this unlikely case, get_pipe() may return NULL.
        """
    def get_engine(self) -> GraphicsEngine:
        """Returns the graphics engine that created this output.  Since there is
        normally only one GraphicsEngine object in an application, this is usually
        the same as the global GraphicsEngine.
        """
    def get_name(self) -> str:
        """Returns the name that was passed to the GraphicsOutput constructor."""
    def count_textures(self) -> int:
        """If the GraphicsOutput is set to render into a texture, returns the number
        of textures that are being rendered into.  Normally, the textures would be
        associated with different buffers - a color texture, a depth texture, and a
        stencil texture.
        """
    def has_texture(self) -> bool:
        """Returns true if the GraphicsOutput is rendering into any textures at all."""
    def get_texture(self, i: int = ...) -> Texture:
        """Returns the nth texture into which the GraphicsOutput renders.  Returns
        NULL if there is no such texture.

        If the texture is non-NULL, it may be applied to geometry to be rendered
        for any other windows or outputs that share the same GSG as this
        GraphicsOutput.  The effect is undefined for windows that share a different
        GSG; usually in these cases the texture will be invalid.
        """
    def get_texture_plane(self, i: int = ...) -> _DrawableRegion_RenderTexturePlane:
        """Returns the RenderTexturePlane associated with the nth render-texture.
        Returns 0 if there is no such texture.
        """
    def get_rtm_mode(self, i: int = ...) -> _GraphicsOutput_RenderTextureMode:
        """Returns the RenderTextureMode associated with the nth render-texture.
        Returns RTM_none if there is no such texture.
        """
    def clear_render_textures(self) -> None:
        """If the GraphicsOutput is currently rendering to a texture, then all
        textures are dissociated from the GraphicsOuput.
        """
    def add_render_texture(
        self, tex: Texture, mode: _GraphicsOutput_RenderTextureMode, bitplane: _DrawableRegion_RenderTexturePlane = ...
    ) -> None:
        """Creates a new Texture object, suitable for rendering the contents of this
        buffer into, and appends it to the list of render textures.

        If tex is not NULL, it is the texture that will be set up for rendering
        into; otherwise, a new Texture object will be created, in which case you
        may call get_texture() to retrieve the new texture pointer.

        You can specify a bitplane to attach the texture to.  the legal choices
        are:

        - RTP_depth
        - RTP_depth_stencil
        - RTP_color
        - RTP_aux_rgba_0
        - RTP_aux_rgba_1
        - RTP_aux_rgba_2
        - RTP_aux_rgba_3

        If you do not specify a bitplane to attach the texture to, this routine
        will use a default based on the texture's format:

        - F_depth_component attaches to RTP_depth
        - F_depth_stencil attaches to RTP_depth_stencil
        - all other formats attach to RTP_color.

        The texture's format will be changed to match the format of the bitplane to
        which it is attached.  For example, if you pass in an F_rgba texture and
        order that it be attached to RTP_depth_stencil, it will turn into an
        F_depth_stencil texture.

        Also see make_texture_buffer(), which is a higher-level interface for
        preparing render-to-a-texture mode.
        """
    def setup_render_texture(self, tex: Texture, allow_bind: bool, to_ram: bool) -> None:
        """This is a deprecated interface that made sense back when GraphicsOutputs
        could only render into one texture at a time.  From now on, use
        clear_render_textures and add_render_texture instead.

        @deprecated Use add_render_texture() instead.
        """
    def get_size(self) -> LVecBase2i:
        """Returns the visible size of the window or buffer, if it is known.  In
        certain cases (e.g.  fullscreen windows), the size may not be known until
        after the object has been fully created.  Check has_size() first.

        Certain objects (like windows) may change size spontaneously; this method
        is not thread-safe.  To get the size of a window in a thread-safe manner,
        query get_properties().
        """
    def get_x_size(self) -> int:
        """Returns the visible width of the window or buffer, if it is known.  In
        certain cases (e.g.  fullscreen windows), the size may not be known until
        after the object has been fully created.  Check has_size() first.

        Certain objects (like windows) may change size spontaneously; this method
        is not thread-safe.  To get the size of a window in a thread-safe manner,
        query get_properties().
        """
    def get_y_size(self) -> int:
        """Returns the visible height of the window or buffer, if it is known.  In
        certain cases (e.g.  fullscreen windows), the size may not be known until
        after the object has been fully created.  Check has_size() first.

        Certain objects (like windows) may change size spontaneously; this method
        is not thread-safe.  To get the size of a window in a thread-safe manner,
        query get_properties().
        """
    def get_fb_size(self) -> LVecBase2i:
        """Returns the internal size of the window or buffer.  This is almost always
        the same as get_size(), except when a pixel_zoom is in effect--see
        set_pixel_zoom().
        """
    def get_fb_x_size(self) -> int:
        """Returns the internal width of the window or buffer.  This is almost always
        the same as get_x_size(), except when a pixel_zoom is in effect--see
        set_pixel_zoom().
        """
    def get_fb_y_size(self) -> int:
        """Returns the internal height of the window or buffer.  This is almost always
        the same as get_y_size(), except when a pixel_zoom is in effect--see
        set_pixel_zoom().
        """
    def get_sbs_left_size(self) -> LVecBase2i:
        """If side-by-side stereo is enabled, this returns the pixel size of the left
        eye, based on scaling get_size() by get_sbs_left_dimensions().  If side-by-
        side stereo is not enabled, this returns the same as get_size().
        """
    def get_sbs_left_x_size(self) -> int:
        """If side-by-side stereo is enabled, this returns the pixel width of the left
        eye, based on scaling get_x_size() by get_sbs_left_dimensions().  If side-
        by-side stereo is not enabled, this returns the same as get_x_size().
        """
    def get_sbs_left_y_size(self) -> int:
        """If side-by-side stereo is enabled, this returns the pixel height of the
        left eye, based on scaling get_y_size() by get_sbs_left_dimensions().  If
        side-by-side stereo is not enabled, this returns the same as get_y_size().
        """
    def get_sbs_right_size(self) -> LVecBase2i:
        """If side-by-side stereo is enabled, this returns the pixel size of the right
        eye, based on scaling get_size() by get_sbs_right_dimensions().  If side-
        by-side stereo is not enabled, this returns the same as get_size().
        """
    def get_sbs_right_x_size(self) -> int:
        """If side-by-side stereo is enabled, this returns the pixel width of the
        right eye, based on scaling get_x_size() by get_sbs_right_dimensions().  If
        side-by-side stereo is not enabled, this returns the same as get_x_size().
        """
    def get_sbs_right_y_size(self) -> int:
        """If side-by-side stereo is enabled, this returns the pixel height of the
        right eye, based on scaling get_y_size() by get_sbs_right_dimensions().  If
        side-by-side stereo is not enabled, this returns the same as get_y_size().
        """
    def has_size(self) -> bool:
        """Returns true if the size of the window/frame buffer is known, false
        otherwise.  In certain cases the size may not be known until after the
        object has been fully created.  Also, certain objects (like windows) may
        change size spontaneously.
        """
    def is_valid(self) -> bool:
        """Returns true if the output is fully created and ready for rendering, false
        otherwise.
        """
    def is_nonzero_size(self) -> bool:
        """Returns true if the output has a nonzero size in both X and Y, or false if
        it is zero (and therefore invalid).
        """
    def set_active(self, active: bool) -> None:
        """Sets the active flag associated with the GraphicsOutput.  If the
        GraphicsOutput is marked inactive, nothing is rendered.
        """
    def is_active(self) -> bool:
        """Returns true if the window is ready to be rendered into, false otherwise."""
    def set_one_shot(self, one_shot: bool) -> None:
        """Changes the current setting of the one-shot flag.  When this is true, the
        GraphicsOutput will render the current frame and then automatically set
        itself inactive.  This is particularly useful for buffers that are created
        for the purposes of render-to-texture, for static textures that don't need
        to be continually re-rendered once they have been rendered the first time.

        Setting the buffer inactive is not the same thing as destroying it.  You
        are still responsible for passing this buffer to
        GraphicsEngine::remove_window() when you no longer need the texture, in
        order to clean up fully.  (However, you should not call remove_window() on
        this buffer while the texture is still needed, because depending on the
        render-to-texture mechanism in use, this may invalidate the texture
        contents.)
        """
    def get_one_shot(self) -> bool:
        """Returns the current setting of the one-shot flag.  When this is true, the
        GraphicsOutput will automatically set itself inactive after the next frame.
        """
    def set_inverted(self, inverted: bool) -> None:
        """Changes the current setting of the inverted flag.  When this is true, the
        scene is rendered into the window upside-down and backwards, that is,
        inverted as if viewed through a mirror placed on the floor.

        This is primarily intended to support DirectX (and a few buggy OpenGL
        graphics drivers) that perform a framebuffer-to-texture copy upside-down
        from the usual OpenGL (and Panda) convention.  Panda will automatically set
        this flag for offscreen buffers on hardware that is known to do this, to
        compensate when rendering offscreen into a texture.
        """
    def get_inverted(self) -> bool:
        """Returns the current setting of the inverted flag.  When this is true, the
        scene is rendered into the window upside-down, flipped like a mirror along
        the X axis.  See set_inverted().
        """
    def set_swap_eyes(self, swap_eyes: bool) -> None:
        """Changes the "swap eyes" flag.  This flag is normally false.  When it is
        true, the left and right channels of a stereo DisplayRegion are sent to the
        opposite channels in the rendering backend.  This is meant to work around
        hardware that inadvertently swaps the output channels, or hardware for
        which it cannot be determined which channel is which until runtime.
        """
    def get_swap_eyes(self) -> bool:
        """Returns the current setting of the "swap eyes" flag.  See set_swap_eyes()."""
    def set_red_blue_stereo(self, red_blue_stereo: bool, left_eye_color_mask: int, right_eye_color_mask: int) -> None:
        """Enables red-blue stereo mode on this particular window.  When red-blue
        stereo mode is in effect, DisplayRegions that have the "left" channel set
        will render in the red (or specified) channel only, while DisplayRegions
        that have the "right" channel set will render in the blue (or specified)
        channel only.

        The remaining two parameters specify the particular color channel(s) to
        associate with each eye.  Use the bits defined in
        ColorWriteAttrib::Channels.

        This can be used to achieve a cheesy stereo mode in the absence of
        hardware-supported stereo.
        """
    def get_red_blue_stereo(self) -> bool:
        """Returns whether red-blue stereo mode is in effect for this particular
        window.  See set_red_blue_stereo().
        """
    def get_left_eye_color_mask(self) -> int:
        """Returns the color mask in effect when rendering a left-eye view in red_blue
        stereo mode.  This is one or more bits defined in
        ColorWriteAttrib::Channels.  See set_red_blue_stereo().
        """
    def get_right_eye_color_mask(self) -> int:
        """Returns the color mask in effect when rendering a right-eye view in
        red_blue stereo mode.  This is one or more bits defined in
        ColorWriteAttrib::Channels.  See set_red_blue_stereo().
        """
    @overload
    def set_side_by_side_stereo(self, side_by_side_stereo: bool) -> None:
        """Enables side-by-side stereo mode on this particular window.  When side-by-
        side stereo mode is in effect, DisplayRegions that have the "left" channel
        set will render on the part of the window specified by sbs_left_dimensions
        (typically the left half: (0, 0.5, 0, 1)), while DisplayRegions that have
        the "right" channel set will render on the part of the window specified by
        sbs_right_dimensions (typically the right half: (0.5, 1, 0, 1)).

        This is commonly used in a dual-monitor mode, where a window is opened that
        spans two monitors, and each monitor represents a different eye.
        """
    @overload
    def set_side_by_side_stereo(
        self, side_by_side_stereo: bool, sbs_left_dimensions: Vec4Like, sbs_right_dimensions: Vec4Like
    ) -> None: ...
    def get_side_by_side_stereo(self) -> bool:
        """Returns whether side-by-side stereo mode is in effect for this particular
        window.  See set_side_by_side_stereo().
        """
    def get_sbs_left_dimensions(self) -> LVecBase4:
        """Returns the effective sub-region of the window for displaying the left
        channel, if side-by-side stereo mode is in effect for the window.  See
        set_side_by_side_stereo().
        """
    def get_sbs_right_dimensions(self) -> LVecBase4:
        """Returns the effective sub-region of the window for displaying the right
        channel, if side-by-side stereo mode is in effect for the window.  See
        set_side_by_side_stereo().
        """
    def get_fb_properties(self) -> FrameBufferProperties:
        """Returns the framebuffer properties of the window."""
    def is_stereo(self) -> bool:
        """Returns Returns true if this window can render stereo DisplayRegions,
        either through red-blue stereo (see set_red_blue_stereo()) or through true
        hardware stereo rendering.
        """
    def clear_delete_flag(self) -> None:
        """Resets the delete flag, so the GraphicsOutput will not be automatically
        deleted before the beginning of the next frame.
        """
    def get_delete_flag(self) -> bool:
        """Returns the current setting of the delete flag.  When this is true, the
        GraphicsOutput will automatically be removed before the beginning of the
        next frame by the GraphicsEngine.
        """
    def set_sort(self, sort: int) -> None:
        """Adjusts the sorting order of this particular GraphicsOutput, relative to
        other GraphicsOutputs.
        """
    def get_sort(self) -> int:
        """Returns the sorting order of this particular GraphicsOutput.  The various
        GraphicsOutputs within a particular thread will be rendered in the
        indicated order.
        """
    def set_child_sort(self, child_sort: int) -> None:
        """Specifies the sort value of future offscreen buffers created by
        make_texture_sort().

        The purpose of this method is to allow the user to limit the sort value
        chosen for a buffer created via make_texture_buffer().  Normally, this
        buffer will be assigned a value of get_sort() - 1, so that it will be
        rendered before this window is rendered; but sometimes this isn't
        sufficiently early, especially if other buffers also have a view into the
        same scene.

        If you specify a value here, then new buffers created via
        make_texture_buffer() will be given that sort value instead of get_sort() -
        1.
        """
    def clear_child_sort(self) -> None:
        """Resets the sort value of future offscreen buffers created by
        make_texture_sort() to the default value.  See set_child_sort().
        """
    def get_child_sort(self) -> int:
        """Returns the sort value of future offscreen buffers created by
        make_texture_sort(). See set_child_sort().
        """
    def trigger_copy(self) -> AsyncFuture:
        """When the GraphicsOutput is in triggered copy mode, this function triggers
        the copy (at the end of the next frame).
        @returns a future that can be awaited.
        """
    @overload
    def make_display_region(self, dimensions: Vec4Like = ...) -> DisplayRegion:
        """`(self)`:
        Creates a new DisplayRegion that covers the entire window.

        If is_stereo() is true for this window, and default-stereo-camera is
        configured true, this actually makes a StereoDisplayRegion.  Call
        make_mono_display_region() or make_stereo_display_region() if you want to
        insist on one or the other.

        `(self, dimensions: LVecBase4)`; `(self, l: float, r: float, b: float, t: float)`:
        Creates a new DisplayRegion that covers the indicated sub-rectangle within
        the window.  The range on all parameters is 0..1.

        If is_stereo() is true for this window, and default-stereo-camera is
        configured true, this actually makes a StereoDisplayRegion.  Call
        make_mono_display_region() or make_stereo_display_region() if you want to
        insist on one or the other.
        """
    @overload
    def make_display_region(self, l: float, r: float, b: float, t: float) -> DisplayRegion: ...
    @overload
    def make_mono_display_region(self, dimensions: Vec4Like = ...) -> DisplayRegion:
        """`(self)`; `(self, l: float, r: float, b: float, t: float)`:
        Creates a new DisplayRegion that covers the entire window.

        This generally returns a mono DisplayRegion, even if is_stereo() is true.
        However, if side-by-side stereo is enabled, this will return a
        StereoDisplayRegion whose two eyes are both set to SC_mono.  (This is
        necessary because in side-by-side stereo mode, it is necessary to draw even
        mono DisplayRegions twice).

        `(self, dimensions: LVecBase4)`:
        Creates a new DisplayRegion that covers the indicated sub-rectangle within
        the window.  The range on all parameters is 0..1.

        This generally returns a mono DisplayRegion, even if is_stereo() is true.
        However, if side-by-side stereo is enabled, this will return a
        StereoDisplayRegion whose two eyes are both set to SC_mono.  (This is
        necessary because in side-by-side stereo mode, it is necessary to draw even
        mono DisplayRegions twice).
        """
    @overload
    def make_mono_display_region(self, l: float, r: float, b: float, t: float) -> DisplayRegion: ...
    @overload
    def make_stereo_display_region(self, dimensions: Vec4Like = ...) -> StereoDisplayRegion:
        """`(self)`; `(self, l: float, r: float, b: float, t: float)`:
        Creates a new DisplayRegion that covers the entire window.

        This always returns a stereo DisplayRegion, even if is_stereo() is false.

        `(self, dimensions: LVecBase4)`:
        Creates a new DisplayRegion that covers the indicated sub-rectangle within
        the window.  The range on all parameters is 0..1.

        This always returns a stereo DisplayRegion, even if is_stereo() is false.
        """
    @overload
    def make_stereo_display_region(self, l: float, r: float, b: float, t: float) -> StereoDisplayRegion: ...
    def remove_display_region(self, display_region: DisplayRegion) -> bool:
        """Removes the indicated DisplayRegion from the window, and destructs it if
        there are no other references.

        Returns true if the DisplayRegion is found and removed, false if it was not
        a part of the window.
        """
    def remove_all_display_regions(self) -> None:
        """Removes all display regions from the window, except the default one that is
        created with the window.
        """
    def get_overlay_display_region(self) -> DisplayRegion:
        """Returns the special "overlay" DisplayRegion that is created for each window
        or buffer.  This DisplayRegion covers the entire window, but cannot be used
        for rendering.  It is a placeholder only, to indicate the dimensions of the
        window, and is usually used internally for purposes such as clearing the
        window, or grabbing a screenshot of the window.

        There are very few applications that require access to this DisplayRegion.
        Normally, you should create your own DisplayRegion that covers the window,
        if you want to render to the window.
        """
    def set_overlay_display_region(self, display_region: DisplayRegion) -> None:
        """Replaces the special "overlay" DisplayRegion that is created for each
        window or buffer.  See get_overlay_display_region().  This must be a new
        DisplayRegion that has already been created for this window, for instance
        via a call to make_mono_display_region().  You are responsible for ensuring
        that the new DisplayRegion covers the entire window.  The previous overlay
        display region is not automatically removed; you must explicitly call
        remove_display_region() on it after replacing it with this method, if you
        wish it to be removed.

        Normally, there is no reason to change the overlay DisplayRegion, so this
        method should be used only in very unusual circumstances.
        """
    def get_num_display_regions(self) -> int:
        """Returns the number of DisplayRegions that have been created within the
        window, active or otherwise.
        """
    def get_display_region(self, n: int) -> DisplayRegion:
        """Returns the nth DisplayRegion of those that have been created within the
        window.  This may return NULL if n is out of bounds; particularly likely if
        the number of display regions has changed since the last call to
        get_num_display_regions().
        """
    def get_num_active_display_regions(self) -> int:
        """Returns the number of active DisplayRegions that have been created within
        the window.
        """
    def get_active_display_region(self, n: int) -> DisplayRegion:
        """Returns the nth active DisplayRegion of those that have been created within
        the window.  This may return NULL if n is out of bounds; particularly
        likely if the number of display regions has changed since the last call to
        get_num_active_display_regions().
        """
    def make_texture_buffer(
        self, name: str, x_size: int, y_size: int, tex: Texture = ..., to_ram: bool = ..., fbp: FrameBufferProperties = ...
    ) -> GraphicsOutput:
        """Creates and returns an offscreen buffer for rendering into, the result of
        which will be a texture suitable for applying to geometry within the scene
        rendered into this window.

        If you pass zero as the buffer size, the buffer will have the same size as
        the host window, and will automatically be resized when the host window is.

        If tex is not NULL, it is the texture that will be set up for rendering
        into; otherwise, a new Texture object will be created.  In either case, the
        target texture can be retrieved from the return value with
        buffer->get_texture() (assuming the return value is not NULL).

        If to_ram is true, the buffer will be set up to download its contents to
        the system RAM memory associated with the Texture object, instead of
        keeping it strictly within texture memory; this is much slower, but it
        allows using the texture with any GSG.

        This will attempt to be smart about maximizing render performance while
        minimizing framebuffer waste.  It might return a GraphicsBuffer set to
        render directly into a texture, if possible; or it might return a
        ParasiteBuffer that renders into this window.  The return value is NULL if
        the buffer could not be created for some reason.

        When you are done using the buffer, you should remove it with a call to
        GraphicsEngine::remove_window().
        """
    def make_cube_map(
        self,
        name: str,
        size: int,
        camera_rig: NodePath,
        camera_mask: DrawMask | int = ...,
        to_ram: bool = ...,
        fbp: FrameBufferProperties = ...,
    ) -> GraphicsOutput:
        """This is similar to make_texture_buffer() in that it allocates a separate
        buffer suitable for rendering to a texture that can be assigned to geometry
        in this window, but in this case, the buffer is set up to render the six
        faces of a cube map.

        The buffer is automatically set up with six display regions and six
        cameras, each of which are assigned the indicated draw_mask and parented to
        the given camera_rig node (which you should then put in your scene to
        render the cube map from the appropriate point of view).

        You may take the texture associated with the buffer and apply it to
        geometry, particularly with TexGenAttrib::M_world_cube_map also in effect,
        to apply a reflection of everything seen by the camera rig.
        """
    @staticmethod
    def make_screenshot_filename(prefix: str = ...) -> Filename:
        """Saves a screenshot of the region to a default filename, and returns the
        filename, or empty string if the screenshot failed.  The default filename
        is generated from the supplied prefix and from the Config variable
        screenshot-filename, which contains the following strings:

        %~p - the supplied prefix %~f - the frame count %~e - the value of
        screenshot-extension All other % strings in strftime().
        """
    def save_screenshot_default(self, prefix: str = ...) -> Filename:
        """Saves a screenshot of the region to a default filename, and returns the
        filename, or empty string if the screenshot failed.  The filename is
        generated by make_screenshot_filename().
        """
    def save_screenshot(self, filename: StrOrBytesPath, image_comment: str = ...) -> bool:
        """Saves a screenshot of the region to the indicated filename.  The image
        comment is an optional user readable string that will be saved with the
        header of the image (if the file format supports embedded data; for example
        jpg allows comments).  Returns true on success, false on failure.
        """
    @overload
    def get_screenshot(self) -> Texture:
        """`(self)`:
        Captures the most-recently rendered image from the framebuffer and returns
        it as Texture, or NULL on failure.

        `(self, image: PNMImage)`:
        Captures the most-recently rendered image from the framebuffer into the
        indicated PNMImage.  Returns true on success, false on failure.
        """
    @overload
    def get_screenshot(self, image: PNMImage) -> bool: ...
    def get_texture_card(self) -> NodePath:
        """Returns a PandaNode containing a square polygon.  The dimensions are
        (-1,0,-1) to (1,0,1). The texture coordinates are such that the texture of
        this GraphicsOutput is aligned properly to the polygon.  The GraphicsOutput
        promises to surgically update the Geom inside the PandaNode if necessary to
        maintain this invariant.

        Each invocation of this function returns a freshly- allocated PandaNode.
        You can therefore safely modify the RenderAttribs of the PandaNode.  The
        PandaNode is initially textured with the texture of this GraphicOutput.
        """
    def share_depth_buffer(self, graphics_output: GraphicsOutput) -> bool:
        """Will attempt to use the depth buffer of the input graphics_output.  The
        buffer sizes must be exactly the same.
        """
    def unshare_depth_buffer(self) -> None:
        """Discontinue sharing the depth buffer."""
    def get_supports_render_texture(self) -> bool:
        """Returns true if this particular GraphicsOutput can render directly into a
        texture, or false if it must always copy-to-texture at the end of each
        frame to achieve this effect.
        """
    def flip_ready(self) -> bool:
        """These are not intended to be called directly by the user, but they're
        published anyway since they might occasionally be useful for low-level
        debugging.
        """
    def get_host(self) -> GraphicsOutput:
        """This is normally called only from within make_texture_buffer().  When
        called on a ParasiteBuffer, it returns the host of that buffer; but when
        called on some other buffer, it returns the buffer itself.
        """
    def get_display_regions(self) -> tuple[DisplayRegion, ...]: ...
    def get_active_display_regions(self) -> tuple[DisplayRegion, ...]: ...
    upcastToGraphicsOutputBase = upcast_to_GraphicsOutputBase
    upcastToDrawableRegion = upcast_to_DrawableRegion
    getGsg = get_gsg
    getPipe = get_pipe
    getEngine = get_engine
    getName = get_name
    countTextures = count_textures
    hasTexture = has_texture
    getTexture = get_texture
    getTexturePlane = get_texture_plane
    getRtmMode = get_rtm_mode
    clearRenderTextures = clear_render_textures
    addRenderTexture = add_render_texture
    setupRenderTexture = setup_render_texture
    getSize = get_size
    getXSize = get_x_size
    getYSize = get_y_size
    getFbSize = get_fb_size
    getFbXSize = get_fb_x_size
    getFbYSize = get_fb_y_size
    getSbsLeftSize = get_sbs_left_size
    getSbsLeftXSize = get_sbs_left_x_size
    getSbsLeftYSize = get_sbs_left_y_size
    getSbsRightSize = get_sbs_right_size
    getSbsRightXSize = get_sbs_right_x_size
    getSbsRightYSize = get_sbs_right_y_size
    hasSize = has_size
    isValid = is_valid
    isNonzeroSize = is_nonzero_size
    setActive = set_active
    isActive = is_active
    setOneShot = set_one_shot
    getOneShot = get_one_shot
    setInverted = set_inverted
    getInverted = get_inverted
    setSwapEyes = set_swap_eyes
    getSwapEyes = get_swap_eyes
    setRedBlueStereo = set_red_blue_stereo
    getRedBlueStereo = get_red_blue_stereo
    getLeftEyeColorMask = get_left_eye_color_mask
    getRightEyeColorMask = get_right_eye_color_mask
    setSideBySideStereo = set_side_by_side_stereo
    getSideBySideStereo = get_side_by_side_stereo
    getSbsLeftDimensions = get_sbs_left_dimensions
    getSbsRightDimensions = get_sbs_right_dimensions
    getFbProperties = get_fb_properties
    isStereo = is_stereo
    clearDeleteFlag = clear_delete_flag
    getDeleteFlag = get_delete_flag
    setSort = set_sort
    getSort = get_sort
    setChildSort = set_child_sort
    clearChildSort = clear_child_sort
    getChildSort = get_child_sort
    triggerCopy = trigger_copy
    makeDisplayRegion = make_display_region
    makeMonoDisplayRegion = make_mono_display_region
    makeStereoDisplayRegion = make_stereo_display_region
    removeDisplayRegion = remove_display_region
    removeAllDisplayRegions = remove_all_display_regions
    getOverlayDisplayRegion = get_overlay_display_region
    setOverlayDisplayRegion = set_overlay_display_region
    getNumDisplayRegions = get_num_display_regions
    getDisplayRegion = get_display_region
    getNumActiveDisplayRegions = get_num_active_display_regions
    getActiveDisplayRegion = get_active_display_region
    makeTextureBuffer = make_texture_buffer
    makeCubeMap = make_cube_map
    makeScreenshotFilename = make_screenshot_filename
    saveScreenshotDefault = save_screenshot_default
    saveScreenshot = save_screenshot
    getScreenshot = get_screenshot
    getTextureCard = get_texture_card
    shareDepthBuffer = share_depth_buffer
    unshareDepthBuffer = unshare_depth_buffer
    getSupportsRenderTexture = get_supports_render_texture
    flipReady = flip_ready
    getHost = get_host
    getDisplayRegions = get_display_regions
    getActiveDisplayRegions = get_active_display_regions

class GraphicsStateGuardian(GraphicsStateGuardianBase):
    """Encapsulates all the communication with a particular instance of a given
    rendering backend.  Tries to guarantee that redundant state-change requests
    are not issued (hence "state guardian").

    There will be one of these objects for each different graphics context
    active in the system.
    """

    SM_00: Final = 0
    SM00: Final = 0
    SM_11: Final = 1
    SM11: Final = 1
    SM_20: Final = 2
    SM20: Final = 2
    SM_2X: Final = 3
    SM2X: Final = 3
    SM_30: Final = 4
    SM30: Final = 4
    SM_40: Final = 5
    SM40: Final = 5
    SM_50: Final = 6
    SM50: Final = 6
    SM_51: Final = 7
    SM51: Final = 7
    active: bool
    incomplete_render: bool
    loader: Loader
    shader_generator: ShaderGenerator
    shader_model: _GraphicsStateGuardian_ShaderModel
    coordinate_system: _CoordinateSystem
    gamma: float
    texture_quality_override: _Texture_QualityLevel
    flash_texture: Texture
    scene: SceneSetup
    @property
    def valid(self) -> bool: ...
    @property
    def effective_incomplete_render(self) -> bool: ...
    @property
    def pipe(self) -> GraphicsPipe: ...
    @property
    def max_vertices_per_array(self) -> int: ...
    @property
    def max_vertices_per_primitive(self) -> int: ...
    @property
    def max_texture_stages(self) -> int: ...
    @property
    def max_texture_dimension(self) -> int: ...
    @property
    def max_3d_texture_dimension(self) -> int: ...
    @property
    def max_2d_texture_array_layers(self) -> int:
        """z axis"""
    @property
    def max_cube_map_dimension(self) -> int:
        """z axis"""
    @property
    def max_buffer_texture_size(self) -> int: ...
    @property
    def supports_texture_combine(self) -> bool: ...
    @property
    def supports_texture_saved_result(self) -> bool: ...
    @property
    def supports_texture_dot3(self) -> bool: ...
    @property
    def supports_3d_texture(self) -> bool: ...
    @property
    def supports_2d_texture_array(self) -> bool: ...
    @property
    def supports_cube_map(self) -> bool: ...
    @property
    def supports_buffer_texture(self) -> bool: ...
    @property
    def supports_cube_map_array(self) -> bool: ...
    @property
    def supports_tex_non_pow2(self) -> bool: ...
    @property
    def supports_texture_srgb(self) -> bool: ...
    @property
    def supports_compressed_texture(self) -> bool: ...
    @property
    def max_lights(self) -> int: ...
    @property
    def max_clip_planes(self) -> int: ...
    @property
    def max_vertex_transforms(self) -> int: ...
    @property
    def max_vertex_transform_indices(self) -> int: ...
    @property
    def copy_texture_inverted(self) -> bool: ...
    @property
    def supports_multisample(self) -> bool: ...
    @property
    def supports_generate_mipmap(self) -> bool: ...
    @property
    def supports_depth_texture(self) -> bool: ...
    @property
    def supports_depth_stencil(self) -> bool: ...
    @property
    def supports_luminance_texture(self) -> bool: ...
    @property
    def supports_shadow_filter(self) -> bool: ...
    @property
    def supports_sampler_objects(self) -> bool: ...
    @property
    def supports_basic_shaders(self) -> bool: ...
    @property
    def supports_geometry_shaders(self) -> bool: ...
    @property
    def supports_tessellation_shaders(self) -> bool: ...
    @property
    def supports_compute_shaders(self) -> bool: ...
    @property
    def supports_glsl(self) -> bool: ...
    @property
    def supports_hlsl(self) -> bool: ...
    @property
    def supports_stencil(self) -> bool: ...
    @property
    def supports_two_sided_stencil(self) -> bool: ...
    @property
    def supports_geometry_instancing(self) -> bool: ...
    @property
    def supports_indirect_draw(self) -> bool: ...
    @property
    def supports_occlusion_query(self) -> bool: ...
    @property
    def supports_timer_query(self) -> bool: ...
    @property
    def timer_queries_active(self) -> bool: ...
    @property
    def max_color_targets(self) -> int: ...
    @property
    def supports_dual_source_blending(self) -> bool: ...
    @property
    def prepared_objects(self) -> PreparedGraphicsObjects: ...
    @property
    def driver_vendor(self) -> str: ...
    @property
    def driver_renderer(self) -> str: ...
    @property
    def driver_version(self) -> str: ...
    @property
    def driver_version_major(self) -> int: ...
    @property
    def driver_version_minor(self) -> int: ...
    @property
    def driver_shader_version_major(self) -> int: ...
    @property
    def driver_shader_version_minor(self) -> int: ...
    def release_all(self) -> None:
        """Releases all prepared objects."""
    def release_all_textures(self) -> int:
        """Frees the resources for all textures associated with this GSG."""
    def release_all_samplers(self) -> int:
        """Frees the resources for all samplers associated with this GSG."""
    def release_all_geoms(self) -> int:
        """Frees the resources for all geoms associated with this GSG."""
    def release_all_vertex_buffers(self) -> int:
        """Frees the resources for all vertex buffers associated with this GSG."""
    def release_all_index_buffers(self) -> int:
        """Frees the resources for all index buffers associated with this GSG."""
    def release_all_shader_buffers(self) -> int:
        """Frees the resources for all index buffers associated with this GSG."""
    def set_active(self, active: bool) -> None:
        """Sets the active flag associated with the GraphicsStateGuardian.  If the
        GraphicsStateGuardian is marked inactive, nothing is rendered.  This is not
        normally turned off unless there is a problem with the rendering detected
        at a low level.
        """
    def is_active(self) -> bool:
        """Returns the active flag associated with the GraphicsStateGuardian."""
    def is_valid(self) -> bool:
        """Returns true if the GSG has been correctly initialized within a graphics
        context, false if there has been some problem or it hasn't been initialized
        yet.
        """
    def needs_reset(self) -> bool:
        """Returns true if the gsg is marked as needing a reset."""
    def set_incomplete_render(self, incomplete_render: bool) -> None:
        """Sets the incomplete_render flag.  When this is true, the frame will be
        rendered even if some of the geometry or textures in the scene are not
        available (e.g.  they have been temporarily paged out).  When this is
        false, the frame will be held up while this data is reloaded.

        Setting this true allows for a smoother frame rate, but occasionally parts
        of the frame will be invisible or missing (they will generally come in
        within a second or two).  Setting this false guarantees that every frame
        will be complete, but may cause more chugs as things are loaded up at
        runtime.

        You may want to set this false during loading screens, to guarantee that
        all of your assets are available by the time you take the loading screen
        down.

        This flag may also be set individually on each DisplayRegion.  It will be
        considered true for a given DisplayRegion only if it is true on both the
        GSG and on the DisplayRegion.
        """
    def set_loader(self, loader: Loader) -> None:
        """Sets the Loader object that will be used by this GSG to load textures when
        necessary, if get_incomplete_render() is true.
        """
    def get_loader(self) -> Loader:
        """Returns the Loader object that will be used by this GSG to load textures
        when necessary, if get_incomplete_render() is true.
        """
    def set_shader_generator(self, shader_generator: GraphicsStateGuardianBase | ShaderGenerator) -> None:
        """Sets the ShaderGenerator object that will be used by this GSG to generate
        shaders when necessary.
        """
    def get_shader_generator(self) -> ShaderGenerator:
        """Returns the ShaderGenerator object that will be used by this GSG to
        generate shaders when necessary.
        """
    def get_pipe(self) -> GraphicsPipe:
        """Returns the graphics pipe on which this GSG was created."""
    def get_engine(self) -> GraphicsEngine: ...
    def get_threading_model(self) -> GraphicsThreadingModel:
        """Returns the threading model that was used to create this GSG."""
    def is_hardware(self) -> bool:
        """Returns true if this GSG appears to be hardware-accelerated, or false if it
        is known to be software only.
        """
    def get_max_texture_stages(self) -> int:
        """Returns the maximum number of simultaneous textures that may be applied to
        geometry with multitexturing, as supported by this particular GSG.  If you
        exceed this number, the lowest-priority texture stages will not be applied.
        Use TextureStage::set_priority() to adjust the relative importance of the
        different texture stages.

        The value returned may not be meaningful until after the graphics context
        has been fully created (e.g.  the window has been opened).
        """
    def get_max_3d_texture_dimension(self) -> int:
        """Returns the largest possible texture size in any one dimension for a 3-d
        texture, or -1 if there is no particular limit.  Returns 0 if 3-d textures
        are not supported.

        The value returned may not be meaningful until after the graphics context
        has been fully created (e.g.  the window has been opened).
        """
    def get_max_2d_texture_array_layers(self) -> int:
        """Returns the largest possible number of pages, or -1 if there is no
        particular limit.  Returns 0 if 2-d texture arrays not supported.

        The value returned may not be meaningful until after the graphics context
        has been fully created (e.g.  the window has been opened).
        """
    def get_max_cube_map_dimension(self) -> int:
        """Returns the largest possible texture size in any one dimension for a cube
        map texture, or -1 if there is no particular limit.  Returns 0 if cube map
        textures are not supported.

        The value returned may not be meaningful until after the graphics context
        has been fully created (e.g.  the window has been opened).
        """
    def get_max_buffer_texture_size(self) -> int:
        """Returns the largest possible buffer texture size, or -1 if there is no
        particular limit.  Returns 0 if cube map textures are not supported.

        The value returned may not be meaningful until after the graphics context
        has been fully created (e.g.  the window has been opened).
        """
    def get_supports_texture_combine(self) -> bool:
        """Returns true if this particular GSG can use the TextureStage::M_combine
        mode, which includes all of the texture blend modes specified by
        set_combine_rgb() and/or set_combine_alpha().  If this is false, you must
        limit yourself to using the simpler blend modes.
        """
    def get_supports_texture_saved_result(self) -> bool:
        """Returns true if this GSG can use the TextureStage::CS_last_saved_result
        source, which allows you to save the result of a TextureStage and re-use it
        for multiple inputs.
        """
    def get_supports_texture_dot3(self) -> bool:
        """Returns true if this GSG can use the TextureStage::CM_dot3_rgb or
        CM_dot3_rgba combine modes.
        """
    def get_supports_3d_texture(self) -> bool:
        """Returns true if this GSG can render 3-d (volumetric) textures."""
    def get_supports_2d_texture_array(self) -> bool:
        """Returns true if this GSG can render 2-d textures array."""
    def get_supports_cube_map(self) -> bool:
        """Returns true if this GSG can render cube map textures."""
    def get_supports_buffer_texture(self) -> bool:
        """Returns true if this GSG can render buffer textures."""
    def get_supports_cube_map_array(self) -> bool:
        """Returns true if this GSG can render cube map arrays."""
    def get_supports_tex_non_pow2(self) -> bool:
        """Returns true if this GSG can handle non power of two sized textures."""
    def get_supports_compressed_texture(self) -> bool:
        """Returns true if this GSG can compress textures as it loads them into
        texture memory, and/or accept pre-compressed textures for storing.
        """
    def get_max_lights(self) -> int:
        """Returns the maximum number of simultaneous lights that may be rendered on
        geometry, or -1 if there is no particular limit.

        The value returned may not be meaningful until after the graphics context
        has been fully created (e.g.  the window has been opened).
        """
    def get_max_clip_planes(self) -> int:
        """Returns the maximum number of simultaneous clip planes that may be applied
        to geometry, or -1 if there is no particular limit.

        The value returned may not be meaningful until after the graphics context
        has been fully created (e.g.  the window has been opened).
        """
    def get_max_vertex_transforms(self) -> int:
        """Returns the maximum number of transform matrices that may be simultaneously
        used to transform any one vertex by the graphics hardware.  If this number
        is 0, then the hardware (or the graphics backend) doesn't support soft-
        skinned vertices (in which case Panda will animate the vertices in
        software).

        The value returned may not be meaningful until after the graphics context
        has been fully created (e.g.  the window has been opened).
        """
    def get_max_vertex_transform_indices(self) -> int:
        """Returns the maximum number of transforms there may be in a single
        TransformTable for this graphics hardware.  If this number is 0 (but
        get_max_transforms() is nonzero), then the graphics hardware (or API)
        doesn't support indexed transforms, but can support direct transform
        references.

        The value returned may not be meaningful until after the graphics context
        has been fully created (e.g.  the window has been opened).
        """
    def get_copy_texture_inverted(self) -> bool:
        """Returns true if this particular GSG has the property that any framebuffer-
        to-texture copy results in a texture that is upside-down and backwards from
        Panda's usual convention; that is, it copies into a texture from the bottom
        up instead of from the top down.

        If this is true, then on offscreen GraphicsBuffer created for the purposes
        of rendering into a texture should be created with the invert flag set
        true, to compensate.  Panda will do this automatically if you create an
        offscreen buffer using GraphicsOutput::make_texture_buffer().
        """
    def get_supports_generate_mipmap(self) -> bool:
        """Returns true if this particular GSG can generate mipmaps for a texture
        automatically, or if they must be generated in software.  If this is true,
        then mipmaps can safely be enabled for rendered textures (e.g.  using the
        MultitexReducer).
        """
    def get_supports_depth_texture(self) -> bool:
        """Returns true if this particular GSG supports textures whose format is
        F_depth_stencil.  This returns true if the GSG supports GL_DEPTH_COMPONENT
        textures, which are considered a limited but still valid case of
        F_depth_stencil.
        """
    def get_supports_depth_stencil(self) -> bool:
        """Returns true if this particular GSG supports textures whose format is
        F_depth_stencil.  This only returns true if the GSG supports the full
        packed depth-stencil functionality.
        """
    def get_supports_luminance_texture(self) -> bool:
        """Returns true if this particular GSG supports luminance textures."""
    def get_supports_sampler_objects(self) -> bool:
        """Returns true if this particular GSG supports the use of sampler objects to
        record texture sampling parameters separately from the texture objects.
        This doesn't really affect functionality, but if this is false, it may mean
        that using the same texture with different SamplerState objects will result
        in reduced performance.
        """
    def get_supports_basic_shaders(self) -> bool:
        """Returns true if this particular GSG supports arbfp1+arbvp1 or above."""
    def get_supports_geometry_shaders(self) -> bool:
        """Returns true if this particular GSG supports geometry shaders."""
    def get_supports_tessellation_shaders(self) -> bool:
        """Returns true if this particular GSG supports tesselation shaders."""
    def get_supports_compute_shaders(self) -> bool:
        """Returns true if this particular GSG supports compute shaders."""
    def get_supports_glsl(self) -> bool:
        """Returns true if this particular GSG supports GLSL shaders."""
    def get_supports_stencil(self) -> bool:
        """Returns true if this particular GSG supports stencil buffers at all."""
    def get_supports_two_sided_stencil(self) -> bool:
        """Returns true if this particular GSG supports two sided stencil: different
        stencil settings for the front and back side of the same polygon.
        """
    def get_supports_geometry_instancing(self) -> bool:
        """Returns true if this particular GSG supports hardware geometry instancing:
        the ability to render multiple copies of a model.  In OpenGL, this is done
        using the EXT_draw_instanced extension.
        """
    def get_supports_indirect_draw(self) -> bool:
        """Returns true if this particular GSG supports draw calls for which the
        information comes from a buffer.
        """
    def get_supports_occlusion_query(self) -> bool:
        """Returns true if this GSG supports an occlusion query.  If this is true,
        then begin_occlusion_query() and end_occlusion_query() may be called to
        bracket a sequence of draw_triangles() (or whatever) calls to measure
        pixels that pass the depth test.
        """
    def get_supports_timer_query(self) -> bool:
        """Returns true if this GSG supports a timer query."""
    def get_timer_queries_active(self) -> bool:
        """Returns true if timer queries are currently enabled on this GSG."""
    def get_max_color_targets(self) -> int:
        """Returns the maximum number of simultaneous color textures that may be
        attached for render-to-texture, as supported by this particular GSG.  If
        you exceed this number, the lowest-priority render targets will not be
        applied.  Use RenderTarget::set_priority() to adjust the relative
        importance of the different render targets.

        The value returned may not be meaningful until after the graphics context
        has been fully created (e.g.  the window has been opened).
        """
    def get_maximum_simultaneous_render_targets(self) -> int:
        """Deprecated.  Use get_max_color_targets() instead, which returns the exact
        same value.
        """
    def get_supports_dual_source_blending(self) -> bool:
        """Returns true if dual source (incoming1_color and incoming1_alpha) blend
        operands are supported by this GSG.
        """
    def get_shader_model(self) -> _GraphicsStateGuardian_ShaderModel:
        """Returns the ShaderModel"""
    def set_shader_model(self, shader_model: _GraphicsStateGuardian_ShaderModel) -> None:
        """Sets the ShaderModel.  This will override the auto- detected shader model
        during GSG reset.  Useful for testing lower-end shaders.
        """
    def get_supports_cg_profile(self, name: str) -> bool: ...
    def get_color_scale_via_lighting(self) -> bool:
        """Returns true if this particular GSG can implement (or would prefer to
        implement) set color and/or color scale using materials and/or ambient
        lights, or false if we need to actually munge the color.
        """
    def get_alpha_scale_via_texture(self, tex_attrib: Texture | TextureAttrib = ...) -> bool:
        """`(self)`:
        Returns true if this particular GSG can implement (or would prefer to
        implement) an alpha scale via an additional Texture layer, or false if we
        need to actually munge the alpha.

        `(self, tex_attrib: TextureAttrib)`:
        This variant of get_alpha_scale_via_texture() answers the question of
        whether the GSG can implement an alpha scale via an additional Texture
        layer, considering the current TextureAttrib that will be in effect.  This
        considers whether there is at least one additional texture slot available
        on the GSG.
        """
    def get_runtime_color_scale(self) -> bool:
        """Returns true if this particular GSG can implement (or would prefer to
        implement) set color and/or color scale directly, without requiring any
        munging of vertices or tricks with lighting.
        """
    @staticmethod
    def get_alpha_scale_texture_stage() -> TextureStage:
        """Returns the TextureStage that will be used to apply an alpha scale, if
        get_alpha_scale_via_texture() returns true.
        """
    def set_coordinate_system(self, cs: _CoordinateSystem) -> None: ...
    def get_coordinate_system(self) -> _CoordinateSystem:
        """Returns the coordinate system in effect on this particular gsg.  Normally,
        this will be the default coordinate system, but it might be set differently
        at runtime.
        """
    def get_internal_coordinate_system(self) -> _CoordinateSystem: ...
    def get_prepared_objects(self) -> PreparedGraphicsObjects: ...
    def set_gamma(self, gamma: float) -> bool: ...
    def get_gamma(self) -> float: ...
    def restore_gamma(self) -> None: ...
    def set_texture_quality_override(self, quality_level: _Texture_QualityLevel) -> None:
        """Specifies the global quality_level to be imposed for all Textures rendered
        by this GSG.  This overrides the value set on individual textures via
        Texture::set_quality_level().  Set this to Texture::QL_default in order to
        allow the individual texture quality levels to be respected.

        This is mainly useful for the tinydisplay software renderer.  See
        Texture::set_quality_level().
        """
    def get_texture_quality_override(self) -> _Texture_QualityLevel:
        """Returns the global quality_level override specified by
        set_texture_quality_override.

        This is mainly useful for the tinydisplay software renderer.  See
        Texture::set_quality_level().
        """
    def get_prepared_textures(self) -> list[Any]: ...
    def set_flash_texture(self, tex: Texture) -> None: ...
    def clear_flash_texture(self) -> None: ...
    def get_flash_texture(self) -> Texture: ...
    def has_extension(self, extension: str) -> bool: ...
    def get_driver_vendor(self) -> str: ...
    def get_driver_renderer(self) -> str: ...
    def get_driver_version(self) -> str: ...
    def get_driver_version_major(self) -> int: ...
    def get_driver_version_minor(self) -> int: ...
    def get_driver_shader_version_major(self) -> int: ...
    def get_driver_shader_version_minor(self) -> int: ...
    def set_scene(self, scene_setup: SceneSetup) -> bool: ...
    def get_scene(self) -> SceneSetup: ...
    def begin_scene(self) -> bool: ...
    def end_scene(self) -> None: ...
    releaseAll = release_all
    releaseAllTextures = release_all_textures
    releaseAllSamplers = release_all_samplers
    releaseAllGeoms = release_all_geoms
    releaseAllVertexBuffers = release_all_vertex_buffers
    releaseAllIndexBuffers = release_all_index_buffers
    releaseAllShaderBuffers = release_all_shader_buffers
    setActive = set_active
    isActive = is_active
    isValid = is_valid
    needsReset = needs_reset
    setIncompleteRender = set_incomplete_render
    setLoader = set_loader
    getLoader = get_loader
    setShaderGenerator = set_shader_generator
    getShaderGenerator = get_shader_generator
    getPipe = get_pipe
    getEngine = get_engine
    getThreadingModel = get_threading_model
    isHardware = is_hardware
    getMaxTextureStages = get_max_texture_stages
    getMax3dTextureDimension = get_max_3d_texture_dimension
    getMax2dTextureArrayLayers = get_max_2d_texture_array_layers
    getMaxCubeMapDimension = get_max_cube_map_dimension
    getMaxBufferTextureSize = get_max_buffer_texture_size
    getSupportsTextureCombine = get_supports_texture_combine
    getSupportsTextureSavedResult = get_supports_texture_saved_result
    getSupportsTextureDot3 = get_supports_texture_dot3
    getSupports3dTexture = get_supports_3d_texture
    getSupports2dTextureArray = get_supports_2d_texture_array
    getSupportsCubeMap = get_supports_cube_map
    getSupportsBufferTexture = get_supports_buffer_texture
    getSupportsCubeMapArray = get_supports_cube_map_array
    getSupportsTexNonPow2 = get_supports_tex_non_pow2
    getSupportsCompressedTexture = get_supports_compressed_texture
    getMaxLights = get_max_lights
    getMaxClipPlanes = get_max_clip_planes
    getMaxVertexTransforms = get_max_vertex_transforms
    getMaxVertexTransformIndices = get_max_vertex_transform_indices
    getCopyTextureInverted = get_copy_texture_inverted
    getSupportsGenerateMipmap = get_supports_generate_mipmap
    getSupportsDepthTexture = get_supports_depth_texture
    getSupportsDepthStencil = get_supports_depth_stencil
    getSupportsLuminanceTexture = get_supports_luminance_texture
    getSupportsSamplerObjects = get_supports_sampler_objects
    getSupportsBasicShaders = get_supports_basic_shaders
    getSupportsGeometryShaders = get_supports_geometry_shaders
    getSupportsTessellationShaders = get_supports_tessellation_shaders
    getSupportsComputeShaders = get_supports_compute_shaders
    getSupportsGlsl = get_supports_glsl
    getSupportsStencil = get_supports_stencil
    getSupportsTwoSidedStencil = get_supports_two_sided_stencil
    getSupportsGeometryInstancing = get_supports_geometry_instancing
    getSupportsIndirectDraw = get_supports_indirect_draw
    getSupportsOcclusionQuery = get_supports_occlusion_query
    getSupportsTimerQuery = get_supports_timer_query
    getTimerQueriesActive = get_timer_queries_active
    getMaxColorTargets = get_max_color_targets
    getMaximumSimultaneousRenderTargets = get_maximum_simultaneous_render_targets
    getSupportsDualSourceBlending = get_supports_dual_source_blending
    getShaderModel = get_shader_model
    setShaderModel = set_shader_model
    getSupportsCgProfile = get_supports_cg_profile
    getColorScaleViaLighting = get_color_scale_via_lighting
    getAlphaScaleViaTexture = get_alpha_scale_via_texture
    getRuntimeColorScale = get_runtime_color_scale
    getAlphaScaleTextureStage = get_alpha_scale_texture_stage
    setCoordinateSystem = set_coordinate_system
    getCoordinateSystem = get_coordinate_system
    getInternalCoordinateSystem = get_internal_coordinate_system
    getPreparedObjects = get_prepared_objects
    setGamma = set_gamma
    getGamma = get_gamma
    restoreGamma = restore_gamma
    setTextureQualityOverride = set_texture_quality_override
    getTextureQualityOverride = get_texture_quality_override
    getPreparedTextures = get_prepared_textures
    setFlashTexture = set_flash_texture
    clearFlashTexture = clear_flash_texture
    getFlashTexture = get_flash_texture
    hasExtension = has_extension
    getDriverVendor = get_driver_vendor
    getDriverRenderer = get_driver_renderer
    getDriverVersion = get_driver_version
    getDriverVersionMajor = get_driver_version_major
    getDriverVersionMinor = get_driver_version_minor
    getDriverShaderVersionMajor = get_driver_shader_version_major
    getDriverShaderVersionMinor = get_driver_shader_version_minor
    setScene = set_scene
    getScene = get_scene
    beginScene = begin_scene
    endScene = end_scene

class GraphicsEngine(ReferenceCount):
    """This class is the main interface to controlling the render process.  There
    is typically only one GraphicsEngine in an application, and it synchronizes
    rendering to all all of the active windows; although it is possible to have
    multiple GraphicsEngine objects if multiple synchronicity groups are
    required.

    The GraphicsEngine is responsible for managing the various cull and draw
    threads.  The application simply calls engine->render_frame() and considers
    it done.
    """

    threading_model: GraphicsThreadingModel
    auto_flip: bool
    portal_cull: bool
    default_loader: Loader
    @property
    def render_lock(self) -> ReMutex: ...
    @property
    def windows(self) -> Sequence[GraphicsOutput]: ...
    def set_threading_model(self, threading_model: GraphicsThreadingModel | str) -> None:
        """Specifies how future objects created via make_gsg(), make_buffer(), and
        make_output() will be threaded.  This does not affect any already-created
        objects.
        """
    def get_threading_model(self) -> GraphicsThreadingModel:
        """Returns the threading model that will be applied to future objects.  See
        set_threading_model().
        """
    def get_render_lock(self) -> ReMutex:
        """Returns a ReMutex object that is held by the GraphicsEngine during the
        entire call to render_frame().  While you hold this lock you can be
        confident that no part of the frame will be rendered (at least by the app
        thread).
        """
    def set_auto_flip(self, auto_flip: bool) -> None:
        """Set this flag true to indicate the GraphicsEngine should automatically
        cause windows to sync and flip as soon as they have finished drawing,
        rather than waiting for all of the windows to finish drawing first so they
        can flip together.

        This only affects the timing of when the flip occurs.  If this is true (the
        default), the flip occurs before render_frame() returns.  If this is false,
        the flip occurs whenever flip_frame() is called, or at the beginning of the
        next call to render_frame(), if flip_frame() is never called.
        """
    def get_auto_flip(self) -> bool:
        """Returns the current setting for the auto-flip flag.  See set_auto_flip."""
    def set_portal_cull(self, value: bool) -> None:
        """Set this flag true to indicate the GraphicsEngine should start portal
        culling
        """
    def get_portal_cull(self) -> bool:
        """Returns the current setting for the portal culling flag."""
    def set_default_loader(self, loader: Loader) -> None:
        """Sets the Loader object that will be assigned to every GSG created with this
        GraphicsEngine.  See GraphicsStateGuardian::set_loader().
        """
    def get_default_loader(self) -> Loader:
        """Returns the Loader object that will be assigned to every GSG created with
        this GraphicsEngine.  See GraphicsStateGuardian::set_loader().
        """
    def make_output(
        self,
        pipe: GraphicsPipe,
        name: str,
        sort: int,
        fb_prop: FrameBufferProperties,
        win_prop: WindowProperties,
        flags: int,
        gsg: GraphicsStateGuardian = ...,
        host: GraphicsOutput = ...,
    ) -> GraphicsOutput: ...
    @overload
    def make_buffer(self, host: GraphicsOutput, name: str, sort: int, x_size: int, y_size: int) -> GraphicsOutput:
        """`(self, host: GraphicsOutput, name: str, sort: int, x_size: int, y_size: int)`:
        Syntactic shorthand for make_output.  This is the preferred way to create
        an offscreen buffer, when you already have an onscreen window or another
        buffer to start with.  For the first parameter, pass an existing
        GraphicsOutput object, e.g.  the main window; this allows the buffer to
        adapt itself to that window's framebuffer properties, and allows maximum
        sharing of resources.

        `(self, gsg: GraphicsStateGuardian, name: str, sort: int, x_size: int, y_size: int)`:
        Syntactic shorthand for make_output.  This flavor accepts a GSG rather than
        a GraphicsOutput as the first parameter, which is too limiting and
        disallows the possibility of creating a ParasiteBuffer if the user's
        graphics hardware prefers that.  It also attempts to request specific
        framebuffer properties and may therefore do a poorer job of sharing the GSG
        between the old buffer and the new.

        For these reasons, this variant is a poor choice unless you are creating an
        offscreen buffer for the first time, without an onscreen window already in
        existence.  If you already have an onscreen window, you should use the
        other flavor of make_buffer() instead, which accepts a GraphicsOutput as
        the first parameter.
        """
    @overload
    def make_buffer(self, gsg: GraphicsStateGuardian, name: str, sort: int, x_size: int, y_size: int) -> GraphicsOutput: ...
    def make_parasite(self, host: GraphicsOutput, name: str, sort: int, x_size: int, y_size: int) -> GraphicsOutput:
        """Syntactic shorthand for make_buffer."""
    def add_window(self, window: GraphicsOutput, sort: int) -> bool:
        """This can be used to add a newly-created GraphicsOutput object (and its GSG)
        to the engine's list of windows, and requests that it be opened.  This
        shouldn't be called by user code as make_output normally does this under
        the hood; it may be useful in esoteric cases in which a custom window
        object is used.

        This can be called during the rendering loop, unlike make_output(); the
        window will be opened before the next frame begins rendering.  Because it
        doesn't call open_windows(), however, it's not guaranteed that the window
        will succeed opening even if it returns true.
        """
    def remove_window(self, window: GraphicsOutput) -> bool:
        """Removes the indicated window or offscreen buffer from the set of windows
        that will be processed when render_frame() is called.  This also closes the
        window if it is open, and removes the window from its GraphicsPipe,
        allowing the window to be destructed if there are no other references to
        it.  (However, the window may not be actually closed until next frame, if
        it is controlled by a sub-thread.)

        The return value is true if the window was removed, false if it was not
        found.

        Unlike remove_all_windows(), this function does not terminate any of the
        threads that may have been started to service this window; they are left
        running (since you might open a new window later on these threads).  If
        your intention is to clean up before shutting down, it is better to call
        remove_all_windows() then to call remove_window() one at a time.
        """
    def remove_all_windows(self) -> None:
        """Removes and closes all windows from the engine.  This also cleans up and
        terminates any threads that have been started to service those windows.
        """
    def reset_all_windows(self, swapchain: bool) -> None:
        """Resets the framebuffer of the current window.  This is currently used by
        DirectX 8 only.  It calls a reset_window function on each active window to
        release/create old/new framebuffer
        """
    def is_empty(self) -> bool:
        """Returns true if there are no windows or buffers managed by the engine,
        false if there is at least one.
        """
    def get_num_windows(self) -> int:
        """Returns the number of windows (or buffers) managed by the engine."""
    def get_window(self, n: int) -> GraphicsOutput:
        """Returns the nth window or buffers managed by the engine, in sorted order."""
    def render_frame(self) -> None:
        """Renders the next frame in all the registered windows, and flips all of the
        frame buffers.
        """
    def open_windows(self) -> None:
        """Fully opens (or closes) any windows that have recently been requested open
        or closed, without rendering any frames.  It is not necessary to call this
        explicitly, since windows will be automatically opened or closed when the
        next frame is rendered, but you may call this if you want your windows now
        without seeing a frame go by.
        """
    def sync_frame(self) -> None:
        """Waits for all the threads that started drawing their last frame to finish
        drawing.  The windows are not yet flipped when this returns; see also
        flip_frame(). It is not usually necessary to call this explicitly, unless
        you need to see the previous frame right away.
        """
    def ready_flip(self) -> None:
        """Waits for all the threads that started drawing their last frame to finish
        drawing.  Returns when all threads have actually finished drawing, as
        opposed to 'sync_frame' we seems to return once all draw calls have been
        submitted.  Calling 'flip_frame' after this function should immediately
        cause a buffer flip.  This function will only work in opengl right now, for
        all other graphics pipelines it will simply return immediately.  In opengl
        it's a bit of a hack: it will attempt to read a single pixel from the frame
        buffer to force the graphics card to finish drawing before it returns
        """
    def flip_frame(self) -> None:
        """Waits for all the threads that started drawing their last frame to finish
        drawing, and then flips all the windows.  It is not usually necessary to
        call this explicitly, unless you need to see the previous frame right away.
        """
    def extract_texture_data(self, tex: Texture, gsg: GraphicsStateGuardian) -> bool:
        """Asks the indicated GraphicsStateGuardian to retrieve the texture memory
        image of the indicated texture and store it in the texture's ram_image
        field.  The image can then be written to disk via Texture::write(), or
        otherwise manipulated on the CPU.

        This is useful for retrieving the contents of a texture that has been
        somehow generated on the graphics card, instead of having been loaded the
        normal way via Texture::read() or Texture::load(). It is particularly
        useful for getting the data associated with a compressed texture image.

        Since this requires a round-trip to the draw thread, it may require waiting
        for the current thread to finish rendering if it is called in a
        multithreaded environment.  However, you can call this several consecutive
        times on different textures for little additional cost.

        If the texture has not yet been loaded to the GSG in question, it will be
        loaded immediately.

        The return value is true if the operation is successful, false otherwise.
        """
    def dispatch_compute(self, work_groups: IntVec3Like, sattr: Shader | ShaderAttrib, gsg: GraphicsStateGuardian) -> None:
        """Asks the indicated GraphicsStateGuardian to dispatch the compute shader in
        the given ShaderAttrib using the given work group counts.  This can act as
        an interface for running a one-off compute shader, without having to store
        it in the scene graph using a ComputeNode.

        Since this requires a round-trip to the draw thread, it may require waiting
        for the current thread to finish rendering if it is called in a
        multithreaded environment.  However, you can call this several consecutive
        times on different textures for little additional cost.

        The return value is true if the operation is successful, false otherwise.
        """
    @staticmethod
    def get_global_ptr() -> GraphicsEngine: ...
    def get_windows(self) -> tuple[GraphicsOutput, ...]: ...
    setThreadingModel = set_threading_model
    getThreadingModel = get_threading_model
    getRenderLock = get_render_lock
    setAutoFlip = set_auto_flip
    getAutoFlip = get_auto_flip
    setPortalCull = set_portal_cull
    getPortalCull = get_portal_cull
    setDefaultLoader = set_default_loader
    getDefaultLoader = get_default_loader
    makeOutput = make_output
    makeBuffer = make_buffer
    makeParasite = make_parasite
    addWindow = add_window
    removeWindow = remove_window
    removeAllWindows = remove_all_windows
    resetAllWindows = reset_all_windows
    isEmpty = is_empty
    getNumWindows = get_num_windows
    getWindow = get_window
    renderFrame = render_frame
    openWindows = open_windows
    syncFrame = sync_frame
    readyFlip = ready_flip
    flipFrame = flip_frame
    extractTextureData = extract_texture_data
    dispatchCompute = dispatch_compute
    getGlobalPtr = get_global_ptr
    getWindows = get_windows

class GraphicsThreadingModel:
    """This represents the user's specification of how a particular frame is
    handled by the various threads.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, model: str = ...) -> None:
        """The threading model accepts a string representing the names of the two
        threads that will process cull and draw for the given window, separated by
        a slash.  The names are completely arbitrary and are used only to
        differentiate threads.  The two names may be the same, meaning the same
        thread, or each may be the empty string, which represents the previous
        thread.

        Thus, for example, "cull/draw" indicates that the window will be culled in
        a thread called "cull", and drawn in a separate thread called "draw".
        "draw/draw" or simply "draw" indicates the window will be culled and drawn
        in the same thread, "draw". On the other hand, "/draw" indicates the thread
        will be culled in the main, or app thread, and drawn in a separate thread
        named "draw".  The empty string, "" or "/", indicates the thread will be
        culled and drawn in the main thread; that is to say, a single-process
        model.

        Finally, if the threading model begins with a "-" character, then cull and
        draw are run simultaneously, in the same thread, with no binning or state
        sorting.  It simplifies the cull process but it forces the scene to render
        in scene graph order; state sorting and alpha sorting is lost.
        """
    @overload
    def __init__(self, copy: GraphicsThreadingModel) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: GraphicsThreadingModel | str) -> Self: ...
    def get_model(self) -> str:
        """Returns the string that describes the threading model.  See the
        constructor.
        """
    def get_cull_name(self) -> str:
        """Returns the name of the thread that will handle culling in this model."""
    def set_cull_name(self, cull_name: str) -> None:
        """Changes the name of the thread that will handle culling in this model.
        This won't change any windows that were already created with this model;
        this only has an effect on newly-opened windows.
        """
    def get_cull_stage(self) -> int:
        """Returns the pipeline stage from which the cull thread should access data.
        This will be 0 if the cull is run in the same thread as app, or 1 if it is
        its own thread.
        """
    def get_draw_name(self) -> str:
        """Returns the name of the thread that will handle sending the actual graphics
        primitives to the graphics API in this model.
        """
    def set_draw_name(self, cull_name: str) -> None:
        """Changes the name of the thread that will handle drawing in this model.
        This won't change any windows that were already created with this model;
        this only has an effect on newly-opened windows.
        """
    def get_draw_stage(self) -> int:
        """Returns the pipeline stage from which the draw thread should access data.
        This will be the same value as get_cull_stage() if cull and draw are run in
        the same thread, or one more than that value if draw should be in its own
        thread.
        """
    def get_cull_sorting(self) -> bool:
        """Returns true if the model involves a separate cull pass, or false if
        culling happens implicitly, at the same time as draw.
        """
    def set_cull_sorting(self, cull_sorting: bool) -> None:
        """Changes the flag that indicates whether the threading model involves a
        separate cull pass.  This won't change any windows that were already
        created with this model; this only has an effect on newly-opened windows.
        """
    def is_single_threaded(self) -> bool:
        """Returns true if the threading model is a single-threaded model, or false if
        it involves threads.
        """
    def is_default(self) -> bool:
        """Returns true if the threading model is the default, cull-then-draw single-
        threaded model, or false otherwise.
        """
    def output(self, out: ostream) -> None: ...
    getModel = get_model
    getCullName = get_cull_name
    setCullName = set_cull_name
    getCullStage = get_cull_stage
    getDrawName = get_draw_name
    setDrawName = set_draw_name
    getDrawStage = get_draw_stage
    getCullSorting = get_cull_sorting
    setCullSorting = set_cull_sorting
    isSingleThreaded = is_single_threaded
    isDefault = is_default

class StereoDisplayRegion(DisplayRegion):
    """This is a special DisplayRegion wrapper that actually includes a pair of
    DisplayRegions internally: the left and right eyes.  The DisplayRegion
    represented here does not have a physical association with the window, but
    it pretends it does.  Instead, it maintains a pointer to the left and right
    DisplayRegions separately.

    Operations on the StereoDisplayRegion object affect both left and right
    eyes together.  To access the left or right eyes independently, use
    get_left_eye() and get_right_eye().
    """

    @property
    def left_eye(self) -> DisplayRegion: ...
    @property
    def right_eye(self) -> DisplayRegion: ...
    def get_left_eye(self) -> DisplayRegion:
        """Returns a pointer to the left DisplayRegion managed by this stereo object."""
    def get_right_eye(self) -> DisplayRegion:
        """Returns a pointer to the right DisplayRegion managed by this stereo object."""
    getLeftEye = get_left_eye
    getRightEye = get_right_eye

class FrameBufferProperties:
    """A container for the various kinds of properties we might ask to have on a
    graphics frameBuffer before we create a GSG.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    depth_bits: int
    """Individual queries."""
    color_bits: int
    red_bits: int
    green_bits: int
    blue_bits: int
    alpha_bits: int
    stencil_bits: int
    accum_bits: int
    aux_rgba: int
    aux_hrgba: int
    aux_float: int
    multisamples: int
    coverage_samples: int
    back_buffers: int
    indexed_color: bool
    rgb_color: bool
    stereo: bool
    force_hardware: bool
    force_software: bool
    srgb_color: bool
    float_color: bool
    float_depth: bool
    def __init__(self, __param0: FrameBufferProperties = ...) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_depth_bits(self) -> int:
        """Individual queries."""
    def get_color_bits(self) -> int: ...
    def get_red_bits(self) -> int: ...
    def get_green_bits(self) -> int: ...
    def get_blue_bits(self) -> int: ...
    def get_alpha_bits(self) -> int: ...
    def get_stencil_bits(self) -> int: ...
    def get_accum_bits(self) -> int: ...
    def get_aux_rgba(self) -> int: ...
    def get_aux_hrgba(self) -> int: ...
    def get_aux_float(self) -> int: ...
    def get_multisamples(self) -> int: ...
    def get_coverage_samples(self) -> int:
        """If coverage samples are specified, and there is hardware support, we use
        coverage multisampling.
        """
    def get_back_buffers(self) -> int: ...
    def get_indexed_color(self) -> bool: ...
    def get_rgb_color(self) -> bool: ...
    def get_stereo(self) -> bool: ...
    def get_force_hardware(self) -> bool: ...
    def get_force_software(self) -> bool: ...
    def get_srgb_color(self) -> bool: ...
    def get_float_color(self) -> bool: ...
    def get_float_depth(self) -> bool: ...
    def set_depth_bits(self, n: int) -> None:
        """Individual assigners."""
    def set_color_bits(self, n: int) -> None:
        """Sets the number of requested color bits as a single number that represents
        the sum of the individual numbers of red, green and blue bits.  Panda won't
        care how the individual bits are divided up.

        See also set_rgba_bits, which allows you to specify requirements for the
        individual components.
        """
    def set_rgba_bits(self, r: int, g: int, b: int, a: int) -> None:
        """Convenience method for setting the red, green, blue and alpha bits in one
        go.
        """
    def set_red_bits(self, n: int) -> None: ...
    def set_green_bits(self, n: int) -> None: ...
    def set_blue_bits(self, n: int) -> None: ...
    def set_alpha_bits(self, n: int) -> None: ...
    def set_stencil_bits(self, n: int) -> None: ...
    def set_accum_bits(self, n: int) -> None: ...
    def set_aux_rgba(self, n: int) -> None: ...
    def set_aux_hrgba(self, n: int) -> None: ...
    def set_aux_float(self, n: int) -> None: ...
    def set_multisamples(self, n: int) -> None: ...
    def set_coverage_samples(self, n: int) -> None:
        """If coverage samples are specified, and there is hardware support, we use
        coverage multisampling
        """
    def set_back_buffers(self, n: int) -> None: ...
    def set_indexed_color(self, n: bool) -> None: ...
    def set_rgb_color(self, n: bool) -> None: ...
    def set_stereo(self, n: bool) -> None: ...
    def set_force_hardware(self, n: bool) -> None: ...
    def set_force_software(self, n: bool) -> None: ...
    def set_srgb_color(self, n: bool) -> None: ...
    def set_float_color(self, n: bool) -> None: ...
    def set_float_depth(self, n: bool) -> None: ...
    @staticmethod
    def get_default() -> FrameBufferProperties:
        """Returns a FrameBufferProperties structure with all of the default values
        filled in according to the user's config file.
        """
    def clear(self) -> None:
        """Unsets all properties that have been specified so far, and resets the
        FrameBufferProperties structure to its initial empty state.
        """
    def set_all_specified(self) -> None:
        """Marks all bits as having been specified."""
    def subsumes(self, other: FrameBufferProperties) -> bool:
        """Returns true if this set of properties makes strictly greater or equal
        demands of the framebuffer than the other set of framebuffer properties.
        """
    def add_properties(self, other: FrameBufferProperties) -> None:
        """Sets any properties that are explicitly specified in other on this object.
        Leaves other properties unchanged.
        """
    def output(self, out: ostream) -> None:
        """Generates a string representation."""
    def set_one_bit_per_channel(self) -> None:
        """If any of the depth, color, alpha, accum, or stencil properties is set to
        more than one, then they are reduced to one.
        """
    def is_stereo(self) -> bool: ...
    def is_single_buffered(self) -> bool: ...
    def get_quality(self, reqs: FrameBufferProperties) -> int:
        """Assumes that these properties are a description of a window.

        Measures how well this window satisfies a specified set of requirements.  A
        higher quality number means that more requirements were satisfied.  A
        quality of zero means that the window is unsuitable.

        The routine deducts a lot if the window fails to provide a requested
        feature.  It deducts less if the window provides a feature, but at a
        degraded level of functionality (ie, the user asks for rgba8, color, but
        the window only provides rgba4).  The routine also deducts a small amount
        for unnecessary features.  For example, if the window has an accumulation
        buffer when one is not requested will reduce quality slightly.  Maximum
        quality is obtained when the window exactly matches the request.

        If you want to know whether the window satisfies all of the requirements,
        use the "subsumes" function.
        """
    def is_any_specified(self) -> bool:
        """Returns true if any properties have been specified, false otherwise."""
    def is_basic(self) -> bool:
        """Returns true if the properties are extremely basic.  The following count as
        basic: rgb or rgba, depth.  If anything else is specified, the properties
        are non-basic.
        """
    def get_aux_mask(self) -> int:
        """Converts the aux bitplanes of the framebuffer into a RenderBuffer::Type."""
    def get_buffer_mask(self) -> int:
        """Converts the non-aux bitplanes of the framebuffer into a
        RenderBuffer::Type.
        """
    def verify_hardware_software(self, props: FrameBufferProperties, renderer: str) -> bool:
        """Validates that the properties represent the desired kind of renderer
        (hardware or software).  If not, prints out an error message and returns
        false.
        """
    def setup_color_texture(self, tex: Texture) -> bool:
        """Sets the texture up for render-to-texture matching these framebuffer
        properties.

        Returns true if there was a format that had enough bits, false otherwise.
        Of course, this is no guarantee that a particular graphics back-end
        supports rendering to textures of that format.
        """
    def setup_depth_texture(self, tex: Texture) -> bool:
        """Sets the texture up for render-to-texture matching these framebuffer
        properties.

        Returns true if there was a format that had enough bits, false otherwise.
        Of course, this is no guarantee that a particular graphics back-end
        supports rendering to textures of that format.
        """
    getDepthBits = get_depth_bits
    getColorBits = get_color_bits
    getRedBits = get_red_bits
    getGreenBits = get_green_bits
    getBlueBits = get_blue_bits
    getAlphaBits = get_alpha_bits
    getStencilBits = get_stencil_bits
    getAccumBits = get_accum_bits
    getAuxRgba = get_aux_rgba
    getAuxHrgba = get_aux_hrgba
    getAuxFloat = get_aux_float
    getMultisamples = get_multisamples
    getCoverageSamples = get_coverage_samples
    getBackBuffers = get_back_buffers
    getIndexedColor = get_indexed_color
    getRgbColor = get_rgb_color
    getStereo = get_stereo
    getForceHardware = get_force_hardware
    getForceSoftware = get_force_software
    getSrgbColor = get_srgb_color
    getFloatColor = get_float_color
    getFloatDepth = get_float_depth
    setDepthBits = set_depth_bits
    setColorBits = set_color_bits
    setRgbaBits = set_rgba_bits
    setRedBits = set_red_bits
    setGreenBits = set_green_bits
    setBlueBits = set_blue_bits
    setAlphaBits = set_alpha_bits
    setStencilBits = set_stencil_bits
    setAccumBits = set_accum_bits
    setAuxRgba = set_aux_rgba
    setAuxHrgba = set_aux_hrgba
    setAuxFloat = set_aux_float
    setMultisamples = set_multisamples
    setCoverageSamples = set_coverage_samples
    setBackBuffers = set_back_buffers
    setIndexedColor = set_indexed_color
    setRgbColor = set_rgb_color
    setStereo = set_stereo
    setForceHardware = set_force_hardware
    setForceSoftware = set_force_software
    setSrgbColor = set_srgb_color
    setFloatColor = set_float_color
    setFloatDepth = set_float_depth
    getDefault = get_default
    setAllSpecified = set_all_specified
    addProperties = add_properties
    setOneBitPerChannel = set_one_bit_per_channel
    isStereo = is_stereo
    isSingleBuffered = is_single_buffered
    getQuality = get_quality
    isAnySpecified = is_any_specified
    isBasic = is_basic
    getAuxMask = get_aux_mask
    getBufferMask = get_buffer_mask
    verifyHardwareSoftware = verify_hardware_software
    setupColorTexture = setup_color_texture
    setupDepthTexture = setup_depth_texture

class GraphicsWindowInputDevice(InputDevice):
    """This is a virtual input device that represents the keyboard and mouse pair
    that is associated with a particular window.  It collects mouse and
    keyboard events from the windowing system while the window is in focus.
    """

    def button_down(self, button: ButtonHandle | str, time: float = ...) -> None:
        """The following interface is for the various kinds of GraphicsWindows to
        record the data incoming on the device.
        """
    def button_resume_down(self, button: ButtonHandle | str, time: float = ...) -> None:
        """Records that the indicated button was depressed earlier, and we only just
        detected the event after the fact.  This is mainly useful for tracking the
        state of modifier keys.
        """
    def button_up(self, button: ButtonHandle | str, time: float = ...) -> None:
        """Records that the indicated button has been released."""
    def keystroke(self, keycode: int, time: float = ...) -> None:
        """Records that the indicated keystroke has been generated."""
    def candidate(self, candidate_string: str, highlight_start: int, highlight_end: int, cursor_pos: int) -> None:
        """Records that the indicated candidate string has been highlighted.  This is
        used to implement IME support for typing in international languages,
        especially Chinese/Japanese/Korean.
        """
    def focus_lost(self, time: float = ...) -> None:
        """This should be called when the window focus is lost, so that we may miss
        upcoming button events (especially "up" events) for the next period of
        time.  It generates keyboard and mouse "up" events for those buttons that
        we previously sent unpaired "down" events, so that the Panda application
        will believe all buttons are now released.
        """
    def raw_button_down(self, button: ButtonHandle | str, time: float = ...) -> None:
        """Records that the indicated button has been depressed."""
    def raw_button_up(self, button: ButtonHandle | str, time: float = ...) -> None:
        """Records that the indicated button has been released."""
    def get_pointer(self) -> PointerData:
        """Returns the PointerData associated with the input device's pointer.  This
        only makes sense if has_pointer() also returns true.
        """
    def set_pointer_in_window(self, x: float, y: float, time: float = ...) -> None:
        """To be called by a particular kind of GraphicsWindow to indicate that the
        pointer is within the window, at the given pixel coordinates.
        """
    def set_pointer_out_of_window(self, time: float = ...) -> None:
        """To be called by a particular kind of GraphicsWindow to indicate that the
        pointer is no longer within the window.
        """
    def update_pointer(self, data: PointerData, time: float = ...) -> None:
        """To be called by a particular kind of GraphicsWindow to indicate that the
        pointer data has changed.
        """
    def pointer_moved(self, x: float, y: float, time: float = ...) -> None:
        """To be called by a particular kind of GraphicsWindow to indicate that the
        pointer has moved by the given relative amount.
        """
    def remove_pointer(self, id: int) -> None:
        """To be called by a particular kind of GraphicsWindow to indicate that the
        pointer no longer exists.
        """
    buttonDown = button_down
    buttonResumeDown = button_resume_down
    buttonUp = button_up
    focusLost = focus_lost
    rawButtonDown = raw_button_down
    rawButtonUp = raw_button_up
    getPointer = get_pointer
    setPointerInWindow = set_pointer_in_window
    setPointerOutOfWindow = set_pointer_out_of_window
    updatePointer = update_pointer
    pointerMoved = pointer_moved
    removePointer = remove_pointer

class TouchInfo:
    """Stores information for a single touch event."""

    TIF_move: Final = 1
    TIFMove: Final = 1
    TIF_down: Final = 2
    TIFDown: Final = 2
    TIF_up: Final = 4
    TIFUp: Final = 4
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: TouchInfo) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_x(self) -> int: ...
    def get_y(self) -> int: ...
    def get_id(self) -> int: ...
    def get_flags(self) -> int: ...
    getX = get_x
    getY = get_y
    getId = get_id
    getFlags = get_flags

class GraphicsWindowProcCallbackData(CallbackData):
    """This specialization on CallbackData is passed when the callback is
    initiated from from an implementation of the GraphicsWindowProc class, such
    as PythonGraphicsWindowProc.
    """

    def get_hwnd(self) -> int:
        """Returns the Windows proc hwnd parameter."""
    def get_msg(self) -> int:
        """Returns the Windows proc msg parameter."""
    def get_wparam(self) -> int:
        """Returns the Windows proc wparam parameter."""
    def get_lparam(self) -> int:
        """Returns the Windows proc lparam parameter."""
    def is_touch_event(self) -> bool:
        """Returns whether the event is a touch event."""
    def get_num_touches(self) -> int:
        """Returns the current number of touches on the window."""
    def get_touch_info(self, index: int) -> TouchInfo:
        """Returns the TouchInfo object describing the specified touch."""
    getHwnd = get_hwnd
    getMsg = get_msg
    getWparam = get_wparam
    getLparam = get_lparam
    isTouchEvent = is_touch_event
    getNumTouches = get_num_touches
    getTouchInfo = get_touch_info

class GraphicsWindow(GraphicsOutput):
    """A window, fullscreen or on a desktop, into which a graphics device sends
    its output for interactive display.
    """

    window_event: str
    close_request_event: str
    unexposed_draw: bool
    @property
    def properties(self) -> WindowProperties: ...
    @property
    def requested_properties(self) -> WindowProperties: ...
    @property
    def rejected_properties(self) -> WindowProperties: ...
    @property
    def closed(self) -> bool: ...
    @property
    def window_handle(self) -> WindowHandle: ...
    def get_properties(self) -> WindowProperties:
        """Returns the current properties of the window."""
    def get_requested_properties(self) -> WindowProperties:
        """Returns the properties of the window that are currently requested.  These
        properties will be applied to the window (if valid) at the next execution
        of process_events().
        """
    def clear_rejected_properties(self) -> None:
        """Empties the set of failed properties that will be returned by
        get_rejected_properties().
        """
    def get_rejected_properties(self) -> WindowProperties:
        """Returns the set of properties that have recently been requested, but could
        not be applied to the window for some reason.  This set of properties will
        remain unchanged until they are changed by a new failed request, or
        clear_rejected_properties() is called.
        """
    def request_properties(self, requested_properties: WindowProperties) -> None:
        """Requests a property change on the window.  For example, use this method to
        request a window change size or minimize or something.

        The change is not made immediately; rather, the request is saved and will
        be applied the next time the window task is run (probably at the next
        frame).
        """
    def is_closed(self) -> bool:
        """Returns true if the window has not yet been opened, or has been fully
        closed, false if it is open.  The window is not opened immediately after
        GraphicsEngine::make_output() is called; nor is it closed immediately after
        GraphicsEngine::remove_window() is called.  Either operation may take a
        frame or two.
        """
    def is_fullscreen(self) -> bool:
        """Returns true if the window has been opened as a fullscreen window, false
        otherwise.
        """
    def set_window_event(self, window_event: str) -> None:
        """Changes the name of the event that is generated when this window is
        modified externally, e.g.  to be resized or closed by the user.

        By default, all windows have the same window event unless they are
        explicitly changed.  When the event is generated, it includes one
        parameter: the window itself.
        """
    def get_window_event(self) -> str:
        """Returns the name of the event that is generated when this window is
        modified externally, e.g.  to be resized or closed by the user.  See
        set_window_event().
        """
    def set_close_request_event(self, close_request_event: str) -> None:
        """Sets the event that is triggered when the user requests to close the
        window, e.g.  via alt-F4, or clicking on the close box.

        The default for each window is for this event to be the empty string, which
        means the window-close request is handled immediately by Panda (and the
        window will be closed without the app getting a chance to intervene).  If
        you set this to a nonempty string, then the window is not closed, but
        instead the event is thrown.  It is then up to the app to respond
        appropriately, for instance by presenting an "are you sure?"  dialog box,
        and eventually calling close_window() when the user is sure.

        It is considered poor form to set this string and then not handle the
        event.  This can frustrate the user by making it difficult for him to
        cleanly shut down the application (and may force the user to hard-kill the
        app, or reboot the machine).
        """
    def get_close_request_event(self) -> str:
        """Returns the name of the event set via set_close_request_event().  If this
        string is nonempty, then when the user requests to close window, this event
        will be generated instead.  See set_close_request_event().
        """
    def set_unexposed_draw(self, unexposed_draw: bool) -> None:
        """If this flag is false, the window is redrawn only after it has received a
        recent "unexpose" or "draw" event from the underlying windowing system.  If
        this flag is true, the window is redrawn every frame regardless.  Setting
        this false may prevent the window from redrawing unnecessarily when it is
        hidden, and may play nicer with other windows on the desktop, but may
        adversely affect frame rate even when the window is fully visible; setting
        it true will ensure that the window contents are always current.
        """
    def get_unexposed_draw(self) -> bool:
        """See set_unexposed_draw()."""
    def get_window_handle(self) -> WindowHandle:
        """Returns the WindowHandle corresponding to this window on the desktop.  This
        is mainly useful for communicating with external libraries.  Use
        window_handle->get_os_handle()->get_handle(), or
        window_handle->get_string_handle(), to get the actual OS-specific window
        handle object, whatever type that might be.
        """
    def get_num_input_devices(self) -> int:
        """Returns the number of separate input devices associated with the window.
        Typically, a window will have exactly one input device: the keyboard/mouse
        pair.  However, some windows may have no input devices, and others may add
        additional devices, for instance for a joystick.
        """
    def get_input_device(self, i: int) -> InputDevice:
        """Returns the nth input device associated with the window.  Typically, a
        window will have exactly one input device: the keyboard/mouse pair.
        """
    def get_input_device_name(self, device: int) -> str:
        """Returns the name of the nth input device."""
    def has_pointer(self, device: int) -> bool:
        """Returns true if the nth input device has a screen-space pointer (for
        instance, a mouse), false otherwise.
        """
    def has_keyboard(self, device: int) -> bool:
        """Returns true if the nth input device has a keyboard, false otherwise."""
    def get_keyboard_map(self) -> ButtonMap:
        """Returns a ButtonMap containing the association between raw buttons and
        virtual buttons.
        """
    def enable_pointer_events(self, device: int) -> None:
        """Turn on the generation of pointer events."""
    def disable_pointer_events(self, device: int) -> None:
        """Turn off the generation of pointer events."""
    def get_pointer(self, device: int) -> MouseData:
        """Returns the MouseData associated with the nth input device's pointer.
        Using this to access raw mice (with an index other than 0) is deprecated,
        see the InputDeviceManager interface instead.
        """
    def move_pointer(self, device: int, x: int, y: int) -> bool:
        """Forces the pointer to the indicated position within the window, if
        possible.

        Returns true if successful, false on failure.  This may fail if the mouse
        is not currently within the window, or if the API doesn't support this
        operation.
        """
    def close_ime(self) -> None:
        """Forces the ime window to close if any"""
    def get_input_devices(self) -> tuple[InputDevice, ...]: ...
    def get_input_device_names(self) -> tuple[str, ...]: ...
    getProperties = get_properties
    getRequestedProperties = get_requested_properties
    clearRejectedProperties = clear_rejected_properties
    getRejectedProperties = get_rejected_properties
    requestProperties = request_properties
    isClosed = is_closed
    isFullscreen = is_fullscreen
    setWindowEvent = set_window_event
    getWindowEvent = get_window_event
    setCloseRequestEvent = set_close_request_event
    getCloseRequestEvent = get_close_request_event
    setUnexposedDraw = set_unexposed_draw
    getUnexposedDraw = get_unexposed_draw
    getWindowHandle = get_window_handle
    getNumInputDevices = get_num_input_devices
    getInputDevice = get_input_device
    getInputDeviceName = get_input_device_name
    hasPointer = has_pointer
    hasKeyboard = has_keyboard
    getKeyboardMap = get_keyboard_map
    enablePointerEvents = enable_pointer_events
    disablePointerEvents = disable_pointer_events
    getPointer = get_pointer
    movePointer = move_pointer
    closeIme = close_ime
    getInputDevices = get_input_devices
    getInputDeviceNames = get_input_device_names

class CallbackGraphicsWindow(GraphicsWindow):
    """This special window object doesn't represent a window in its own right, but
    instead hooks into some third-party API for creating and rendering to
    windows via callbacks.  This can be used to allow Panda to render into an
    already-created OpenGL context, for instance.
    """

    class WindowCallbackData(CallbackData):
        DtoolClassDict: ClassVar[dict[str, Any]]
        @property
        def window(self) -> CallbackGraphicsWindow: ...
        def get_window(self) -> CallbackGraphicsWindow:
            """Returns the window this callback was triggered from."""
        @staticmethod
        def get_class_type() -> TypeHandle: ...
        getWindow = get_window
        getClassType = get_class_type

    class EventsCallbackData(CallbackGraphicsWindow.WindowCallbackData):  # noqa: F821
        DtoolClassDict: ClassVar[dict[str, Any]]
        @staticmethod
        def get_class_type() -> TypeHandle: ...
        getClassType = get_class_type

    class PropertiesCallbackData(CallbackGraphicsWindow.WindowCallbackData):  # noqa: F821
        DtoolClassDict: ClassVar[dict[str, Any]]
        def get_properties(self) -> WindowProperties:
            """Returns the WindowProperties object that this callback should process.  Any
            properties that are handled should be removed from this object; properties
            that are unhandled should be left alone.
            """
        @staticmethod
        def get_class_type() -> TypeHandle: ...
        getProperties = get_properties
        getClassType = get_class_type

    class RenderCallbackData(CallbackGraphicsWindow.WindowCallbackData):  # noqa: F821
        DtoolClassDict: ClassVar[dict[str, Any]]
        render_flag: bool
        @property
        def callback_type(self) -> _CallbackGraphicsWindow_RenderCallbackType: ...
        @property
        def frame_mode(self) -> _GraphicsOutput_FrameMode: ...
        def get_callback_type(self) -> _CallbackGraphicsWindow_RenderCallbackType:
            """Since the render callback is shared for several functions, this method is
            needed to indicate which particular function is being invoked with this
            callback.
            """
        def get_frame_mode(self) -> _GraphicsOutput_FrameMode:
            """If the callback type (returned by get_callback_type) is RCT_begin_frame or
            RCT_end_frame, then this method will return the particular frame mode
            indicating what, precisely, we want to do this frame.
            """
        def set_render_flag(self, render_flag: bool) -> None:
            """If the callback type is RCT_begin_frame, this call is available to specify
            the return value from the begin_frame() call.  If this is true (the
            default), the frame is rendered normally; if it is false, the frame is
            omitted.
            """
        def get_render_flag(self) -> bool:
            """Returns the current setting of the render flag.  See set_render_flag()."""
        @staticmethod
        def get_class_type() -> TypeHandle: ...
        getCallbackType = get_callback_type
        getFrameMode = get_frame_mode
        setRenderFlag = set_render_flag
        getRenderFlag = get_render_flag
        getClassType = get_class_type

    RCT_begin_frame: Final = 0
    RCTBeginFrame: Final = 0
    RCT_end_frame: Final = 1
    RCTEndFrame: Final = 1
    RCT_begin_flip: Final = 2
    RCTBeginFlip: Final = 2
    RCT_end_flip: Final = 3
    RCTEndFlip: Final = 3
    def set_events_callback(self, object: Callable | CallbackObject) -> None:
        """Sets the CallbackObject that will be notified when this window is polled
        for window events, including mouse and keyboard events, as well as window
        resize events and other system-generated events.

        This callback will receive a CallbackGraphicsWindow::EventsCallbackData.

        This callback should process any system-generated events, and call
        data->upcall() to process requested property change requests made via
        request_properties().
        """
    def clear_events_callback(self) -> None:
        """Removes the callback set by an earlier call to set_events_callback()."""
    def get_events_callback(self) -> CallbackObject:
        """Returns the CallbackObject set by set_events_callback()."""
    def set_properties_callback(self, object: Callable | CallbackObject) -> None:
        """Sets the CallbackObject that will be notified when this window receives a
        property change request from user code (e.g.  via request_properties).

        This callback will receive a
        CallbackGraphicsWindow::PropertiesCallbackData, which provides a
        get_properties() method that returns a modifiable reference to a
        WindowsProperties object.  This object will contain only those properties
        requested by user code.  The callback should handle any of the requests it
        finds, including and especially set_open(), and remove them from the object
        when it has handled them.  Any unhandled properties should be left
        unchanged in the properties object.
        """
    def clear_properties_callback(self) -> None:
        """Removes the callback set by an earlier call to set_properties_callback()."""
    def get_properties_callback(self) -> CallbackObject:
        """Returns the CallbackObject set by set_properties_callback()."""
    def set_render_callback(self, object: Callable | CallbackObject) -> None:
        """Sets the CallbackObject that will be notified when this window is invoked
        (in the draw thread) to render its contents, and/or flip the graphics
        buffers.

        This callback will actually serve several different functions.  It
        receivces a RenderCallbackData, and you can query data->get_callback_type()
        to return the actual function of each particular callback.
        """
    def clear_render_callback(self) -> None:
        """Removes the callback set by an earlier call to set_render_callback()."""
    def get_render_callback(self) -> CallbackObject:
        """Returns the CallbackObject set by set_render_callback()."""
    def create_input_device(self, name: str) -> int:
        """Adds a new input device (mouse) to the window with the indicated name.
        Returns the index of the new device.
        """
    setEventsCallback = set_events_callback
    clearEventsCallback = clear_events_callback
    getEventsCallback = get_events_callback
    setPropertiesCallback = set_properties_callback
    clearPropertiesCallback = clear_properties_callback
    getPropertiesCallback = get_properties_callback
    setRenderCallback = set_render_callback
    clearRenderCallback = clear_render_callback
    getRenderCallback = get_render_callback
    createInputDevice = create_input_device

class DisplayMode:
    DtoolClassDict: ClassVar[dict[str, Any]]
    width: int
    height: int
    bits_per_pixel: int
    refresh_rate: int
    fullscreen_only: int
    def __init__(self, __param0: DisplayMode = ...) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def output(self, out: ostream) -> None: ...

class DisplayRegionCullCallbackData(CallbackData):
    """This specialization on CallbackData is passed when the callback is
    initiated from the cull traversal, for a DisplayRegion.
    """

    def get_scene_setup(self) -> SceneSetup:
        """Returns a pointer to the SceneSetup object, which contains information
        about the camera and such.
        """
    getSceneSetup = get_scene_setup

class DisplayRegionDrawCallbackData(CallbackData):
    """This specialization on CallbackData is passed when the callback is
    initiated from the draw traversal, for a DisplayRegion.
    """

    def get_cull_result(self) -> CullResult:
        """Returns a pointer to the CullResult, the list of CullableObjects that
        should be drawn in this DisplayRegion.
        """
    def get_scene_setup(self) -> SceneSetup:
        """Returns a pointer to the SceneSetup object, which contains information
        about the camera and such.
        """
    getCullResult = get_cull_result
    getSceneSetup = get_scene_setup

class DisplaySearchParameters:
    """Parameters used for searching display capabilities."""

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: DisplaySearchParameters = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_minimum_width(self, minimum_width: int) -> None: ...
    def set_maximum_width(self, maximum_width: int) -> None: ...
    def set_minimum_height(self, minimum_height: int) -> None: ...
    def set_maximum_height(self, maximum_height: int) -> None: ...
    def set_minimum_bits_per_pixel(self, minimum_bits_per_pixel: int) -> None: ...
    def set_maximum_bits_per_pixel(self, maximum_bits_per_pixel: int) -> None: ...
    setMinimumWidth = set_minimum_width
    setMaximumWidth = set_maximum_width
    setMinimumHeight = set_minimum_height
    setMaximumHeight = set_maximum_height
    setMinimumBitsPerPixel = set_minimum_bits_per_pixel
    setMaximumBitsPerPixel = set_maximum_bits_per_pixel

class GraphicsBuffer(GraphicsOutput):
    """An offscreen buffer for rendering into.  This is similar in function to a
    GraphicsWindow, except that the output is not visible to the user.
    """

    def set_size(self, x: int, y: int) -> None:
        """This is called by the GraphicsEngine to request that the buffer resize
        itself.  Although calls to get the size will return the new value, much of
        the actual resizing work doesn't take place until the next begin_frame.
        Not all buffers are resizeable.
        """
    setSize = set_size

class GraphicsPipeSelection:
    """This maintains a list of GraphicsPipes by type that are available for
    creation.  Normally there is one default interactive GraphicsPipe, and
    possibly other types available as well.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def pipe_types(self) -> Sequence[TypeHandle]: ...
    def get_num_pipe_types(self) -> int:
        """Returns the number of different types of GraphicsPipes that are available
        to create through this interface.
        """
    def get_pipe_type(self, n: int) -> TypeHandle:
        """Returns the nth type of GraphicsPipe available through this interface."""
    def print_pipe_types(self) -> None:
        """Writes a list of the currently known GraphicsPipe types to nout, for the
        user's information.
        """
    @overload
    def make_pipe(self, type: TypeHandle | type) -> GraphicsPipe:
        """`(self, type: TypeHandle)`:
        Creates a new GraphicsPipe of the indicated type (or a type more specific
        than the indicated type, if necessary) and returns it.  Returns NULL if the
        type cannot be matched.

        `(self, type_name: str, module_name: str = ...)`:
        Creates a new GraphicsPipe of the indicated type (or a type more specific
        than the indicated type, if necessary) and returns it.  Returns NULL if the
        type cannot be matched.

        If the type is not already defined, this will implicitly load the named
        module, or if module_name is empty, it will call load_aux_modules().
        """
    @overload
    def make_pipe(self, type_name: str, module_name: str = ...) -> GraphicsPipe: ...
    def make_module_pipe(self, module_name: str) -> GraphicsPipe:
        """Returns a new GraphicsPipe of a type defined by the indicated module.
        Returns NULL if the module is not found or does not properly recommend a
        GraphicsPipe.
        """
    def make_default_pipe(self) -> GraphicsPipe:
        """Creates a new GraphicsPipe of some arbitrary type.  The user may specify a
        preference using the Configrc file; otherwise, one will be chosen
        arbitrarily.
        """
    def get_num_aux_modules(self) -> int:
        """Returns the number of display modules that are still to be loaded.  If this
        is nonzero, then calling load_aux_modules() will likely increase the number
        of GraphicsPipes available.
        """
    def load_aux_modules(self) -> None:
        """Loads all the modules named in the aux-display Configrc variable, making as
        many graphics pipes as possible available.
        """
    @staticmethod
    def get_global_ptr() -> GraphicsPipeSelection:
        """Returns a pointer to the one global GraphicsPipeSelection object."""
    def get_pipe_types(self) -> tuple[TypeHandle, ...]: ...
    getNumPipeTypes = get_num_pipe_types
    getPipeType = get_pipe_type
    printPipeTypes = print_pipe_types
    makePipe = make_pipe
    makeModulePipe = make_module_pipe
    makeDefaultPipe = make_default_pipe
    getNumAuxModules = get_num_aux_modules
    loadAuxModules = load_aux_modules
    getGlobalPtr = get_global_ptr
    getPipeTypes = get_pipe_types

class MouseAndKeyboard(DataNode):
    """Reads the mouse and/or keyboard data sent from a GraphicsWindow, and
    transmits it down the data graph.

    The mouse and keyboard devices are bundled together into one device here,
    because they interrelate so much.  A mouse might be constrained by the
    holding down of the shift key, for instance, or the clicking of the mouse
    button might be handled in much the same way as a keyboard key.

    Mouse data is sent down the data graph as an x,y position as well as the
    set of buttons currently being held down; keyboard data is sent down as a
    set of keypress events in an EventDataTransition.  To throw these events to
    the system, you must attach an EventThrower to the MouseAndKeyboard object;
    otherwise, the events will be discarded.
    """

    @overload
    def __init__(self, __param0: MouseAndKeyboard) -> None: ...
    @overload
    def __init__(self, window: GraphicsWindow, device: int, name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_source(self, window: GraphicsWindow, device: int) -> None:
        """Redirects the class to get the data from the mouse and keyboard associated
        with a different window and/or device number.
        """
    setSource = set_source

@final
class NativeWindowHandle(WindowHandle):
    """This subclass of WindowHandle exists to allow simple creation of a
    WindowHandle of the appropriate type to the current OS.

    This class exists for name scoping only.  Don't use the constructor
    directly; use one of the make_* methods.
    """

    @staticmethod
    def make_int(window: int) -> WindowHandle:
        """Constructs a new WindowHandle with an int value, which is understood to be
        either an HWND or a Window, cast to int.  This method exists for the
        convenience of Python, which likes to deal with ints; C++ code should use
        one of the more specific make_x11() or make_win32() methods instead.
        """
    @staticmethod
    def make_subprocess(filename: StrOrBytesPath) -> WindowHandle:
        """Constructs a new WindowHandle that references a SubprocessWindowBuffer read
        in another process, with the named pipe filename that it uses for
        communication.

        This is (at present, and maybe always) useful only on the OS X platform,
        where parenting child windows is particularly problematic.
        """
    makeInt = make_int
    makeSubprocess = make_subprocess

class ParasiteBuffer(GraphicsOutput):
    """This is a special GraphicsOutput type that acts a lot like a
    GraphicsBuffer, effectively allowing rendering to an offscreen buffer,
    except it does not create any framebuffer space for itself.  Instead, it
    renders into the framebuffer owned by some other GraphicsOutput.

    The x_size and y_size must therefore fit within the bounds of the source
    GraphicsOutput.

    Since the framebuffer will be subsequently cleared when the actual owner
    draws in it later, this only makes sense if we are going to copy the
    contents of the framebuffer to a texture immediately after we draw it.
    Thus, has_texture() is implicitly true for a ParasiteBuffer.

    This class is useful to render offscreen to a texture while preventing the
    waste of framebuffer memory for API's that are unable to render directly
    into a texture (and must render into a separate framebuffer first and then
    copy to texture).  It is also the only way to render to a texture on API's
    that do not support offscreen rendering.
    """

    def set_size(self, x: int, y: int) -> None:
        """This is called by the GraphicsEngine to request that the buffer resize
        itself.  Although calls to get the size will return the new value, much of
        the actual resizing work doesn't take place until the next begin_frame.
        Not all buffers are resizeable.
        """
    setSize = set_size
