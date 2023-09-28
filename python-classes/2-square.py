"""class Square that defines a square by: (based on 1-square.py).
"""


class Square:
    """__init__ method to initialize the Square instance.
    Args:
        size (int): size of the square.
    """

    def __init__(self, size=0):
        """private instance attribute: size.
        """
        self.__size = size
    """public instance method: def area(self).
    Returns:
        the current square area.
    """

    def area(self):
        return self.__size**2


"""Create an instance x of class Square, size = 5.
"""
x = Square(5)
"""Call the area method and print the result.
"""
x.area()
