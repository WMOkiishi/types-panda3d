from .LevelLoaderBase import LevelLoaderBase

class LevelLoader(LevelLoaderBase):
    defaultPath: str  # pyright: ignore[reportIncompatibleVariableOverride]
    def initLoader(self) -> None: ...
