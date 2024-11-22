class CRUDGenero:
    def __init__(self, repositorio_genero):
        self.repositorio = repositorio_genero

    def mostrar_generos(self):
        generos = self.repositorio.obtener_generos()
        if not generos:
            print("\nNo hay géneros literarios registrados.")
        else:
            print("\n=== Lista de Géneros Literarios ===")
            for genero in generos:
                print(f"ID: {genero['genero_id']} | Género Literario: {genero['nombre_genero']}")

    def agregar_genero(self, nombre_genero):
        if not self.repositorio.buscar_genero_por_nombre(nombre_genero):
            self.repositorio.agregar_genero(nombre_genero)
        else:
            print(f"El género '{nombre_genero}' ya está registrado.")

    def eliminar_genero(self, genero_id):
        self.repositorio.eliminar_genero(genero_id)

    def buscar_genero(self, nombre_genero):
        genero = self.repositorio.buscar_genero_por_nombre(nombre_genero)
        if genero:
            print(f"Género encontrado: ID {genero['genero_id']} | Nombre: {genero['nombre_genero']}")
        else:
            print(f"No se encontró el género '{nombre_genero}'.")
