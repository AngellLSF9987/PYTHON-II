import random

class Construccion:

    def __init__(self):
        """Constructoer vacío de la clase Construcción. Alojará una lista vacías de figuras."""
        self.figura = []

    def construir(self, piezas):
        """Método para construir una figura de LEGO con las piezas en orden aleeatorio."""

        piezas_random = random.sample(piezas, len(piezas))

        print("Construyendo la figura LEGO:\n")

        for i, pieza in enumerate(piezas_random):

            if i == 0:
                print(f"La primera pieza es: {pieza}. No encaja con ninguna.")
            else:
                print(f"LA pieza {i + 1} encaja con la pieza anterior {pieza}")

            self.figura.append(pieza) 
