#!/usr/bin/python3
"""Python3"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherited from Rectangle"""

    def __init__(self, size):
        """Constructor for size of Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
