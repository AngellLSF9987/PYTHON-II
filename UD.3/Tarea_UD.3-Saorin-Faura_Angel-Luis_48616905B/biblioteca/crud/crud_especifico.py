import json
class CRUDEspecifico:
    def __init__(self, ruta_json, repositorio_genero):
        self.ruta_json = ruta_json
        self.repositorio_genero = repositorio_genero

    def agregar_especifico(self, genero_nombre, nombre_especifico, tipo=None):
        """Agrega un nuevo subgénero, asociado a un género."""
        # Verificar si el género existe
        genero = self.repositorio_genero.obtener_genero_por_nombre(genero_nombre)
        if genero is None:
            raise ValueError(f"No se encontró el género '{genero_nombre}'. Primero, debes crear el género.")

        # Verificar que el subgénero no exista
        if self.obtener_especifico_por_nombre(nombre_especifico):
            raise ValueError(f"El subgénero '{nombre_especifico}' ya existe.")

        # Crear un nuevo subgénero y agregarlo
        especifico_id = str(len(self.obtener_especificos()) + 1)  # ID autoincremental
        subgenero = {
            "especifico_id": especifico_id,
            "nombre_especifico": nombre_especifico,
            "tipo": tipo or "Sin especificar",
            "genero_id": genero["genero_id"],
            "nombre_genero": genero_nombre,
        }

        self.agregar_especifico_a_lista(subgenero)
        self.guardar_datos()

    def agregar_especifico_a_lista(self, subgenero):
        """Agrega un subgénero a la lista interna."""
        self.especificos.append(subgenero)

    def obtener_especificos(self):
        """Obtiene todos los subgéneros."""
        return self.especificos

    def obtener_especifico_por_nombre(self, nombre_especifico):
        """Obtiene un subgénero por su nombre."""
        for especifico in self.especificos:
            if especifico["nombre_especifico"] == nombre_especifico:
                return especifico
        return None

    def obtener_especifico_por_id(self, especifico_id):
        """Obtiene un subgénero por su ID."""
        for especifico in self.especificos:
            if especifico["especifico_id"] == especifico_id:
                return especifico
        return None

    def guardar_datos(self):
        """Guarda los datos de los subgéneros en el archivo JSON."""
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump({"subgeneros": self.especificos}, archivo, ensure_ascii=False, indent=4)
            print("Subgéneros guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar los subgéneros: {e}")
