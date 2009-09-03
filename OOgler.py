from pyglet import window,image
from pyglet.window import key
from pyglet.gl import *
import glhelpers
import projectors
import geometry.axis

class SetupHelper(object):
    def opengl_init(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glDepthFunc(GL_LEQUAL)

class TestingLineDrawer(object):
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


class ViewportParameters(object):
    w,h=640,480
    far=8192
    fov=60
    mode=1


class Camera(object):
    x,y,z=0,0,512
    rx,ry,rz=30,-45,0
    viewport = ViewportParameters()
    projection_method=None

    def view(self,width,height):
        self.viewport.w,self.viewport.h=width,height
        glViewport(0, 0, width, height)
        print "Viewport "+str(width)+"x"+str(height)
        if self.viewport.mode==2: self.isometric()
        elif self.viewport.mode==3: self.perspective()
        else: self.default()

    def default(self):
        self.projection_method=projectors.DefaultProjection(self.viewport)
        self._set_projection()

    def isometric(self):
        self.projection_method=projectors.IsometricProjection(self.viewport)
        self._set_projection()

    def perspective(self):
        self.projection_method=projectors.PerspectiveProjection(self.viewport)
        self._set_projection()

    def _set_projection(self):
        self.projection_method.set_projection()

    def key(self, symbol, modifiers):
        if symbol==key.F1:
            self.viewport.mode=1
            self.default()
            print "Projection: Pyglet default"
        elif symbol==key.F2:
            print "Projection: 3D Isometric"
            self.viewport.mode=2
            self.isometric()
        elif symbol==key.F3:
            print "Projection: 3D Perspective"
            self.viewport.mode=3
            self.perspective()
        elif self.viewport.mode==3 and symbol==key.NUM_SUBTRACT:
            self.viewport.fov-=1
            self.perspective()
        elif self.viewport.mode==3 and symbol==key.NUM_ADD:
            self.viewport.fov+=1
            self.perspective()
        else: print "KEY "+key.symbol_string(symbol)

    def drag(self, x, y, dx, dy, button, modifiers):
        if button==1:
            self.x-=dx*2
            self.y-=dy*2
        elif button==2:
            self.x-=dx*2
            self.z-=dy*2
        elif button==4:
            self.ry+=dx/4.
            self.rx-=dy/4.

    def apply(self):
        glLoadIdentity()
        if self.viewport.mode==1: return
        glTranslatef(-self.x,-self.y,-self.z)
        glRotatef(self.rx,1,0,0)
        glRotatef(self.ry,0,1,0)
        glRotatef(self.rz,0,0,1)

class ArrayDrawer(object):
    def draw(self, scene_object, mode=GL_LINES):
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(4, GL_FLOAT, 0, scene_object.colours)
        glVertexPointer(3, GL_FLOAT, 0, scene_object.vertices)
        glDrawArrays(GL_QUADS, 0, len(scene_object.vertices)/3)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)


#class AxisFactory(object):
#    def create(self, ortho_radius=200):
#        return Axis(ortho_radius, ArrayDrawer())


#class Axis(object):
#    vertices = None
#    colours = None
#    drawer = None
#
#    def __init__(self, ortho_radius, drawer):
#        self.vertices, self.colours = self._axis(ortho_radius)
#        self.drawer = drawer
#
#    def _axis(self, d=200):
#        vertices,colors=[],[]
#        #XZ RED--
#        vertices.extend([-d, 0,-d, d, 0,-d, d, 0, d,-d, 0, d])
#        for i in range (0,4): colors.extend([1,0,0,0.5])
#        #YZ GREEN--
#        vertices.extend([ 0,-d,-d, 0,-d, d, 0, d, d, 0, d,-d])
#        for i in range (0,4): colors.extend([0,1,0,0.5])
#        #XY BLUE--
#        vertices.extend([-d,-d, 0, d,-d, 0, d, d, 0,-d, d, 0])
#        for i in range (0,4): colors.extend([0,0,1,0.5])
#        return glhelpers.glfloat_list(vertices),glhelpers.glfloat_list(colors)


class ObjectDrawer(object):
    object_to_draw = None

    def __init__(self, object_to_draw):
        self.object_to_draw = object_to_draw

    def draw(self):
        glEnable(GL_DEPTH_TEST)
        self.object_to_draw.drawer.draw(self.object_to_draw)
        glDisable(GL_DEPTH_TEST)

drawers = []

axis_factory = geometry.axis.AxisFactory()
axis = axis_factory.create()
drawers.append(ObjectDrawer(axis))

cam=Camera()

win = window.Window(resizable=True)
win.on_resize=cam.view
win.on_key_press=cam.key
win.on_mouse_drag=cam.drag

SetupHelper().opengl_init()

drawers.append(TestingLineDrawer())

while not win.has_exit:
    win.dispatch_events()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cam.apply()
    for drawer in drawers:
        drawer.draw()
    win.flip()
