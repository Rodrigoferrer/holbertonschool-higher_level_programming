#!/usr/bin/python3
"""A class Square that defines a square by size"""


class Square:
    """Square class with private size attribute"""

    def __init__(self, size=0):
        """Initialize square with optional size

        Args:
            size (int, optional): Size of square side. Defaults to 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.size = size  # Usar el setter para establecer el tamaño

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size

        Args:
            value (int): New size of the square side.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size
    
    def my_print(self):
        """Prints hasthags"""
        if self.size == 0:
            print("")
            return
        for i in range(self.size):
            print("#" * self.size)
