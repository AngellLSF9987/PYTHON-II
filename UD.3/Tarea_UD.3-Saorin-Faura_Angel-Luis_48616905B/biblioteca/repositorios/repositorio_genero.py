# biblioteca/repositorios/repositorio_genero.py

import json
class RepositorioGenero:
    
    def __init__(self, ruta_json):
        """Constructor del repositorio de géneros."""
        self.generos = []  # Lista para almacenar instancias de Genero
        self.ruta_json = ruta_json  # Ruta al archivo JSON

    def agregar_generos(self, datos_generos):
        """Carga una lista completa de géneros en el repositorio."""
        try:
            for genero in datos_generos:
                self.agregar_genero(genero)
            print("Carga de datos de Géneros Literarios correcta.")
        except Exception as e:
            print(f"Error al cargar géneros: {e}")

    def agregar_genero(self, genero):
        """Agrega un único género al repositorio."""
        if isinstance(genero, dict) and "genero_id" in genero:
            if not self.obtener_genero_por_id(genero["genero_id"]):
                self.generos.append({
                    "genero_id": genero["genero_id"],
                    "nombre_genero": genero.get("nombre_genero", "Desconocido")
                })
            else:
                print(f"El género con ID {genero['genero_id']} ya existe.")
        else:
            print(f"Formato inválido para género: {genero}")

    def mostrar_generos(self):
        """Devuelve la lista de géneros literarios en el repositorio."""
        if not self.generos:
            return "No hay géneros literarios cargados en el repositorio."
        print("Géneros cargados:", self.generos)  # Verifica los géneros cargados
        return "\n".join(f"ID: {genero['genero_id']}\nNombre del Género Literario: {genero['nombre_genero']}" for genero in self.generos)

    def obtener_genero_por_id(self, genero_id):
        """Busca un género por su ID."""
        # Convertir el ID a string para garantizar coincidencia
        genero_id = str(genero_id)
        for genero in self.generos:
            if str(genero["genero_id"]) == genero_id:
                return genero
        return None