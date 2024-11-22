# crud_especifico.py
class CRUDEspecifico:
    def __init__(self, repositorio_especifico):
        self.repositorio_especifico = repositorio_especifico

    def mostrar_especificos(self):
        """Muestra todos los datos persistentes en el fichero JSON. de Subgéneros, Tipo y Géneros Literarios Asociados."""
        especificos = self.repositorio_especifico.obtener_especificos()
        if especificos:
            print("\n=== Lista de Subgéneros Literarios===")
            for especifico in especificos:
                print(f"ID: {especifico['especifico_id']} | Subgénero Literario: {especifico['nombre_especifico']} | Tipo Específico: {especifico['tipo']} | Género Asociado: {especifico['nombre_genero']}")
        else:
            print("No hay subgéneros registrados.")

    def agregar_especifico(self, genero_nombre, nombre_especifico, tipo=None):
        """ Agrega un nuevo género con ID autoincremental definido en su respectiva clase Repositorio. """
        self.repositorio_especifico.agregar_especifico(genero_nombre, nombre_especifico, tipo)

    def actualizar_especifico(self, especifico_id, nuevo_nombre, nuevo_tipo):
        self.repositorio_especifico.actualizar_especifico(especifico_id, nuevo_nombre, nuevo_tipo)

    def eliminar_especifico(self, especifico_id):
        self.repositorio_especifico.eliminar_especifico(especifico_id)

    def obtener_especificos_por_genero(self, genero_id):
        return self.repositorio_especifico.obtener_especificos_por_genero(genero_id)
