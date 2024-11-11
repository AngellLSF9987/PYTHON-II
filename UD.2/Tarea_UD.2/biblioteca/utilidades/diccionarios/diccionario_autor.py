# Biblioteca/utilidades/diccionarios/diccionario_autor.py
from biblioteca.modelos.autor import Autor

# Diccionario de Autores

Autores = {
    1: Autor(nombre="Gabriel", 
             apellido1="García", 
             apellido2="Márquez",
             pseudonimo="Gabriel García Márquez",
             nacido="06-03-1927",
             fallecido="17-04-2014",
             nacionalidad="Colombia"
            ),
    2: Autor(nombre="Jhon Ronald", 
             apellido1="Reuel", 
             apellido2="Tolkien",
             pseudonimo="J.R.R. Tolkien",
             nacido="03-01-1892",
             fallecido="02-09-1973",
             nacionalidad="Reino Unido"
            ),
    3: Autor(nombre="Eric", 
             apellido1="Arthur", 
             apellido2="Blair",
             pseudonimo="George Orwell",
             nacido="25-06-1903",
             fallecido="21-01-1950",
             nacionalidad="Reino Unido"
            ),
    4: Autor(nombre="Stephen", 
             apellido1="Edwing", 
             apellido2="King",
             pseudonimo="Stephen King",
             nacido="32-09-1947",
             fallecido="No Fallecido",
             nacionalidad="EE.UU"
            ),
    5: Autor(nombre="Nelle", 
             apellido1="Harper", 
             apellido2="Lee",
             pseudonimo="Harper Lee",
             nacido="28-04-1926",
             fallecido="19-02-2016",
             nacionalidad="EE.UU"
            )
}