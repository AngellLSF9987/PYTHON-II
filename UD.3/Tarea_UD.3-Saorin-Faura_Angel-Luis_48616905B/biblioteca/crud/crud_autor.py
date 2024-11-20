import json
import shutil  # Para respaldar datos antes de guardar

class CRUDAutor:

    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.datos = self.cargar_datos()
        self.autor_id_actual = self.obtener_max_id() + 1  # Inicializar ID autoincremental

    def cargar_datos(self):
        """Carga los datos desde el archivo JSON."""
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {"autores": []}  # Si no existe el archivo, inicializa con lista vacía
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Archivo vacío o malformado.")
            return {"autores": []}

    def guardar_datos(self):
        """Guarda los datos en el archivo JSON y realiza un respaldo previo."""
        try:
            # Crear respaldo del archivo
            shutil.copy(self.ruta_json, self.ruta_json + ".bak")
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump(self.datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def obtener_max_id(self):
        """Obtiene el máximo ID existente en los autores."""
        if not self.datos["autores"]:
            return 0  # Si no hay autores, inicia en 0
        return max(int(autor["autor_id"]) for autor in self.datos["autores"])

    def agregar_autor(self, autor):
        """Agrega un nuevo autor con ID autoincremental."""
        autor["autor_id"] = str(self.autor_id_actual)
        self.datos["autores"].append(autor)
        self.autor_id_actual += 1  # Incrementa el ID para el próximo autor
        self.guardar_datos()

    def actualizar_autor(self, id_autor, nuevos_datos):
        """Actualiza los datos de un autor buscando por su ID."""
        for autor in self.datos["autores"]:
            if autor["autor_id"] == id_autor:
                autor.update({k: v for k, v in nuevos_datos.items() if v})  # Solo actualiza campos no vacíos
                self.guardar_datos()
                return True
        return False

    def eliminar_autor(self, id_autor):
        """Elimina un autor por su ID."""
        for autor in self.datos["autores"]:
            if autor["autor_id"] == id_autor:
                self.datos["autores"].remove(autor)
                self.guardar_datos()
                return True
        return False

    def buscar_autor_por_id(self, id_autor):
        """Busca un autor por su ID."""
        for autor in self.datos["autores"]:
            if autor["autor_id"] == id_autor:
                return autor
        return None

    def buscar_autor_por_nombre_o_pseudonimo(self, nombre_o_pseudonimo):
        """Busca un autor por nombre o pseudónimo."""
        for autor in self.datos["autores"]:
            if (autor["nombre"].lower() == nombre_o_pseudonimo.lower() or
                    autor.get("pseudonimo", "").lower() == nombre_o_pseudonimo.lower()):
                return autor
        return None

    def mostrar_autores(self):
        """Muestra todos los autores registrados."""
        if not self.datos["autores"]:
            print("\nNo hay autores registrados.")
            return
        for autor in self.datos["autores"]:
            print(f"ID: {autor['autor_id']}, Nombre: {autor['nombre']}, "
                  f"Pseudónimo: {autor.get('pseudonimo', 'No disponible')}")
