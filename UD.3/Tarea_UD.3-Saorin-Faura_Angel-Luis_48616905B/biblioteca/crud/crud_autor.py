# biblioteca/crud/crud_autor.py
import json

class CRUDAutor:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.datos = self.cargar_datos()

    def cargar_datos(self):
        # Cargar los datos desde el archivo JSON
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {"autores": []}  # Si no hay archivo, devolver un diccionario vacío

    def guardar_datos(self):
        # Guardar todos los datos al archivo JSON
        with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
            json.dump(self.datos, archivo, ensure_ascii=False, indent=4)

    def agregar_autor(self, autor):
        # Agregar un autor al listado de autores
        self.datos["autores"].append(autor)
        self.guardar_datos()  # Guardar después de agregar

    def actualizar_autor(self, id_autor, nuevos_datos):
        # Buscar el autor por ID y actualizar sus datos
        for autor in self.datos["autores"]:
            if autor["id"] == id_autor:
                autor.update(nuevos_datos)  # Actualiza los datos del autor
                self.guardar_datos()  # Guardar después de actualizar
                return True
        return False  # Si no se encuentra el autor, devuelve False

    def eliminar_autor(self, id_autor):
        # Eliminar un autor por ID
        for autor in self.datos["autores"]:
            if autor["id"] == id_autor:
                self.datos["autores"].remove(autor)
                self.guardar_datos()  # Guardar después de eliminar
                return True
        return False  # Si no se encuentra el autor, devuelve False









# from biblioteca.modelos.autor import Autor
# from biblioteca.utilidades.validaciones import validar_fecha

# def crear_autor(biblioteca):
#     """Crear un nuevo autor y lo añade a la Biblioteca."""

#     try:
#         print("\n- Nuevo Registro de Autor -\n")
#         nombre = input("Introduce el nombre del autor:\n")
#         apellido1 = input("Introduce el primer apellido o segundo nombre del autor:\n")
#         apellido2 = input("Introduce el segundo apellido o el apellido único del autor:\n")
#         pseudonimo = input("Introduce el pseudónimo que se le atribuye al autor(si no existe, introduce el nombre completo):\n")

#         # Tratamiento de validación de la fecha de nacimiento como objeto date()
#         nacido_str = input("Introduce la fecha de nacimiento (DD-MM-AAAA):\n")
#         nacido = validar_fecha(nacido_str)

#         if not nacido:
#             print("\nRegistro cancelado: Fecha de nacimiento inválida. Revise la información proporcionada.\n")
#             return
        
#         # Tratamiento de validación de la fecha de fallecimiento como objeto date()
#         fallecido_str = input("Introduce la fecha de fallecimiento (DD-MM-AAAA):\n")
#         fallecido = validar_fecha(fallecido_str)

#         if not fallecido:
#             print("\nRegistro cancelado: Fecha de fallecimiento inválida. Revise la información proporcionada.\n")
#             return

#         nacionalidad = input("Introduce la nacionalidad del autor:\n")

#         # Creación y registro del nuevo objeto libro
#         autor = Autor(nombre, apellido1, apellido2, pseudonimo, nacido, fallecido, nacionalidad)
#         biblioteca.agregar_autor(autor)  # Usar la instancia de biblioteca

#         print("\nAutor registrado correctamente.\n")

#     except ValueError as e:                              # Valores incorrectos al ingresar datos
#         print(f"\nError: Entrada inválida. {e}\n")
#     except Exception as e:                               # Errores imprevistos
#         print(f"\nSe produjo un error inesperado: {e}\n")

# def leer_autor(biblioteca):
#     """Busca y muestra la información de un autor por nombre o pseudónimo."""
#     try:
#         print("\n- Información del Registro deseado -\n")
#         tipo_busqueda = input("¿Deseas buscar por pseudónimo (P) o por nombre completo (N)?\n").strip().lower()
        
#         if tipo_busqueda == "p":
#             pseudonimo = input("Introduce el pseudónimo del autor:\n").strip().lower()
#             autor = biblioteca.buscar_autor_nombre(pseudonimo)
            
#             if autor:
#                 print("\nRegistro encontrado.\n")
#                 print(autor.mostrar_datos_autor())
#             else:
#                 print("\nNo se encontró ningún autor con ese pseudónimo.")
        
#         elif tipo_busqueda == "n":
#             nombre = input("Introduce el nombre del autor:\n").strip().lower()
#             apellido1 = input("Introduce el primer apellido del autor:\n").strip().lower()
#             apellido2 = input("Introduce el segundo apellido del autor (opcional):\n").strip().lower()
            
#             # Aquí se hace la búsqueda del autor por nombre completo
#             autores_encontrados = [autor for autor in biblioteca.autores if 
#                                    autor.get_nombre().lower() == nombre and
#                                    autor.get_apellido1().lower() == apellido1 and
#                                    (apellido2 == "" or autor.get_apellido2().lower() == apellido2)]
            
#             if autores_encontrados:
#                 print("\nRegistro(s) encontrado(s):")
#                 for autor in autores_encontrados:
#                     print(autor.mostrar_datos_autor())
#             else:
#                 print("\nNo se encontró ningún autor con ese nombre completo.")
        
#         else:
#             print("\nOpción no válida.")
    
#     except Exception as e:
#         print(f"Se produjo un error al buscar el autor: {e}")


# def mostrar_autores(biblioteca):
#     """Devuelve una lista completa de todos los autores existentes en la Biblioteca."""
#     if not biblioteca.autores:
#         print("\nNo hay autores registrados en la biblioteca")
#         return 
#     print(f"\n- Lista de Autores -\n")
#     for autor in biblioteca.autores:
#         print(autor.mostrar_datos_autor())
#         print()

# def actualizar_autor(biblioteca):
#     """Actualiza la información de un autor existente."""

#     try:
#         print("\n- Actualización del Registro -\n")
#         nombre = input("Introduce el nombre o pseudonimo del autor que deseas actualizar:\n")
#         autor = biblioteca.buscar_autor_nombre(nombre)

#         if autor:
#             print("\nIntroduce los nuevos datos del autor (deja en blanco para mantener la información actual:)\n")

#             nuevo_nombre = input(f"Nombre del autor[{autor.get_nombre()}] o presione ENTER si no es el dato a modificar:\n") or autor.get_nombre()
#             nuevo_apellido1 = input(f"Primer apellido o Segundo nombre del autor [{autor.get_apellido1()}] o presione ENTER si no es el dato a modificar:\n") or autor.get_apellido1()
#             nuevo_apellido2 = input(f"Segundo apellido o apellido único del autor [{autor.get_apellido2()}] o presione ENTER si no es el dato a modificar:\n") or autor.get_apellido2()
            
#             nueva_nacido = input(f"Fecha de Nacimiento del autor[{autor.get_nacido()}] o presione ENTER si no es el dato a modificar:\n") or autor.get_nacido()
#             nueva_fallecido = input(f"Fecha de Fallecimiento del autor[{autor.get_fallecido()}] o presione ENTER si no es el dato a modificar:\n") or autor.get_fallecido()
            
#             nueva_nacionalidad = input(f"Nacionalidad del autor[{autor.get_nacionalidad()}] o presione ENTER si no es el dato a modificar:\n") or autor.get_nacionalidad()
            
#             autor.set_nombre(nuevo_nombre)
#             autor.set_apellido1(nuevo_apellido1)
#             autor.set_apellido2(nuevo_apellido2)
#             autor.set_nacido(nueva_nacido)
#             autor.set_fallecido(nueva_fallecido)
#             autor.set_nacionalidad(nueva_nacionalidad)

#             print("\nAutor actualizado correctamente.\n")

#         else:
#             print("\nAutor no encontrado.\n")

#     except ValueError as e:                                                    # Valores incorrectos al ingresar datos
#         print(f"Error: Entrada inválida. {e}")

#     except Exception as e:                                                     # Errores imprevistos
#         print(f"Se produjo un error inesperado. {e}")

# def eliminar_autor(biblioteca):
#     """Elimina un libro de la biblioteca búscado por título."""

#     try:
#         print("\n- Borrado de Registro -\n")
#         nombre = input("Introduce el nombre o pseudonimo del autor que deseas borrar:\n")
        
#         autor_eliminado = None
#         for autor in biblioteca.autores:
#             if autor.get_nombre().lower() == nombre.lower():
#                 autor_eliminado = autor
#                 break # Sale del bucle una vez encontrado el titulo.

#         if autor_eliminado:
#             biblioteca.autores.remove(autor_eliminado)  # Elimina el libro de la lista
#             print("El registro ha sido eliminado correctamente.")
#             #return True   ->   # True si se elimina con éxito
#             biblioteca.reestructurar_ids_autores()  # Reestructura los ids del resto de registros después de eliminar
#         else:
#             print("No se encontró ningún registro de autor con ese nombre.\nCompruebe búsqueda e inténtelo de nuevo.")
#             #return False  ->  # False si no se encuentra el libro.
#     except Exception as e:                                                     # Errores imprevistos
#         print(f"\nSe produjo un error al intentar eliminar el autor: {e}\n")