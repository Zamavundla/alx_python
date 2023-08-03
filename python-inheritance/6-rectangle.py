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


bg = BaseGeometry()
print(dir(bg))

bg = BaseGeometry()
bg.integer_validator("myint", 12)

bg = BaseGeometry()
bg.integer_validator("myint", 12)
bg.integer_validator("width", 89)

bg = BaseGeometry()
try:
    bg.integer_validator("name", "John")
except TypeError as e:
    print("[{}] {}".format(e.__class__.__name__, e))

bg = BaseGeometry()
try:
    bg.integer_validator("age", 0)
except ValueError as e:
    print("[{}] {}".format(e.__class__.__name__, e))

bg = BaseGeometry()
try:
    bg.integer_validator("age", -4)
except ValueError as e:
    print("[{}] {}".format(e.__class__.__name__, e))

bg = BaseGeometry()
try:
    bg.integer_validator("age", 13.5)
except TypeError as e:
    print("[{}] {}".format(e.__class__.__name__, e))

bg = BaseGeometry()
try:
    bg.area()
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
