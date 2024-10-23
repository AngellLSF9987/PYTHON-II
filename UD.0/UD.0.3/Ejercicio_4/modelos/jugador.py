import random

class Jugador:

    def __init__(self, nombre):
        """Constructor que inicializa el nombre del jugador."""

        self.nombre = nombre
        self.puntuacion = 0
        
    def __str__(self):
        """Devuelve el nombre del jugador."""
        return self.nombre

    def ganar_punto(self):
        """Incrementa losm puntos del jugador."""

        self.puntos += 1

    def reiniciar_puntuacion(self):
        """Reinicia los puntos del jugador después de un juego."""

        self.puntuacion = 0
    
