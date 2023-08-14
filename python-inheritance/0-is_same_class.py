def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
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
