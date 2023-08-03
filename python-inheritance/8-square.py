class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    def __init__(self, size):
        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)


print(dir(Square))  # Output: ['_Rectangle__height', '_Rectangle__width', '_Square__size', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']

print(issubclass(Square, Rectangle))  # Output: True

s = Square(4)
print(s)  # Output: [Square] 4/4
print(s.area())  # Output: 16

s = Square(1340)
print(s)  # Output: [Square] 1340/1340
print(s.area())  # Output: 1795600

s = Square()
print(s)  # Output: [Square] 0/0
print(s.area())  # Output: 0

try:
    s = Square("13")
except TypeError as e:
    print(e)  # Output: size must be an integer

s = Square(13)
print(s)  # Output: [Square] 13/13
print(s.area())  # Output: 169
print(s.width)  # Output: 13
print(s.height)  # Output: 13
