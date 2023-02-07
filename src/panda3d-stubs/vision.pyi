from _typeshed import StrOrBytesPath
from collections.abc import Sequence
from typing import Any, ClassVar
from typing_extensions import Self

from panda3d.core._dtoolutil import ostream
from panda3d.core._gobj import Texture
from panda3d.core._movies import MovieVideo
from panda3d.core._pgraph import Camera, NodePath

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
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def make(camera: NodePath[Camera], paramfile: StrOrBytesPath, markersize: float) -> ARToolKit:
        """Create a new ARToolKit instance.

        Camera must be the nodepath of a panda camera object.  The panda camera's
        field of view is initialized to match the field of view of the physical
        webcam.  Each time you call analyze, all marker nodepaths will be moved
        into a position which is relative to this camera.  The marker_size
        parameter indicates how large you printed the physical markers.  You should
        use the same size units that you wish to use in the panda code.
        """
    def set_threshold(self, n: float) -> None:
        """As part of its analysis, the ARToolKit occasionally converts images to
        black and white by thresholding them.  The threshold is set to 0.5 by
        default, but you can tweak it here.
        """
    def attach_pattern(self, pattern: StrOrBytesPath, path: NodePath) -> None:
        """Associates the specified glyph with the specified NodePath.  Each time you
        call analyze, ARToolKit will update the NodePath's transform.  If the node
        is not visible, its scale will be set to zero.
        """
    def detach_patterns(self) -> None:
        """Dissociates all patterns from all NodePaths."""
    def analyze(self, tex: Texture, do_flip_texture: bool = ...) -> None:
        """Analyzes the non-pad region of the specified texture.  This causes all
        attached nodepaths to move.  The parameter do_flip_texture is true by
        default, because Panda's representation of textures is upside down from
        ARToolKit.  If you already have a texture that's upside-down, however, you
        should set it to false.
        """
    setThreshold = set_threshold
    attachPattern = attach_pattern
    detachPatterns = detach_patterns

class WebcamVideo(MovieVideo):
    """Allows you to open a webcam or other video capture device as a video
    stream.
    """

    @property
    def options(self) -> Sequence[WebcamVideo]: ...
    @staticmethod
    def get_num_options() -> int:
        """Returns the number of webcam options.  An "option" consists of a device
        plus a set of configuration parameters.  For example, "Creative Webcam Live
        at 640x480, 30 fps" is an option.
        """
    @staticmethod
    def get_option(n: int) -> WebcamVideo:
        """Returns the nth webcam option."""
    def get_size_x(self) -> int:
        """Returns the camera's size_x."""
    def get_size_y(self) -> int:
        """Returns the camera's size_y."""
    def get_fps(self) -> float:
        """Returns the camera's framerate.  This is a maximum theoretical: the actual
        performance will depend on the speed of the hardware.
        """
    def get_pixel_format(self) -> str:
        """Returns the camera's pixel format, as a FourCC code, if known."""
    def output(self, out: ostream) -> None:
        """Outputs the WebcamVideo.  This function simply writes the name, size and
        FPS to the output stream.
        """
    def get_options(self) -> tuple[WebcamVideo, ...]: ...
    getNumOptions = get_num_options
    getOption = get_option
    getSizeX = get_size_x
    getSizeY = get_size_y
    getFps = get_fps
    getPixelFormat = get_pixel_format
    getOptions = get_options
