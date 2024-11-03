class Estuche:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.boligrafos = []

    def agregar_boligrafo(self):
        if len(self.boligrafos) > self.capacidad:
            self.boligrafos.append(boligrafo)
        else:
            raise EstucheLlenoError("El estuche está lleno")

    def quitar_boligrafo(self, indice):
            boligrafo = self.boligrafos.pop(indice)
            return boligrafo

class EstucheLlenoError():
    pass

mi_estuche = Estuche(5)

Estuche.agregar_boligrafo("Azul")
Estuche.agregar_boligrafo("Negro")
Estuche.agregar_boligrafo("Rojo")
Estuche.agregar_boligrafo("Verde")
Estuche.agregar_boligrafo("Violeta")

try:
    mi_estuche.agregar_boligrafo("Gris")
except EstucheLlenoError as e:
    print(e)

try:
    boligrafo = mi_estuche.quitar_boligrafo()
    print("Quité un bolígrafo:", boligrafo)
except IndexError as e:
    print(e)