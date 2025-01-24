#!/usr/bin/python3
import * from random
var1 = input("ingrese cantidad de letras: ")
var2 = input("ingrese cantidad de caracteres especiales: ")
var3 = input("ingrese longitud deseada: ")
lista = list(var1 + var2 + var3)
if len(lista) < 0:
        print("Error")
else:
    print("{}".format(random.randint(0, len(lista))))

    


