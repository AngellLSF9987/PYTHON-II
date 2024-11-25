import json
import shutil
class CRUDLibro:
    def __init__(self, ruta_json, repositorio_autor, repositorio_especifico, repositorio_genero):
        self.ruta_json = ruta_json
        self.repositorio_autor = repositorio_autor
        self.repositorio_especifico = repositorio_especifico
        self.repositorio_genero = repositorio_genero
        self.datos = self._cargar_libros()  # Carga los datos al inicializar
        self.libro_id_actual = self.obtener_max_id() + 1  # Inicializar ID autoincremental

    def _cargar_libros(self):
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)
                print("Libros cargados correctamente.")
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            print("Archivo de Libros no encontrado o vacío. Se iniciará con una lista vacía.")
            return {"libros": []}  # Retorna un diccionario vacío en caso de error

    def _guardar_libros(self):
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump(self.datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def obtener_max_id(self):
        """Obtiene el máximo ID existente en los libros."""
        if not self.datos["libros"]:
            return 0  # Si no hay libros, inicia en 0
        return max(int(libro["libro_id"]) for libro in self.datos["libros"])

    def agregar_libro(self, nuevo_libro):
        """Agrega un nuevo Libro con ID autoincremental."""
        nuevo_libro["libro_id"] = str(self.libro_id_actual)
        self.datos["libros"].append(nuevo_libro)
        self.libro_id_actual += 1  # Incrementa el ID para el siguiente registro
        self._guardar_libros()
        print(f"✅ Libro agregado con éxito: {nuevo_libro['titulo']}")
        return True

    def actualizar_libro(self, id_libro, nuevos_datos):
        """Busca un libro por ID y actualiza sus datos."""
        for libro in self.datos["libros"]:
            if libro["libro_id"] == id_libro:
                libro.update(nuevos_datos)  # Actualiza los datos del libro
                self._guardar_libros()  # Guarda después de actualizar
                return True
        return False  # Si no se encuentra el libro, devuelve False

    def mostrar_libros(self):
        """Muestra todos los libros registrados, con detalles de autor y subgénero."""
        libros = self.datos["libros"]
        if not libros:
            print("⚠️ No hay libros registrados.")
            return

        print("\n=== Lista de Libros ===")
        for libro in libros:
            # Obtener autor por autor_id
            autor = self.repositorio_autor.obtener_autor_por_id(libro['autor_id'])
            # print(f"Autor encontrado para ID {libro['autor_id']}: {autor}")
            nombre_autor_completo = (
                    f"{autor['nombre']} {autor['apellido1']} {autor['apellido2']} | Pseudónimo: {autor['pseudonimo']}" if autor else "Autor desconocido"
                )
            
            # Obtener género y tipo por genero_id
            genero = self.repositorio_genero.obtener_genero_por_id(libro['genero_id'])
            # print(f"Género encontrado para ID {libro['genero_id']}: {genero}")
            nombre_genero = f"{genero['nombre_genero']}"

            # Obtener subgénero y tipo por especifico_id
            especifico = self.repositorio_especifico.obtener_especifico_por_id(libro['especifico_id'])
            # print(f"Subgénero encontrado para ID {libro['especifico_id']}: {especifico}")
            nombre_especifico = f"{especifico['nombre_especifico']}" if especifico else "Subgénero desconocido"
            tipo_especifico = f"{especifico['tipo']}" if especifico else "Tipo desconocido"
            


            # Imprimir información del libro
            print(f"ID: {libro['libro_id']} | Título del Libro: {libro['titulo']}")
            print(f"Autor: {nombre_autor_completo}")
            print(f"Género Literario: {nombre_genero} | Subgénero Literario: {nombre_especifico} - Tipo de Subgénero Literario: {tipo_especifico}")
            print(f"Fecha de publicación: {libro['fecha_publicacion']} | Número de páginas: {libro['num_paginas']}")
            print("-----")

    def buscar_libro_por_id(self, id_libro):
        """Busca un libro por su ID."""
        for libro in self.datos["libros"]:
            if libro["libro_id"] == id_libro:
                return libro
        return None  # Si no se encuentra, devuelve None
    
    def buscar_libro_por_titulo(self, biblioteca):
        """Permite buscar un libro por su título y muestra detalles relevantes."""
        titulo = input("\nIngrese el título del libro que desea buscar:\n").strip()

        if not titulo:
            print("\n⚠️ No ingresó un título. Inténtelo de nuevo.")
            return

        try:
            libros = biblioteca.repositorio_libro.libros
            resultados = [libro for libro in libros if titulo.lower() in libro["titulo"].lower()]

            if resultados:
                print("\n=== Resultados de la búsqueda ===\n")
                for libro in resultados:
                    genero = biblioteca.repositorio_genero.obtener_genero_por_id(libro["genero_id"])
                    nombre_genero = genero["nombre_genero"] if genero else "Género Literario Desconocido"
                    especifico = biblioteca.repositorio_especifico.obtener_especifico_por_id(libro["especifico_id"])                
                    nombre_especifico = especifico["nombre_especifico"] if especifico else "Subgénero Literario Desconocido"
                    tipo = especifico['tipo'] if especifico else "Tipo Desconocido"
                    autor = biblioteca.repositorio_autor.obtener_autor_por_id(libro["autor_id"])
                    autor_nombre = autor["nombre"] if autor else " Autor Desconocido"


                    print(
                        f"ID: {libro['libro_id']}\n"
                        f"Título: {libro['titulo']}\n"
                        f"Género Literario: {nombre_genero} | Subgénero Literario: {nombre_especifico} - Tipo: {tipo}\n"
                        f"Fecha de Publicación: {libro['fecha_publicacion']}\n"
                        f"Autor: {autor_nombre}\n"
                    )
            else:
                print("\n⚠️ No se encontraron libros con ese título.")
        except Exception as e:
            print(f"\n⚠️ Error inesperado al buscar libros: {e}")


    def eliminar_libro(self, id_libro):
        """Elimina un libro por ID."""
        for libro in self.datos["libros"]:
            if libro["libro_id"] == id_libro:
                self.datos["libros"].remove(libro)
                self._guardar_libros()  # Guarda después de eliminar
                return True
        return False  # Si no se encuentra el libro, devuelve False
