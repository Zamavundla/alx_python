#!/usr/bin/env python3
"""This module tests the 3-square.py file.
"""
Square = __import__('3-square').Square
"""Create an instance of Square from 3-square.py.
"""
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))
"""Create an instance of square size =  3.
"""
my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))
"""Handle exceptions for size attribute.
"""
try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)