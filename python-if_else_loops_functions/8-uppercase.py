#!/usr/bin/python3
def uppercase(str):
    stringcopy = ""
    for char in str:
        if char >= 'a' and char <= 'z':
            stringcopy += chr(ord(char) - 32)
        else:
            stringcopy += char
    print("{}".format(stringcopy))
