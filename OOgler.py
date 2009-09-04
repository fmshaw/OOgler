"""
This is the main module for launching the OOgler

Here we are just testing that the scene root can be instansiated.

>>> root = scene.root.SceneRoot()
>>> root #doctest:+ELLIPSIS
<scene.root.SceneRoot object at 0x...>
"""
import scene.root

root = scene.root.SceneRoot()
root.main_loop()

