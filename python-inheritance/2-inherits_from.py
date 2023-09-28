"""This function uses the 2-main.py module to test the 2-is_same_class.py module."""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    elif not issubclass(type(obj), a_class):
        return False


inherits_from(1, int)
