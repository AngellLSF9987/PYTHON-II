# Biblioteca/utilidades/validaciones.py

from datetime import datetime
from biblioteca.modelos.generos.genero import Genero
from biblioteca.modelos.autor import Autor
from biblioteca.modelos.generos.especifico import Especifico

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

def validar_genero_especifico(biblioteca):
    
    # Verificar si el género ya existe en la biblioteca
        nombre_genero = input("Introduce el Género Literario:\n").lower()
        genero_encontrado = None
        
        for genero in biblioteca.generos:
            if genero.get_nombre_genero().lower() == nombre_genero:
                genero_encontrado = genero
                print(f"\nGénero '{nombre_genero}' encontrado.\n")
                break
        
        # Si el género no existe, crearlo y añadirlo a la biblioteca
        
        if genero_encontrado is None:
            print(f"\n\nGénero '{nombre_genero}' no encontrado. Creando nuevo género.\n")
            genero_encontrado = Genero(nombre_genero)
            biblioteca.generos.append(genero_encontrado)
        
        nombre_especifico = input("Introduce el Subgénero Literario:\n").lower()
        tipo = input("Introduce el Tipo Específico de Subgénero:\n").lower()
            
        # Verificar si el Género, Subgénero y tipo de subgénero (específico) existe
        especifico_encontrado = None

        for especifico in biblioteca.especificos:
            if (especifico.get_nombre_genero().lower() == genero_encontrado.get_nombre_genero().lower()
                and especifico.get_nombre_especifico().lower() == nombre_especifico.lower()
                and especifico.get_tipo().lower() == tipo.lower()):
                    especifico_encontrado = especifico
                    break

            # Si no se encontró el Subgénero Literario, solicitar los demás datos y crear uno nuevo
        if especifico_encontrado is None:
                print(f"\n\nSubgénero '{nombre_especifico}' y Tipo de Subgénero '{tipo}' no encontrado. Creando nuevo género.\n")
                nombre_especifico = input("Introduce el nombre del Subgénero Literario:\n")
                tipo = input("Introduce el Tipo Específico de Subgénero Literario:\n")        
            
                especifico_encontrado = Especifico(genero_encontrado, nombre_especifico, tipo)
                biblioteca.especificos.append(especifico_encontrado)
                
        return especifico_encontrado
        
def validar_autor(biblioteca):
    
        # Verificar o crear autor
        nombre = input("Introduce el nombre de pila del autor: ")
        pseudonimo = None # Valor por defecto
        
        # Comprobar psseudonimo
        tiene_pseudonimo = input("Introduce el pseudonimo del autor(si se le atribuye) - (s = [sí] / n = [no]):\n").strip().lower()
        
        if tiene_pseudonimo == "s":
                pseudonimo = input("Introduce el pseudónimo del autor: ").strip().lower()
            
        
        autor_encontrado = None

        for autor in biblioteca.autores:
            # Coincide el pseudonimo con autor y pseudonimo
            if (autor.get_nombre().lower() == nombre and autor.get_pseudonimo() and 
                autor.get_pseudonimo().lower() == pseudonimo):
                autor_encontrado = autor
                print(f"\nEl Autor con nombre '{nombre}' o pseudonimo '{pseudonimo}' ha sido encontrado.\n")
                break
            # No coincide pseudónimo: coincidencia de solo el nombre
            else:
                if autor.get_nombre().lower() == nombre and not autor.get_pseudonimo():
                    autor_encontrado = autor
                    print(f"\nEl Autor '{nombre}' (sin pseudónimo) ha sido encontrado.\n")
                    break
        if autor_encontrado is None:
            print(f"\n\nEl Autor con nombre '{nombre}' o pseudonimo '{pseudonimo}' no ha sido encontrado. Creando nuevo autor.\n")
            apellido1 = input("Introduce el primer apellido del autor: ")
            apellido2 = input("Introduce el segundo apellido del autor: ")
            nacido = input("Introduce la fecha de nacimiento del autor (DD-MM-AAAA): ")
            fallecido = input("Introduce la fecha de fallecimiento del autor (si aplica, DD-MM-AAAA): ")
            nacionalidad = input("Introduce la nacionalidad del autor: ") 
            
            autor_encontrado = Autor(nombre, apellido1, apellido2, pseudonimo, nacido, fallecido, nacionalidad)
            biblioteca.autores.append(autor_encontrado)
        
        return autor_encontrado
