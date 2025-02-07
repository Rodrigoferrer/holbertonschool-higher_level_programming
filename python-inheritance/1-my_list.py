#!/usr/bin/python3
"""script to be runned in python3 env"""


class MyList(list):
    """Clase"""

    def print_sorted(self):
        """funcion print"""
        print(sorted(self))
