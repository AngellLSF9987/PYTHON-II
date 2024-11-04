# biblioteca/modelos/biblioteca.py

from .libro import Libro
from ..utilidades.validaciones import validar_fecha

class Biblioteca:
    def __init__(self):
        """Método constructor a partir de la instanciación de un diccionario vacío donde quedarán alojados los objetos libro existentes o creados."""
        self.libros = []
        self.inicializar_biblioteca() # Llamada al método de inicialización

    def agregar_libro(self, libro):
        """- Agrega un libro nuevo a la lista de libros de la biblioteca. """
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        """Busca un libro usando el método get_titulo(), que encapsula el atributo título, como referencia de la búsqueda. 
           Devuelve el objeto si se encuentra en la lista."""
        for libro in self.libros:
            if libro.get_titulo().lower() == titulo.lower(): # Uso del método get_titulo(), que encapsula el atributo título.
                return libro
        return None

    def reestructurar_ids(self):
        for index, libro in enumerate(self.libros):
            libro.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.

    def mostrar_libros(self):
        """Devuelve una lista completa de todos los libros existentes en la Biblioteca."""
        return [libro.mostrar_datos() for libro in self.libros]
    
    def mostrar_libros_por_autor(self, autor):
        """Muestra todos los libros existentes, publicados por un autor específico."""
        return [libro for libro in self.libros if libro.get_autor().lower() == autor.lower()]
        
    def paginas_por_libro(self, titulo):
        """Devuelve el número de páginas que tiene un libro."""
        libro = self.buscar_libro(titulo)
        if libro:
            return libro.get_num_paginas()
        else:
            return "El libro no se encuentra en el listado de registros de la Biblioteca."
        
    def inicializar_biblioteca(self):
            """Lista de libros registrados ya en la Biblioteca."""
            libros_existentes = [
                {
                    "titulo": "Cien años de soledad",
                    "autor": "Gabriel García Márquez",
                    "fecha_publicacion": "05-06-1967",
                    "num_paginas": 417
                },
                {
                    "titulo": "El hobbit",
                    "autor": "J.R.R. Tolkien",
                    "fecha_publicacion": "21-09-1937",
                    "num_paginas": 310
                },
                {
                    "titulo": "1984",
                    "autor": "George Orwell",
                    "fecha_publicacion": "08-06-1949",
                    "num_paginas": 328
                },
                {
                    "titulo": "Matar a un ruiseñor",
                    "autor": "Harper Lee",
                    "fecha_publicacion": "11-07-1960",
                    "num_paginas": 281
                },
                {
                    "titulo": "El Resplandor",
                    "autor": "Stephen King",
                    "fecha_publicacion": "28-01-1977",
                    "num_paginas": 688
                }
            ]

            for libro_info in libros_existentes:
                fecha_publicacion = validar_fecha(libro_info["fecha_publicacion"])

                if fecha_publicacion:
                    libro = Libro(libro_info["titulo"], libro_info["autor"], fecha_publicacion, libro_info["num_paginas"])
                    self.agregar_libro(libro)
            print("Biblioteca inicializada con registros de libros.")