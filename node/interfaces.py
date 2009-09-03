import zope.interface

class IDrawnNode(zope.interface.Interface):
    """These nodes need to be drawn"""
    def draw(self):
        """Draw this node here"""
        pass

