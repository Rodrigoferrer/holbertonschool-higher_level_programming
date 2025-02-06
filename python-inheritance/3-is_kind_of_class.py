#!/usr/bin/python3
"""Python3"""


def is_kind_of_class(obj, a_class):
    """class

    """
    
    class_object = type(obj)

    if class_object isinstance(a_class):
        return True
    else:
        return False
