from modelos.pieza import Pieza
from modelos.construccion import Construccion

def main():

    # Instanciar 5 objetos de la clase Pieza

    pieza1 = Pieza("rojo", "grande")
    pieza2 = Pieza("azul", "mediana")
    pieza3 = Pieza("verde", "pequeña")
    pieza4 = Pieza("amarilla", "mediana")
    pieza5 = Pieza("lila", "grande")

    lista_piezas = [pieza1, pieza2, pieza3, pieza4, pieza5]

    lego = Construccion()

    lego.construir(lista_piezas)

if __name__ == "__main__":
    main()
