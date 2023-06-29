from _typeshed import StrOrBytesPath
from collections.abc import Callable, Iterator, Sequence
from enum import Enum
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias, final

from panda3d._typing import (
    DoubleMat4Like,
    DoubleVec2Like,
    DoubleVec3Like,
    DoubleVec4Like,
    IntVec2Like,
    IntVec3Like,
    IntVec4Like,
    Mat4Like,
    Vec2Like,
    Vec3Like,
    Vec4Like,
)
from panda3d.core._dtoolbase import TypedObject, TypeHandle
from panda3d.core._dtoolutil import Filename, istream, ostream
from panda3d.core._express import (
    Datagram,
    DatagramGenerator,
    DatagramIterator,
    DatagramSink,
    FileReference,
    HashVal,
    PointerToVoid,
    ReferenceCount,
    TypedReferenceCount,
    VirtualFile,
)
from panda3d.core._linmath import (
    LMatrix3d,
    LMatrix3f,
    LMatrix4d,
    LMatrix4f,
    LVecBase2d,
    LVecBase2f,
    LVecBase2i,
    LVecBase3d,
    LVecBase3f,
    LVecBase3i,
    LVecBase4d,
    LVecBase4f,
    LVecBase4i,
)
from panda3d.core._pipeline import Thread
from panda3d.core._prc import ConfigPage, ConfigVariableFilename, ConfigVariableSearchPath

_ColorSpace: TypeAlias = Literal[0, 1, 2, 3]
_AutoTextureScale: TypeAlias = Literal[0, 1, 2, 3, 4]
_BamEnums_BamEndian: TypeAlias = Literal[0, 1, 1]
_BamEnums_BamTextureMode: TypeAlias = Literal[0, 1, 2, 3, 4]
_ClockObject_Mode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]

class PointerToBase_ReferenceCountedVector_ushort(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerToArrayBase_ushort(PointerToBase_ReferenceCountedVector_ushort):
    def __eq__(self, __other: object) -> bool:
        """These are implemented in PointerToVoid, but expose them here."""
    def __ne__(self, __other: object) -> bool: ...

class ConstPointerToArray_ushort(PointerToArrayBase_ushort):
    def __init__(self, copy: ConstPointerToArray_ushort | PointerToArray_ushort) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> int: ...
    def __deepcopy__(self, memo) -> ConstPointerToArray_ushort: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[int]: ...  # Doesn't actually exist
    def get_element(self, n: int) -> int: ...
    def get_data(self) -> bytes: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: int) -> int: ...
    getElement = get_element
    getData = get_data
    getSubdata = get_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class PointerToArray_ushort(PointerToArrayBase_ushort):
    @overload
    def __init__(self, type_handle: TypeHandle | type = ...) -> None: ...
    @overload
    def __init__(self, copy: PointerToArray_ushort) -> None: ...
    @overload
    def __init__(self, source: Sequence[int]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> int: ...
    def __setitem__(self, n: int, value: int) -> None: ...
    def __deepcopy__(self, memo) -> PointerToArray_ushort: ...
    def __copy__(self) -> Self: ...
    def __iter__(self) -> Iterator[int]: ...  # Doesn't actually exist
    @staticmethod
    def empty_array(n: int, type_handle: TypeHandle | type = ...) -> PointerToArray_ushort: ...
    def push_back(self, x: int) -> None: ...
    def pop_back(self) -> None: ...
    def get_element(self, n: int) -> int: ...
    def set_element(self, n: int, value: int) -> None: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: bytes) -> None: ...
    def get_subdata(self, n: int, count: int) -> bytes: ...
    def set_subdata(self, n: int, count: int, data: str) -> None: ...
    def get_ref_count(self) -> int: ...
    def get_node_ref_count(self) -> int: ...
    def count(self, __param0: int) -> int: ...
    emptyArray = empty_array
    pushBack = push_back
    popBack = pop_back
    getElement = get_element
    setElement = set_element
    getData = get_data
    setData = set_data
    getSubdata = get_subdata
    setSubdata = set_subdata
    getRefCount = get_ref_count
    getNodeRefCount = get_node_ref_count

class AnimInterface:
    """This is the fundamental interface for things that have a play/loop/stop
    type interface for frame-based animation, such as animated characters.
    This is the base class for AnimControl and other, similar classes.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    play_rate: float
    @property
    def frame_rate(self) -> float: ...
    @property
    def num_frames(self) -> int: ...
    @property
    def frame(self) -> int: ...
    @property
    def next_frame(self) -> int: ...
    @property
    def frac(self) -> float: ...
    @property
    def full_frame(self) -> int: ...
    @property
    def full_fframe(self) -> float: ...
    @property
    def playing(self) -> bool: ...
    @overload
    def play(self) -> None:
        """`(self)`:
        Runs the entire animation from beginning to end and stops.

        `(self, _from: float, to: float)`:
        Runs the animation from the frame "from" to and including the frame "to",
        at which point the animation is stopped.  Both "from" and "to" frame
        numbers may be outside the range (0, get_num_frames()) and the animation
        will follow the range correctly, reporting numbers modulo get_num_frames().
        For instance, play(0, get_num_frames() * 2) will play the animation twice
        and then stop.
        """
    @overload
    def play(self, _from: float, to: float) -> None: ...
    @overload
    def loop(self, restart: bool) -> None:
        """`(self, restart: bool)`:
        Starts the entire animation looping.  If restart is true, the animation is
        restarted from the beginning; otherwise, it continues from the current
        frame.

        `(self, restart: bool, _from: float, to: float)`:
        Loops the animation from the frame "from" to and including the frame "to",
        indefinitely.  If restart is true, the animation is restarted from the
        beginning; otherwise, it continues from the current frame.
        """
    @overload
    def loop(self, restart: bool, _from: float, to: float) -> None: ...
    @overload
    def pingpong(self, restart: bool) -> None:
        """`(self, restart: bool)`:
        Starts the entire animation bouncing back and forth between its first frame
        and last frame.  If restart is true, the animation is restarted from the
        beginning; otherwise, it continues from the current frame.

        `(self, restart: bool, _from: float, to: float)`:
        Loops the animation from the frame "from" to and including the frame "to",
        and then back in the opposite direction, indefinitely.
        """
    @overload
    def pingpong(self, restart: bool, _from: float, to: float) -> None: ...
    def stop(self) -> None:
        """Stops a currently playing or looping animation right where it is.  The
        animation remains posed at the current frame.
        """
    def pose(self, frame: float) -> None:
        """Sets the animation to the indicated frame and holds it there."""
    def set_play_rate(self, play_rate: float) -> None:
        """Changes the rate at which the animation plays.  1.0 is the normal speed,
        2.0 is twice normal speed, and 0.5 is half normal speed.  0.0 is legal to
        pause the animation, and a negative value will play the animation
        backwards.
        """
    def get_play_rate(self) -> float:
        """Returns the rate at which the animation plays.  See set_play_rate()."""
    def get_frame_rate(self) -> float:
        """Returns the native frame rate of the animation.  This is the number of
        frames per second that will elapse when the play_rate is set to 1.0.  It is
        a fixed property of the animation and may not be adjusted by the user.
        """
    def get_num_frames(self) -> int:
        """Returns the number of frames in the animation.  This is a property of the
        animation and may not be directly adjusted by the user (although it may
        change without warning with certain kinds of animations, since this is a
        virtual method that may be overridden).
        """
    def get_frame(self) -> int:
        """Returns the current integer frame number.  This number will be in the range
        0 <= f < get_num_frames().
        """
    def get_next_frame(self) -> int:
        """Returns the current integer frame number + 1, constrained to the range 0 <=
        f < get_num_frames().

        If the play mode is PM_play, this will clamp to the same value as
        get_frame() at the end of the animation.  If the play mode is any other
        value, this will wrap around to frame 0 at the end of the animation.
        """
    def get_frac(self) -> float:
        """Returns the fractional part of the current frame.  Normally, this is in the
        range 0.0 <= f < 1.0, but in the one special case of an animation playing
        to its end frame and stopping, it might exactly equal 1.0.

        It will always be true that get_full_frame() + get_frac() ==
        get_full_fframe().
        """
    def get_full_frame(self) -> int:
        """Returns the current integer frame number.

        Unlike the value returned by get_frame(), this frame number may extend
        beyond the range of get_num_frames() if the frame range passed to play(),
        loop(), etc.  did.

        Unlike the value returned by get_full_fframe(), this return value will
        never exceed the value passed to to_frame in the play() method.
        """
    def get_full_fframe(self) -> float:
        """Returns the current floating-point frame number.

        Unlike the value returned by get_frame(), this frame number may extend
        beyond the range of get_num_frames() if the frame range passed to play(),
        loop(), etc.  did.

        Unlike the value returned by get_full_frame(), this return value may equal
        (to_frame + 1.0), when the animation has played to its natural end.
        However, in this case the return value of get_full_frame() will be
        to_frame, not (to_frame + 1).
        """
    def is_playing(self) -> bool:
        """Returns true if the animation is currently playing, false if it is stopped
        (e.g.  because stop() or pose() was called, or because it reached the end
        of the animation after play() was called).
        """
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setPlayRate = set_play_rate
    getPlayRate = get_play_rate
    getFrameRate = get_frame_rate
    getNumFrames = get_num_frames
    getFrame = get_frame
    getNextFrame = get_next_frame
    getFrac = get_frac
    getFullFrame = get_full_frame
    getFullFframe = get_full_fframe
    isPlaying = is_playing
    getClassType = get_class_type

class UpdateSeq:
    """This is a sequence number that increments monotonically.  It can be used to
    track cache updates, or serve as a kind of timestamp for any changing
    properties.

    A special class is used instead of simply an int, so we can elegantly
    handle such things as wraparound and special cases.  There are two special
    cases.  Firstly, a sequence number is 'initial' when it is first created.
    This sequence is older than any other sequence number.  Secondly, a
    sequence number may be explicitly set to 'old'.  This is older than any
    other sequence number except 'initial'.  Finally, we have the explicit
    number 'fresh', which is newer than any other sequence number.  All other
    sequences are numeric and are monotonically increasing.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def seq(self) -> int: ...
    def __init__(self, copy: UpdateSeq = ...) -> None:
        """Creates an UpdateSeq in the 'initial' state."""
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: UpdateSeq) -> bool: ...
    def __le__(self, other: UpdateSeq) -> bool: ...
    def __gt__(self, other: UpdateSeq) -> bool: ...
    def __ge__(self, other: UpdateSeq) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def initial() -> UpdateSeq: ...
    @staticmethod
    def old() -> UpdateSeq: ...
    @staticmethod
    def fresh() -> UpdateSeq: ...
    def assign(self, copy: Self) -> Self: ...
    def clear(self) -> None:
        """Resets the UpdateSeq to the 'initial' state."""
    def is_initial(self) -> bool:
        """Returns true if the UpdateSeq is in the 'initial' state."""
    def is_old(self) -> bool:
        """Returns true if the UpdateSeq is in the 'old' state."""
    def is_fresh(self) -> bool:
        """Returns true if the UpdateSeq is in the 'fresh' state."""
    def is_special(self) -> bool:
        """Returns true if the UpdateSeq is in any special states, i.e.  'initial',
        'old', or 'fresh'.
        """
    def increment(self) -> UpdateSeq: ...
    def get_seq(self) -> int:
        """Returns the internal integer value associated with the UpdateSeq.  Useful
        for debugging only.
        """
    def output(self, out: ostream) -> None: ...
    isInitial = is_initial
    isOld = is_old
    isFresh = is_fresh
    isSpecial = is_special
    getSeq = get_seq

class TypedWritable(TypedObject):
    """Base class for objects that can be written to and read from Bam files.

    See also TypedObject for detailed instructions.
    """

    def __reduce_persist__(self, pickler): ...
    def fillin(self, scan: Datagram | DatagramIterator, manager: BamReader) -> None:
        """This internal function is intended to be called by each class's
        make_from_bam() method to read in all of the relevant data from the BamFile
        for the new object.  It is also called directly by the BamReader to re-read
        the data for an object that has been placed on the stream for an update.
        """
    def mark_bam_modified(self) -> None:
        """Increments the bam_modified counter, so that this object will be
        invalidated and retransmitted on any open bam streams.  This should
        normally not need to be called by user code; it should be called internally
        when the object has been changed in a way that legitimately requires its
        retransmission to any connected clients.
        """
    def get_bam_modified(self) -> UpdateSeq:
        """Returns the current bam_modified counter.  This counter is normally
        incremented automatically whenever the object is modified.
        """
    @overload
    def encode_to_bam_stream(self) -> bytes:
        """`(self)`:
        Converts the TypedWritable object into a single stream of data using a
        BamWriter, and returns that data as a bytes object.  Returns an empty bytes
        object on failure.

        This is a convenience method particularly useful for cases when you are
        only serializing a single object.  If you have many objects to process, it
        is more efficient to use the same BamWriter to serialize all of them
        together.

        `(self, data: bytes, writer: BamWriter = ...)`:
        Converts the TypedWritable object into a single stream of data using a
        BamWriter, and stores that data in the indicated string.  Returns true on
        success, false on failure.

        This is a convenience method particularly useful for cases when you are
        only serializing a single object.  If you have many objects to process, it
        is more efficient to use the same BamWriter to serialize all of them
        together.
        """
    @overload
    def encode_to_bam_stream(self, data: bytes, writer: BamWriter = ...) -> bool: ...
    markBamModified = mark_bam_modified
    getBamModified = get_bam_modified
    encodeToBamStream = encode_to_bam_stream

class TypedWritableReferenceCount(TypedWritable, ReferenceCount):
    """A base class for things which need to inherit from both TypedWritable and
    from ReferenceCount.  It's convenient to define this intermediate base
    class instead of multiply inheriting from the two classes each time they
    are needed, so that we can sensibly pass around pointers to things which
    are both TypedWritables and ReferenceCounters.

    See also TypedObject for detailed instructions.
    """

    def upcast_to_TypedWritable(self) -> TypedWritable: ...
    def upcast_to_ReferenceCount(self) -> ReferenceCount: ...
    @staticmethod
    def decode_from_bam_stream(data: bytes, reader: BamReader = ...) -> TypedWritableReferenceCount:
        """Reads the bytes created by a previous call to encode_to_bam_stream(), and
        extracts and returns the single object on those bytes.  Returns NULL on
        error.

        This method is intended to replace decode_raw_from_bam_stream() when you
        know the stream in question returns an object of type
        TypedWritableReferenceCount, allowing for easier reference count
        management.  Note that the caller is still responsible for maintaining the
        reference count on the return value.
        """
    upcastToTypedWritable = upcast_to_TypedWritable
    upcastToReferenceCount = upcast_to_ReferenceCount
    decodeFromBamStream = decode_from_bam_stream

class BamCacheRecord(TypedWritableReferenceCount):
    """An instance of this class is written to the front of a Bam or Txo file to
    make the file a cached instance of some other loadable resource.  This
    record contains information needed to test the validity of the cache.
    """

    data: TypedWritable
    @property
    def source_pathname(self) -> Filename: ...
    @property
    def cache_filename(self) -> Filename: ...
    @property
    def source_timestamp(self) -> int: ...
    @property
    def recorded_time(self) -> int: ...
    def __eq__(self, __other: object) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def make_copy(self) -> BamCacheRecord:
        """Returns a duplicate of the BamCacheRecord.  The duplicate will not have a
        data pointer set, even though one may have been assigned to the original
        via set_data().
        """
    def get_source_pathname(self) -> Filename:
        """Returns the full pathname to the source file that originally generated this
        cache request.  In some cases, for instance in the case of a of a multipage
        texture like "cube_#.png", this may not not a true filename on disk.
        """
    def get_cache_filename(self) -> Filename:
        """Returns the name of the cache file as hashed from the source_pathname.
        This will be relative to the root of the cache directory, and it will not
        include any suffixes that may be appended to resolve hash conflicts.
        """
    def get_source_timestamp(self) -> int:
        """Returns the file timestamp of the original source file that generated this
        cache record, if available.  In some cases the original file timestamp is
        not available, and this will return 0.
        """
    def get_recorded_time(self) -> int:
        """Returns the time at which this particular record was recorded or updated."""
    def get_num_dependent_files(self) -> int:
        """Returns the number of source files that contribute to the cache."""
    def get_dependent_pathname(self, n: int) -> Filename:
        """Returns the full pathname of the nth source files that contributes to the
        cache.
        """
    def dependents_unchanged(self) -> bool:
        """Returns true if all of the dependent files are still the same as when the
        cache was recorded, false otherwise.
        """
    def clear_dependent_files(self) -> None:
        """Empties the list of files that contribute to the data in this record."""
    @overload
    def add_dependent_file(self, pathname: StrOrBytesPath) -> None:
        """`(self, pathname: Filename)`:
        Adds the indicated file to the list of files that will be loaded to
        generate the data in this record.  This should be called once for the
        primary source file, and again for each secondary source file, if any.

        `(self, file: VirtualFile)`:
        Variant of add_dependent_file that takes an already opened VirtualFile.
        """
    @overload
    def add_dependent_file(self, file: VirtualFile) -> None: ...
    def has_data(self) -> bool:
        """Returns true if this cache record has an in-memory data object associated--
        that is, the object stored in the cache.
        """
    def clear_data(self) -> None:
        """Removes the in-memory data object associated with this record, if any.
        This does not affect the on-disk representation of the record.
        """
    def get_data(self) -> TypedWritable:
        """Returns a pointer to the data stored in the record, or NULL if there is no
        data.  The pointer is not removed from the record.
        """
    @overload
    def set_data(self, ptr: TypedWritable, ref_ptr: ReferenceCount = ...) -> None:
        """`(self, ptr: TypedWritable)`:
        This variant on set_data() is provided to easily pass objects deriving from
        TypedWritable.

        `(self, ptr: TypedWritable, ref_ptr: ReferenceCount)`:
        Stores a new data object on the record.  You should pass the same pointer
        twice, to both parameters; this allows the C++ typecasting to automatically
        convert the pointer into both a TypedWritable and a ReferenceCount pointer,
        so that the BamCacheRecord object can reliably manage the reference counts.

        You may pass 0 or NULL as the second parameter.  If you do this, the
        BamCacheRecord will not manage the object's reference count; it will be up
        to you to ensure the object is not deleted during the lifetime of the
        BamCacheRecord object.

        `(self, ptr: TypedWritable, dummy: int)`:
        This variant on set_data() is provided just to allow Python code to pass a
        0 as the second parameter.

        `(self, ptr: TypedWritableReferenceCount)`:
        This variant on set_data() is provided to easily pass objects deriving from
        TypedWritableReferenceCount.
        """
    @overload
    def set_data(self, ptr: TypedWritable, dummy: int) -> None: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    makeCopy = make_copy
    getSourcePathname = get_source_pathname
    getCacheFilename = get_cache_filename
    getSourceTimestamp = get_source_timestamp
    getRecordedTime = get_recorded_time
    getNumDependentFiles = get_num_dependent_files
    getDependentPathname = get_dependent_pathname
    dependentsUnchanged = dependents_unchanged
    clearDependentFiles = clear_dependent_files
    addDependentFile = add_dependent_file
    hasData = has_data
    clearData = clear_data
    getData = get_data
    setData = set_data

class BamCache:
    """This class maintains a cache of Bam and/or Txo objects generated from model
    files and texture images (as well as possibly other kinds of loadable
    objects that can be stored in bam file format).

    This class also maintains a persistent index that lists all of the cached
    objects (see BamCacheIndex). We go through some considerable effort to make
    sure this index gets saved correctly to disk, even in the presence of
    multiple different processes writing to the same index, and without relying
    too heavily on low-level os-provided file locks (which work poorly with C++
    iostreams).
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    active: bool
    cache_models: bool
    cache_textures: bool
    cache_compressed_textures: bool
    cache_compiled_shaders: bool
    root: Filename
    flush_time: int
    cache_max_kbytes: int
    read_only: bool
    def __init__(self) -> None: ...
    def set_active(self, flag: bool) -> None:
        """Changes the state of the active flag.  "active" means that the cache should
        be consulted automatically on loads, "not active" means that objects should
        be loaded directly without consulting the cache.

        This represents the global flag.  Also see the individual cache_models,
        cache_textures, cache_compressed_textures flags.
        """
    def get_active(self) -> bool:
        """Returns true if the BamCache is currently active, false if it is not.
        "active" means that the cache should be consulted automatically on loads,
        "not active" means that objects should be loaded directly without
        consulting the cache.

        This represents the global flag.  Also see the individual cache_models,
        cache_textures, cache_compressed_textures flags.
        """
    def set_cache_models(self, flag: bool) -> None:
        """Indicates whether model files (e.g.  egg files and bam files) will be
        stored in the cache, as bam files.
        """
    def get_cache_models(self) -> bool:
        """Returns whether model files (e.g.  egg files and bam files) will be stored
        in the cache, as bam files.

        This also returns false if get_active() is false.
        """
    def set_cache_textures(self, flag: bool) -> None:
        """Indicates whether texture files will be stored in the cache, as
        uncompressed txo files.
        """
    def get_cache_textures(self) -> bool:
        """Returns whether texture files (e.g.  egg files and bam files) will be
        stored in the cache, as txo files.

        This also returns false if get_active() is false.
        """
    def set_cache_compressed_textures(self, flag: bool) -> None:
        """Indicates whether compressed texture files will be stored in the cache, as
        compressed txo files.  The compressed data may either be generated in-CPU,
        via the squish library, or it may be extracted from the GSG after the
        texture has been loaded.

        This may be set in conjunction with set_cache_textures(), or independently
        of it.  If set_cache_textures() is true and this is false, all textures
        will be cached in their uncompressed form.  If set_cache_textures() is
        false and this is true, only compressed textures will be cached, and they
        will be cached in their compressed form.  If both are true, all textures
        will be cached, in their uncompressed or compressed form appropriately.
        """
    def get_cache_compressed_textures(self) -> bool:
        """Returns whether compressed texture files will be stored in the cache, as
        compressed txo files.  See set_cache_compressed_textures().

        This also returns false if get_active() is false.
        """
    def set_cache_compiled_shaders(self, flag: bool) -> None:
        """Indicates whether compiled shader programs will be stored in the cache, as
        binary .sho files.  This may not be supported by all shader languages or
        graphics renderers.
        """
    def get_cache_compiled_shaders(self) -> bool:
        """Returns whether compiled shader programs will be stored in the cache, as
        binary .txo files.  See set_cache_compiled_shaders().

        This also returns false if get_active() is false.
        """
    def set_root(self, root: StrOrBytesPath) -> None:
        """Changes the current root pathname of the cache.  This specifies where the
        cache files are stored on disk.  This should name a directory that is on a
        disk local to the machine (not on a network-mounted disk), for instance,
        /tmp/panda-cache or /c/panda-cache.

        If the directory does not already exist, it will be created as a result of
        this call.
        """
    def get_root(self) -> Filename:
        """Returns the current root pathname of the cache.  See set_root()."""
    def set_flush_time(self, flush_time: int) -> None:
        """Specifies the time in seconds between automatic flushes of the cache index."""
    def get_flush_time(self) -> int:
        """Returns the time in seconds between automatic flushes of the cache index."""
    def set_cache_max_kbytes(self, max_kbytes: int) -> None:
        """Specifies the maximum size, in kilobytes, which the cache is allowed to
        grow to.  If a newly cached file would exceed this size, an older file is
        removed from the cache.

        Note that in the case of multiple different processes simultaneously
        operating on the same cache directory, the actual cache size may slightly
        exceed this value from time to time due to latency in checking between the
        processes.
        """
    def get_cache_max_kbytes(self) -> int:
        """Returns the maximum size, in kilobytes, which the cache is allowed to grow
        to.  See set_cache_max_kbytes().
        """
    def set_read_only(self, ro: bool) -> None:
        """Can be used to put the cache in read-only mode, or take it out of read-only
        mode.  Note that if you put it into read-write mode, and it discovers that
        it does not have write access, it will put itself right back into read-only
        mode.
        """
    def get_read_only(self) -> bool:
        """Returns true if the cache is in read-only mode.  Normally, the cache starts
        in read-write mode.  It can put itself into read-only mode automatically if
        it discovers that it does not have write access to the cache.
        """
    def lookup(self, source_filename: StrOrBytesPath, cache_extension: str) -> BamCacheRecord:
        """Looks up a file in the cache.

        If the file is cacheable, then regardless of whether the file is found in
        the cache or not, this returns a BamCacheRecord.  On the other hand, if the
        file cannot be cached, returns NULL.

        If record->has_data() returns true, then the file was found in the cache,
        and you may call record->extract_data() to get the object.  If
        record->has_data() returns false, then the file was not found in the cache
        or the cache was stale; and you should reload the source file (calling
        record->add_dependent_file() for each file loaded, including the original
        source file), and then call record->set_data() to record the resulting
        loaded object; and finally, you should call store() to write the cached
        record to disk.
        """
    def store(self, record: BamCacheRecord) -> bool:
        """Flushes a cache entry to disk.  You must have retrieved the cache record
        via a prior call to lookup(), and then stored the data via
        record->set_data().  Returns true on success, false on failure.
        """
    def consider_flush_index(self) -> None:
        """Flushes the index if enough time has elapsed since the index was last
        flushed.
        """
    def flush_index(self) -> None:
        """Ensures the index is written to disk."""
    def list_index(self, out: ostream, indent_level: int = ...) -> None:
        """Writes the contents of the index to standard output."""
    @staticmethod
    def get_global_ptr() -> BamCache:
        """Returns a pointer to the global BamCache object, which is used
        automatically by the ModelPool and TexturePool.
        """
    @staticmethod
    def consider_flush_global_index() -> None:
        """If there is a global BamCache object, calls consider_flush_index() on it."""
    @staticmethod
    def flush_global_index() -> None:
        """If there is a global BamCache object, calls flush_index() on it."""
    setActive = set_active
    getActive = get_active
    setCacheModels = set_cache_models
    getCacheModels = get_cache_models
    setCacheTextures = set_cache_textures
    getCacheTextures = get_cache_textures
    setCacheCompressedTextures = set_cache_compressed_textures
    getCacheCompressedTextures = get_cache_compressed_textures
    setCacheCompiledShaders = set_cache_compiled_shaders
    getCacheCompiledShaders = get_cache_compiled_shaders
    setRoot = set_root
    getRoot = get_root
    setFlushTime = set_flush_time
    getFlushTime = get_flush_time
    setCacheMaxKbytes = set_cache_max_kbytes
    getCacheMaxKbytes = get_cache_max_kbytes
    setReadOnly = set_read_only
    getReadOnly = get_read_only
    considerFlushIndex = consider_flush_index
    flushIndex = flush_index
    listIndex = list_index
    getGlobalPtr = get_global_ptr
    considerFlushGlobalIndex = consider_flush_global_index
    flushGlobalIndex = flush_global_index

class BamEnums:
    """This class exists just to provide scoping for the enums shared by BamReader
    and BamWriter.
    """

    BE_bigendian: Final = 0
    BEBigendian: Final = 0
    BE_littleendian: Final = 1
    BELittleendian: Final = 1
    BE_native: Final = 1
    BENative: Final = 1
    BOC_push: Final = 0
    BOCPush: Final = 0
    BOC_pop: Final = 1
    BOCPop: Final = 1
    BOC_adjunct: Final = 2
    BOCAdjunct: Final = 2
    BOC_remove: Final = 3
    BOCRemove: Final = 3
    BOC_file_data: Final = 4
    BOCFileData: Final = 4
    BTM_unchanged: Final = 0
    BTMUnchanged: Final = 0
    BTM_fullpath: Final = 1
    BTMFullpath: Final = 1
    BTM_relative: Final = 2
    BTMRelative: Final = 2
    BTM_basename: Final = 3
    BTMBasename: Final = 3
    BTM_rawdata: Final = 4
    BTMRawdata: Final = 4
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: BamEnums = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...

class LoaderOptions:
    """Specifies parameters that may be passed to the loader."""

    LF_search: Final = 1
    LFSearch: Final = 1
    LF_report_errors: Final = 2
    LFReportErrors: Final = 2
    LF_convert_skeleton: Final = 4
    LFConvertSkeleton: Final = 4
    LF_convert_channels: Final = 8
    LFConvertChannels: Final = 8
    LF_convert_anim: Final = 12
    LFConvertAnim: Final = 12
    LF_no_disk_cache: Final = 16
    LFNoDiskCache: Final = 16
    LF_no_ram_cache: Final = 32
    LFNoRamCache: Final = 32
    LF_no_cache: Final = 48
    LFNoCache: Final = 48
    LF_cache_only: Final = 64
    LFCacheOnly: Final = 64
    LF_allow_instance: Final = 128
    LFAllowInstance: Final = 128
    TF_preload: Final = 4
    TFPreload: Final = 4
    TF_preload_simple: Final = 8
    TFPreloadSimple: Final = 8
    TF_allow_1d: Final = 16
    TFAllow1d: Final = 16
    TF_generate_mipmaps: Final = 32
    TFGenerateMipmaps: Final = 32
    TF_multiview: Final = 64
    TFMultiview: Final = 64
    TF_integer: Final = 128
    TFInteger: Final = 128
    TF_float: Final = 256
    TFFloat: Final = 256
    TF_allow_compression: Final = 512
    TFAllowCompression: Final = 512
    DtoolClassDict: ClassVar[dict[str, Any]]
    flags: int
    texture_flags: int
    texture_num_views: int
    auto_texture_scale: _AutoTextureScale
    @overload
    def __init__(self, flags: int = ...) -> None: ...
    @overload
    def __init__(self, __param0: LoaderOptions) -> None: ...
    @overload
    def __init__(self, flags: int, texture_flags: int) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_flags(self, flags: int) -> None: ...
    def get_flags(self) -> int: ...
    def set_texture_flags(self, flags: int) -> None: ...
    def get_texture_flags(self) -> int: ...
    def set_texture_num_views(self, num_views: int) -> None:
        """Specifies the expected number of views to load for the texture.  This is
        ignored unless TF_multiview is included in texture_flags.  This must be
        specified when loading a 3-d multiview texture or 2-d texture array, in
        which case it is used to differentiate z levels from separate views; it
        may be zero in the case of 2-d textures or cube maps, in which case the
        number of views can be inferred from the number of images found on disk.
        """
    def get_texture_num_views(self) -> int:
        """See set_texture_num_views()."""
    def set_auto_texture_scale(self, scale: _AutoTextureScale) -> None:
        """Set this flag to ATS_none, ATS_up, ATS_down, or ATS_pad to control how a
        texture is scaled from disk when it is subsequently loaded.  Set it to
        ATS_unspecified to restore the default behavior.
        """
    def get_auto_texture_scale(self) -> _AutoTextureScale:
        """See set_auto_texture_scale()."""
    def output(self, out: ostream) -> None: ...
    setFlags = set_flags
    getFlags = get_flags
    setTextureFlags = set_texture_flags
    getTextureFlags = get_texture_flags
    setTextureNumViews = set_texture_num_views
    getTextureNumViews = get_texture_num_views
    setAutoTextureScale = set_auto_texture_scale
    getAutoTextureScale = get_auto_texture_scale

class BamReader(BamEnums):
    """This is the fundamental interface for extracting binary objects from a Bam
    file, as generated by a BamWriter.

    A Bam file can be thought of as a linear collection of objects.  Each
    object is an instance of a class that inherits, directly or indirectly,
    from TypedWritable.  The objects may include pointers to other objects
    within the Bam file; the BamReader automatically manages these (with help
    from code within each class) and restores the pointers correctly.

    This is the abstract interface and does not specifically deal with disk
    files, but rather with a DatagramGenerator of some kind, which is simply a
    linear source of Datagrams.  It is probably from a disk file, but it might
    conceivably be streamed directly from a network or some such nonsense.

    Bam files are most often used to store scene graphs or subgraphs, and by
    convention they are given filenames ending in the extension ".bam" when
    they are used for this purpose.  However, a Bam file may store any
    arbitrary list of TypedWritable objects; in this more general usage, they
    are given filenames ending in ".boo" to differentiate them from the more
    common scene graph files.

    See also BamFile, which defines a higher-level interface to read and write
    Bam files on disk.
    """

    source: DatagramGenerator
    loader_options: LoaderOptions
    @property
    def filename(self) -> Filename: ...
    @property
    def file_version(self) -> tuple[int, int]: ...
    @property
    def file_endian(self) -> _BamEnums_BamEndian: ...
    @property
    def file_stdfloat_double(self) -> bool: ...
    def __init__(self, source: DatagramGenerator = ...) -> None:
        """The primary interface for a caller."""
    def set_source(self, source: DatagramGenerator) -> None:
        """Changes the source of future datagrams for this BamReader.  This also
        implicitly calls init() if it has not already been called.
        """
    def get_source(self) -> DatagramGenerator:
        """Returns the current source of the BamReader as set by set_source() or the
        constructor.
        """
    def init(self) -> bool:
        """Initializes the BamReader prior to reading any objects from its source.
        This includes reading the Bam header.

        This returns true if the BamReader successfully initialized, false
        otherwise.
        """
    def get_filename(self) -> Filename:
        """If a BAM is a file, then the BamReader should contain the name of the file.
        This enables the reader to interpret pathnames in the BAM as relative to
        the directory containing the BAM.
        """
    def get_loader_options(self) -> LoaderOptions:
        """Returns the LoaderOptions passed to the loader when the model was
        requested, if any.
        """
    def set_loader_options(self, options: LoaderOptions) -> None:
        """Specifies the LoaderOptions for this BamReader."""
    def read_object(self) -> TypedWritable:
        """Reads a single object from the Bam file.  If the object type is known, a
        new object of the appropriate type is created and returned; otherwise, NULL
        is returned.  NULL is also returned when the end of the file is reached.
        is_eof() may be called to differentiate between these two cases.

        This may be called repeatedly to extract out all the objects in the Bam
        file, but typically (especially for scene graph files, indicated with the
        .bam extension), only one object is retrieved directly from the Bam file:
        the root of the scene graph.  The remaining objects will all be retrieved
        recursively by the first object.

        Note that the object returned may not yet be complete.  In particular, some
        of its pointers may not be filled in; you must call resolve() to fill in
        all the available pointers before you can safely use any objects returned
        by read_object().

        This flavor of read_object() requires the caller to know what type of
        object it has received in order to properly manage the reference counts.
        """
    def is_eof(self) -> bool:
        """Returns true if the reader has reached end-of-file, false otherwise.  This
        call is only valid after a call to read_object().
        """
    def resolve(self) -> bool:
        """This may be called at any time during processing of the Bam file to resolve
        all the known pointers so far.  It is usually called at the end of the
        processing, after all objects have been read, which is generally the best
        time to call it.

        This must be called at least once after reading a particular object via
        get_object() in order to validate that object.

        The return value is true if all objects have been resolved, or false if
        some objects are still outstanding (in which case you will need to call
        resolve() again later).
        """
    def change_pointer(self, orig_pointer: TypedWritable, new_pointer: TypedWritable) -> bool:
        """Indicates that an object recently read from the bam stream should be
        replaced with a new object.  Any future occurrences of the original object
        in the stream will henceforth return the new object instead.

        The return value is true if the replacement was successfully made, or false
        if the object was not read from the stream (or if change_pointer had
        already been called on it).
        """
    def get_file_major_ver(self) -> int:
        """Returns the major version number of the Bam file currently being read."""
    def get_file_minor_ver(self) -> int:
        """Returns the minor version number of the Bam file currently being read."""
    def get_file_endian(self) -> _BamEnums_BamEndian:
        """Returns the endian preference indicated by the Bam file currently being
        read.  This does not imply that every number is stored using the indicated
        convention, but individual objects may choose to respect this flag when
        recording data.
        """
    def get_file_stdfloat_double(self) -> bool:
        """Returns true if the file stores all "standard" floats as 64-bit doubles, or
        false if they are 32-bit floats.  This is determined by the compilation
        flags of the version of Panda that generated this file.
        """
    def get_current_major_ver(self) -> int:
        """Returns the major version number of Bam files supported by the current code
        base.  This must match get_file_major_ver() in order to successfully read a
        file.
        """
    def get_current_minor_ver(self) -> int:
        """Returns the minor version number of Bam files supported by the current code
        base.  This must match or exceed get_file_minor_ver() in order to
        successfully read a file.
        """
    def get_file_version(self) -> tuple[int, int]: ...
    @staticmethod
    def register_factory(handle: TypeHandle | type, func) -> None: ...
    setSource = set_source
    getSource = get_source
    getFilename = get_filename
    getLoaderOptions = get_loader_options
    setLoaderOptions = set_loader_options
    readObject = read_object
    isEof = is_eof
    changePointer = change_pointer
    getFileMajorVer = get_file_major_ver
    getFileMinorVer = get_file_minor_ver
    getFileEndian = get_file_endian
    getFileStdfloatDouble = get_file_stdfloat_double
    getCurrentMajorVer = get_current_major_ver
    getCurrentMinorVer = get_current_minor_ver
    getFileVersion = get_file_version
    registerFactory = register_factory

class BamWriter(BamEnums):
    """This is the fundamental interface for writing binary objects to a Bam file,
    to be extracted later by a BamReader.

    A Bam file can be thought of as a linear collection of objects.  Each
    object is an instance of a class that inherits, directly or indirectly,
    from TypedWritable.  The objects may include pointers to other objects; the
    BamWriter automatically manages these (with help from code within each
    class) and writes all referenced objects to the file in such a way that the
    pointers may be correctly restored later.

    This is the abstract interface and does not specifically deal with disk
    files, but rather with a DatagramSink of some kind, which simply accepts a
    linear stream of Datagrams.  It is probably written to a disk file, but it
    might conceivably be streamed directly to a network or some such nonsense.

    Bam files are most often used to store scene graphs or subgraphs, and by
    convention they are given filenames ending in the extension ".bam" when
    they are used for this purpose.  However, a Bam file may store any
    arbitrary list of TypedWritable objects; in this more general usage, they
    are given filenames ending in ".boo" to differentiate them from the more
    common scene graph files.

    See also BamFile, which defines a higher-level interface to read and write
    Bam files on disk.
    """

    target: DatagramSink
    root_node: TypedWritable
    @property
    def filename(self) -> Filename: ...
    @property
    def file_endian(self) -> _BamEnums_BamEndian: ...
    @property
    def file_stdfloat_double(self) -> bool: ...
    @property
    def file_texture_mode(self) -> _BamEnums_BamTextureMode: ...
    @overload
    def __init__(self, target: DatagramSink = ...) -> None: ...
    @overload
    def __init__(self, __param0: BamWriter) -> None: ...
    def set_target(self, target: DatagramSink) -> None:
        """Changes the destination of future datagrams written by the BamWriter.  This
        also implicitly calls init() if it has not already been called.
        """
    def get_target(self) -> DatagramSink:
        """Returns the current target of the BamWriter as set by set_target() or the
        constructor.
        """
    def init(self) -> bool:
        """Initializes the BamWriter prior to writing any objects to its output
        stream.  This includes writing out the Bam header.

        This returns true if the BamWriter successfully initialized, false
        otherwise.
        """
    def get_filename(self) -> Filename:
        """If a BAM is a file, then the BamWriter should contain the name of the file.
        This enables the writer to convert pathnames in the BAM to relative to the
        directory containing the BAM.
        """
    def write_object(self, obj: TypedWritable) -> bool:
        """Writes a single object to the Bam file, so that the
        BamReader::read_object() can later correctly restore the object and all its
        pointers.

        This implicitly also writes any additional objects this object references
        (if they haven't already been written), so that pointers may be fully
        resolved.

        This may be called repeatedly to write a sequence of objects to the Bam
        file, but typically (especially for scene graph files, indicated with the
        .bam extension), only one object is written directly from the Bam file: the
        root of the scene graph.  The remaining objects will all be written
        recursively by the first object.

        Returns true if the object is successfully written, false otherwise.
        """
    def has_object(self, obj: TypedWritable) -> bool:
        """Returns true if the object has previously been written (or at least
        requested to be written) to the bam file, or false if we've never heard of
        it before.
        """
    def flush(self) -> None:
        """Ensures that all data written thus far is manifested on the output stream."""
    def get_file_major_ver(self) -> int:
        """Returns the major version number of the Bam file currently being written."""
    def get_file_minor_ver(self) -> int:
        """Returns the minor version number of the Bam file currently being written."""
    def set_file_minor_ver(self, minor_ver: int) -> None:
        """Changes the minor .bam version to write.  This should be called before
        init().  Each Panda version has only a fairly narrow range of versions it
        is able to write; consult the .bam documentation for more information.
        """
    def get_file_endian(self) -> _BamEnums_BamEndian:
        """Returns the endian preference indicated by the Bam file currently being
        written.  This does not imply that every number is stored using the
        indicated convention, but individual objects may choose to respect this
        flag when recording data.
        """
    def get_file_stdfloat_double(self) -> bool:
        """Returns true if the file will store all "standard" floats as 64-bit
        doubles, or false if they are 32-bit floats.  This isn't runtime settable;
        it's based on the compilation flags of the version of Panda that generated
        this file.
        """
    def get_file_texture_mode(self) -> _BamEnums_BamTextureMode:
        """Returns the BamTextureMode preference indicated by the Bam file currently
        being written.  Texture objects written to this Bam file will be encoded
        according to the specified mode.
        """
    def set_file_texture_mode(self, file_texture_mode: _BamEnums_BamTextureMode) -> None:
        """Changes the BamTextureMode preference for the Bam file currently being
        written.  Texture objects written to this Bam file will be encoded
        according to the specified mode.
        """
    def get_root_node(self) -> TypedWritable:
        """Returns the root node of the part of the scene graph we are currently
        writing out.  This is used for determining what to make NodePaths relative
        to.
        """
    def set_root_node(self, root_node: TypedWritable) -> None:
        """Sets the root node of the part of the scene graph we are currently writing
        out.  NodePaths written to this bam file will be relative to this node.
        """
    setTarget = set_target
    getTarget = get_target
    getFilename = get_filename
    writeObject = write_object
    hasObject = has_object
    getFileMajorVer = get_file_major_ver
    getFileMinorVer = get_file_minor_ver
    setFileMinorVer = set_file_minor_ver
    getFileEndian = get_file_endian
    getFileStdfloatDouble = get_file_stdfloat_double
    getFileTextureMode = get_file_texture_mode
    setFileTextureMode = set_file_texture_mode
    getRootNode = get_root_node
    setRootNode = set_root_node

class BitMask_uint16_t_16:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: BitMask_uint16_t_16 = ...) -> None: ...
    @overload
    def __init__(self, init_value: int) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: BitMask_uint16_t_16 | int) -> bool: ...
    def __and__(self, other: BitMask_uint16_t_16 | int) -> BitMask_uint16_t_16: ...
    def __or__(self, other: BitMask_uint16_t_16 | int) -> BitMask_uint16_t_16: ...
    def __xor__(self, other: BitMask_uint16_t_16 | int) -> BitMask_uint16_t_16: ...
    def __invert__(self) -> BitMask_uint16_t_16: ...
    def __lshift__(self, shift: int) -> BitMask_uint16_t_16: ...
    def __rshift__(self, shift: int) -> BitMask_uint16_t_16: ...
    def __iand__(self, other: BitMask_uint16_t_16 | int) -> Self: ...
    def __ior__(self, other: BitMask_uint16_t_16 | int) -> Self: ...
    def __ixor__(self, other: BitMask_uint16_t_16 | int) -> Self: ...
    def __ilshift__(self, shift: int) -> Self: ...
    def __irshift__(self, shift: int) -> Self: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def all_on() -> BitMask_uint16_t_16: ...
    @staticmethod
    def all_off() -> BitMask_uint16_t_16: ...
    @staticmethod
    def lower_on(on_bits: int) -> BitMask_uint16_t_16: ...
    @staticmethod
    def bit(index: int) -> BitMask_uint16_t_16: ...
    @staticmethod
    def range(low_bit: int, size: int) -> BitMask_uint16_t_16: ...
    @staticmethod
    def has_max_num_bits() -> bool: ...
    @staticmethod
    def get_max_num_bits() -> int: ...
    def get_num_bits(self) -> int: ...
    def get_bit(self, index: int) -> bool: ...
    def set_bit(self, index: int) -> None: ...
    def clear_bit(self, index: int) -> None: ...
    def set_bit_to(self, index: int, value: bool) -> None: ...
    def is_zero(self) -> bool: ...
    def is_all_on(self) -> bool: ...
    def extract(self, low_bit: int, size: int) -> int: ...
    def store(self, value: int, low_bit: int, size: int) -> None: ...
    def has_any_of(self, low_bit: int, size: int) -> bool: ...
    def has_all_of(self, low_bit: int, size: int) -> bool: ...
    def set_range(self, low_bit: int, size: int) -> None: ...
    def clear_range(self, low_bit: int, size: int) -> None: ...
    def set_range_to(self, value: bool, low_bit: int, size: int) -> None: ...
    def get_word(self) -> int: ...
    def set_word(self, value: int) -> None: ...
    def get_num_on_bits(self) -> int: ...
    def get_num_off_bits(self) -> int: ...
    def get_lowest_on_bit(self) -> int: ...
    def get_lowest_off_bit(self) -> int: ...
    def get_highest_on_bit(self) -> int: ...
    def get_highest_off_bit(self) -> int: ...
    def get_next_higher_different_bit(self, low_bit: int) -> int: ...
    def invert_in_place(self) -> None: ...
    def has_bits_in_common(self, other: BitMask_uint16_t_16 | int) -> bool: ...
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...
    def output_binary(self, out: ostream, spaces_every: int = ...) -> None: ...
    def output_hex(self, out: ostream, spaces_every: int = ...) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def compare_to(self, other: BitMask_uint16_t_16 | int) -> int: ...
    def flood_down_in_place(self) -> None: ...
    def flood_up_in_place(self) -> None: ...
    def flood_bits_down(self) -> BitMask_uint16_t_16: ...
    def flood_bits_up(self) -> BitMask_uint16_t_16: ...
    @overload
    def keep_next_highest_bit(self, other: BitMask_uint16_t_16 = ...) -> BitMask_uint16_t_16: ...
    @overload
    def keep_next_highest_bit(self, index: int) -> BitMask_uint16_t_16: ...
    @overload
    def keep_next_lowest_bit(self, other: BitMask_uint16_t_16 = ...) -> BitMask_uint16_t_16: ...
    @overload
    def keep_next_lowest_bit(self, index: int) -> BitMask_uint16_t_16: ...
    def get_key(self) -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    allOn = all_on
    allOff = all_off
    lowerOn = lower_on
    hasMaxNumBits = has_max_num_bits
    getMaxNumBits = get_max_num_bits
    getNumBits = get_num_bits
    getBit = get_bit
    setBit = set_bit
    clearBit = clear_bit
    setBitTo = set_bit_to
    isZero = is_zero
    isAllOn = is_all_on
    hasAnyOf = has_any_of
    hasAllOf = has_all_of
    setRange = set_range
    clearRange = clear_range
    setRangeTo = set_range_to
    getWord = get_word
    setWord = set_word
    getNumOnBits = get_num_on_bits
    getNumOffBits = get_num_off_bits
    getLowestOnBit = get_lowest_on_bit
    getLowestOffBit = get_lowest_off_bit
    getHighestOnBit = get_highest_on_bit
    getHighestOffBit = get_highest_off_bit
    getNextHigherDifferentBit = get_next_higher_different_bit
    invertInPlace = invert_in_place
    hasBitsInCommon = has_bits_in_common
    outputBinary = output_binary
    outputHex = output_hex
    compareTo = compare_to
    floodDownInPlace = flood_down_in_place
    floodUpInPlace = flood_up_in_place
    floodBitsDown = flood_bits_down
    floodBitsUp = flood_bits_up
    keepNextHighestBit = keep_next_highest_bit
    keepNextLowestBit = keep_next_lowest_bit
    getKey = get_key
    getClassType = get_class_type

class BitMask_uint32_t_32:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: BitMask_uint32_t_32 = ...) -> None: ...
    @overload
    def __init__(self, init_value: int) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: BitMask_uint32_t_32 | int) -> bool: ...
    def __and__(self, other: BitMask_uint32_t_32 | int) -> BitMask_uint32_t_32: ...
    def __or__(self, other: BitMask_uint32_t_32 | int) -> BitMask_uint32_t_32: ...
    def __xor__(self, other: BitMask_uint32_t_32 | int) -> BitMask_uint32_t_32: ...
    def __invert__(self) -> BitMask_uint32_t_32: ...
    def __lshift__(self, shift: int) -> BitMask_uint32_t_32: ...
    def __rshift__(self, shift: int) -> BitMask_uint32_t_32: ...
    def __iand__(self, other: BitMask_uint32_t_32 | int) -> Self: ...
    def __ior__(self, other: BitMask_uint32_t_32 | int) -> Self: ...
    def __ixor__(self, other: BitMask_uint32_t_32 | int) -> Self: ...
    def __ilshift__(self, shift: int) -> Self: ...
    def __irshift__(self, shift: int) -> Self: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def all_on() -> BitMask_uint32_t_32: ...
    @staticmethod
    def all_off() -> BitMask_uint32_t_32: ...
    @staticmethod
    def lower_on(on_bits: int) -> BitMask_uint32_t_32: ...
    @staticmethod
    def bit(index: int) -> BitMask_uint32_t_32: ...
    @staticmethod
    def range(low_bit: int, size: int) -> BitMask_uint32_t_32: ...
    @staticmethod
    def has_max_num_bits() -> bool: ...
    @staticmethod
    def get_max_num_bits() -> int: ...
    def get_num_bits(self) -> int: ...
    def get_bit(self, index: int) -> bool: ...
    def set_bit(self, index: int) -> None: ...
    def clear_bit(self, index: int) -> None: ...
    def set_bit_to(self, index: int, value: bool) -> None: ...
    def is_zero(self) -> bool: ...
    def is_all_on(self) -> bool: ...
    def extract(self, low_bit: int, size: int) -> int: ...
    def store(self, value: int, low_bit: int, size: int) -> None: ...
    def has_any_of(self, low_bit: int, size: int) -> bool: ...
    def has_all_of(self, low_bit: int, size: int) -> bool: ...
    def set_range(self, low_bit: int, size: int) -> None: ...
    def clear_range(self, low_bit: int, size: int) -> None: ...
    def set_range_to(self, value: bool, low_bit: int, size: int) -> None: ...
    def get_word(self) -> int: ...
    def set_word(self, value: int) -> None: ...
    def get_num_on_bits(self) -> int: ...
    def get_num_off_bits(self) -> int: ...
    def get_lowest_on_bit(self) -> int: ...
    def get_lowest_off_bit(self) -> int: ...
    def get_highest_on_bit(self) -> int: ...
    def get_highest_off_bit(self) -> int: ...
    def get_next_higher_different_bit(self, low_bit: int) -> int: ...
    def invert_in_place(self) -> None: ...
    def has_bits_in_common(self, other: BitMask_uint32_t_32 | int) -> bool: ...
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...
    def output_binary(self, out: ostream, spaces_every: int = ...) -> None: ...
    def output_hex(self, out: ostream, spaces_every: int = ...) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def compare_to(self, other: BitMask_uint32_t_32 | int) -> int: ...
    def flood_down_in_place(self) -> None: ...
    def flood_up_in_place(self) -> None: ...
    def flood_bits_down(self) -> BitMask_uint32_t_32: ...
    def flood_bits_up(self) -> BitMask_uint32_t_32: ...
    @overload
    def keep_next_highest_bit(self, other: BitMask_uint32_t_32 = ...) -> BitMask_uint32_t_32: ...
    @overload
    def keep_next_highest_bit(self, index: int) -> BitMask_uint32_t_32: ...
    @overload
    def keep_next_lowest_bit(self, other: BitMask_uint32_t_32 = ...) -> BitMask_uint32_t_32: ...
    @overload
    def keep_next_lowest_bit(self, index: int) -> BitMask_uint32_t_32: ...
    def get_key(self) -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    allOn = all_on
    allOff = all_off
    lowerOn = lower_on
    hasMaxNumBits = has_max_num_bits
    getMaxNumBits = get_max_num_bits
    getNumBits = get_num_bits
    getBit = get_bit
    setBit = set_bit
    clearBit = clear_bit
    setBitTo = set_bit_to
    isZero = is_zero
    isAllOn = is_all_on
    hasAnyOf = has_any_of
    hasAllOf = has_all_of
    setRange = set_range
    clearRange = clear_range
    setRangeTo = set_range_to
    getWord = get_word
    setWord = set_word
    getNumOnBits = get_num_on_bits
    getNumOffBits = get_num_off_bits
    getLowestOnBit = get_lowest_on_bit
    getLowestOffBit = get_lowest_off_bit
    getHighestOnBit = get_highest_on_bit
    getHighestOffBit = get_highest_off_bit
    getNextHigherDifferentBit = get_next_higher_different_bit
    invertInPlace = invert_in_place
    hasBitsInCommon = has_bits_in_common
    outputBinary = output_binary
    outputHex = output_hex
    compareTo = compare_to
    floodDownInPlace = flood_down_in_place
    floodUpInPlace = flood_up_in_place
    floodBitsDown = flood_bits_down
    floodBitsUp = flood_bits_up
    keepNextHighestBit = keep_next_highest_bit
    keepNextLowestBit = keep_next_lowest_bit
    getKey = get_key
    getClassType = get_class_type

class BitMask_uint64_t_64:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: BitMask_uint64_t_64 = ...) -> None: ...
    @overload
    def __init__(self, init_value: int) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: BitMask_uint64_t_64 | int) -> bool: ...
    def __and__(self, other: BitMask_uint64_t_64 | int) -> BitMask_uint64_t_64: ...
    def __or__(self, other: BitMask_uint64_t_64 | int) -> BitMask_uint64_t_64: ...
    def __xor__(self, other: BitMask_uint64_t_64 | int) -> BitMask_uint64_t_64: ...
    def __invert__(self) -> BitMask_uint64_t_64: ...
    def __lshift__(self, shift: int) -> BitMask_uint64_t_64: ...
    def __rshift__(self, shift: int) -> BitMask_uint64_t_64: ...
    def __iand__(self, other: BitMask_uint64_t_64 | int) -> Self: ...
    def __ior__(self, other: BitMask_uint64_t_64 | int) -> Self: ...
    def __ixor__(self, other: BitMask_uint64_t_64 | int) -> Self: ...
    def __ilshift__(self, shift: int) -> Self: ...
    def __irshift__(self, shift: int) -> Self: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def all_on() -> BitMask_uint64_t_64: ...
    @staticmethod
    def all_off() -> BitMask_uint64_t_64: ...
    @staticmethod
    def lower_on(on_bits: int) -> BitMask_uint64_t_64: ...
    @staticmethod
    def bit(index: int) -> BitMask_uint64_t_64: ...
    @staticmethod
    def range(low_bit: int, size: int) -> BitMask_uint64_t_64: ...
    @staticmethod
    def has_max_num_bits() -> bool: ...
    @staticmethod
    def get_max_num_bits() -> int: ...
    def get_num_bits(self) -> int: ...
    def get_bit(self, index: int) -> bool: ...
    def set_bit(self, index: int) -> None: ...
    def clear_bit(self, index: int) -> None: ...
    def set_bit_to(self, index: int, value: bool) -> None: ...
    def is_zero(self) -> bool: ...
    def is_all_on(self) -> bool: ...
    def extract(self, low_bit: int, size: int) -> int: ...
    def store(self, value: int, low_bit: int, size: int) -> None: ...
    def has_any_of(self, low_bit: int, size: int) -> bool: ...
    def has_all_of(self, low_bit: int, size: int) -> bool: ...
    def set_range(self, low_bit: int, size: int) -> None: ...
    def clear_range(self, low_bit: int, size: int) -> None: ...
    def set_range_to(self, value: bool, low_bit: int, size: int) -> None: ...
    def get_word(self) -> int: ...
    def set_word(self, value: int) -> None: ...
    def get_num_on_bits(self) -> int: ...
    def get_num_off_bits(self) -> int: ...
    def get_lowest_on_bit(self) -> int: ...
    def get_lowest_off_bit(self) -> int: ...
    def get_highest_on_bit(self) -> int: ...
    def get_highest_off_bit(self) -> int: ...
    def get_next_higher_different_bit(self, low_bit: int) -> int: ...
    def invert_in_place(self) -> None: ...
    def has_bits_in_common(self, other: BitMask_uint64_t_64 | int) -> bool: ...
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...
    def output_binary(self, out: ostream, spaces_every: int = ...) -> None: ...
    def output_hex(self, out: ostream, spaces_every: int = ...) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def compare_to(self, other: BitMask_uint64_t_64 | int) -> int: ...
    def flood_down_in_place(self) -> None: ...
    def flood_up_in_place(self) -> None: ...
    def flood_bits_down(self) -> BitMask_uint64_t_64: ...
    def flood_bits_up(self) -> BitMask_uint64_t_64: ...
    @overload
    def keep_next_highest_bit(self, other: BitMask_uint64_t_64 = ...) -> BitMask_uint64_t_64: ...
    @overload
    def keep_next_highest_bit(self, index: int) -> BitMask_uint64_t_64: ...
    @overload
    def keep_next_lowest_bit(self, other: BitMask_uint64_t_64 = ...) -> BitMask_uint64_t_64: ...
    @overload
    def keep_next_lowest_bit(self, index: int) -> BitMask_uint64_t_64: ...
    def get_key(self) -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    allOn = all_on
    allOff = all_off
    lowerOn = lower_on
    hasMaxNumBits = has_max_num_bits
    getMaxNumBits = get_max_num_bits
    getNumBits = get_num_bits
    getBit = get_bit
    setBit = set_bit
    clearBit = clear_bit
    setBitTo = set_bit_to
    isZero = is_zero
    isAllOn = is_all_on
    hasAnyOf = has_any_of
    hasAllOf = has_all_of
    setRange = set_range
    clearRange = clear_range
    setRangeTo = set_range_to
    getWord = get_word
    setWord = set_word
    getNumOnBits = get_num_on_bits
    getNumOffBits = get_num_off_bits
    getLowestOnBit = get_lowest_on_bit
    getLowestOffBit = get_lowest_off_bit
    getHighestOnBit = get_highest_on_bit
    getHighestOffBit = get_highest_off_bit
    getNextHigherDifferentBit = get_next_higher_different_bit
    invertInPlace = invert_in_place
    hasBitsInCommon = has_bits_in_common
    outputBinary = output_binary
    outputHex = output_hex
    compareTo = compare_to
    floodDownInPlace = flood_down_in_place
    floodUpInPlace = flood_up_in_place
    floodBitsDown = flood_bits_down
    floodBitsUp = flood_bits_up
    keepNextHighestBit = keep_next_highest_bit
    keepNextLowestBit = keep_next_lowest_bit
    getKey = get_key
    getClassType = get_class_type

class BitArray:
    """A dynamic array with an unlimited number of bits.

    This is similar to a BitMask, except it appears to contain an infinite
    number of bits.  You can use it very much as you would use a BitMask.
    """

    num_bits_per_word: Final = 64
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, _from: BitArray | SparseArray = ...) -> None: ...
    @overload
    def __init__(self, init_value: int) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: BitArray | SparseArray | int) -> bool: ...
    def __and__(self, other: BitArray | SparseArray | int) -> BitArray: ...
    def __or__(self, other: BitArray | SparseArray | int) -> BitArray: ...
    def __xor__(self, other: BitArray | SparseArray | int) -> BitArray: ...
    def __invert__(self) -> BitArray: ...
    def __lshift__(self, shift: int) -> BitArray: ...
    def __rshift__(self, shift: int) -> BitArray: ...
    def __iand__(self, other: BitArray | SparseArray | int) -> Self: ...
    def __ior__(self, other: BitArray | SparseArray | int) -> Self: ...
    def __ixor__(self, other: BitArray | SparseArray | int) -> Self: ...
    def __ilshift__(self, shift: int) -> Self: ...
    def __irshift__(self, shift: int) -> Self: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def all_on() -> BitArray:
        """Returns a BitArray with an infinite array of bits, all on."""
    @staticmethod
    def all_off() -> BitArray:
        """Returns a BitArray whose bits are all off."""
    @staticmethod
    def lower_on(on_bits: int) -> BitArray:
        """Returns a BitArray whose lower on_bits bits are on."""
    @staticmethod
    def bit(index: int) -> BitArray:
        """Returns a BitArray with only the indicated bit on."""
    @staticmethod
    def range(low_bit: int, size: int) -> BitArray:
        """Returns a BitArray whose size bits, beginning at low_bit, are on."""
    @staticmethod
    def has_max_num_bits() -> bool: ...
    @staticmethod
    def get_max_num_bits() -> int: ...
    @staticmethod
    def get_num_bits_per_word() -> int: ...
    def get_num_bits(self) -> int:
        """Returns the current number of possibly different bits in this array.  There
        are actually an infinite number of bits, but every bit higher than this bit
        will have the same value, either 0 or 1 (see get_highest_bits()).

        This number may grow and/or shrink automatically as needed.
        """
    def get_bit(self, index: int) -> bool:
        """Returns true if the nth bit is set, false if it is cleared.  It is valid
        for n to increase beyond get_num_bits(), but the return value
        get_num_bits() will always be the same.
        """
    def set_bit(self, index: int) -> None:
        """Sets the nth bit on.  If n >= get_num_bits(), this automatically extends
        the array.
        """
    def clear_bit(self, index: int) -> None:
        """Sets the nth bit off.  If n >= get_num_bits(), this automatically extends
        the array.
        """
    def set_bit_to(self, index: int, value: bool) -> None:
        """Sets the nth bit either on or off, according to the indicated bool value."""
    def get_highest_bits(self) -> bool:
        """Returns true if the infinite set of bits beyond get_num_bits() are all on,
        or false of they are all off.
        """
    def is_zero(self) -> bool:
        """Returns true if the entire bitmask is zero, false otherwise."""
    def is_all_on(self) -> bool:
        """Returns true if the entire bitmask is one, false otherwise."""
    def extract(self, low_bit: int, size: int) -> int:
        """Returns a word that represents only the indicated range of bits within this
        BitArray, shifted to the least-significant position.  size must be <=
        get_num_bits_per_word().
        """
    def store(self, value: int, low_bit: int, size: int) -> None:
        """Stores the indicated word into the indicated range of bits with this
        BitArray.
        """
    def has_any_of(self, low_bit: int, size: int) -> bool:
        """Returns true if any bit in the indicated range is set, false otherwise."""
    def has_all_of(self, low_bit: int, size: int) -> bool:
        """Returns true if all bits in the indicated range are set, false otherwise."""
    def set_range(self, low_bit: int, size: int) -> None:
        """Sets the indicated range of bits on."""
    def clear_range(self, low_bit: int, size: int) -> None:
        """Sets the indicated range of bits off."""
    def set_range_to(self, value: bool, low_bit: int, size: int) -> None:
        """Sets the indicated range of bits to either on or off."""
    def get_num_on_bits(self) -> int:
        """Returns the number of bits that are set to 1 in the array.  Returns -1 if
        there are an infinite number of 1 bits.
        """
    def get_num_off_bits(self) -> int:
        """Returns the number of bits that are set to 0 in the array.  Returns -1 if
        there are an infinite number of 0 bits.
        """
    def get_lowest_on_bit(self) -> int:
        """Returns the index of the lowest 1 bit in the array.  Returns -1 if there
        are no 1 bits.
        """
    def get_lowest_off_bit(self) -> int:
        """Returns the index of the lowest 0 bit in the array.  Returns -1 if there
        are no 0 bits.
        """
    def get_highest_on_bit(self) -> int:
        """Returns the index of the highest 1 bit in the array.  Returns -1 if there
        are no 1 bits or if there an infinite number of 1 bits.
        """
    def get_highest_off_bit(self) -> int:
        """Returns the index of the highest 0 bit in the array.  Returns -1 if there
        are no 0 bits or if there an infinite number of 1 bits.
        """
    def get_next_higher_different_bit(self, low_bit: int) -> int:
        """Returns the index of the next bit in the array, above low_bit, whose value
        is different that the value of low_bit.  Returns low_bit again if all bits
        higher than low_bit have the same value.

        This can be used to quickly iterate through all of the bits in the array.
        """
    def get_num_words(self) -> int:
        """Returns the number of possibly-unique words stored in the array."""
    def get_word(self, n: int) -> BitMask_uint32_t_32 | BitMask_uint64_t_64:
        """Returns the nth word in the array.  It is valid for n to be greater than
        get_num_words(), but the return value beyond get_num_words() will always be
        the same.
        """
    def set_word(self, n: int, value: int) -> None:
        """Replaces the nth word in the array.  If n >= get_num_words(), this
        automatically extends the array.
        """
    def invert_in_place(self) -> None:
        """Inverts all the bits in the BitArray.  This is equivalent to array =
        ~array.
        """
    def has_bits_in_common(self, other: BitArray | SparseArray | int) -> bool:
        """Returns true if this BitArray has any "one" bits in common with the other
        one, false otherwise.

        This is equivalent to (array & other) != 0, but may be faster.
        """
    def clear(self) -> None:
        """Sets all the bits in the BitArray off."""
    def output(self, out: ostream) -> None:
        """Writes the BitArray out as a hex number.  For a BitArray, this is always
        the same as output_hex(); it's too confusing for the output format to
        change back and forth at runtime.
        """
    def output_binary(self, out: ostream, spaces_every: int = ...) -> None:
        """Writes the BitArray out as a binary number, with spaces every four bits."""
    def output_hex(self, out: ostream, spaces_every: int = ...) -> None:
        """Writes the BitArray out as a hexadecimal number, with spaces every four
        digits.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes the BitArray out as a binary or a hex number, according to the
        number of bits.
        """
    def compare_to(self, other: BitArray | SparseArray | int) -> int:
        """Returns a number less than zero if this BitArray sorts before the indicated
        other BitArray, greater than zero if it sorts after, or 0 if they are
        equivalent.  This is based on the same ordering defined by operator <.
        """
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    allOn = all_on
    allOff = all_off
    lowerOn = lower_on
    hasMaxNumBits = has_max_num_bits
    getMaxNumBits = get_max_num_bits
    getNumBitsPerWord = get_num_bits_per_word
    getNumBits = get_num_bits
    getBit = get_bit
    setBit = set_bit
    clearBit = clear_bit
    setBitTo = set_bit_to
    getHighestBits = get_highest_bits
    isZero = is_zero
    isAllOn = is_all_on
    hasAnyOf = has_any_of
    hasAllOf = has_all_of
    setRange = set_range
    clearRange = clear_range
    setRangeTo = set_range_to
    getNumOnBits = get_num_on_bits
    getNumOffBits = get_num_off_bits
    getLowestOnBit = get_lowest_on_bit
    getLowestOffBit = get_lowest_off_bit
    getHighestOnBit = get_highest_on_bit
    getHighestOffBit = get_highest_off_bit
    getNextHigherDifferentBit = get_next_higher_different_bit
    getNumWords = get_num_words
    getWord = get_word
    setWord = set_word
    invertInPlace = invert_in_place
    hasBitsInCommon = has_bits_in_common
    outputBinary = output_binary
    outputHex = output_hex
    compareTo = compare_to
    getClassType = get_class_type

@final
class ButtonHandle:
    """A ButtonHandle represents a single button from any device, including
    keyboard buttons and mouse buttons (but see KeyboardButton and
    MouseButton).
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def index(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def ascii_equivalent(self) -> str: ...
    @property
    def alias(self) -> ButtonHandle: ...
    @overload
    def __init__(self, __param0: ButtonHandle = ...) -> None:
        """`(self)`:
        The default constructor must do nothing, because we can't guarantee
        ordering of static initializers.  If the constructor tried to initialize
        its value, it  might happen after the value had already been set
        previously by another static initializer!

        `(self, index: int)`:
        Constructs a ButtonHandle with the corresponding index number, which may
        have been returned by an earlier call to ButtonHandle::get_index().

        `(self, name: str)`:
        Constructs a ButtonHandle with the corresponding name, which is looked up
        in the ButtonRegistry.  This exists for the purpose of being able to
        automatically coerce a string into a ButtonHandle; for most purposes, you
        should use either the static KeyboardButton/MouseButton getters or
        ButtonRegistry::register_button().
        """
    @overload
    def __init__(self, index: int) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: ButtonHandle | str) -> bool: ...
    def __le__(self, other: ButtonHandle | str) -> bool: ...
    def __gt__(self, other: ButtonHandle | str) -> bool: ...
    def __ge__(self, other: ButtonHandle | str) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def compare_to(self, other: ButtonHandle | str) -> int:
        """Sorts ButtonHandles arbitrarily (according to <, >, etc.).  Returns a
        number less than 0 if this type sorts before the other one, greater than
        zero if it sorts after, 0 if they are equivalent.
        """
    def get_hash(self) -> int:
        """Returns a hash code suitable for phash_map."""
    def get_name(self) -> str:
        """Returns the name of the button."""
    def has_ascii_equivalent(self) -> bool:
        """Returns true if the button was created with an ASCII equivalent code (e.g.
        for a standard keyboard button).
        """
    def get_ascii_equivalent(self) -> str:
        """Returns the character code associated with the button, or '\\0' if no ASCII
        code was associated.
        """
    def get_alias(self) -> ButtonHandle:
        """Returns the alias (alternate name) associated with the button, if any, or
        ButtonHandle::none() if the button has no alias.

        Each button is allowed to have one alias, and multiple different buttons
        can refer to the same alias.  The alias should be the more general name for
        the button, for instance, shift is an alias for lshift, but not vice-versa.
        """
    def matches(self, other: ButtonHandle | str) -> bool:
        """Returns true if this ButtonHandle is the same as the other one, or if the
        other one is an alias for this one.  (Does not return true if this button
        is an alias for the other one, however.)

        This is a more general comparison than operator ==.
        """
    def get_index(self) -> int:
        """Returns the integer index associated with this ButtonHandle.  Each
        different ButtonHandle will have a different index.  However, you probably
        shouldn't be using this method; you should just treat the ButtonHandles as
        opaque classes.  This is provided for the convenience of non-C++ scripting
        languages to build a hashtable of ButtonHandles.
        """
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def none() -> ButtonHandle: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    compareTo = compare_to
    getHash = get_hash
    getName = get_name
    hasAsciiEquivalent = has_ascii_equivalent
    getAsciiEquivalent = get_ascii_equivalent
    getAlias = get_alias
    getIndex = get_index
    getClassType = get_class_type

class ButtonRegistry:
    """The ButtonRegistry class maintains all the assigned ButtonHandles in a
    given system.  There should be only one ButtonRegistry class during the
    lifetime of the application.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: ButtonRegistry) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_button(self, name: str) -> ButtonHandle:
        """Finds a ButtonHandle in the registry matching the indicated name.  If there
        is no such ButtonHandle, registers a new one and returns it.
        """
    def find_button(self, name: str) -> ButtonHandle:
        """Finds a ButtonHandle in the registry matching the indicated name.  If there
        is no such ButtonHandle, returns ButtonHandle::none().
        """
    def find_ascii_button(self, ascii_equivalent: str) -> ButtonHandle:
        """Finds a ButtonHandle in the registry matching the indicated ASCII
        equivalent character.  If there is no such ButtonHandle, returns
        ButtonHandle::none().
        """
    def write(self, out: ostream) -> None: ...
    @staticmethod
    def ptr() -> ButtonRegistry:
        """Returns the pointer to the global ButtonRegistry object."""
    getButton = get_button
    findButton = find_button
    findAsciiButton = find_ascii_button

class ButtonMap(TypedReferenceCount):
    """This class represents a map containing all of the buttons of a (keyboard)
    device, though it can also be used as a generic mapping between
    ButtonHandles.  It maps an underlying 'raw' button to a 'virtual' button,
    which may optionally be associated with an appropriate platform-specific
    name for the button.
    """

    def __init__(self, __param0: ButtonMap = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_num_buttons(self) -> int:
        """Returns the number of buttons that this button mapping specifies."""
    def get_raw_button(self, i: int) -> ButtonHandle:
        """Returns the underlying raw button associated with the nth button."""
    @overload
    def get_mapped_button(self, raw: ButtonHandle) -> ButtonHandle:
        """`(self, raw: ButtonHandle)`; `(self, raw_name: str)`:
        Returns the button that the given button is mapped to, or
        ButtonHandle::none() if this map does not specify a mapped button for the
        given raw button.

        `(self, i: int)`:
        Returns the nth mapped button, meaning the button that the nth raw button
        is mapped to.
        """
    @overload
    def get_mapped_button(self, i: int) -> ButtonHandle: ...
    @overload
    def get_mapped_button(self, raw_name: str) -> ButtonHandle: ...
    @overload
    def get_mapped_button_label(self, raw: ButtonHandle) -> str:
        """`(self, raw: ButtonHandle)`; `(self, raw_name: str)`:
        If the button map specifies a special name for the button (eg.  if the
        operating system or keyboard device has a localized name describing the
        key), returns it, or the empty string otherwise.

        Note that this is not the same as get_mapped_button().get_name(), which
        returns the name of the Panda event associated with the button.

        `(self, i: int)`:
        Returns the label associated with the nth mapped button, meaning the button
        that the nth raw button is mapped to.
        """
    @overload
    def get_mapped_button_label(self, i: int) -> str: ...
    @overload
    def get_mapped_button_label(self, raw_name: str) -> str: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    getNumButtons = get_num_buttons
    getRawButton = get_raw_button
    getMappedButton = get_mapped_button
    getMappedButtonLabel = get_mapped_button_label

class CallbackObject(TypedReferenceCount):
    """This is a generic object that can be assigned to a callback at various
    points in the rendering process.  This is actually a base class for a
    handful of specialized callback object types.  You can also subclass it
    yourself to make your own callback handler.
    """

    def __init__(self, __param0: Callable | CallbackObject) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def make(function: Callable) -> PythonCallbackObject: ...

class CachedTypedWritableReferenceCount(TypedWritableReferenceCount):
    """This is a special extension to ReferenceCount that includes dual reference
    counts: the standard reference count number, which includes all references
    to the object, and a separate number (the cache reference count) that
    counts the number of references to the object just within its cache alone.
    When get_ref_count() == get_cache_ref_count(), the object is not referenced
    outside the cache.

    The cache refs must be explicitly maintained; there is no PointerTo<> class
    to maintain the cache reference counts automatically.  The cache reference
    count is automatically included in the overall reference count: calling
    cache_ref() and cache_unref() automatically calls ref() and unref().
    """

    @property
    def cache_ref_count(self) -> int: ...
    def get_cache_ref_count(self) -> int:
        """Returns the current reference count."""
    def cache_ref(self) -> None:
        """Explicitly increments the cache reference count and the normal reference
        count simultaneously.
        """
    def cache_unref(self) -> bool:
        """Explicitly decrements the cache reference count and the normal reference
        count simultaneously.

        The return value is true if the new reference count is nonzero, false if it
        is zero.
        """
    def test_ref_count_integrity(self) -> bool:
        """Does some easy checks to make sure that the reference count isn't
        completely bogus.
        """
    getCacheRefCount = get_cache_ref_count
    cacheRef = cache_ref
    cacheUnref = cache_unref
    testRefCountIntegrity = test_ref_count_integrity

class CallbackData(TypedObject):
    """This is a generic data block that is passed along to a CallbackObject when
    a callback is made.  It contains data specific to the particular callback
    type in question.

    This is actually an abstract base class and contains no data.
    Specializations of this class will contain the actual data relevant to each
    callback type.
    """

    def output(self, out: ostream) -> None: ...
    def upcall(self) -> None:
        """You should make this call during the callback if you want to continue the
        normal function that would have been done in the absence of a callback.
        """

class PythonCallbackObject(CallbackObject):
    """This is a specialization on CallbackObject to allow a callback to directly
    call an arbitrary Python function.  Powerful!  But use with caution.
    """

    function: Callable
    @overload
    def __init__(self, function: Callable = ...) -> None: ...
    @overload
    def __init__(self, __param0: PythonCallbackObject) -> None: ...
    def set_function(self, function: Callable) -> None:
        """Replaces the function that is called for the callback.  runs.  The
        parameter should be a Python callable object.
        """
    def get_function(self) -> Callable:
        """Returns the function that is called for the callback."""
    setFunction = set_function
    getFunction = get_function

class TimeVal:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: TimeVal = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_sec(self) -> int: ...
    def get_usec(self) -> int: ...
    getSec = get_sec
    getUsec = get_usec

class ClockObject(ReferenceCount):
    """A ClockObject keeps track of elapsed real time and discrete time.  In
    normal mode, get_frame_time() returns the time as of the last time tick()
    was called.  This is the "discrete" time, and is usually used to get the
    time as of, for instance, the beginning of the current frame.

    In other modes, as set by set_mode() or the clock-mode config variable,
    get_frame_time() may return other values to simulate different timing
    effects, for instance to perform non-real-time animation.  See set_mode().

    In all modes, get_real_time() always returns the elapsed real time in
    seconds since the ClockObject was constructed, or since it was last reset.

    You can create your own ClockObject whenever you want to have your own
    local timer.  There is also a default, global ClockObject intended to
    represent global time for the application; this is normally set up to tick
    every frame so that its get_frame_time() will return the time for the
    current frame.
    """

    M_normal: Final = 0
    MNormal: Final = 0
    M_non_real_time: Final = 1
    MNonRealTime: Final = 1
    M_forced: Final = 2
    MForced: Final = 2
    M_degrade: Final = 3
    MDegrade: Final = 3
    M_slave: Final = 4
    MSlave: Final = 4
    M_limited: Final = 5
    MLimited: Final = 5
    M_integer: Final = 6
    MInteger: Final = 6
    M_integer_limited: Final = 7
    MIntegerLimited: Final = 7
    mode: _ClockObject_Mode
    frame_time: float
    real_time: float
    frame_count: int
    dt: float
    max_dt: float
    degrade_factor: float
    average_frame_rate_interval: float
    @property
    def long_time(self) -> float: ...
    @property
    def average_frame_rate(self) -> float: ...
    @property
    def max_frame_duration(self) -> float: ...
    @overload
    def __init__(self, mode: _ClockObject_Mode = ...) -> None: ...
    @overload
    def __init__(self, copy: ClockObject) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_mode(self, mode: _ClockObject_Mode) -> None:
        """Changes the mode of the clock.  Normally, the clock is in mode M_normal.
        In this mode, each call to tick() will set the value returned by
        get_frame_time() to the current real time; thus, the clock simply reports
        time advancing.

        Other possible modes:

        M_non_real_time - the clock ignores real time completely; at each call to
        tick(), it pretends that exactly dt seconds have elapsed since the last
        call to tick().  You may set the value of dt with set_dt() or
        set_frame_rate().

        M_limited - the clock will run as fast as it can, as in M_normal, but will
        not run faster than the rate specified by set_frame_rate().  If the
        application would run faster than this rate, the clock will slow down the
        application.

        M_integer - the clock will run as fast as it can, but the rate will be
        constrained to be an integer multiple or divisor of the rate specified by
        set_frame_rate().  The clock will slow down the application a bit to
        guarantee this.

        M_integer_limited - a combination of M_limited and M_integer; the clock
        will not run faster than set_frame_rate(), and if it runs slower, it will
        run at a integer divisor of that rate.

        M_forced - the clock forces the application to run at the rate specified by
        set_frame_rate().  If the application would run faster than this rate, the
        clock will slow down the application; if the application would run slower
        than this rate, the clock slows down time so that the application believes
        it is running at the given rate.

        M_degrade - the clock runs at real time, but the application is slowed down
        by a set factor of its frame rate, specified by set_degrade_factor().

        M_slave - the clock does not advance, but relies on the user to call
        set_frame_time() and/or set_frame_count() each frame.
        """
    def get_mode(self) -> _ClockObject_Mode:
        """Returns the current mode of the clock.  See set_mode()."""
    def get_frame_time(self, current_thread: Thread = ...) -> float:
        """Returns the time in seconds as of the last time tick() was called
        (typically, this will be as of the start of the current frame).

        This is generally the kind of time you want to ask for in most rendering
        and animation contexts, since it's important that all of the animation for
        a given frame remains in sync with each other.
        """
    def get_real_time(self) -> float:
        """Returns the actual number of seconds elapsed since the ClockObject was
        created, or since it was last reset.  This is useful for doing real timing
        measurements, e.g.  for performance statistics.

        This returns the most precise timer we have for short time intervals, but
        it may tend to drift over the long haul.  If more accurate timekeeping is
        needed over a long period of time, use get_long_time() instead.
        """
    def get_long_time(self) -> float:
        """Returns the actual number of seconds elapsed since the ClockObject was
        created, or since it was last reset.

        This is similar to get_real_time(), except that it uses the most accurate
        counter we have over a long period of time, and so it is less likely to
        drift.  However, it may not be very precise for measuring short intervals.
        On Windows, for instace, this is only accurate to within about 55
        milliseconds.
        """
    def reset(self) -> None:
        """Simultaneously resets both the time and the frame count to zero."""
    def set_real_time(self, time: float) -> None:
        """Resets the clock to the indicated time.  This changes only the real time of
        the clock as reported by get_real_time(), but does not immediately change
        the time reported by get_frame_time()--that will change after the next call
        to tick().  Also see reset(), set_frame_time(), and set_frame_count().
        """
    def set_frame_time(self, time: float, current_thread: Thread = ...) -> None:
        """Changes the time as reported for the current frame to the indicated time.
        Normally, the way to adjust the frame time is via tick(); this function is
        provided only for occasional special adjustments.
        """
    def set_frame_count(self, frame_count: int, current_thread: Thread = ...) -> None:
        """Resets the number of frames counted to the indicated number.  Also see
        reset(), set_real_time(), and set_frame_time().
        """
    def get_frame_count(self, current_thread: Thread = ...) -> int:
        """Returns the number of times tick() has been called since the ClockObject
        was created, or since it was last reset.  This is generally the number of
        frames that have been rendered.
        """
    def get_net_frame_rate(self, current_thread: Thread = ...) -> float:
        """Returns the average frame rate since the last reset.  This is simply the
        total number of frames divided by the total elapsed time.  This reports the
        virtual frame rate if the clock is in (or has been in) M_non_real_time
        mode.
        """
    def get_dt(self, current_thread: Thread = ...) -> float:
        """Returns the elapsed time for the previous frame: the number of seconds
        elapsed between the last two calls to tick().
        """
    def set_dt(self, dt: float) -> None:
        """In non-real-time mode, sets the number of seconds that should appear to
        elapse between frames.  In forced mode or limited mode, sets our target dt.
        In normal mode, this has no effect.

        Also see set_frame_rate(), which is a different way to specify the same
        quantity.
        """
    def set_frame_rate(self, frame_rate: float) -> None:
        """In non-real-time mode, sets the number of frames per second that we should
        appear to be running.  In forced mode or limited mode, sets our target
        frame rate.  In normal mode, this has no effect.

        Also see set_dt(), which is a different way to specify the same quantity.
        """
    def get_max_dt(self) -> float:
        """Returns the current maximum allowable time elapsed between any two frames.
        See set_max_dt().
        """
    def set_max_dt(self, max_dt: float) -> None:
        """Sets a limit on the value returned by get_dt().  If this value is less than
        zero, no limit is imposed; otherwise, this is the maximum value that will
        ever be returned by get_dt(), regardless of how much time has actually
        elapsed between frames.

        This limit is only imposed in real-time mode; in non-real-time mode, the dt
        is fixed anyway and max_dt is ignored.

        This is generally used to guarantee reasonable behavior even in the
        presence of a very slow or chuggy frame rame.
        """
    def get_degrade_factor(self) -> float:
        """In degrade mode, returns the ratio by which the performance is degraded.  A
        value of 2.0 causes the clock to be slowed down by a factor of two
        (reducing performance to 1/2 what would be otherwise).

        This has no effect if mode is not M_degrade.
        """
    def set_degrade_factor(self, degrade_factor: float) -> None:
        """In degrade mode, sets the ratio by which the performance is degraded.  A
        value of 2.0 causes the clock to be slowed down by a factor of two
        (reducing performance to 1/2 what would be otherwise).

        This has no effect if mode is not M_degrade.
        """
    def set_average_frame_rate_interval(self, time: float) -> None:
        """Specifies the interval of time (in seconds) over which
        get_average_frame_rate() averages the number of frames per second to
        compute the frame rate.  Changing this does not necessarily immediately
        change the result of get_average_frame_rate(), until this interval of time
        has elapsed again.

        Setting this to zero disables the computation of get_average_frame_rate().
        """
    def get_average_frame_rate_interval(self) -> float:
        """Returns the interval of time (in seconds) over which
        get_average_frame_rate() averages the number of frames per second to
        compute the frame rate.
        """
    def get_average_frame_rate(self, current_thread: Thread = ...) -> float:
        """Returns the average frame rate in number of frames per second over the last
        get_average_frame_rate_interval() seconds.  This measures the virtual frame
        rate if the clock is in M_non_real_time mode.
        """
    def get_max_frame_duration(self, current_thread: Thread = ...) -> float:
        """Returns the maximum frame duration over the last
        get_average_frame_rate_interval() seconds.
        """
    def calc_frame_rate_deviation(self, current_thread: Thread = ...) -> float:
        """Returns the standard deviation of the frame times of the frames rendered
        over the past get_average_frame_rate_interval() seconds.  This number gives
        an estimate of the chugginess of the frame rate; if it is large, there is a
        large variation in the frame rate; if is small, all of the frames are
        consistent in length.

        A large value might also represent just a recent change in frame rate, for
        instance, because the camera has just rotated from looking at a simple
        scene to looking at a more complex scene.
        """
    def tick(self, current_thread: Thread = ...) -> None:
        """Instructs the clock that a new frame has just begun.  In normal, real-time
        mode, get_frame_time() will henceforth report the time as of this instant
        as the current start-of-frame time.  In non-real-time mode,
        get_frame_time() will be incremented by the value of dt.
        """
    def sync_frame_time(self, current_thread: Thread = ...) -> None:
        """Resets the frame time to the current real time.  This is similar to tick(),
        except that it does not advance the frame counter and does not affect dt.
        This is intended to be used in the middle of a particularly long frame to
        compensate for the time that has already elapsed.

        In non-real-time mode, this function has no effect (because in this mode
        all frames take the same length of time).
        """
    def check_errors(self, current_thread: Thread) -> bool:
        """Returns true if a clock error was detected since the last time
        check_errors() was called.  A clock error means that something happened, an
        OS or BIOS bug, for instance, that makes the current value of the clock
        somewhat suspect, and an application may wish to resynchronize with any
        external clocks.
        """
    @staticmethod
    def get_global_clock() -> ClockObject:
        """Returns a pointer to the global ClockObject.  This is the ClockObject that
        most code should use for handling scene graph rendering and animation.
        """
    setMode = set_mode
    getMode = get_mode
    getFrameTime = get_frame_time
    getRealTime = get_real_time
    getLongTime = get_long_time
    setRealTime = set_real_time
    setFrameTime = set_frame_time
    setFrameCount = set_frame_count
    getFrameCount = get_frame_count
    getNetFrameRate = get_net_frame_rate
    getDt = get_dt
    setDt = set_dt
    setFrameRate = set_frame_rate
    getMaxDt = get_max_dt
    setMaxDt = set_max_dt
    getDegradeFactor = get_degrade_factor
    setDegradeFactor = set_degrade_factor
    setAverageFrameRateInterval = set_average_frame_rate_interval
    getAverageFrameRateInterval = get_average_frame_rate_interval
    getAverageFrameRate = get_average_frame_rate
    getMaxFrameDuration = get_max_frame_duration
    calcFrameRateDeviation = calc_frame_rate_deviation
    syncFrameTime = sync_frame_time
    checkErrors = check_errors
    getGlobalClock = get_global_clock

class CopyOnWriteObject(CachedTypedWritableReferenceCount):
    """This base class provides basic reference counting, but also can be used
    with a CopyOnWritePointer to provide get_read_pointer() and
    get_write_pointer().
    """

    def cache_ref(self) -> None:
        """@see CachedTypedWritableReferenceCount::cache_ref()"""
    def cache_unref(self) -> bool:
        """@see CachedTypedWritableReferenceCount::cache_unref()"""
    cacheRef = cache_ref
    cacheUnref = cache_unref

class DatagramBuffer(DatagramSink, DatagramGenerator):  # type: ignore[misc]
    """This class can be used to write a series of datagrams into a memory buffer.
    It acts as both a datagram sink and generator; you can fill it up with
    datagrams and then read as many datagrams from it.

    This uses the same format as DatagramInputFile and DatagramOutputFile,
    meaning that Datagram sizes are always stored little-endian.
    """

    data: bytes
    def __init__(self, data: bytes = ...) -> None:
        """`(self)`:
        Initializes an empty datagram buffer.

        `(self, data: bytes)`:
        Initializes the buffer with the given data.
        """
    def upcast_to_DatagramSink(self) -> DatagramSink: ...
    def upcast_to_DatagramGenerator(self) -> DatagramGenerator: ...
    def clear(self) -> None:
        """Clears the internal buffer."""
    upcastToDatagramSink = upcast_to_DatagramSink
    upcastToDatagramGenerator = upcast_to_DatagramGenerator

class DatagramInputFile(DatagramGenerator):
    """This class can be used to read a binary file that consists of an arbitrary
    header followed by a number of datagrams.
    """

    def __init__(self) -> None: ...
    @overload
    def open(self, file: ConfigVariableFilename | FileReference) -> bool:
        """`(self, file: FileReference)`; `(self, filename: Filename)`:
        Opens the indicated filename for reading.  Returns true on success, false
        on failure.

        `(self, _in: istream, filename: Filename = ...)`:
        Starts reading from the indicated stream.  Returns true on success, false
        on failure.  The DatagramInputFile does not take ownership of the stream;
        you are responsible for closing or deleting it when you are done.
        """
    @overload
    def open(self, filename: StrOrBytesPath) -> bool: ...
    @overload
    def open(self, _in: istream, filename: StrOrBytesPath = ...) -> bool: ...
    def get_stream(self) -> istream:
        """Returns the istream represented by the input file."""
    def close(self) -> None:
        """Closes the file.  This is also implicitly done when the DatagramInputFile
        destructs.
        """
    getStream = get_stream

class DatagramOutputFile(DatagramSink):
    """This class can be used to write a binary file that consists of an arbitrary
    header followed by a number of datagrams.
    """

    @property
    def stream(self) -> ostream: ...
    def __init__(self) -> None: ...
    @overload
    def open(self, file: ConfigVariableFilename | FileReference) -> bool:
        """`(self, file: FileReference)`:
        Opens the indicated filename for writing.  Returns true if successful,
        false on failure.

        `(self, filename: Filename)`:
        Opens the indicated filename for writing.  Returns true on success, false
        on failure.

        `(self, out: ostream, filename: Filename = ...)`:
        Starts writing to the indicated stream.  Returns true on success, false on
        failure.  The DatagramOutputFile does not take ownership of the stream; you
        are responsible for closing or deleting it when you are done.
        """
    @overload
    def open(self, filename: StrOrBytesPath) -> bool: ...
    @overload
    def open(self, out: ostream, filename: StrOrBytesPath = ...) -> bool: ...
    def close(self) -> None:
        """Closes the file.  This is also implicitly done when the DatagramOutputFile
        destructs.
        """
    def write_header(self, header: str) -> bool:
        """Writes a sequence of bytes to the beginning of the datagram file.  This may
        be called any number of times after the file has been opened and before the
        first datagram is written.  It may not be called once the first datagram is
        written.
        """
    writeHeader = write_header

class DoubleBitMask_BitMaskNative:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: DoubleBitMask_BitMaskNative = ...) -> None: ...
    @overload
    def __init__(self, init_value) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: DoubleBitMask_BitMaskNative) -> bool: ...
    def __and__(self, other: DoubleBitMask_BitMaskNative) -> DoubleBitMask_BitMaskNative: ...
    def __or__(self, other: DoubleBitMask_BitMaskNative) -> DoubleBitMask_BitMaskNative: ...
    def __xor__(self, other: DoubleBitMask_BitMaskNative) -> DoubleBitMask_BitMaskNative: ...
    def __invert__(self) -> DoubleBitMask_BitMaskNative: ...
    def __lshift__(self, shift: int) -> DoubleBitMask_BitMaskNative: ...
    def __rshift__(self, shift: int) -> DoubleBitMask_BitMaskNative: ...
    def __iand__(self, other: DoubleBitMask_BitMaskNative) -> Self: ...
    def __ior__(self, other: DoubleBitMask_BitMaskNative) -> Self: ...
    def __ixor__(self, other: DoubleBitMask_BitMaskNative) -> Self: ...
    def __ilshift__(self, shift: int) -> Self: ...
    def __irshift__(self, shift: int) -> Self: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def all_on() -> DoubleBitMask_BitMaskNative: ...
    @staticmethod
    def all_off() -> DoubleBitMask_BitMaskNative: ...
    @staticmethod
    def lower_on(on_bits: int) -> DoubleBitMask_BitMaskNative: ...
    @staticmethod
    def bit(index: int) -> DoubleBitMask_BitMaskNative: ...
    @staticmethod
    def range(low_bit: int, size: int) -> DoubleBitMask_BitMaskNative: ...
    @staticmethod
    def has_max_num_bits() -> bool: ...
    @staticmethod
    def get_max_num_bits() -> int: ...
    def get_num_bits(self) -> int: ...
    def get_bit(self, index: int) -> bool: ...
    def set_bit(self, index: int) -> None: ...
    def clear_bit(self, index: int) -> None: ...
    def set_bit_to(self, index: int, value: bool) -> None: ...
    def is_zero(self) -> bool: ...
    def is_all_on(self) -> bool: ...
    def extract(self, low_bit: int, size: int) -> int: ...
    def store(self, value: int, low_bit: int, size: int) -> None: ...
    def has_any_of(self, low_bit: int, size: int) -> bool: ...
    def has_all_of(self, low_bit: int, size: int) -> bool: ...
    def set_range(self, low_bit: int, size: int) -> None: ...
    def clear_range(self, low_bit: int, size: int) -> None: ...
    def set_range_to(self, value: bool, low_bit: int, size: int) -> None: ...
    def get_num_on_bits(self) -> int: ...
    def get_num_off_bits(self) -> int: ...
    def get_lowest_on_bit(self) -> int: ...
    def get_lowest_off_bit(self) -> int: ...
    def get_highest_on_bit(self) -> int: ...
    def get_highest_off_bit(self) -> int: ...
    def get_next_higher_different_bit(self, low_bit: int) -> int: ...
    def invert_in_place(self) -> None: ...
    def has_bits_in_common(self, other: DoubleBitMask_BitMaskNative) -> bool: ...
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...
    def output_binary(self, out: ostream, spaces_every: int = ...) -> None: ...
    def output_hex(self, out: ostream, spaces_every: int = ...) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def compare_to(self, other: DoubleBitMask_BitMaskNative) -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    allOn = all_on
    allOff = all_off
    lowerOn = lower_on
    hasMaxNumBits = has_max_num_bits
    getMaxNumBits = get_max_num_bits
    getNumBits = get_num_bits
    getBit = get_bit
    setBit = set_bit
    clearBit = clear_bit
    setBitTo = set_bit_to
    isZero = is_zero
    isAllOn = is_all_on
    hasAnyOf = has_any_of
    hasAllOf = has_all_of
    setRange = set_range
    clearRange = clear_range
    setRangeTo = set_range_to
    getNumOnBits = get_num_on_bits
    getNumOffBits = get_num_off_bits
    getLowestOnBit = get_lowest_on_bit
    getLowestOffBit = get_lowest_off_bit
    getHighestOnBit = get_highest_on_bit
    getHighestOffBit = get_highest_off_bit
    getNextHigherDifferentBit = get_next_higher_different_bit
    invertInPlace = invert_in_place
    hasBitsInCommon = has_bits_in_common
    outputBinary = output_binary
    outputHex = output_hex
    compareTo = compare_to
    getClassType = get_class_type

class DoubleBitMask_DoubleBitMaskNative:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: DoubleBitMask_DoubleBitMaskNative = ...) -> None: ...
    @overload
    def __init__(self, init_value) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: DoubleBitMask_DoubleBitMaskNative) -> bool: ...
    def __and__(self, other: DoubleBitMask_DoubleBitMaskNative) -> DoubleBitMask_DoubleBitMaskNative: ...
    def __or__(self, other: DoubleBitMask_DoubleBitMaskNative) -> DoubleBitMask_DoubleBitMaskNative: ...
    def __xor__(self, other: DoubleBitMask_DoubleBitMaskNative) -> DoubleBitMask_DoubleBitMaskNative: ...
    def __invert__(self) -> DoubleBitMask_DoubleBitMaskNative: ...
    def __lshift__(self, shift: int) -> DoubleBitMask_DoubleBitMaskNative: ...
    def __rshift__(self, shift: int) -> DoubleBitMask_DoubleBitMaskNative: ...
    def __iand__(self, other: DoubleBitMask_DoubleBitMaskNative) -> Self: ...
    def __ior__(self, other: DoubleBitMask_DoubleBitMaskNative) -> Self: ...
    def __ixor__(self, other: DoubleBitMask_DoubleBitMaskNative) -> Self: ...
    def __ilshift__(self, shift: int) -> Self: ...
    def __irshift__(self, shift: int) -> Self: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def all_on() -> DoubleBitMask_DoubleBitMaskNative: ...
    @staticmethod
    def all_off() -> DoubleBitMask_DoubleBitMaskNative: ...
    @staticmethod
    def lower_on(on_bits: int) -> DoubleBitMask_DoubleBitMaskNative: ...
    @staticmethod
    def bit(index: int) -> DoubleBitMask_DoubleBitMaskNative: ...
    @staticmethod
    def range(low_bit: int, size: int) -> DoubleBitMask_DoubleBitMaskNative: ...
    @staticmethod
    def has_max_num_bits() -> bool: ...
    @staticmethod
    def get_max_num_bits() -> int: ...
    def get_num_bits(self) -> int: ...
    def get_bit(self, index: int) -> bool: ...
    def set_bit(self, index: int) -> None: ...
    def clear_bit(self, index: int) -> None: ...
    def set_bit_to(self, index: int, value: bool) -> None: ...
    def is_zero(self) -> bool: ...
    def is_all_on(self) -> bool: ...
    def extract(self, low_bit: int, size: int) -> int: ...
    def store(self, value: int, low_bit: int, size: int) -> None: ...
    def has_any_of(self, low_bit: int, size: int) -> bool: ...
    def has_all_of(self, low_bit: int, size: int) -> bool: ...
    def set_range(self, low_bit: int, size: int) -> None: ...
    def clear_range(self, low_bit: int, size: int) -> None: ...
    def set_range_to(self, value: bool, low_bit: int, size: int) -> None: ...
    def get_num_on_bits(self) -> int: ...
    def get_num_off_bits(self) -> int: ...
    def get_lowest_on_bit(self) -> int: ...
    def get_lowest_off_bit(self) -> int: ...
    def get_highest_on_bit(self) -> int: ...
    def get_highest_off_bit(self) -> int: ...
    def get_next_higher_different_bit(self, low_bit: int) -> int: ...
    def invert_in_place(self) -> None: ...
    def has_bits_in_common(self, other: DoubleBitMask_DoubleBitMaskNative) -> bool: ...
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...
    def output_binary(self, out: ostream, spaces_every: int = ...) -> None: ...
    def output_hex(self, out: ostream, spaces_every: int = ...) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def compare_to(self, other: DoubleBitMask_DoubleBitMaskNative) -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    allOn = all_on
    allOff = all_off
    lowerOn = lower_on
    hasMaxNumBits = has_max_num_bits
    getMaxNumBits = get_max_num_bits
    getNumBits = get_num_bits
    getBit = get_bit
    setBit = set_bit
    clearBit = clear_bit
    setBitTo = set_bit_to
    isZero = is_zero
    isAllOn = is_all_on
    hasAnyOf = has_any_of
    hasAllOf = has_all_of
    setRange = set_range
    clearRange = clear_range
    setRangeTo = set_range_to
    getNumOnBits = get_num_on_bits
    getNumOffBits = get_num_off_bits
    getLowestOnBit = get_lowest_on_bit
    getLowestOffBit = get_lowest_off_bit
    getHighestOnBit = get_highest_on_bit
    getHighestOffBit = get_highest_off_bit
    getNextHigherDifferentBit = get_next_higher_different_bit
    invertInPlace = invert_in_place
    hasBitsInCommon = has_bits_in_common
    outputBinary = output_binary
    outputHex = output_hex
    compareTo = compare_to
    getClassType = get_class_type

class GamepadButton:
    """This class is just used as a convenient namespace for grouping all of these
    handy functions that return buttons which map to gamepad buttons.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: GamepadButton = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def lstick() -> ButtonHandle: ...
    @staticmethod
    def rstick() -> ButtonHandle: ...
    @staticmethod
    def lshoulder() -> ButtonHandle: ...
    @staticmethod
    def rshoulder() -> ButtonHandle: ...
    @staticmethod
    def ltrigger() -> ButtonHandle: ...
    @staticmethod
    def rtrigger() -> ButtonHandle: ...
    @staticmethod
    def lgrip() -> ButtonHandle: ...
    @staticmethod
    def rgrip() -> ButtonHandle: ...
    @staticmethod
    def dpad_left() -> ButtonHandle: ...
    @staticmethod
    def dpad_right() -> ButtonHandle: ...
    @staticmethod
    def dpad_up() -> ButtonHandle: ...
    @staticmethod
    def dpad_down() -> ButtonHandle: ...
    @staticmethod
    def back() -> ButtonHandle: ...
    @staticmethod
    def guide() -> ButtonHandle: ...
    @staticmethod
    def start() -> ButtonHandle: ...
    @staticmethod
    def next() -> ButtonHandle: ...
    @staticmethod
    def previous() -> ButtonHandle: ...
    @staticmethod
    def face_a() -> ButtonHandle: ...
    @staticmethod
    def face_b() -> ButtonHandle: ...
    @staticmethod
    def face_c() -> ButtonHandle: ...
    @staticmethod
    def face_x() -> ButtonHandle: ...
    @staticmethod
    def face_y() -> ButtonHandle: ...
    @staticmethod
    def face_z() -> ButtonHandle: ...
    @staticmethod
    def face_1() -> ButtonHandle: ...
    @staticmethod
    def face_2() -> ButtonHandle: ...
    @staticmethod
    def trigger() -> ButtonHandle:
        """Flight stick buttons, takes zero-based index.  First is always trigger."""
    @staticmethod
    def joystick(button_number: int) -> ButtonHandle:
        """Returns the ButtonHandle associated with the particular numbered joystick
        button (zero-based), if there is one, or ButtonHandle::none() if there is
        not.
        """
    @staticmethod
    def hat_up() -> ButtonHandle: ...
    @staticmethod
    def hat_down() -> ButtonHandle: ...
    @staticmethod
    def hat_left() -> ButtonHandle: ...
    @staticmethod
    def hat_right() -> ButtonHandle: ...
    dpadLeft = dpad_left
    dpadRight = dpad_right
    dpadUp = dpad_up
    dpadDown = dpad_down
    faceA = face_a
    faceB = face_b
    faceC = face_c
    faceX = face_x
    faceY = face_y
    faceZ = face_z
    face1 = face_1
    face2 = face_2
    hatUp = hat_up
    hatDown = hat_down
    hatLeft = hat_left
    hatRight = hat_right

class KeyboardButton:
    """This class is just used as a convenient namespace for grouping all of these
    handy functions that return buttons which map to standard keyboard keys.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: KeyboardButton = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def ascii_key(ascii_equivalent: str) -> ButtonHandle:
        """Returns the ButtonHandle associated with the particular ASCII character, if
        there is one, or ButtonHandle::none() if there is not.
        """
    @staticmethod
    def space() -> ButtonHandle: ...
    @staticmethod
    def backspace() -> ButtonHandle: ...
    @staticmethod
    def tab() -> ButtonHandle: ...
    @staticmethod
    def enter() -> ButtonHandle: ...
    @staticmethod
    def escape() -> ButtonHandle: ...
    @staticmethod
    def f1() -> ButtonHandle: ...
    @staticmethod
    def f2() -> ButtonHandle: ...
    @staticmethod
    def f3() -> ButtonHandle: ...
    @staticmethod
    def f4() -> ButtonHandle: ...
    @staticmethod
    def f5() -> ButtonHandle: ...
    @staticmethod
    def f6() -> ButtonHandle: ...
    @staticmethod
    def f7() -> ButtonHandle: ...
    @staticmethod
    def f8() -> ButtonHandle: ...
    @staticmethod
    def f9() -> ButtonHandle: ...
    @staticmethod
    def f10() -> ButtonHandle: ...
    @staticmethod
    def f11() -> ButtonHandle: ...
    @staticmethod
    def f12() -> ButtonHandle: ...
    @staticmethod
    def f13() -> ButtonHandle:
        """PC keyboards don't have these four buttons, but Macs do."""
    @staticmethod
    def f14() -> ButtonHandle: ...
    @staticmethod
    def f15() -> ButtonHandle: ...
    @staticmethod
    def f16() -> ButtonHandle: ...
    @staticmethod
    def left() -> ButtonHandle: ...
    @staticmethod
    def right() -> ButtonHandle: ...
    @staticmethod
    def up() -> ButtonHandle: ...
    @staticmethod
    def down() -> ButtonHandle: ...
    @staticmethod
    def page_up() -> ButtonHandle: ...
    @staticmethod
    def page_down() -> ButtonHandle: ...
    @staticmethod
    def home() -> ButtonHandle: ...
    @staticmethod
    def end() -> ButtonHandle: ...
    @staticmethod
    def insert() -> ButtonHandle: ...
    @staticmethod
    def _del() -> ButtonHandle:
        """delete is a C++ keyword."""
    @staticmethod
    def help() -> ButtonHandle:
        """delete is a C++ keyword."""
    @staticmethod
    def menu() -> ButtonHandle: ...
    @staticmethod
    def shift() -> ButtonHandle: ...
    @staticmethod
    def control() -> ButtonHandle: ...
    @staticmethod
    def alt() -> ButtonHandle: ...
    @staticmethod
    def meta() -> ButtonHandle: ...
    @staticmethod
    def caps_lock() -> ButtonHandle: ...
    @staticmethod
    def shift_lock() -> ButtonHandle: ...
    @staticmethod
    def num_lock() -> ButtonHandle: ...
    @staticmethod
    def scroll_lock() -> ButtonHandle: ...
    @staticmethod
    def print_screen() -> ButtonHandle: ...
    @staticmethod
    def pause() -> ButtonHandle: ...
    @staticmethod
    def lshift() -> ButtonHandle: ...
    @staticmethod
    def rshift() -> ButtonHandle: ...
    @staticmethod
    def lcontrol() -> ButtonHandle: ...
    @staticmethod
    def rcontrol() -> ButtonHandle: ...
    @staticmethod
    def lalt() -> ButtonHandle: ...
    @staticmethod
    def ralt() -> ButtonHandle: ...
    @staticmethod
    def lmeta() -> ButtonHandle: ...
    @staticmethod
    def rmeta() -> ButtonHandle: ...
    asciiKey = ascii_key
    pageUp = page_up
    pageDown = page_down
    capsLock = caps_lock
    shiftLock = shift_lock
    numLock = num_lock
    scrollLock = scroll_lock
    printScreen = print_screen

class ModifierButtons:
    """This class monitors the state of a number of individual buttons and tracks
    whether each button is known to be down or up.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def buttons(self) -> Sequence[ButtonHandle]: ...
    def __init__(self, copy: ModifierButtons = ...) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: ModifierButtons) -> bool: ...
    def __and__(self, other: ModifierButtons) -> ModifierButtons: ...
    def __or__(self, other: ModifierButtons) -> ModifierButtons: ...
    def __iand__(self, other: ModifierButtons) -> Self: ...
    def __ior__(self, other: ModifierButtons) -> Self: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def set_button_list(self, other: ModifierButtons) -> None:
        """Sets the list of buttons to watch to be the same as that of the other
        ModifierButtons object.  This makes the lists pointer equivalent (until one
        or the other is later modified).

        This will preserve the state of any button that was on the original list
        and is also on the new lists.  Any other buttons will get reset to the
        default state of "up".
        """
    def matches(self, other: ModifierButtons) -> bool:
        """Returns true if the set of buttons indicated as down by this
        ModifierButtons object is the same set of buttons indicated as down by the
        other ModifierButtons object.  The buttons indicated as up are not
        relevant.
        """
    def add_button(self, button: ButtonHandle | str) -> bool:
        """Adds the indicated button to the set of buttons that will be monitored for
        upness and downness.  Returns true if the button was added, false if it was
        already being monitored or if too many buttons are currently being
        monitored.
        """
    def has_button(self, button: ButtonHandle | str) -> bool:
        """Returns true if the indicated button is in the set of buttons being
        monitored, false otherwise.
        """
    def remove_button(self, button: ButtonHandle | str) -> bool:
        """Removes the indicated button from the set of buttons being monitored.
        Returns true if the button was removed, false if it was not being monitored
        in the first place.

        Unlike the other methods, you cannot remove a button by removing its alias;
        you have to remove exactly the button itself.
        """
    def get_num_buttons(self) -> int:
        """Returns the number of buttons that the ModifierButtons object is monitoring
        (e.g.  the number of buttons passed to add_button()).
        """
    def get_button(self, index: int) -> ButtonHandle:
        """Returns the nth button that the ModifierButtons object is monitoring (the
        nth button passed to add_button()).  This must be in the range 0 <= index <
        get_num_buttons().
        """
    def button_down(self, button: ButtonHandle | str) -> bool:
        """Records that a particular button has been pressed.  If the given button is
        one of the buttons that is currently being monitored, this will update the
        internal state appropriately; otherwise, it will do nothing.  Returns true
        if the button is one that was monitored, or false otherwise.
        """
    def button_up(self, button: ButtonHandle | str) -> bool:
        """Records that a particular button has been released.  If the given button is
        one of the buttons that is currently being monitored, this will update the
        internal state appropriately; otherwise, it will do nothing.  Returns true
        if the button is one that was monitored, or false otherwise.
        """
    def all_buttons_up(self) -> None:
        """Marks all monitored buttons as being in the "up" state."""
    @overload
    def is_down(self, button: ButtonHandle | str) -> bool:
        """`(self, button: ButtonHandle)`:
        Returns true if the indicated button is known to be down, or false if it is
        known to be up or if it is not in the set of buttons being tracked.

        `(self, index: int)`:
        Returns true if the indicated button is known to be down, or false if it is
        known to be up.
        """
    @overload
    def is_down(self, index: int) -> bool: ...
    def is_any_down(self) -> bool:
        """Returns true if any of the tracked button are known to be down, or false if
        all of them are up.
        """
    def get_prefix(self) -> str:
        """Returns a string which can be used to prefix any button name or event name
        with the unique set of modifier buttons currently being held.
        """
    def output(self, out: ostream) -> None:
        """Writes a one-line summary of the buttons known to be down."""
    def write(self, out: ostream) -> None:
        """Writes a multi-line summary including all of the buttons being monitored
        and which ones are known to be down.
        """
    def get_buttons(self) -> tuple[ButtonHandle, ...]: ...
    setButtonList = set_button_list
    addButton = add_button
    hasButton = has_button
    removeButton = remove_button
    getNumButtons = get_num_buttons
    getButton = get_button
    buttonDown = button_down
    buttonUp = button_up
    allButtonsUp = all_buttons_up
    isDown = is_down
    isAnyDown = is_any_down
    getPrefix = get_prefix
    getButtons = get_buttons

class MouseButton:
    """This class is just used as a convenient namespace for grouping all of these
    handy functions that return buttons which map to standard mouse buttons.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: MouseButton = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def button(button_number: int) -> ButtonHandle:
        """Returns the ButtonHandle associated with the particular numbered mouse
        button (zero-based), if there is one, or ButtonHandle::none() if there is
        not.
        """
    @staticmethod
    def one() -> ButtonHandle:
        """Returns the ButtonHandle associated with the first mouse button."""
    @staticmethod
    def two() -> ButtonHandle:
        """Returns the ButtonHandle associated with the second mouse button."""
    @staticmethod
    def three() -> ButtonHandle:
        """Returns the ButtonHandle associated with the third mouse button."""
    @staticmethod
    def four() -> ButtonHandle:
        """Returns the ButtonHandle associated with the fourth mouse button."""
    @staticmethod
    def five() -> ButtonHandle:
        """Returns the ButtonHandle associated with the fifth mouse button."""
    @staticmethod
    def wheel_up() -> ButtonHandle:
        """Returns the ButtonHandle generated when the mouse wheel is rolled one notch
        upwards.
        """
    @staticmethod
    def wheel_down() -> ButtonHandle:
        """Returns the ButtonHandle generated when the mouse wheel is rolled one notch
        downwards.
        """
    @staticmethod
    def wheel_left() -> ButtonHandle:
        """Returns the ButtonHandle generated when the mouse is scrolled to the left.
        Usually, you'll only find the horizontal scroll on laptops.
        """
    @staticmethod
    def wheel_right() -> ButtonHandle:
        """Returns the ButtonHandle generated when the mouse is scrolled to the right.
        Usually, you'll only find the horizontal scroll on laptops.
        """
    @staticmethod
    def is_mouse_button(button: ButtonHandle | str) -> bool:
        """Returns true if the indicated ButtonHandle is a mouse button, false if it
        is some other kind of button.
        """
    wheelUp = wheel_up
    wheelDown = wheel_down
    wheelLeft = wheel_left
    wheelRight = wheel_right
    isMouseButton = is_mouse_button

class PointerType(Enum):
    unknown: int
    mouse: int
    finger: int
    stylus: int
    eraser: int

class PointerData:
    """Holds the data that might be generated by a 2-d pointer input device, such
    as the mouse in the GraphicsWindow.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    @property
    def type(self) -> PointerType: ...
    @property
    def id(self) -> int: ...
    @property
    def in_window(self) -> bool: ...
    @property
    def pressure(self) -> float: ...
    def __init__(self, __param0: PointerData = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def get_in_window(self) -> bool:
        """If this returns false, the pointer is not currently present in the window
        and the values returned by get_x() and get_y() may not be meaningful.
        """
    getX = get_x
    getY = get_y
    getInWindow = get_in_window

class NodeCachedReferenceCount(CachedTypedWritableReferenceCount):
    """This class further specializes CachedTypedWritableReferenceCount to also
    add a node_ref_count, for the purposes of counting the number of times the
    object is referenced by a "node", presumably a PandaNode.

    This essentially combines the functionality of NodeReferenceCount and
    CachedTypedWritableReferenceCount, so that a derivative of this object
    actually has three counters: the standard reference count, the "cache"
    reference count, and the "node" reference count.  Rather than multiply
    inheriting from the two reference count classes, we inherit only from
    CachedTypedWritableReferenceCount and simply duplicate the functionality of
    NodeReferenceCount, to avoid all of the problems associated with multiple
    inheritance.

    The intended design is to use this as a base class for RenderState and
    TransformState, both of which are held by PandaNodes, and also have caches
    which are independently maintained.  By keeping track of how many nodes
    hold a pointer to a particular object, we can classify each object into
    node-referenced, cache-referenced, or other, which is primarily useful for
    PStats reporting.

    As with CachedTypedWritableReferenceCount's cache_ref() and cache_unref(),
    the new methods node_ref() and node_unref() automatically increment and
    decrement the primary reference count as well.  In this case, however,
    there does exist a NodePointerTo<> class to maintain the node_ref counters
    automatically.
    """

    R_node: Final = 1
    RNode: Final = 1
    R_cache: Final = 2
    RCache: Final = 2
    def get_node_ref_count(self) -> int:
        """Returns the current reference count."""
    def node_ref(self) -> None:
        """Explicitly increments the reference count.

        This function is const, even though it changes the object, because
        generally fiddling with an object's reference count isn't considered part
        of fiddling with the object.  An object might be const in other ways, but
        we still need to accurately count the number of references to it.
        """
    def node_unref(self) -> bool:
        """Explicitly decrements the node reference count and the normal reference
        count simultaneously.

        The return value is true if the new reference count is nonzero, false if it
        is zero.
        """
    def get_referenced_bits(self) -> int:
        """Returns the union of the values defined in the Referenced enum that
        represents the various things that appear to be holding a pointer to this
        object.

        If R_node is included, at least one node is holding a pointer; if R_cache
        is included, at least one cache element is.
        """
    getNodeRefCount = get_node_ref_count
    nodeRef = node_ref
    nodeUnref = node_unref
    getReferencedBits = get_referenced_bits

class SparseArray:
    """This class records a set of integers, where each integer is either present
    or not present in the set.

    It is similar in principle and in interface to a BitArray (which can be
    thought of as a set of integers, one integer corresponding to each
    different bit position), but the SparseArray is implemented as a list of
    min/max subrange lists, rather than as a bitmask.

    This makes it particularly efficient for storing sets which consist of
    large sections of consecutively included or consecutively excluded
    elements, with arbitrarily large integers, but particularly inefficient for
    doing boolean operations such as & or |.

    Also, unlike BitArray, the SparseArray can store negative integers.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, _from: BitArray | SparseArray | int = ...) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: BitArray | SparseArray) -> bool: ...
    def __and__(self, other: BitArray | SparseArray) -> SparseArray: ...
    def __or__(self, other: BitArray | SparseArray) -> SparseArray: ...
    def __xor__(self, other: BitArray | SparseArray) -> SparseArray: ...
    def __invert__(self) -> SparseArray: ...
    def __lshift__(self, shift: int) -> SparseArray: ...
    def __rshift__(self, shift: int) -> SparseArray: ...
    def __iand__(self, other: BitArray | SparseArray) -> Self: ...
    def __ior__(self, other: BitArray | SparseArray) -> Self: ...
    def __ixor__(self, other: BitArray | SparseArray) -> Self: ...
    def __ilshift__(self, shift: int) -> Self: ...
    def __irshift__(self, shift: int) -> Self: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def all_on() -> SparseArray:
        """Returns a SparseArray with an infinite array of bits, all on."""
    @staticmethod
    def all_off() -> SparseArray:
        """Returns a SparseArray whose bits are all off."""
    @staticmethod
    def lower_on(on_bits: int) -> SparseArray:
        """Returns a SparseArray whose lower on_bits bits are on."""
    @staticmethod
    def bit(index: int) -> SparseArray:
        """Returns a SparseArray with only the indicated bit on."""
    @staticmethod
    def range(low_bit: int, size: int) -> SparseArray:
        """Returns a SparseArray whose size bits, beginning at low_bit, are on."""
    @staticmethod
    def has_max_num_bits() -> Literal[False]:
        """Returns true if there is a maximum number of bits that may be stored in
        this structure, false otherwise.  If this returns true, the number may be
        queried in get_max_num_bits().

        This method always returns false.  The SparseArray has no maximum number of
        bits.  This method is defined so generic programming algorithms can use
        BitMask or SparseArray interchangeably.
        """
    @staticmethod
    def get_max_num_bits() -> int:
        """If get_max_num_bits() returned true, this method may be called to return
        the maximum number of bits that may be stored in this structure.  It is an
        error to call this if get_max_num_bits() return false.

        It is always an error to call this method.  The SparseArray has no maximum
        number of bits.  This method is defined so generic programming algorithms
        can use BitMask or SparseArray interchangeably.
        """
    def get_num_bits(self) -> int:
        """Returns the current number of possibly different bits in this array.  There
        are actually an infinite number of bits, but every bit higher than this bit
        will have the same value, either 0 or 1 (see get_highest_bits()).

        This number may grow and/or shrink automatically as needed.
        """
    def get_bit(self, index: int) -> bool:
        """Returns true if the nth bit is set, false if it is cleared.  It is valid
        for n to increase beyond get_num_bits(), but the return value
        get_num_bits() will always be the same.
        """
    def set_bit(self, index: int) -> None:
        """Sets the nth bit on.  If n >= get_num_bits(), this automatically extends
        the array.
        """
    def clear_bit(self, index: int) -> None:
        """Sets the nth bit off.  If n >= get_num_bits(), this automatically extends
        the array.
        """
    def set_bit_to(self, index: int, value: bool) -> None:
        """Sets the nth bit either on or off, according to the indicated bool value."""
    def get_highest_bits(self) -> bool:
        """Returns true if the infinite set of bits beyond get_num_bits() are all on,
        or false of they are all off.
        """
    def is_zero(self) -> bool:
        """Returns true if the entire bitmask is zero, false otherwise."""
    def is_all_on(self) -> bool:
        """Returns true if the entire bitmask is one, false otherwise."""
    def has_any_of(self, low_bit: int, size: int) -> bool:
        """Returns true if any bit in the indicated range is set, false otherwise."""
    def has_all_of(self, low_bit: int, size: int) -> bool:
        """Returns true if all bits in the indicated range are set, false otherwise."""
    def set_range(self, low_bit: int, size: int) -> None:
        """Sets the indicated range of bits on."""
    def clear_range(self, low_bit: int, size: int) -> None:
        """Sets the indicated range of bits off."""
    def set_range_to(self, value: bool, low_bit: int, size: int) -> None:
        """Sets the indicated range of bits to either on or off."""
    def get_num_on_bits(self) -> int:
        """Returns the number of bits that are set to 1 in the array.  Returns -1 if
        there are an infinite number of 1 bits.
        """
    def get_num_off_bits(self) -> int:
        """Returns the number of bits that are set to 0 in the array.  Returns -1 if
        there are an infinite number of 0 bits.
        """
    def get_lowest_on_bit(self) -> int:
        """Returns the index of the lowest 1 bit in the array.  Returns -1 if there
        are no 1 bits or if there are an infinite number of 1 bits.
        """
    def get_lowest_off_bit(self) -> int:
        """Returns the index of the lowest 0 bit in the array.  Returns -1 if there
        are no 0 bits or if there are an infinite number of 1 bits.
        """
    def get_highest_on_bit(self) -> int:
        """Returns the index of the highest 1 bit in the array.  Returns -1 if there
        are no 1 bits or if there an infinite number of 1 bits.
        """
    def get_highest_off_bit(self) -> int:
        """Returns the index of the highest 0 bit in the array.  Returns -1 if there
        are no 0 bits or if there an infinite number of 1 bits.
        """
    def get_next_higher_different_bit(self, low_bit: int) -> int:
        """Returns the index of the next bit in the array, above low_bit, whose value
        is different that the value of low_bit.  Returns low_bit again if all bits
        higher than low_bit have the same value.

        This can be used to quickly iterate through all of the bits in the array.
        """
    def invert_in_place(self) -> None:
        """Inverts all the bits in the SparseArray.  This is equivalent to array =
        ~array.
        """
    def has_bits_in_common(self, other: BitArray | SparseArray) -> bool:
        """Returns true if this SparseArray has any "one" bits in common with the
        other one, false otherwise.

        This is equivalent to (array & other) != 0, but may be faster.
        """
    def clear(self) -> None:
        """Sets all the bits in the SparseArray off."""
    def output(self, out: ostream) -> None: ...
    def compare_to(self, other: BitArray | SparseArray) -> int:
        """Returns a number less than zero if this SparseArray sorts before the
        indicated other SparseArray, greater than zero if it sorts after, or 0 if
        they are equivalent.  This is based on the same ordering defined by
        operator <.
        """
    def is_inverse(self) -> bool:
        """If this is true, the SparseArray is actually defined as a list of subranges
        of integers that are *not* in the set.  If this is false (the default),
        then the subranges define the integers that *are* in the set.  This affects
        the interpretation of the values returned by iterating through
        get_num_subranges().
        """
    def get_num_subranges(self) -> int:
        """Returns the number of separate subranges stored in the SparseArray.  You
        can use this limit to iterate through the subranges, calling
        get_subrange_begin() and get_subrange_end() for each one.

        Also see is_inverse().
        """
    def get_subrange_begin(self, n: int) -> int:
        """Returns the first numeric element in the nth subrange.

        Also see is_inverse().
        """
    def get_subrange_end(self, n: int) -> int:
        """Returns the last numeric element, plus one, in the nth subrange.

        Also see is_inverse().
        """
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    allOn = all_on
    allOff = all_off
    lowerOn = lower_on
    hasMaxNumBits = has_max_num_bits
    getMaxNumBits = get_max_num_bits
    getNumBits = get_num_bits
    getBit = get_bit
    setBit = set_bit
    clearBit = clear_bit
    setBitTo = set_bit_to
    getHighestBits = get_highest_bits
    isZero = is_zero
    isAllOn = is_all_on
    hasAnyOf = has_any_of
    hasAllOf = has_all_of
    setRange = set_range
    clearRange = clear_range
    setRangeTo = set_range_to
    getNumOnBits = get_num_on_bits
    getNumOffBits = get_num_off_bits
    getLowestOnBit = get_lowest_on_bit
    getLowestOffBit = get_lowest_off_bit
    getHighestOnBit = get_highest_on_bit
    getHighestOffBit = get_highest_off_bit
    getNextHigherDifferentBit = get_next_higher_different_bit
    invertInPlace = invert_in_place
    hasBitsInCommon = has_bits_in_common
    compareTo = compare_to
    isInverse = is_inverse
    getNumSubranges = get_num_subranges
    getSubrangeBegin = get_subrange_begin
    getSubrangeEnd = get_subrange_end
    getClassType = get_class_type

class ParamValueBase(TypedWritableReferenceCount):
    """A non-template base class of ParamValue (below), which serves mainly to
    define the placeholder for the virtual output function.
    """

    def get_value_type(self) -> TypeHandle:
        """Returns the type of the underlying value."""
    def output(self, out: ostream) -> None: ...
    getValueType = get_value_type

class ParamTypedRefCount(ParamValueBase):
    """A class object for storing specifically objects of type
    TypedReferenceCount, which is different than TypedWritableReferenceCount.
    """

    @property
    def value(self) -> TypedReferenceCount: ...
    def __init__(self, value: TypedReferenceCount) -> None: ...
    def get_value(self) -> TypedReferenceCount:
        """Retrieves the value stored in the parameter."""
    getValue = get_value

class ParamValue_string(ParamValueBase):
    value: str
    def __init__(self, value: str) -> None: ...
    def set_value(self, value: str) -> None: ...
    def get_value(self) -> str: ...
    setValue = set_value
    getValue = get_value

class ParamValue_wstring(ParamValueBase):
    value: str
    def __init__(self, value: str) -> None: ...
    def set_value(self, value: str) -> None: ...
    def get_value(self) -> str: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LVecBase2d(ParamValueBase):
    value: LVecBase2d
    def __init__(self, value: DoubleVec2Like) -> None: ...
    def set_value(self, value: DoubleVec2Like) -> None: ...
    def get_value(self) -> LVecBase2d: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LVecBase2f(ParamValueBase):
    value: LVecBase2f
    def __init__(self, value: Vec2Like) -> None: ...
    def set_value(self, value: Vec2Like) -> None: ...
    def get_value(self) -> LVecBase2f: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LVecBase2i(ParamValueBase):
    value: LVecBase2i
    def __init__(self, value: IntVec2Like) -> None: ...
    def set_value(self, value: IntVec2Like) -> None: ...
    def get_value(self) -> LVecBase2i: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LVecBase3d(ParamValueBase):
    value: LVecBase3d
    def __init__(self, value: DoubleVec3Like) -> None: ...
    def set_value(self, value: DoubleVec3Like) -> None: ...
    def get_value(self) -> LVecBase3d: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LVecBase3f(ParamValueBase):
    value: LVecBase3f
    def __init__(self, value: Vec3Like) -> None: ...
    def set_value(self, value: Vec3Like) -> None: ...
    def get_value(self) -> LVecBase3f: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LVecBase3i(ParamValueBase):
    value: LVecBase3i
    def __init__(self, value: IntVec3Like) -> None: ...
    def set_value(self, value: IntVec3Like) -> None: ...
    def get_value(self) -> LVecBase3i: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LVecBase4d(ParamValueBase):
    value: LVecBase4d
    def __init__(self, value: DoubleVec4Like) -> None: ...
    def set_value(self, value: DoubleVec4Like) -> None: ...
    def get_value(self) -> LVecBase4d: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LVecBase4f(ParamValueBase):
    value: LVecBase4f
    def __init__(self, value: Vec4Like) -> None: ...
    def set_value(self, value: Vec4Like) -> None: ...
    def get_value(self) -> LVecBase4f: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LVecBase4i(ParamValueBase):
    value: LVecBase4i
    def __init__(self, value: IntVec4Like) -> None: ...
    def set_value(self, value: IntVec4Like) -> None: ...
    def get_value(self) -> LVecBase4i: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LMatrix3d(ParamValueBase):
    value: LMatrix3d
    def __init__(self, value: LMatrix3d) -> None: ...
    def set_value(self, value: LMatrix3d) -> None: ...
    def get_value(self) -> LMatrix3d: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LMatrix3f(ParamValueBase):
    value: LMatrix3f
    def __init__(self, value: LMatrix3f) -> None: ...
    def set_value(self, value: LMatrix3f) -> None: ...
    def get_value(self) -> LMatrix3f: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LMatrix4d(ParamValueBase):
    value: LMatrix4d
    def __init__(self, value: DoubleMat4Like) -> None: ...
    def set_value(self, value: DoubleMat4Like) -> None: ...
    def get_value(self) -> LMatrix4d: ...
    setValue = set_value
    getValue = get_value

class ParamValue_LMatrix4f(ParamValueBase):
    value: LMatrix4f
    def __init__(self, value: Mat4Like) -> None: ...
    def set_value(self, value: Mat4Like) -> None: ...
    def get_value(self) -> LMatrix4f: ...
    setValue = set_value
    getValue = get_value

class WritableConfigurable(TypedWritable):
    """Defined as a fix to allow creating Configurable and Writable objects.
    Otherwise the compiler gets confused since both TypedWritable and
    Configurable inherit from TypedObject.

    An object that has data or parameters that are set less frequently (at
    least occasionally) than every frame.  We can cache the configuration info
    by by using the "dirty" flag.
    """

class UniqueIdAllocator:
    """Manage a set of ID values from min to max inclusive.  The ID numbers that
    are freed will be allocated (reused) in the same order.  I.e.  the oldest
    ID numbers will be allocated.

    This implementation will use 4 bytes per id number, plus a few bytes of
    management data.  e.g.  10,000 ID numbers will use 40KB.

    Also be advised that ID -1 and -2 are used internally by the allocator.  If
    allocate returns IndexEnd (-1) then the allocator is out of free ID
    numbers.

    There are other implementations that can better leverage runs of used or
    unused IDs or use bit arrays for the IDs.  But, it takes extra work to
    track the age of freed IDs, which is required for what we wanted.  If you
    would like to kick around other implementation ideas, please contact
    Schuyler.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, min: int = ..., max: int = ...) -> None:
        """Create a free id pool in the range [min:max]."""
    @overload
    def __init__(self, __param0: UniqueIdAllocator) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def allocate(self) -> int:
        """Returns an id between _min and _max (that were passed to the constructor).
        IndexEnd is returned if no ids are available.
        """
    def initial_reserve_id(self, id: int) -> None:
        """This may be called to mark a particular id as having already been allocated
        (for instance, by a prior pass).  The specified id is removed from the
        available pool.

        Because of the limitations of this algorithm, this is most efficient when
        it is called before the first call to allocate(), and when all the calls to
        initial_reserve_id() are made in descending order by id.  However, this is
        a performance warning only; if performance is not an issue, any id may be
        reserved at any time.
        """
    def free(self, index: int) -> None:
        """Free an allocated index (index must be between _min and _max that were
        passed to the constructor).
        """
    def fraction_used(self) -> float:
        """return the decimal fraction of the pool that is used.  The range is 0 to
        1.0 (e.g.  75% would be 0.75).
        """
    def output(self, out: ostream) -> None:
        """...intended for debugging only."""
    def write(self, out: ostream) -> None:
        """...intended for debugging only."""
    initialReserveId = initial_reserve_id
    fractionUsed = fraction_used

ATS_none: Final = 0
ATSNone: Final = 0
ATS_down: Final = 1
ATSDown: Final = 1
ATS_up: Final = 2
ATSUp: Final = 2
ATS_pad: Final = 3
ATSPad: Final = 3
ATS_unspecified: Final = 4
ATSUnspecified: Final = 4
CS_unspecified: Final = 0
CSUnspecified: Final = 0
CS_linear: Final = 1
CSLinear: Final = 1
CS_sRGB: Final = 2
CSSRGB: Final = 2
CS_scRGB: Final = 3
CSScRGB: Final = 3

def parse_color_space_string(str: str) -> _ColorSpace: ...
def format_color_space(cs: _ColorSpace) -> str: ...
def get_model_path() -> ConfigVariableSearchPath: ...
def get_plugin_path() -> ConfigVariableSearchPath: ...
def load_prc_file(filename: StrOrBytesPath) -> ConfigPage:
    """A convenience function for loading explicit prc files from a disk file or
    from within a multifile (via the virtual file system).  Save the return
    value and pass it to unload_prc_file() if you ever want to unload this file
    later.

    The filename is first searched along the default prc search path, and then
    also along the model path, for convenience.

    This function is defined in putil instead of in dtool with the read of the
    prc stuff, so that it can take advantage of the virtual file system (which
    is defined in express), and the model path (which is in putil).
    """

def load_prc_file_data(name: str, data: str) -> ConfigPage:
    """Another convenience function to load a prc file from an explicit string,
    which represents the contents of the prc file.

    The first parameter is an arbitrary name to assign to this in-memory prc
    file.  Supply a filename if the data was read from a file, or use any other
    name that is meaningful to you.  The name is only used when the set of
    loaded prc files is listed.
    """

def unload_prc_file(page: ConfigPage) -> bool: ...
def hash_prc_variables(hash: HashVal) -> None: ...
def py_decode_TypedWritable_from_bam_stream(this_class, data: bytes):
    """This wrapper is defined as a global function to suit pickle's needs.

    This hooks into the native pickle and cPickle modules, but it cannot
    properly handle self-referential BAM objects.
    """

def py_decode_TypedWritable_from_bam_stream_persist(unpickler, this_class, data: bytes):
    """This wrapper is defined as a global function to suit pickle's needs.

    This is similar to py_decode_TypedWritable_from_bam_stream, but it provides
    additional support for the missing persistent-state object needed to
    properly support self-referential BAM objects written to the pickle stream.
    This hooks into the pickle and cPickle modules implemented in
    direct/src/stdpy.
    """

parseColorSpaceString = parse_color_space_string
formatColorSpace = format_color_space
getModelPath = get_model_path
getPluginPath = get_plugin_path
loadPrcFile = load_prc_file
loadPrcFileData = load_prc_file_data
unloadPrcFile = unload_prc_file
hashPrcVariables = hash_prc_variables
pyDecodeTypedWritableFromBamStream = py_decode_TypedWritable_from_bam_stream
pyDecodeTypedWritableFromBamStreamPersist = py_decode_TypedWritable_from_bam_stream_persist
ConstPointerToArrayUshort = ConstPointerToArray_ushort
PointerToArrayBaseUshort = PointerToArrayBase_ushort
PointerToBaseReferenceCountedVectorUshort = PointerToBase_ReferenceCountedVector_ushort
PointerToArrayUshort = PointerToArray_ushort
BitMaskUint16T16 = BitMask_uint16_t_16
BitMask16 = BitMask_uint16_t_16
BitMaskUint32T32 = BitMask_uint32_t_32
BitMask32 = BitMask_uint32_t_32
BitMaskUint64T64 = BitMask_uint64_t_64
BitMask64 = BitMask_uint64_t_64
CollideMask = BitMask32
DoubleBitMaskBitMaskNative = DoubleBitMask_BitMaskNative
DoubleBitMaskNative = DoubleBitMask_BitMaskNative
DoubleBitMaskDoubleBitMaskNative = DoubleBitMask_DoubleBitMaskNative
QuadBitMaskNative = DoubleBitMask_DoubleBitMaskNative
DrawMask = BitMask32
MouseData = PointerData
ParamValueString = ParamValue_string
ParamString = ParamValue_string
ParamValueWstring = ParamValue_wstring
ParamWstring = ParamValue_wstring
ParamValueLVecBase2d = ParamValue_LVecBase2d
ParamVecBase2d = ParamValue_LVecBase2d
ParamValueLVecBase2f = ParamValue_LVecBase2f
ParamVecBase2f = ParamValue_LVecBase2f
ParamValueLVecBase2i = ParamValue_LVecBase2i
ParamVecBase2i = ParamValue_LVecBase2i
ParamValueLVecBase3d = ParamValue_LVecBase3d
ParamVecBase3d = ParamValue_LVecBase3d
ParamValueLVecBase3f = ParamValue_LVecBase3f
ParamVecBase3f = ParamValue_LVecBase3f
ParamValueLVecBase3i = ParamValue_LVecBase3i
ParamVecBase3i = ParamValue_LVecBase3i
ParamValueLVecBase4d = ParamValue_LVecBase4d
ParamVecBase4d = ParamValue_LVecBase4d
ParamValueLVecBase4f = ParamValue_LVecBase4f
ParamVecBase4f = ParamValue_LVecBase4f
ParamValueLVecBase4i = ParamValue_LVecBase4i
ParamVecBase4i = ParamValue_LVecBase4i
ParamValueLMatrix3d = ParamValue_LMatrix3d
ParamMatrix3d = ParamValue_LMatrix3d
ParamValueLMatrix3f = ParamValue_LMatrix3f
ParamMatrix3f = ParamValue_LMatrix3f
ParamValueLMatrix4d = ParamValue_LMatrix4d
ParamMatrix4d = ParamValue_LMatrix4d
ParamValueLMatrix4f = ParamValue_LMatrix4f
ParamMatrix4f = ParamValue_LMatrix4f
ParamVecBase2 = ParamVecBase2f
ParamVecBase3 = ParamVecBase3f
ParamVecBase4 = ParamVecBase4f
ParamMatrix3 = ParamMatrix3f
ParamMatrix4 = ParamMatrix4f
PortalMask = BitMask32
