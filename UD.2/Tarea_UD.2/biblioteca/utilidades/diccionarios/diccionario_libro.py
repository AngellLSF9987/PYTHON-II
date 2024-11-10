# Biblioteca/utilidades/diccionarios/diccionario_libro.py
from biblioteca.modelos.libro import Libro

# Diccionario de Libros

Libros = {
    1: Libro(titulo="Cien Años de Soledad", 
             especifico=("Narrativo_Novela_Realismo Mágico"), 
             fecha_publicacion="05-06-1967",
             num_paginas=417,
             autor="Gabriel García Marquéz"
            ),
    2: Libro(titulo="El Hobbit", 
             especifico=("Narrativo_Novela_Fantasía"), 
             fecha_publicacion="21-09-1937",
             num_paginas=310,
             autor="J.R.R. Tolkien"
            ),
    3: Libro(titulo="1984", 
             especifico=("Narrativo_Novela_Distópica"), 
             fecha_publicacion="08-06-1949",
             num_paginas=328,
             autor="George Orwell"
            ),
    4: Libro(titulo="Matar a un ruiseñor", 
             especifico=("Narrativo_Novela_Suspense"), 
             fecha_publicacion="11-07-1960",
             num_paginas=281,
             autor="Harper Lee"
            ),
    5: Libro(titulo="El Resplandor", 
             especifico=("Narrativo_Novela_Terror"), 
             fecha_publicacion="28-01-1977",
             num_paginas=688,
             autor="Stephen King"
            )
}