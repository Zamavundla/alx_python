def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class.

    :param obj: The object to be checked.
    :param a_class: The class to compare against.
    :return: True if the object is an instance of the specified class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)

# Test cases
a = 1
if is_kind_of_class(a, int):
    print(True)
else:
    print(False)

a = True
if is_kind_of_class(a, int):
    print(True)
else:
    print(False)

a = 3.14
if is_kind_of_class(a, int):
    print(True)
else:
    print(False)

a = True
if is_kind_of_class(a, object):
    print(True)
else:
    print(False)

a = None
if is_kind_of_class(a, object):
    print(True)
else:
    print(False)

a = None
if is_kind_of_class(a, list):
    print(False)
else:
    print(True)

a = [1, 2, 3]
if is_kind_of_class(a, list):
    print(True)
else:
    print(False)

a = [1, 2, 3]
if is_kind_of_class(a, object):
    print(True)
else:
    print(False)
