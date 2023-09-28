#!/usr/bin/env python3
"""This module tests 0-is_same_class file if it works correctly.
 """
is_same_class = __import__('0-is_same_class').is_same_class
"""Created an instance of the class int and assigned it to a variable a.
"""
a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
