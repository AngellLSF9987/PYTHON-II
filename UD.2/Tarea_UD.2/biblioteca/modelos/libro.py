# biblioteca/modelos/libro.py

# from datetime import date
from biblioteca.modelos.autor import Autor
from biblioteca.modelos.generos.genero import Genero
from biblioteca.modelos.generos.subgenero import Subgenero
class Libro:

    __id_counter = 1 # Contador para los registros existentes y los nuevos que se añadan

    def __init__(self, titulo, autor, genero, subgenero, fecha_publicacion, num_paginas):

        self.__id = Libro.__id_counter  # Asigna el ID actual, es decir, el ID = 1
        Libro.__id_counter += 1         # Contador autoincremental

        self.__titulo = titulo
        self.__autor = autor        
        self.__genero = genero
        self.__subgenero = subgenero
        self.__fecha_publicacion = fecha_publicacion
        self.__num_paginas = num_paginas

    def get_id(self):
        return self.__id

    def set_id(self, nuevo_id):
        self.__id = nuevo_id    # Método para actualizar el ID

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, value):
        self.__titulo = value

    def get_autor(self):
        return self.__autor

    def set_autor(self, value):
        self.__autor = value        

    def get_genero(self):
        return self.__genero

    def set_genero(self, value):
        self.__genero = value

    def get_subgenero(self):
        return self.__subgenero

    def set_subgenero(self, value):
        self.__subgenero = value       

    def get_fecha_publicacion(self):
        return self.__fecha_publicacion
    
    def set_fecha_publicacion(self, value):
        self.__fecha_publicacion = value

    def get_num_paginas(self):
        return self.__num_paginas

    def set_num_paginas(self, value):
        self.__num_paginas = value

    def mostrar_datos_libro(self):
        """Muestra todos los datos del libro. Actúa como método __str__"""
        return f"Id: {self.get_id()}.\nTítulo: {self.get_titulo()}.\nAutor: {self.get_autor()}.\nGénero Literario: {self.get_genero()}.\nSubgénero Literario: {self.get_subgenero()}.\nFecha Publicación: {self.get_fecha_publicacion()}.\nNº Páginas: {self.get_num_paginas()}.\n" 