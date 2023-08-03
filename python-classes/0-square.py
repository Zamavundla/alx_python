class Square:
    def __init__(self, size):
        self.__size = size

# Correct output - case: mysquare = Square(3)
mysquare = Square(3)
print(type(mysquare))  # Output: <class '__main__.Square'>
print(mysquare.__dict__)  # Output: {'_Square__size': 3}

# Correct output - case: mysquare = Square(89)
mysquare = Square(89)
print(type(mysquare))  # Output: <class '__main__.Square'>
print(mysquare.__dict__)  # Output: {'_Square__size': 89}

# Try to access the 'size' attribute directly (Not recommended)
# This will raise an AttributeError since 'size' is a private attribute and not directly accessible
try:
    print(mysquare.size)
except AttributeError as e:
    print(e)  # Output: 'Square' object has no attribute 'size'

# Try to access the '_size' attribute directly (Not recommended)
# This will raise an AttributeError since '_size' is a private attribute and not directly accessible
try:
    print(mysquare._size)
except AttributeError as e:
    print(e)  # Output: 'Square' object has no attribute '_size'
