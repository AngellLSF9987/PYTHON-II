import json

class RepositorioLibro:
    def __init__(self, repositorio_autor, repositorio_especifico, ruta_json):
        """
        Constructor del repositorio de libros.
        :param repositorio_autor: Instancia de RepositorioAutor.
        :param repositorio_especifico: Instancia de RepositorioEspecifico.
        :param ruta_json: Ruta del archivo JSON donde se guardan los datos.
        """
        self.repositorio_autor = repositorio_autor  # Repositorio de autores
        self.repositorio_especifico = repositorio_especifico  # Repositorio de géneros específicos
        self.ruta_json = ruta_json  # Ruta del archivo JSON de libros
        self.libros = []  # Lista para almacenar los libros como diccionarios
        self.cargar_libros()

    def cargar_libros(self):
        """Carga los libros desde el archivo JSON a la lista de libros."""
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)
                self.libros = data.get("libros", [])
            print("Carga de datos de libros correcta.")
        except Exception as e:
            print(f"Error al cargar libros: {e}")

    def obtener_libros(self):
        """Devuelve todos los Libros."""
        return self.libros

    def guardar_datos(self):
        """Guarda los datos actuales en el archivo JSON."""
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump({"libros": self.libros}, archivo, ensure_ascii=False, indent=4)
            print("Datos guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def agregar_libro(self, libro):
        """Agrega un único libro al repositorio."""
        if isinstance(libro, dict) and "libro_id" in libro:
            if not self.obtener_libro_por_id(libro["libro_id"]):
                # Obtener subgénero y autor si existen
                especifico = self.repositorio_especifico.obtener_especifico_por_id(libro.get("especifico_id"))
                if especifico is None:
                    print(f"Aviso: No se encontró un subgénero con ID {libro.get('especifico_id')}. Asignando 'Género desconocido'.")
                    especifico_nombre = "Género desconocido"
                else:
                    especifico_nombre = especifico["nombre_especifico"]

                autor = self.repositorio_autor.obtener_autor_por_id(libro.get("autor_id"))
                if autor is None:
                    print(f"Aviso: No se encontró un autor con ID {libro.get('autor_id')}. Asignando 'Autor desconocido'.")
                    autor_nombre = "Autor desconocido"
                else:
                    autor_nombre = autor["pseudonimo"]

                # Validación del título del libro
                titulo = libro.get("titulo", "").strip()
                if not titulo:
                    print(f"Aviso: El libro no tiene un título definido. Asignando 'Título desconocido'.")
                    titulo = "Título desconocido"

                # Validación de la fecha de publicación
                fecha_publicacion = libro.get("fecha_publicacion", "").strip()
                if not fecha_publicacion:
                    print(f"Aviso: El libro no tiene una fecha de publicación definida. Asignando 'Fecha desconocida'.")
                    fecha_publicacion = "Fecha desconocida"

                # Validación del número de páginas
                num_paginas = libro.get("num_paginas", "").strip()
                if not num_paginas:
                    print(f"Aviso: El libro no tiene un número de páginas definido. Asignando '0'.")
                    num_paginas = "0"

                # Agregar el libro
                libro_dict = {
                    "libro_id": libro["libro_id"],
                    "titulo": titulo,
                    "especifico_id": libro.get("especifico_id"),
                    "nombre_especifico": especifico_nombre,
                    "fecha_publicacion": fecha_publicacion,
                    "num_paginas": num_paginas,
                    "autor_id": libro.get("autor_id"),
                    "nombre_autor": autor_nombre,
                }
                self.libros.append(libro_dict)
                print(f"Libro con ID {libro['libro_id']} agregado correctamente.")
                self.guardar_datos()  # Guardar los cambios al archivo JSON
            else:
                print(f"El libro con ID {libro['libro_id']} ya existe.")
        else:
            print(f"Formato inválido para el libro: {libro}")

    def obtener_libro_por_id(self, libro_id):
        """Busca un libro por su ID."""
        for libro in self.libros:
            if libro["libro_id"] == libro_id:
                return libro
        return None

    def obtener_libros_por_autor(self, autor_id):
        """Obtiene todos los libros asociados a un autor dado."""
        libros_autor = [libro for libro in self.libros if libro["autor_id"] == autor_id]
        if not libros_autor:
            print(f"No se encontraron libros para el autor con ID {autor_id}.")
        return libros_autor

    def obtener_libros_por_especifico(self, especifico_id):
        """Obtiene todos los libros asociados a un subgénero específico dado."""
        libros_especifico = [libro for libro in self.libros if libro["especifico_id"] == especifico_id]
        if not libros_especifico:
            print(f"No se encontraron libros para el subgénero específico con ID {especifico_id}.")
        return libros_especifico

    def mostrar_libros(self):
        """Muestra todos los libros cargados."""
        if self.libros:
            print("=== Todos los Libros ===")
            for libro in self.libros:
                print(f"ID: {libro['libro_id']} | Título: {libro['titulo']} | Autor: {libro['autor_id']} | "
                      f"Subgénero: {libro['especifico_id']} | Fecha de Publicación: {libro['fecha_publicacion']} | "
                      f"Num. Páginas: {libro['num_paginas']}")
        else:
            print("No hay libros cargados.")

    def eliminar_libro_por_id(self, libro_id):
        """Elimina un libro del repositorio por su ID."""
        libro = self.obtener_libro_por_id(libro_id)
        if libro:
            self.libros.remove(libro)
            print(f"Libro con ID {libro_id} eliminado correctamente.")
            self.guardar_datos()  # Guardar los cambios al archivo JSON
        else:
            print(f"No se encontró un libro con ID {libro_id} para eliminar.")
