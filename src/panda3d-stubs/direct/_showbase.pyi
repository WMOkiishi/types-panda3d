from panda3d.core._display import GraphicsWindow
from panda3d.core._prc import ConfigVariableSearchPath

def get_particle_path() -> ConfigVariableSearchPath: ...
def throw_new_frame() -> None: ...
def init_app_for_gui() -> None: ...
def add_fullscreen_testsize(xsize: int, ysize: int) -> None:
    """klunky interface since we cant pass array from python->C++"""

def runtest_fullscreen_sizes(win: GraphicsWindow) -> None: ...
def query_fullscreen_testresult(xsize: int, ysize: int) -> bool: ...
def store_accessibility_shortcut_keys() -> None:
    """to handle windows stickykeys"""

def allow_accessibility_shortcut_keys(allowKeys: bool) -> None: ...

getParticlePath = get_particle_path
throwNewFrame = throw_new_frame
initAppForGui = init_app_for_gui
addFullscreenTestsize = add_fullscreen_testsize
runtestFullscreenSizes = runtest_fullscreen_sizes
queryFullscreenTestresult = query_fullscreen_testresult
storeAccessibilityShortcutKeys = store_accessibility_shortcut_keys
allowAccessibilityShortcutKeys = allow_accessibility_shortcut_keys
