"""Function that returns True if the object is exactly an instance of the specified class ; otherwise False.
"""
def is_same_class(obj, a_class):
    """condition to check if obj is an instance of a_class.

    Args:
        obj (_type_): check if obj is an instance of a_class.
        a_class (_type_): check if obj is an instance of a_class.

    Returns:
        _type_: _description_
    """
    if type(obj) is a_class:
        return True
    elif obj is not a_class:
        return False
is_same_class(1, 2)