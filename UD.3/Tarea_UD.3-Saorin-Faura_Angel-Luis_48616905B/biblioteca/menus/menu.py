from biblioteca.modelos.biblioteca import Biblioteca
from biblioteca.menus.submenus import submenu_tareas


def menu():
    """
    Función principal del menú de la Biblioteca.
    Permite interactuar con las funcionalidades principales del sistema.
    """
    # Inicializa la Biblioteca
    biblioteca = Biblioteca()

    while True:
        print("\n- Bienvenid@ a Biblioteca AVANZA! -\n")
        print("1. Menú Tareas de Biblioteca.")
        print("2. Buscar Libro por Título.")
        print("3. Buscar Autor por Nombre Completo o Pseudónimo.")
        print("4. Mostrar Todos los Libros.")
        print("5. Mostrar Todos los Autores.")
        print("6. Mostrar Todos los Géneros Literarios.")
        print("7. Mostrar Todos los Subgéneros Literarios Específicos.")
        print("0. Salir")

        opcion = input("\nElija una opción:\n")

        if opcion == "1":
            # Llama al submenu de tareas y le pasa la instancia de Biblioteca
            submenu_tareas.submenu_tareas(biblioteca)

        elif opcion == "2":
            buscar_libro_por_titulo(biblioteca)

        elif opcion == "3":
            buscar_autor_por_nombre_o_pseudonimo(biblioteca)

        elif opcion == "4":
            mostrar_todos_los_libros(biblioteca)

        elif opcion == "5":
            mostrar_todos_los_autores(biblioteca)

        elif opcion == "6":
            mostrar_todos_los_generos(biblioteca)

        elif opcion == "7":
            mostrar_todos_los_subgeneros(biblioteca)

        elif opcion == "0":
            print("\n¡Hasta luego! Gracias por usar Biblioteca AVANZA.\n")
            break

        else:
            print("\n⚠️ Opción no válida. Por favor, elija una opción válida.\n")

def buscar_libro_por_titulo(biblioteca):
    """
    Permite buscar un libro por su título y muestra el autor y género.
    """
    titulo = input("\nIngrese el título del libro que desea buscar:\n").strip()
    libros = biblioteca.repositorio_libro.libros
    resultados = [libro for libro in libros if titulo.lower() in libro["titulo"].lower()]

    if resultados:
        print("\n=== Resultados de la búsqueda ===")
        for libro in resultados:
            autor = biblioteca.repositorio_autor.obtener_autor_por_id(libro["autor_id"])
            especifico = biblioteca.repositorio_especifico.obtener_especifico_por_id(libro["especifico_id"])
            genero_nombre = especifico["nombre_especifico"] if especifico else "Desconocido"
            autor_nombre = autor["nombre"] if autor else "Desconocido"

            print(
                f"ID: {libro['libro_id']}\n"
                f"Título: {libro['titulo']}\n"
                f"Género: {genero_nombre}\n"
                f"Fecha de Publicación: {libro['fecha_publicacion']}\n"
                f"Autor: {autor_nombre}\n"
            )
    else:
        print("\nNo se encontraron libros con ese título.")

def buscar_autor_por_nombre_o_pseudonimo(biblioteca):
    """
    Permite buscar un autor por su nombre completo o pseudónimo.
    """
    criterio = input("\nIngrese el nombre completo o pseudónimo del autor que desea buscar:\n").strip()
    autores = biblioteca.repositorio_autor.autores
    resultados = [
        autor for autor in autores if 
        criterio.lower() in autor["nombre"].lower() or
        criterio.lower() in autor["pseudonimo"].lower()
    ]

    if resultados:
        print("\n=== Resultados de la búsqueda ===")
        for autor in resultados:
            print(
                f"ID: {autor['autor_id']}\nNombre: {autor['nombre']}\n"
                f"Pseudónimo: {autor['pseudonimo']}\n"
                f"Nacionalidad: {autor.get('nacionalidad', 'Desconocida')}\n"
            )
    else:
        print("\nNo se encontraron autores con ese criterio.")

def mostrar_todos_los_libros(biblioteca):
    """
    Muestra todos los libros registrados en la biblioteca.
    """
    print("\n=== Todos los Libros ===")
    print(biblioteca.repositorio_libro.mostrar_libros())

def mostrar_todos_los_autores(biblioteca):
    """
    Muestra todos los autores registrados en la biblioteca.
    """
    print("\n=== Todos los Autores ===")
    print(biblioteca.repositorio_autor.mostrar_autores())

def mostrar_todos_los_generos(biblioteca):
    """
    Muestra todos los géneros literarios registrados en la biblioteca.
    """
    print("\n=== Todos los Géneros Literarios ===")
    print(biblioteca.repositorio_genero.mostrar_generos())

def mostrar_todos_los_subgeneros(biblioteca):
    """
    Muestra todos los subgéneros literarios específicos registrados en la biblioteca.
    """
    print("\n=== Todos los Subgéneros Literarios ===")
    print(biblioteca.repositorio_especifico.mostrar_especificos())
