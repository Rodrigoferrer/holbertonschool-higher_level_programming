#!/usr/bin/python3
"""Python3"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):

        self.integer_validator("width", width)  # Pasar el nombre del parámetro
        self.__width = width
        self.integer_validator("height", height)  # Pasar el nombre del parámetro
        self.__height = height

