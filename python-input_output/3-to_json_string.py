#!/usr/bin/python3
"""Python3"""


import json


def to_json_string(my_obj):
    """Function that takes an object of python and converts it to json"""

    my_obj_cpy = json.dumps(my_obj)
    return my_obj_cpy
