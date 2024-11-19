# biblioteca/repositorios/repositorio_especifico.py

from biblioteca.utilidades.lector_json import cargar_datos_json
from biblioteca.modelos.generos.especifico import Especifico

class RepositorioEspecifico:
    def __init__(self, repositorio_genero):
        """
        Constructor del repositorio de específicos.
        :param repositorio_genero: Instancia de RepositorioGenero.
        """
        self.__repositorio_genero = repositorio_genero
        self.__especificos = []  # Lista para almacenar instancias de Especifico

    def cargar_especificos(self, especificos):
        """
        Carga los datos de específicos en el repositorio.
        :param especificos: Lista de diccionarios con los datos de específicos.
        """
        for dato in especificos:
            genero = self.__repositorio_genero.obtener_genero_por_id(dato["id_genero"])
            especifico = Especifico(
                id_especifico=dato["id_especifico"],
                descripcion=dato["descripcion"],
                id_genero=genero.id_genero,
                nombre_genero=genero.nombre_genero
            )
            self.__especificos.append(especifico)

    def obtener_especificos(self):
        """Devuelve la lista de específicos almacenados."""
        return self.__especificos

    def mostrar_especificos(self):
        """Muestra información de todos los específicos almacenados."""
        for especifico in self.__especificos:
            print(f"ID: {especifico.id_especifico}, Descripción: {especifico.descripcion}, "
                  f"Género: {especifico.nombre_genero}")
