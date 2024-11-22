import json
class RepositorioGenero:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.datos = self._cargar_generos()
        self.generos = self.datos.get("generos", [])

    def _cargar_generos(self):
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {"generos": []}

    def _guardar_datos(self):
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump(self.datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def obtener_generos(self):
        return self.generos

    def buscar_genero_por_nombre(generos, nombre_buscar):
        for genero in generos:
            nombre = genero.get('nombre_genero', '')
            if isinstance(nombre, str) and nombre.lower() == nombre_buscar.lower():
                return genero
        return None


    def agregar_genero(self, genero):
        if self.buscar_genero_por_nombre(genero["nombre_genero"]):
            print(f"El género '{genero['nombre_genero']}' ya existe.")
            return
        self.generos.append(genero)
        self.datos["generos"] = self.generos
        self._guardar_datos()
        print(f"Género '{genero['nombre_genero']}' agregado correctamente.")

    def mostrar_generos(self):
        """
        Muestra todos los géneros literarios almacenados.
        """
        if self.generos:
            print("\n=== Lista de Géneros Literarios ===")
            for genero in self.generos:
                print(f"ID: {genero['genero_id']} | Nombre: {genero['nombre_genero']}")
        else:
            print("No hay géneros registrados.")


    def eliminar_genero(self, genero_id):
        genero = self.obtener_genero_por_id(genero_id)
        if genero:
            self.generos.remove(genero)
            self.datos["generos"] = self.generos
            self._guardar_datos()
            print(f"Género eliminado: {genero}")
        else:
            print(f"No se encontró el género con ID {genero_id}")

    def obtener_genero_por_id(self, genero_id):
        return next((g for g in self.generos if g["genero_id"] == genero_id), None)
