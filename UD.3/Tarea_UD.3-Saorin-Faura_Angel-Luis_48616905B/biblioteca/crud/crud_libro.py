import json

class CRUDLibro:
    def __init__(self, ruta_json, repositorio_autor, repositorio_especifico, repositorio_genero):
        self.ruta_json = ruta_json
        self.repositorio_autor = repositorio_autor  # Asegúrate de inicializarlo
        self.repositorio_especifico = repositorio_especifico
        self.repositorio_genero = repositorio_genero
        self.datos = self.cargar_datos()  # Carga los datos al inicializar

    def cargar_datos(self):
        """Carga los datos desde el archivo JSON y los asigna a self.datos."""
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {"libros": [], "subgeneros": [], "autores": [], "generos": []}  # Datos vacíos por defecto

    def guardar_datos(self):
        """Guarda todos los datos en el archivo JSON."""
        with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
            json.dump(self.datos, archivo, ensure_ascii=False, indent=4)

    def obtener_ultimo_libro_id(self):
        """Obtiene el último ID de libro para autoincrementar el siguiente."""
        if self.datos["libros"]:
            return max(libro["libro_id"] for libro in self.datos["libros"])
        return 0  # Si no hay libros, comienza con ID 0

    def agregar_libro(self, libro):
        """Agrega un nuevo libro al listado de libros."""
        libro["libro_id"] = self.obtener_ultimo_libro_id() + 1  # Autoincrementa el ID
        self.datos["libros"].append(libro)
        self.guardar_datos()  # Guarda después de agregar

    def actualizar_libro(self, id_libro, nuevos_datos):
        """Busca un libro por ID y actualiza sus datos."""
        for libro in self.datos["libros"]:
            if libro["libro_id"] == id_libro:
                libro.update(nuevos_datos)  # Actualiza los datos del libro
                self.guardar_datos()  # Guarda después de actualizar
                return True
        return False  # Si no se encuentra el libro, devuelve False

    def mostrar_libros_crud(self, biblioteca):
        """Muestra todos los libros registrados, con detalles de autor y subgénero."""
        libros = self.datos["libros"]
        if not libros:
            print("⚠️ No hay libros registrados.")
            return

        print("\n=== Lista de Libros ===")
        for libro in libros:
            # Obtener autor por autor_id
            autor = self.repositorio_autor.obtener_autor_por_id(libro['autor_id'])
            autor_nombre_completo = f"{autor['nombre']} {autor['apellido1']} {autor['apellido2']}" if autor else "Autor desconocido"
            
            # Obtener subgénero y género por especifico_id
            especifico = self.repositorio_especifico.obtener_especifico_por_id(libro['especifico_id'])
            if especifico:
                genero = self.repositorio_genero.obtener_genero_por_id(especifico['genero_id'])
                genero_nombre = genero["nombre_genero"] if genero else "Género desconocido"
                subgenero_nombre = especifico["nombre_especifico"]
                subgenero_tipo = especifico["tipo"]
            else:
                genero_nombre = subgenero_nombre = subgenero_tipo = "Subgénero desconocido"

            print(
                f"ID: {libro['libro_id']} | Título del Libro: {libro['titulo']} | "
                f"Género: {genero_nombre} | Subgénero: {subgenero_nombre} | Tipo: {subgenero_tipo} | "
                f"Fecha de Publicación: {libro['fecha_publicacion']} | Núm. Páginas: {libro['num_paginas']} | "
                f"Autor: {autor_nombre_completo}"
            )

    def buscar_libro_por_id(self, id_libro):
        """Busca un libro por su ID."""
        for libro in self.datos["libros"]:
            if libro["libro_id"] == id_libro:
                return libro
        return None  # Si no se encuentra, devuelve None

    def eliminar_libro(self, id_libro):
        """Elimina un libro por ID."""
        for libro in self.datos["libros"]:
            if libro["libro_id"] == id_libro:
                self.datos["libros"].remove(libro)
                self.guardar_datos()  # Guarda después de eliminar
                return True
        return False  # Si no se encuentra el libro, devuelve False
