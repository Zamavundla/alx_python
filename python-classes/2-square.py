#!/usr/bin/python3
"""This a module of a class, that defines a class with size =0 and an area of the
square, the instance must have an exception"""

class Square:
    """initialise the created square instance"""
    def __init__(self, size=0):
        """To initialise the square size."""
        if not isinstance(size, int):
            """The instance must be an integer if not there must be a TypeError"""
            raise TypeError("size must be an integer")
        
        elif size < 0:
            """The instance for size must be < 0 or have ValueError"""
            raise ValueError("size must be >=0")
        
        else:
            self.__size = size
    
    def area(self):
        """public instance for area"""
        return self.__size * self.__size