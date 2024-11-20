class RepositorioLibro:
    def __init__(self, repositorio_autor, repositorio_especifico):
        """
        Constructor del repositorio de libros.
        :param repositorio_autor: Instancia de RepositorioAutor.
        :param repositorio_especifico: Instancia de RepositorioEspecifico.
        """
        self.repositorio_autor = repositorio_autor  # Repositorio de autores
        self.repositorio_especifico = repositorio_especifico  # Repositorio de géneros específicos
        self.libros = []  # Lista para almacenar los libros como diccionarios

    def agregar_libros(self, datos_libros):
        """Carga una lista completa de libros en el repositorio."""
        try:
            for libro in datos_libros:
                self.agregar_libro(libro)
            print("Carga de datos de libros correcta.")
        except Exception as e:
            print(f"Error al cargar libros: {e}")

    def agregar_libro(self, libro):
        """Agrega un único libro al repositorio."""
        if isinstance(libro, dict) and "libro_id" in libro:
            if not self.obtener_libro_por_id(libro["libro_id"]):
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

                self.libros.append({
                    "libro_id": libro.get("libro_id"),
                    "titulo": libro.get("titulo", "Desconocido"),
                    "especifico_id": libro.get("especifico_id"),
                    "nombre_especifico": especifico_nombre,
                    "fecha_publicacion": libro.get("fecha_publicacion", "Desconocido"),
                    "num_paginas": libro.get("num_paginas", "Desconocido"),
                    "autor_id": libro.get("autor_id"),
                    "nombre_autor": autor_nombre,
                })
            else:
                print(f"El libro con ID {libro['libro_id']} ya existe.")
        else:
            print(f"Formato inválido para el libro: {libro}")

    def mostrar_libros(self):
        """Devuelve una representación formateada de los libros en el repositorio."""
        if not self.libros:
            return "No hay libros cargados en el repositorio."

        return "\n".join(
            f"ID: {libro['libro_id']}\nTítulo: {libro['titulo']}\n"
            f"Género y Subgénero Específico: {libro['nombre_especifico']}\n"
            f"Fecha de Publicación: {libro['fecha_publicacion']}\n"
            f"Número de Páginas: {libro['num_paginas']}\n"
            f"Autor: {libro['nombre_autor']}\n"
            for libro in self.libros
        )

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

    def eliminar_libro_por_id(self, libro_id):
        """Elimina un libro del repositorio por su ID."""
        libro = self.obtener_libro_por_id(libro_id)
        if libro:
            self.libros.remove(libro)
            print(f"Libro con ID {libro_id} eliminado correctamente.")
        else:
            print(f"No se encontró un libro con ID {libro_id} para eliminar.")
