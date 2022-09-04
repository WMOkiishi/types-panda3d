__all__ = ['ProgressBar']

from tkinter import Canvas, Frame
from typing import Any

class ProgressBar:
    master: Any
    orientation: str
    min: int
    max: int
    width: int
    height: int
    doLabel: bool
    fillColor: str
    labelFont: str
    labelColor: str
    background: str
    labelText: str
    labelFormat: str
    value: int
    frame: Frame
    canvas: Canvas
    scale: int
    label: int
    def __init__(
        self,
        master=None,
        orientation: str = 'horizontal',
        min: int = 0,
        max: int = 100,
        width: int = 100,
        height: int = 18,
        doLabel: bool = True,
        appearance: str = 'sunken',
        fillColor: str = 'blue',
        background: str = 'gray',
        labelColor: str = 'yellow',
        labelFont: str = 'Verdana',
        labelText: str = '',
        labelFormat: str = '%d%%',
        value: int = 50,
        bd: int = 2,
    ) -> None: ...
    def updateProgress(self, newValue: int, newMax: int | None = None) -> None: ...
    def update(self) -> None: ...
