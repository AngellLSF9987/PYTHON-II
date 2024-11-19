# biblioteca/modelos/biblioteca.py

from biblioteca.repositorios.repositorio_autor import RepositorioAutor
from biblioteca.repositorios.repositorio_genero import RepositorioGenero
from biblioteca.repositorios.repositorio_especifico import RepositorioEspecifico
from biblioteca.repositorios.repositorio_libro import RepositorioLibro
from biblioteca.utilidades.lector_json import cargar_datos_json

class Biblioteca:
    def __init__(self):
        """
        Constructor de la clase Biblioteca.
        Inicializa repositorios para almacenar libros, autores, géneros y específicos.
        """
        self.datos_biblioteca = {}  # Diccionario para almacenar los datos JSON cargados
        self.repositorio_autor = RepositorioAutor()
        self.repositorio_genero = RepositorioGenero()
        self.repositorio_especifico = RepositorioEspecifico(self.repositorio_genero)
        self.repositorio_libro = RepositorioLibro(self.repositorio_autor, self.repositorio_especifico)
        self.cargar_datos_biblioteca()  # Carga los datos del archivo JSON sin procesarlos

    def cargar_datos_biblioteca(self):
        """Carga los datos desde el archivo JSON y los guarda internamente."""
        try:
            self.datos_biblioteca = cargar_datos_json()
        except FileNotFoundError as e:
            print(f"Error: No se encontró el archivo en la ruta especificada:\n{e}")

    def obtener_datos_seccion(self, seccion):
        """Obtiene los datos de una sección específica ('autores', 'libros', etc.) del JSON."""
        return self.datos_biblioteca.get(seccion, [])
