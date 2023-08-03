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


print("Available attributes and methods of Rectangle class:", dir(Rectangle))
# Output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']

r1 = Rectangle(1, 4)
print(r1.area())  # Output: 4

r2 = Rectangle(1411, 781)
print(r2.area())  # Output: 1103591

r3 = Rectangle(5, 5)
print(r3.area())  # Output: 25

r4 = Rectangle(1411, 781)
print(r4)  # Output: [Rectangle] 1411/781

r5 = Rectangle(1, 4)
print(r5)  # Output: [Rectangle] 1/4

r6 = Rectangle(5, 5)
print(r6)  # Output: [Rectangle] 5/5

# The following instantiations will raise TypeError and ValueError
try:
    r7 = Rectangle()
except TypeError as e:
    print("[TypeError] {}".format(e))  # Output: [TypeError] __init__() missing 2 required positional arguments: 'width' and 'height'

try:
    r8 = Rectangle(1)
except TypeError as e:
    print("[TypeError] {}".format(e))  # Output: [TypeError] __init__() missing 1 required positional argument: 'height'

try:
    r9 = Rectangle(1, [12, 52])
except TypeError as e:
    print("[TypeError] {}".format(e))  # Output: [TypeError] height must be an integer

try:
    r10 = Rectangle(4, 5)
except ValueError as e:
    print("[ValueError] {}".format(e))  # Output: [ValueError] height must be greater than 0

try:
    r11 = Rectangle(4, 0)
except ValueError as e:
    print("[ValueError] {}".format(e))  # Output: [ValueError] height must be greater than 0
