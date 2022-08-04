from collections.abc import Sequence
from os import PathLike
from typing import Any, ClassVar, TypeAlias, overload
from panda3d.core import (
    ConfigVariableFilename,
    Datagram,
    DatagramIterator,
    Filename,
    Namable,
    SubfileInfo,
    Texture,
    TypeHandle,
    TypedReferenceCount,
    TypedWritableReferenceCount,
    istream,
)

_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike

class MovieAudio(TypedWritableReferenceCount, Namable):
    """A MovieAudio is actually any source that provides a sequence of audio
    samples.  That could include an AVI file, a microphone, or an internet TV
    station.
    
    The difference between a MovieAudio and a MovieAudioCursor is like the
    difference between a filename and a file handle.  The MovieAudio just
    indicates a particular movie.  The MovieAudioCursor is what allows access.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def filename(self) -> Filename: ...
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, __param0: MovieAudio) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def open(self) -> MovieAudioCursor: ...
    @staticmethod
    def get(name: _Filename) -> MovieAudio: ...
    def get_filename(self) -> Filename: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToNamable = upcast_to_Namable
    getFilename = get_filename
    getClassType = get_class_type

class FlacAudio(MovieAudio):
    """Reads FLAC audio files.  Ogg-encapsulated FLAC files are not supported.
    
    @since 1.10.0
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, name: _Filename) -> None: ...
    @overload
    def __init__(self, __param0: FlacAudio) -> None: ...
    @staticmethod
    def make(name: _Filename) -> MovieAudio: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class MovieAudioCursor(TypedWritableReferenceCount):
    """A MovieAudio is actually any source that provides a sequence of audio
    samples.  That could include an AVI file, a microphone, or an internet TV
    station.  A MovieAudioCursor is a handle that lets you read data
    sequentially from a MovieAudio.
    
    Thread safety: each individual MovieAudioCursor must be owned and accessed
    by a single thread.  It is OK for two different threads to open the same
    file at the same time, as long as they use separate MovieAudioCursor
    objects.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, src: MovieAudio) -> None: ...
    @overload
    def __init__(self, __param0: MovieAudioCursor) -> None: ...
    def get_source(self) -> MovieAudio: ...
    def audio_rate(self) -> int: ...
    def audio_channels(self) -> int: ...
    def length(self) -> float: ...
    def can_seek(self) -> bool: ...
    def can_seek_fast(self) -> bool: ...
    def tell(self) -> float: ...
    def skip_samples(self, n: int) -> None: ...
    def aborted(self) -> bool: ...
    def ready(self) -> int: ...
    def seek(self, offset: float) -> None: ...
    @overload
    def read_samples(self, n: int) -> str: ...
    @overload
    def read_samples(self, n: int, dg: Datagram) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getSource = get_source
    audioRate = audio_rate
    audioChannels = audio_channels
    canSeek = can_seek
    canSeekFast = can_seek_fast
    skipSamples = skip_samples
    readSamples = read_samples
    getClassType = get_class_type

class FlacAudioCursor(MovieAudioCursor):
    """Implements decoding of FLAC audio files.
    
    @see FlacAudio
    @since 1.10.0
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: FlacAudioCursor) -> None: ...
    @overload
    def __init__(self, src: FlacAudio, stream: istream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class MovieVideo(TypedWritableReferenceCount, Namable):
    """A MovieVideo is actually any source that provides a sequence of video
    frames.  That could include an AVI file, a digital camera, or an internet
    TV station.
    
    The difference between a MovieVideo and a MovieVideoCursor is like the
    difference between a filename and a file handle.  The MovieVideo just
    indicates a particular movie.  The MovieVideoCursor is what allows access.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def filename(self) -> Filename: ...
    @property
    def subfile_info(self) -> SubfileInfo: ...
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, __param0: MovieVideo) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def open(self) -> MovieVideoCursor: ...
    @staticmethod
    def get(name: _Filename) -> MovieVideo: ...
    def get_filename(self) -> Filename: ...
    def get_subfile_info(self) -> SubfileInfo: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToNamable = upcast_to_Namable
    getFilename = get_filename
    getSubfileInfo = get_subfile_info
    getClassType = get_class_type

class InkblotVideo(MovieVideo):
    """A cellular automaton that generates an amusing pattern of swirling colors."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: InkblotVideo) -> None: ...
    @overload
    def __init__(self, x: int, y: int, fps: int) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class MovieVideoCursor(TypedWritableReferenceCount):
    """A MovieVideo is actually any source that provides a sequence of video
    frames.  That could include an AVI file, a digital camera, or an internet
    TV station.  A MovieVideoCursor is a handle that lets you read data
    sequentially from a MovieVideo.
    
    Thread safety: each individual MovieVideoCursor must be owned and accessed
    by a single thread.  It is OK for two different threads to open the same
    file at the same time, as long as they use separate MovieVideoCursor
    objects.
    """
    class Buffer(TypedReferenceCount):
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: MovieVideoCursor.Buffer) -> None: ...
        def compare_timestamp(self, other: MovieVideoCursor.Buffer) -> int: ...
        def get_timestamp(self) -> float: ...
        @staticmethod
        def get_class_type() -> TypeHandle: ...
        compareTimestamp = compare_timestamp
        getTimestamp = get_timestamp
        getClassType = get_class_type
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: MovieVideoCursor) -> None: ...
    def get_source(self) -> MovieVideo: ...
    def size_x(self) -> int: ...
    def size_y(self) -> int: ...
    def get_num_components(self) -> int: ...
    def length(self) -> float: ...
    def can_seek(self) -> bool: ...
    def can_seek_fast(self) -> bool: ...
    def aborted(self) -> bool: ...
    def ready(self) -> bool: ...
    def streaming(self) -> bool: ...
    def setup_texture(self, tex: Texture) -> None: ...
    def set_time(self, timestamp: float, loop_count: int) -> bool: ...
    def fetch_buffer(self) -> MovieVideoCursor.Buffer: ...
    def apply_to_texture(self, buffer: MovieVideoCursor.Buffer, t: Texture, page: int) -> None: ...
    def apply_to_texture_rgb(self, buffer: MovieVideoCursor.Buffer, t: Texture, page: int) -> None: ...
    def apply_to_texture_alpha(self, buffer: MovieVideoCursor.Buffer, t: Texture, page: int, alpha_src: int) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getSource = get_source
    sizeX = size_x
    sizeY = size_y
    getNumComponents = get_num_components
    canSeek = can_seek
    canSeekFast = can_seek_fast
    setupTexture = setup_texture
    setTime = set_time
    fetchBuffer = fetch_buffer
    applyToTexture = apply_to_texture
    applyToTextureRgb = apply_to_texture_rgb
    applyToTextureAlpha = apply_to_texture_alpha
    getClassType = get_class_type

class InkblotVideoCursor(MovieVideoCursor):
    """A cellular automaton that generates an amusing pattern of swirling colors."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, src: InkblotVideo) -> None: ...
    @overload
    def __init__(self, __param0: InkblotVideoCursor) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class MicrophoneAudio(MovieAudio):
    """Class MicrophoneAudio provides the means to read raw audio samples from a
    microphone.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def options(self) -> Sequence[MicrophoneAudio]: ...
    @property
    def channels(self) -> int: ...
    @property
    def rate(self) -> int: ...
    @staticmethod
    def get_num_options() -> int: ...
    @staticmethod
    def get_option(n: int) -> MicrophoneAudio: ...
    def get_channels(self) -> int: ...
    def get_rate(self) -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_options(self) -> tuple[MicrophoneAudio, ...]: ...
    getNumOptions = get_num_options
    getOption = get_option
    getChannels = get_channels
    getRate = get_rate
    getClassType = get_class_type
    getOptions = get_options

class OpusAudio(MovieAudio):
    """Interfaces with the libopusfile library to implement decoding of Opus
    audio files.
    
    @since 1.10.0
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, name: _Filename) -> None: ...
    @overload
    def __init__(self, __param0: OpusAudio) -> None: ...
    @staticmethod
    def make(name: _Filename) -> MovieAudio: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class OpusAudioCursor(MovieAudioCursor):
    """Interfaces with the libopusfile library to implement decoding of Opus
    audio files.
    
    @see OpusAudio
    @since 1.10.0
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: OpusAudioCursor) -> None: ...
    @overload
    def __init__(self, src: OpusAudio, stream: istream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class UserDataAudio(MovieAudio):
    """A UserDataAudio is a way for the user to manually supply raw audio samples.
    remove_after_read means the data will be removed if read once.  Else data
    will be stored (enable looping and seeking). Expects data as 16 bit signed
    (word); Example for stereo: 1.word = 1.channel,2.word = 2.channel, 3.word =
    1.channel,4.word = 2.channel, etc.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: UserDataAudio) -> None: ...
    @overload
    def __init__(self, rate: int, channels: int, remove_after_read: bool = ...) -> None: ...
    @overload
    def append(self, str: str) -> None: ...
    @overload
    def append(self, src: DatagramIterator, len: int = ...) -> None: ...
    def done(self) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class UserDataAudioCursor(MovieAudioCursor):
    """A UserDataAudioCursor is a means to manually supply a sequence of raw audio
    samples.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, src: UserDataAudio) -> None: ...
    @overload
    def __init__(self, __param0: UserDataAudioCursor) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class VorbisAudio(MovieAudio):
    """Interfaces with the libvorbisfile library to implement decoding of Ogg
    Vorbis audio files.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, name: _Filename) -> None: ...
    @overload
    def __init__(self, __param0: VorbisAudio) -> None: ...
    @staticmethod
    def make(name: _Filename) -> MovieAudio: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class VorbisAudioCursor(MovieAudioCursor):
    """Interfaces with the libvorbisfile library to implement decoding of Ogg
    Vorbis audio files.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: VorbisAudioCursor) -> None: ...
    @overload
    def __init__(self, src: VorbisAudio, stream: istream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class WavAudio(MovieAudio):
    """A native PCM .wav loader.  Supported formats are linear PCM, IEEE float,
    A-law and mu-law.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, name: _Filename) -> None: ...
    @overload
    def __init__(self, __param0: WavAudio) -> None: ...
    @staticmethod
    def make(name: _Filename) -> MovieAudio: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class WavAudioCursor(MovieAudioCursor):
    """Used for reading PCM .wav files.  Supported formats are linear PCM, IEEE
    float, A-law and mu-law.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: WavAudioCursor) -> None: ...
    @overload
    def __init__(self, src: WavAudio, stream: istream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type
