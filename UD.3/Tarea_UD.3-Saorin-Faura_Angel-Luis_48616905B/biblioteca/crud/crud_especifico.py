import json
import shutil  # Para realizar respaldos de los datos

class CRUDEspecifico:
    def __init__(self, ruta_json, repositorio_genero):
        """
        Inicializa la clase CRUDEspecifico con la ruta del archivo JSON y un repositorio de géneros.
        :param ruta_json: Ruta del archivo JSON donde se almacenan los subgéneros.
        :param repositorio_genero: Instancia del repositorio de géneros (se usa para obtener géneros asociados).
        """
        self.ruta_json = ruta_json
        self.repositorio_genero = repositorio_genero  # Agregamos el repositorio de géneros
        self.datos = self.cargar_datos()
        self.especifico_id_actual = self.obtener_max_id() + 1  # Inicializa el ID autoincremental

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
            shutil.copy(self.ruta_json, self.ruta_json + ".bak")  # Respaldo
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump(self.datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def obtener_max_id(self):
        """Obtiene el máximo ID existente de los subgéneros específicos."""
        if not self.datos["especificos"]:
            return 0
        return max(int(especifico["especifico_id"]) for especifico in self.datos["especificos"])

    def agregar_especifico(self, especifico):
        """Agrega un único subgénero específico al repositorio."""
        if isinstance(especifico, dict) and "especifico_id" in especifico:
            genero_id = str(especifico["genero_id"])  # Convertimos a str para coherencia
            genero = self.repositorio_genero.obtener_genero_por_id(genero_id)
            
            if genero is None:
                print(f"Aviso: No se encontró un género con ID {genero_id}. Asignando 'Género desconocido'.")
                nombre_genero = "Género desconocido"
            else:
                nombre_genero = genero["nombre_genero"]

            if not self.obtener_especifico_por_id(especifico["especifico_id"]):
                self.datos["especificos"].append({
                    "especifico_id": especifico["especifico_id"],
                    "genero_id": genero_id,
                    "nombre_genero": nombre_genero,
                    "nombre_especifico": especifico.get("nombre_especifico", "Desconocido"),
                    "tipo": especifico.get("tipo", "Sin especificar"),
                })
                self.guardar_datos()  # Guardamos los datos después de la adición
                print(f"✅ Subgénero '{especifico['nombre_especifico']}' agregado con éxito.")
            else:
                print(f"⚠️ El subgénero con ID {especifico['especifico_id']} ya existe.")
        else:
            print("⚠️ Formato inválido para subgénero específico. Se requiere un diccionario con 'especifico_id'.")

    def mostrar_especificos_crud(self, biblioteca):
        """Muestra todos los subgéneros literarios específicos."""
        especificos = self.datos["especificos"]
        generos = biblioteca.repositorio_genero.obtener_generos()
        
        if not especificos:
            print("⚠️ No hay subgéneros específicos registrados.")
            return

        print("\n=== Lista de Subgéneros ===")
        for especifico in especificos:
            # Buscar el género asociado al genero_id
            genero_asociado = next((genero for genero in generos if genero['genero_id'] == especifico['genero_id']), None)
            nombre_genero = genero_asociado['nombre_genero'] if genero_asociado else 'Desconocido'
            
            print(
                f"ID: {especifico['especifico_id']} | Subgénero: {especifico['nombre_especifico']} | "
                f"Tipo: {especifico['tipo']} | Género Asociado: {nombre_genero}"
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
        
    def obtener_especifico_por_id(self, especifico_id):
        """Busca un subgénero específico por su ID."""
        for especifico in self.datos["especificos"]:
            if especifico["especifico_id"] == especifico_id:
                return especifico
        return None
