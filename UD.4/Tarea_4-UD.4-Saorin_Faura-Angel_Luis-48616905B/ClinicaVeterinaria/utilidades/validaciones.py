# ClinicaVeterinaria/utilidades/validaciones.py

import re
from datetime import datetime
import sys

# Valida fechas en formato DD-MM-AAAA
def validar_fecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, "%d-%m-%Y")
        return fecha.date()
    except ValueError:
        print("Fecha inválida. Introduce la fecha en formato DD-MM-AAAA.")
        return None

# Valida nombres (mascotas, propietarios)
def validar_nombre(nombre):
    if nombre and nombre.isalpha() and len(nombre) <= 50:
        return nombre.capitalize()
    print("Nombre inválido. Asegúrate de usar solo letras y no superar 50 caracteres.")
    return None

# Valida DNI para propietarios
def validar_dni(dni):
    if re.match(r'^\d{8}[A-Z]$', dni):
        return dni
    print("DNI inválido. Asegúrate de usar el formato correcto (8 dígitos seguidos de una letra mayúscula).")
    return None

# Valida direcciones (opcionalmente puedes definir un máximo de caracteres)
def validar_direccion(direccion):
    if direccion and len(direccion) <= 100:
        return direccion
    print("Dirección inválida. Asegúrate de no superar los 100 caracteres.")
    return None

# Valida correos electrónicos
def validar_correo(correo):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo):
        return correo
    print("Correo electrónico inválido. Introduce un formato válido.")
    return None

# Valida ID de mascota (números enteros positivos)
def validar_id_mascota(id_mascota):
    if isinstance(id_mascota, int) and id_mascota > 0:
        return id_mascota
    print("ID de mascota inválido. Introduce un número entero positivo.")
    return None

# Valida visitas (motivo y observaciones)
def validar_visita(motivo, observaciones):
    if not motivo or len(motivo) > 100:
        print("Motivo de visita inválido. Asegúrate de no superar 100 caracteres.")
        return None
    if observaciones and len(observaciones) > 250:
        print("Observaciones inválidas. Asegúrate de no superar 250 caracteres.")
        return None
    return motivo, observaciones

# Valida montos de facturas
def validar_monto(monto):
    try:
        monto = float(monto)
        if monto > 0:
            return round(monto, 2)
        else:
            print("El monto debe ser un número positivo.")
    except ValueError:
        print("Monto inválido. Asegúrate de introducir un número.")
    return None

# Validación general para IDs
def validar_id(id_value, entity_name="elemento"):
    if isinstance(id_value, int) and id_value > 0:
        return id_value
    print(f"ID de {entity_name} inválido. Debe ser un número entero positivo.")
    return None

def opcion_no_valida():
    """
    Función que muestra un mensaje indicando que la opción seleccionada no es válida.
    """
    print("Opción no válida. Por favor, intenta de nuevo.")

def salir():
    """
    Función para salir del sistema o cerrar el menú de manera segura.
    """
    print("Saliendo... ¡Hasta luego!")
    sys.exit()  # Finaliza el programa
