#!/usr/bin/python3
def max_integer(my_list=[]):
    temp = list[0]
    for i in my_list:
        if temp < i:
            temp = i
    return temp
