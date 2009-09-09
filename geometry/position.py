
class Position(object):
    position = ((0.0,0.0,0.0),(0.0,0.0,0.0))

    def __init__(self,displacement=(0.0,0.0,0.0),rotation=(0.0,0.0,0.0)):
        self.position = (displacement, rotation)

    def getdisplacement(self):
        return self.position[0]

    def setdisplacement(self, displacement):
        self.position = (displacement, self.position[1])

    displacement = property(getdisplacement, setdisplacement)

    def getrotation(self):
        return self.position[0]

    def setrotation(self,rotation):
        self.position = (self.position[0], rotation)

    rotation = property(getrotation, setrotation)

    def absolute_position(self, origin):
        """Here we calculate what the displacement and rotation are from
        a given origin. The idea being that the relative positions are
        the same regardless of origin"""
        return Position()

