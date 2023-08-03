class Square:
    def __init__(self, size):
        self.__size = size


# Create a square with size 5
square1 = Square(5)

# Access the size attribute (Not recommended, but still possible)
print("Size of square1:", square1._Square__size)

# Try to directly modify the size attribute (Not recommended)
# square1._Square__size = 10

# Create another square with size 3
square2 = Square(3)

# Access the size attribute of square2 (Not recommended)
print("Size of square2:", square2._Square__size)
