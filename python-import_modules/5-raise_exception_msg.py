def raise_exception_msg(message=""):
    raise NameError(message)

try:
    raise_exception_msg()
except NameError as ne:
    print("Caught NameError with empty message:", ne)
