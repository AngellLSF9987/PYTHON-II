# deportes/modelos/futbolista.py
# CLASE HIJA

from .deportista import Deportista

class Futbolista(Deportista):
    
    def __init__(self, nombre, edad, nacionalidad, equipo, goles):
        super().__init__(nombre,edad, nacionalidad)
        
        self.__equipo = equipo
        self.__goles = goles

    def get_equipo(self):
        return self.__equipo

    def set_equipo(self, value):
        self.__equipo = value

    def get_goles(self):
        return self.__goles

    def set_goles(self, value):
        self.__goles = value

    def mostrar_datos(self):
        """Actúa como método __str__"""
        return f"{super().mostrar_datos()}\nEquipo: {self.get_equipo()}\nGoles: {self.get_goles()}"
    
    