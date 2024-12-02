from biblioteca.repositorios.repositorio_autor import RepositorioAutor
from biblioteca.repositorios.repositorio_especifico import RepositorioEspecifico
from biblioteca.repositorios.repositorio_genero import RepositorioGenero
from biblioteca.utilidades.ruta_datos_json import RUTA_DATOS_BIBLIOTECA
from biblioteca.crud.crud_libro import CRUDLibro
from biblioteca.utilidades.validaciones import validar_autor, validar_genero, validar_especifico

def submenu_libro(biblioteca):
    # Inicializar los repositorios necesarios
    ruta_json = RUTA_DATOS_BIBLIOTECA
    repositorio_autor = RepositorioAutor(ruta_json)
    repositorio_especifico = RepositorioEspecifico(ruta_json)
    repositorio_genero = RepositorioGenero(ruta_json)

    # Crear instancia de CRUDLibro pasando los repositorios
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

        opcion = input("\nSelecciona una opción:\n").strip()

        if opcion == "1":
            crud_libro.mostrar_libros()

        elif opcion == "2":
            # Validar la existencia del autor
            autor = validar_autor(biblioteca)
            if not autor:
                print("⚠️ Error al validar el autor. Intenta nuevamente.")
                continue

            # Validar la existencia del género
            genero = validar_genero(biblioteca)
            if not genero:
                print("⚠️ Error al validar el género. Intenta nuevamente.")
                continue

            # Validar la existencia del subgénero
            especifico = validar_especifico(biblioteca)
            if not especifico:
                print("⚠️ Error al validar el subgénero. Intenta nuevamente.")
                continue

            # Recopilar otros datos del libro
            titulo = input("Introduce el título del libro: ").strip()
            fecha_publicacion = input("Introduce la fecha de publicación (AAAA-MM-DD): ").strip()
            num_paginas = input("Introduce el número de páginas: ").strip()

            # Crear el libro
            nuevo_libro = {
                "libro_id": len(biblioteca.repositorio_libro.obtener_libros()) + 1,  # Generar ID automáticamente
                "titulo": titulo,
                "genero_id": genero["genero_id"], # Utiliza el ID del subgénero validado
                "especifico_id": especifico["especifico_id"],  # Utiliza el ID del subgénero validado
                "fecha_publicacion": fecha_publicacion,
                "num_paginas": num_paginas,
                "autor_id": autor  # Utiliza el ID del autor validado
            }
            biblioteca.repositorio_libro.agregar_libro(nuevo_libro)
            print(f"Libro '{titulo}' añadido exitosamente.")

        elif opcion == "3":
            crud_libro.buscar_libro_por_titulo(biblioteca)

        elif opcion == "4":
            libro_id = input("Introduce el ID del libro a modificar: ").strip()
            nuevos_datos = {}

            libro = crud_libro.buscar_libro_por_id(libro_id)
            if libro:
                print(f"Libro encontrado: {libro['titulo']}")
                titulo = input(f"Nuevo título (actual: {libro['titulo']}): ").strip()
                if titulo:
                    nuevos_datos["titulo"] = titulo

                autor = validar_autor(biblioteca)
                if autor:
                    nuevos_datos["autor_id"] = autor.get_id()

                subgenero = validar_especifico(biblioteca)
                if subgenero:
                    nuevos_datos["especifico_id"] = subgenero.get_id()

                fecha_publicacion = input(f"Nueva fecha de publicación (actual: {libro['fecha_publicacion']}): ").strip()
                if fecha_publicacion:
                    nuevos_datos["fecha_publicacion"] = fecha_publicacion

                num_paginas = input(f"Nuevo número de páginas (actual: {libro['num_paginas']}): ").strip()
                if num_paginas:
                    nuevos_datos["num_paginas"] = num_paginas

                if crud_libro.actualizar_libro(libro_id, nuevos_datos):
                    print(f"✅ Libro con ID {libro_id} actualizado exitosamente.")
                else:
                    print("⚠️ No se pudo actualizar el libro.")
            else:
                print(f"⚠️ No se encontró un libro con ID {libro_id}.")

        elif opcion == "5":
            libro_id = input("Introduce el ID del libro a eliminar: ").strip()
            if crud_libro.eliminar_libro(libro_id):
                print(f"✅ Libro con ID {libro_id} eliminado exitosamente.")
            else:
                print(f"⚠️ No se encontró un libro con ID {libro_id}.")

        elif opcion == "0":
            return  # Volver al Menú de Biblioteca

        else:
            print("\n⚠️ Opción no válida. Intenta de nuevo.\n")
