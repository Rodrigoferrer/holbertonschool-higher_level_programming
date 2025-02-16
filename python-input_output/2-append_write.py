#!/usr/bin/python3
"""Python3"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8)
    Args:
        filename: name of the file
        text: text to append
    Returns:
        number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
