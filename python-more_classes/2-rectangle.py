#!/usr/bin/python3
"""Script that runs in python3 env"""


class Rectangle:
    """Representa un rectángulo."""

    def __init__(self, width=0, height=0):
        """Inicializa un nuevo rectángulo.

        Args:
            width (int): El ancho del rectángulo. Por defecto es 0.
            height (int): La altura del rectángulo. Por defecto es 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtiene el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el ancho del rectángulo.

        Args:
            value (int): El nuevo ancho del rectángulo.

        Raises:
            TypeError: Si el ancho no es un entero.
            ValueError: Si el ancho es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
