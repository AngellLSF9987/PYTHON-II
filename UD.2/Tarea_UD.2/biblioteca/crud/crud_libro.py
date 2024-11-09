# biblioteca/crud/crud_libro.py

from biblioteca.modelos.libro import Libro
from biblioteca.utilidades.validaciones import validar_fecha

def crear_libro(biblioteca):
    """Crear un nuevo libro y lo añade a la Biblioteca."""

    try:
        print("\n- Nuevo Registro de Libro -\n")
        titulo = input("Introduce el titulo:\n")
        autor = input("Introduce el autor:\n")

        # Tratamiento de validación de la fecha de publicación como objeto date()
        fecha_publicacion_str = input("Introduce la fecha de publicación (DD-MM-AAAA):\n")
        fecha_publicacion = validar_fecha(fecha_publicacion_str)

        if not fecha_publicacion:
            print("\nRegistro cancelado: Fecha de publicación inválida. Revise la información proporcionada.\n")
            return
        
        num_paginas = int(input("\nIntroduce el numero de paginas:\n"))

        # Creación y registro del nuevo objeto libro
        libro = Libro(titulo,autor,fecha_publicacion,num_paginas)
        biblioteca.agregar_libro(libro)  # Usar la instancia de biblioteca

        print("\nLibro registrado correctamente.\n")

    except ValueError as e:                              # Valores incorrectos al ingresar datos
        print(f"\nError: Entrada inválida. {e}\n")
    except Exception as e2:                               # Errores imprevistos
        print(f"\nSe produjo un error inesperado: {e}\n")

def leer_libro(biblioteca):
    """Busca y muestra la información de un libro por título."""

    try:
        print("\n- Información del Registro deseado -\n")
        titulo = input("Introduzca el título del libro a buscar:\n")
        libro = biblioteca.buscar_libro_titulo(titulo)

        if libro:
            print("\nRegistro encontrado.\n")
            print(libro.mostrar_datos())
        else:
            print("\nTítulo no encontrado. Revise la información proporcionada e inténtelo de nuevo.\n")

    except Exception as e:                                         # Errores imprevistos
        print(f"Se produjo un error al buscar el libro: {e}")

def actualizar_libro(biblioteca):
    """Actualiza la información de un libro existente."""

    try:
        print("\n- Actualización del Registro -\n")
        titulo = input("Introduce el título del libro que deseas actualizar:\n")
        libro = biblioteca.buscar_libro_titulo(titulo)

        if libro:
            print("\nIntroduce los nuevos datos del libro (deja en blanco para mantener la información actual:)\n")

            nuevo_titulo = input(f"Título [{libro.get_titulo()}]: ") or libro.get_titulo()
            nuevo_autor = input(f"Autor [{libro.get_autor()}]: ") or libro.get_autor()
            nueva_fecha_publicacion = input(f"Fecha de Publicación [{libro.get_fecha_publicacion()}]: ") or libro.get_fecha_publicacion()
            nueva_num_paginas = input(f"Nº de Páginas[{libro.get_num_paginas()}]: ") or libro.get_num_paginas()
            
            libro.set_titulo(nuevo_titulo)
            libro.set_autor(nuevo_autor)
            libro.set_fecha_publicacion(nueva_fecha_publicacion)

            if nueva_num_paginas:
                libro.set_num_paginas(int(nueva_num_paginas))

            print("\nLibro actualizado correctamente.\n")

        else:
            print("\nLibro no encontrado.\n")

    except ValueError as e:                                                    # Valores incorrectos al ingresar datos
        print(f"Error: Entrada inválida. {e}")

    except Exception as e:                                                     # Errores imprevistos
        print(f"Se produjo un error inesperado. {e}")

def eliminar_libro(biblioteca):
    """Elimina un libro de la biblioteca búscado por título."""

    try:
        print("\n- Borrado de Registro -\n")
        titulo = input("Introduce el título del libro que deseas borrar:\n")
        
        libro_eliminado = None
        for libro in biblioteca.libros:
            if libro.get_titulo().lower() == titulo.lower():
                libro_eliminado = libro
                break # Sale del bucle una vez encontrado el titulo.

        if libro_eliminado:
            biblioteca.libros.remove(libro_eliminado)  # Elimina el libro de la lista
            print("El registro ha sido eliminado correctamente.")
            #return True   ->   # True si se elimina con éxito
            biblioteca.reestructurar_ids_libros()  # Reestructura los ids del resto de registros después de eliminar
        else:
            print("No se encontró ningún registro con ese título.\nCompruebe búsqueda e inténtelo de nuevo.")
            #return False  ->  # False si no se encuentra el libro.
    except Exception as e:                                                     # Errores imprevistos
        print(f"\nSe produjo un error al intentar eliminar el libro: {e}\n")