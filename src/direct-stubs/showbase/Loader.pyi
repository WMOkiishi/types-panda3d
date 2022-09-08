__all__ = ['Loader']

from collections.abc import Callable, Iterable, Sequence
from os import PathLike
from typing import Any, ClassVar, overload
from typing_extensions import Literal, Self, TypeAlias

from panda3d import core
from panda3d.core import (
    AsyncTask,
    AudioManager,
    AudioSound,
    ConfigVariableColor,
    ConfigVariableFilename,
    Filename,
    LMatrix4f,
    LoaderOptions,
    LVecBase4f,
    ModelNode,
    NodePath,
    PandaNode,
    Shader,
    TextFont,
    Texture,
    UnalignedLVecBase4f,
)
from ..directnotify.Notifier import Notifier
from .DirectObject import DirectObject

_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike
_FilterType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
_TextFont_RenderMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor

phaseChecker: Callable[[str, LoaderOptions], object] | None

class _ResultAwaiter:
    requestList: Sequence[AsyncTask]
    index: int
    def __init__(self, requestList: Sequence[AsyncTask]) -> None: ...
    def __await__(self) -> Self: ...
    def __anext__(self) -> Self: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> AsyncTask: ...

class _Callback:
    objects: list
    gotList: bool
    callback: Callable[..., object]
    extraArgs: Iterable[Any]
    requests: set[AsyncTask] | None
    requestList: list[AsyncTask] | None
    def __init__(
        self,
        loader: Loader,
        numObjects: int,
        gotList: bool,
        callback: Callable[..., object],
        extraArgs: Iterable[Any],
    ) -> None: ...
    def gotObject(self, index: int, object) -> None: ...
    def cancel(self) -> None: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def result(self) -> list[Any] | Any: ...
    def exception(self) -> None: ...
    def __await__(self) -> _ResultAwaiter: ...
    def __aiter__(self) -> _ResultAwaiter: ...

class Loader(DirectObject):
    notify: ClassVar[Notifier]
    loaderIndex: ClassVar[int]
    base = ...
    loader: core.Loader
    hook: str
    def __init__(self, base) -> None: ...
    def destroy(self) -> None: ...
    @overload
    def load_model(
        self,
        modelPath: str,
        loaderOptions: LoaderOptions | None = None,
        noCache: bool | None = None,
        allowInstance: bool = False,
        okMissing: bool | None = None,
        callback: None = None,
        extraArgs: Iterable[Any] = ...,
        priority: float | None = None,
        blocking: Literal[True] | None = None,
    ) -> NodePath | None: ...
    @overload
    def load_model(
        self,
        modelPath: list[str] | set[str] | tuple[str, ...],
        loaderOptions: LoaderOptions | None = None,
        noCache: bool | None = None,
        allowInstance: bool = False,
        okMissing: bool | None = None,
        callback: None = None,
        extraArgs: Iterable[Any] = ...,
        priority: float | None = None,
        blocking: Literal[True] | None = None,
    ) -> list[NodePath | None]: ...
    @overload
    def load_model(
        self,
        modelPath: str | list[str] | set[str] | tuple[str, ...],
        loaderOptions: LoaderOptions | None = None,
        noCache: bool | None = None,
        allowInstance: bool = False,
        okMissing: bool | None = None,
        callback: Callable[..., object] = ...,
        extraArgs: Iterable[Any] = ...,
        priority: float | None = None,
        blocking: Literal[False] | None = None,
    ) -> _Callback: ...
    def cancelRequest(self, cb: _Callback) -> None: ...
    def isRequestPending(self, cb: _Callback) -> bool: ...
    def loadModelOnce(self, modelPath: str) -> NodePath | None: ...
    def loadModelCopy(self, modelPath: str, loaderOptions: LoaderOptions | None = None) -> NodePath | None: ...
    def loadModelNode(self, modelPath: str) -> PandaNode | None: ...
    def unload_model(self, model: NodePath | ModelNode | Filename | str) -> None: ...
    @overload
    def save_model(
        self,
        modelPath: str,
        node: NodePath | PandaNode,
        loaderOptions: LoaderOptions | None = None,
        callback: None = None,
        extraArgs: Iterable[Any] = ...,
        priority: int | None = None,
        blocking: Literal[True] | None = None,
    ) -> bool: ...
    @overload
    def save_model(
        self,
        modelPath: list[str] | set[str] | tuple[str, ...],
        node: NodePath | PandaNode,
        loaderOptions: LoaderOptions | None = None,
        callback: None = None,
        extraArgs: Iterable[Any] = ...,
        priority: int | None = None,
        blocking: bool | None = None,
    ) -> list[bool]: ...
    @overload
    def save_model(
        self,
        modelPath: str | list[str] | set[str] | tuple[str, ...],
        node: NodePath | PandaNode,
        loaderOptions: LoaderOptions | None = None,
        callback: Callable[..., object] = ...,
        extraArgs: Iterable[Any] = ...,
        priority: int | None = None,
        blocking: Literal[False] | None = None,
    ) -> _Callback: ...
    def load_font(
        self,
        modelPath: str,
        spaceAdvance: float | None = None,
        lineHeight: float | None = None,
        pointSize: float | None = None,
        pixelsPerUnit: float | None = None,
        scaleFactor: float | None = None,
        textureMargin: int | None = None,
        polyMargin: float | None = None,
        minFilter: _FilterType | None = None,
        magFilter: _FilterType | None = None,
        anisotropicDegree: int | None = None,
        color: _Vec4f | None = None,
        outlineWidth: float | None = None,
        outlineFeather: float = 0.1,
        outlineColor: _Vec4f = ...,
        renderMode: _TextFont_RenderMode | None = None,
        okMissing: bool = False,
    ) -> TextFont: ...
    def load_texture(
        self,
        texturePath: _Filename,
        alphaPath: _Filename | None = None,
        readMipmaps: bool = False,
        okMissing: bool = False,
        minfilter: _FilterType | None = None,
        magfilter: _FilterType | None = None,
        anisotropicDegree: int | None = None,
        loaderOptions: LoaderOptions | None = None,
        multiview: bool | None = None,
    ) -> Texture: ...
    def load_3d_texture(
        self,
        texturePattern: _Filename,
        readMipmaps: bool = False,
        okMissing: bool = False,
        minfilter: _FilterType | None = None,
        magfilter: _FilterType | None = None,
        anisotropicDegree: int | None = None,
        loaderOptions: LoaderOptions | None = None,
        multiview: bool | None = None,
        numViews: int = 2,
    ) -> Texture: ...
    def load2DTextureArray(
        self,
        texturePattern: _Filename,
        readMipmaps: bool = False,
        okMissing: bool = False,
        minfilter: _FilterType | None = None,
        magfilter: _FilterType | None = None,
        anisotropicDegree: int | None = None,
        loaderOptions: LoaderOptions | None = None,
        multiview: bool | None = None,
        numViews: int = 2,
    ) -> Texture: ...
    def load_cube_map(
        self,
        texturePattern: _Filename,
        readMipmaps: bool = False,
        okMissing: bool = False,
        minfilter: _FilterType | None = None,
        magfilter: _FilterType | None = None,
        anisotropicDegree: int | None = None,
        loaderOptions: LoaderOptions | None = None,
        multiview: bool | None = None,
        numViews: int = 2,
    ) -> Texture: ...
    def unload_texture(self, texture: Texture) -> None: ...
    def load_sfx(
        self,
        soundPath: _Filename | list[_Filename] | set[_Filename] | tuple[_Filename, ...],
        positional: bool = False,
        callback: Callable[..., object] | None = None,
        extraArgs: Iterable[Any] = ...,
    ) -> _Callback | None: ...
    def load_music(
        self,
        soundPath: _Filename | list[_Filename] | set[_Filename] | tuple[_Filename, ...],
        positional: bool = False,
        callback: Callable[..., object] | None = None,
        extraArgs: Iterable[Any] = ...,
    ) -> _Callback | None: ...
    def load_sound(
        self,
        manager: AudioManager,
        soundPath: _Filename | list[_Filename] | set[_Filename] | tuple[_Filename, ...],
        positional: bool = False,
        callback: Callable[..., object] | None = None,
        extraArgs: Iterable[Any] = ...,
    ) -> _Callback: ...
    def unloadSfx(self, sfx: AudioSound) -> None: ...
    def load_shader(self, shaderPath: _Filename, okMissing: bool = False) -> Shader: ...
    def unload_shader(self, shaderPath: _Filename | None) -> None: ...
    def async_flatten_strong(
        self,
        model: NodePath | Iterable[NodePath],
        inPlace: bool = True,
        callback: Callable[..., object] | None = None,
        extraArgs: Iterable[Any] = ...,
    ) -> _Callback: ...
    loadModel = load_model
    unloadModel = unload_model
    saveModel = save_model
    loadFont = load_font
    loadTexture = load_texture
    load3DTexture = load_3d_texture
    loadCubeMap = load_cube_map
    unloadTexture = unload_texture
    loadSfx = load_sfx
    loadShader = load_shader
    unloadShader = unload_shader
    asyncFlattenStrong = async_flatten_strong