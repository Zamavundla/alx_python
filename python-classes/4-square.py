class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)


mysquare = Square(3)
print(type(mysquare))  # Output: <class '__main__.Square'>
print(mysquare.__dict__)  # Output: {'_Square__size': 3}
mysquare.my_print()  # Output: ###
                    #         ###
                    #         ###

# Correct output - case: mysquare = Square(89)
mysquare = Square(89)
print(type(mysquare))  # Output: <class '__main__.Square'>
print(mysquare.__dict__)  # Output: {'_Square__size': 89}
mysquare.my_print()  # Output: ##########
                    #         ##########
                    #         ##########
                    #         ##########
                    #         ##########
                    #         ##########
                    #         ##########
                    #         ##########
                    #         ##########
