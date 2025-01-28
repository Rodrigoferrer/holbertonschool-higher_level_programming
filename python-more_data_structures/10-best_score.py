#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    # Funcion max() para encontrar la clave con el valor máximo a traves del metodo get
    return max(a_dictionary, key=a_dictionary.get)
