# biblioteca/repositorios/repositorio_genero.py

from biblioteca.utilidades.lector_json import cargar_datos_json

from biblioteca.modelos.generos.genero import Genero

class RepositorioGenero:
    def __init__(self):
        """Constructor del repositorio de géneros."""
        self.generos = []  # Lista para almacenar instancias de Genero

    def cargar_generos(self, datos_generos):
        """
        Carga los datos de géneros en el repositorio.
        :param generos: Lista de diccionarios con los datos de géneros.
        """
        # Cargar los datos desde el archivo JSON
        datos = cargar_datos_json()
        # Si los datos no son válidos (diccionario vacío), termina la función
        if not datos:
            return
        
        for genero in datos_generos:
            print(f"Cargando Género..\n'ID:'{genero['id']}\n'Nombre del Género Literario:'{genero['nombre_genero']}")

    # def obtener_genero_por_id(self, id_genero):
    #     """
    #     Devuelve un género por su ID.
    #     :param id_genero: Identificador del género.
    #     :return: Instancia de Genero o None si no se encuentra.
    #     """
    #     for genero in self.__generos:
    #         if genero.id_genero == id_genero:
    #             return genero
    #     return None

    # def obtener_generos(self):
    #     """Devuelve la lista de géneros almacenados."""
    #     return self.__generos
