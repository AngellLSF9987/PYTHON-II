# biblioteca/crud/crud_autor.py

from ..modelos.autor import Autor
from ..utilidades.validaciones import validar_fecha

def crear_autor(biblioteca):
    """Crear un nuevo autor y lo añade a la Biblioteca."""

    try:
        print("\n- Nuevo Registro de Autor -\n")
        nombre = input("Introduce el nombre:\n")
        apellido = input("Introduce el apellido:\n")

        # Tratamiento de validación de la fecha de nacimiento como objeto date()
        nacido_str = input("Introduce la fecha de nacimiento (DD-MM-AAAA):\n")
        nacido = validar_fecha(nacido_str)

        if not nacido:
            print("\nRegistro cancelado: Fecha de nacimiento inválida. Revise la información proporcionada.\n")
            return
        
        # Tratamiento de validación de la fecha de fallecimiento como objeto date()
        fallecido_str = input("Introduce la fecha de fallecimiento (DD-MM-AAAA):\n")
        fallecido = validar_fecha(fallecido_str)

        if not fallecido:
            print("\nRegistro cancelado: Fecha de fallecimiento inválida. Revise la información proporcionada.\n")
            return

        nacionalidad = input("Introduce el apellido:\n")

        # Creación y registro del nuevo objeto libro
        autor = Autor(nombre, apellido, nacido, fallecido, nacionalidad)
        biblioteca.agregar_autor(autor)  # Usar la instancia de biblioteca

        print("\nAutor registrado correctamente.\n")

    except ValueError as e:                              # Valores incorrectos al ingresar datos
        print(f"\nError: Entrada inválida. {e}\n")
    except Exception as e2:                               # Errores imprevistos
        print(f"\nSe produjo un error inesperado: {e}\n")

def leer_autor(biblioteca):
    """Busca y muestra la información de un autor por nombre."""

    try:
        print("\n- Información del Registro deseado -\n")
        nombre = input("Introduzca el nombre del autor a buscar:\n")
        autor = biblioteca.buscar_autor_nombre(nombre)

        if autor:
            print("\nRegistro encontrado.\n")
            print(autor.mostrar_datos_autor())
        else:
            print("\nAutor no encontrado. Revise la información proporcionada e inténtelo de nuevo.\n")

    except Exception as e:                                         # Errores imprevistos
        print(f"Se produjo un error al buscar el libro: {e}")

def actualizar_autor(biblioteca):
    """Actualiza la información de un autor existente."""

    try:
        print("\n- Actualización del Registro -\n")
        nombre = input("Introduce el nombre del autor que deseas actualizar:\n")
        autor = biblioteca.buscar_autor_nombre(nombre)

        if autor:
            print("\nIntroduce los nuevos datos del autor (deja en blanco para mantener la información actual:)\n")

            nuevo_nombre = input(f"Nombre [{autor.get_nombre()}]: ") or autor.get_nombre()
            nuevo_apellido = input(f"Apellido [{autor.get_apellido()()}]: ") or autor.get_apellido()
            
            nueva_nacido = input(f"Fecha de Nacimiento [{autor.get_nacido}]: ") or autor.get_nacido()
            nueva_fallecido = input(f"Nº de Páginas[{autor.get_fallecido()}]: ") or autor.get_fallecido()
            
            nueva_nacionalidad = input(f"Nacionalidad [{autor.get_nacionalidad()}]: ") or autor.get_nacionalidad()
            
            autor.set_nombre(nuevo_nombre)
            autor.set_apellido(nuevo_apellido)
            autor.set_nacido(nueva_nacido)
            autor.set_fallecido(nueva_fallecido)
            autor.set_nacionalidad(nueva_nacionalidad)

            print("\nAutor actualizado correctamente.\n")

        else:
            print("\nAutor no encontrado.\n")

    except ValueError as e:                                                    # Valores incorrectos al ingresar datos
        print(f"Error: Entrada inválida. {e}")

    except Exception as e:                                                     # Errores imprevistos
        print(f"Se produjo un error inesperado. {e}")

def eliminar_autor(biblioteca):
    """Elimina un libro de la biblioteca búscado por título."""

    try:
        print("\n- Borrado de Registro -\n")
        nombre = input("Introduce el nombre del autor que deseas borrar:\n")
        
        autor_eliminado = None
        for autor in biblioteca.autores:
            if autor.get_nombre().lower() == nombre.lower():
                autor_eliminado = autor
                break # Sale del bucle una vez encontrado el titulo.

        if autor_eliminado:
            biblioteca.autores.remove(autor_eliminado)  # Elimina el libro de la lista
            print("El registro ha sido eliminado correctamente.")
            #return True   ->   # True si se elimina con éxito
            biblioteca.reestructurar_ids_autores()  # Reestructura los ids del resto de registros después de eliminar
        else:
            print("No se encontró ningún registro de autor con ese nombre.\nCompruebe búsqueda e inténtelo de nuevo.")
            #return False  ->  # False si no se encuentra el libro.
    except Exception as e:                                                     # Errores imprevistos
        print(f"\nSe produjo un error al intentar eliminar el autor: {e}\n")