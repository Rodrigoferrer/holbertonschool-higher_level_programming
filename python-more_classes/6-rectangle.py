    #!/usr/bin/python3
"""Script that runs in python3 environ"""


class Rectangle:
    """Representa un rectángulo."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Inicializa un nuevo rectángulo.

        Args:
            width (int): El ancho del rectángulo. Por defecto es 0.
            height (int): La altura del rectángulo. Por defecto es 0.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        self.__width = value

    @property
    def height(self):
        """Obtiene la altura del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece la altura del rectángulo.

        Args:
            value (int): La nueva altura del rectángulo.

        Raises:
            TypeError: Si la altura no es un entero.
            ValueError: Si la altura es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula el área del rectángulo.

        Returns:
            int: El área del rectángulo.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calcula el perímetro del rectángulo.

        Returns:
            int: El perímetro, o 0 si el ancho o la altura son 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):

        """Devuelve una representación en cadena del rectangulo."""

        if self.__width == 0 or self.__height == 0:
            return ""

        s = ""
        for i in range(self.__height):
            for j in range(self.__width):
                s += '#'
            if i < self.height - 1:
                s += '\n'

        return s

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
