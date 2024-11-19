# biblioteca/repositorios/repositorio_libro.py

from biblioteca.modelos.libro import Libro
from biblioteca.modelos.generos.especifico import Especifico
from biblioteca.utilidades.lector_json import cargar_datos_json

class RepositorioLibro:
    
    def __init__(self, repositorio_autor, repositorio_especifico):
        self.libros = []  # Lista donde se almacenarán los libros
        #self.diccionario_libros = {}  # Diccionario con libros indexados por su título
        self.repositorio_autor = repositorio_autor  # Repositorio de autores
        self.repositorio_genero = repositorio_especifico  # Repositorio de géneros

    def cargar_libros(self, datos_libros):
        """
        Carga los libros desde un archivo JSON utilizando la función cargar_datos_json.
        """
        # Cargar los datos desde el archivo JSON
        datos = cargar_datos_json()
        
        # Si los datos no son válidos (diccionario vacío), termina la función
        if not datos:
            return
        
        # Recorrer la lista de libros en el JSON
        for libro in datos_libros:
            # Buscar el autor en el repositorio de autores por pseudónimo
            autor = self.repositorio_autor.buscar_autor_nombre(libro["autor"].lower())
            if not autor:
                print(f"Autor {libro['autor']} no encontrado.")
                continue
            
            # Buscar el género en el repositorio de géneros por nombre
            especifico = self.repositorio_especifico.buscar_especifico_nombre(libro["especifico"].lower())
            if not especifico:
                print(f"Género y Subgénero Específico {libro['especifico']} no encontrado.")
                continue
            
            # Crear una instancia del tipo Especifico (se asume que 'especifico' es una categoría válida)
            especifico = Especifico(libro["especifico"])  # Este es solo un ejemplo de cómo se podría manejar
            
            print(f"Cargando Libro..\n'ID:'{libro['id']}\n'Título del Libro:'{libro['titulo']}\n'Género y Subgénero Específico:'{libro['especifico']} \
                'Fecha de Publicación:'{libro['fecha_publicacion']}\n'Num. Páginas:'{libro['num_paginas']}")

    # def agregar_libro(self, libro):
    #     """Agrega un libro nuevo al diccionario de libros de la biblioteca."""
    #     try:
    #         # Verifica que el libro no esté ya registrado
    #         if libro.get_titulo().lower() not in self.diccionario_libros:
    #             self.diccionario_libros[libro.get_titulo().lower()] = libro
    #             self.libros.append(libro)
    #     except Exception as e:
    #         print(f'Error al agregar el libro: {e}')

    # def buscar_libro_titulo(self, titulo):
    #     """Busca un libro por título en el diccionario de libros."""
    #     return self.diccionario_libros.get(titulo.lower(), None)

    # def mostrar_libros(self):
    #     """Devuelve una lista de todos los libros de la biblioteca."""
    #     return [libro.mostrar_datos_libro() for libro in self.diccionario_libros.values()]

    # def mostrar_libros_por_autor(self, autor):
    #     """Muestra todos los libros de un autor específico."""
    #     autor_buscado = autor.lower()
    #     libros_del_autor = [libro for libro in self.diccionario_libros.values() if libro.get_autor().get_pseudonimo().lower() == autor_buscado]
    #     return [libro.mostrar_datos_libro() for libro in libros_del_autor]

    # def mostrar_libros_por_genero(self, genero):
    #     """Muestra todos los libros de un género específico."""
    #     return [libro.mostrar_datos_libro() for libro in self.diccionario_libros.values() if libro.get_especifico().get_nombre().lower() == genero.lower()]

    # def mostrar_libros_especifico(self, especifico):
    #     """Muestra todos los libros de un subgénero específico."""
    #     return [libro.mostrar_datos_libro() for libro in self.diccionario_libros.values() if libro.get_especifico().get_nombre().lower() == especifico.lower()]

    # def reestructurar_ids_libros(self):
    #     """Reestructura los IDs de los libros, haciendo que sean consecutivos."""
    #     for index, libro in enumerate(self.libros):
    #         libro.set_id(index + 1)  # Actualiza los IDs para que empiecen desde 1
