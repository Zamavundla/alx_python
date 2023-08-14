def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    :param obj: The object to be checked.
    :param a_class: The class to compare against.
    :return: True if the object is an instance of a subclass of the specified class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

# Test cases
a = 1
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))

a = 3.14
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))

a = None
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))

a = None
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))

a = [1, 2, 3]
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))

a = [1, 2, 3]
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
