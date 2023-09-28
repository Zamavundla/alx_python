#!/usr/bin/env python3
"""This module tests the 2-square.py file.
 """
Square = __import__('2-square').Square
"""Create an instance of Square from 2-square.py.

Args:
    size (int): size of the square.
   
   print the size of the square.
"""
my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))
"""Handle exceptions for size attribute.
"""
try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)
"""Create another instance of Square from 2-square.py.
 
Args:
    size (int): size of the square.
    
    print area of the square.

"""
my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
