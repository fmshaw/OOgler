import geometry.euclid

class Position(object):

    def __init__(self,
                 displacement=geometry.euclid.Vector3(0.0,0.0,0.0),
                 rotation=geometry.euclid.Vector3(0.0,0.0,0.0)):
        self.position = (displacement, rotation)

    def getdisplacement(self):
        return self.position[0]

    def setdisplacement(self, displacement):
        self.position = (displacement, self.position[0])

    displacement = property(getdisplacement, setdisplacement)

    def getrotation(self):
        return self.position[1]

    def setrotation(self,rotation):
        self.position = (self.position[1], rotation)

    rotation = property(getrotation, setrotation)

    def absolute_position(self, origin):
        """Here we calculate what the displacement and rotation are from
        a given origin. The idea being that the relative positions are
        the same for different origins, the absolute position differs
        for different origins"""
        # Unpack parents rotation values for the euler rotation
        heading, attitude, bank = origin.rotation
        # Make a euler matrix
        orientation = geometry.euclid.Matrix4.new_rotate_euler(heading,
                                                               attitude,
                                                               bank)
        # Transform our displacement by the matrix
        relative_displacement = orientation * self.displacement
        # Add our reoriented displacement
        absolute_displacement = origin.displacement + relative_displacement
        absolute_rotation = origin.rotation + self.rotation
        return Position(absolute_displacement, absolute_rotation)

