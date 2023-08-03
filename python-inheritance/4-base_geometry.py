class BaseGeometry:
    """ BaseGeometry class documentation """
    
    def area(self):
        raise Exception("area() is not implemented")

bg = BaseGeometry()
print(dir(bg))

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
