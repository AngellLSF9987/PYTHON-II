from modelos.jugador import Jugador
import random

class Partido:

    def __init__(self, jugador1, jugador2):
        """Constructor que inicializa los jugadores del partido y sus puntuaciones."""

        self.jugadores = (jugador1, jugador2)

    def jugar_juego(self):
        """Simula un juego entre los dos jugadores."""
        
        puntos = [0, 0]
        while True:
            # Simular el ganador de un punto

            ganador = random.choice([self.jugadores])

            if ganador == self.jugadores[0]:
                puntos[0] +=1
                print(f"{self.jugadores[0]. nombre} gana el punto!")
            else:
                puntos[1] += 1
                print(f"{self.jugadores[1]. nombre} gana el punto!")

            # Verificar si hay ya un ganador del juego

            if puntos[0] >= 4 and puntos[0] - puntos[1] >= 2:
                print(f"{self.jugadores[0]. nombre} gana el juego!")
                self.jugadores[0].reiniciar_puntuacion()

                return 0

            elif puntos[1] >= 4 and puntos[1] - puntos[0] >= 2:
                print(f"{self.jugadores[1]. nombre} gana el juego!")
                self.jugadores[1].reiniciar_puntuacion()

                return 1               
    
    def jugar_set(self):
        """Simula un set entre los dos jugadores."""
        juegos = [0, 0]

        while True:
            print("Comienza el set!")
            self.jugar_juego()

            juegos[self.jugar_juego()] += 1 # Aumenta el contador de juegos

            # Verificar si hay ya un ganador del set

            if juegos[0] >= 6 and juegos[0] - juegos[1] >= 2:
                print(f"{self.jugadores[0]. nombre} gana el set!")
                self.jugadores[0].reiniciar_puntuacion()

                return 0

            elif juegos[1] >= 6 and juegos[1] - juegos[0] >= 2:
                print(f"{self.jugadores[1]. nombre} gana el set!")
                self.jugadores[1].reiniciar_puntuacion()

                return 1   

    def jugar_partido(self, sets_jugar):
        """Simula un partido entre los dos jugadores. Teniendo en cuenta si el partido se juega a 3 o 5 sets."""
        print("Comienza el partido!")
        sets_ganados = [0, 0]

        for _ in range(sets_jugar):
            self.jugar_set()

            sets_ganados[self.jugar_set()] += 1 # Contador de sets jugados

            # Verificar si ya hay un ganador de partido
            
            if sets_ganados[0] > sets_jugar // 2:
                print(f"{self.jugadores[0]. nombre} gana el partido!")
                self.jugadores[0].reiniciar_puntuacion()

                return self.jugadores[0]

            elif sets_ganados[1] > sets_jugar // 2:
                print(f"{self.jugadores[1]. nombre} gana el partido!")
                self.jugadores[1].reiniciar_puntuacion()

                return self.jugadores[1]

        
