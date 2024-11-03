# Biblioteca/crud/crud.py

from modelos.libro import Libro
from modelos.biblioteca import Biblioteca
from utilidades.validaciones import validar_fecha

# Instancia Global de la Biblioteca

biblioteca = Biblioteca()

def inicializar_biblioteca():
    """Lista de libros registrados ya en la Biblioteca."""
    libros_existentes = [
        {
            "autor": "Gabriel García Márquez",
            "titulo": "Cien años de soledad",
            "fecha_publicacion": "05-06-1967",
            "num_paginas": 417
        },
        {
            "autor": "J.R.R. Tolkien",
            "titulo": "El hobbit",
            "fecha_publicacion": "21-09-1937",
            "num_paginas": 310
        },
        {
            "autor": "George Orwell",
            "titulo": "1984",
            "fecha_publicacion": "08-06-1949",
            "num_paginas": 328
        },
        {
            "autor": "Harper Lee",
            "titulo": "Matar a un ruiseñor",
            "fecha_publicacion": "11-07-1960",
            "num_paginas": 281
        }
    ]

    for libro_info in libros_existentes:
        fecha_publicacion = validar_fecha(libro_info["fecha_publicacion"])

        if fecha_publicacion:
            libro = Libro(libro_info["autor"], libro_info["titulo"], fecha_publicacion, libro_info["num_paginas"])
            biblioteca.agregar_libro(libro)
    print("Biblioteca inicializada con registros de libros.")

def crear_libro():
    """Crear un nuevo libro y lo añade a la Biblioteca."""

    try:
        print("Nuevo Registro de Libro.")
        titulo = input("Introduce el titulo:\n")
        autor = input("Introduce el autor:\n")

        # Tratamiento de validación de la fecha de publicación como objeto date()
        fecha_publicacion_str = input("Introduce la fecha de publicación (DD-MM-AAAA):\n")
        fecha_publicacion = validar_fecha(fecha_publicacion_str)

        if not fecha_publicacion:
            print("Registro cancelado: Fecha de publicación inválida. Revise la información proporcionada.")
            return
        
        num_paginas = int("Introduce el numero de paginas:\n")

        # Creación y registro del nuevo objeto libro
        libro = Libro(autor,titulo,fecha_publicacion,num_paginas)
        Biblioteca.agregar_libro(libro)

        print("Libro registrado correctamente.")

    except ValueError as e1:                              # Valores incorrectos al ingresar datos
        print(f"Error: Entrada inválida. {e1}")
    except Exception as e2:                               # Errores imprevistos
        print(f"Se produjo un error inesperado: {e2}")

def leer_libro():
    """Busca y muestra la información de un libro por título."""

    try:
        print("Información del Registrado deseado.")
        titulo = input("Introduzca el título del libro a buscar:\n")
        libro = biblioteca.buscar_libro(titulo)

        if libro:
            print("Registro encontrado:")
            print(libro.mostrar_datos())
        else:
            print("Título no encontrado. Revise la información proporcionada e inténtelo de nuevo.")

    except Exception as e3:                                         # Errores imprevistos
        print(f"Se produjo un error al buscar el libro: {e3}")

def actualizar_libro():
    """Actualiza la información de un libro existente."""

    try:
        print("Actualización del Registro.")
        titulo = input("Introduce el título del libro que deseas actualizar:\n")
        libro = biblioteca.buscar_libro(titulo)

        if libro:
            print("Introduce los nuevos datos del libro (deja en blanco para mantener la información actual:)")

            nuevo_titulo = input(f"Título [{libro.get_titulo()}]: ") or libro.get_titulo()
            nuevo_autor = input(f"Autor [{libro.get_autor()}]: ") or libro.get_autor()
            nueva_fecha_publicacion = input(f"Fecha de Publicación [{libro.get_fecha_publicacion()}]: ") or libro.get_fecha_publicacion()
            nueva_num_paginas = input(f"Nº de Páginas[{libro.get_num_páginas()}]: ") or libro.get_num_páginas()

            libro.set_titulo(nuevo_titulo)
            libro.set_autor(nuevo_autor)
            libro.set_fecha_publicacion(nueva_fecha_publicacion)
            libro.set_num_paginas(int(nueva_num_paginas))

            print("Libro actualizado correctamente.")

        else:
            print("Libro no encontrado.")

    except ValueError as e4:                                                    # Valores incorrectos al ingresar datos
        print(f"Error: Entrada inválida. {e4}")

    except Exception as e5:                                                     # Errores imprevistos
        print(f"Se produjo un error inesperado. {e5}")

def eliminar_libro():
    """Elimina un libro de la biblioteca búscado por título."""

    try:
        print("Borrado de Registro.")
        titulo = input("Introduce el título del libro que deseas borrar:\n")

        if biblioteca.eliminar_libro(titulo):
            print("Libro eliminado correctamente.")
        else:
            print("El libro no se encuentra en el listado de registros de la Biblioteca.")

    except Exception as e6:                                                     # Errores imprevistos
        print(f"Se produjo un error al intentar eliminar el libro: {e6}")

def consultar_paginas():
    """Consulta el número de páginas de un libro específico.
    
        - Función < isinstance(objeto, clase) >: verifica que objeto pertenece al tipo o clase especificada,
                   antes de realizar alguna operación con ese valor.
                   Evita errores en tiempo de ejecución.
    """

    try:
        titulo = input("Introduce el título del libro que deseas consultar:\n")
        paginas = biblioteca.paginas_por_libro(titulo)

        if isinstance(paginas, int):
        # Ratifica que paginas sea de tipo int (entero). Si paginas fuera None o cualquier otro tipo de dato, el programa mostrará
        # un mensaje de error, evitando problemas si se intentara imprimir o usar paginas como un entero cuando no lo es.
            """Ratifica que paginas sea de tipo int (entero). Si paginas fuera None o cualquier otro tipo de dato, el programa mostrará
               un mensaje de error, evitando problemas si se intentara imprimir o usar paginas como un entero cuando no lo es."""
            print(f"El libro '{titulo}' tiene {paginas} páginas.")
        else:
            print("El libro no se encuentra en el listado de registros de la Biblioteca.")
    
    except Exception as e7:
        print(f"Se produjo un error al consultar las páginas del libro: {e7}")
