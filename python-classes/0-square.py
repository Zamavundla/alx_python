class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initialize the Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def dict_(self):
        """
        Returns a dictionary representation of the square instance.

        Returns:
            dict: A dictionary containing the size of the square.
        """
        return {"size": self.__size}

if __name__ == "__main__":
    mysquare = Square(3)
    print(type(mysquare))
    print(mysquare.dict_())

    mysquare = Square(89)
    print(type(mysquare))
    print(mysquare.dict_())

    mysquare = Square(3)
    print(type(mysquare))
    print(mysquare.dict_())

    try:
        print(mysquare.size)
    except Exception as e:
        print(e)

    mysquare = Square(3)
    print(type(mysquare))
    try:
        print(mysquare._size)
    except Exception as e:
        print(e)
