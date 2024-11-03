# Biblioteca/modelos/libro.py

from datetime import date

class Libro:

    __id_counter = 1 # Contador para los registros existentes y los nuevos que se añadan

    def __init__(self, titulo, autor, fecha_publicacion, num_paginas):

        self.__id = Libro.__id_counter  # Asigna el ID actual, es decir, el ID = 1
        Libro.__id_counter += 1         # Contador autoincremental

        self.__titulo = titulo
        self.__autor = autor
        self.__fecha_publicacion = fecha_publicacion
        self.__num_paginas = num_paginas

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, value):
        self.__titulo = value

    def get_autor(self):
        return self.__autor

    def set_autor(self, value):
        self.__autor = value

    def get_fecha_publicacion(self):
        return self.__fecha_publicacion
    
    def set_fecha_publicacion(self, value):
        self.__fecha_publicacion = value

    def get_num_paginas(self):
        return self.__num_paginas

    def set_num_paginas(self, value):
        self.__num_paginas = value

    def mostrar_datos(self):
        """Muestra todos los datos del cliente. Actúa como método __str__"""
        return f"Id:Id: {self.get_id()}\nTítulo: {self.get_titulo()}.\nAutor: {self.get_autor()}.\nFecha Publicación: {self.get_fecha_publicacion()}.\nNº Páginas: {self.get_num_paginas()}.\n" 