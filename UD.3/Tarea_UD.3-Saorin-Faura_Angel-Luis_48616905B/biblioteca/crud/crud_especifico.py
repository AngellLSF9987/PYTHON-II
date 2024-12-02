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
        nuevo_especifico["especifico_id"] = str(self.genero_id_actual)
        self.datos["especificos"].append(nuevo_especifico)
        self.genero_id_actual += 1  # Incrementa el ID para el siguiente registro
        self.guardar_datos()
        print(f"✅ Subgénero Literario agregado con éxito: {nuevo_especifico['nombre_especifico']}")
        return True

    def actualizar_especifico(self):
        """Permite actualizar un subgénero literario existente por nombre_especifico y tipo."""
        print("\n- Actualizar Subgénero Literario -\n")

        # Solicitar atributos del subgénero
        nombre_especifico = input("Introduce el nombre exacto del Subgénero Literario a actualizar:\n").strip()
        tipo = input("Introduce el Tipo exacto del Subgénero Literario:\n").strip()

        # Buscar subgéneros que coincidan con los atributos
        especificos_encontrados = [e for e in self.datos["especificos"] 
                                if e["nombre_especifico"] == nombre_especifico and e["tipo"] == tipo]

        if not especificos_encontrados:
            print(f"❌ No se encontró ningún Subgénero Literario con nombre '{nombre_especifico}' y tipo '{tipo}'.")
            return False

        if len(especificos_encontrados) > 1:
            print("⚠️ Se encontraron varios registros con estos atributos:")
            for e in especificos_encontrados:
                print(f"> ID: {e['especifico_id']} | Subgénero Literario: {e['nombre_especifico']} | Tipo: {e['tipo']}")
            especifico_id = input("Introduce el ID del registro que deseas actualizar:\n").strip()
            especifico_actual = next((e for e in especificos_encontrados if e["especifico_id"] == especifico_id), None)
            if not especifico_actual:
                print("❌ ID no válido.")
                return False
        else:
            especifico_actual = especificos_encontrados[0]

        # Mostrar datos actuales y solicitar nuevas entradas
        nuevo_nombre_especifico = input(f"Introduce el nuevo nombre del subgénero [{especifico_actual['nombre_especifico']}] o presiona ENTER para no modificar:\n").strip() or especifico_actual['nombre_especifico']
        nuevo_tipo = input(f"Introduce el nuevo tipo del subgénero [{especifico_actual['tipo']}] o presiona ENTER para no modificar:\n").strip() or especifico_actual['tipo']

        # Actualizar los datos
        especifico_actual["nombre_especifico"] = nuevo_nombre_especifico
        especifico_actual["tipo"] = nuevo_tipo

        # Guardar cambios
        self.guardar_datos()
        print(f"✅ Subgénero Literario actualizado correctamente.")
        return True

    def eliminar_especifico(self):
        """Elimina un Subgénero Literario por su nombre y tipo y reestructura los IDs restantes."""
        # Solicitar al usuario el nombre y tipo del subgénero a eliminar
        nombre_especifico = input("Introduce el nombre del subgénero a eliminar: ")
        tipo = input("Introduce el tipo del subgénero a eliminar: ")
        
        # Buscar el subgénero por nombre y tipo
        especifico = next(
            (e for e in self.datos["especificos"] if e["nombre_especifico"] == nombre_especifico and e["tipo"] == tipo), 
            None
        )
        
        if especifico:
            self.datos["especificos"].remove(especifico)  # Elimina el subgénero
            self.reestructurar_ids_especificos()  # Reestructura los IDs si se eliminó algo
            print(f"✅ Subgénero Literario '{nombre_especifico}' eliminado correctamente.")
            return True
        else:
            print(f"❌ No se encontró ningún Subgénero Literario con nombre '{nombre_especifico}' y tipo '{tipo}'.")
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