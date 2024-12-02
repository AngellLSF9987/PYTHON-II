from biblioteca.modelos.biblioteca import Biblioteca
from biblioteca.menus.submenus import submenu_tareas
from biblioteca.utilidades.ruta_datos_json import RUTA_DATOS_BIBLIOTECA

def menu():
    """
    Función principal del menú de la Biblioteca.
    Permite interactuar con las funcionalidades principales del sistema.
    
    - FUNCIONES LAMBDA:
       - Las expresiones lambda pueden ser utilizadas para contener funcionalidades que no necesitan ser 
         nombradas y normalmente se utilizan en un tiempo corto.
    """
    biblioteca = Biblioteca(RUTA_DATOS_BIBLIOTECA)

    opciones = {
        "1": lambda: submenu_tareas.submenu_tareas(biblioteca),
        "2": lambda: buscar_libro_por_titulo(biblioteca),
        "3": lambda: buscar_autor_por_nombre_o_pseudonimo(biblioteca),
        "4": lambda: mostrar_todos_los_libros(biblioteca),
        "5": lambda: mostrar_todos_los_autores(biblioteca),
        "6": lambda: mostrar_todos_los_generos(biblioteca),
        "7": lambda: mostrar_todos_los_subgeneros(biblioteca),
        "0": salir
    }

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
        accion = opciones.get(opcion, opcion_no_valida)
        accion()

def opcion_no_valida():
    print("\n⚠️ Opción no válida. Por favor, elija una opción válida.\n")

def salir():
    print("\n¡Hasta luego! Gracias por usar Biblioteca AVANZA.\n")
    exit()

def buscar_libro_por_titulo(biblioteca):
    """Permite buscar un libro por su título y muestra detalles relevantes."""
    titulo = input("\nIngrese el título del libro que desea buscar:\n").strip()

    if not titulo:
        print("\n⚠️ No ingresó un título. Inténtelo de nuevo.")
        return

    try:
        libros = biblioteca.repositorio_libro.libros
        resultados = [libro for libro in libros if titulo.lower() in libro["titulo"].lower()]

        if resultados:
            print("\n=== Resultados de la búsqueda ===\n")
            for libro in resultados:
                genero = biblioteca.repositorio_genero.obtener_genero_por_id(libro["genero_id"])
                nombre_genero = genero["nombre_genero"] if genero else "Género Literario Desconocido"
                especifico = biblioteca.repositorio_especifico.obtener_especifico_por_id(libro["especifico_id"])                
                nombre_especifico = especifico["nombre_especifico"] if especifico else "Subgénero Literario Desconocido"
                tipo = especifico['tipo'] if especifico else "Tipo Desconocido"
                autor = biblioteca.repositorio_autor.obtener_autor_por_id(libro["autor_id"])
                autor_nombre = autor["nombre"] if autor else " Autor Desconocido"


                print(
                    f"ID: {libro['libro_id']}\n"
                    f"Título: {libro['titulo']}\n"
                    f"Género Literario: {nombre_genero} | Subgénero Literario: {nombre_especifico} - Tipo: {tipo}\n"
                    f"Fecha de Publicación: {libro['fecha_publicacion']}\n"
                    f"Autor: {autor_nombre}\n"
                )
        else:
            print("\n⚠️ No se encontraron libros con ese título.")
    except Exception as e:
        print(f"\n⚠️ Error inesperado al buscar libros: {e}")

def buscar_autor_por_nombre_o_pseudonimo(biblioteca):
    """Permite buscar un autor por su nombre completo o pseudónimo."""
    criterio = input("\nIngrese el nombre completo o pseudónimo del autor que desea buscar:\n").strip()

    if not criterio:
        print("\n⚠️ No ingresó un criterio de búsqueda. Inténtelo de nuevo.")
        return

    try:
        autores = biblioteca.repositorio_autor.obtener_autores()
        resultados = [
            autor for autor in autores
            if criterio.lower() in autor["nombre"].lower() or
               criterio.lower() in autor["pseudonimo"].lower()
        ]

        if resultados:
            print("\n=== Resultados de la búsqueda ===\n")
            for autor in resultados:
                print(
                    f"\nID: {autor['autor_id']}\n"
                    f"Nombre Completo: {autor['nombre']} {autor['apellido1']} {autor['apellido2']}\n"
                    f"Pseudónimo: {autor['pseudonimo']}\n"
                    f"Nacionalidad: {autor.get('nacionalidad', 'Desconocida')}\n"
                    f"Fechas: {autor['nacido']} - {autor.get('fallecido', 'Presente')}\n"
                )
        else:
            print("\n⚠️ No se encontraron autores con ese criterio.")
    except Exception as e:
        print(f"\n⚠️ Error inesperado al buscar autores: {e}")

def mostrar_todos_los_libros(biblioteca):
    """Muestra todos los libros registrados en la biblioteca con detalles completos."""
    try:
        libros = biblioteca.repositorio_libro.mostrar_libros()  # Obtiene todos los libros
        
        if libros:
            for libro in libros:
                # Manejo seguro para obtener autor, género y subgénero
                autor = biblioteca.repositorio_autor.obtener_autor_por_id(libro["autor_id"])
                genero = biblioteca.repositorio_genero.obtener_genero_por_id(libro.get("genero_id"))
                especifico = biblioteca.repositorio_especifico.obtener_especifico_por_id(libro.get("especifico_id"))
                
                # Preparar datos del autor
                if autor:
                    nombre_autor = f"{autor['nombre']} {autor['apellido1']} {autor['apellido2']}"
                    pseudonimo = f"({autor['pseudonimo']})" if autor.get("pseudonimo") else ""
                    autor_info = f"{nombre_autor} {pseudonimo}"
                else:
                    autor_info = "Autor Desconocido"

                # Preparar datos del género
                if genero:
                    nombre_genero = f"{genero["nombre_genero"]}" if genero else "Género Literario Desconocido"

                # Preparar datos del subgénero
                if especifico:
                    nombre_especifico = f"{especifico["nombre_especifico"]}"
                    tipo_especifico = f"{especifico["tipo"]}"
                else:
                    nombre_especifico = "Subgénero Literario Desconocido"
                    tipo_especifico = "Desconocido"

                # Mostrar información del libro
                print(
                    f"ID: {libro['libro_id']}\n"
                    f"Título: {libro['titulo']}\n"
                    f"Autor: {autor_info}\n"
                    f"Género Literario: {nombre_genero}\n"
                    f"Subgénero Literario: {nombre_especifico} - Tipo: ({tipo_especifico})\n"
                    f"Fecha de Publicación: {libro['fecha_publicacion']}\n"
                    f"Número de Páginas: {libro['num_paginas']}\n"
                )
    except Exception as e:
        print(f"\n⚠️ Error inesperado al mostrar los libros: {e}")

def mostrar_todos_los_autores(biblioteca):
    """Muestra todos los autores registrados en la biblioteca."""
    try:
        biblioteca.repositorio_autor.mostrar_autores()
    except Exception as e:
        print(f"\n⚠️ Error al mostrar los autores: {e}")

def mostrar_todos_los_generos(biblioteca):
    """Muestra todos los géneros literarios registrados en la biblioteca."""
    try:
        biblioteca.repositorio_genero.mostrar_generos()
    except Exception as e:
        print(f"\n⚠️ Error al mostrar los géneros: {e}")

def mostrar_todos_los_subgeneros(biblioteca):
    """Muestra todos los subgéneros literarios específicos registrados en la biblioteca."""
    try:
        biblioteca.repositorio_especifico.mostrar_especificos()
    except Exception as e:
        print(f"\n⚠️ Error al mostrar los subgéneros: {e}")
