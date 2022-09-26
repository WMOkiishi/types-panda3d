from .LevelLoaderBase import LevelLoaderBase

class LevelLoader(LevelLoaderBase):
    defaultPath: str
    def initLoader(self) -> None: ...
