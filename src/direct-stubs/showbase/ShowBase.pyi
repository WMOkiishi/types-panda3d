__all__ = ['ShowBase', 'WindowControls']

from types import ModuleType
from typing import Any, ClassVar, overload
from typing_extensions import Literal, TypeAlias

from direct._typing import SimpleCallback, Unused
from direct.directnotify.Notifier import Notifier
from direct.directtools.DirectSession import DirectSession
from direct.p3d.AppRunner import AppRunner
from direct.showutil.TexMemWatcher import TexMemWatcher
from direct.task.Task import Task, TaskManager
from panda3d._typing import Filepath, Vec4Like
from panda3d.core import (
    AudioManager,
    AudioSound,
    BitMask32,
    ButtonThrower,
    Camera,
    ClockObject,
    CollisionTraverser,
    DataGraphTraverser,
    DisplayRegion,
    DriveInterface,
    FrameBufferProperties,
    FrameRateMeter,
    GeomNode,
    GraphicsEngine,
    GraphicsOutput,
    GraphicsPipe,
    GraphicsWindow,
    InputDevice,
    InputDeviceManager,
    LColor,
    Lens,
    LRGBColor,
    LVecBase2i,
    ModelNode,
    MouseInterfaceNode,
    MouseWatcher,
    NodePath,
    PandaNode,
    PGTop,
    RecorderController,
    SceneGraphAnalyzerMeter,
    Texture,
    Trackball,
    Transform2SG,
    WindowProperties,
)
from panda3d.physics import ParticleSystemManager, PhysicsManager
from .BufferViewer import BufferViewer
from .BulletinBoard import BulletinBoard
from .DirectObject import DirectObject
from .EventManager import EventManager
from .JobManager import JobManager
from .Loader import Loader
from .Messenger import Messenger
from .PythonUtil import Stack
from .Transitions import Transitions

_WindowType: TypeAlias = Literal['onscreen', 'offscreen', 'none']

def exitfunc() -> None: ...

class ShowBase(DirectObject):
    config: ClassVar[ModuleType]
    notify: ClassVar[Notifier]
    __dev__: bool
    mainDir: str
    main_dir: str
    appRunner: AppRunner | None
    app_runner: AppRunner | None
    debugRunningMultiplier: int
    nextWindowIndex: int
    sfxActive: bool
    musicActive: bool
    wantFog: bool
    wantRender2dp: bool
    screenshotExtension: str
    musicManager: AudioManager
    musicManagerIsValid: bool
    sfxManagerList: list[AudioManager]
    sfxManagerIsValidList: list[bool]
    wantStats: bool
    wantTk: bool
    wantWx: bool
    wantDirect: bool
    exitFunc: SimpleCallback | None
    finalExitCallbacks: list[SimpleCallback]
    windowType: _WindowType
    requireWindow: bool
    win: GraphicsEngine
    frameRateMeter: FrameRateMeter | None
    sceneGraphAnalyzerMeter: SceneGraphAnalyzerMeter | None
    winList: list[GraphicsEngine]
    winControls: list[WindowControls]
    mainWinMinimized: bool
    mainWinForeground: bool
    pipe: GraphicsPipe
    pipeList: list[GraphicsPipe]
    mouse2cam: NodePath[Transform2SG]
    buttonThrowers: list[ButtonThrower]
    mouseWatcher: NodePath[MouseWatcher]
    mouseWatcherNode: MouseWatcher
    pointerWatcherNodes: list[MouseWatcher]
    mouseInterface: NodePath[MouseInterfaceNode]
    mouseInterfaceNode: MouseInterfaceNode
    drive: NodePath[DriveInterface]
    trackball: NodePath[Trackball]
    texmem: TexMemWatcher | None
    showVertices: NodePath[Camera] | None
    deviceButtonThrowers: list[NodePath[ButtonThrower]]
    cam: NodePath[Camera]
    cam2d: NodePath[Camera]
    cam2dp: NodePath[Camera]
    camera: NodePath[ModelNode]
    camera2d: NodePath[PandaNode]
    camera2dp: NodePath[PandaNode]
    camList: list[NodePath[Camera]]
    camNode: Camera
    camLens: Lens
    camFrustumVis: NodePath[GeomNode] | None
    direct: DirectSession | None
    wxApp: Any
    wxAppCreated: bool
    tkRoot: Any
    tkRootCreated: bool
    clusterSyncFlag: bool
    hidden: NodePath[PandaNode]
    graphicsEngine: GraphicsEngine
    graphics_engine: GraphicsEngine
    cTrav: CollisionTraverser | Literal[0]
    shadowTrav: CollisionTraverser | Literal[0]
    cTravStack: Stack[CollisionTraverser]
    appTrav: CollisionTraverser | Literal[0]
    dgTrav: DataGraphTraverser
    recorder: RecorderController | None
    loader: Loader
    eventMgr: EventManager
    messenger: Messenger
    bboard: BulletinBoard
    taskMgr: TaskManager
    task_mgr: TaskManager
    jobMgr: JobManager
    particleMgr: ParticleSystemManager | None
    particleMgrEnabled: bool
    physicsMgr: PhysicsManager | None
    phyiscsMgrEnabled: bool
    physicsMgrAngular: bool
    devices: InputDeviceManager
    AppHasAudioFocus: bool
    clock: ClockObject
    transitions: Transitions
    clientSleep: float
    multiClientSleep: bool
    bufferViewer: BufferViewer
    render: NodePath[PandaNode]
    backfaceCullingEnabled: bool
    textureEnabled: bool
    wireframeEnabled: bool
    render2d: NodePath[PandaNode]
    a2dBackground: NodePath[PandaNode]
    a2dTop: float
    a2dBottom: float
    a2dLeft: float
    a2dRight: float
    a2dTopCenter: NodePath[PandaNode]
    a2dTopCenterNs: NodePath[PandaNode]
    a2dBottomCenter: NodePath[PandaNode]
    a2dBottomCenterNs: NodePath[PandaNode]
    a2dLeftCenter: NodePath[PandaNode]
    a2dLeftCenterNs: NodePath[PandaNode]
    a2dRightCenter: NodePath[PandaNode]
    a2dRightCenterNs: NodePath[PandaNode]
    a2dTopLeft: NodePath[PandaNode]
    a2dTopLeftNs: NodePath[PandaNode]
    a2dTopRight: NodePath[PandaNode]
    a2dTopRightNs: NodePath[PandaNode]
    a2dBottomLeft: NodePath[PandaNode]
    a2dBottomLeftNs: NodePath[PandaNode]
    a2dBottomRight: NodePath[PandaNode]
    a2dBottomRightNs: NodePath[PandaNode]
    pixel2d: NodePath[PGTop]
    render2dp: NodePath[PandaNode]
    aspect2dp: NodePath[PGTop]
    a2dpTop: float
    a2dpBottom: float
    a2dpLeft: float
    a2dpRight: float
    a2dpTopCenter: NodePath[PandaNode]
    a2dpBottomCenter: NodePath[PandaNode]
    a2dpLeftCenter: NodePath[PandaNode]
    a2dpRightCenter: NodePath[PandaNode]
    a2dpTopLeft: NodePath[PandaNode]
    a2dpTopRight: NodePath[PandaNode]
    a2dpBottomLeft: NodePath[PandaNode]
    a2dpBottomRight: NodePath[PandaNode]
    pixel2dp: NodePath[PGTop]
    dataRoot: NodePath[PandaNode]
    dataRootNode: PandaNode
    def __init__(self, fStartDirect: bool = ..., windowType: _WindowType | None = ...) -> None: ...
    def pushCTrav(self, cTrav: CollisionTraverser) -> None: ...
    def popCTrav(self) -> None: ...
    def getExitErrorCode(self) -> Literal[0]: ...
    def printEnvDebugInfo(self) -> None: ...
    def destroy(self) -> None: ...
    def make_default_pipe(self, printPipeTypes: bool | None = ...) -> None: ...
    def make_module_pipe(self, moduleName: str) -> GraphicsPipe: ...
    def make_all_pipes(self) -> None: ...
    def open_window(
        self,
        props: WindowProperties | None = ...,
        fbprops: FrameBufferProperties | None = ...,
        pipe: GraphicsPipe | None = ...,
        gsg: GraphicsOutput | None = ...,
        host: GraphicsOutput | None = ...,
        type: _WindowType | None = ...,
        name: str | None = ...,
        size: LVecBase2i | tuple[int, int] | None = ...,
        aspectRatio: float | None = ...,
        makeCamera: bool = ...,
        keepCamera: bool = ...,
        scene: NodePath | None = ...,
        stereo: bool | None = ...,
        unexposedDraw: bool | None = ...,
        callbackWindowDict: dict[str, SimpleCallback] | None = ...,
        requireWindow: bool | None = ...,
    ) -> GraphicsWindow: ...
    def close_window(self, win: GraphicsOutput, keepCamera: bool = ..., removeWindow: bool = ...) -> None: ...
    def open_default_window(
        self,
        props: WindowProperties | None = ...,
        fbprops: FrameBufferProperties | None = ...,
        pipe: GraphicsPipe | None = ...,
        gsg: GraphicsOutput | None = ...,
        host: GraphicsOutput | None = ...,
        type: _WindowType | None = ...,
        name: str | None = ...,
        size: LVecBase2i | tuple[int, int] | None = ...,
        aspectRatio: float | None = ...,
        makeCamera: bool = ...,
        keepCamera: bool = ...,
        scene: NodePath | None = ...,
        stereo: bool | None = ...,
        unexposedDraw: bool | None = ...,
        callbackWindowDict: dict[str, SimpleCallback] | None = ...,
        requireWindow: bool | None = ...,
    ) -> bool: ...
    def open_main_window(
        self,
        props: WindowProperties | None = ...,
        fbprops: FrameBufferProperties | None = ...,
        pipe: GraphicsPipe | None = ...,
        gsg: GraphicsOutput | None = ...,
        host: GraphicsOutput | None = ...,
        type: _WindowType | None = ...,
        name: str | None = ...,
        size: LVecBase2i | tuple[int, int] | None = ...,
        aspectRatio: float | None = ...,
        makeCamera: bool = ...,
        keepCamera: bool = ...,
        scene: NodePath | None = ...,
        stereo: bool | None = ...,
        unexposedDraw: bool | None = ...,
        callbackWindowDict: dict[str, SimpleCallback] | None = ...,
        requireWindow: bool | None = ...,
    ) -> bool: ...
    def set_sleep(self, amount: float) -> None: ...
    def set_frame_rate_meter(self, flag: bool) -> None: ...
    def set_scene_graph_analyzer_meter(self, flag: bool) -> None: ...
    def setup_window_controls(self, winCtrl: WindowControls | None = ...) -> None: ...
    def setup_render(self) -> None: ...
    def setup_render2d(self) -> None: ...
    def setup_render2dp(self) -> None: ...
    def set_aspect_ratio(self, aspectRatio: float) -> None: ...
    def get_aspect_ratio(self, win: GraphicsEngine | None = ...) -> float: ...
    def get_size(self, win: GraphicsEngine | None = ...) -> tuple[float, float]: ...
    def make_camera(
        self,
        win: GraphicsOutput,
        sort: int = ...,
        scene: NodePath | None = ...,
        displayRegion: Vec4Like | tuple[float, float, float, float] = ...,
        stereo: bool | None = ...,
        aspectRatio: float | None = ...,
        clearDepth: bool = ...,
        clearColor: Vec4Like | None = ...,
        lens: Lens | None = ...,
        camName: str = ...,
        mask: BitMask32 | int | None = ...,
        useCamera: NodePath[Camera] | None = ...,
    ) -> NodePath[Camera]: ...
    def make_camera2d(
        self,
        win: GraphicsOutput,
        sort: int = ...,
        displayRegion: Vec4Like | tuple[float, float, float, float] = ...,
        coords: Vec4Like | tuple[float, float, float, float] = ...,
        lens: Lens | None = ...,
        cameraName: str | None = ...,
    ) -> NodePath[Camera]: ...
    def make_camera2dp(
        self,
        win: GraphicsOutput,
        sort: int = ...,
        displayRegion: Vec4Like | tuple[float, float, float, float] = ...,
        coords: Vec4Like | tuple[float, float, float, float] = ...,
        lens: Lens | None = ...,
        cameraName: str | None = ...,
    ) -> NodePath[Camera]: ...
    def setup_data_graph(self) -> None: ...
    def setup_mouse(self, win: GraphicsWindow, fMultiWin: bool = ...) -> NodePath[ButtonThrower]: ...
    def setup_mouse_cb(self, win: GraphicsWindow) -> tuple[list[NodePath[ButtonThrower]], list[MouseWatcher]]: ...
    def enable_software_mouse_pointer(self) -> None: ...
    def getAlt(self) -> bool: ...
    def getShift(self) -> bool: ...
    def getControl(self) -> bool: ...
    def getMeta(self) -> bool: ...
    def attach_input_device(self, device: InputDevice, prefix: str | None = ..., watch: bool = ...) -> None: ...
    def detach_input_device(self, device: InputDevice) -> None: ...
    def add_angular_integrator(self) -> None: ...
    def enable_particles(self) -> None: ...
    def disable_particles(self) -> None: ...
    def toggle_particles(self) -> None: ...
    def isParticleMgrEnabled(self) -> bool: ...
    def isPhysicsMgrEnabled(self) -> bool: ...
    def updateManagers(self, state: Unused) -> Literal[1]: ...
    def create_stats(self, hostname: str | None = ..., port: int | None = ...) -> bool: ...
    def add_sfx_manager(self, extraSfxManager: AudioManager) -> None: ...
    def createBaseAudioManagers(self) -> None: ...
    def enable_music(self, bEnableMusic: bool) -> None: ...
    def SetAllSfxEnables(self, bEnabled: bool) -> None: ...
    def enable_sound_effects(self, bEnableSoundEffects: bool) -> None: ...
    def disable_all_audio(self) -> None: ...
    def enable_all_audio(self) -> None: ...
    def loadSfx(self, name: Filepath) -> Any: ...
    def loadMusic(self, name: Filepath) -> Any: ...
    def playSfx(
        self,
        sfx: AudioSound,
        looping: bool = ...,
        interrupt: bool = ...,
        volume: float | None = ...,
        time: float = ...,
        node: NodePath | None = ...,
        listener: NodePath | None = ...,
        cutoff: float | None = ...,
    ) -> None: ...
    def playMusic(
        self, music: AudioSound, looping: bool = ..., interrupt: bool = ..., volume: float | None = ..., time: float = ...
    ) -> None: ...
    def init_shadow_trav(self) -> None: ...
    def restart(self, clusterSync: bool = ..., cluster: Any = ...) -> None: ...
    def shutdown(self) -> None: ...
    def get_background_color(self, win: GraphicsEngine | None = ...) -> LColor: ...
    @overload
    def set_background_color(
        self, r: LColor | LRGBColor, g: None = ..., b: None = ..., a: float = ..., win: GraphicsEngine | None = ...
    ) -> None: ...
    @overload
    def set_background_color(self, r: float, g: float, b: float, a: float = ..., win: GraphicsEngine | None = ...) -> None: ...
    def toggle_backface(self) -> None: ...
    def backface_culling_on(self) -> None: ...
    def backface_culling_off(self) -> None: ...
    def toggle_texture(self) -> None: ...
    def texture_on(self) -> None: ...
    def texture_off(self) -> None: ...
    def toggle_wireframe(self) -> None: ...
    def wireframe_on(self) -> None: ...
    def wireframe_off(self) -> None: ...
    def disable_mouse(self) -> None: ...
    def enable_mouse(self) -> None: ...
    def silence_input(self) -> None: ...
    def revive_input(self) -> None: ...
    def set_mouse_on_node(self, newNode: Transform2SG) -> None: ...
    def change_mouse_interface(self, changeTo: NodePath[MouseInterfaceNode]) -> None: ...
    def use_drive(self) -> None: ...
    def use_trackball(self) -> None: ...
    def toggle_tex_mem(self) -> None: ...
    def toggle_show_vertices(self) -> None: ...
    def oobe(self, cam: NodePath[Camera] | None = ...) -> None: ...
    def oobe_cull(self, cam: NodePath[Camera] | None = ...) -> None: ...
    def show_camera_frustum(self) -> None: ...
    def remove_camera_frustum(self) -> None: ...
    def screenshot(
        self, namePrefix: str = ..., defaultFilename: bool = ..., source: GraphicsEngine | None = ..., imageComment: str = ...
    ) -> str | None: ...
    def save_cube_map(
        self,
        namePrefix: str = ...,
        defaultFilename: bool = ...,
        source: GraphicsEngine | None = ...,
        camera: NodePath[ModelNode] | None = ...,
        size: int = ...,
        cameraMask: BitMask32 = ...,
        sourceLens: Lens | None = ...,
    ) -> str | None: ...
    def save_sphere_map(
        self,
        namePrefix: str = ...,
        defaultFilename: bool = ...,
        source: GraphicsEngine | None = ...,
        camera: NodePath[ModelNode] | None = ...,
        size: int = ...,
        cameraMask: BitMask32 = ...,
        numVertices: int = ...,
        sourceLens: Lens | None = ...,
    ) -> str | None: ...
    def movie(
        self,
        namePrefix: str = ...,
        duration: float = ...,
        fps: int = ...,
        format: str = ...,
        sd: int = ...,
        source: GraphicsWindow | DisplayRegion | Texture | None = ...,
    ) -> Task: ...
    def windowEvent(self, win: GraphicsEngine) -> None: ...
    def adjustWindowAspectRatio(self, aspectRatio: float) -> None: ...
    def userExit(self) -> None: ...
    def finalizeExit(self) -> None: ...
    def start_wx(self, fWantWx: bool = ...) -> None: ...
    def spawnWxLoop(self) -> None: ...
    def wxRun(self) -> None: ...
    def start_tk(self, fWantTk: bool = ...) -> None: ...
    def spawnTkLoop(self) -> None: ...
    def tkRun(self) -> None: ...
    def start_direct(self, fWantDirect: bool = ..., fWantTk: bool = ..., fWantWx: bool = ...) -> None: ...
    def getRepository(self) -> None: ...
    def getAxes(self) -> NodePath: ...
    def run(self) -> None: ...
    makeDefaultPipe = make_default_pipe
    makeModulePipe = make_module_pipe
    makeAllPipes = make_all_pipes
    openWindow = open_window
    closeWindow = close_window
    openDefaultWindow = open_default_window
    openMainWindow = open_main_window
    setSleep = set_sleep
    setFrameRateMeter = set_frame_rate_meter
    setSceneGraphAnalyzerMeter = set_scene_graph_analyzer_meter
    setupWindowControls = setup_window_controls
    setupRender = setup_render
    setupRender2d = setup_render2d
    setupRender2dp = setup_render2dp
    setAspectRatio = set_aspect_ratio
    getAspectRatio = get_aspect_ratio
    getSize = get_size
    makeCamera = make_camera
    makeCamera2d = make_camera2d
    makeCamera2dp = make_camera2dp
    setupDataGraph = setup_data_graph
    setupMouse = setup_mouse
    setupMouseCB = setup_mouse_cb
    enableSoftwareMousePointer = enable_software_mouse_pointer
    attachInputDevice = attach_input_device
    detachInputDevice = detach_input_device
    addAngularIntegrator = add_angular_integrator
    enableParticles = enable_particles
    disableParticles = disable_particles
    toggleParticles = toggle_particles
    createStats = create_stats
    addSfxManager = add_sfx_manager
    enableMusic = enable_music
    enableSoundEffects = enable_sound_effects
    disableAllAudio = disable_all_audio
    enableAllAudio = enable_all_audio
    initShadowTrav = init_shadow_trav
    getBackgroundColor = get_background_color
    setBackgroundColor = set_background_color
    toggleBackface = toggle_backface
    backfaceCullingOn = backface_culling_on
    backfaceCullingOff = backface_culling_off
    toggleTexture = toggle_texture
    textureOn = texture_on
    textureOff = texture_off
    toggleWireframe = toggle_wireframe
    wireframeOn = wireframe_on
    wireframeOff = wireframe_off
    disableMouse = disable_mouse
    enableMouse = enable_mouse
    silenceInput = silence_input
    reviveInput = revive_input
    setMouseOnNode = set_mouse_on_node
    changeMouseInterface = change_mouse_interface
    useDrive = use_drive
    useTrackball = use_trackball
    toggleTexMem = toggle_tex_mem
    toggleShowVertices = toggle_show_vertices
    oobeCull = oobe_cull
    showCameraFrustum = show_camera_frustum
    removeCameraFrustum = remove_camera_frustum
    saveCubeMap = save_cube_map
    saveSphereMap = save_sphere_map
    startWx = start_wx
    startTk = start_tk
    startDirect = start_direct

class WindowControls:
    win: GraphicsEngine
    camera: NodePath | None
    camNode: Camera | None
    camera2d: NodePath | None
    mouseWatcher: MouseWatcher | None
    mouseKeyboard: NodePath | None
    closeCommand: SimpleCallback
    grid: Any
    def __init__(
        self,
        win: GraphicsEngine,
        cam: NodePath | None = ...,
        camNode: Camera | None = ...,
        cam2d: NodePath | None = ...,
        mouseWatcher: MouseWatcher | None = ...,
        mouseKeyboard: NodePath | None = ...,
        closeCmd: SimpleCallback = ...,
        grid: Any = ...,
    ) -> None: ...
