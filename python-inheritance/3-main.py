#!/usr/bin/env python3
"""This module tests 3-base_geometry file if it works correctly.
"""
BaseGeometry = __import__('3-base_geometry').BaseGeometry
"""Created an instance of the class BaseGeometry and assigned it to a variable bg.
"""
bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))
