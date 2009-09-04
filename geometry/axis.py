import zope.interface
import zope.component
import geometry.interfaces
import drawer.basic
import glhelpers


class AxisFactory(object):
    zope.interface.implements(geometry.interfaces.IGeometryFactory)
    def create(self, args={}):
        ortho_radius = 200
        if 'ortho_radius' in args:
            ortho_radius = args['ortho_radius']
        gsm = zope.component.getGlobalSiteManager()
        array_drawer = gsm.getUtility(
            drawer.interfaces.IArrayDrawer,
            name='ArrayDrawer')
        return Axis(ortho_radius, array_drawer)


class Axis(object):
    zope.interface.implements(geometry.interfaces.IGeometry)
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

gsm = zope.component.getGlobalSiteManager()
gsm.registerUtility(factory=AxisFactory, name='Axis')
del gsm
