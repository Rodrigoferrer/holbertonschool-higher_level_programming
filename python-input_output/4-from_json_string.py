#!/usr/bin/python3
"""Python3"""


import json


def from_json_string(my_str):
    """Function that converts a json to a python data struct"""

    my_str_cpy = json.loads(my_str)
    return my_str_cpy
