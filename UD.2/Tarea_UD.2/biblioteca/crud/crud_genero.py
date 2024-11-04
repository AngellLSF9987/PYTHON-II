# biblioteca/crud/crud_genero.py

from ..modelos.genero import Genero
from ..utilidades.validaciones import validar_fecha

def crear_genero(biblioteca):
    """Crear un nuevo género literario y lo añade a la Biblioteca."""

    try:
        print("\n- Nuevo Registro de Género Literario -\n")
        nombre = input("Introduce el nombre:\n")

        # Creación y registro del nuevo objeto libro
        genero = Genero(nombre)
        biblioteca.agregar_genero(genero)  # Usar la instancia de biblioteca

        print("\nGénero Literario registrado correctamente.\n")

    except ValueError as e:                              # Valores incorrectos al ingresar datos
        print(f"\nError: Entrada inválida. {e}\n")
    except Exception as e2:                               # Errores imprevistos
        print(f"\nSe produjo un error inesperado: {e}\n")

def leer_libro(biblioteca):
    """Busca y muestra la información de un libro por título."""

    try:
        print("\n- Información del Registro deseado -\n")
        nombre = input("Introduzca el título del libro a buscar:\n")
        genero = biblioteca.buscar_genero(nombre)

        if genero:
            print("\nRegistro encontrado.\n")
            print(genero.mostrar_datos())
        else:
            print("\nGénero Literario no encontrado. Revise la información proporcionada e inténtelo de nuevo.\n")

    except Exception as e:                                         # Errores imprevistos
        print(f"Se produjo un error al buscar el libro: {e}")

def actualizar_genero(biblioteca):
    """Actualiza la información de un género literario existente."""

    try:
        print("\n- Actualización del Registro -\n")
        nombre = input("Introduce el nombre del género literario que deseas actualizar:\n")
        genero = biblioteca.buscar_nombre(nombre)

        if genero:
            print("\nIntroduce los nuevos datos del género literario (deja en blanco para mantener la información actual:)\n")

            nuevo_nombre = input(f"Nombre [{genero.get_nombre()}]: ") or genero.get_nombre()

            genero.set_titulo(nuevo_nombre)

            print("\nGénero Literario actualizado correctamente.\n")

        else:
            print("\nGénero Literario no encontrado.\n")

    except ValueError as e:                                                    # Valores incorrectos al ingresar datos
        print(f"Error: Entrada inválida. {e}")

    except Exception as e:                                                     # Errores imprevistos
        print(f"Se produjo un error inesperado. {e}")

def eliminar_genero(biblioteca):
    """Elimina un género literario de la biblioteca búscado por nombre."""

    try:
        print("\n- Borrado de Registro -\n")
        nombre = input("Introduce el nombre del género literario que deseas borrar:\n")
        
        genero_eliminado = None
        for genero in biblioteca.generos:
            if genero.get_titulo().lower() == genero.lower():
                genero_eliminado = genero
                break # Sale del bucle una vez encontrado el titulo.

        if genero_eliminado:
            biblioteca.generos.remove(genero_eliminado)  # Elimina el género literario de la lista
            print("El registro ha sido eliminado correctamente.")
            #return True   ->   # True si se elimina con éxito
            biblioteca.reestructurar_ids()  # Reestructura los ids del resto de registros después de eliminar
        else:
            print("No se encontró ningún registro con ese nombre.\nCompruebe búsqueda e inténtelo de nuevo.")
            #return False  ->  # False si no se encuentra el libro.
    except Exception as e:                                                     # Errores imprevistos
        print(f"\nSe produjo un error al intentar eliminar el género literario: {e}\n")