# biblioteca/crud/crud_subgenero.py

from biblioteca.modelos.generos.especifico import Especifico

def crear_especifico(biblioteca):
    """Crear un nuevo subgénero literario y lo añade a la Biblioteca."""

    try:
        print("\n- Nuevo Registro de SubGénero Literario -\n")
        nombre_especifico = input("Introduce el nombre:\n")

        # Creación y registro del nuevo objeto subgenero
        especifico = Especifico(nombre_especifico)
        biblioteca.agregar_especifico(especifico)  # Usar la instancia de biblioteca

        print("\nSubgénero Literario registrado correctamente.\n")

    except ValueError as e:                              # Valores incorrectos al ingresar datos
        print(f"\nError: Entrada inválida. {e}\n")
    except Exception as e2:                               # Errores imprevistos
        print(f"\nSe produjo un error inesperado: {e}\n")

def leer_especifico(biblioteca):
    """Busca y muestra la información de un subgenero por nombre."""

    try:
        print("\n- Información del Registro deseado -\n")
        nombre_especifico = input("Introduzca el nombre del subgénero literario a buscar:\n")
        especifico = biblioteca.buscar_especifico_nombre(nombre_especifico)

        if especifico:
            print("\nRegistro encontrado.\n")
            print(especifico.mostrar_datos_especifico())
        else:
            print("\nSubgénero Literario no encontrado. Revise la información proporcionada e inténtelo de nuevo.\n")

    except Exception as e:                                         # Errores imprevistos
        print(f"Se produjo un error al buscar el libro: {e}")


def mostrar_especificos(biblioteca):
    """Devuelve una lista completa de todos los géneros literarios existentes en la Biblioteca."""
    if not biblioteca.especificos:
        print("\nNo hay subgéneros literarios registrados en la biblioteca")
        return 
    print(f"\n- Lista de Subgéneros Literarios -\n")
    for especifico in biblioteca.especificos:
        print(especifico.mostrar_datos_especifico())
        print()

def actualizar_especifico(biblioteca):
    """Actualiza la información de un subgénero literario existente."""

    try:
        print("\n- Actualización del Registro -\n")
        nombre_especifico = input("Introduce el nombre del subgénero literario que deseas actualizar:\n")
        especifico = biblioteca.buscar_especifico_nombre(nombre_especifico)

        if especifico:
            print("\nIntroduce los nuevos datos del subgénero literario (deja en blanco para mantener la información actual:)\n")

            nuevo_nombre_especifico = input(f"Nombre [{especifico.get_nombre_especifico()}]: ") or especifico.get_nombre_especifico()

            especifico.set_nombre_especifico(nuevo_nombre_especifico)

            print("\nSubgénero Literario actualizado correctamente.\n")

        else:
            print("\nSubgénero Literario no encontrado.\n")

    except ValueError as e:                                                    # Valores incorrectos al ingresar datos
        print(f"Error: Entrada inválida. {e}")

    except Exception as e:                                                     # Errores imprevistos
        print(f"Se produjo un error inesperado. {e}")

def eliminar_especifico(biblioteca):
    """Elimina un subgénero literario de la biblioteca búscado por nombre."""

    try:
        print("\n- Borrado de Registro -\n")
        nombre_especifico = input("Introduce el nombre del subgénero literario que deseas borrar:\n")
        
        especifico_eliminado = None
        for especifico in biblioteca.especificos:
            if especifico.get_nombre_especifico().lower() == nombre_especifico.lower():
                especifico_eliminado = especifico
                break # Sale del bucle una vez encontrado el titulo.

        if especifico_eliminado:
            biblioteca.especificos.remove(especifico_eliminado)  # Elimina el subgénero literario de la lista
            print("El registro ha sido eliminado correctamente.")
            #return True   ->   # True si se elimina con éxito
            biblioteca.reestructurar_ids_especificos()  # Reestructura los ids del resto de registros después de eliminar
        else:
            print("No se encontró ningún registro con ese nombre.\nCompruebe búsqueda e inténtelo de nuevo.")
            #return False  ->  # False si no se encuentra el subgénero.
    except Exception as e:                                                     # Errores imprevistos
        print(f"\nSe produjo un error al intentar eliminar el subgénero literario: {e}\n")