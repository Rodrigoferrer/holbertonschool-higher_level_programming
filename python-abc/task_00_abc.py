#!/usr/bin/python3
"""Python3"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Class Animal"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Class dog, inherits from abstract Class Animal"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Class Cat, inherits from abstract class animal"""
    def sound(self):
        return "Meow"
