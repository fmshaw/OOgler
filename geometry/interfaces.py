import zope.interface

class IGeometryFactory(zope.interface.Interface):
    """Geometry factories take a dict of args and return geometry"""
    def create(self, args=None):
        """Make a new instance of geometry with the args supplied"""
        pass

class IGeometry(zope.interface.Interface):
    """Marker interface for geometry"""
    pass

