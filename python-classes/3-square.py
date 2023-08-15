#!/usr/bin/python
"""A module for class that defines the area of a
square with size=0"""

class Square:
    """initialising the created square instance"""
    def __init__(self, size=0):
        """For initialisation of square size"""
        self.__size = size
    
    @property
    def size(self):
        """To get square size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """For setting the square size"""
        
        if not isinstance(value, int):
            """Instance must be an integer if not must be a TypeError"""
            raise TypeError("size must be an integer")
        
        elif value < 0:
            """Instance for value must be less 
            than zero if not there must be a valueError"""
            raise ValueError("size must be >= 0")
        
        else:
            self.__size = value

    def area(self):
        """public instance for the area"""
        return self.__size * self.__size