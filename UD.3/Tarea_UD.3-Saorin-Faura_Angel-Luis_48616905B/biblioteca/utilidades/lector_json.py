# biblioteca/utilidades/lector_json.py

import json
from biblioteca.utilidades.ruta_datos_json import RUTA_DATOS_BIBLIOTECA

def cargar_datos_json(ruta = RUTA_DATOS_BIBLIOTECA):
    """Leer los datos desde un fichero JSON y devuelve un diccionario con los datos.
    
    Args:
        RUTA_DATOS_BIBLIOTECA (str): Ruta al archivo JSON.
        
    Returns:
        dict: Diccionario con los datos cargados del archivo JSON.
        
    Si ocurre un error, devolverá un diccionario vacío.    
    """
    try:
        with open(ruta, "r", encoding="utf-8-sig") as datos_biblioteca:
            datos = json.load(datos_biblioteca)
            print(f"Datos cargados exitosamente desde {ruta}")
            return datos
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta especificada:\n{ruta}")
        return {}
    
    except json.JSONDecodeError:
        print(f"Error: El archivo JSON en la ruta {ruta} no tiene un formato válido.")
        return {}
