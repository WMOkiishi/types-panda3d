from os import PathLike
from typing import Any, ClassVar, Literal, TypeAlias, overload

_AudioSound_SoundStatus: TypeAlias = Literal[0, 1, 2]
_AudioManager_SpeakerModeCategory: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike
_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow

class FilterProperties(TypedReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: FilterProperties) -> None: ...
    def clear(self) -> None: ...
    def add_lowpass(self, cutoff_freq: float, resonance_q: float) -> None: ...
    def add_highpass(self, cutoff_freq: float, resonance_q: float) -> None: ...
    def add_echo(self, drymix: float, wetmix: float, delay: float, decayratio: float) -> None: ...
    def add_flange(self, drymix: float, wetmix: float, depth: float, rate: float) -> None: ...
    def add_distort(self, level: float) -> None: ...
    def add_normalize(self, fadetime: float, threshold: float, maxamp: float) -> None: ...
    def add_parameq(self, center_freq: float, bandwidth: float, gain: float) -> None: ...
    def add_pitchshift(self, pitch: float, fftsize: float, overlap: float) -> None: ...
    def add_chorus(self, drymix: float, wet1: float, wet2: float, wet3: float, delay: float, rate: float, depth: float) -> None: ...
    def add_sfxreverb(self, drylevel: float = ..., room: float = ..., roomhf: float = ..., decaytime: float = ..., decayhfratio: float = ..., reflectionslevel: float = ..., reflectionsdelay: float = ..., reverblevel: float = ..., reverbdelay: float = ..., diffusion: float = ..., density: float = ..., hfreference: float = ..., roomlf: float = ..., lfreference: float = ...) -> None: ...
    def add_compress(self, threshold: float, attack: float, release: float, gainmakeup: float) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type

class AudioSound(TypedReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    BAD: ClassVar[Literal[0]]
    READY: ClassVar[Literal[1]]
    PLAYING: ClassVar[Literal[2]]
    def play(self) -> None: ...
    def stop(self) -> None: ...
    def set_loop(self, loop: bool = ...) -> None: ...
    def get_loop(self) -> bool: ...
    def set_loop_count(self, loop_count: int = ...) -> None: ...
    def get_loop_count(self) -> int: ...
    def set_time(self, start_time: float = ...) -> None: ...
    def get_time(self) -> float: ...
    def set_volume(self, volume: float = ...) -> None: ...
    def get_volume(self) -> float: ...
    def set_balance(self, balance_right: float = ...) -> None: ...
    def get_balance(self) -> float: ...
    def set_play_rate(self, play_rate: float = ...) -> None: ...
    def get_play_rate(self) -> float: ...
    def set_active(self, flag: bool = ...) -> None: ...
    def get_active(self) -> bool: ...
    def set_finished_event(self, event: str) -> None: ...
    def get_finished_event(self) -> str: ...
    def get_name(self) -> str: ...
    def length(self) -> float: ...
    def set_3d_attributes(self, px: float, py: float, pz: float, vx: float, vy: float, vz: float) -> None: ...
    def set_3d_min_distance(self, dist: float) -> None: ...
    def get_3d_min_distance(self) -> float: ...
    def set_3d_max_distance(self, dist: float) -> None: ...
    def get_3d_max_distance(self) -> float: ...
    def get_speaker_mix(self, speaker: int) -> float: ...
    def set_speaker_mix(self, frontleft: float, frontright: float, center: float, sub: float, backleft: float, backright: float, sideleft: float, sideright: float) -> None: ...
    def get_speaker_level(self, index: int) -> float: ...
    def set_speaker_levels(self, level1: float, level2: float = ..., level3: float = ..., level4: float = ..., level5: float = ..., level6: float = ..., level7: float = ..., level8: float = ..., level9: float = ...) -> None: ...
    def get_priority(self) -> int: ...
    def set_priority(self, priority: int) -> None: ...
    def configure_filters(self, config: FilterProperties) -> bool: ...
    def status(self) -> _AudioSound_SoundStatus: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type

class AudioManager(TypedReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    SPEAKERMODE_raw: ClassVar[Literal[0]]
    SPEAKERMODE_mono: ClassVar[Literal[1]]
    SPEAKERMODE_stereo: ClassVar[Literal[2]]
    SPEAKERMODE_quad: ClassVar[Literal[3]]
    SPEAKERMODE_surround: ClassVar[Literal[4]]
    SPEAKERMODE_5point1: ClassVar[Literal[5]]
    SPEAKERMODE_7point1: ClassVar[Literal[6]]
    SPEAKERMODE_max: ClassVar[Literal[7]]
    SPEAKERMODE_COUNT: ClassVar[Literal[8]]
    SPK_none: ClassVar[Literal[0]]
    SPK_frontleft: ClassVar[Literal[1]]
    SPK_frontright: ClassVar[Literal[2]]
    SPK_center: ClassVar[Literal[3]]
    SPK_sub: ClassVar[Literal[4]]
    SPK_backleft: ClassVar[Literal[5]]
    SPK_backright: ClassVar[Literal[6]]
    SPK_sideleft: ClassVar[Literal[7]]
    SPK_sideright: ClassVar[Literal[8]]
    SPK_COUNT: ClassVar[Literal[9]]
    SM_heuristic: ClassVar[Literal[0]]
    SM_sample: ClassVar[Literal[1]]
    SM_stream: ClassVar[Literal[2]]
    @property
    def dls_pathname(self) -> Filename: ...
    def get_speaker_setup(self) -> int: ...
    def set_speaker_setup(self, cat: _AudioManager_SpeakerModeCategory) -> None: ...
    def configure_filters(self, config: FilterProperties) -> bool: ...
    @staticmethod
    def create_AudioManager() -> AudioManager: ...
    def shutdown(self) -> None: ...
    def is_valid(self) -> bool: ...
    @overload
    def get_sound(self, file_name: _Filename, positional: bool = ..., mode: int = ...) -> AudioSound: ...
    @overload
    def get_sound(self, source: MovieAudio, positional: bool = ..., mode: int = ...) -> AudioSound: ...
    def get_null_sound(self) -> AudioSound: ...
    def uncache_sound(self, file_name: _Filename) -> None: ...
    def clear_cache(self) -> None: ...
    def set_cache_limit(self, count: int) -> None: ...
    def get_cache_limit(self) -> int: ...
    def set_volume(self, volume: float) -> None: ...
    def get_volume(self) -> float: ...
    def set_active(self, flag: bool) -> None: ...
    def get_active(self) -> bool: ...
    def set_concurrent_sound_limit(self, limit: int = ...) -> None: ...
    def get_concurrent_sound_limit(self) -> int: ...
    def reduce_sounds_playing_to(self, count: int) -> None: ...
    def stop_all_sounds(self) -> None: ...
    def update(self) -> None: ...
    def audio_3d_set_listener_attributes(self, px: float, py: float, pz: float, vx: float, vy: float, vz: float, fx: float, fy: float, fz: float, ux: float, uy: float, uz: float) -> None: ...
    def audio_3d_set_distance_factor(self, factor: float) -> None: ...
    def audio_3d_get_distance_factor(self) -> float: ...
    def audio_3d_set_doppler_factor(self, factor: float) -> None: ...
    def audio_3d_get_doppler_factor(self) -> float: ...
    def audio_3d_set_drop_off_factor(self, factor: float) -> None: ...
    def audio_3d_get_drop_off_factor(self) -> float: ...
    @staticmethod
    def get_dls_pathname() -> Filename: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    def set_speaker_configuration(self, speaker1: _Vec3f, speaker2: _Vec3f = ..., speaker3: _Vec3f = ..., speaker4: _Vec3f = ..., speaker5: _Vec3f = ..., speaker6: _Vec3f = ..., speaker7: _Vec3f = ..., speaker8: _Vec3f = ..., speaker9: _Vec3f = ...) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type
    SPEAKERMODERaw = SPEAKERMODE_raw
    SPEAKERMODEMono = SPEAKERMODE_mono
    SPEAKERMODEStereo = SPEAKERMODE_stereo
    SPEAKERMODEQuad = SPEAKERMODE_quad
    SPEAKERMODESurround = SPEAKERMODE_surround
    SPEAKERMODE5point1 = SPEAKERMODE_5point1
    SPEAKERMODE7point1 = SPEAKERMODE_7point1
    SPEAKERMODEMax = SPEAKERMODE_max
    SPEAKERMODECOUNT = SPEAKERMODE_COUNT
    SPKNone = SPK_none
    SPKFrontleft = SPK_frontleft
    SPKFrontright = SPK_frontright
    SPKCenter = SPK_center
    SPKSub = SPK_sub
    SPKBackleft = SPK_backleft
    SPKBackright = SPK_backright
    SPKSideleft = SPK_sideleft
    SPKSideright = SPK_sideright
    SPKCOUNT = SPK_COUNT
    SMHeuristic = SM_heuristic
    SMSample = SM_sample
    SMStream = SM_stream

class AudioLoadRequest(AsyncTask):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: AudioLoadRequest) -> None: ...
    @overload
    def __init__(self, audio_manager: AudioManager, filename: str, positional: bool) -> None: ...
    def get_audio_manager(self) -> AudioManager: ...
    def get_filename(self) -> str: ...
    def get_positional(self) -> bool: ...
    def is_ready(self) -> bool: ...
    def get_sound(self) -> AudioSound: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getAudioManager = get_audio_manager
    getFilename = get_filename
    getPositional = get_positional
    isReady = is_ready
    getSound = get_sound
    getClassType = get_class_type