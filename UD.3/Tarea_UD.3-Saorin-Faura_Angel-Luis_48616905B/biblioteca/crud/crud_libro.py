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




# from biblioteca.modelos.libro import Libro
# from biblioteca.utilidades.validaciones import *

# def crear_libro(biblioteca):
#     """Crear un nuevo libro y lo añade a la Biblioteca."""

#     try:
#         print("\n- Nuevo Registro de Libro -\n")
#         titulo = input("Introduce el título del libro:\n")
        
#         try:         
#             especifico = validar_genero_especifico(biblioteca)
        
#         except Exception as ErrorValidarEspecifico:
#             print(f"Error: Método validar_especifico no funciona, {ErrorValidarEspecifico}")
             
#         num_paginas = int(input("\nIntroduce el numero de paginas:\n"))

#         try:        
#             # Tratamiento de validación de la fecha de publicación como objeto date()
#             fecha_publicacion_str = input("Introduce la fecha de publicación (DD-MM-AAAA):\n")
#             fecha_publicacion = validar_fecha(fecha_publicacion_str)

#             if not fecha_publicacion:
#                 print("\nRegistro cancelado: Fecha de publicación inválida. Revise la información proporcionada.\n")
#                 return
        
#         except Exception as ErrorValidarFecha:
#             print(f"Error: Método validar_fecha no funciona, {ErrorValidarFecha}")

#         try:
#             autor = validar_autor(biblioteca)
        
#         except Exception as ErrorValidarAutor:
#             print(f"Error: Método validar_fecha no funciona, {ErrorValidarAutor}")
            
#         # Creación y registro del nuevo objeto libro
#         libro = Libro(titulo = titulo, especifico = especifico, fecha_publicacion = fecha_publicacion, num_paginas = num_paginas, autor = autor)
#         biblioteca.agregar_libro(libro)  # Usar la instancia de biblioteca

#         print(f"\nEl libro '{titulo}' registrado correctamente.\n")

#     except ValueError as e:                              # Valores incorrectos al ingresar datos
#         print(f"\nError: Entrada inválida. {e}\n")
#     except Exception as e2:                               # Errores imprevistos
#         print(f"\nSe produjo un error inesperado: {e2}\n")

# def mostrar_libros(biblioteca):
#     """Devuelve una lista completa de todos los libros existentes en la Biblioteca."""
#     libros = biblioteca.mostrar_libros()
#     if libros:
#         print("\n- Registro Completo de Libros existentes en la Biblioteca -\n")
#         for libro in libros:
#             print(libro)
#     else:
#         print("\nNo existe ningún registro aún en la Biblioteca.\n")
#     return

# def leer_libro(biblioteca):
#     """Busca y muestra la información de un libro por título."""

#     try:
#         print("\n- Información del Registro deseado -\n")
#         titulo = input("Introduzca el título del libro a buscar:\n")
#         libro = biblioteca.buscar_libro_titulo(titulo)

#         if libro:
#             print("\nRegistro encontrado.\n")
#             print(libro.mostrar_datos_libro())
#         else:
#             print("\nTítulo no encontrado. Revise la información proporcionada e inténtelo de nuevo.\n")

#     except Exception as e:                                         # Errores imprevistos
#         print(f"Se produjo un error al buscar el libro: {e}")

# def actualizar_libro(biblioteca):
#     """Actualiza la información de un libro existente."""

#     try:
#         print("\n- Actualización del Registro -\n")
#         titulo = input("Introduce el título del libro que deseas actualizar:\n")
#         libro = biblioteca.buscar_libro_titulo(titulo)

#         if libro:
#             print("\nIntroduce los nuevos datos del libro (deja en blanco para mantener la información actual:)\n")

#             nuevo_titulo = input(f"Título [{libro.get_titulo()}] o presione ENTER si no es el dato a modificar:\n") or libro.get_titulo()
#             nuevo_autor = input(f"Autor [{libro.get_autor()}] o presione ENTER si no es el dato a modificar:\n") or libro.get_autor()
#             nueva_fecha_publicacion = input(f"Fecha de Publicación [{libro.get_fecha_publicacion()}] o presione ENTER si no es el dato a modificar:\n") or libro.get_fecha_publicacion()
#             nueva_num_paginas = input(f"Nº de Páginas[{libro.get_num_paginas()}] o presione ENTER si no es el dato a modificar:\n") or libro.get_num_paginas()
            
#             libro.set_titulo(nuevo_titulo)
#             libro.set_autor(nuevo_autor)
#             libro.set_fecha_publicacion(nueva_fecha_publicacion)

#             if nueva_num_paginas:
#                 libro.set_num_paginas(int(nueva_num_paginas))

#             print("\nLibro actualizado correctamente.\n")

#         else:
#             print("\nLibro no encontrado.\n")

#     except ValueError as e:                                                    # Valores incorrectos al ingresar datos
#         print(f"Error: Entrada inválida. {e}")

#     except Exception as e:                                                     # Errores imprevistos
#         print(f"Se produjo un error inesperado. {e}")



# def eliminar_libro(biblioteca):
#     """Elimina un libro de la biblioteca y reestructura los IDs."""
#     try:
#         print("\n- Borrado de Registro -\n")
#         titulo = input("Introduce el título del libro que deseas borrar:\n").strip().lower()
        
#         # Usar el método buscar_libro_titulo para encontrar el libro
#         libro_a_eliminar = biblioteca.buscar_libro_titulo(titulo)
#         print(f"Título ingresado: '{titulo}'")  # Para depuración
        
#         if libro_a_eliminar:
#             print(f"Libro encontrado para eliminar: {libro_a_eliminar.get_titulo()}")  # Depuración
#             libro_id = libro_a_eliminar.get_id()
#             print(f"ID del libro a eliminar: {libro_id}")  # Depuración
            
#             # Eliminar del diccionario usando el título (clave)
#             if titulo in biblioteca.diccionario_libros:
#                 del biblioteca.diccionario_libros[titulo]
#                 print("El registro ha sido eliminado correctamente.")
                
#                 # Actualizar la lista de libros después de eliminar
#                 biblioteca.libros = list(biblioteca.diccionario_libros.values())
                
#                 # Reestructurar los IDs de diccionario después de eliminar
#                 biblioteca.reestructurar_ids_libros()
#             else:
#                 print(f"Error: No se pudo encontrar el libro con título '{titulo}' en el diccionario.")
            
#         else:
#             print("No se encontró ningún registro con ese título.\nCompruebe búsqueda e inténtelo de nuevo.")

#     except Exception as e:
#         print(f"\nSe produjo un error al intentar eliminar el libro: {e}\n")



