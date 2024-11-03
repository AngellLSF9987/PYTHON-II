# deportes/modelos/tenista.py
# CLASE HIJA

from .deportista import Deportista

class Tenista(Deportista):
    
    __id_counter = 1 # Contador único para registros de Tenistas

    def __init__(self, nombre, apellido, edad, nacionalidad, ranking, trofeos_ganados):
        super().__init__(nombre, apellido, edad, nacionalidad)

        self.__id = Tenista.__id_counter # Asigna el ID actual, es decir, el ID = 1        
        Tenista.__id_counter += 1 # Contador autoincremental
                
        self.__ranking = ranking
        self.__trofeos_ganados = trofeos_ganados

    def get_id(self):
        return self.__id

    def get_ranking(self):
        return self.__ranking

    def set_ranking(self, value):
        self.__ranking = value

    def get_trofeos_ganados(self):
        return self.__trofeos_ganados

    def set_trofeos_ganados(self, value):
        self.__trofeos_ganados = value

    def mostrar_datos(self):
        """Actúa como método __str__"""
        return f"{super().mostrar_datos()}\nId: {self.get_id()}\nRanking: {self.get_ranking()}\nTrofeos Ganados: {self.get_trofeos_ganados()}"
    
    