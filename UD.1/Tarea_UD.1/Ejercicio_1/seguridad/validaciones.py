import re  # Módulo nativo expresiones regulares.

def comprobar_dni(dni):
    """Verifica que el DNI sea válido (formato 8 números + letra)."""
    patrones_regulares = r"^\d{8}[A-Z]$"

    return bool(re.match(patrones_regulares,dni))