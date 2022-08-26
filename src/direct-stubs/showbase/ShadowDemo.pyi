__all__ = ['ShadowCaster', 'arbitraryShadow', 'avatarShadow', 'piratesAvatarShadow']

from typing import ClassVar

from panda3d.core import Camera, GraphicsOutput, NodePath, OrthographicLens, Texture, TextureStage

sc: ShadowCaster | None

class ShadowCaster:
    texXSize: ClassVar[int]
    texYSize: ClassVar[int]
    lightPath: NodePath
    objectPath: NodePath
    groundPath: NodePath | None
    buffer: GraphicsOutput
    tex: Texture
    camera: Camera
    cameraPath: NodePath[Camera]
    lens: OrthographicLens
    stage: TextureStage
    def __init__(self, lightPath: NodePath, objectPath: NodePath, filmX: float, filmY: float) -> None: ...
    def setGround(self, groundPath: NodePath) -> None: ...
    def clear(self) -> None: ...

def avatarShadow() -> ShadowCaster: ...
def piratesAvatarShadow() -> ShadowCaster: ...
def arbitraryShadow(node: NodePath) -> ShadowCaster: ...
