# biblioteca/modelos/biblioteca.py

from biblioteca.modelos.libro import Libro
from biblioteca.modelos.autor import Autor
from biblioteca.modelos.generos.genero import Genero
from biblioteca.modelos.generos.especifico import Especifico
from biblioteca.utilidades.validaciones import validar_fecha

class Biblioteca:
    def __init__(self):
        """Método constructor a partir de la instanciación de un diccionario vacío donde quedarán alojados los objetos libro existentes o creados."""
        self.libros = []
        self.generos = []
        self.especificos = []       
        self.autores = []
        
        # Diccionarios de búsqueda rápida
        self.diccionario_libros = {}
        self.diccionario_autores = {}
        self.diccionario_generos = {}
        self.diccionario_especificos = {}
        
        self.inicializar_biblioteca() # Llamada al método de inicialización


    def inicializar_biblioteca(self):
        """Inicializa la biblioteca con autores, géneros literarios y libros registrados ya en la Biblioteca."""
