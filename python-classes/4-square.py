#!/usr/bin/python3
"""module that defines a square class"""

class Square:
    """Initialising the created square"""
    def __init__(self, size=0):
        """Iinitialising the square size"""
        self.__size = size

    @property
    def size(self):
        """For getting the size of square"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """For setting square size"""

        if not isinstance(value, int):
            """instance must be an int or be a type error"""
            raise TypeError("size must be an integer")
        
        elif value < 0:
            """Instance size must be less than 0 or valueError"""
            raise ValueError("value must be >= 0")
        
        else:
            self.__size = value

    def area(self):
            """Public instance for area of the square"""
            return self.__size * self.__size
        
    def my_print(self):
        """Public instant to print"""
        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                print("#" * self.__size)