from biblioteca.crud.crud_especifico import CRUDEspecifico
from biblioteca.repositorios.repositorio_genero import RepositorioGenero
from biblioteca.utilidades.ruta_datos_json import RUTA_DATOS_BIBLIOTECA

def submenu_especifico(biblioteca):
    """
    Submenú para gestionar tareas de subgéneros literarios específicos.
    """
    ruta_json = RUTA_DATOS_BIBLIOTECA

    # Inicializar el repositorio de géneros
    repositorio_genero = RepositorioGenero(ruta_json)

    # Inicializar CRUDEspecifico correctamente
    crud_especifico = CRUDEspecifico(ruta_json, repositorio_genero)

    while True:
        print("\n- Tareas de Subgéneros Literarios -\n")
        print("1. Mostrar Subgéneros.")
        print("2. Añadir Subgénero.")
        print("3. Actualizar Subgénero.")
        print("4. Eliminar Subgénero.")
        print("5. Mostrar Subgéneros por Género.")
        print("0. Volver al Menú Principal.")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            # Mostrar subgéneros
            crud_especifico.mostrar_especificos()

        elif opcion == "2":
            # Añadir un subgénero
            genero_nombre = input("Introduce el nombre del Género Literario asociado: ").strip()
            nombre_especifico = input("Introduce el nombre del Subgénero Literario: ").strip()
            tipo = input("Introduce el tipo (opcional): ").strip()

            try:
                # Intentar agregar el subgénero y asociar el género
                crud_especifico.agregar_especifico(genero_nombre, nombre_especifico, tipo)
                print("Subgénero Literario agregado correctamente.")
            except Exception as e:
                print(f"Error al agregar el Subgénero Literario: {e}")

        elif opcion == "3":
            # Actualizar un subgénero
            crud_especifico.actualizar_especifico(biblioteca)

        elif opcion == "4":
            # Eliminar un subgénero
            crud_especifico.eliminar_especifico(biblioteca)

        elif opcion == "5":
            # Mostrar subgéneros por género
            genero_id = input("Introduce el ID del género: ").strip()
            subgeneros = crud_especifico.obtener_especificos_por_genero(genero_id)

            if subgeneros:
                print("\n=== Subgéneros por Género ===")
                for especifico in subgeneros:
                    print(
                        f"ID: {especifico['especifico_id']} | Subgénero Literario: {especifico['nombre_especifico']} | "
                        f"Tipo: {especifico['tipo']} | Género Literario Asociado: {especifico['nombre_genero']}"
                    )
            else:
                print(f"No se encontraron subgéneros específicos para el género con ID {genero_id}.")

        elif opcion == "0":
            # Volver al menú principal
            print("Regresando al Menú Principal...")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
