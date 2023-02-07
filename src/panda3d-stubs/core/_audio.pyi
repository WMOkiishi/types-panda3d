from _typeshed import StrOrBytesPath
from typing import overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import Vec3Like
from panda3d.core._dtoolutil import Filename, ostream
from panda3d.core._event import AsyncTask
from panda3d.core._express import TypedReferenceCount
from panda3d.core._movies import MovieAudio

_AudioSound_SoundStatus: TypeAlias = Literal[0, 1, 2]
_AudioManager_SpeakerModeCategory: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]

class FilterProperties(TypedReferenceCount):
    def __init__(self, __param0: FilterProperties = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def clear(self) -> None:
        """Removes all DSP postprocessing."""
    def add_lowpass(self, cutoff_freq: float, resonance_q: float) -> None:
        """Add a lowpass filter to the end of the DSP chain."""
    def add_highpass(self, cutoff_freq: float, resonance_q: float) -> None:
        """Add a highpass filter to the end of the DSP chain."""
    def add_echo(self, drymix: float, wetmix: float, delay: float, decayratio: float) -> None:
        """Add a echo filter to the end of the DSP chain."""
    def add_flange(self, drymix: float, wetmix: float, depth: float, rate: float) -> None:
        """Add a flange filter to the end of the DSP chain."""
    def add_distort(self, level: float) -> None:
        """Add a distort filter to the end of the DSP chain."""
    def add_normalize(self, fadetime: float, threshold: float, maxamp: float) -> None:
        """Add a normalize filter to the end of the DSP chain."""
    def add_parameq(self, center_freq: float, bandwidth: float, gain: float) -> None:
        """Add a parameq filter to the end of the DSP chain."""
    def add_pitchshift(self, pitch: float, fftsize: float, overlap: float) -> None:
        """Add a pitchshift filter to the end of the DSP chain."""
    def add_chorus(self, drymix: float, wet1: float, wet2: float, wet3: float, delay: float, rate: float, depth: float) -> None:
        """Add a chorus filter to the end of the DSP chain."""
    def add_sfxreverb(
        self,
        drylevel: float = ...,
        room: float = ...,
        roomhf: float = ...,
        decaytime: float = ...,
        decayhfratio: float = ...,
        reflectionslevel: float = ...,
        reflectionsdelay: float = ...,
        reverblevel: float = ...,
        reverbdelay: float = ...,
        diffusion: float = ...,
        density: float = ...,
        hfreference: float = ...,
        roomlf: float = ...,
        lfreference: float = ...,
    ) -> None:
        """Add a reverb filter to the end of the DSP chain."""
    def add_compress(self, threshold: float, attack: float, release: float, gainmakeup: float) -> None:
        """Add a compress filter to the end of the DSP chain."""
    addLowpass = add_lowpass
    addHighpass = add_highpass
    addEcho = add_echo
    addFlange = add_flange
    addDistort = add_distort
    addNormalize = add_normalize
    addParameq = add_parameq
    addPitchshift = add_pitchshift
    addChorus = add_chorus
    addSfxreverb = add_sfxreverb
    addCompress = add_compress

class AudioSound(TypedReferenceCount):
    BAD: Final = 0
    READY: Final = 1
    PLAYING: Final = 2
    def play(self) -> None:
        """For best compatibility, set the loop_count, volume, and balance, prior to
        calling play().  You may set them while they're playing, but it's
        implementation specific whether you get the results.  - Calling play() a
        second time on the same sound before it is finished will start the sound
        again (creating a skipping or stuttering effect).
        """
    def stop(self) -> None: ...
    def set_loop(self, loop: bool = ...) -> None:
        """loop: false = play once; true = play forever.  inits to false."""
    def get_loop(self) -> bool: ...
    def set_loop_count(self, loop_count: int = ...) -> None:
        """loop_count: 0 = forever; 1 = play once; n = play n times.  inits to 1."""
    def get_loop_count(self) -> int: ...
    def set_time(self, start_time: float = ...) -> None:
        """Control time position within the sound, in seconds.  This is similar (in
        concept) to the seek position within a file.  The value starts at 0.0 (the
        default) and ends at the value given by the length() method.

        The current time position will not change while the sound is playing; you
        must call play() again to effect the change.  To play the same sound from
        a time offset a second time, explicitly set the time position again.  When
        looping, the second and later loops will start from the beginning of the
        sound.

        If a sound is playing, calling get_time() repeatedly will return different
        results over time.  e.g.
        @code
        PN_stdfloat percent_complete = s.get_time() / s.length();
        @endcode
        """
    def get_time(self) -> float: ...
    def set_volume(self, volume: float = ...) -> None:
        """0 = minimum; 1.0 = maximum.  inits to 1.0."""
    def get_volume(self) -> float: ...
    def set_balance(self, balance_right: float = ...) -> None:
        """-1.0 is hard left 0.0 is centered 1.0 is hard right inits to 0.0."""
    def get_balance(self) -> float: ...
    def set_play_rate(self, play_rate: float = ...) -> None:
        """play_rate is any positive PN_stdfloat value.  inits to 1.0."""
    def get_play_rate(self) -> float: ...
    def set_active(self, flag: bool = ...) -> None:
        """inits to manager's state."""
    def get_active(self) -> bool: ...
    def set_finished_event(self, event: str) -> None:
        """Set (or clear) the event that will be thrown when the sound finishes
        playing.  To clear the event, pass an empty string.
        """
    def get_finished_event(self) -> str: ...
    def get_name(self) -> str:
        """There is no set_name(), this is intentional."""
    def length(self) -> float:
        """return: playing time in seconds."""
    def set_3d_attributes(self, px: float, py: float, pz: float, vx: float, vy: float, vz: float) -> None:
        """Controls the position of this sound's emitter.  px, py and pz are the
        emitter's position.  vx, vy and vz are the emitter's velocity in UNITS
        PER SECOND (default: meters).
        """
    def set_3d_min_distance(self, dist: float) -> None:
        """Controls the distance (in units) that this sound begins to fall off.
        Also affects the rate it falls off.  Default is 1.0 CloserFaster, <1.0
        FartherSlower, >1.0
        """
    def get_3d_min_distance(self) -> float: ...
    def set_3d_max_distance(self, dist: float) -> None:
        """Controls the maximum distance (in units) that this sound stops falling
        off.  The sound does not stop at that point, it just doesn't get any
        quieter.  You should rarely need to adjust this.  Default is 1000000000.0
        """
    def get_3d_max_distance(self) -> float: ...
    def get_speaker_mix(self, speaker: int) -> float:
        """speaker_mix and speaker_level(s) serve the same purpose.
        speaker_mix is for use with FMOD. speaker_level(s) is for use with
        Miles.  Both interfaces exist because of a significant difference in the
        two APIs.  Hopefully the difference can be reconciled into a single
        interface at some point.
        """
    def set_speaker_mix(
        self,
        frontleft: float,
        frontright: float,
        center: float,
        sub: float,
        backleft: float,
        backright: float,
        sideleft: float,
        sideright: float,
    ) -> None: ...
    def get_speaker_level(self, index: int) -> float: ...
    def set_speaker_levels(
        self,
        level1: float,
        level2: float = ...,
        level3: float = ...,
        level4: float = ...,
        level5: float = ...,
        level6: float = ...,
        level7: float = ...,
        level8: float = ...,
        level9: float = ...,
    ) -> None: ...
    def get_priority(self) -> int: ...
    def set_priority(self, priority: int) -> None: ...
    def configure_filters(self, config: FilterProperties) -> bool: ...
    def status(self) -> _AudioSound_SoundStatus: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    setLoop = set_loop
    getLoop = get_loop
    setLoopCount = set_loop_count
    getLoopCount = get_loop_count
    setTime = set_time
    getTime = get_time
    setVolume = set_volume
    getVolume = get_volume
    setBalance = set_balance
    getBalance = get_balance
    setPlayRate = set_play_rate
    getPlayRate = get_play_rate
    setActive = set_active
    getActive = get_active
    setFinishedEvent = set_finished_event
    getFinishedEvent = get_finished_event
    getName = get_name
    set3dAttributes = set_3d_attributes
    set3dMinDistance = set_3d_min_distance
    get3dMinDistance = get_3d_min_distance
    set3dMaxDistance = set_3d_max_distance
    get3dMaxDistance = get_3d_max_distance
    getSpeakerMix = get_speaker_mix
    setSpeakerMix = set_speaker_mix
    getSpeakerLevel = get_speaker_level
    setSpeakerLevels = set_speaker_levels
    getPriority = get_priority
    setPriority = set_priority
    configureFilters = configure_filters

class AudioManager(TypedReferenceCount):
    SPEAKERMODE_raw: Final = 0
    SPEAKERMODERaw: Final = 0
    SPEAKERMODE_mono: Final = 1
    SPEAKERMODEMono: Final = 1
    SPEAKERMODE_stereo: Final = 2
    SPEAKERMODEStereo: Final = 2
    SPEAKERMODE_quad: Final = 3
    SPEAKERMODEQuad: Final = 3
    SPEAKERMODE_surround: Final = 4
    SPEAKERMODESurround: Final = 4
    SPEAKERMODE_5point1: Final = 5
    SPEAKERMODE5point1: Final = 5
    SPEAKERMODE_7point1: Final = 6
    SPEAKERMODE7point1: Final = 6
    SPEAKERMODE_max: Final = 7
    SPEAKERMODEMax: Final = 7
    SPEAKERMODE_COUNT: Final = 8
    SPEAKERMODECOUNT: Final = 8
    SPK_none: Final = 0
    SPKNone: Final = 0
    SPK_frontleft: Final = 1
    SPKFrontleft: Final = 1
    SPK_frontright: Final = 2
    SPKFrontright: Final = 2
    SPK_center: Final = 3
    SPKCenter: Final = 3
    SPK_sub: Final = 4
    SPKSub: Final = 4
    SPK_backleft: Final = 5
    SPKBackleft: Final = 5
    SPK_backright: Final = 6
    SPKBackright: Final = 6
    SPK_sideleft: Final = 7
    SPKSideleft: Final = 7
    SPK_sideright: Final = 8
    SPKSideright: Final = 8
    SPK_COUNT: Final = 9
    SPKCOUNT: Final = 9
    SM_heuristic: Final = 0
    SMHeuristic: Final = 0
    SM_sample: Final = 1
    SMSample: Final = 1
    SM_stream: Final = 2
    SMStream: Final = 2
    @property
    def dls_pathname(self) -> Filename: ...
    def get_speaker_setup(self) -> int: ...
    def set_speaker_setup(self, cat: _AudioManager_SpeakerModeCategory) -> None: ...
    def configure_filters(self, config: FilterProperties) -> bool: ...
    @staticmethod
    def create_AudioManager() -> AudioManager: ...
    def shutdown(self) -> None: ...
    def is_valid(self) -> bool:
        """If you're interested in knowing whether this audio manager is valid,
        here's the call to do it.  It is not necessary to check whether the audio
        manager is valid before making other calls.  You are free to use an
        invalid sound manager, you may get silent sounds from it though.  The
        sound manager and the sounds it creates should not crash the application
        even when the objects are not valid.
        """
    @overload
    def get_sound(self, file_name: StrOrBytesPath, positional: bool = ..., mode: int = ...) -> AudioSound:
        """Get a sound:"""
    @overload
    def get_sound(self, source: MovieAudio, positional: bool = ..., mode: int = ...) -> AudioSound: ...
    def get_null_sound(self) -> AudioSound: ...
    def uncache_sound(self, file_name: StrOrBytesPath) -> None:
        """Tell the AudioManager there is no need to keep this one cached.  This
        doesn't break any connection between AudioSounds that have already given
        by get_sound() from this manager.  It's only affecting whether the
        AudioManager keeps a copy of the sound in its poolcache.
        """
    def clear_cache(self) -> None: ...
    def set_cache_limit(self, count: int) -> None: ...
    def get_cache_limit(self) -> int: ...
    def set_volume(self, volume: float) -> None:
        """Control volume: FYI: If you start a sound with the volume off and turn
        the volume up later, you'll hear the sound playing at that late point.  0
        = minimum; 1.0 = maximum.  inits to 1.0.
        """
    def get_volume(self) -> float: ...
    def set_active(self, flag: bool) -> None:
        """Turn the manager on or off.  If you play a sound while the manager is
        inactive, it won't start.  If you deactivate the manager while sounds are
        playing, they'll stop.  If you activate the manager while looping sounds
        are playing (those that have a loop_count of zero), they will start
        playing from the beginning of their loop.  Defaults to true.
        """
    def get_active(self) -> bool: ...
    def set_concurrent_sound_limit(self, limit: int = ...) -> None:
        """This controls the number of sounds that you allow at once.  This is more
        of a user choice -- it avoids talk over and the creation of a cacophony.
        It can also be used to help performance.  0 == unlimited.  1 == mutually
        exclusive (one sound at a time).  Which is an example of: n == allow n
        sounds to be playing at the same time.
        """
    def get_concurrent_sound_limit(self) -> int: ...
    def reduce_sounds_playing_to(self, count: int) -> None:
        """This is likely to be a utility function for the concurrent_sound_limit
        options.  It is exposed as an API, because it's reasonable that it may be
        useful to be here.  It reduces the number of concurrently playing sounds
        to count by some implementation specific means.  If the number of sounds
        currently playing is at or below count then there is no effect.
        """
    def stop_all_sounds(self) -> None:
        """Stop playback on all sounds managed by this manager.  This is effectively
        the same as reduce_sounds_playing_to(0), but this call may be for
        efficient on some implementations.
        """
    def update(self) -> None:
        """This should be called every frame.  Failure to call could cause problems."""
    def audio_3d_set_listener_attributes(
        self,
        px: float,
        py: float,
        pz: float,
        vx: float,
        vy: float,
        vz: float,
        fx: float,
        fy: float,
        fz: float,
        ux: float,
        uy: float,
        uz: float,
    ) -> None:
        """This controls the "set of ears" that listens to 3D spacialized sound px,
        py, pz are position coordinates.  vx, vy, vz are a velocity vector in
        UNITS PER SECOND (default: meters). fx, fy and fz are the respective
        components of a unit forward-vector ux, uy and uz are the respective
        components of a unit up-vector
        """
    def audio_3d_set_distance_factor(self, factor: float) -> None:
        """Control the "relative scale that sets the distance factor" units for 3D
        spacialized audio. This is a float in units-per-meter. Default value is
        1.0, which means that Panda units are understood as meters; for e.g.
        feet, set 3.28. This factor is applied only to Fmod and OpenAL at the
        moment.
        """
    def audio_3d_get_distance_factor(self) -> float: ...
    def audio_3d_set_doppler_factor(self, factor: float) -> None:
        """Control the presence of the Doppler effect.  Default is 1.0 Exaggerated
        Doppler, use >1.0 Diminshed Doppler, use <1.0
        """
    def audio_3d_get_doppler_factor(self) -> float: ...
    def audio_3d_set_drop_off_factor(self, factor: float) -> None:
        """Exaggerate or diminish the effect of distance on sound.  Default is 1.0
        Valid range is 0 to 10 Faster drop off, use >1.0 Slower drop off, use
        <1.0
        """
    def audio_3d_get_drop_off_factor(self) -> float: ...
    @staticmethod
    def get_dls_pathname() -> Filename: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    def set_speaker_configuration(
        self,
        speaker1: Vec3Like,
        speaker2: Vec3Like = ...,
        speaker3: Vec3Like = ...,
        speaker4: Vec3Like = ...,
        speaker5: Vec3Like = ...,
        speaker6: Vec3Like = ...,
        speaker7: Vec3Like = ...,
        speaker8: Vec3Like = ...,
        speaker9: Vec3Like = ...,
    ) -> None:
        """set_speaker_configuration is a Miles only method."""
    getSpeakerSetup = get_speaker_setup
    setSpeakerSetup = set_speaker_setup
    configureFilters = configure_filters
    createAudioManager = create_AudioManager
    isValid = is_valid
    getSound = get_sound
    getNullSound = get_null_sound
    uncacheSound = uncache_sound
    clearCache = clear_cache
    setCacheLimit = set_cache_limit
    getCacheLimit = get_cache_limit
    setVolume = set_volume
    getVolume = get_volume
    setActive = set_active
    getActive = get_active
    setConcurrentSoundLimit = set_concurrent_sound_limit
    getConcurrentSoundLimit = get_concurrent_sound_limit
    reduceSoundsPlayingTo = reduce_sounds_playing_to
    stopAllSounds = stop_all_sounds
    audio3dSetListenerAttributes = audio_3d_set_listener_attributes
    audio3dSetDistanceFactor = audio_3d_set_distance_factor
    audio3dGetDistanceFactor = audio_3d_get_distance_factor
    audio3dSetDopplerFactor = audio_3d_set_doppler_factor
    audio3dGetDopplerFactor = audio_3d_get_doppler_factor
    audio3dSetDropOffFactor = audio_3d_set_drop_off_factor
    audio3dGetDropOffFactor = audio_3d_get_drop_off_factor
    getDlsPathname = get_dls_pathname
    setSpeakerConfiguration = set_speaker_configuration

class AudioLoadRequest(AsyncTask):
    """A class object that manages a single asynchronous audio load request.  This
    works in conjunction with the Loader class defined in pgraph, or really
    with any AsyncTaskManager.  Create a new AudioLoadRequest, and add it to
    the loader via load_async(), to begin an asynchronous load.
    """

    @overload
    def __init__(self, __param0: AudioLoadRequest) -> None:
        """Create a new AudioLoadRequest, and add it to the loader via load_async(),
        to begin an asynchronous load.
        """
    @overload
    def __init__(self, audio_manager: AudioManager, filename: str, positional: bool) -> None: ...
    def get_audio_manager(self) -> AudioManager:
        """Returns the AudioManager that will serve this asynchronous
        AudioLoadRequest.
        """
    def get_filename(self) -> str:
        """Returns the filename associated with this asynchronous AudioLoadRequest."""
    def get_positional(self) -> bool:
        """Returns the positional flag associated with this asynchronous
        AudioLoadRequest.
        """
    def is_ready(self) -> bool:
        """Returns true if this request has completed, false if it is still pending.
        When this returns true, you may retrieve the sound loaded by calling
        get_sound().
        Equivalent to `req.done() and not req.cancelled()`.
        @see done()
        """
    def get_sound(self) -> AudioSound:
        """Returns the sound that was loaded asynchronously, if any, or nullptr if
        there was an error.  It is an error to call this unless done() returns
        true.
        @deprecated Use result() instead.
        """
    getAudioManager = get_audio_manager
    getFilename = get_filename
    getPositional = get_positional
    isReady = is_ready
    getSound = get_sound
