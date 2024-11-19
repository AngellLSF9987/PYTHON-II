# biblioteca/repositorios/repositorio_especifico.py

from biblioteca.utilidades.lector_json import cargar_datos_json
from biblioteca.modelos.generos.especifico import Especifico

class RepositorioEspecifico:
    def __init__(self, repositorio_genero):
        """
        Constructor del repositorio de específicos.
        :param repositorio_genero: Instancia de RepositorioGenero.
        """
        self.repositorio_genero = repositorio_genero
        self.especificos = []  # Lista para almacenar instancias de Especifico

    def cargar_especificos(self, datos_especificos):
        """
        Carga los datos de específicos en el repositorio.
        :param especificos: Lista de diccionarios con los datos de específicos.
        """
        # Cargar los datos desde el archivo JSON
        datos = cargar_datos_json()
        
        # Si los datos no son válidos (diccionario vacío), termina la función
        if not datos:
            return
        
        for especifico in datos_especificos:
            genero = self.repositorio_genero.obtener_genero_por_id(genero["id_genero"])
            
            print(f"Cargando Género y Subgénero Específico..\n'ID:'{especifico['id']}\n'Nombre del Género:'{especifico['genero']}\n \
                'Nombre del Subgénero:'{especifico['nombre_especifico']}\n'Tipo de Subgénero:'{especifico['tipo']}")

    # def obtener_especificos(self):
    #     """Devuelve la lista de específicos almacenados."""
    #     return self.__especificos

    # def mostrar_especificos(self):
    #     """Muestra información de todos los específicos almacenados."""
    #     for especifico in self.__especificos:
    #         print(f"ID: {especifico.id_especifico}, Descripción: {especifico.descripcion}, "
    #               f"Género: {especifico.nombre_genero}")
