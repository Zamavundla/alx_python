"""function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
"""
def is_kind_of_class(obj, a_class):
    """condition to check if obj is an instance of a_class.

    Args:
        obj (_type_): check if obj is an instance of a_class.
        a_class (_type_): check if obj is an instance of a_class.

    Returns:
        _type_: _description_
    """
    if isinstance(obj, a_class):
        return True
    elif not isinstance(obj, a_class):
        return False