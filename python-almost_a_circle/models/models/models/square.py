#!/usr/bin/python3
from models.rectangle import Rectangle

"""This module is for a square class that will inherit from the rectangle class"""

"""To import rectangle class from rectangle file"""

"""class that inherits from rectangle class"""
class Square(Rectangle):
    """Define the class square inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method to initialise the init if class square"""
        super().__init__(size, size, x, y, id)
        """Method defining super"""
    
    """Public method getter size"""
    @property
    def size(self):
        """Public getter Method defining size"""
        return self.width
        """To return size """
    
    """Public method setter for size"""
    @size.setter
    def size(self, value):
        """Method to set attributes to value"""
        self.width = value
        self.height = value
    
    def __str__(self):
        """To define the str function"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        """Return overloading square"""