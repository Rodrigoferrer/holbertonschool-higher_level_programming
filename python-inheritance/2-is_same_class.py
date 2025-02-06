#!/usr/bin/python3
"""Python3"""


def is_same_class(obj, a_class):
    """Class"""

    tipo = type(obj, a_class)
    
    if tipo is a_class:
        return True
    else:
        return False
