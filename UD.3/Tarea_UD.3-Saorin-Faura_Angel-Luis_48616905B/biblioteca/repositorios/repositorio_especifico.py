import json
class RepositorioEspecifico:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.datos = self._cargar_especificos()

    def _cargar_especificos(self):
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {"especificos": []}

    def _guardar_datos(self):
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump(self.datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            raise IOError(f"Error al guardar los datos: {e}")
        
    def mostrar_especificos(self):
        """
        Muestra todos los subgéneros literarios con sus detalles.
        """
        if self.especificos:
            print("\n=== Lista de Subgéneros Literarios ===")
            for especifico in self.especificos:
                print(
                    f"ID: {especifico['especifico_id']} | Subgénero: {especifico['nombre_especifico']} | "
                    f"Tipo: {especifico['tipo']} | Género Asociado: {especifico.get('nombre_genero', 'Desconocido')}"
                )
        else:
            print("No hay subgéneros registrados.")


    def agregar_especifico(self, genero_nombre, nombre_especifico, tipo=None):
        if not nombre_especifico or not genero_nombre:
            raise ValueError("El nombre del género y del subgénero son obligatorios.")

        genero_id, nombre_genero = self._obtener_genero_por_nombre(genero_nombre)
        if not genero_id:
            raise ValueError(f"No se encontró el género '{genero_nombre}'.")

        especificos = self.datos.get("especificos", [])
        if any(e["nombre_especifico"] == nombre_especifico for e in especificos):
            raise ValueError(f"El subgénero '{nombre_especifico}' ya existe.")

        especifico_id = len(especificos) + 1
        nuevo_especifico = {
            "especifico_id": especifico_id,
            "nombre_especifico": nombre_especifico,
            "tipo": tipo or "Sin especificar",
            "genero_id": genero_id,
            "nombre_genero": nombre_genero,
        }
        especificos.append(nuevo_especifico)
        self._guardar_datos()

    def actualizar_especifico(self, especifico_id, nuevo_nombre=None, nuevo_tipo=None):
        especificos = self.datos.get("especificos", [])
        for especifico in especificos:
            if especifico["especifico_id"] == especifico_id:
                especifico["nombre_especifico"] = nuevo_nombre or especifico["nombre_especifico"]
                especifico["tipo"] = nuevo_tipo or especifico["tipo"]
                self._guardar_datos()
                return
        raise ValueError(f"No se encontró el Subgénero con ID {especifico_id}.")

    def eliminar_especifico(self, especifico_id):
        especificos = self.datos.get("especificos", [])
        nuevos_especificos = [e for e in especificos if e["especifico_id"] != especifico_id]
        if len(nuevos_especificos) == len(especificos):
            raise ValueError(f"No se encontró el Subgénero con ID {especifico_id}.")
        self.datos["especificos"] = nuevos_especificos
        self._guardar_datos()

    def obtener_especificos_por_genero(self, genero_id):
        return [e for e in self.datos["especificos"] if e["genero_id"] == genero_id]

    def _obtener_genero_por_nombre(self, genero_nombre):
        # Aquí debes integrar con el RepositorioGenero
        raise NotImplementedError("Esta función debe ser implementada o importada.")
