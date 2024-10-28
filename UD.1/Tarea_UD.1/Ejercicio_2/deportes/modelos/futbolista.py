from .deportista import Deportista

class Futbolista(Deportista):
    
    def __init__(self, nombre, edad, nacionalidad, equipo, goles):
        super().__init__(nombre,edad, nacionalidad)
        
        self._equipo = equipo
        self._goles = goles


    def mostrar_datos(self):
        return f"{super().mostrar_datos()()}\nEquipo: {self._equipo}\nGoles: {self._goles}"
    
    