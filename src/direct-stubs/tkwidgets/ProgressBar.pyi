__all__ = ['ProgressBar']

import tkinter
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
    frame: tkinter.Frame
    canvas: tkinter.Canvas
    scale: int
    label: int
    def __init__(
        self,
        master=...,
        orientation: str = ...,
        min: int = ...,
        max: int = ...,
        width: int = ...,
        height: int = ...,
        doLabel: bool = ...,
        appearance: str = ...,
        fillColor: str = ...,
        background: str = ...,
        labelColor: str = ...,
        labelFont: str = ...,
        labelText: str = ...,
        labelFormat: str = ...,
        value: int = ...,
        bd: int = ...,
    ) -> None: ...
    def updateProgress(self, newValue: int, newMax: int | None = ...) -> None: ...
    def update(self) -> None: ...
