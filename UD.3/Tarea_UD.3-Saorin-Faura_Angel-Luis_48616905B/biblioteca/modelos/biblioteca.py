# biblioteca/modelos/biblioteca.py

from biblioteca.repositorios.repositorio_autor import RepositorioAutor
from biblioteca.repositorios.repositorio_genero import RepositorioGenero
from biblioteca.repositorios.repositorio_especifico import RepositorioEspecifico
from biblioteca.repositorios.repositorio_libro import RepositorioLibro

from biblioteca.utilidades.ruta_datos_json import RUTA_DATOS_BIBLIOTECA
from biblioteca.utilidades.lector_json import cargar_datos_json

class Biblioteca:
    def __init__(self):
        """
        Constructor de la clase Biblioteca.
        Inicializa repositorios para almacenar libros, autores, géneros y específicos.
        """
        # Inicializamos los repositorios
        self.repositorio_autor = RepositorioAutor()
        self.repositorio_genero = RepositorioGenero()
        self.repositorio_especifico = RepositorioEspecifico(self.repositorio_genero)
        
        # El repositorio de libros necesita los repositorios de autor y específico (repositorio especifico ya contiene los datos de repositorio género)
        self.repositorio_libro = RepositorioLibro(self.repositorio_autor, self.repositorio_especifico)
        
        # Inicializar biblioteca con los datos del archivo JSON
        self.inicializar_biblioteca()

    def inicializar_biblioteca(self):
        """
        Inicializa la biblioteca cargando datos desde el archivo JSON.
        """
        # Cargar datos desde el JSON
        datos = cargar_datos_json(RUTA_DATOS_BIBLIOTECA)
        
        # Cargar cada sección de datos si están presentes en el JSON
        self.repositorio_autor.cargar_autores(datos.get("autores", []))
        self.repositorio_genero.cargar_generos(datos.get("generos", []))
        self.repositorio_especifico.cargar_especificos(datos.get("especificos", []))
        self.repositorio_libro.cargar_libros(datos.get("libros", []))
