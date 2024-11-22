import json
class RepositorioLibro:
    def __init__(self, repositorio_autor, repositorio_especifico, ruta_json):
        self.repositorio_autor = repositorio_autor
        self.repositorio_especifico = repositorio_especifico
        self.ruta_json = ruta_json
        self.libros = []
        self.cargar_libros()

    def cargar_libros(self):
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)
                self.libros = data.get("libros", [])
            print("Libros cargados correctamente.")
        except Exception as e:
            print(f"Error al cargar libros: {e}")

    def guardar_datos(self):
        try:
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump({"libros": self.libros}, archivo, ensure_ascii=False, indent=4)
            print("Datos de libros guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def agregar_libro(self, libro):
        if any(l["libro_id"] == libro["libro_id"] for l in self.libros):
            print(f"El libro con ID {libro['libro_id']} ya existe.")
            return

        libro["num_paginas"] = int(libro.get("num_paginas", 0))
        autor = self.repositorio_autor.obtener_autor_por_id(libro.get("autor_id")) or {"pseudonimo": "Autor desconocido"}
        especifico = self.repositorio_especifico.obtener_especifico_por_id(libro.get("especifico_id")) or {"nombre_especifico": "Género desconocido"}

        libro["nombre_autor"] = autor["pseudonimo"]
        libro["nombre_especifico"] = especifico["nombre_especifico"]

        self.libros.append(libro)
        self.guardar_datos()
        print(f"Libro '{libro['titulo']}' agregado correctamente.")

    def obtener_libro_por_id(self, libro_id):
        return next((l for l in self.libros if l["libro_id"] == libro_id), None)

    def mostrar_libros(self):
        return self.libros
