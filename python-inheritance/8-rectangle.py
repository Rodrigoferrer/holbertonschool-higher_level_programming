#!/usr/bin/python3
"""Python3"""


class BaseGeometry:
    """Class for base geometry"""

    def __init__(self, width, height):
        pass
    
    def area(self):
        return self.__width * self.__height
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):

        self.integer_validator("width", width)  # Pasar el nombre del parámetro
        self.__width = width
        self.integer_validator("height", height)  # Pasar el nombre del parámetro
        self.__height = height
