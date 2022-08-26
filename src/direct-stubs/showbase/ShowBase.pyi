__all__ = ['ShowBase', 'WindowControls']

from collections.abc import Callable
from types import ModuleType
from typing import ClassVar, overload
from typing_extensions import Literal, TypeAlias

from panda3d.core import (
    AudioManager,
    AudioSound,
    BitMask_uint32_t_32,
    ButtonThrower,
    Camera,
    ClockObject,
    CollisionTraverser,
    ConfigVariableColor,
    DataGraphTraverser,
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
    Lens,
    LMatrix4f,
    LVecBase2i,
    LVecBase3f,
    LVecBase4f,
    ModelNode,
    MouseInterfaceNode,
    MouseWatcher,
    NodePath,
    PandaNode,
    PGTop,
    RecorderController,
    SceneGraphAnalyzerMeter,
    Trackball,
    Transform2SG,
    UnalignedLVecBase4f,
    WindowProperties,
)
from panda3d.physics import ParticleSystemManager, PhysicsManager
from ..directnotify.Notifier import Notifier
from ..directtools.DirectSession import DirectSession
from ..showutil.TexMemWatcher import TexMemWatcher
from ..task.Task import Task, TaskManager
from .BufferViewer import BufferViewer
from .BulletinBoard import BulletinBoard
from .DirectObject import DirectObject
from .EventManager import EventManager
from .JobManager import JobManager
from .Loader import Loader
from .Messenger import Messenger
from .PythonUtil import Stack
from .Transitions import Transitions

_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_WindowType: TypeAlias = Literal['onscreen', 'offscreen', 'none']

def exitfunc() -> None: ...

class ShowBase(DirectObject):
    config: ClassVar[ModuleType]
    notify: ClassVar[Notifier]
    __dev__: bool
    mainDir: str
    main_dir: str
    appRunner = ...
    app_runner = ...
    debugRunningMultiplier: int
    nextWindowIndex: int
    sfxActive: bool
    musicActive: bool
    wantFog: bool
    wantRender2dp: bool
    screenshotExtension: str
    musicManager: AudioManager | None
    musicManagerIsValid: bool | None
    sfxManagerList: list[AudioManager]
    sfxManagerIsValidList: list[bool]
    wantStats: bool
    wantTk: bool
    wantWx: bool
    wantDirect: bool
    exitFunc: Callable[[], object] | None
    finalExitCallbacks: list[Callable[[], object]]
    windowType: _WindowType
    requireWindow: bool
    win: GraphicsEngine | None
    frameRateMeter: FrameRateMeter | None
    sceneGraphAnalyzerMeter: SceneGraphAnalyzerMeter | None
    winList: list[GraphicsEngine]
    winControls: list[WindowControls]
    mainWinMinimized: bool
    mainWinForeground: bool
    pipe: GraphicsPipe | None
    pipeList: list[GraphicsPipe]
    mouse2cam: NodePath[Transform2SG] | None
    buttonThrowers: list[ButtonThrower] | None
    mouseWatcher: NodePath[MouseWatcher] | None
    mouseWatcherNode: MouseWatcher | None
    pointerWatcherNodes: list[MouseWatcher] | None
    mouseInterface: NodePath[MouseInterfaceNode]
    mouseInterfaceNode: MouseInterfaceNode
    drive: NodePath[DriveInterface] | None
    trackball: NodePath[Trackball] | None
    texmem: TexMemWatcher | None
    showVertices: NodePath[Camera] | None
    deviceButtonThrowers: list[NodePath[ButtonThrower]]
    cam: NodePath[Camera] | None
    cam2d: NodePath[Camera] | None
    cam2dp: NodePath[Camera] | None
    camera: NodePath[ModelNode] | None
    camera2d: NodePath | None
    camera2dp: NodePath | None
    camList: list[NodePath[Camera]]
    camNode: Camera | None
    camLens: Lens | None
    camFrustumVis: NodePath[GeomNode] | None
    direct: DirectSession | None
    wxApp = ...
    wxAppCreated: bool
    tkRoot = ...
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
    def __init__(
        self,
        fStartDirect: bool = True,
        windowType: _WindowType | None = None,
    ) -> None: ...
    def pushCTrav(self, cTrav: CollisionTraverser) -> None: ...
    def popCTrav(self) -> None: ...
    def getExitErrorCode(self) -> Literal[0]: ...
    def printEnvDebugInfo(self) -> None: ...
    def destroy(self) -> None: ...
    def make_default_pipe(self, printPipeTypes: bool | None) -> None: ...
    def make_module_pipe(self, moduleName: str) -> GraphicsPipe: ...
    def make_all_pipes(self) -> None: ...
    def open_window(
        self,
        props: WindowProperties | None = None,
        fbprops: FrameBufferProperties | None = None,
        pipe: GraphicsPipe | None = None,
        gsg: GraphicsOutput | None = None,
        host: GraphicsOutput | None = None,
        type: _WindowType | None = None,
        name: str | None = None,
        size: LVecBase2i | tuple[int, int] | None = None,
        aspectRatio: float | None = None,
        makeCamera: bool = True,
        keepCamera: bool = False,
        scene: NodePath | None = None,
        stereo: bool | None = None,
        unexposedDraw: bool | None = None,
        callbackWindowDict: dict[str, Callable[[], object]] | None = None,
        requireWindow: bool | None = None,
    ) -> GraphicsWindow: ...
    def close_window(self, win, keepCamera: bool = False, removeWindow: bool = True) -> None: ...
    def open_default_window(self, *args, **kw) -> bool: ...
    def open_main_window(self, *args, **kw) -> bool: ...
    def set_sleep(self, amount: float) -> None: ...
    def set_frame_rate_meter(self, flag: bool) -> None: ...
    def set_scene_graph_analyzer_meter(self, flag: bool) -> None: ...
    def setup_window_controls(self, winCtr: WindowControls | None = None) -> None: ...
    def setup_render(self) -> None: ...
    def setup_render2d(self) -> None: ...
    def setup_render2dp(self) -> None: ...
    def set_aspect_ratio(self, aspectRatio: float) -> None: ...
    def get_aspect_ratio(self, win: GraphicsEngine | None = None) -> float: ...
    def get_size(self, win: GraphicsEngine | None = None) -> tuple[float, float]: ...
    def make_camera(
        self,
        win: GraphicsOutput,
        sort: int = 0,
        scene: NodePath | None = None,
        displayRegion: _Vec4f | tuple[float, float, float, float] = ...,
        stereo: bool | None = None,
        aspectRatio: float | None = None,
        clearDepth: bool = False,
        clearColor: _Vec4f | None = None,
        lens: Lens | None = None,
        camName: str = 'cam',
        mask=None,
        useCamera: NodePath[Camera] | None = None,
    ) -> NodePath[Camera]: ...
    def make_camera2d(
        self,
        win: GraphicsOutput,
        sort: int = 10,
        displayRegion: _Vec4f | tuple[float, float, float, float] = ...,
        coords: _Vec4f | tuple[float, float, float, float] = ...,
        lens: Lens | None = None,
        cameraName: str | None = None,
    ) -> NodePath[Camera]: ...
    def make_camera2dp(
        self,
        win: GraphicsOutput,
        sort: int = 10,
        displayRegion: _Vec4f | tuple[float, float, float, float] = ...,
        coords: _Vec4f | tuple[float, float, float, float] = ...,
        lens: Lens | None = None,
        cameraName: str | None = None,
    ) -> NodePath[Camera]: ...
    def setup_data_graph(self) -> None: ...
    def setup_mouse(self, win, fMultiWin: bool = False) -> NodePath[ButtonThrower]: ...
    def setup_mouse_cb(self, win) -> tuple[list[NodePath[ButtonThrower]], list[MouseWatcher]]: ...
    def enable_software_mouse_pointer(self) -> None: ...
    def getAlt(self) -> bool: ...
    def getShift(self) -> bool: ...
    def getControl(self) -> bool: ...
    def getMeta(self) -> bool: ...
    def attach_input_device(self, device: InputDevice, prefix: str | None = None, watch: bool = False) -> None: ...
    def detach_input_device(self, device: InputDevice) -> None: ...
    def add_angular_integrator(self) -> None: ...
    def enable_particles(self) -> None: ...
    def disable_particles(self) -> None: ...
    def toggle_particles(self) -> None: ...
    def isParticleMgrEnabled(self) -> bool: ...
    def isPhysicsMgrEnabled(self) -> bool: ...
    def updateManagers(self, state: object) -> Literal[1]: ...
    def create_stats(self, hostname: str | None = None, port: int | None = None) -> bool: ...
    def add_sfx_manager(self, extraSfxManager: AudioManager) -> None: ...
    def createBaseAudioManagers(self) -> None: ...
    def enable_music(self, bEnableMusic: bool) -> None: ...
    def SetAllSfxEnables(self, bEnabled: bool) -> None: ...
    def enable_sound_effects(self, bEnableSoundEffects: bool) -> None: ...
    def disable_all_audio(self) -> None: ...
    def enable_all_audio(self) -> None: ...
    def loadSfx(self, name): ...
    def loadMusic(self, name): ...
    def playSfx(
        self,
        sfx: AudioSound,
        looping: bool = False,
        interrupt: bool = True,
        volume: float | None = None,
        time: float = 0,
        node: NodePath | None = None,
        listener: NodePath | None = None,
        cutoff: float | None = None,
    ) -> None: ...
    def playMusic(
        self,
        music: AudioSound,
        looping: bool = False,
        interrupt: bool = True,
        volume: float | None = None,
        time: float = 0,
    ) -> None: ...
    def init_shadow_trav(self) -> None: ...
    def restart(self, clusterSync: bool = False, cluster=None) -> None: ...
    def shutdown(self) -> None: ...
    def get_background_color(self, win: GraphicsEngine | None = None) -> LVecBase4f: ...
    @overload
    def set_background_color(self, r: LVecBase3f | LVecBase4f, *, a: float = 0, win: GraphicsEngine | None = None) -> None: ...
    @overload
    def set_background_color(self, r: float, g: float, b: float, a: float = 0, win: GraphicsEngine | None = None) -> None: ...
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
    def oobe(self, cam: NodePath[Camera] | None = None) -> None: ...
    def oobe_cull(self, cam: NodePath[Camera] | None = None) -> None: ...
    def show_camera_frustum(self) -> None: ...
    def remove_camera_frustum(self) -> None: ...
    def screenshot(
        self,
        namePrefix: str = 'screenshot',
        defaultFilename: bool = True,
        source=None,
        imageComment: str = '',
    ) -> str | None: ...
    def save_cube_map(
        self,
        namePrefix: str = 'cube_map_#.png',
        defaultFilename: bool = False,
        source=None,
        camera: NodePath[ModelNode] | None = None,
        size: int = 128,
        cameraMask: BitMask_uint32_t_32 = ...,
        sourceLens: Lens | None = None,
    ) -> str | None: ...
    def save_sphere_map(
        self,
        namePrefix: str = 'spheremap.png',
        defaultFilename: bool = False,
        source=None,
        camera: NodePath[ModelNode] | None = None,
        size: int = 256,
        numVertices: int = 1000,
        sourceLens: Lens | None = None,
    ) -> str | None: ...
    def movie(
        self,
        namePrefix: str = 'movie',
        duration: float = 1,
        fps: int = 30,
        format: str = 'png',
        sd: int = 4,
        source=None,
    ) -> Task: ...
    def windowEvent(self, win: GraphicsEngine) -> None: ...
    def adjustWindowAspectRatio(self, aspectRatio: float) -> None: ...
    def userExit(self) -> None: ...
    def finalizeExit(self) -> None: ...
    def start_wx(self, fWantWx: bool = True) -> None: ...
    def spawnWxLoop(self) -> None: ...
    def wxRun(self) -> None: ...
    def start_tk(self, fWantTk: bool = True) -> None: ...
    def spawnTkLoop(self) -> None: ...
    def tkRun(self) -> None: ...
    def start_direct(self, fWantDirect: bool = True, fWantTk: bool = True, fWantWx: bool = False) -> None: ...
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
    closeCommand: Callable[[], object]
    grid = ...
    def __init__(
        self,
        win: GraphicsEngine,
        cam: NodePath | None = None,
        camNode: Camera | None = None,
        cam2d: NodePath | None =None,
        mouseWatcher: MouseWatcher | None = None,
        mouseKeyboard: NodePath | None = None,
        closeCmd: Callable[[], object] = ...,
        grid=None,
    ) -> None: ...
    def __str__(self) -> str: ...
