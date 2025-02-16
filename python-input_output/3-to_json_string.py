#!/usr/bin/python3
"""Python3"""

import json

def to_json_string(my_obj):
    my_obj_cpy = json.dumps(my_obj)
    return my_obj_cpy
