import json
import shutil  # Para respaldar datos antes de guardar

class CRUDAutor:

    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.datos = self.cargar_datos()
        self.autor_id_actual = self.obtener_max_id() + 1  # Inicializar ID autoincremental

    def cargar_datos(self):
        """Carga los datos desde el archivo JSON."""
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            print("Archivo JSON no encontrado. Se creará un nuevo archivo.")
            return {"autores": []}  # Inicializa con lista vacía si no existe
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Archivo vacío o malformado.")
            return {"autores": []}

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

    def agregar_genero(self, nombre_genero):
        """
        Agrega un nuevo Género Literario con ID autoincremental.
        Parámetros:
            - nombre: Nombre completo del Género Literario (obligatorio).
        """
        if not nombre_genero.strip():
            print("⚠️ El nombre del autor no puede estar vacío.")
            return False

        genero = {
            "genero_id": str(self.genero_id_actual),
            "nombre_genero": nombre_genero.strip(),
        }
        self.datos["generos"].append(genero)
        self.genero_id_actual += 1
        self.guardar_datos()
        print(f"✅ Género Literario agregado con éxito: {genero}")
        return True
    
    def actualizar_genero(self, genero_id, nuevos_datos):
        """
        Actualiza los datos de un autor buscando por su ID.
        Parámetros:
            - id_autor: ID del Género Literario a actualizar.
            - nuevos_datos: Diccionario con los nuevos valores.
        """
        for genero in self.datos["autores"]:
            if genero["genero_id"] == genero_id:
                genero.update({clave: valor.strip() for clave, valor in nuevos_datos.items() if valor is not None})
                self.guardar_datos()
                print(f"✅ Género Literario actualizado con éxito: {genero}")
                return True
        print(f"⚠️ No se encontró un autor con ID {genero_id}.")
        return False
    
    def eliminar_genero(self, genero_id):
        """
        Elimina un autor por su ID.
        Parámetros:
            - genero_id: ID del Género Literario a eliminar.
        """
        for genero in self.datos["generos"]:
            if genero["genero_id"] == genero_id:
                self.datos["generos"].remove(genero)
                self.guardar_datos()
                print(f"✅ Genero Literario eliminado con éxito: {genero}")
                return True
        print(f"⚠️ No se encontró un Genero Literario con ID {genero_id}.")
        return False

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
