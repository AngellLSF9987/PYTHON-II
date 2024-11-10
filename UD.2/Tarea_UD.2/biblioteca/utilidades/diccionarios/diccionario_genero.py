# Biblioteca/utilidades/diccionarios/diccionario_subgenero.py
from biblioteca.modelos.generos.genero import Genero

# Diccionario de subgéneros con IDs y nombre

GENEROS = {
    1: Genero(nombre_genero="Narrativo"),
    2: Genero(nombre_genero="Lirico"),
    3: Genero(nombre_genero="Dramatico")
}

# def obtener_genero_id(genero_id):
#     genero = GENEROS.get(genero_id)

#     if genero:   # True
#         return genero
#     else:
#         raise ValueError(f"El subgénero con ID {genero_id} no existe")