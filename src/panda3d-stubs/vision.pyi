from collections.abc import Sequence
from os import PathLike
from typing import Any, ClassVar, TypeAlias
from panda3d.core import ConfigVariableFilename, Filename, MovieVideo, NodePath, Texture, TypeHandle, ostream

_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike

class ARToolKit:
    """ARToolKit is a software library for building Augmented Reality (AR)
    applications.  These are applications that involve the overlay of virtual
    imagery on the real world.  It was developed by Dr.  Hirokazu Kato.  Its
    ongoing development is being supported by the Human Interface Technology
    Laboratory (HIT Lab) at the University of Washington, HIT Lab NZ at the
    University of Canterbury, New Zealand, and ARToolworks, Inc, Seattle.  It
    is available under a GPL license.  It is also possible to negotiate other
    licenses with the copyright holders.
    
    This class is a wrapper around the ARToolKit library.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: ARToolKit) -> None: ...
    @staticmethod
    def make(camera: NodePath, paramfile: _Filename, markersize: float) -> ARToolKit: ...
    def set_threshold(self, n: float) -> None: ...
    def attach_pattern(self, pattern: _Filename, path: NodePath) -> None: ...
    def detach_patterns(self) -> None: ...
    def analyze(self, tex: Texture, do_flip_texture: bool = ...) -> None: ...
    setThreshold = set_threshold
    attachPattern = attach_pattern
    detachPatterns = detach_patterns

class WebcamVideo(MovieVideo):
    """Allows you to open a webcam or other video capture device as a video
    stream.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def options(self) -> Sequence[WebcamVideo]: ...
    @staticmethod
    def get_num_options() -> int: ...
    @staticmethod
    def get_option(n: int) -> WebcamVideo: ...
    def get_size_x(self) -> int: ...
    def get_size_y(self) -> int: ...
    def get_fps(self) -> float: ...
    def get_pixel_format(self) -> str: ...
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_options(self) -> tuple[WebcamVideo, ...]: ...
    getNumOptions = get_num_options
    getOption = get_option
    getSizeX = get_size_x
    getSizeY = get_size_y
    getFps = get_fps
    getPixelFormat = get_pixel_format
    getClassType = get_class_type
    getOptions = get_options
