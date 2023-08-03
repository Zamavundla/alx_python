def raise_exception():
    raise TypeError("Exception has been raised")

try:
    raise_exception()
except TypeError:
    print("Exception has been raised")
