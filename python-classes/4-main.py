#!/usr/bin/env python3
"""This module instantiates an object of the class Square.
   Prints in stdout the square with the character #.
"""
Square = __import__('4-square').Square
"""Create an instance my_square of class Square, size = 3.
"""
my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")
