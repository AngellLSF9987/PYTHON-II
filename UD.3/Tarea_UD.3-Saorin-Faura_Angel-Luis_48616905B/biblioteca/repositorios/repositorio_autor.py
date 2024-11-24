
import json
class RepositorioAutor:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.datos = self._cargar_autores()
        self.autores = self.datos.get("autores", [])

    def _cargar_autores(self):
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)
                print("Autores cargados correctamente.")
                return data  # Retorna directamente el contenido del archivo
        except (FileNotFoundError, json.JSONDecodeError):
            print("Archivo de Autores no encontrado o vacío. Se iniciará con una lista vacía.")
            return {"autores": []}  # Retorna un diccionario vacío en caso de error

    def _guardar_datos(self):
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump(self.datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def agregar_autor(self, autor):
        # Verifica si el autor tiene el campo autor_id
        if "autor_id" not in autor:
            autor["autor_id"] = len(self.autores) + 1  # Asigna un ID único, autoincremental

        if any(a["autor_id"] == autor["autor_id"] for a in self.autores):
            print(f"El autor con ID {autor['autor_id']} ya existe.")
            return
        self.autores.append(autor)
        self._guardar_datos()
        print(f"Autor '{autor['nombre']} {autor['apellido1']}' agregado correctamente.")

    def mostrar_autores(self):
        """Muestra todos los autores almacenados."""
        if self.autores:
            print("\n=== Lista de Autores ===\n")
            for autor in self.autores:
                print(f"> ID: {autor['autor_id']} | Nombre Completo: {autor['nombre']} {autor['apellido1']} {autor['apellido2']} | Pseudónimo: {autor.get('pseudonimo', 'N/A')}\n \
Fecha Nacimiento: {autor['nacido']} | Fecha Fallecimiento: {autor['fallecido'] or 'No fallecido'}\n Nacionalidad: {autor['nacionalidad']}\n")
        else:
            print("No hay autores registrados.")

    def obtener_autor_por_id(self, autor_id):
        for autor in self.autores:
            if autor['autor_id'] == (autor_id):
                return autor
        return None

    def obtener_autores(self):
        """Devuelve la lista de autores."""
        return self.autores

    def obtener_autor_por_pseudonimo(self, pseudonimo):
        """Devuelve un autor por su pseudónimo si existe, sino devuelve None."""
        for autor in self.autores:
            if autor.get("pseudonimo") == pseudonimo:
                return autor  # Si encuentra el autor con el pseudónimo, lo devuelve
        return None  # Si no se encuentra, devuelve None