from biblioteca.repositorios.repositorio_autor import RepositorioAutor
from biblioteca.repositorios.repositorio_especifico import RepositorioEspecifico
from biblioteca.repositorios.repositorio_genero import RepositorioGenero
from biblioteca.utilidades.ruta_datos_json import RUTA_DATOS_BIBLIOTECA
from biblioteca.crud.crud_libro import CRUDLibro

def submenu_libro(biblioteca):
    # Inicializar los repositorios necesarios
    ruta_json = RUTA_DATOS_BIBLIOTECA
    repositorio_autor = RepositorioAutor(ruta_json)
    repositorio_especifico = RepositorioEspecifico(ruta_json)
    repositorio_genero = RepositorioGenero(ruta_json)

    # Crea la instancia de CRUDLibro pasando todos los repositorios
    crud_libro = CRUDLibro(
        biblioteca.ruta_json,
        repositorio_autor,
        repositorio_especifico,
        repositorio_genero
    )
    
    while True:
        print("\n- Tareas de Libros -\n")
        print("1. Mostrar Libros.")
        print("2. Añadir Libro.")
        print("3. Buscar Libro por Título.")
        print("4. Modificar Datos Libro.")
        print("5. Eliminar Libro.")
        print("0. Menú Tareas de Biblioteca.")

        opcion = input("\nSelecciona una opción:\n")
        
        if opcion == "1":
            crud_libro.mostrar_libros_crud(biblioteca)

        elif opcion == "2":
            # Añadir un libro
            titulo = input("Introduce el título del libro: ").strip()
            autor_id = input("Introduce el ID del autor: ").strip()
            especifico_id = input("Introduce el ID del subgénero: ").strip()
            fecha_publicacion = input("Introduce la fecha de publicación (AAAA-MM-DD): ").strip()
            num_paginas = input("Introduce el número de páginas: ").strip()

            libro = {
                "titulo": titulo,
                "autor_id": autor_id,
                "especifico_id": especifico_id,
                "fecha_publicacion": fecha_publicacion,
                "num_paginas": num_paginas,
                "nombre_genero": "Desconocido",  # Esto podría ser más dinámico según la relación con géneros
            }

            crud_libro.agregar_libro(libro)
            print(f"Libro '{titulo}' agregado exitosamente.")

        elif opcion == "3":
            # Buscar un libro por título
            titulo_buscar = input("Introduce el título del libro a buscar: ").strip()
            libro_encontrado = None

            # Buscar libro por título
            for libro in crud_libro.datos["libros"]:
                if libro["titulo"].lower() == titulo_buscar.lower():
                    libro_encontrado = libro
                    break

            if libro_encontrado:
                print("\n=== Libro Encontrado ===")
                print(
                    f"ID: {libro_encontrado['libro_id']} | Título: {libro_encontrado['titulo']} | "
                    f"Autor: {libro_encontrado['autor_id']} | Género: {libro_encontrado['nombre_genero']} | "
                    f"Subgénero: {libro_encontrado['especifico_id']} | Fecha de Publicación: {libro_encontrado['fecha_publicacion']} | "
                    f"Núm. Páginas: {libro_encontrado['num_paginas']}"
                )
            else:
                print(f"No se encontró ningún libro con el título '{titulo_buscar}'.")

        elif opcion == "4":
            # Modificar los datos de un libro
            libro_id = input("Introduce el ID del libro a modificar: ").strip()
            nuevos_datos = {}

            # Buscar el libro por ID
            libro = crud_libro.buscar_libro_por_id(libro_id)
            if libro:
                print(f"Libro encontrado: {libro['titulo']}")
                titulo = input(f"Nuevo título (actual: {libro['titulo']}): ").strip()
                if titulo:
                    nuevos_datos["titulo"] = titulo
                autor_id = input(f"Nuevo ID del autor (actual: {libro['autor_id']}): ").strip()
                if autor_id:
                    nuevos_datos["autor_id"] = autor_id
                especifico_id = input(f"Nuevo ID del subgénero (actual: {libro['especifico_id']}): ").strip()
                if especifico_id:
                    nuevos_datos["especifico_id"] = especifico_id
                fecha_publicacion = input(f"Nueva fecha de publicación (actual: {libro['fecha_publicacion']}): ").strip()
                if fecha_publicacion:
                    nuevos_datos["fecha_publicacion"] = fecha_publicacion
                num_paginas = input(f"Nuevo número de páginas (actual: {libro['num_paginas']}): ").strip()
                if num_paginas:
                    nuevos_datos["num_paginas"] = num_paginas

                if crud_libro.actualizar_libro(libro_id, nuevos_datos):
                    print(f"Libro con ID {libro_id} actualizado exitosamente.")
                else:
                    print("No se pudo actualizar el libro.")
            else:
                print(f"No se encontró un libro con ID {libro_id}.")

        elif opcion == "5":
            # Eliminar un libro
            libro_id = input("Introduce el ID del libro a eliminar: ").strip()
            if crud_libro.eliminar_libro(libro_id):
                print(f"Libro con ID {libro_id} eliminado exitosamente.")
            else:
                print(f"No se encontró un libro con ID {libro_id}.")

        elif opcion == "0":
            return  # Volver SubMenú Tareas de Biblioteca

        else:
            print("\nOpción no válida.\n")
