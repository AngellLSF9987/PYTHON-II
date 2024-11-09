# biblioteca/modelos/generos/subgenero.py

from biblioteca.modelos.generos.genero import Genero

class Subgenero(Genero):

    __id_counter = 1 # Contador para los registros existentes y los nuevos que se añadan

    def __init__(self,nombre_genero, nombre_subgenero, tipo = None):
        super().__init__(nombre_genero)


        self.__id = Subgenero.__id_counter  # Asigna el ID actual, es decir, el ID = 1
        Subgenero.__id_counter += 1         # Contador autoincremental

        self.__nombre_subgenero = nombre_subgenero
        self.__tipo = tipo

    def get_id(self):
        return self.__id
    
    def set_id(self, nuevo_id):
        self.__id = nuevo_id    # Método para actualizar el ID

    def get_nombre_subgenero(self):
        return self.__nombre_subgenero

    def set_nombre_subgenero(self, value):
        self.__nombre_subgenero = value

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, value):
        self.__tipo = value


    def mostrar_datos_subgenero(self):
        """Muestra todos los datos del Género Literario. Actúa como método __str__"""
        return f"{super().mostrar_datos_genero()}\nId: {self.get_id()}.\nNombre Subgénero Literario: {self.get_nombre_subgenero()}({self.get_tipo() if self.get_tipo() else "Tipo no definido"})."
