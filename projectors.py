import pyglet.gl

class ProjectionMethod(object):
    def __init__(self, viewport):
        self.viewport = viewport

class IsometricProjection(ProjectionMethod):
    def set_projection(self):
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glOrtho(-self.viewport.w/2.,self.viewport.w/2.,-self.viewport.h/2.,self.viewport.h/2.,0,self.viewport.far)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

class PerspectiveProjection(ProjectionMethod):
    def set_projection(self):
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.gluPerspective(self.viewport.fov, float(self.viewport.w)/self.viewport.h, 0.1, self.viewport.far)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

DefaultProjection = IsometricProjection
