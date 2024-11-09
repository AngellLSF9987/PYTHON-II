# biblioteca/modelos/biblioteca.py

from biblioteca.modelos.libro import Libro
from biblioteca.modelos.autor import Autor
from biblioteca.modelos.generos.genero import Genero
from biblioteca.modelos.generos.subgenero import Subgenero
from biblioteca.utilidades.validaciones import validar_fecha

class Biblioteca:
    def __init__(self):
        """Método constructor a partir de la instanciación de un diccionario vacío donde quedarán alojados los objetos libro existentes o creados."""
        self.libros = []
        self.generos = []
        self.subgeneros = []       
        self.autores = []
        self.inicializar_biblioteca() # Llamada al método de inicialización

#####   1.    REGION INTERFAZ GESTIÓN BIBLIOTECA - LIBROS     #####

    def agregar_libro(self, libro):
        """- Agrega un libro nuevo a la lista de libros de la biblioteca. """
        self.libros.append(libro)

    def buscar_libro_titulo(self, titulo):
        """Busca un libro usando el método get_titulo(), que encapsula el atributo título, como referencia de la búsqueda. 
           Devuelve el objeto si se encuentra en la lista."""
        for libro in self.libros:
            if libro.get_titulo().lower() == titulo.lower(): # Uso del método get_titulo(), que encapsula el atributo título.
                return libro
        return None

    def reestructurar_ids_libros(self):
        for index, libro in enumerate(self.libros):
            libro.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.

    def mostrar_libros(self):
        """Devuelve una lista completa de todos los libros existentes en la Biblioteca."""
        return [libro.mostrar_datos_libro() for libro in self.libros]
    
    def mostrar_libros_por_autor(self, autor):
        """Muestra todos los libros existentes, publicados por un autor específico."""
        return [libro for libro in self.libros if libro.get_autor().lower() == autor.lower()]
    
    def mostrar_libros_por_genero(self, genero):
        """Muestra todos los libros existentes, publicados por un genero específico."""
        return [libro for libro in self.libros if libro.get_genero().lower() == genero.lower()]

#####       FIN REGION INTERFAZ GESTIÓN BIBLIOTECA - LIBROS     #####

#####   2.    REGION INTERFAZ GESTIÓN BIBLIOTECA - AUTORES     #####

def agregar_autor(self, autor):
    """- Agrega un autor nuevo a la lista de autores de la biblioteca. """
    self.autores.append(autor)

def buscar_autor_nombre(self, nombre):
    """- Busca un autor específico, usando la propiedad nombre, en la lista de autores. Devuelve el objeto Autor buscado si existe."""
    for autor in self.autores:
        if autor.get_nombre().lower() == nombre.lower():
            return autor
    return None

def reestructurar_ids_autores(self):
    for index, autor in enumerate(self.autores):
        autor.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.

def mostrar_autores(self):
    """Devuelve una lista completa de todos los autores existentes en la Biblioteca."""
    return [autor.mostrar_datos_autor() for autor in self.autores]

#####       FIN REGION INTERFAZ GESTIÓN BIBLIOTECA - AUTORES     #####

#####   3.    REGION INTERFAZ GESTIÓN BIBLIOTECA - GÉNEROS Y SUBGÉNEROS LITERARIOS    #####

            ####   3.1.     GÉNEROS LITERARIOS      ####

def agregar_genero(self, genero):
    """- Agrega un género literario nuevo a la lista de generos de la biblioteca. """
    self.generos.append(genero)

def buscar_genero_nombre(self, nombre_genero):
    """- Busca un género literario específico, usando la propiedad nombre, en la lista de generos. Devuelve el objeto Género buscado si existe."""
    for genero in self.generos:
        if genero.get_nombre_genero().lower() == nombre_genero.lower():
            return genero
    return None

def reestructurar_ids_generos(self):
    for index, genero in enumerate(self.generos):
        genero.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.

def mostrar_generos(self):
    """Devuelve una lista completa de todos los géneros literarios existentes en la Biblioteca."""
    return [genero.mostrar_datos_genero() for genero in self.generos]

            ####   3.2.     SUBGÉNEROS LITERARIOS      ####

def agregar_subgenero(self, subgenero):
    """- Agrega un género literario nuevo a la lista de generos de la biblioteca. """
    self.subgeneros.append(subgenero)

def buscar_genero_nombre(self, nombre_subgenero):
    """- Busca un género literario específico, usando la propiedad nombre, en la lista de generos. Devuelve el objeto Género buscado si existe."""
    for subgenero in self.subgeneros:
        if subgenero.get_nombre_subgenero().lower() == nombre_subgenero.lower():
            return subgenero
    return None

def reestructurar_ids_subgeneros(self):
    for index, subgenero in enumerate(self.subgeneros):
        subgenero.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.

def mostrar_subgeneros(self):
    """Devuelve una lista completa de todos los géneros literarios existentes en la Biblioteca."""
    return [subgenero.mostrar_datos_subgenero() for subgenero in self.subgeneros]

#####       FIN REGION INTERFAZ GESTIÓN BIBLIOTECA - GÉNEROS Y SUBGÉNEROS LITERARIOS     #####


#####   4.    REGION INICIALIZACIÓN DE LA INTERFAZ BIBLIOTECA CON OBJETOS AÑADIDOS     #####

def inicializar_biblioteca(self):
    """Inicializa la biblioteca con autores, géneros literarios y libros registrados ya en la Biblioteca."""

    # Inicializar lista de Autores

    autores_existentes = [
        {"nombre": "Gabriel", "apellido1": "García", "apellido2": "Márquez", "conocido":" " ,"nacido": "06-03-1927", "fallecido": "17-04-2014", "nacionalidad": "Colombiano"},
        {"nombre": "Jhon Ronald", "apellido1": "Reuel", "apellido2": "Tolkien","conocido":"J.R.R. Tolkien", "nacido": "03-01-1892", "fallecido": "02-09-1973", "nacionalidad": "Británico"},
        {"nombre": "Eric", "apellido1": "Arthur", "apellido2": "Blair","conocido":"George Orwell", "nacido": "25-06-1903", "fallecido": "21-01-1950", "nacionalidad": "Británico"},
        {"nombre": "Stephen", "apellido1": "Edwing", "apellido2": "King","conocido":"Stephen King", "nacido": "21-09-1947", "fallecido": "No fallecido", "nacionalidad": "EE.UU"},
        {"nombre": "Nelle", "apellido1": "Harper", "apellido2": "Lee","conocido":"Harper Lee", "nacido": "28-04-1926", "fallecido": "19-02-2016", "nacionalidad": "EE.UU"},
    ]

    for autor_info in autores_existentes:
        autor = Autor(autor_info["nombre"], autor_info["apellido1"], autor_info["apellido2"], autor_info["conocido"], autor_info["nacido"], autor_info["fallecido"], autor_info["nacionalidad"])
        self.agregar_autor(autor)

    # Inicializar lista de Géneros Literarios

    generos_existentes = [
        {"nombre_genero":"Narrativo"},
        {"nombre_genero":"Lírico"},
        {"nombre_genero":"Drámatico"},
        {"nombre_genero":"Didáctico"},
    ]

    for genero_info in generos_existentes:
        genero = Genero(genero_info["nombre_genero"])
        self.agregar_genero(genero)

    # Inicializar lista de Subgéneros Literarios

    subgeneros_existentes = [
        {"nombre_genero":"Narrativo","nombre_subgenero":"Novela"},
        {"nombre_genero":"Narrativo","nombre_subgenero":"Cuento"},
        {"nombre_genero":"Narrativo","nombre_subgenero":"Fábula"},
        {"nombre_genero":"Narrativo","nombre_subgenero":"Leyenda"},
        {"nombre_genero":"Lírico","nombre_subgenero":"Égloga"},
        {"nombre_genero":"Lírico","nombre_subgenero":"Sátira"},
        {"nombre_genero":"Lírico","nombre_subgenero":"Soneto"},
        {"nombre_genero":"Lírico","nombre_subgenero":"Himno"},
        {"nombre_genero":"Dramático","nombre_subgenero":"Tragedia"},
        {"nombre_genero":"Dramático","nombre_subgenero":"Drama"},
        {"nombre_genero":"Dramático","nombre_subgenero":"Comedia"},
        {"nombre_genero":"Didáctico","nombre_subgenero":"Ensayo"},
        {"nombre_genero":"Dramático","nombre_subgenero":"Biografía"},
        {"nombre_genero":"Dramático","nombre_subgenero":"Carta"},
        {"nombre_genero":"Dramático","nombre_subgenero":"Artículo Científico"},
        {"nombre_genero":"Dramático","nombre_subgenero":"Discurso"}
    ]

    for subgenero_info in subgeneros_existentes:
        subgenero = Subgenero(subgenero_info["nombre_genero"], subgenero_info["nombre_subgenero"])
        self.agregar_subgenero(subgenero)


    # Inicializar lista de Libros

    libros_existentes = [
                {
                    "titulo": "Cien años de soledad",
                    "autor": "Gabriel García Márquez",
                    "genero": "Narrativo",
                    "subgenero": "Novela",
                    "fecha_publicacion": "05-06-1967",
                    "num_paginas": 417
                },
                {
                    "titulo": "El hobbit",
                    "autor": "J.R.R. Tolkien",
                    "genero": "Narrativo",
                    "subgenero": "Novela",
                    "fecha_publicacion": "21-09-1937",
                    "num_paginas": 310
                },
                {
                    "titulo": "1984",
                    "autor": "George Orwell",
                    "genero": "Narrativo",
                    "subgenero": "Novela",                    
                    "fecha_publicacion": "08-06-1949",
                    "num_paginas": 328
                },
                {
                    "titulo": "Matar a un ruiseñor",
                    "autor": "Harper Lee",
                    "genero": "Narrativo",
                    "subgenero": "Novela",
                    "tipo": "Suspense",                    
                    "fecha_publicacion": "11-07-1960",
                    "num_paginas": 281
                },
                {
                    "titulo": "El Resplandor",
                    "autor": "Stephen King",
                    "genero": "Narrativo",
                    "subgenero": "Novela",
                    "fecha_publicacion": "28-01-1977",
                    "num_paginas": 688
                }
            ]

    for libro_info in libros_existentes:
        fecha_publicacion = validar_fecha(libro_info["fecha_publicacion"])

        if fecha_publicacion:
            libro = Libro(libro_info["titulo"], libro_info["autor"], libro_info["genero"], libro_info["subgenero"], fecha_publicacion, libro_info["num_paginas"])
            self.agregar_libro(libro)
    print("Biblioteca inicializada con registros de libros.")