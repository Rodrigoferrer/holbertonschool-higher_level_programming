#!/usr/bin/python3
"""python3"""


def read_file(filename=""):
    """Read and print the content of a file.

    Args:
        filename (str): The name of the file to read.
    """

    with open(filename, 'r+', encoding='utf-8') as text:
        print(text.read(), end='')
