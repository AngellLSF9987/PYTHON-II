# CLASE HIJA

from .deportista import Deportista

class Runner(Deportista):
    
    def __init__(self, nombre, edad, nacionalidad, especialidad, record):
        super().__init__(nombre,edad, nacionalidad)
        
        self._especialidad = especialidad
        self._record = record


    def mostrar_datos(self):
        return f"{super().mostrar_datos()}\nEspecialidad: {self._especialidad}\nRecord: {self._record}"
    
    