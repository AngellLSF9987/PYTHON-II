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
            return {"generos": []}  # Inicializa con lista vacía si no existe
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Archivo vacío o malformado.")
            return {"generos": []}

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
        """Obtiene el máximo ID existente en los generos."""
        if not self.datos["generos"]:
            return 0  # Si no hay generos, inicia en 0
        return max(int(genero["genero_id"]) for genero in self.datos["generos"])

    def agregar_genero(self, nuevo_genero):
        """Agrega un nuevo genero con ID autoincremental."""
        nuevo_genero["genero_id"] = str(self.genero_id_actual)
        self.datos["generos"].append(nuevo_genero)
        self.genero_id_actual += 1
        self.guardar_datos()
        print(f"✅ Género Literario agregado con éxito: {nuevo_genero['nombre_genero']}")
        return True

    def actualizar_genero(self):
        """Permite actualizar un género literario existente por nombre_genero."""
        print("\n- Actualizar Subgénero Literario -\n")

        # Solicitar atributos del género
        nombre_genero = input("Introduce el nombre exacto del Género Literario a actualizar:\n").strip()

        # Buscar subgéneros que coincidan con los atributos
        generos_encontrados = [g for g in self.datos["generos"] 
                                if g["nombre_genero"] == nombre_genero]
        
        if not generos_encontrados:
            print(f"❌ No se encontró ningún Género Literario con nombre '{nombre_genero}'.")
            return False

        if len(generos_encontrados) > 1:
            print("⚠️ Se encontraron varios registros con estos atributos:")
            for g in generos_encontrados:
                print(f"> ID: {g['genero_id']} | Género Literario: {g['nombre_genero']} |")
            genero_id = input("Introduce el ID del registro que deseas actualizar:\n").strip()
            genero_actual = next((g for g in generos_encontrados if g["genero_id"] == genero_id), None)
            if not genero_actual:
                print("❌ ID no válido.")
                return False
        else:
            genero_actual = generos_encontrados[0]

        # Mostrar datos actuales y solicitar nuevas entradas
        nuevo_nombre_genero = input(f"Introduce el nuevo nombre del Género [{genero_actual['nombre_genero']}] o presiona ENTER para no modificar:\n").strip() or genero_actual['nombre_genero']

        # Actualizar los datos
        genero_actual["nombre_genero"] = nuevo_nombre_genero

        # Guardar cambios
        self.guardar_datos()
        print(f"✅ Género Literario actualizado correctamente.")
        return True

    def eliminar_genero(self):
        """Elimina un Género Literario por su nombre y reestructura los IDs restantes."""
        # Solicitar al usuario el nombre del Género a eliminar
        nombre_genero = input("Introduce el nombre del Género Literario a eliminar: ")

        # Buscar el subgénero por nombre y tipo
        genero = next(
            (g for g in self.datos["generos"] if g["nombre_genero"] == nombre_genero), 
            None
        )
        
        if genero:
            self.datos["generos"].remove(genero)  # Elimina el género
            self.reestructurar_ids_generos()  # Reestructura los IDs si se eliminó algo
            print(f"✅ Género Literario '{nombre_genero}' eliminado correctamente.")
            return True
        else:
            print(f"❌ No se encontró ningún Género Literario con nombre '{nombre_genero}'.")
            return False

    def reestructurar_ids_generos(self):
        """Reestructura los IDs de los Géneros Literarios para que sean consecutivos 
        después de una eliminación."""
        for index, genero in enumerate(self.datos["generos"]):
            genero["genero_id"] = str(index + 1)  # Asigna IDs consecutivos como cadenas
        self.genero_id_actual = len(self.datos["generos"]) + 1  # Ajusta el ID siguiente
        self.guardar_datos()

    def buscar_genero(self, nombre_genero):
        genero = self.repositorio.buscar_genero_por_nombre(nombre_genero)
        if genero:
            print(f"Género Literario encontrado: ID {genero['genero_id']} | Nombre: {genero['nombre_genero']}")
        else:
            print(f"No se encontró el Género Literario '{nombre_genero}'.")

    def mostrar_generos(self):
        """Muestra todos los Géneros Literarios registrados."""
        if not self.datos["generos"]:
            print("No hay Género Literario registrados.")
            return []
        print("\n=== Lista de los Géneros Literarios ===\n")
        for genero in self.datos["generos"]:
            print(f"> ID: {genero['genero_id']} | Género Literario: {genero['nombre_genero']}")
        return self.datos["generos"]