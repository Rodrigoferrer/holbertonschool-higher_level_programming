#!/usr/bin/python3
"""Python3"""


class BaseGeometry:
    """Class for base geometry"""

    def __init__(self):
        return

    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if value is not a int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
