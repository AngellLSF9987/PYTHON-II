# crud_especifico.py
import json
import shutil # Para respaldar datos antes de guardar
class CRUDEspecifico:
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
            return {"especificos": []}  # Inicializa con lista vacía si no existe
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Archivo vacío o malformado.")
            return {"especificos": []}

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
        """Obtiene el máximo ID existente en los especificos."""
        if not self.datos["especificos"]:
            return 0  # Si no hay especificos, inicia en 0
        return max(int(especifico["especifico_id"]) for especifico in self.datos["especificos"])

    def agregar_especifico(self, nuevo_especifico):
        """Agrega un nuevo Subgénero Literario con ID autoincremental."""
        nuevo_especifico["especifico_id"] = str(self.especifico_id_actual)
        self.datos["especificos"].append(nuevo_especifico)
        self.especifico_id_actual += 1
        self.guardar_datos()
        print(f"✅Subgénero Literario agregado con éxito: {nuevo_especifico['nombre_especifico']}")
        return True

    def actualizar_especifico(self, especifico_id, datos_actualizados):
        """Actualiza los datos de un Subgénero Literario existente."""
        for especifico in self.datos["especificos"]:
            if especifico["especifico_id"] == especifico_id:
                especifico.update(datos_actualizados)
                self.guardar_datos()
                print(f"✅ Subgénero Literario con ID {especifico_id} actualizado.")
                return True
        print(f"No se encontró ningún Subgénero Literario con ID {especifico_id}.")
        return False

    def eliminar_especifico(self, especifico_id):
        """Elimina un Subgénero Literario por su ID y reestructura los IDs restantes."""
        for especifico in self.datos["especificos"]:
            if especifico["especifico_id"] == especifico_id:
                self.datos["especificos"].remove(especifico)
                self.reestructurar_ids_especificos()  # Llamada para reestructurar IDs
                print(f"✅ Subgénero Literarios con ID {especifico_id} eliminado.")
                return True
        print(f"No se encontró ningún Subgénero Literario con ID {especifico_id}.")
        return False

    def reestructurar_ids_especificos(self):
        """Reestructura los IDs de los Subgéneros Literarios para que sean consecutivos 
        después de una eliminación."""
        for index, especifico in enumerate(self.datos["especificos"]):
            especifico["especifico_id"] = str(index + 1)  # Asigna IDs consecutivos como cadenas
        self.especifico_id_actual = len(self.datos["especificos"]) + 1  # Ajusta el ID siguiente
        self.guardar_datos()
    
    def mostrar_especificos(self):
        """Muestra todos los Subgéneros Literarios registrados."""
        if not self.datos["especificos"]:
            print("No hay Género Literario registrados.")
            return []
        print("\n=== Lista de los Géneros Literarios ===\n")
        for especifico in self.datos["especificos"]:
            print(f"> ID: {especifico['especifico_id']} | Subgénero Literario: {especifico['nombre_especifico']} | Tipo: {especifico['tipo']}")
        return self.datos["especificos"]