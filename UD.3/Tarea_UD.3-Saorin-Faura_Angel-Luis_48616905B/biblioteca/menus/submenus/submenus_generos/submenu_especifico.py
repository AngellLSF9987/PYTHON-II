from biblioteca.crud.crud_genero import CRUDGenero
from biblioteca.repositorios.repositorio_genero import RepositorioGenero
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
            crud_especifico.mostrar_especificos_crud(biblioteca)

        elif opcion == "2":
            # Añadir un subgénero
            nombre_especifico = input("Introduce el nombre del subgénero: ").strip()
            tipo = input("Introduce el tipo del subgénero: ").strip()
            genero_id = input("Introduce el nombre del género asociado: ").strip()

            # Buscar si el género existe
            genero = repositorio_genero.buscar_genero_por_nombre(genero_id)  # Buscar por nombre

            if not genero:
                print(f"No se encontró el género '{genero_id}'. ¿Deseas crearlo? (s/n): ", end="")
                respuesta = input().strip().lower()
                if respuesta == "s":
                    # Si el género no existe, lo creamos
                    nuevo_genero = {
                        "genero_id": genero_id,  # Asignar un ID de género único
                        "nombre_genero": genero_id
                    }
                    repositorio_genero.agregar_genero(nuevo_genero)
                    print(f"Género '{genero_id}' agregado con éxito.")
                    genero = nuevo_genero
                else:
                    print("No se ha creado el género.")
                    continue  # Volver al menú si no se desea crear el género

            # Crear el subgénero
            especifico_id = str(len(biblioteca.repositorio_especifico.obtener_especificos()) + 1)  # ID auto-incremental
            subgenero = {
                "especifico_id": especifico_id,
                "genero_id": genero['genero_id'],  # Usamos el ID del género
                "nombre_especifico": nombre_especifico,
                "tipo": tipo,  # O cualquier valor predeterminado
            }

            # Agregar el subgénero
            crud_especifico.agregar_especifico(subgenero)
            biblioteca.guardar_datos_biblioteca()  # Guardar datos después de la operación

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
                        f"ID: {especifico['especifico_id']} | Subgénero: {especifico['nombre_especifico']} | "
                        f"Tipo: {especifico['tipo']} | Género Asociado: {especifico['nombre_genero']}"
                    )
            else:
                print(f"No se encontraron subgéneros específicos para el género con ID {genero_id}.")

        elif opcion == "0":
            # Volver al menú principal
            print("Regresando al Menú Principal...")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
