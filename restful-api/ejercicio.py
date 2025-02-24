#!/usr/bin/python3

def square_digits(num):

    num = str(num)

    for digit in num:
        digit += int(digit ** 2)
    return digit


    
    r