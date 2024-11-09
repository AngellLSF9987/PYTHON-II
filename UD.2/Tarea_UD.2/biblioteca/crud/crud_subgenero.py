# biblioteca/crud/crud_genero.py

from ..modelos.generos.subgenero import Subgenero

def crear_subgenero(biblioteca):
    """Crear un nuevo género literario y lo añade a la Biblioteca."""

    try:
        print("\n- Nuevo Registro de Género Literario -\n")
        nombre = input("Introduce el nombre:\n")

        # Creación y registro del nuevo objeto subgenero
        subgenero = Subgenero(nombre)
        biblioteca.agregar_subgenero(subgenero)  # Usar la instancia de biblioteca

        print("\nSubgénero Literario registrado correctamente.\n")

    except ValueError as e:                              # Valores incorrectos al ingresar datos
        print(f"\nError: Entrada inválida. {e}\n")
    except Exception as e2:                               # Errores imprevistos
        print(f"\nSe produjo un error inesperado: {e}\n")

def leer_subgenero(biblioteca):
    """Busca y muestra la información de un subgenero por nombre."""

    try:
        print("\n- Información del Registro deseado -\n")
        nombre = input("Introduzca el nombre del subgénero literario a buscar:\n")
        subgenero = biblioteca.buscar_subgenero_nombre(nombre)

        if subgenero:
            print("\nRegistro encontrado.\n")
            print(subgenero.mostrar_datos_subgenero())
        else:
            print("\nSubgénero Literario no encontrado. Revise la información proporcionada e inténtelo de nuevo.\n")

    except Exception as e:                                         # Errores imprevistos
        print(f"Se produjo un error al buscar el libro: {e}")

def actualizar_subgenero(biblioteca):
    """Actualiza la información de un subgénero literario existente."""

    try:
        print("\n- Actualización del Registro -\n")
        nombre = input("Introduce el nombre del subgénero literario que deseas actualizar:\n")
        subgenero = biblioteca.buscar_subgenero_nombre(nombre)

        if subgenero:
            print("\nIntroduce los nuevos datos del subgénero literario (deja en blanco para mantener la información actual:)\n")

            nuevo_nombre = input(f"Nombre [{subgenero.get_nombre()}]: ") or subgenero.get_nombre()

            subgenero.set_nombre(nuevo_nombre)

            print("\nSubgénero Literario actualizado correctamente.\n")

        else:
            print("\nSubgénero Literario no encontrado.\n")

    except ValueError as e:                                                    # Valores incorrectos al ingresar datos
        print(f"Error: Entrada inválida. {e}")

    except Exception as e:                                                     # Errores imprevistos
        print(f"Se produjo un error inesperado. {e}")

def eliminar_subgenero(biblioteca):
    """Elimina un subgénero literario de la biblioteca búscado por nombre."""

    try:
        print("\n- Borrado de Registro -\n")
        nombre = input("Introduce el nombre del subgénero literario que deseas borrar:\n")
        
        subgenero_eliminado = None
        for subgenero in biblioteca.subgeneros:
            if subgenero.get_nombre().lower() == nombre.lower():
                subgenero_eliminado = subgenero
                break # Sale del bucle una vez encontrado el titulo.

        if subgenero_eliminado:
            biblioteca.generos.remove(subgenero_eliminado)  # Elimina el subgénero literario de la lista
            print("El registro ha sido eliminado correctamente.")
            #return True   ->   # True si se elimina con éxito
            biblioteca.reestructurar_ids_subgeneros()  # Reestructura los ids del resto de registros después de eliminar
        else:
            print("No se encontró ningún registro con ese nombre.\nCompruebe búsqueda e inténtelo de nuevo.")
            #return False  ->  # False si no se encuentra el subgénero.
    except Exception as e:                                                     # Errores imprevistos
        print(f"\nSe produjo un error al intentar eliminar el subgénero literario: {e}\n")