# biblioteca/repositorios/repositorio_autor.py

import json

class RepositorioAutor:
    def __init__(self, ruta_json):
        """Constructor del repositorio de autores."""
        self.ruta_json = ruta_json  # Ruta al archivo JSON
        self.autores = []  # Lista para almacenar autores como diccionarios
        self.cargar_autores()

    def cargar_autores(self):
        """Carga los libros desde el archivo JSON a la lista de libros."""
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)
                self.libros = data.get("libros", [])
            print("Carga de datos de libros correcta.")
        except Exception as e:
            print(f"Error al cargar libros: {e}")

    def obtener_autores(self):
        """Devuelve todos los Autores."""
        return self.autores

    def guardar_datos(self):
        """Guarda los datos actuales en el archivo JSON."""
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump({"autores": self.autores}, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def agregar_autores(self, datos_autores):
        """Carga una lista completa de autores en el repositorio."""
        try:
            for autor in datos_autores:
                self.agregar_autor(autor)
            print("Carga de datos de Autores correcta.")
        except Exception as e:
            print(f"Error al cargar autores: {e}")

    def agregar_autor(self, autor):
        """Agrega un único autor al repositorio."""
        if isinstance(autor, dict) and "autor_id" in autor:
            if not self.obtener_autor_por_id(autor["autor_id"]):
                self.autores.append({
                    "autor_id": autor["autor_id"],
                    "nombre": autor.get("nombre", "Desconocido"),
                    "apellido1": autor.get("apellido1", "Desconocido"),
                    "apellido2": autor.get("apellido2", ""),
                    "pseudonimo": autor.get("pseudonimo", "Sin pseudónimo"),
                    "nacido": autor.get("nacido", "No especificado"),
                    "fallecido": autor.get("fallecido", "No especificado"),
                    "nacionalidad": autor.get("nacionalidad", "Desconocida")
                })
            else:
                print(f"El autor con ID {autor['autor_id']} ya existe.")
        else:
            print(f"Formato inválido para autor: {autor}")

    def obtener_autor_por_id(self, autor_id):
        """Busca un autor por su ID."""
        autor_id = str(autor_id)  # Asegura la coincidencia con el ID como cadena
        for autor in self.autores:
            if str(autor["autor_id"]) == autor_id:
                return autor
        return None

    def buscar_autor_por_nombre_completo(self, nombre, apellido1, apellido2=""):
        """Busca un autor por su nombre completo."""
        for autor in self.autores:
            if (autor["nombre"] == nombre and 
                autor["apellido1"] == apellido1 and 
                autor["apellido2"] == apellido2):
                return autor
        return None

    def buscar_autor_por_pseudonimo(self, pseudonimo):
        """Busca un autor por su pseudónimo."""
        for autor in self.autores:
            if autor["pseudonimo"].lower() == pseudonimo.lower():
                return autor
        return None
    
    def mostrar_autores(self):
        """Devuelve la lista de autores almacenados en el repositorio."""
        if self.autores:
            print("=== Todos los Autores ===")
            for autor in self.autores:
                print(f"ID: {autor['autor_id']}\nNombre: {autor['nombre']} {autor['apellido1']} {autor['apellido2']}\n"
                    f"Pseudónimo: {autor['pseudonimo']}\nNacionalidad: {autor['nacionalidad']}\n"
                    f"Nacido: {autor['nacido']}\nFallecido: {autor['fallecido']}")
        else:
            print("No hay autores cargados en el repositorio.")

    def eliminar_autor_por_id(self, autor_id):
        """Elimina un autor del repositorio por su ID."""
        autor = self.obtener_autor_por_id(autor_id)
        if autor:
            self.autores.remove(autor)
            print(f"Autor con ID {autor_id} eliminado correctamente.")
        else:
            print(f"No se encontró un autor con ID {autor_id} para eliminar.")
