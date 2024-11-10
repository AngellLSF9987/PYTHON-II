# Biblioteca/utilidades/diccionarios/diccionario_especifico.py
from biblioteca.modelos.generos.especifico import Especifico

# Diccionario de subgéneros con IDs y nombre

Especificos = {
    1: Especifico(nombre_genero="Narrativo", nombre_especifico="Novela",
                 tipo = {
                     "Fantasía",
                     "Terror",
                     "Suspense",
                     "Realismo Mágico",
                     "Distópica"
                 }),
    2: Especifico(nombre_genero="Narrativo", nombre_especifico="Cuento",
                 tipo= {
                     
                 }),
    3: Especifico(nombre_genero="Narrativo", nombre_especifico="Fábula",
                 tipo= {
                     
                 }),
    4: Especifico(nombre_genero="Narrativo", nombre_especifico="Leyenda",
                 tipo= {
                     
                 }),
    5: Especifico(nombre_genero="Lirico", nombre_especifico="Égloga",
                 tipo= {
                     
                 }),
    6: Especifico(nombre_genero="Lirico", nombre_especifico="Sátira",
                 tipo= {
                     
                 }),
    7: Especifico(nombre_genero="Lirico", nombre_especifico="Soneto",
                 tipo= {
                     
                 }),
    8: Especifico(nombre_genero="Lirico", nombre_especifico="Himno",
                 tipo= {
                     
                 }),
    9: Especifico(nombre_genero="Dramatico", nombre_especifico="Tragedia",
                 tipo= {
                     
                 }),
    10: Especifico(nombre_genero="Dramatico", nombre_especifico="Drama",
                  tipo= {
                      
                  }),
    11: Especifico(nombre_genero="Dramatico", nombre_especifico="Comedia",
                  tipo= {
                      
                  })
}

# def obtener_especifico_id(especifico_id):
#     especifico = especificos.get(especifico_id)

#     if especifico:   # True
#         return especifico
#     else:
#         raise ValueError(f"El subgénero con ID {especifico_id} no existe")