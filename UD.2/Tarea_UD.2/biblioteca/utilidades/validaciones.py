# Biblioteca/utilidades/validaciones.py

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
