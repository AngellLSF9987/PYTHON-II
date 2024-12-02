# biblioteca/utilidades/validaciones.py

from datetime import datetime

def validar_fecha(fecha_str):

    """
    Valida y convierte una fecha en formato DD-MM-AAA como string a un objeto date.

    Args:
        fecha_str(str): La fecha como cadena en formato DD-MM-AAAA.

    Returns:
        date: La fecha como objeto de tipo date, o None si el formato dado es incorrecto.
    """

    try:
        return datetime.strptime(fecha_str, "%d-%m-%Y").date()
    
    except ValueError:
        errorDate = "Error: La fecha no tiene el formato correcto (DD-MM-AAAA)."
        print(f"{errorDate}. Valor retornado: None")
        return None
    
def validar_autor(biblioteca):
    """
    Valida si un autor existe en la biblioteca por su pseudónimo. Si no existe, lo crea.
    """
    autores = biblioteca.repositorio_autor.obtener_autores()
    print(f"DEBUG: Autores disponibles: {biblioteca.repositorio_autor.obtener_autores()}")
    
    if autores is None:
        print("Error: No se pudieron cargar los Géneros Literarios.\n")
        return None
    
    pseudonimo = input("Introduce el pseudónimo del autor: \n").strip().lower()    
    # Buscar el autor por pseudónimo
    autor = biblioteca.repositorio_autor.obtener_autor_por_pseudonimo(pseudonimo)

    for autor in autores:
        # Asegurar de que get_nombre_genero() devuelve un string
        if autor.get("pseudonimo").strip().lower() == pseudonimo.lower() is None:
            print(f"El autor '{pseudonimo}' no existe en la base de datos.")
        
        if autor.get("pseudonimo").strip().lower() == pseudonimo.lower():
            print(f"Autor '{pseudonimo}' encontrado.")
        return pseudonimo
    
        
    # Si el autor no existe, preguntar si se desea crear uno nuevo
    # print(f"El autor '{pseudonimo}' no existe en la base de datos.")           

    crear_nuevo = input("¿Deseas crear este autor? (s/n): ").strip().lower()

    # Si no se encuentra, crearlo
    if crear_nuevo == 's':
        print(f"\nEl autor '{pseudonimo}' no ha sido encontrado. Creando nuevo autor.")
        nombre = input("Introduce el nombre del autor:\n").strip()
        apellido1 = input("Introduce el primer apellido del autor:\n").strip()
        apellido2 = input("Introduce el segundo apellido del autor:\n").strip()
        nacido = input("Introduce la fecha de nacimiento del autor (DD-MM-AAAA):\n").strip()
        fallecido = input("Introduce la fecha de fallecimiento del autor (si aplica, DD-MM-AAAA) - ENTER para valor 'Null':\n").strip()
        nacionalidad = input("Introduce la nacionalidad del autor:\n").strip()
        
        nuevo_autor = {
            "id": len(biblioteca.repositorio_autor.obtener_autores()) + 1,  # Asignar un ID incremental
            "nombre": nombre,
            "apellido1": apellido1,
            "apellido2": apellido2,
            "pseudonimo": pseudonimo or None,
            "nacido": nacido,
            "fallecido": fallecido or None,
            "nacionalidad": nacionalidad
        }
        biblioteca.repositorio_autor.agregar_autor(nuevo_autor)
        print(f"El Autor '{pseudonimo}' ha sido creado exitosamente.\n")
        print("DEBUG: Autores después de agregar:", biblioteca.repositorio_autor.obtener_autores())
        return nuevo_autor
    else:
        print("No se realizó ningún cambio.")
        return None

def validar_genero(biblioteca):
    """
    Valida si un Género Literario con el nombre ingresado ya existe en la biblioteca.
    Si no existe, permite crear uno nuevo.
    """ 
    # Verificar si el género ya existe
    generos = biblioteca.repositorio_genero.obtener_generos()
    print(f"DEBUG: Géneros Literarios disponibles: {biblioteca.repositorio_genero.obtener_generos()}")
    
    if generos is None:
        print("Error: No se pudieron cargar los Géneros Literarios.\n")
        return None    

    nombre_genero = input("Introduce el Género Literario:\n").strip().lower()
    # Buscar el género por nombre
    genero = biblioteca.repositorio_genero.buscar_genero_por_nombre(nombre_genero)
    
    for genero in generos:
        # Asegurar de que get_nombre_genero() devuelve un string
        if genero.get("nombre_genero").strip().lower() == nombre_genero.lower() is None:
            print(f"El Género Literario '{nombre_genero}' no existe en la base de datos.")
        
        if genero.get("nombre_genero").strip().lower() == nombre_genero.lower():
            print(f"El Género Literario {nombre_genero} ha sido encontrado.\n")
            return genero           

    crear_nuevo = input("¿Deseas crear este Género Literario? (s/n): ").strip().lower()


    if crear_nuevo == 's':
        nombre_genero = input("Introduce el Género Literario del libro:\n").strip()
            
        nuevo_genero = {
            "id": len(biblioteca.repositorio_genero.obtener_generos()) + 1, # Asignar un ID incremental
            "nombre_genero": nombre_genero
        }
        biblioteca.repositorio_genero.agregar_genero(nuevo_genero)
        print(f"El Género Literario'{nombre_genero}' ha sido creado exitosamente.\n")
        print("DEBUG: Géneros Literarios después de agregar:", biblioteca.repositorio_genero.obtener_generos())
        return nuevo_genero
    else:
        print("No se realizó ningún cambio.")
        return None

def validar_especifico(biblioteca):
    """
    Valida si un Subgénero Literario y el Tipo de Subgénero Literario con el nombre_especifico y el tipo ingresados ya existen en la biblioteca.
    Si no existen, permite crear un nuevo dato.
    """
    # Verificar si los subgéneros ya están cargados
    especificos = biblioteca.repositorio_especifico.obtener_especificos()
    print(f"DEBUG: Subgéneros Literarios disponibles: {especificos}")
    
    if especificos is None:
        print("Error: No se pudieron cargar los Subgéneros y Tipos Literarios.\n")
        return None

    # Solicitar datos al usuario
    nombre_especifico = input("Introduce el Subgénero Literario:\n").strip()
    tipo = input("Introduce el Tipo Específico de Subgénero:\n").strip()

    # Buscar el subgénero literario por nombre y tipo
    especifico_existente = biblioteca.repositorio_especifico.buscar_especifico_por_nombre_y_tipo(nombre_especifico, tipo)
    
    if especifico_existente:
        print(f"El Subgénero Literario '{nombre_especifico}' y Tipo de Subgénero Literario '{tipo}' ya existen.\n")
        return especifico_existente
    else:
        print(f"El Subgénero Literario '{nombre_especifico}' y Tipo de Subgénero Literario '{tipo}' no existen en la base de datos.")

    # Crear un nuevo subgénero si el usuario lo desea
    crear_nuevo = input("¿Deseas crear este Subgénero y Tipo Literario? (s/n): ").strip().lower()
    if crear_nuevo == 's':
        nuevo_especifico = {
            "especifico_id": len(especificos) + 1,  # ID único
            "nombre_especifico": nombre_especifico,
            "tipo": tipo
        }
        biblioteca.repositorio_especifico.agregar_especifico(nuevo_especifico)
        print(f"El Subgénero Literario '{nombre_especifico}' y Tipo de Subgénero Literario '{tipo}' ha sido creado exitosamente.\n")
        print("DEBUG: Subgéneros Literarios después de agregar:", biblioteca.repositorio_especifico.obtener_especificos())
        return nuevo_especifico
    else:
        print("No se realizó ningún cambio.")
        return None

