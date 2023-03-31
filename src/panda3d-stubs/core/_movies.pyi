from _typeshed import StrOrBytesPath
from collections.abc import Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Self

from panda3d.core._dtoolbase import TypeHandle
from panda3d.core._dtoolutil import Filename, istream
from panda3d.core._express import Datagram, DatagramIterator, Namable, SubfileInfo, TypedReferenceCount
from panda3d.core._gobj import Texture
from panda3d.core._prc import ConfigVariableFilename
from panda3d.core._putil import TypedWritableReferenceCount

class MovieAudio(TypedWritableReferenceCount, Namable):
    """A MovieAudio is actually any source that provides a sequence of audio
    samples.  That could include an AVI file, a microphone, or an internet TV
    station.

    The difference between a MovieAudio and a MovieAudioCursor is like the
    difference between a filename and a file handle.  The MovieAudio just
    indicates a particular movie.  The MovieAudioCursor is what allows access.
    """

    @property
    def filename(self) -> Filename: ...
    @overload
    def __init__(self, name: str = ...) -> None:
        """This constructor returns a null audio stream --- a stream of total silence,
        at 8000 samples per second.  To get more interesting audio, you need to
        construct a subclass of this class.
        """
    @overload
    def __init__(self, __param0: MovieAudio) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def open(self) -> MovieAudioCursor:
        """Open this audio, returning a MovieAudioCursor"""
    @staticmethod
    def get(name: StrOrBytesPath) -> MovieAudio:
        """Obtains a MovieAudio that references a file.  Just calls
        MovieTypeRegistry::make_audio().
        """
    def get_filename(self) -> Filename:
        """Returns the movie's filename.  A movie is not guaranteed to have a
        filename, if not, then this function returns a null filename.
        """
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToNamable = upcast_to_Namable
    getFilename = get_filename

class FlacAudio(MovieAudio):
    """Reads FLAC audio files.  Ogg-encapsulated FLAC files are not supported.

    @since 1.10.0
    """

    @overload
    def __init__(self, name: StrOrBytesPath) -> None:
        """xxx"""
    @overload
    def __init__(self, __param0: ConfigVariableFilename | FlacAudio) -> None: ...
    @staticmethod
    def make(name: StrOrBytesPath) -> MovieAudio:
        """Obtains a MovieAudio that references a file."""

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

    @overload
    def __init__(self, src: MovieAudio) -> None:
        """This constructor returns a null audio stream --- a stream of total silence,
        at 8000 samples per second.  To get more interesting audio, you need to
        construct a subclass of this class.
        """
    @overload
    def __init__(self, __param0: MovieAudioCursor) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_source(self) -> MovieAudio:
        """Returns the MovieAudio which this cursor references."""
    def audio_rate(self) -> int:
        """Returns the audio sample rate."""
    def audio_channels(self) -> int:
        """Returns the number of audio channels (ie, two for stereo, one for mono)."""
    def length(self) -> float:
        """Returns the length of the movie.  Attempting to read audio samples beyond
        the specified length will produce silent samples.

        Some kinds of Movie, such as internet TV station, might not have a
        predictable length.  In that case, the length will be set to a very large
        number: 1.0E10.

        Some AVI files have incorrect length values encoded into them - they may be
        a second or two long or short.  When playing such an AVI using the Movie
        class, you may see a slightly truncated video, or a slightly elongated
        video (padded with black frames).  There are utilities out there to fix the
        length values in AVI files.

        An audio consumer needs to check the length, the ready status, and the
        aborted flag.
        """
    def can_seek(self) -> bool:
        """Returns true if the movie can seek.  If this is true, seeking is still not
        guaranteed to be fast: for some movies, seeking is implemented by rewinding
        to the beginning and then fast-forwarding to the desired location.  Even if
        the movie cannot seek, the seek method can still advance to an arbitrary
        location by reading samples and discarding them.  However, to move
        backward, can_seek must return true.
        """
    def can_seek_fast(self) -> bool:
        """Returns true if seek operations are constant time."""
    def tell(self) -> float:
        """Returns the current offset within the file."""
    def skip_samples(self, n: int) -> None:
        """Skip audio samples from the stream.  This is mostly for debugging purposes."""
    def aborted(self) -> bool:
        """If aborted is true, it means that the "ready" samples are not being
        replenished.  See the method "ready" for an explanation.
        """
    def ready(self) -> int:
        """Returns the number of audio samples that are ready to read.  This is
        primarily relevant for sources like microphones which produce samples at a
        fixed rate.  If you try to read more samples than are ready, the result
        will be silent samples.

        Some audio streams do not have a limit on how fast they can produce
        samples.  Such streams will always return 0x40000000 as the ready-count.
        This may well exceed the length of the audio stream.  You therefore need to
        check length separately.

        If the aborted flag is set, that means the ready count is no longer being
        replenished.  For example, a MovieAudioCursor might be reading from an
        internet radio station, and it might buffer data to avoid underruns.  If it
        loses connection to the radio station, it will set the aborted flag to
        indicate that the buffer is no longer being replenished.  But it is still
        ok to read the samples that are in the buffer, at least until they run out.
        Once those are gone, there will be no more.

        An audio consumer needs to check the length, the ready status, and the
        aborted flag.
        """
    def seek(self, offset: float) -> None:
        """Skips to the specified offset within the file.

        If the movie reports that it cannot seek, then this method can still
        advance by reading samples and discarding them.  However, to move backward,
        can_seek must be true.

        If the movie reports that it can_seek, it doesn't mean that it can do so
        quickly.  It may have to rewind the movie and then fast forward to the
        desired location.  Only if can_seek_fast returns true can seek operations
        be done in constant time.

        Seeking may not be precise, because AVI files often have inaccurate
        indices.  After seeking, tell will indicate that the cursor is at the
        target location.  However, in truth, the data you read may come from a
        slightly offset location.
        """
    @overload
    def read_samples(self, n: int) -> str:
        """`(self, n: int)`:
        Read audio samples from the stream and returns them as a string.  The
        samples are stored little-endian in the string.  N is the number of samples
        you wish to read.  Multiple-channel audio will be interleaved.

        This is not particularly efficient, but it may be a convenient way to
        manipulate samples in python.

        `(self, n: int, dg: Datagram)`:
        Read audio samples from the stream into a Datagram.  N is the number of
        samples you wish to read.  Multiple-channel audio will be interleaved.

        This is not particularly efficient, but it may be a convenient way to
        manipulate samples in python.
        """
    @overload
    def read_samples(self, n: int, dg: Datagram) -> None: ...
    getSource = get_source
    audioRate = audio_rate
    audioChannels = audio_channels
    canSeek = can_seek
    canSeekFast = can_seek_fast
    skipSamples = skip_samples
    readSamples = read_samples

class FlacAudioCursor(MovieAudioCursor):
    """Implements decoding of FLAC audio files.

    @see FlacAudio
    @since 1.10.0
    """

    @overload
    def __init__(self, __param0: FlacAudioCursor) -> None:
        """Reads the .wav header from the indicated stream.  This leaves the read
        pointer positioned at the start of the data.
        """
    @overload
    def __init__(self, src: ConfigVariableFilename | Filename | FlacAudio, stream: istream) -> None: ...

class MovieVideo(TypedWritableReferenceCount, Namable):
    """A MovieVideo is actually any source that provides a sequence of video
    frames.  That could include an AVI file, a digital camera, or an internet
    TV station.

    The difference between a MovieVideo and a MovieVideoCursor is like the
    difference between a filename and a file handle.  The MovieVideo just
    indicates a particular movie.  The MovieVideoCursor is what allows access.
    """

    @property
    def filename(self) -> Filename: ...
    @property
    def subfile_info(self) -> SubfileInfo: ...
    @overload
    def __init__(self, name: str = ...) -> None:
        """This constructor returns a null video stream --- a stream of plain blue and
        white frames that last one second each.  To get more interesting video, you
        need to construct a subclass of this class.
        """
    @overload
    def __init__(self, __param0: MovieVideo) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def open(self) -> MovieVideoCursor:
        """Open this video, returning a MovieVideoCursor of the appropriate type.
        Returns NULL on error.
        """
    @staticmethod
    def get(name: StrOrBytesPath) -> MovieVideo:
        """Obtains a MovieVideo that references a file.  Just calls
        MovieTypeRegistry::make_video().
        """
    def get_filename(self) -> Filename:
        """Returns the movie's filename.  A movie is not guaranteed to have a
        filename, if not, then this function returns an empty filename.
        """
    def get_subfile_info(self) -> SubfileInfo:
        """If the movie is to be loaded from a subfile on disk, this returns the
        subfile info.  Check info.is_empty() to see if this is valid data.
        """
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToNamable = upcast_to_Namable
    getFilename = get_filename
    getSubfileInfo = get_subfile_info

class InkblotVideo(MovieVideo):
    """A cellular automaton that generates an amusing pattern of swirling colors."""

    @overload
    def __init__(self, __param0: InkblotVideo) -> None:
        """xxx"""
    @overload
    def __init__(self, x: int, y: int, fps: int) -> None: ...

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
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...
        def compare_timestamp(self, other: MovieVideoCursor.Buffer) -> int:
            """Used to sort different buffers to ensure they correspond to the same source
            frame, particularly important when synchronizing the different pages of a
            multi-page texture.

            Returns 0 if the two buffers are of the same frame, <0 if this one comes
            earlier than the other one, and >0 if the other one comes earlier.
            """
        def get_timestamp(self) -> float:
            """Returns the nearest timestamp value of this particular buffer.  Ideally,
            MovieVideoCursor::set_time() for this timestamp would return this buffer
            again.  This need be defined only if compare_timestamp() is also defined.
            """
        @staticmethod
        def get_class_type() -> TypeHandle: ...
        compareTimestamp = compare_timestamp
        getTimestamp = get_timestamp
        getClassType = get_class_type

    def __init__(self, __param0: MovieVideoCursor) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_source(self) -> MovieVideo:
        """Get the MovieVideo which this cursor references."""
    def size_x(self) -> int:
        """Get the horizontal size of the movie."""
    def size_y(self) -> int:
        """Get the vertical size of the movie."""
    def get_num_components(self) -> int:
        """Returns 4 if the movie has an alpha channel, 3 otherwise."""
    def length(self) -> float:
        """Returns the length of the movie.

        Some kinds of Movie, such as internet TV station, might not have a
        predictable length.  In that case, the length will be set to a very large
        number: 1.0E10. If the internet TV station goes offline, the video or audio
        stream will set its abort flag.  Reaching the end of the movie (ie, the
        specified length) normally does not cause the abort flag to be set.

        The video and audio streams produced by get_video and get_audio are always
        of unlimited duration - you can always read another video frame or another
        audio sample.  This is true even if the specified length is reached, or an
        abort is flagged.  If either stream runs out of data, it will synthesize
        blank video frames and silent audio samples as necessary to satisfy read
        requests.

        Some AVI files have incorrect length values encoded into them - usually,
        they're a second or two long or short.  When playing such an AVI using the
        Movie class, you may see a slightly truncated video, or a slightly
        elongated video (padded with black frames).  There are utilities out there
        to fix the length values in AVI files.
        """
    def can_seek(self) -> bool:
        """Returns true if the movie can seek.  If this is true, seeking is still not
        guaranteed to be fast: for some movies, seeking is implemented by rewinding
        to the beginning and then fast-forwarding to the desired location.  Even if
        the movie cannot seek, the fetch methods can still advance to an arbitrary
        location by reading frames and discarding them.  However, to move backward,
        can_seek must return true.
        """
    def can_seek_fast(self) -> bool:
        """Returns true if seek operations are constant time."""
    def aborted(self) -> bool:
        """Returns true if the video has aborted prematurely.  For example, this could
        occur if the Movie was actually an internet TV station, and the connection
        was lost.  Reaching the normal end of the video does not constitute an
        'abort' condition.
        """
    def ready(self) -> bool:
        """Returns true if the cursor is a streaming source, and if a video frame is
        ready to be read.  For non- streaming sources, this is always false.
        """
    def streaming(self) -> bool:
        """Returns true if the video frames are being "pushed" at us by something that
        operates at its own speed - for example, a webcam.  In this case, the
        frames come when they're ready to come.  Attempting to read too soon will
        produce nothing, reading too late will cause frames to be dropped.  In this
        case, the ready flag can be used to determine whether or not a frame is
        ready for reading.

        When streaming, you should still pay attention to last_start, but the value
        of next_start is only a guess.
        """
    def setup_texture(self, tex: Texture) -> None:
        """Set up the specified Texture object to contain content from this movie.
        This should be called once, not every frame.
        """
    def set_time(self, timestamp: float, loop_count: int) -> bool:
        """Updates the cursor to the indicated time.  If loop_count >= 1, the time is
        clamped to the movie's length * loop_count.  If loop_count <= 0, the time
        is understood to be modulo the movie's length.

        Returns true if a new frame is now available, false otherwise.  If this
        returns true, you should immediately follow this with exactly *one* call to
        fetch_buffer().

        If the movie reports that it can_seek, you may also specify a time value
        less than the previous value you passed to set_time().  Otherwise, you may
        only specify a time value greater than or equal to the previous value.

        If the movie reports that it can_seek, it doesn't mean that it can do so
        quickly.  It may have to rewind the movie and then fast forward to the
        desired location.  Only if can_seek_fast returns true can it seek rapidly.
        """
    def fetch_buffer(self) -> MovieVideoCursor.Buffer:
        """Gets the current video frame (as specified by set_time()) from the movie
        and returns it in a pre-allocated buffer.  You may simply let the buffer
        dereference and delete itself when you are done with it.

        This may return NULL (even if set_time() returned true) if the frame is not
        available for some reason.
        """
    def apply_to_texture(self, buffer: MovieVideoCursor.Buffer, t: Texture, page: int) -> None:
        """Stores this buffer's contents in the indicated texture."""
    def apply_to_texture_rgb(self, buffer: MovieVideoCursor.Buffer, t: Texture, page: int) -> None:
        """Copies this buffer's contents into the RGB channels of the supplied
        texture.  The alpha channel of the texture is not touched.
        """
    def apply_to_texture_alpha(self, buffer: MovieVideoCursor.Buffer, t: Texture, page: int, alpha_src: int) -> None:
        """Copies this buffer's contents into the alpha channel of the supplied
        texture.  The RGB channels of the texture are not touched.
        """
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

class InkblotVideoCursor(MovieVideoCursor):
    """A cellular automaton that generates an amusing pattern of swirling colors."""

    @overload
    def __init__(self, src: InkblotVideo) -> None:
        """xxx"""
    @overload
    def __init__(self, __param0: InkblotVideoCursor) -> None: ...

class MicrophoneAudio(MovieAudio):
    """Class MicrophoneAudio provides the means to read raw audio samples from a
    microphone.
    """

    @property
    def options(self) -> Sequence[MicrophoneAudio]: ...
    @property
    def channels(self) -> int: ...
    @property
    def rate(self) -> int: ...
    @staticmethod
    def get_num_options() -> int:
        """Returns the number of microphone options.  An "option" consists of a device
        plus a set of configuration parameters.  For example, "Soundblaster Audigy
        Line in at 44,100 samples/sec" would be an option.
        """
    @staticmethod
    def get_option(n: int) -> MicrophoneAudio:
        """Returns the nth microphone option."""
    def get_channels(self) -> int:
        """Returns the number of channels."""
    def get_rate(self) -> int:
        """Returns the sample rate."""
    def get_options(self) -> tuple[MicrophoneAudio, ...]: ...
    getNumOptions = get_num_options
    getOption = get_option
    getChannels = get_channels
    getRate = get_rate
    getOptions = get_options

class OpusAudio(MovieAudio):
    """Interfaces with the libopusfile library to implement decoding of Opus
    audio files.

    @since 1.10.0
    """

    @overload
    def __init__(self, name: StrOrBytesPath) -> None:
        """xxx"""
    @overload
    def __init__(self, __param0: ConfigVariableFilename | OpusAudio) -> None: ...
    @staticmethod
    def make(name: StrOrBytesPath) -> MovieAudio:
        """Obtains a MovieAudio that references a file."""

class OpusAudioCursor(MovieAudioCursor):
    """Interfaces with the libopusfile library to implement decoding of Opus
    audio files.

    @see OpusAudio
    @since 1.10.0
    """

    @overload
    def __init__(self, __param0: OpusAudioCursor) -> None:
        """Reads the .wav header from the indicated stream.  This leaves the read
        pointer positioned at the start of the data.
        """
    @overload
    def __init__(self, src: ConfigVariableFilename | Filename | OpusAudio, stream: istream) -> None: ...

class UserDataAudio(MovieAudio):
    """A UserDataAudio is a way for the user to manually supply raw audio samples.
    remove_after_read means the data will be removed if read once.  Else data
    will be stored (enable looping and seeking). Expects data as 16 bit signed
    (word); Example for stereo: 1.word = 1.channel,2.word = 2.channel, 3.word =
    1.channel,4.word = 2.channel, etc.
    """

    @overload
    def __init__(self, __param0: UserDataAudio) -> None:
        """This constructor returns a UserDataAudio --- a means to supply raw audio
        samples manually.
        """
    @overload
    def __init__(self, rate: int, channels: int, remove_after_read: bool = ...) -> None: ...
    @overload
    def append(self, str: str) -> None:
        """`(self, src: DatagramIterator, len: int = ...)`:
        Appends audio samples to the buffer from a datagram.  This is intended to
        make it easy to send streaming raw audio over a network.

        `(self, str: str)`:
        Appends audio samples to the buffer from a string.  The samples must be
        stored little-endian in the string.  This is not particularly efficient,
        but it may be convenient to deal with samples in python.
        """
    @overload
    def append(self, src: Datagram | DatagramIterator, len: int = ...) -> None: ...
    def done(self) -> None:
        """Promises not to append any more samples, ie, this marks the end of the
        audio stream.
        """

class UserDataAudioCursor(MovieAudioCursor):
    """A UserDataAudioCursor is a means to manually supply a sequence of raw audio
    samples.
    """

    @overload
    def __init__(self, src: UserDataAudio) -> None: ...
    @overload
    def __init__(self, __param0: UserDataAudioCursor) -> None: ...

class VorbisAudio(MovieAudio):
    """Interfaces with the libvorbisfile library to implement decoding of Ogg
    Vorbis audio files.
    """

    @overload
    def __init__(self, name: StrOrBytesPath) -> None:
        """xxx"""
    @overload
    def __init__(self, __param0: ConfigVariableFilename | VorbisAudio) -> None: ...
    @staticmethod
    def make(name: StrOrBytesPath) -> MovieAudio:
        """Obtains a MovieAudio that references a file."""

class VorbisAudioCursor(MovieAudioCursor):
    """Interfaces with the libvorbisfile library to implement decoding of Ogg
    Vorbis audio files.
    """

    @overload
    def __init__(self, __param0: VorbisAudioCursor) -> None:
        """Reads the .wav header from the indicated stream.  This leaves the read
        pointer positioned at the start of the data.
        """
    @overload
    def __init__(self, src: ConfigVariableFilename | Filename | VorbisAudio, stream: istream) -> None: ...

class WavAudio(MovieAudio):
    """A native PCM .wav loader.  Supported formats are linear PCM, IEEE float,
    A-law and mu-law.
    """

    @overload
    def __init__(self, name: StrOrBytesPath) -> None:
        """xxx"""
    @overload
    def __init__(self, __param0: ConfigVariableFilename | WavAudio) -> None: ...
    @staticmethod
    def make(name: StrOrBytesPath) -> MovieAudio:
        """Obtains a MovieAudio that references a file."""

class WavAudioCursor(MovieAudioCursor):
    """Used for reading PCM .wav files.  Supported formats are linear PCM, IEEE
    float, A-law and mu-law.
    """

    @overload
    def __init__(self, __param0: WavAudioCursor) -> None:
        """Reads the .wav header from the indicated stream.  This leaves the read
        pointer positioned at the start of the data.
        """
    @overload
    def __init__(self, src: ConfigVariableFilename | Filename | WavAudio, stream: istream) -> None: ...
