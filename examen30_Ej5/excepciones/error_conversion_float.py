
# Excepción personalizada para errores de conversión
class ErrorConversionFloat(Exception):
    """Excepción personalizada para errores de conversión"""
    def __init_(self, mensaje = "Error: La cadena no se puede convertir. Compruebe e inténtelo nuevamente."):
        
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        
        


def convertir_float(cadena):
    """Función personalizada para convertir una cadena a float."""
    try:
        entrada = float(cadena)
        return entrada
        
    except ValueError:
        raise ErrorConversionFloat(f"No se pudo convertir '{cadena}' a float.")
    