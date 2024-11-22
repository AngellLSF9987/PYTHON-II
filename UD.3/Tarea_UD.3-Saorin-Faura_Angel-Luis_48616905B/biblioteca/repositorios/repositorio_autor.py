
import json
class RepositorioAutor:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.autores = []
        self._cargar_autores()

    def _cargar_autores(self):
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)
                self.autores = data.get("autores", [])
            print("Autores cargados correctamente.")
        except Exception as e:
            print(f"Error al cargar autores: {e}")

    def _guardar_datos(self):
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump({"autores": self.autores}, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def agregar_autor(self, autor):
        if any(a["autor_id"] == autor["autor_id"] for a in self.autores):
            print(f"El autor con ID {autor['autor_id']} ya existe.")
            return
        self.autores.append(autor)
        self._guardar_datos()
        print(f"Autor '{autor['nombre']} {autor['apellido1']}' agregado correctamente.")

    def mostrar_autores(self):
        """
        Muestra todos los autores almacenados.
        """
        if self.autores:
            print("\n=== Lista de Autores ===")
            for autor in self.autores:
                print(f"ID: {autor['autor_id']} | Nombre Completo: {autor['nombre']} | Pseudónimo: {autor.get('pseudonimo', 'N/A')}")
        else:
            print("No hay autores registrados.")

