# deportes/modelos/runner.py
# CLASE HIJA

from .deportista import Deportista

class Runner(Deportista):
    
    def __init__(self, nombre, edad, nacionalidad, especialidad, record):
        super().__init__(nombre,edad, nacionalidad)
        
        self.__especialidad = especialidad
        self.__record = record

    def get_especialidad(self):
        return self.__especialidad

    def set_especialidad(self, value):
        self.__especialidad = value

    def get_record(self):
        return self.__record

    def set_record(self, value):
        self.__record = value

    def mostrar_datos(self):
        """Actúa como método __str__"""
        return f"{super().mostrar_datos()}\nEspecialidad: {self.get_especialidad()}\nRecord: {self.get_record()}"
    
    