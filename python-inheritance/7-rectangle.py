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

# Test cases
print("Available attributes and methods of Rectangle class:", dir(Rectangle))

r1 = Rectangle(1, 4)
print("Area of r1:", r1.area())  # Output: 4

r2 = Rectangle(1411, 781)
print("Area of r2:", r2.area())  # Output: 1103591

r3 = Rectangle(5, 5)
print("Area of r3:", r3.area())  # Output: 25

r4 = Rectangle(1411, 781)
print(r4)  # Output: [Rectangle] 1411/781

r5 = Rectangle(1, 4)
print(r5)  # Output: [Rectangle] 1/4

r6 = Rectangle(5, 5)
print(r6)  # Output: [Rectangle] 5/5

# The following instantiations will raise TypeError and ValueError
r7 = Rectangle()
r8 = Rectangle(1)
r9 = Rectangle(1, [12, 52])
r10 = Rectangle(4, 5)
r11 = Rectangle(4, 0)
