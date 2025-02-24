#!/usr/bin/python3

def suma(a):
    primer = a[0]
    segundo = a[1]
    return primer + segundo
numeros = [(1, 2), (2, 3), (4, 3)]

calular = map(suma, numeros)

print(calular)
print(list(calular))