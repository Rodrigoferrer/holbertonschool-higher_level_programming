#!/usr/bin/python3
"""Python3"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inherited from Rectangle"""
    
    def __init__(self, size):
        """Constructor for size of Square"""
        self.integer_validator("size", size)
        self.__size = size
    
    def area(self, size):
        return size * size
