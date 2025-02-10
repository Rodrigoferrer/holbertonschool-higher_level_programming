#!/usr/bin/python3
"""Python3"""


from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Class Father Shape"""
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """Class circle, inherits from abstract class Shape"""
    
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        area = math.pi * (self.radius ** 2)
        return area
    
    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

class Rectangle(Shape):
    """Class rectangle, inherits from abstract class shape"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

def shape_info(shape):
    area = shape.area()
    perimeter = shape.perimeter()
    print ({area})
    print ({perimeter})
