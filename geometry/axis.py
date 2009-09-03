import drawers
import glhelpers


class AxisFactory(object):
    def create(self, ortho_radius=200):
        return Axis(ortho_radius, ArrayDrawer())


class Axis(object):
    vertices = None
    colours = None
    drawer = None

    def __init__(self, ortho_radius, drawer):
        self.vertices, self.colours = self._axis(ortho_radius)
        self.drawer = drawer

    def _axis(self, d=200):
        vertices,colors=[],[]
        #XZ RED--
        vertices.extend([-d, 0,-d, d, 0,-d, d, 0, d,-d, 0, d])
        for i in range (0,4): colors.extend([1,0,0,0.5])
        #YZ GREEN--
        vertices.extend([ 0,-d,-d, 0,-d, d, 0, d, d, 0, d,-d])
        for i in range (0,4): colors.extend([0,1,0,0.5])
        #XY BLUE--
        vertices.extend([-d,-d, 0, d,-d, 0, d, d, 0,-d, d, 0])
        for i in range (0,4): colors.extend([0,0,1,0.5])
        return glhelpers.glfloat_list(vertices),glhelpers.glfloat_list(colors)
