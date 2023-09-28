"""class Square that defines a square by: (based on 0-square.py).
"""
class Square:
    """class Square with a private attribute - size.
    """
    def __init__(self,size = 0):
        self.__size = size
        """Handle the exception TypeError and ValueError.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
square_size = Square(3)
