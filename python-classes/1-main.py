#!/usr/bin/python3
"""this module tests 1-square.py.
"""
Square = __import__('1-square').Square
"""Create an instance of the class Square.

Args:
    size (int): size of the square.
   
   Prints the type of the instance.
"""
my_square_1 = Square(3)

print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)
"""Raises an exception.
   
   if size is not an integer.
   
   Raises:
   
   ValueError: if size is less than 0.
   
   
"""
try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)
