import json

class RepositorioEspecifico:
    def __init__(self, ruta_json, repositorio_genero):
        """
        Constructor del repositorio de Subgéneros Literarios específicos.
        :param repositorio_genero: Instancia de RepositorioGenero.
        :param ruta_json: Ruta al archivo JSON donde se almacenan los datos.
        """
        self.repositorio_genero = repositorio_genero
        self.ruta_json = ruta_json
        self.datos = self.cargar_datos()

    def cargar_datos(self):
        """Carga los datos desde el archivo JSON."""
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            # Si no existe el archivo, retorna un diccionario vacío
            return {"especificos": [], "generos": []}

    def guardar_datos(self):
        """Guarda los datos modificados en el archivo JSON."""
        with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
            json.dump({"especificos": self.datos["especificos"], "generos": self.datos["generos"]}, archivo, ensure_ascii=False, indent=4)

    def obtener_especificos(self):
        """Obtiene todos los subgéneros específicos."""
        return self.datos.get("especificos", [])

    def agregar_especifico(self, genero_nombre, nombre_especifico, tipo):
        """
        Agrega un nuevo subgénero a la lista de subgéneros.
        Si el género no existe, se crea uno nuevo.
        """
        # Verificar si el género ya existe
        genero_id = None
        for genero in self.datos["generos"]:
            if genero["nombre_genero"].strip().lower() == genero_nombre.strip().lower():
                genero_id = genero["genero_id"]
                break

        # Si el género no existe, crear uno nuevo
        if not genero_id:
            print(f"No se encontró el género '{genero_nombre}'")
            respuesta = input(f"No se encontró el género '{genero_nombre}'. ¿Deseas crearlo? (s/n): ").strip().lower()
            if respuesta == 's':
                genero_id = str(len(self.datos["generos"]) + 1)  # Asigna un ID nuevo al género
                nueva_entrada_genero = {
                    "genero_id": genero_id,
                    "nombre_genero": genero_nombre
                }
                self.datos["generos"].append(nueva_entrada_genero)
                print(f"Género '{genero_nombre}' agregado con éxito.")

        # Crear el específico (subgénero) solo si el genero_id es válido
        if genero_id:
            # Asignar un nuevo ID para el específico
            especifico_id = str(len(self.datos["especificos"]) + 1)  # ID autoincremental para el específico
            nuevo_especifico = {
                "especifico_id": especifico_id,
                "genero_id": genero_id,  # Aquí usamos el ID del género, no su nombre
                "nombre_especifico": nombre_especifico,
                "tipo": tipo if tipo else "Sin especificar"  # Usamos "Sin especificar" si no se proporciona un tipo
            }
            self.datos["especificos"].append(nuevo_especifico)
            self.guardar_datos()
            print(f"✅ Específico (subgénero) '{nombre_especifico}' agregado con éxito.")

    def mostrar_especificos(self):
        """Muestra todos los subgéneros y su información asociada."""
        for especifico in self.datos["especificos"]:
            genero = self.repositorio_genero.obtener_genero_por_id(especifico["genero_id"])
            nombre_genero = genero["nombre_genero"] if genero else "Desconocido"
            print(f"ID: {especifico['especifico_id']} | Subgénero: {especifico['nombre_especifico']} | Género: {nombre_genero}")

    def obtener_especifico_por_id(self, especifico_id):
        """Busca un subgénero específico por su ID."""
        for especifico in self.datos["especificos"]:
            if especifico["especifico_id"] == especifico_id:
                return especifico
        return None

    def obtener_especificos_por_genero(self, genero_id):
        """Obtiene todos los subgéneros específicos asociados a un género dado."""
        return [
            especifico for especifico in self.datos["especificos"]
            if especifico["genero_id"] == genero_id
        ]

    def eliminar_especifico(self):
        """Elimina un subgénero literario específico."""
        especifico_id = input("Introduce el ID del subgénero a eliminar: ").strip()
        especifico = self.obtener_especifico_por_id(especifico_id)

        if not especifico:
            print(f"⚠️ No existe un subgénero con ID {especifico_id}.")
            return

        # Confirmación antes de eliminar
        confirmacion = input(
            f"¿Estás seguro de que deseas eliminar el subgénero '{especifico['nombre_especifico']}'? (s/n): "
        ).strip().lower()

        if confirmacion == 's':
            self.datos["especificos"].remove(especifico)
            self.guardar_datos()
            print(f"✅ Subgénero '{especifico['nombre_especifico']}' eliminado con éxito.")
        else:
            print("❌ Eliminación cancelada.")
