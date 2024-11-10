# Biblioteca/utilidades/diccionarios/diccionario_especifico.py

from biblioteca.modelos.generos.especifico import Especifico

# Diccionario de Subgéneros Específicos

Especificos = {
    1: Especifico(nombre_genero="Narrativo", nombre_especifico="Novela",
                 tipo = {
                     "Fantasía",
                     "Terror",
                     "Suspense",
                     "Realismo Mágico",
                     "Distópica"
                 })
}

def obtener_especificos():
    """Devuelve el diccionario con los subgéneros específicos"""
    return {
        1: Especifico(
            nombre_genero="Narrativo",
            nombre_especifico="Novela",
            tipo = {
                "Fantasía",
                "Terror",
                "Suspense",
                "Realismo Mágico",
                "Distópica"
            }
        )
    }