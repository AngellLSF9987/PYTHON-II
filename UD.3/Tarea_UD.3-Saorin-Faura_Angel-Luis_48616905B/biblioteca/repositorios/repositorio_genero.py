# biblioteca/repositorios/repositorio_genero.py

import json
class RepositorioGenero:
    def __init__(self):
        """Constructor del repositorio de géneros."""
        self.generos = []  # Lista para almacenar instancias de Genero

    def cargar_generos(self, datos_generos):
        """Carga los datos de los Géneros Literarios desde el JSON en la memoria del repositorio."""
        try:
            self.generos = [
                {
                    "genero_id": genero.get("genero_id"),
                    "nombre_genero": genero.get("nombre_genero", "Desconocido") 
                }
                for genero in datos_generos
            ]
            print("Carga de datos de Géneros Literarios correcta.")

        except FileExistsError as DictGenderError:
            print(f"{DictGenderError}: La sección de datos pertenciente a Géneros Literarios registrados no ha sido cargada correctamente.")

    def mostrar_generos(self):
        """Devuelve la lista de géneros literarios en el repositorio."""
        if not self.generos:
            return "No hay géneros literarios cargados en el repositorio."
        return "\n".join(f"ID: {genero['genero_id']}\nNombre del Género Literario: {genero['nombre_genero']}" for genero in self.generos)

    def obtener_genero_por_id(self, genero_id):
        """Busca un género por su ID."""
        print(f"Buscando género con ID {genero_id}...")  # Depuración
        for genero in self.generos:
            print(f"Comparando con género: {genero}")  # Depuración
            if genero["genero_id"] == genero_id:
                return genero
        print(f"No se encontró un género con ID {genero_id}.")  # Depuración
        return None