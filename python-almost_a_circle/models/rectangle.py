"""Write the class Rectangle that inherits from Base.
"""
from models.base import Base
"""Module for creating a Rectangle class."""


class Rectangle(Base):
    """Rectangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """Getters and setters."""

    @property
    def width(self):
        """width getter."""
        return self.__width

    @property
    def height(self):
        """height getter."""
        return self.__height

    @property
    def x(self):
        """x getter."""
        return self.__x

    @property
    def y(self):
        """y getter."""
        return self.__y

    @width.setter
    def width(self, value):
        """width setter."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """height setter."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """x setter."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """y setter."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
            
    def area(self):
        """Area method."""
        return self.width * self.height
    
    def display(self):
        """Display method."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)
            
    def __str__(self):
        """str method."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def update(self, *args, **kwargs):
        """Update method."""
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
        
    
