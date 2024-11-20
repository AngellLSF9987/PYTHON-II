# biblioteca/repositorios/repositorio_libro.py

from biblioteca.modelos.libro import Libro
from biblioteca.modelos.generos.especifico import Especifico

class RepositorioLibro:
    
    def __init__(self, repositorio_autor, repositorio_especifico):
        """
        Constructor del repositorio de específicos.
        :param repositorio_especifico: Instancia de RepositorioEspecifico.
        :param repositorio_autor: Instancia de RepositorioAutor.
        """

        self.repositorio_autor = repositorio_autor  # Repositorio de autores
        self.repositorio_especifico = repositorio_especifico  # Repositorio de géneros
        self.libros = []  # Lista donde se almacenarán los libros

    def cargar_libros(self, datos_libros):
        """Carga los datos de los Subgéneros Literarios específicos desde el JSON en la memoria del repositorio."""
        try:
            self.libros = []
            for libro in datos_libros:
                especifico = self.repositorio_especifico.obtener_especifico_por_id(libro["especifico_id"])
                if especifico is None:
                    print(f"Aviso: No se encontró ningún Género y Subgénero Específicos con ID {libro['especifico_id']}.")
                    especifico_nombre = "Género desconocido"
                else:
                    especifico_nombre = especifico["nombre_especifico"]
                
                autor = self.repositorio_autor.obtener_autor_por_id(libro["autor_id"])
                if autor is None:
                    print(f"Aviso: No se encontró ningún Autor con ID {libro['autor_id']}.")
                    autor_nombre = "Autor desconocido"
                else:
                    autor_nombre = autor["pseudonimo"]
                
                self.libros.append({
                    "libro_id": libro.get("libro_id"),
                    "titulo": libro.get("titulo", "Desconocido"),
                    "especifico_id": especifico_nombre,
                    "fecha_publicacion": libro.get("fecha_publicacion", "Desconocido"),
                    "num_paginas": libro.get("num_paginas", "Desconocido"),
                    "autor_id": autor_nombre
                })
            print("Carga de datos de Libro correcta.")

        except KeyError as KeyEspecificoError:
            print(f"{KeyEspecificoError}: Falta la clave o no coincide en los datos de un Libro.")
        except FileExistsError as DictEspecificoError:
            print(f"{DictEspecificoError}: La sección de datos pertenciente a Libro registrados no ha sido cargada correctamente.")
        
    def mostrar_libros(self):
        """Devuelve la lista de libros en el repositorio."""
        if not self.libros:
            return "No hay autores cargados en el repositorio."
        return "\n".join(f"ID: {libro['libro_id']}\nTítulo del libro/a: {libro['titulo']}\nGénero y Subgénero Específico: {libro['especifico_id']}\n\
Fecha de Publicación: {libro['fecha_publicacion']}\nNum. Páginas: {libro['num_paginas']}\nAutor: {libro['autor_id']}\n"\
        for libro in self.libros)

    def obtener_libro_por_id(self, libro_id):
        """Busca un libro por su ID."""
        print(f"Buscando libro con ID {libro_id}...")  # Depuración
        for libro in self.libros:
            print(f"Comparando con libro: {libro_id}")  # Depuración
            if libro["libro_id"] == libro_id:
                return libro
        print(f"No se encontró un libro con ID {libro_id}.")  # Depuración
        return None
