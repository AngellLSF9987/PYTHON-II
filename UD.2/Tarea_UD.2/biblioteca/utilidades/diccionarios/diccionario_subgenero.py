# Biblioteca/utilidades/diccionarios/diccionario_Especifico.py
from biblioteca.modelos.generos.especifico import Especifico

# Diccionario de subgéneros con IDs y nombre

EspecificoS = {
    1: Especifico(nombre_genero="Narrativo", nombre_Especifico="Novela",
                 tipo = {
                     "Fantasía",
                     "Terror",
                     "Suspense",
                     "Realismo Mágico",
                     "Distópica"
                 }),
    2: Especifico(nombre_genero="Narrativo", nombre_Especifico="Cuento",
                 tipo= {
                     
                 }),
    3: Especifico(nombre_genero="Narrativo", nombre_Especifico="Fábula",
                 tipo= {
                     
                 }),
    4: Especifico(nombre_genero="Narrativo", nombre_Especifico="Leyenda",
                 tipo= {
                     
                 }),
    5: Especifico(nombre_genero="Lirico", nombre_Especifico="Égloga",
                 tipo= {
                     
                 }),
    6: Especifico(nombre_genero="Lirico", nombre_Especifico="Sátira",
                 tipo= {
                     
                 }),
    7: Especifico(nombre_genero="Lirico", nombre_Especifico="Soneto",
                 tipo= {
                     
                 }),
    8: Especifico(nombre_genero="Lirico", nombre_Especifico="Himno",
                 tipo= {
                     
                 }),
    9: Especifico(nombre_genero="Dramatico", nombre_Especifico="Tragedia",
                 tipo= {
                     
                 }),
    10: Especifico(nombre_genero="Dramatico", nombre_Especifico="Drama",
                  tipo= {
                      
                  }),
    11: Especifico(nombre_genero="Dramatico", nombre_Especifico="Comedia",
                  tipo= {
                      
                  })
}

# def obtener_Especifico_id(Especifico_id):
#     Especifico = EspecificoS.get(Especifico_id)

#     if Especifico:   # True
#         return Especifico
#     else:
#         raise ValueError(f"El subgénero con ID {Especifico_id} no existe")