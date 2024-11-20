# biblioteca/repositorios/repositorio_especifico.py

class RepositorioEspecifico:
    def __init__(self, repositorio_genero):
        """
        Constructor del repositorio de subgéneros específicos.
        :param repositorio_genero: Instancia de RepositorioGenero.
        """
        self.repositorio_genero = repositorio_genero
        self.especificos = []  # Lista para almacenar subgéneros específicos como diccionarios

    def agregar_especificos(self, datos_especificos):
        """Carga una lista completa de subgéneros específicos en el repositorio."""
        try:
            for especifico in datos_especificos:
                self.agregar_especifico(especifico)
            print("Carga de datos de Subgéneros Literarios Específicos correcta.")
        except Exception as e:
            print(f"Error al cargar subgéneros específicos: {e}")

    def agregar_especifico(self, especifico):
        """Agrega un único subgénero específico al repositorio."""
        if isinstance(especifico, dict) and "especifico_id" in especifico:
            # Verificar que el género asociado al subgénero existe
            genero = self.repositorio_genero.obtener_genero_por_id(especifico["genero_id"])
            if genero is None:
                print(f"Aviso: No se encontró un género con ID {especifico['genero_id']}. Asignando 'Género desconocido'.")
                nombre_genero = "Género desconocido"
            else:
                nombre_genero = genero["nombre_genero"]
            
            if not self.obtener_especifico_por_id(especifico["especifico_id"]):
                self.especificos.append({
                    "especifico_id": especifico["especifico_id"],
                    "genero_id": especifico["genero_id"],
                    "nombre_genero": nombre_genero,
                    "nombre_especifico": especifico.get("nombre_especifico", "Desconocido"),
                    "tipo": especifico.get("tipo", "Sin especificar"),
                })
                #print(f"Subgénero {especifico['nombre_especifico']} agregado correctamente.")
            else:
                print(f"El subgénero con ID {especifico['especifico_id']} ya existe.")
        else:
            print(f"Formato inválido para subgénero específico: {especifico}")


    def mostrar_especificos(self):
        """Devuelve la lista de subgéneros específicos en el repositorio."""
        if not self.especificos:
            return "No hay subgéneros específicos cargados en el repositorio."

        return "\n".join(
            f"ID: {especifico['especifico_id']}\nNombre del Subgénero: {especifico['nombre_especifico']}\n"
            f"Tipo: {especifico['tipo']}\n"
            f"Género Asociado: {especifico['nombre_genero']}\n"
            for especifico in self.especificos
        )

    def obtener_especifico_por_id(self, especifico_id):
        """Busca un subgénero específico por su ID."""
        for especifico in self.especificos:
            if especifico["especifico_id"] == especifico_id:
                return especifico
        return None

    def obtener_especificos_por_genero(self, genero_id):
        """Obtiene todos los subgéneros específicos asociados a un género dado."""
        subgeneros = [especifico for especifico in self.especificos if especifico["genero_id"] == genero_id]
        if not subgeneros:
            print(f"No se encontraron subgéneros específicos para el género con ID {genero_id}.")
        return subgeneros

    def eliminar_especifico_por_id(self, especifico_id):
        """Elimina un subgénero específico del repositorio por su ID."""
        especifico = self.obtener_especifico_por_id(especifico_id)
        if especifico:
            self.especificos.remove(especifico)
            print(f"Subgénero con ID {especifico_id} eliminado correctamente.")
        else:
            print(f"No se encontró un subgénero con ID {especifico_id} para eliminar.")