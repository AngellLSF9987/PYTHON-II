# CLASE HIJA

from .deportista import Deportista

class Tenista(Deportista):
    
    def __init__(self, nombre, edad, nacionalidad, ranking, trofeos_ganados):
        super().__init__(nombre,edad, nacionalidad)
        
        self._ranking = ranking
        self._trofeos_ganados = trofeos_ganados


    def mostrar_datos(self):
        return f"{super().mostrar_datos()}\nRanking: {self._ranking}\nTrofeos Ganados: {self._trofeos_ganados}"
    
    