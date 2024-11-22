# biblioteca/repositorios/repositorio_genero.py

import json
class RepositorioGenero:
    
    def __init__(self, ruta_json):
        """Constructor del repositorio de Géneros Literarios."""
        self.generos = []  # Lista para almacenar instancias de Genero
        self.ruta_json = ruta_json  # Ruta al archivo JSON

    def cargar_generos(self, datos_generos):
        """Carga una lista completa de Géneros Literarios en el repositorio."""
        try:
            self.generos.extend(datos_generos)
            print("Carga de datos de Géneros Literarios correcta.")
        except Exception as e:
            print(f"Error al cargar Géneros Literarios: {e}")

    def obtener_generos(self):
        """Retorna la lista de géneros."""
        return self.generos

    def buscar_genero_por_nombre(self, nombre_genero):
        """Busca un género por su nombre."""
        generos = self.obtener_generos()  # Obtener la lista de géneros
        for genero in generos:
            if genero['nombre_genero'].lower() == nombre_genero.lower():
                return genero
        return None  # Retorna None si no se encuentra el género

    def guardar_datos(self):
        """Guarda los datos actuales en el archivo JSON."""
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump({"generos": self.datos}, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

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
        # print("Géneros cargados:", self.generos)  # Verifica los géneros cargados
        return "\n".join(f"ID: {genero['genero_id']}\nNombre del Género Literario: {genero['nombre_genero']}" for genero in self.generos)
    
    def obtener_genero_por_id(self, genero_id):
        """Devuelve un género dado su ID.
        Convertir el ID a string para garantizar coincidencia."""
        return next((genero for genero in self.generos if str(genero['genero_id']) == str(genero_id)), None)
