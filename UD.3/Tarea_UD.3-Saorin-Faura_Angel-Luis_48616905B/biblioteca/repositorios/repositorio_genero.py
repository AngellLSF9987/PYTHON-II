from biblioteca.utilidades.lector_json import cargar_datos_json
from biblioteca.modelos.generos.genero import Genero

class RepositorioGenero:
        
    def __init__(self):
        """Inicializa el repositorio con una lista de géneros y un diccionario de géneros."""
        self.generos = []  # Lista para almacenar los objetos Genero
        self.diccionario_generos = {}  # Diccionario para buscar géneros por nombre_genero

    def cargar_generos(self, datos_biblioteca):
        """
        Carga la lista de géneros literarios en el repositorio.

        Args:
            lista_generos (list): Una lista de diccionarios con los nombres de los géneros a cargar.
        """
        # Cargar los datos desde el archivo JSON
        datos = cargar_datos_json(datos_biblioteca)
        
        # Si los datos no son válidos (diccionario vacío), termina la función
        if not datos:
            print(f"Error: No se pudo cargar el archivo {datos_biblioteca}.")
            return
        
        for genero_data in datos.get("generos", []):
            nuevo_genero = Genero(
                    genero_data["nombre_genero"]
            )
            # Añadir el género a la lista de géneros
            self.generos.append(nuevo_genero)
            # Añadir el género al diccionario, usando su nombre en minúsculas como clave
            self.diccionario_generos[nuevo_genero.get_nombre_genero().lower()] = nuevo_genero
        
        print(f"Generos cargados desde {datos_biblioteca}")
        
    def agregar_genero(self, genero):
        """
        Agrega un nuevo género literario al repositorio.

        Args:
            genero (Genero): Un objeto Genero que representa el género a agregar.
        """
        if isinstance(genero, Genero):
            self.generos.append(genero)
            self.diccionario_generos[genero.get_nombre_genero().lower()] = genero
        else:
            raise ValueError("El parámetro debe ser un objeto de tipo Genero.")

    def buscar_genero_nombre(self, nombre_genero):
        """
        Busca un género literario por su nombre en el repositorio.

        Args:
            nombre_genero (str): El nombre del género a buscar.

        Returns:
            Genero: El objeto Genero encontrado o None si no se encuentra.
        """
        return self.diccionario_generos.get(nombre_genero.lower(), None)

    def mostrar_generos(self):
        """
        Devuelve una lista con las representaciones en cadena de todos los géneros en el repositorio.

        Returns:
            list: Lista de cadenas con los detalles de cada género.
        """
        return [genero.__str__() for genero in self.generos]

    def reestructurar_ids_generos(self):
        """
        Reestructura los IDs de los géneros para que sean consecutivos, empezando desde 1.
        """
        for index, genero in enumerate(self.generos):
            genero.set_id(index + 1)  # Actualiza los ids, asegurando que sean consecutivos
