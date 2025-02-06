#!/usr/bin/python3
"""Python3"""


def is_same_class(obj, a_class):
    """Class"""

    if issubclass(obj, a_class):
        return True
    else:
        return False
