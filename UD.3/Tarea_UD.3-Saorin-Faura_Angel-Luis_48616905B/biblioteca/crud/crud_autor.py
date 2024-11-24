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
            print("Datos guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def obtener_max_id(self):
        """Obtiene el máximo ID existente en los autores."""
        if not self.datos["autores"]:
            return 0  # Si no hay autores, inicia en 0
        return max(int(autor["autor_id"]) for autor in self.datos["autores"])

    def agregar_autor(self, nuevo_autor):
        """
        Agrega un nuevo autor con ID autoincremental.
        """
        nuevo_autor["autor_id"] = str(self.autor_id_actual)
        if any(a["autor_id"] == nuevo_autor["autor_id"] for a in self.datos["autores"]):
            print("⚠️ El ID del autor ya existe.")
            return False
        self.datos["autores"].append(nuevo_autor)
        self.autor_id_actual += 1
        self.guardar_datos()
        print(f"✅ Autor agregado con éxito: {nuevo_autor['nombre']} {nuevo_autor['apellido1']}")
        return True

    def actualizar_autor(self, autor_id, datos_actualizados):
        """Actualiza los datos de un autor existente."""
        for autor in self.datos["autores"]:
            if autor["autor_id"] == autor_id:
                autor.update(datos_actualizados)
                self.guardar_datos()
                print(f"✅ Autor con ID {autor_id} actualizado.")
                return True
        print(f"No se encontró un autor con ID {autor_id}.")
        return False

    def eliminar_autor(self, autor_id):
        """
        Elimina un autor por su ID y reestructura los IDs restantes.
        """
        for autor in self.datos["autores"]:
            if autor["autor_id"] == autor_id:
                self.datos["autores"].remove(autor)
                self.reestructurar_ids_autores()  # Llamada para reestructurar IDs
                print(f"✅ Autor con ID {autor_id} eliminado.")
                return True
        print(f"No se encontró un autor con ID {autor_id}.")
        return False
    
    def reestructurar_ids_autores(self):
        """
        Reestructura los IDs de los autores para que sean consecutivos después de una eliminación.
        """
        for index, autor in enumerate(self.datos["autores"]):
            autor["autor_id"] = str(index + 1)  # Asigna IDs consecutivos como cadenas
        self.autor_id_actual = len(self.datos["autores"]) + 1  # Ajusta el ID siguiente
        self.guardar_datos()

    def buscar_autor_por_nombre_o_pseudonimo(self, nombre_o_pseudonimo):
        """
        Busca un autor por nombre completo o pseudónimo.
        """
        for autor in self.datos["autores"]:
            nombre_completo = f"{autor['nombre']} {autor['apellido1']} {autor.get('apellido2', '')}".strip()
            if (nombre_completo.lower() == nombre_o_pseudonimo.lower() or
                    autor.get("pseudonimo", "").lower() == nombre_o_pseudonimo.lower()):
                return autor
        print(f"No se encontró un autor con nombre o pseudónimo: {nombre_o_pseudonimo}")
        return None

    def mostrar_autores(self):
        """Muestra todos los autores registrados."""
        if not self.datos["autores"]:
            print("No hay autores registrados.")
            return []
        print("=== Todos los Autores ===")
        for autor in self.datos["autores"]:
            print(f"ID: {autor['autor_id']} | {autor['nombre']} {autor['apellido1']} {autor.get('apellido2', '')}")
        return self.datos["autores"]
