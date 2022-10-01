__all__ = ['ParticlePanel']

from tkinter import Checkbutton, Entry, Frame, IntVar, Menu, Menubutton, Misc, Radiobutton, StringVar, Variable
from typing import Any, SupportsInt
from typing_extensions import Literal, TypeAlias

from direct.particles.ParticleEffect import ParticleEffect
from direct.tkwidgets.AppShell import AppShell
from direct.tkwidgets.Dial import AngleDial
from direct.tkwidgets.Floater import Floater
from direct.tkwidgets.Slider import Slider
from direct.tkwidgets.VectorWidgets import ColorEntry, Vector2Entry, Vector3Entry

Pmw: Any

_TkAnchor: TypeAlias = Literal['nw', 'n', 'ne', 'w', 'center', 'e', 'sw', 's', 'se']
_TkFill: TypeAlias = Literal['none', 'x', 'y', 'both']
_TkRelief: TypeAlias = Literal['raised', 'sunken', 'flat', 'ridge', 'solid', 'groove']
_TkSide: TypeAlias = Literal['left', 'right', 'top', 'bottom']
_TkState: TypeAlias = Literal['normal', 'active', 'disabled']

class ParticlePanel(AppShell):
    particleEffect: ParticleEffect
    effectsDict: dict[str, ParticleEffect]
    forcePagesDict: dict
    particleMgrActive: IntVar
    effectsLabel: Menubutton
    effectsLabelMenu: Menu
    effectsEnableMenu: Menu
    particlesLabel: Menubutton
    particlesLabelMenu: Menu
    particlesEnableMenu: Menu
    forceGroupLabel: Menubutton
    forceGroupLabelMenu: Menu
    forceGroupEnableMenu: Menu
    mainNotebook: Pmw.NoteBook
    factoryNotebook: Pmw.NoteBook
    emissionType: IntVar
    emitterNotebook: Pmw.NoteBook
    ringCustomFrame: Frame
    rendererNotebook: Pmw.NoteBook
    rendererGeomNode: StringVar
    rendererGeomNodeEntry: Entry
    rendererGeomSegmentFrame = ...
    rendererSegmentWidgetList: list
    rendererSpriteAnimationFrame = ...
    rendererSpriteAnimationWidgetList: list
    rendererSpriteTexture: StringVar
    rendererSpriteFile: StringVar
    rendererSpriteNode: StringVar
    rendererSpriteSegmentFrame = ...
    addForceButton: Menubutton
    sf: Pmw.ScrolledFrame
    forceFrame = ...
    forceGroupNotebook: Pmw.NoteBook
    def __init__(self, particleEffect: ParticleEffect | None = None, **kw) -> None: ...
    def createCheckbutton(
        self,
        parent: Misc | None,
        category: str,
        text: str,
        balloonHelp,
        command,
        initialState,
        side: _TkSide = 'top'
    ) -> Checkbutton: ...
    def createRadiobutton(
        self,
        parent: Misc | None,
        side: _TkSide,
        category: str,
        text: str,
        balloonHelp,
        variable: Variable | Literal[''],
        value,
        command,
    ) -> Radiobutton: ...
    def createFloaters(self, parent, widgetDefinitions) -> list[Floater]: ...
    def createFloater(
        self,
        parent,
        category: str,
        text: str,
        balloonHelp,
        command=None,
        min: float = ...,
        max: float | None = None,
        resolution: float | None = None,
        numDigits: int | None = None,
        **kw,
    ) -> Floater: ...
    def createAngleDial(self, parent, category: str, text: str, balloonHelp, command=None, **kw) -> AngleDial: ...
    def createSlider(
        self,
        parent,
        category: str,
        text: str,
        balloonHelp,
        command=None,
        min: float = ...,
        max: float = ...,
        resolution: float = ...,
        **kw,
    ) -> Slider: ...
    def createVector2Entry(self, parent, category: str, text: str, balloonHelp, command=None, **kw) -> Vector2Entry: ...
    def createVector3Entry(self, parent, category: str, text: str, balloonHelp, command=None, **kw) -> Vector3Entry: ...
    def createColorEntry(self, parent, category: str, text: str, balloonHelp, command=None, **kw) -> ColorEntry: ...
    def createOptionMenu(self, parent, category: str, text: str, balloonHelp, items, command) -> StringVar: ...
    def createComboBox(self, parent, category: str, text: str, balloonHelp, items, command, history: int = ...) -> Pmw.ComboBox: ...
    def updateMenusAndLabels(self) -> None: ...
    def updateLabels(self) -> None: ...
    def updateMenus(self) -> None: ...
    def updateEffectsMenus(self) -> None: ...
    def updateParticlesMenus(self) -> None: ...
    def updateForceGroupMenus(self) -> None: ...
    def selectEffectNamed(self, name: str) -> None: ...
    def toggleEffect(self, effect, var) -> None: ...
    def selectParticlesNamed(self, name: str) -> None: ...
    def toggleParticles(self, particles, var) -> None: ...
    def selectForceGroupNamed(self, name: str) -> None: ...
    def toggleForceGroup(self, forceGroup, var) -> None: ...
    def toggleForce(self, force, pageName: str, variableName: str) -> None: ...
    def getWidget(self, category: str, text: str) -> Any: ...
    def getVariable(self, category: str, text: str) -> Any: ...
    def loadParticleEffectFromFile(self) -> None: ...
    def saveParticleEffectToFile(self) -> None: ...
    def toggleParticleMgr(self) -> None: ...
    def updateInfo(self, page: Literal['System', 'Factory', 'Emitter', 'Renderer', 'Force'] = ...) -> None: ...
    def toggleParticleEffect(self) -> None: ...
    def updateSystemWidgets(self) -> None: ...
    def setSystemPoolSize(self, value: SupportsInt) -> None: ...
    def setSystemBirthRate(self, value) -> None: ...
    def setSystemLitterSize(self, value: SupportsInt) -> None: ...
    def setSystemLitterSpread(self, value: SupportsInt) -> None: ...
    def setSystemLifespan(self, value) -> None: ...
    def toggleSystemLocalVelocity(self) -> None: ...
    def toggleSystemGrowsOlder(self) -> None: ...
    def setSystemPos(self, pos) -> None: ...
    def setSystemHpr(self, pos) -> None: ...
    def selectFactoryType(self, type) -> None: ...
    def selectFactoryPage(self) -> None: ...
    def updateFactoryWidgets(self) -> None: ...
    def setFactoryLifeSpan(self, value) -> None: ...
    def setFactoryLifeSpanSpread(self, value) -> None: ...
    def setFactoryParticleMass(self, value) -> None: ...
    def setFactoryParticleMassSpread(self, value) -> None: ...
    def setFactoryTerminalVelocity(self, value) -> None: ...
    def setFactoryTerminalVelocitySpread(self, value) -> None: ...
    def setFactoryZSpinInitialAngle(self, angle) -> None: ...
    def setFactoryZSpinInitialAngleSpread(self, spread) -> None: ...
    def setFactoryZSpinFinalAngle(self, angle) -> None: ...
    def setFactoryZSpinFinalAngleSpread(self, spread) -> None: ...
    def setFactoryZSpinAngularVelocity(self, vel) -> None: ...
    def setFactoryZSpinAngularVelocitySpread(self, spread) -> None: ...
    def selectEmitterType(self, type) -> None: ...
    def selectEmitterPage(self) -> None: ...
    def updateEmitterWidgets(self) -> None: ...
    def setEmissionType(self, newType: int | None = None) -> None: ...
    def setEmitterAmplitude(self, value) -> None: ...
    def setEmitterAmplitudeSpread(self, value) -> None: ...
    def setEmitterOffsetForce(self, vec) -> None: ...
    def setEmitterRadiateOrigin(self, origin) -> None: ...
    def setEmitterExplicitLaunchVector(self, vec) -> None: ...
    def setEmitterBoxPoint1(self, point) -> None: ...
    def setEmitterBoxPoint2(self, point) -> None: ...
    def setEmitterDiscRadius(self, radius) -> None: ...
    def setEmitterDiscInnerAngle(self, angle) -> None: ...
    def setEmitterDiscInnerVelocity(self, velocity) -> None: ...
    def setEmitterDiscOuterAngle(self, angle) -> None: ...
    def setEmitterDiscOuterVelocity(self, velocity) -> None: ...
    def toggleEmitterDiscCubicLerping(self) -> None: ...
    def setEmitterLinePoint1(self, point) -> None: ...
    def setEmitterLinePoint2(self, point) -> None: ...
    def setEmitterPointPosition(self, pos) -> None: ...
    def setEmitterRectanglePoint1(self, point) -> None: ...
    def setEmitterRectanglePoint2(self, point) -> None: ...
    def setEmitterRingRadius(self, radius) -> None: ...
    def setEmitterRingRadiusSpread(self, radiusSpread) -> None: ...
    def setEmitterRingLaunchAngle(self, angle) -> None: ...
    def setEmitterSphereSurfaceRadius(self, radius) -> None: ...
    def setEmitterSphereVolumeRadius(self, radius) -> None: ...
    def setEmitterTangentRingRadius(self, radius) -> None: ...
    def setEmitterTangentRingRadiusSpread(self, radiusSpread) -> None: ...
    def selectRendererType(self, type) -> None: ...
    def updateRendererWidgets(self) -> None: ...
    def selectRendererPage(self) -> None: ...
    def setRendererAlphaMode(self, alphaMode: Literal['NO_ALPHA', 'ALPHA_OUT', 'ALPHA_IN', 'ALPHA_IN_OUT', 'ALPHA_USER']) -> None: ...
    def setRendererUserAlpha(self, alpha) -> None: ...
    def setRendererLineHeadColor(self, color) -> None: ...
    def setRendererLineTailColor(self, color) -> None: ...
    def setRendererLineScaleFactor(self, sf) -> None: ...
    def setRendererGeomNode(self, event) -> None: ...
    def setRendererPointSize(self, size) -> None: ...
    def setRendererPointStartColor(self, color) -> None: ...
    def setRendererPointEndColor(self, color) -> None: ...
    def rendererPointSelectBlendType(self, blendType: Literal['PP_ONE_COLOR', 'PP_BLEND_LIFE', 'PP_BLEND_VEL']) -> None: ...
    def rendererPointSelectBlendMethod(self, blendMethod: Literal['PP_NO_BLEND', 'PP_BLEND_LINEAR', 'PP_BLEND_CUBIC']) -> None: ...
    def setRendererSparkleCenterColor(self, color) -> None: ...
    def setRendererSparkleEdgeColor(self, color) -> None: ...
    def setRendererSparkleBirthRadius(self, radius) -> None: ...
    def setRendererSparkleDeathRadius(self, radius) -> None: ...
    def setRendererSparkleLifeScale(self, lifeScaleMethod: str) -> None: ...
    def setSpriteSourceType(self) -> None: ...
    def setRendererSpriteAnimationFrameRate(self, rate) -> None: ...
    def setRendererSpriteAnimationEnable(self) -> None: ...
    def addRendererSpriteAnimationTexture(self) -> None: ...
    def addRendererSpriteAnimationFromNode(self) -> None: ...
    def toggleRendererSpriteXScale(self) -> None: ...
    def toggleRendererSpriteYScale(self) -> None: ...
    def toggleRendererSpriteAnimAngle(self) -> None: ...
    def toggleAngularVelocity(self) -> None: ...
    def setRendererSpriteInitialXScale(self, xScale) -> None: ...
    def setRendererSpriteFinalXScale(self, xScale) -> None: ...
    def setRendererSpriteInitialYScale(self, yScale) -> None: ...
    def setRendererSpriteFinalYScale(self, yScale) -> None: ...
    def setRendererSpriteNonAnimatedTheta(self, theta) -> None: ...
    def setRendererSpriteBlendMethod(self, blendMethod: str) -> None: ...
    def toggleRendererSpriteAlphaDisable(self) -> None: ...
    def setRendererColorBlendAttrib(self, rendererName: str, blendMethodStr: str, incomingOperandStr: str, fbufferOperandStr: str) -> None: ...
    def setRendererSpriteColorBlendMethod(self, blendMethod: str) -> None: ...
    def setRendererSpriteColorBlendIncomingOperand(self, operand: str) -> None: ...
    def setRendererSpriteColorBlendFbufferOperand(self, operand: str) -> None: ...
    def toggleRendererGeomXScale(self) -> None: ...
    def toggleRendererGeomYScale(self) -> None: ...
    def toggleRendererGeomZScale(self) -> None: ...
    def setRendererGeomInitialXScale(self, xScale) -> None: ...
    def setRendererGeomFinalXScale(self, xScale) -> None: ...
    def setRendererGeomInitialYScale(self, yScale) -> None: ...
    def setRendererGeomFinalYScale(self, yScale) -> None: ...
    def setRendererGeomInitialZScale(self, zScale) -> None: ...
    def setRendererGeomFinalZScale(self, zScale) -> None: ...
    def setRendererGeomColorBlendMethod(self, blendMethod: str) -> None: ...
    def setRendererGeomColorBlendIncomingOperand(self, operand: str) -> None: ...
    def setRendererGeomColorBlendFbufferOperand(self, operand: str) -> None: ...
    def addConstantInterpolationSegment(self, id=None) -> None: ...
    def addLinearInterpolationSegment(self, id=None) -> None: ...
    def addStepwaveInterpolationSegment(self, id=None) -> None: ...
    def addSinusoidInterpolationSegment(self, id=None) -> None: ...
    def createWidgetForExistingInterpolationSegment(self, id) -> None: ...
    def createInterpolationSegmentFrame(self, parent, segName: str, seg) -> Frame: ...
    def createConstantInterpolationSegmentWidget(self, parent, segName: str, segment) -> Frame: ...
    def createLinearInterpolationSegmentWidget(self, parent, segName: str, segment) -> Frame: ...
    def createStepwaveInterpolationSegmentWidget(self, parent, segName: str, segment) -> Frame: ...
    def createSinusoidInterpolationSegmentWidget(self, parent, segName: str, segment) -> Frame: ...
    def createSpriteAnimationFrame(self, parent, anim, animName: str) -> Frame: ...
    def createSpriteAnimationTextureWidget(self, parent, anim, animName: str) -> Frame: ...
    def createSpriteAnimationNodeWidget(self, parent, anim, animName: str) -> Frame: ...
    def readSpriteRendererAnimations(self) -> None: ...
    def writeSpriteRendererAnimations(self) -> None: ...
    def updateForceWidgets(self) -> None: ...
    def addLinearVectorForce(self) -> None: ...
    def addLinearFrictionForce(self) -> None: ...
    def addLinearJitterForce(self) -> None: ...
    def addLinearNoiseForce(self) -> None: ...
    def addLinearSinkForce(self) -> None: ...
    def addLinearSourceForce(self) -> None: ...
    def addLinearCylinderVortexForce(self) -> None: ...
    def addLinearUserDefinedForce(self) -> None: ...
    def addForce(self, f) -> None: ...
    def createNewEffect(self) -> None: ...
    def createNewParticles(self) -> None: ...
    def createNewForceGroup(self) -> None: ...
    def addForceGroupNotebookPage(self, particleEffect, forceGroup) -> None: ...
    def addForceWidget(self, forceGroup, force) -> None: ...
    def createForceFrame(self, forcePage, forceName, force): ...
    def createLinearForceWidgets(self, frame, pageName: str, forceName: str, force) -> None: ...
    def createForceActiveWidget(self, frame, pageName: str, forceName: str, force) -> None: ...
    def createLinearVectorForceWidget(self, forcePage, pageName: str, count: int, force) -> None: ...
    def createLinearRandomForceWidget(self, forcePage, pageName: str, count: int, force, type) -> None: ...
    def createLinearFrictionForceWidget(self, forcePage, pageName: str, count: int, force) -> None: ...
    def createLinearCylinderVortexForceWidget(self, forcePage, pageName: str, count: int, force) -> None: ...
    def createLinearDistanceForceWidget(self, forcePage, pageName: str, count: int, force, type) -> None: ...
