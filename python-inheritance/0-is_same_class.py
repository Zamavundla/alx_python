"""This module will return True if the object is an instance of 
a specified class either False"""
def is_same_class(obj, a_class):
    """A prototype for instance, which defines an object and a class"""
    
    if type(obj) is a_class:
        """This defines if the object is exactly a class and return true"""
        return True
    
    else:
        """If the object is not a class therefore false must be returned"""
        return False

obj = 1
if is_same_class(obj, int):
    print("{} is an instance of the class {}".format(obj, int.__name__))
if is_same_class(obj, float):
    print("{} is an instance of the class {}".format(obj, float.__name__))
if is_same_class(obj, object):
    print("{} is an instance of the class {}".format(obj, int.__name__))
