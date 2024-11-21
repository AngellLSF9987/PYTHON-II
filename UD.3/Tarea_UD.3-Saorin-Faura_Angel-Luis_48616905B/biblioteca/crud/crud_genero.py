import json
import shutil  # Para respaldar datos antes de guardar

class CRUDGenero:

    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.datos = self.cargar_datos()
        self.genero_id_actual = self.obtener_max_id() + 1  # Inicializar ID autoincremental

    def cargar_datos(self):
        """Carga los datos desde el archivo JSON."""
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            print("Archivo JSON no encontrado. Se creará un nuevo archivo.")
            return {"genero": []}  # Inicializa con lista vacía si no existe
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Archivo vacío o malformado.")
            return {"genero": []}

    def guardar_datos(self):
        """Guarda los datos en el archivo JSON y realiza un respaldo previo."""
        try:
            # Crear respaldo del archivo
            shutil.copy(self.ruta_json, self.ruta_json + ".bak")
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump(self.datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def obtener_max_id(self):
        """Obtiene el máximo ID existente en los Géneros Literarios."""
        if not self.datos["generos"]:
            return 0  # Si no hay géneros, inicia en 0
        return max(int(genero["genero_id"]) for genero in self.datos["generos"])

    def agregar_genero(self, nuevo_genero):
        """
        Agrega un nuevo género con ID autoincremental.
        """
        nuevo_genero["genero_id"] = str(self.genero_id_actual)
        self.datos["generos"].append(nuevo_genero)
        self.genero_id_actual += 1
        self.guardar_datos()
        print(f"✅ Género Literario agregado con éxito: {nuevo_genero}")
        return True

    def actualizar_genero(self, genero_id, datos_actualizados):
        for genero in self.datos["generos"]:
            if genero["genero_id"] == genero_id:
                genero.update(datos_actualizados)
                self.guardar_datos()
                return True
        return False
    
    def eliminar_genero(self, genero_id):
        """
        Elimina un Género Literario por su ID y reestructura los IDs restantes.
        """
        for genero in self.datos["generos"]:
            if genero["genero_id"] == genero_id:
                self.datos["generos"].remove(genero)
                self.reestructurar_ids_genero()  # Llamada para reestructurar IDs
                return True
        return False
    
    def reestructurar_ids_genero(self):
        """
        Reestructura los IDs de los Géneros Literarios para que sean consecutivos después de una eliminación.
        """
        for index, genero in enumerate(self.datos["generos"]):
            genero["genero_id"] = str(index + 1)  # Asigna IDs consecutivos como cadenas
        self.genero_id_actual = len(self.datos["generos"]) + 1  # Ajusta el ID siguiente
        self.guardar_datos()


    def buscar_genero_por_nombre_genero(self, nombre_genero):
        """
        Busca un Género Literario por nombre completo o pseudónimo.
        """
        for genero in self.datos["generos"]:
            nombre_genero = f"{genero['nombre_genero']}".strip()
            if (nombre_genero.lower() == nombre_genero.lower() or
                    genero.get("nombre_genero", "").lower() == nombre_genero.lower()):
                return genero
        return None

    def mostrar_generos(self):
        """
        Muestra todos los Géneros Literarios registrados.
        """
        if not self.datos["generos"]:
            print("\nNo hay Géneros Literarios registrados.")
            return
        print("\n=== Lista de Géneros Literarios ===")
        for genero in self.datos["generos"]:
            print(f"ID: {genero['genero_id']}", 
                  f"Nombre: {genero['nombre_genero']}")
