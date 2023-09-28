"""This class uses a module 0-main.py to test the class Square.
"""

class Square:
    """class Square with a private attribute - size.
     Args:  
            size (int): size of the square.
    
    """

    def __init__(self, size=0):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.
            
            instance attribute: size
        """
        self.__size = size

square = Square()
