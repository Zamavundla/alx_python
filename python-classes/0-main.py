#!/usr/bin/env python3
"""Square class with a private attribute - size.
    Args:
         size (int): size of the square.
    
    Raises:
           TypeError: if size is not an integer.
    
    Attributes: 
               size (int): size of the square.
"""
Square = __import__('0-square').Square
my_square = Square(3)
"""Print the type square size.
"""
print(type(my_square))

print(my_square.__dict__)
"""Handle the exception TypeError.
"""
try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
