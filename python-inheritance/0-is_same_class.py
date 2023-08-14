"""The module returns True if the object is an instance of a specified class/ False"""

def is_same_class(obj, a_class):
    """prototype for the instance, which defines an object and a class."""
    
    if type(obj) is a_class:
        """To define if if the obj is exactly a class and return true."""
        
        return True
    
    else:
        """If obj is not a class it must return false."""
        return False
        a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
        
    a = True
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
        
    a = 3.14
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
        
    a = True
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
        
    a = None
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
        
    a = None
    if is_same_class(a, list):
        print("{} is an instance of the class {}".format(a, list.__name__))
        
    a = [1, 2, 3]
    if is_same_class(a, list):
        print("{} is an instance of the class {}".format(a, list.__name__))
        
    a = [1, 2, 3]
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
