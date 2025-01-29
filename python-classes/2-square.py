#!/usr/bin/python3
""" Alta clase tiene este objeto cuadrado """


class Square:
    """ Siguen las clases  """
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
    return self.__size
