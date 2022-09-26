from panda3d._typing import Filepath
from panda3d.physics import SpriteParticleRenderer

class SpriteParticleRendererExt(SpriteParticleRenderer):
    sourceTextureName: str | None
    sourceFileName: str | None
    sourceNodeName: str | None
    def getSourceTextureName(self) -> str: ...
    def setSourceTextureName(self, name: str) -> None: ...
    def setTextureFromFile(self, fileName: Filepath | None = None) -> bool: ...
    def addTextureFromFile(self, fileName: Filepath | None = None) -> bool: ...
    def getSourceFileName(self) -> str: ...
    def setSourceFileName(self, name: str) -> None: ...
    def getSourceNodeName(self) -> str: ...
    def setSourceNodeName(self, name: str) -> None: ...
    def setTextureFromNode(self, modelName: str | None = None, nodeName: str | None = None, sizeFromTexels: bool = False) -> bool: ...
    def addTextureFromNode(self, modelName: str | None = None, nodeName: str | None = None, sizeFromTexels: bool = False) -> bool: ...
