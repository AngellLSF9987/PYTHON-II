# biblioteca/crud/crud_libro.py
import json

class CRUDLibro:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.datos = self.cargar_datos()

    def cargar_datos(self):
        # Cargar los datos desde el archivo JSON
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {"libros": []}  # Si no hay archivo, devolver un diccionario vacío

    def guardar_datos(self):
        # Guardar todos los datos al archivo JSON
        with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
            json.dump(self.datos, archivo, ensure_ascii=False, indent=4)

    def agregar_libro(self, libro):
        # Agregar un libro al listado de libros
        self.datos["libros"].append(libro)
        self.guardar_datos()  # Guardar después de agregar

    def actualizar_libro(self, id_libro, nuevos_datos):
        # Buscar el libro por ID y actualizar sus datos
        for libro in self.datos["libros"]:
            if libro["id"] == id_libro:
                libro.update(nuevos_datos)  # Actualiza los datos del libro
                self.guardar_datos()  # Guardar después de actualizar
                return True
        return False  # Si no se encuentra el libro, devuelve False

    def eliminar_libro(self, id_libro):
        # Eliminar un libro por ID
        for libro in self.datos["libros"]:
            if libro["id"] == id_libro:
                self.datos["libros"].remove(libro)
                self.guardar_datos()  # Guardar después de eliminar
                return True
        return False  # Si no se encuentra el libro, devuelve False

    def mostrar_libros_crud(self, biblioteca):
        """Muestra todos los Libros."""
        libros = self.datos["libros"]
        if not libros:
            print("⚠️ No hay libros registrados.")
            return

        print("\n=== Lista de Libros ===")
        for libro in libros:
            print(
                f"ID: {libro['libro_id']} | Género y Subgénero Literario: {libro['especifico_id']} | "
                f"Fecha de Publicación: {libro['fecha_publicacion']} | Núm. Páginas: {libro['num_paginas']} | "
                f"Autor: {libro['autor_id']} | Género Asociado: {libro['nombre_genero']}"
            )



