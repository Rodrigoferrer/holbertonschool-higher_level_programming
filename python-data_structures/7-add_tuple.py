#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lt1 = len(tuple_a)
    lt2 = len(tuple_b)
    res = []
    for i in range(2):
        suma = 0
        if i < lt1:
            suma += tuple_a[i]
        if i < lt2:
            suma += tuple_b[i]
        res.append(suma)
    return tuple(res)
