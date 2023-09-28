def raise_exception():
    x = "charles"
    if type(x) is not int:
        raise TypeError("Only integers are allowed")
