# biblioteca/modelos/generos/especifico.py

from biblioteca.modelos.generos.genero import Genero

class Especifico(Genero):

    __id_counter = 1 # Contador para los registros existentes y los nuevos que se añadan

    def __init__(self, nombre_genero, nombre_especifico, tipo=None):
        super().__init__(nombre_genero)

        self.__id = Especifico.__id_counter  # Asigna el ID actual, es decir, el ID = 1
        Especifico.__id_counter += 1         # Contador autoincremental

        self.__nombre_especifico = nombre_especifico
        self.__tipo = tipo

    def get_id(self):
        return self.__id
    
    def set_id(self, nuevo_id):
        self.__id = nuevo_id    # Método para actualizar el ID

    def get_nombre_especifico(self):
        return self.__nombre_especifico

    def set_nombre_especifico(self, value):
        self.__nombre_especifico = value

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, value):
        self.__tipo = value

    def __str__(self):
        """Método __str__. Muestra todos los datos de modelo Subgénero"""
        return f"Id: {self.get_id()}.\nGénero Literario:{super().get_nombre_genero()}\nSubgénero Literario: {self.get_nombre_especifico()} - Tipo Subgénero: {self.get_tipo() if self.get_tipo() else "Tipo no definido"}."

    def mostrar_datos_especifico(self):
        """Muestra los datos especificos del Género Literario."""
        return f"Género Literario:{super().get_nombre_genero()}\nSubgénero Literario: {self.get_nombre_especifico()} - Tipo Subgénero: {self.get_tipo() if self.get_tipo() else "Tipo no definido"}."
