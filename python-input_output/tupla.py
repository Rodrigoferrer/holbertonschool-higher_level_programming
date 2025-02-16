#!/usr/bin/python3

class Coordenadas:

    numero = 3

    def __init__(self, coordenadas):
        self.coordenada1 = coordenadas[0]
        self.coordenada2 = coordenadas[1]
    
    def cambiar_coordenadas(self, cantidad):
        self.coordenada1 = self.coordenada1 + cantidad
        self.coordenada2 = self.coordenada2 + cantidad
        return self.coordenada1, self.coordenada2
    
    def contador_instancia(self):
        Coordenadas.numero = Coordenadas.numero + 1
    
