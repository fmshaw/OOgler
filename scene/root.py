import zope.component
from pyglet import window
from pyglet.gl import *
import geometry.axis
import node.basic
import scene.camera

class SetupHelper(object):
    def opengl_init(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glDepthFunc(GL_LEQUAL)


class SceneRoot(object):
    nodes = []

    def __init__(self):
        axis_factory = geometry.axis.AxisFactory()
        axis = axis_factory.create()
        self.nodes.append(node.basic.BasicObjectNode(axis))

        self.cam=scene.camera.Camera()

        self.win = window.Window(resizable=True)
        self.win.on_resize=self.cam.view
        self.win.on_key_press=self.cam.key
        self.win.on_mouse_drag=self.cam.drag

        SetupHelper().opengl_init()

        self.nodes.append(node.basic.TestingNode())

    def main_loop(self):
        SetupHelper().opengl_init()
        while not self.win.has_exit:
            self.win.dispatch_events()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.cam.apply()
            for node in self.nodes:
                node.draw()
            self.win.flip()
