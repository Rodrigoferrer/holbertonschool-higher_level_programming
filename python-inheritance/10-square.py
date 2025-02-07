#!/usr/bin/python3
"""Python3"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inherited from Rectangle"""
    
    def __init__(self, size, size):
        """Constructor for size of Square"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
        
    
    def area(self, size):
        return self.__size * self.__size
