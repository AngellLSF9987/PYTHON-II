from modelos.jugador import Jugador
from modelos.partido import Partido

def menu():
    """Muestra el menú de opciones de partido al usuario."""
    print("\nMenú de Partidos de Tenis\n")
    print("1. Jugar un partido al mejor de 3 sets.")
    print("2. Jugar un partido al mejor de 5 sets.")
    print("3. Salir.")

    return input("Selecciona una de la opciones [1], [2], [3]:\n")

def main():
    # Solicitar nombres de los jugadores

    nombre_jugador1 = input("Introduce el nombre para el Jugador 1:\n")
    nombre_jugador2 = input("Introduce el nombre para el Jugador 2:\n")

    jugador1 = Jugador(nombre_jugador1)
    jugador2 = Jugador(nombre_jugador2)

    while True: 
        opcion = menu()

        if opcion == "1":
            partido = Partido(jugador1, jugador2)
            partido.jugar_partido(3)
        
        elif opcion == "2":
            partido = Partido(jugador1, jugador2)
            partido.jugar_partido(5)

        elif opcion == "3":
            print("Hasta luego!")
        
        else:
            print("OJO! Opción no válida.")

if __name__ == "__main__":
    main()
        