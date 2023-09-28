#!/usr/bin/env python3
"""This module tests 2-inherits_from file if it works correctly.
"""
inherits_from = __import__('2-inherits_from').inherits_from
"""Created an instance of the class int and assigned it to a variable a.
"""
a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
