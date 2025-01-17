#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    suma = add(a, b)
    resta = sub(a, b)
    multi = mul(a, b)
    divi = div(a, b)
    print("{} + {} = {}".format(a, b, suma))
    print("{} - {} = {}".format(a, b, resta))
    print("{} * {} = {}".format(a, b, multi))
    print("{} / {} = {}".format(a, b, divi))
    
    