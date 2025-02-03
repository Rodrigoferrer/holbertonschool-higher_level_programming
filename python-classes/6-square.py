#!/usr/bin/python3
"""A class Square that defines a square by size"""


class Square:
    """Square class with private size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with optional size

        Args:
            size (int, optional): Size of square side. Defaults to 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
            return

        for _ in range(self.position[1]):
            print("")

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
