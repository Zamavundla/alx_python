#!/usr/bin/python3
"""module for the Base class"""

class Base:
    """This is the base class which will be referenced throught the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is a class constructor which initialises id"""
        if id is not None:
            """public instance attribute with id as argument value"""
            self.id = id

        else:
            Base.__nb_objects += 1
            """To assign new value to the public instance attribute and increment it by 1"""

            self.id = Base.__nb_objects