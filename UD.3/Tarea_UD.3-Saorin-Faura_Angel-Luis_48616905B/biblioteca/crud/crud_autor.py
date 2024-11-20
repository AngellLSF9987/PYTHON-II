# biblioteca/crud/crud_autor.py
import json

class CRUDAutor:

    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.datos = self.cargar_datos()

    def cargar_datos(self):
        """Carga los datos desde el archivo JSON."""
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            # Si no existe el archivo, se crea con una lista vacía de autores
            return {"autores": []}
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. El archivo está vacío o malformado.")
            return {"autores": []}

    def guardar_datos(self):
        """Guarda los datos al archivo JSON."""
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump(self.datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos en el archivo: {e}")

    def agregar_autor(self, autor):
        """Agrega un nuevo autor al listado de autores."""
        self.datos["autores"].append(autor)
        self.guardar_datos()  # Guardar después de agregar

    def actualizar_autor(self, id_autor, nuevos_datos):
        """Actualiza los datos de un autor buscando por su ID."""
        for autor in self.datos["autores"]:
            if autor["autor_id"] == id_autor:
                autor.update(nuevos_datos)  # Actualiza los datos del autor
                self.guardar_datos()  # Guardar después de actualizar
                return True
        return False  # Si no se encuentra el autor, devuelve False

    def eliminar_autor(self, id_autor):
        """Elimina un autor por su ID."""
        for autor in self.datos["autores"]:
            if autor["autor_id"] == id_autor:
                self.datos["autores"].remove(autor)
                self.guardar_datos()  # Guardar después de eliminar
                return True
        return False  # Si no se encuentra el autor, devuelve False

    def buscar_autor_por_id(self, id_autor):
        """Busca un autor por su ID y devuelve los datos del autor si lo encuentra."""
        for autor in self.datos["autores"]:
            if autor["autor_id"] == id_autor:
                return autor
        return None  # Retorna None si no encuentra el autor

    def mostrar_autores(self):
        """Devuelve todos los autores registrados en el sistema."""
        if not self.datos["autores"]:
            print("\nNo hay autores registrados.")
            return []
        for autor in self.datos["autores"]:
            print(f"ID: {autor['autor_id']}, Nombre: {autor['nombre']}, Pseudónimo: {autor.get('pseudonimo', 'No disponible')}")
        return self.datos["autores"]

    def buscar_autor_por_nombre_o_pseudonimo(self, nombre_o_pseudonimo):
        """Busca un autor por nombre o pseudónimo y devuelve los datos."""
        for autor in self.datos["autores"]:
            if autor['nombre'].lower() == nombre_o_pseudonimo.lower() or autor.get('pseudonimo', '').lower() == nombre_o_pseudonimo.lower():
                return autor
        return None  # Retorna None si no encuentra el autor
