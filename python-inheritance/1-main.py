#!/usr/bin/env python3
"""This module tests 1-is_kind_of_class file if it works correctly.
"""
is_kind_of_class = __import__('1-is_kind_of_class').is_kind_of_class
"""Created an instance of the class int and assigned it to a variable a.
"""
a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
