#!/usr/bin/python3
"""python3"""


def read_file(filename=""):
    """Function that reads file from main"""

    with open(filename, 'r+', encoding='utf-8') as text:
        print(text.read(), end='')
