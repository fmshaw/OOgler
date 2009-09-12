from pyglet.gl import *
import node.interfaces
import zope.interface

class SimpleObjectNode(object):
    zope.interface.implements(node.interfaces.IDrawnNode)
    object_to_draw = None

    def __init__(self, object_to_draw):
        self.object_to_draw = object_to_draw

    def draw(self):
        
        glEnable(GL_DEPTH_TEST)
        self.object_to_draw.drawer.draw(self.object_to_draw)
        glDisable(GL_DEPTH_TEST)

class SimpleNodeFactory(object):
    class_object = None
    parameters = None

    def __init__(self, class_object, parameters):
        self.class_object = class_object
        self.parameters = parameters

    def create(self):
        return self.class_object(self.parameters)

