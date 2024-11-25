# biblioteca/utilidades/validaciones.py

from datetime import datetime
from biblioteca.modelos.generos.genero import Genero

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
    pseudonimo = input("Introduce el pseudónimo del autor: ").strip().lower()
    
    # Buscar el autor por pseudónimo
    autor = biblioteca.repositorio_autor.obtener_autor_por_pseudonimo(pseudonimo)

    if autor:
        print(f"Autor '{pseudonimo}' encontrado.")
        return autor

    # Si el autor no existe, preguntar si se desea crear uno nuevo
    print(f"El autor '{pseudonimo}' no existe en la base de datos.")
    crear_nuevo = input("¿Deseas crear este autor? (s/n): ").strip().lower()

    # Si no se encuentra, crearlo
    if crear_nuevo == 's':
        print(f"\nEl autor '{pseudonimo}' no ha sido encontrado. Creando nuevo autor.")
        nombre = input("Introduce el nombre del autor:\n").strip().lower()
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
    
    return nuevo_autor


def validar_genero(biblioteca):
    """
    Valida si un Género Literario con el nombre ingresado ya existe en la biblioteca.
    Si no existe, permite crear uno nuevo.
    """ 
    generos = biblioteca.repositorio_genero.obtener_generos()
    if generos is None:
        print("Error: No se pudieron cargar los Géneros Literarios.\n")
        return None    

    nombre_genero = input("Introduce el Género Literario:\n").strip().lower()

    for genero in generos:
        # Asegurar de que get_nombre_genero() devuelve un string
        if genero.get("nombre_genero").strip().lower() == nombre_genero.lower():
            print(f"Género Literario {nombre_genero} ha sido encontrado.\n")
            return genero           

    if nuevo_genero is None:
        # Crear si no se encontró el género
        print(f"\nSubgénero Literario '{nombre_genero}' no encontrado. Creando nuevo Género Literario.\n")
        nombre_genero = input("Introduce el Género Literario del libro:\n").strip()
            
        nuevo_genero = {
            "id": len(biblioteca.repositorio_genero.obtener_generos()) + 1, # Asignar un ID incremental
            "nombre_genero": nombre_genero
        }
        biblioteca.repositorio_genero.agregar_genero(nuevo_genero)
    print(f"El Género Literario'{nombre_genero}' ha sido creado exitosamente.\n")
    return nuevo_genero

def validar_especifico(biblioteca):
    """
    Valida si un Subgénero Literario y el Tipo de Subgenero Literario con el nombre_especifico y el tipo ingresados ya existen en la biblioteca.
    Si no existen, permite crearan un nuevo dato.
    """ 
    # Verificar si el subgénero y el tipo de subgénero ya existen
    especificos = biblioteca.repositorio_especifico.obtener_especificos()
    if especificos is None:
        print("Error: No se pudieron cargar los Subgéneros y Tipos Literarios.\n")
        return None
              
    nombre_especifico = input("Introduce el Subgénero Literario:\n").strip().lower()
    tipo = input("Introduce el Tipo Específico de Subgénero:\n").strip().lower()
    
    for especifico in especificos:
        if (especifico.get('nombre_especifico').strip().lower() == nombre_especifico and
            especifico.get('tipo').strip().lower() == tipo):
            print(f"Subgénero Literario {nombre_especifico} y Tipo de Subgénero Literario {tipo} encontrados.\n")
            return especifico
    
    if nuevo_especifico is None:
        # Crear si no se encontró el subgénero
        print(f"\nSubgénero Literario '{nombre_especifico}' y Tipo de Subgénero Literario '{tipo}' no encontrado. Creando nuevo Subgénero y Tipo Literarios.\n")
        nombre_especifico = input("Introduce el Subgénero Literario del libro:\n").strip()
        tipo = input("Introduce el Tipo de Subgénero Literario del libro:\n").strip()

        nuevo_especifico = {
            "id": len(biblioteca.repositorio_especifico.obtener_especificos()) + 1,
            "nombre_especifico": nombre_especifico,
            "tipo": tipo
        }
        biblioteca.repositorio_especificos.agregar_especifico(nuevo_especifico)
    print(f"El Subgénero Literario'{nombre_especifico}' y Tipo de Subgénero Literario '{tipo}' ha sido creado exitosamente.\n")
    return nuevo_especifico
