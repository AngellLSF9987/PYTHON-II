from biblioteca.repositorios.repositorio_autor import RepositorioAutor
from biblioteca.repositorios.repositorio_genero import RepositorioGenero
from biblioteca.repositorios.repositorio_especifico import RepositorioEspecifico
from biblioteca.repositorios.repositorio_libro import RepositorioLibro
from biblioteca.utilidades.lector_json import cargar_datos_json
from biblioteca.utilidades.ruta_datos_json import RUTA_DATOS_BIBLIOTECA

import json

class Biblioteca:
    def __init__(self,ruta_json):
        """
        Inicializa la biblioteca cargando todos los repositorios y los datos desde el JSON.
        """
        # Inicialización de los repositorios
        self.ruta_json = ruta_json
        self.repositorio_autor = RepositorioAutor(RUTA_DATOS_BIBLIOTECA)
        self.repositorio_genero = RepositorioGenero(RUTA_DATOS_BIBLIOTECA)

        # Crear el repositorio de subgéneros específicos, pasando correctamente el repositorio de géneros
        self.repositorio_especifico = RepositorioEspecifico(RUTA_DATOS_BIBLIOTECA, self.repositorio_genero)

        self.repositorio_libro = RepositorioLibro(self.repositorio_autor, self.repositorio_especifico, RUTA_DATOS_BIBLIOTECA)

        # Cargar los datos desde el archivo JSON
        self.cargar_datos_biblioteca()

    def cargar_datos_biblioteca(self):
        """
        Carga los datos desde el JSON y los distribuye en los repositorios correspondientes.
        """
        try:
            self.datos_biblioteca = cargar_datos_json()  # Cargar datos desde JSON
            self.cargar_generos(self.datos_biblioteca.get('generos', []))
            self.cargar_especificos(self.datos_biblioteca.get('especificos', []))
            self.cargar_autores(self.datos_biblioteca.get('autores', []))
            self.cargar_libros(self.datos_biblioteca.get('libros', []))
        except Exception as e:
            print(f"Error al cargar los datos: {e}")

    def guardar_datos_biblioteca(self):
        """
        Guarda todos los datos de la biblioteca en el archivo JSON.
        """
        try:
            datos_a_guardar = {
                "autores": self.repositorio_autor.obtener_autores(),
                "generos": self.repositorio_genero.obtener_generos(),
                "especificos": self.repositorio_especifico.obtener_especificos(),
                "libros": self.repositorio_libro.obtener_libros(),
            }
            with open(RUTA_DATOS_BIBLIOTECA, 'w', encoding='utf-8') as archivo:
                json.dump(datos_a_guardar, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos en el archivo JSON: {e}")

    def obtener_datos_seccion(self, seccion):
        """
        Obtiene los datos de una sección específica del JSON.
        Parámetro - seccion: Nombre de la sección (e.g., "autores", "libros").
        Devuelve - Lista de datos de la sección o una lista vacía si no existe.
        """
        datos = self.datos_biblioteca.get(seccion, [])
        if not isinstance(datos, list):
            print(f"Aviso: La sección '{seccion}' no contiene una lista válida.")
            return []
        return datos

    def cargar_autores(self, datos_autores):
        """
        Carga los datos de los autores en el repositorio correspondiente.
        Parámetro - datos_autores: Lista de diccionarios con datos de autores.
        """
        if not datos_autores:
            print("No hay datos de autores para cargar.")
            return

        for autor in datos_autores:
            if isinstance(autor, dict):
                self.repositorio_autor.agregar_autor(autor)
            else:
                print(f"Formato inválido para autor: {autor}")

    def cargar_generos(self, datos_generos):
        """
        Carga los datos de los géneros en el repositorio correspondiente.
        Parámetro - datos_generos: Lista de diccionarios con datos de géneros.
        """
        if not datos_generos:
            print("No hay datos de géneros para cargar.")
            return

        for genero in datos_generos:
            if isinstance(genero, dict):
                self.repositorio_genero.agregar_genero(genero)
            else:
                print(f"Formato inválido para género: {genero}")

    def cargar_especificos(self, datos_especificos):
        """
        Carga los datos de los subgéneros específicos en el repositorio correspondiente.
        Parámetro - datos_especificos: Lista de diccionarios con datos de subgéneros.
        """
        if not datos_especificos:
            print("No hay datos de subgéneros específicos para cargar.")
            return

        for especifico in datos_especificos:
            if isinstance(especifico, dict):
                self.repositorio_especifico.agregar_especifico(especifico)
            else:
                print(f"Formato inválido para subgénero: {especifico}")

    def cargar_libros(self, datos_libros):
        """
        Carga los datos de los libros en el repositorio correspondiente.
        Parámetro - datos_libros: Lista de diccionarios con datos de libros.
        """
        if not datos_libros:
            print("No hay datos de libros para cargar.")
            return

        for libro in datos_libros:
            if isinstance(libro, dict):
                self.repositorio_libro.agregar_libro(libro)
            else:
                print(f"Formato inválido para libro: {libro}")

    def mostrar_todo(self):
        """
        Muestra todos los datos cargados en la biblioteca.
        """
        print("=== AUTORES ===")
        print(self.repositorio_autor.mostrar_autores())

        print("\n=== GÉNEROS ===")
        print(self.repositorio_genero.mostrar_generos())

        print("\n=== SUBGÉNEROS ===")
        print(self.repositorio_especifico.mostrar_especificos())

        print("\n=== LIBROS ===")
        print(self.repositorio_libro.mostrar_libros())
