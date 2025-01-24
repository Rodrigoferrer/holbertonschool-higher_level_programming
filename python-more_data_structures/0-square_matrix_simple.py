#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = []
    for i in matrix:
        lista_aux = []
        for j in i:
            lista_aux.append(j**2) # [16,25,36]
        copy.append(lista_aux) # [[1,4,9], [16,25,36]]
    return copy


