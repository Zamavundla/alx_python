def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)

#if __name__ == "__main__":
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
