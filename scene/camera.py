from pyglet import window
from pyglet.window import key
from pyglet.gl import *
import projectors

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
            print "Projection: Default"
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


