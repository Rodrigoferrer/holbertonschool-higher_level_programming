#!/usr/bin/python3
"""Python3s"""


def write_file(filename="", text=""):
    """Read, modify and print the content of a file.

    Args:
        filename (str): The name of the file to read.
        text (str): the text to add
    """
    with open(filename, 'w', encoding='utf-8') as text1:
        stringtofile = text1.write(text)
        return stringtofile
