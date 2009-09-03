import zope.interface

class IDrawingHelper(zope.interface.Interface):
    """
    A drawing helper may be used by more than one object to apply
    the same drawing logic to a group of different objects with a
    common interface
    """
    def draw(self, object):
        """Draw object"""
        pass

class IArrayDrawer(IDrawingHelper):
    """
    An array drawer draws an object with colour and vertex arrays
    """
    def draw(self, object):
        """Draw object with vertex and colour arrays"""
        pass

