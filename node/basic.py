from pyglet.gl import *
import node.interfaces
import zope.interface

class TestingNode(object):
    zope.interface.implements(node.interfaces.IDrawnNode)

    def draw(self):
        # Draw a line across the frame buffer
        # Bottom left to top right
        glBegin(GL_LINES)
        glColor4f(1,1,1,1)
        glVertex3f(0,0,0)
        glColor4f(0,0,0,0)
        glVertex3f(320,240,0)

        glColor4f(0,0,0,0)
        glVertex3f(320,240,0)
        glColor4f(1,1,1,1)
        glVertex3f(640,480,0)
        glEnd()


class BasicObjectNode(object):
    zope.interface.implements(node.interfaces.IDrawnNode)
    object_to_draw = None

    def __init__(self, object_to_draw):
        self.object_to_draw = object_to_draw

    def draw(self):
        glEnable(GL_DEPTH_TEST)
        self.object_to_draw.drawer.draw(self.object_to_draw)
        glDisable(GL_DEPTH_TEST)

class NodeFactory(object):
    class_object = None
    parameters = None

    def __init__(self, class_object, parameters):
        self.class_object = class_object
        self.parameters = parameters

    def create(self):
        return self.class_object(self.parameters)

