import json
class RepositorioLibro:
    def __init__(self, repositorio_autor, repositorio_genero, repositorio_especifico, ruta_json):
        self.repositorio_autor = repositorio_autor
        self.repositorio_genero = repositorio_genero
        self.repositorio_especifico = repositorio_especifico
        self.ruta_json = ruta_json
        self.datos = self._cargar_libros()
        self.libros = self.datos.get("libros", [])

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

    def agregar_libro(self, libro):
        if any(l["libro_id"] == libro["libro_id"] for l in self.libros):
            print(f"El libro con ID {libro['libro_id']} ya existe.")
            return

        libro["num_paginas"] = int(libro.get("num_paginas", 0))
        autor = self.repositorio_autor.obtener_autor_por_id(libro.get("autor_id")) or {"pseudonimo": "Autor desconocido"}
        genero = self.repositorio_genero.obtener_genero_por_id(libro.get("genero_id")) or {"nombre_genero": "Género desconocido"}
        especifico = self.repositorio_especifico.obtener_especifico_por_id(libro.get("especifico_id")) or {"nombre_especifico": "Subgénero desconocido"}

        libro["nombre_autor"] = autor["pseudonimo"]
        libro["nombre_genero"] = genero["nombre_genero"]
        libro["nombre_especifico"] = especifico["nombre_especifico"]

        self.libros.append(libro)
        self._guardar_libros()
        print(f"Libro '{libro['titulo']}' agregado correctamente.")

    def obtener_libro_por_id(self, libro_id):
        return next((l for l in self.libros if l["libro_id"] == libro_id), None)

    def mostrar_libros(self):
        if not self.libros:  # Verificar si no hay libros antes de procesarlos
            print("⚠️ No hay libros registrados en la biblioteca.")
            return

        print("\n=== Lista de Libros ===\n")
        libros_mostrados = 0  # Contador de libros correctamente procesados

        for libro in self.libros:
            try:
                # Obtener los datos relacionados
                autor = self.repositorio_autor.obtener_autor_por_id(libro["autor_id"])
                especifico = self.repositorio_especifico.obtener_especifico_por_id(libro["especifico_id"])
                genero = self.repositorio_genero.obtener_genero_por_id(libro["genero_id"])

                # Validar datos obtenidos
                nombre_autor_completo = (
                    f"{autor['nombre']} {autor['apellido1']} {autor['apellido2']} | Pseudónimo: {autor['pseudonimo']}" if autor else "Autor desconocido"
                )
                nombre_genero = genero["nombre_genero"] if genero else "Género desconocido"
                nombre_especifico = especifico["nombre_especifico"] if especifico else "Subgénero desconocido"
                tipo_especifico = especifico["tipo"] if especifico else "Desconocido"

                # Imprimir información del libro
                print(f"ID: {libro['libro_id']} | Título del Libro: {libro['titulo']}")
                print(f"Autor: {nombre_autor_completo}")
                print(f"Género Literario: {nombre_genero} | Subgénero Literario: {nombre_especifico} - Tipo de Subgénero Literario: {tipo_especifico}")
                print(f"Fecha de publicación: {libro['fecha_publicacion']} | Número de páginas: {libro['num_paginas']}")
                print("-----")

                libros_mostrados += 1  # Incrementar el contador de libros mostrados

            except Exception as e:
                print(f"⚠️ Error al procesar el libro con ID {libro['libro_id']}: {e}")

    def obtener_libros(self):
        """Devuelve la lista de libros."""
        return self.libros