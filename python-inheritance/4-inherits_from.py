#!/usr/bin/python3
"""python3"""


def inherits_from(obj, a_class):
    """class"""

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
