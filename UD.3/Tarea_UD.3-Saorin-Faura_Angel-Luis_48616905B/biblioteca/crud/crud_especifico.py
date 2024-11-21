import json
import shutil  # Para realizar respaldos de los datos

class CRUDEspecifico:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.datos = self.cargar_datos()
        self.especifico_id_actual = self.obtener_max_id() + 1  # Inicializa el ID autoincremental

    def cargar_datos(self):
        """Carga los datos desde el archivo JSON."""
        try:
            with open(self.ruta_json, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            print("Archivo JSON no encontrado. Creando uno nuevo.")
            return {"especificos": []}
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Archivo vacío o malformado.")
            return {"especificos": []}

    def guardar_datos(self):
        """Guarda los datos en el archivo JSON con un respaldo previo."""
        try:
            shutil.copy(self.ruta_json, self.ruta_json + ".bak")  # Respaldo
            with open(self.ruta_json, "w", encoding="utf-8") as archivo:
                json.dump(self.datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def obtener_max_id(self):
        """Obtiene el máximo ID existente."""
        if not self.datos["especificos"]:
            return 0
        return max(int(especifico["especifico_id"]) for especifico in self.datos["especificos"])

    def crear_especifico(self, biblioteca):
        """Crea un nuevo subgénero literario específico."""
        genero_id = input("Introduce el ID del género asociado: ").strip()
        genero = biblioteca.repositorio_genero.obtener_genero_por_id(genero_id)

        if not genero:
            print(f"No existe un género con ID {genero_id}.")
            return

        nuevo_especifico = {
            "especifico_id": str(self.especifico_id_actual),
            "genero_id": genero_id,
            "nombre_genero": genero["nombre_genero"],
            "nombre_especifico": input("Introduce el nombre del subgénero: ").strip(),
            "tipo": input("Introduce el tipo de subgénero: ").strip(),
        }

        self.datos["especificos"].append(nuevo_especifico)
        self.especifico_id_actual += 1
        self.guardar_datos()
        print(f"✅ Subgénero '{nuevo_especifico['nombre_especifico']}' creado con éxito.")

    def mostrar_especificos_crud(self, biblioteca):
        """Muestra todos los subgéneros literarios específicos."""
        especificos = self.datos["especificos"]
        if not especificos:
            print("⚠️ No hay subgéneros específicos registrados.")
            return

        print("\n=== Lista de Subgéneros ===")
        for especifico in especificos:
            print(
                f"ID: {especifico['especifico_id']} | Subgénero: {especifico['nombre_especifico']} | "
                f"Tipo: {especifico['tipo']} | Género Asociado: {especifico['nombre_genero']}"
            )

    def actualizar_especifico(self, biblioteca):
        """Actualiza un subgénero literario específico."""
        especifico_id = input("Introduce el ID del subgénero a modificar: ").strip()
        especifico = next(
            (e for e in self.datos["especificos"] if e["especifico_id"] == especifico_id), None
        )

        if not especifico:
            print(f"⚠️ No existe un subgénero con ID {especifico_id}.")
            return

        print("\n=== Modificando Subgénero ===")
        especifico["nombre_especifico"] = input(
            f"Nuevo nombre del subgénero ({especifico['nombre_especifico']}): "
        ).strip() or especifico["nombre_especifico"]
        especifico["tipo"] = input(
            f"Nuevo tipo ({especifico['tipo']}): "
        ).strip() or especifico["tipo"]
        self.guardar_datos()
        print(f"✅ Subgénero '{especifico['nombre_especifico']}' actualizado con éxito.")

    def eliminar_especifico(self, biblioteca):
        """Elimina un subgénero literario específico."""
        especifico_id = input("Introduce el ID del subgénero a eliminar: ").strip()
        especifico = next(
            (e for e in self.datos["especificos"] if e["especifico_id"] == especifico_id), None
        )

        if not especifico:
            print(f"⚠️ No existe un subgénero con ID {especifico_id}.")
            return

        self.datos["especificos"].remove(especifico)
        self.guardar_datos()
        print(f"✅ Subgénero '{especifico['nombre_especifico']}' eliminado con éxito.")
