import drawer.interfaces
import zope.interface
import zope.component
from pyglet.gl import *


class ArrayDrawer(object):
    zope.interface.implements(drawer.interfaces.IArrayDrawer)
    def draw(self, scene_object):
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(4, GL_FLOAT, 0, scene_object.colours)
        glVertexPointer(3, GL_FLOAT, 0, scene_object.vertices)
        glDrawArrays(GL_QUADS, 0, len(scene_object.vertices)/3)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)

components = zope.component.registry.Components('OOgler')
components.registerUtility(factory=ArrayDrawer, name='ArrayDrawer')
del components
