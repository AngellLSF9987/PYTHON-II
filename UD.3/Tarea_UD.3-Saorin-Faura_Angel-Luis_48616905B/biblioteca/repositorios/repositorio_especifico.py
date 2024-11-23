import json
from biblioteca.modelos.generos.genero import Genero
class RepositorioEspecifico:
    def __init__(self, ruta_json):
        
        self.ruta_json = ruta_json
        self.datos = self._cargar_especificos()
        self.especificos = self.datos.get("especificos", [])

    def _cargar_especificos(self):
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)
                print("Subgéneros cargados correctamente.")
                return data  # Retorna directamente el contenido del archivo
        except (FileNotFoundError, json.JSONDecodeError):
            print("Archivo de Subgéneros no encontrado o vacío. Se iniciará con una lista vacía.")
            return {"especificos": []}  # Retorna un diccionario vacío en caso de error

    def _guardar_datos(self):
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump(self.datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def agregar_especifico(self, especifico):
        if any(a["especifico_id"] == especifico["especifico_id"] for a in self.especificos):
            print(f"El especifico con ID {especifico['especifico_id']} ya existe.")
            return
        self.especificos.append(especifico)
        self._guardar_datos()
        print(f"especifico '{especifico['nombre']} {especifico['tipo']}' agregado correctamente.")

    def mostrar_especificos(self):
        """Muestra todos los géneros literarios almacenados."""
        if self.especificos:
            print("\n=== Lista de Subgéneros Literarios ===\n")
            for especifico in self.especificos:
                print(f"> ID: {especifico['especifico_id']} | Subgénero Literario: {especifico['nombre_especifico']} | Tipo: {especifico['tipo']}")
        else:
            print("No hay géneros registrados.")

    def obtener_especifico_por_id(self, especifico_id):
        for especifico in self.especificos:
            if especifico['especifico_id'] == especifico_id:
                return especifico
        return None

    def obtener_especificos(self):
        """Devuelve la lista de autores."""
        return self.especificos