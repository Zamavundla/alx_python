class Square:
    def __init__(self, size):
        self.__size = size


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
