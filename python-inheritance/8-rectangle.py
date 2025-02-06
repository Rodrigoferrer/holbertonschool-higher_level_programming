#!/usr/bin/python3
"""Python3"""


class BaseGeometry:
    """Class for base geometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    
    @property    
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
    
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """class Rectangle"""

        
    def area(self):
        """Calcula el área del rectángulo"""
        return self.__width * self.__height
