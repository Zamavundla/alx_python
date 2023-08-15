#!/usr/bin/python3
"""A module for class Square that define its size."""

class Square:
    """Initialise the created square instance"""

    def __init__(self, size=0):
        """initialise square size with size=0"""
        if not isinstance(size, int):
            """Initialised the instance must be an integer or must have a TypeError"""
            raise TypeError("size must be an integer")
        
        elif size < 0:
            """The second instance the size must be  < 0 or have ValueError"""
            raise ValueError("size must be >= 0")
        
        else:
            self.__size = size
        