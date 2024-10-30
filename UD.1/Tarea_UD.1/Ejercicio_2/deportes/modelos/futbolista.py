# deportes/modelos/futbolista.py
# CLASE HIJA

from .deportista import Deportista

class Futbolista(Deportista):
    
    __id_counter = 1 # Contador único para registros de Futbolistas
    
    def __init__(self, nombre, apellido, edad, nacionalidad, equipo, goles):
        super().__init__(nombre, apellido, edad, nacionalidad)
        
        self.__id = Futbolista.__id_counter # Asigna el ID actual, es decir, el ID = 1        
        Futbolista.__id_counter += 1 # Contador autoincremental
                
        self.__equipo = equipo
        self.__goles = goles

    def get_id(self):
        return self.__id

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
        return f"{super().mostrar_datos()}\nId: {self.get_id}\nEquipo: {self.get_equipo()}\nGoles: {self.get_goles()}"
    
    