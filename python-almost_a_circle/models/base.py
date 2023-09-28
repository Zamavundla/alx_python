"""This Class implements the base of all other classes in this project.
"""
class Base:
    """Base class.
    """
    __nb_objects = 0
    """Private attr instanciation.
    """
    def __init__(self, id=None):
        """init method."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects