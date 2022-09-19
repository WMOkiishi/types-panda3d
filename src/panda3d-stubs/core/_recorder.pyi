from typing import Any, ClassVar, overload
from panda3d._typing import Filepath
from panda3d.core import DataNode, Datagram, Filename, ReferenceCount, SocketStream, TypeHandle, TypedReferenceCount

class RecorderBase:
    """This is the base class to a number of objects that record particular kinds
    of user input (like a MouseRecorder) to use in conjunction with a
    RecorderController to record the user's inputs for a session.
    
    Note that RecorderBase does not actually inherit from TypedObject, even
    though it defines get_type().  The assumption is that the classes that
    derive from RecorderBase might also inherit independently from TypedObject.
    
    It also does not inherit from TypedWritable, but it defines a method called
    write_recorder() which is very similar to a TypedWritable's
    write_datagram(). Classes that derive from RecorderBase and also inherit
    from TypedWritable may choose to remap write_recorder() to do exactly the
    same thing as write_datagram(), or they may choose to write something
    slightly different.
    
    Most types of recorders should derive from Recorder, as it derives from
    ReferenceCount, except for MouseRecorder, which would otherwise doubly
    inherit from ReferenceCount.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def is_recording(self) -> bool:
        """Returns true if this recorder is presently recording data for saving to a
        session file, false otherwise.  If this is true, record_data() will be
        called from time to time.
        """
        ...
    def is_playing(self) -> bool:
        """Returns true if this recorder is presently playing back data from session
        file, false otherwise.  If this is true, play_data() will be called from
        time to time.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    isRecording = is_recording
    isPlaying = is_playing
    getClassType = get_class_type

class MouseRecorder(DataNode, RecorderBase):
    """This object records any data generated by a particular MouseAndKeyboard
    node on the datagraph for a session for eventual playback via a
    DataGraphPlayback (and a PlaybackController).  To use it, make it a child
    of the node you wish to record.  It also serves as a pass-through, so that
    additional child nodes may be parented directly to it.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str) -> None: ...
    def upcast_to_DataNode(self) -> DataNode: ...
    def upcast_to_RecorderBase(self) -> RecorderBase: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToDataNode = upcast_to_DataNode
    upcastToRecorderBase = upcast_to_RecorderBase
    getClassType = get_class_type

class RecorderController(TypedReferenceCount):
    """This object manages the process of recording the user's runtime inputs to a
    bam file so that the session can be recreated later.
    """
    def __init__(self) -> None: ...
    def begin_record(self, filename: Filepath) -> bool:
        """Begins recording data to the indicated filename.  All of the recorders in
        use should already have been added.
        """
        ...
    def begin_playback(self, filename: Filepath) -> bool:
        """Begins playing back data from the indicated filename.  All of the recorders
        in use should already have been added, although this may define additional
        recorders if they are present in the file (these new recorders will not be
        used).  This may also undefine recorders that were previously added but are
        not present in the file.
        """
        ...
    def close(self) -> None:
        """Finishes recording data to the indicated filename."""
        ...
    def get_start_time(self) -> int:
        """Returns the time (and date) at which the current session was originally
        recorded (or, in recording mode, the time at which the current session
        began).
        """
        ...
    def set_random_seed(self, random_seed: int) -> None:
        """Indicates an arbitrary number to be recorded in the session file as a
        random seed, should the application wish to take advantage of it.  This
        must be set before begin_record() is called.
        """
        ...
    def get_random_seed(self) -> int:
        """Returns the random seed that was set by a previous call to
        set_random_seed(), or the number read from the session file after
        begin_playback() has been called.
        """
        ...
    def is_recording(self) -> bool:
        """Returns true if the controller has been opened for output, false otherwise."""
        ...
    def is_playing(self) -> bool:
        """Returns true if the controller has been opened for input, false otherwise."""
        ...
    def is_open(self) -> bool:
        """Returns true if the controller has been opened for either input or output,
        false otherwise.
        """
        ...
    def get_filename(self) -> Filename:
        """Returns the filename that was passed to the most recent call to
        begin_record() or begin_playback().
        """
        ...
    def is_error(self) -> bool:
        """Returns true if the controller has been opened for input or output output
        and there is an error on the stream, or false if the controller is closed
        or if there is no problem.
        """
        ...
    def get_clock_offset(self) -> float:
        """Returns the delta offset between the actual frame time and the frame time
        written to the log.  This is essentially the time at which the recording
        (or playback) started.
        """
        ...
    def get_frame_offset(self) -> int:
        """Returns the delta offset between the actual frame count and the frame count
        written to the log.  This is essentially the frame number at which the
        recording (or playback) started.
        """
        ...
    def add_recorder(self, name: str, recorder: RecorderBase) -> None:
        """Adds the named recorder to the set of recorders that are in use.
        
        If the controller is in recording mode, the named recorder will begin
        recording its status to the session file.  If the controller is in playback
        mode and the name and type matches a recorder in the session file, the
        recorder will begin receiving data.
        """
        ...
    def has_recorder(self, name: str) -> bool:
        """Returns true if the named recorder has been added to the table by a
        previous call to add_recorder(), false otherwise.
        
        If the controller is in playback mode, this will also return false for a
        recorder that was found in the session file but was never explicitly added
        via add_recorder(); see get_recorder().
        """
        ...
    def get_recorder(self, name: str) -> RecorderBase:
        """Returns the recorder with the indicated name, or NULL if there is no such
        recorder.
        
        If the controller is in playback mode, this may return the recorder
        matching the indicated name as read from the session file, even if it was
        never added to the table by the user.  In this case, has_recorder() may
        return false, but get_recorder() will return a non-NULL value.
        """
        ...
    def remove_recorder(self, name: str) -> bool:
        """Removes the named recorder from the table.  Returns true if successful,
        false if there was no such recorder.
        
        If the controller is in recording mode, the named recorder will stop
        recording.  If the controller is in playback mode, the named recorder will
        disassociate itself from the session file (but if the session file still
        has data for this name, a default recorder will take its place to decode
        the data from the session file).
        """
        ...
    def set_frame_tie(self, frame_tie: bool) -> None:
        """Sets the frame_tie flag.
        
        When this is true, sessions are played back frame-for-frame, based on the
        frame count of the recorded session.  This gives the most accurate
        playback, but the playback rate will vary according to the frame rate of
        the playback machine.
        
        When this is false, sessions are played back at real time, based on the
        clock of the recorded session.  This may introduce playback discrepencies
        if the frames do not fall at exactly the same times as they did in the
        original.
        """
        ...
    def get_frame_tie(self) -> bool:
        """See set_frame_tie()."""
        ...
    def record_frame(self) -> None:
        """Gets the next frame of data from all of the active recorders and adds it to
        the output file.
        """
        ...
    def play_frame(self) -> None:
        """Gets the next frame of data from all of the active recorders and adds it to
        the output file.
        """
        ...
    beginRecord = begin_record
    beginPlayback = begin_playback
    getStartTime = get_start_time
    setRandomSeed = set_random_seed
    getRandomSeed = get_random_seed
    isRecording = is_recording
    isPlaying = is_playing
    isOpen = is_open
    getFilename = get_filename
    isError = is_error
    getClockOffset = get_clock_offset
    getFrameOffset = get_frame_offset
    addRecorder = add_recorder
    hasRecorder = has_recorder
    getRecorder = get_recorder
    removeRecorder = remove_recorder
    setFrameTie = set_frame_tie
    getFrameTie = get_frame_tie
    recordFrame = record_frame
    playFrame = play_frame

class SocketStreamRecorder(RecorderBase, ReferenceCount):
    """Records any data received from the indicated socket stream.  On playback,
    it will act as if the incoming data is coming over the wire again even if
    an actual connection is not available.
    
    Outbound data will not be recorded, but will be sent straight through to
    the socket if it is connected, or silently ignored if it is not.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, stream: SocketStream, owns_stream: bool) -> None: ...
    def upcast_to_RecorderBase(self) -> RecorderBase: ...
    def upcast_to_ReferenceCount(self) -> ReferenceCount: ...
    def receive_datagram(self, dg: Datagram) -> bool:
        """Receives a datagram over the socket by expecting a little-endian 16-bit
        byte count as a prefix.  If the socket stream is non-blocking, may return
        false if the data is not available; otherwise, returns false only if the
        socket closes.
        """
        ...
    def send_datagram(self, dg: Datagram) -> bool:
        """See SocketStream::send_datagram()."""
        ...
    def is_closed(self) -> bool:
        """See SocketStream::is_closed()."""
        ...
    def close(self) -> None:
        """See SocketStream::close()."""
        ...
    def set_collect_tcp(self, collect_tcp: bool) -> None:
        """See SocketStream::set_collect_tcp()."""
        ...
    def get_collect_tcp(self) -> bool:
        """See SocketStream::get_collect_tcp()."""
        ...
    def set_collect_tcp_interval(self, interval: float) -> None:
        """See SocketStream::set_collect_tcp_interval()."""
        ...
    def get_collect_tcp_interval(self) -> float:
        """See SocketStream::get_collect_tcp_interval()."""
        ...
    def consider_flush(self) -> bool:
        """See SocketStream::consider_flush()"""
        ...
    def flush(self) -> bool:
        """See SocketStream::flush()"""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToRecorderBase = upcast_to_RecorderBase
    upcastToReferenceCount = upcast_to_ReferenceCount
    receiveDatagram = receive_datagram
    sendDatagram = send_datagram
    isClosed = is_closed
    setCollectTcp = set_collect_tcp
    getCollectTcp = get_collect_tcp
    setCollectTcpInterval = set_collect_tcp_interval
    getCollectTcpInterval = get_collect_tcp_interval
    considerFlush = consider_flush
    getClassType = get_class_type