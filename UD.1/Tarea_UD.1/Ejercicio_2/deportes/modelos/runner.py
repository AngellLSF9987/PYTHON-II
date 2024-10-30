# deportes/modelos/runner.py
# CLASE HIJA

from .deportista import Deportista

class Runner(Deportista):
    
    __id_counter = 1 # Contador único para registros de Futbolistas    
    
    def __init__(self, nombre, apellido, edad, nacionalidad, especialidad, record):
        super().__init__(nombre, apellido, edad, nacionalidad)
        
        self.__id = Runner.__id_counter # Asigna el ID actual, es decir, el ID = 1        
        Runner.__id_counter += 1 # Contador autoincremental
        
        self.__especialidad = especialidad
        self.__record = record

    def get_id(self):
        return self.__id
        
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
        return f"{super().mostrar_datos()}\nId: {self.get_id}\nEspecialidad: {self.get_especialidad()}\nRecord: {self.get_record()}"
    
    