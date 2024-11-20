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
            print("Archivo JSON no encontrado. Se creará un nuevo archivo.")
            return {"autores": []}  # Inicializa con lista vacía si no existe
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

    def agregar_autor(self, nombre, pseudonimo=None, nacionalidad=None):
        """
        Agrega un nuevo autor con ID autoincremental.
        Parámetros:
            - nombre: Nombre completo del autor (obligatorio).
            - pseudonimo: Pseudónimo del autor (opcional).
            - nacionalidad: Nacionalidad del autor (opcional).
        """
        if not nombre.strip():
            print("⚠️ El nombre del autor no puede estar vacío.")
            return False

        autor = {
            "autor_id": str(self.autor_id_actual),
            "nombre": nombre.strip(),
            "pseudonimo": pseudonimo.strip() if pseudonimo else None,
            "nacionalidad": nacionalidad.strip() if nacionalidad else "Desconocida",
        }
        self.datos["autores"].append(autor)
        self.autor_id_actual += 1
        self.guardar_datos()
        print(f"✅ Autor agregado con éxito: {autor}")
        return True

    def actualizar_autor(self, autor_id, nuevos_datos):
        """
        Actualiza los datos de un autor buscando por su ID.
        Parámetros:
            - id_autor: ID del autor a actualizar.
            - nuevos_datos: Diccionario con los nuevos valores.
        """
        for autor in self.datos["autores"]:
            if autor["autor_id"] == autor_id:
                autor.update({clave: valor.strip() for clave, valor in nuevos_datos.items() if valor is not None})
                self.guardar_datos()
                print(f"✅ Autor actualizado con éxito: {autor}")
                return True
        print(f"⚠️ No se encontró un autor con ID {autor_id}.")
        return False

    def eliminar_autor(self, autor_id):
        """
        Elimina un autor por su ID.
        Parámetros:
            - id_autor: ID del autor a eliminar.
        """
        for autor in self.datos["autores"]:
            if autor["autor_id"] == autor_id:
                self.datos["autores"].remove(autor)
                self.guardar_datos()
                print(f"✅ Autor eliminado con éxito: {autor}")
                return True
        print(f"⚠️ No se encontró un autor con ID {autor_id}.")
        return False

    def buscar_autor_por_id(self, autor_id):
        """
        Busca un autor por su ID.
        Parámetros:
            - autor_id: ID del autor a buscar.
        """
        for autor in self.datos["autores"]:
            if autor["autor_id"] == autor_id:
                return autor
        return None

    def buscar_autor_por_nombre_o_pseudonimo(self, nombre_o_pseudonimo):
        """
        Busca un autor por nombre o pseudónimo.
        Parámetros:
            - nombre_o_pseudonimo: Nombre completo o pseudónimo del autor.
        """
        for autor in self.datos["autores"]:
            if (autor["nombre"].lower() == nombre_o_pseudonimo.lower() or
                    autor.get("pseudonimo", "").lower() == nombre_o_pseudonimo.lower()):
                return autor
        return None

    def buscar_autor_por_coincidencia(self, criterio):
        """
        Busca autores que coincidan parcialmente con un nombre o pseudónimo.
        Parámetros:
            - criterio: Texto para buscar coincidencias.
        """
        coincidencias = [
            autor for autor in self.datos["autores"]
            if criterio.lower() in autor["nombre"].lower() or
               criterio.lower() in autor.get("pseudonimo", "").lower()
        ]
        return coincidencias

    def mostrar_autores(self):
        """
        Muestra todos los autores registrados.
        """
        if not self.datos["autores"]:
            print("\nNo hay autores registrados.")
            return
        print("\n=== Lista de Autores ===")
        for autor in self.datos["autores"]:
            print(f"ID: {autor['autor_id']}, Nombre: {autor['nombre']}, "
                  f"Pseudónimo: {autor.get('pseudonimo', 'No disponible')}, "
                  f"Nacionalidad: {autor['nacionalidad']}")
