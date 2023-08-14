# This module defines a function that checks if an object is an instance of a specified
# class or its subclasses.

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class.

    :param obj: The object to be checked.
    :param a_class: The class to compare against.
    :return: True if the object is an instance of the specified class or its subclass, 
    otherwise False.
    """
    return isinstance(obj, a_class)

# Test cases
a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))

a = True
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))

a = 3.14
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))

a = True
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

a = None
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

a = None
if is_kind_of_class(a, list):
    print("{} comes from {}".format(a, list.__name__))

a = [1, 2, 3]
if is_kind_of_class(a, list):
    print("{} comes from {}".format(a, list.__name__))

a = [1, 2, 3]
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
