# Panda3D Type Stubs

This package contains type stubs for the Python bindings of
[Panda3D](https://www.panda3d.org/), as well as for the included `direct`
package. The stubs are still in development, but should be usable with a wide
range of projects.

## How to Use the Package

Run `python -m pip install --upgrade types-panda3d` in whatever environment you
wish to install the stubs. If Panda3D is also installed, a type checker should
then know what to do with the stubs.

## How to Help

Currently, the best way to help is to test the stubs against your own Panda3D
code. Any false positives or negatives in a type checker's analysis are fair
game for a bug report. Given the size of the Panda3D library, testing on a
wide variety of codebases is really the only practical way to ensure the stubs
are useful and accurate.
