#!/usr/bin/python3
"""Module for class Rectangle that inherits from Base"""

"""To import the base file import the class Base"""
from models.base import Base

"""class module that inherits from Base class"""
class Rectangle(Base):
    """Defined rectangle class that will inherit from Base class"""

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """To initialise the attributs """
        super().__init__(id)
        """super to call and use the logic of the init of the Base class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    """To get width instance"""
    @property
    def width(self):
        """To difine width method"""
        return self.__width
    
    """To get height instance"""
    @property
    def height(self):
        """To difine width method"""
        return self.__height
    
    """To get x instance"""
    @property
    def x(self):
        """for defining x method"""
        return self.__x
    
    """To get y instance"""
    @property
    def y(self):
        """To define y method"""
        return self.__y
    
    """To set instance for width"""
    @width.setter
    def width(self, value):
        """To define the width method"""

        if not isinstance(value, int):
            """To raise exception if the input is not an int"""
            raise TypeError("width must be an integer")
            """To inform that the input needs to be an integer"""            
        
        elif value <= 0:
            """For the given attribute must be <=0"""

            raise ValueError("width must be > 0")
            """To raise a ValueError if width is not <=0"""
        
        else:
            self.__width = value 
    
    
    """To set instance for height"""
    @height.setter
    def height(self, value):
        """To define the height method"""
        
        if not isinstance(value, int):
            """To raise exception if the input is not an int"""
            raise TypeError("height must be an integer")
            """To inform that the input needs to be an integer"""            
        
        elif value <= 0:
            """For the given attribute must be <=0"""
            raise ValueError("height must be > 0")
            """To raise a ValueError if height is not <=0"""
        else:
            self.__height = value
    
    """To set instance for X"""
    @x.setter
    def x(self, value):
        """To define the x method to set"""
        if not isinstance(value, int):
            """To raise exception if the input is not an int"""
            raise TypeError("x must be an integer")
            """To inform that the input needs to be an integer"""            
            
        elif value < 0:
            """For the given attribute must be <=0"""
            raise ValueError("x must be >= 0")
            """To raise a ValueError is x is not <=0"""
        else:
            self.__x = value

    """To set instance for Y"""
    @y.setter
    def y(self, value):
        """to define the y method"""
        
        if not isinstance(value, int):
            """To raise exception if the input is not an int"""
            raise TypeError("y must be an integer")
            """To inform that the input needs to be an integer"""            
        
        elif value < 0:
            """For the given attribute must be >=0"""
            raise ValueError("y must be >= 0")
            """To raise a ValueError is y is not >=0"""
        else:
            self.__y = value
        
    def area(self):
        """To define the area method"""
        return self.__height * self.__width
        """Use rectangle area formular"""

#a = Rectangle(width=12, height=3)
#print(a.area())
    
    def display(self):
        """To define the display public method"""
        for i in range(self.__y):
            """The instance of characher # range"""
            print()
            """To dispaly results"""
        
        for i in range(self.__height):
            """To define the range"""
            print(" " * self.__x + "#" * self.__width)
            """To display characters '#' as a rectangle"""

    def __str__(self):
        """To define the str method"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
        """To return the string"""
    
    def update(self, *args, **kwargs):
        """Public method that assigns an argument to each attribute"""
        if len(args) >= 1:
            """First argument"""
            self.id = args[0]
            """ID attribute"""
        if len(args) >= 2:
            """Second argument"""
            self.width = args[1]
            """width attribute"""
        if len(args) >= 3:
            """Third argument"""
            self.height = args[2]
            """height attribute"""
        if len(args) >= 4:
            """Fourth argument"""
            self.x = args[3]
            """x attribute"""
        if len(args) >= 5:
            """Fifth argument"""
            self.y = args[4]
            """Y attribute"""
        
        for key, value in kwargs.items():
            """**kwargs must be skipped if args exists and not empty"""
            setattr(self, key, value)
            """Set attributes to"""