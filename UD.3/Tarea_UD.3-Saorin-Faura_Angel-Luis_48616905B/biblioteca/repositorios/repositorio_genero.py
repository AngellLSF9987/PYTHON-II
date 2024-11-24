import json
class RepositorioGenero:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.datos = self._cargar_generos()
        self.generos = self.datos.get("generos", [])

    def _cargar_generos(self):
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)
                print("Géneros cargados correctamente.")
                return data  # Retorna directamente el contenido del archivo
        except (FileNotFoundError, json.JSONDecodeError):
            print("Archivo de géneros no encontrado o vacío. Se iniciará con una lista vacía.")
            return {"generos": []}  # Retorna un diccionario vacío en caso de error

    def _guardar_datos(self):
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump(self.datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def agregar_genero(self, genero):
        # Verifica si el autor tiene el campo genero_id
        if "genero_id" not in genero:
            genero["genero_id"] = len(self.generos) + 1   # Asigna un ID único, autoincremental
        
        if any(g["genero_id"] == genero["genero_id"] for g in self.generos):
            print(f"El Género Literario con ID {genero['genero_id']} ya existe.")
            return
        self.generos.append(genero)
        self._guardar_datos()
        print(f"Género Literario: '{genero['nombre_genero']}")

    def buscar_genero_por_nombre(self, nombre_buscar):
        """Busca un género por nombre."""
        for genero in self.generos:
            nombre_genero = genero.get('nombre_genero', '')
            if isinstance(nombre_genero, str) and nombre_genero.lower() == nombre_buscar.lower():
                return genero
        return None

    def mostrar_generos(self):
        """Muestra todos los géneros literarios almacenados."""
        if self.generos:
            print("\n=== Lista de Géneros Literarios ===\n")
            for genero in self.generos:
                print(f"> ID: {genero['genero_id']} | Nombre: {genero['nombre_genero']}")
        else:
            print("No hay géneros registrados.")

    def obtener_genero_por_id(self, genero_id):
        for genero in self.generos:
            if genero['genero_id'] == (genero_id):
                return genero
        return None
    
    def obtener_generos(self):
        """Devuelve la lista de géneros."""
        return self.generos
