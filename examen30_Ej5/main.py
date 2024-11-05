
from excepciones.error_conversion_float import ErrorConversionFloat
from excepciones.error_conversion_float import convertir_float
        
# Ejemplo de uso de la función
if __name__ == "__main__":
    cadena = input("Introduce una cadena de texto para convertir a float: ")
    
    try:
        resultado = convertir_float(cadena)
        print(f"Conversión exitosa: {resultado}")
    except ErrorConversionFloat as e:
        print(e)