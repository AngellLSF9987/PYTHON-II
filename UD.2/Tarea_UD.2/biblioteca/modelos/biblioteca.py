# biblioteca/modelos/biblioteca.py

from biblioteca.modelos.libro import Libro
from biblioteca.modelos.autor import Autor
from biblioteca.modelos.generos.genero import Genero
from biblioteca.modelos.generos.especifico import Especifico
from biblioteca.utilidades.validaciones import validar_fecha

class Biblioteca:
    def __init__(self):
        """Método constructor a partir de la instanciación de un diccionario vacío donde quedarán alojados los objetos libro existentes o creados."""
        self.libros = []
        self.generos = []
        self.especificos = []       
        self.autores = []
        
        # Diccionarios de búsqueda rápida
        self.diccionario_libros = {}
        self.diccionario_autores = {}
        self.diccionario_generos = {}
        self.diccionario_especificos = {}
        
        self.inicializar_biblioteca() # Llamada al método de inicialización

#####   1.    REGION INTERFAZ GESTIÓN BIBLIOTECA - LIBROS     #####

    def agregar_libro(self, libro):
        """- Agrega un libro nuevo al diccionario de libros de la biblioteca. """
        try:
            titulo = libro.get_titulo().lower()
        
            if titulo not in self.diccionario_libros:
                self.diccionario_libros[titulo] = libro
        except Exception as e:
            print(f'El libro "{libro.get_titulo()}" ya está registrado. {e}')            

    def buscar_libro_titulo(self, titulo):
        """Busca un libro usando el método get_titulo(), que encapsula el atributo título, como referencia de la búsqueda. 
           Devuelve el objeto si se encuentra en la lista."""
        for libro in self.diccionario_libros.values():
            if libro.get_titulo().lower() == titulo.lower(): # Uso del método get_titulo(), que encapsula el atributo título.
                return libro
        return None

    def reestructurar_ids_libros(self):
        for index, libro in enumerate(self.libros):
            libro.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.

    def mostrar_libros(self):
        """Devuelve una lista completa de todos los libros existentes en la Biblioteca."""
        return [libro.mostrar_datos_libro() for libro in self.diccionario_libros.values()]
    
    def mostrar_libros_por_autor(self, autor):
        """Muestra todos los libros existentes, publicados por un autor específico."""
        autor_buscado = autor.lower() # El autor que buscas debe ser un pseudónimo en minúsculas
        libros_del_autor = [libro for libro in self.diccionario_libros.values() if libro.get_autor().lower() == autor_buscado]
        
        # Muestra los resultados
        for libro in libros_del_autor:
            print(libro.mostrar_datos_libro())
    
    def mostrar_libros_por_genero(self, genero):
        """Muestra todos los libros existentes, publicados por un genero específico."""
        return [libro for libro in self.libros if libro.get_genero().lower() == genero.lower()]
    
    def mostrar_libros_especifico(self, especifico):
        """Muestra todos los libros existentes, publicados por un genero específico."""
        return [libro for libro in self.libros if libro.get_especifico().lower() == especifico.lower()]

#####       FIN REGION INTERFAZ GESTIÓN BIBLIOTECA - LIBROS     #####

#####   2.    REGION INTERFAZ GESTIÓN BIBLIOTECA - AUTORES     #####

    def agregar_autor(self, autor):
        """- Agrega un autor nuevo a la lista de autores de la biblioteca. """
        self.autores.append(autor)
        self.diccionario_autores[autor.get_pseudonimo().lower()] = autor

    def buscar_autor_nombre(self, pseudonimo):
        """- Busca un autor específico, usando su atributo pseudonimo, dentro del diccionario de autores. Devuelve el objeto Autor buscado si existe."""
        return self.diccionario_autores.get(pseudonimo.lower(), None)

    def reestructurar_ids_autores(self):
        for index, autor in enumerate(self.autores):
            autor.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.

    def mostrar_autores(self):
        """Devuelve una lista completa de todos los autores existentes en la Biblioteca."""
        return [autor.__str__() for autor in self.autores]

#####       FIN REGION INTERFAZ GESTIÓN BIBLIOTECA - AUTORES     #####

#####   3.    REGION INTERFAZ GESTIÓN BIBLIOTECA - GÉNEROS Y SUBGÉNEROS LITERARIOS    #####

            ####   3.1.     GÉNEROS LITERARIOS      ####

    def agregar_genero(self, genero):
        """- Agrega un género literario nuevo a la lista de generos de la biblioteca. """
        self.generos.append(genero)
        self.diccionario_generos[genero.get_nombre_genero().lower()] = genero

    def buscar_genero_nombre(self, nombre_genero):
        """- Busca un género literario, usando su atributo nombre_genero, dentro del diccionario de generos. Devuelve el objeto Género buscado si existe."""
        return self.diccionario_generos.get(nombre_genero.lower(), None)

    def reestructurar_ids_generos(self):
        for index, genero in enumerate(self.generos):
            genero.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.

    def mostrar_generos(self):
        """Devuelve una lista completa de todos los géneros literarios existentes en la Biblioteca."""
        return [genero.__str__() for genero in self.generos]

            ####   3.2.     SUBGÉNEROS LITERARIOS      ####

    def agregar_especifico(self, especifico):
        """Agrega un subgénero literario nuevo a la lista de específicos de la biblioteca."""

        # Verificar si alguno de los valores es None antes de agregar
        if especifico.get_nombre_genero() is None or especifico.get_nombre_especifico() is None or especifico.get_tipo() is None:
            raise ValueError("El nombre del género, el subgénero o el tipo no pueden ser nulos.")

        # Asegurar de que el género existe antes de agregar el subgénero
        genero = especifico.get_nombre_genero().lower()  # Obtener el género en minúsculas
        if genero not in self.diccionario_generos:
            raise ValueError(f"El género '{genero}' no existe en la biblioteca. Por favor, primero agregue el género.")

        # Pasar verificación, se agrega el subgénero
        self.especificos.append(especifico)

        # Crear la clave compuesta o "clave de tupla" para el diccionario (género, subgénero, tipo)
        clave = (
            especifico.get_nombre_genero().lower(),
            especifico.get_nombre_especifico().lower(),
            especifico.get_tipo().lower()
        )

        # Almacenar el objeto 'Especifico' en el diccionario usando la clave compuesta
        self.diccionario_especificos[clave] = especifico
        print(f"Subgénero '{especifico.get_nombre_especifico()}' agregado correctamente al género '{especifico.get_nombre_genero()}'.")



    def buscar_especifico_nombre(self, nombre_genero, nombre_especifico, tipo):
        """Busca un subgénero literario por su género, nombre específico y tipo en el diccionario."""
        # Crear la clave compuesta con los tres parámetros
        clave = (
            nombre_genero.lower(),
            nombre_especifico.lower(),
            tipo.lower()
        )
        
        # Buscar en el diccionario usando la clave
        return self.diccionario_especificos.get(clave, None)


    def reestructurar_ids_especificos(self):
        for index, especifico in enumerate(self.especificos):
            especifico.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.

    def mostrar_especificos(self):
        """Devuelve una lista completa de todos los géneros literarios existentes en la Biblioteca."""
        return [especifico.__str__() for especifico in self.especificos]

#####       FIN REGION INTERFAZ GESTIÓN BIBLIOTECA - GÉNEROS Y SUBGÉNEROS LITERARIOS     #####


#####   4.    REGION INICIALIZACIÓN DE LA INTERFAZ BIBLIOTECA CON OBJETOS AÑADIDOS     #####

    def inicializar_biblioteca(self):
        """Inicializa la biblioteca con autores, géneros literarios y libros registrados ya en la Biblioteca."""

        # Inicializar lista de Autores

        autores_existentes = [
            {"nombre": "Gabriel", "apellido1": "García", "apellido2": "Márquez", "pseudonimo":"Gabriel García Márquez" ,"nacido": "06-03-1927", "fallecido": "17-04-2014", "nacionalidad": "Colombia"},
            {"nombre": "Jhon Ronald", "apellido1": "Reuel", "apellido2": "Tolkien","pseudonimo":"J.R.R. Tolkien", "nacido": "03-01-1892", "fallecido": "02-09-1973", "nacionalidad": "Reino Unido"},
            {"nombre": "Eric", "apellido1": "Arthur", "apellido2": "Blair","pseudonimo":"George Orwell", "nacido": "25-06-1903", "fallecido": "21-01-1950", "nacionalidad": "Reino Unido"},
            {"nombre": "Stephen", "apellido1": "Edwing", "apellido2": "King","pseudonimo":"Stephen King", "nacido": "21-09-1947", "fallecido": "No fallecido", "nacionalidad": "EE.UU"},
            {"nombre": "Nelle", "apellido1": "Harper", "apellido2": "Lee","pseudonimo":"Harper Lee", "nacido": "28-04-1926", "fallecido": "19-02-2016", "nacionalidad": "EE.UU"},
        ]

        for autor_info in autores_existentes:
            autor = Autor(autor_info["nombre"], autor_info["apellido1"], autor_info["apellido2"], autor_info["pseudonimo"], autor_info["nacido"], autor_info["fallecido"], autor_info["nacionalidad"])
            self.agregar_autor(autor)

        # Inicializar lista de Géneros Literarios

        generos_existentes = [
            {"nombre_genero":"Narrativo"},
            {"nombre_genero":"Lirico"},
            {"nombre_genero":"Dramatico"},
        ]

        for genero_info in generos_existentes:
            genero = Genero(genero_info["nombre_genero"])
            self.agregar_genero(genero)

        # Inicializar lista de Específicos Literarios

        especificos_existentes = [
            {"nombre_genero":"Narrativo","nombre_especifico":"Novela", "tipo":"Terror"},
            {"nombre_genero":"Narrativo","nombre_especifico":"Novela", "tipo":"Suspense"},
            {"nombre_genero":"Narrativo","nombre_especifico":"Novela", "tipo":"Distópica"},
            {"nombre_genero":"Narrativo","nombre_especifico":"Novela", "tipo":"Realismo Mágico"},
            {"nombre_genero":"Narrativo","nombre_especifico":"Novela", "tipo":"Fantasía"}
        ]

        for especifico_info in especificos_existentes:
            especifico = Especifico(especifico_info["nombre_genero"], especifico_info["nombre_especifico"], especifico_info["tipo"])
            self.agregar_especifico(especifico)


        # Inicializar lista de Libros

        libros_existentes = [
                    {
                        "titulo": "Cien años de soledad",
                        "especifico": self.buscar_especifico_nombre("Narrativo", "Novela", "Realismo Mágico"),
                        "fecha_publicacion": "05-06-1967",
                        "num_paginas": 417,
                        "autor" : self.buscar_autor_nombre("Gabriel García Márquez")                        
                    },
                    {
                        "titulo": "El hobbit",
                        "especifico": self.buscar_especifico_nombre("Narrativo", "Novela", "Fantasía"),
                        "fecha_publicacion": "21-09-1937",
                        "num_paginas": 310,
                        "autor" : self.buscar_autor_nombre("J.R.R. Tolkien")
                    },
                    {
                        "titulo": "1984",
                        "especifico": self.buscar_especifico_nombre("Narrativo", "Novela", "Distópica"),               
                        "fecha_publicacion": "08-06-1949",
                        "num_paginas": 328,
                        "autor" : self.buscar_autor_nombre("George Orwell")
                    },
                    {
                        "titulo": "Matar a un ruiseñor",
                        "especifico": self.buscar_especifico_nombre("Narrativo", "Novela", "Suspense"),                  
                        "fecha_publicacion": "11-07-1960",
                        "num_paginas": 281,
                        "autor" : self.buscar_autor_nombre("Harper Lee")                        
                    },
                    {
                        "titulo": "El Resplandor",
                        "especifico": self.buscar_especifico_nombre("Narrativo", "Novela", "Terror"),
                        "fecha_publicacion": "28-01-1977",
                        "num_paginas": 688,
                        "autor" : self.buscar_autor_nombre("Stephen King")                        
                    }
                ]

        for libro_info in libros_existentes:
            if libro_info["especifico"] and libro_info["autor"]:
                fecha_publicacion = validar_fecha(libro_info["fecha_publicacion"])

                if fecha_publicacion:
                    libro = Libro(libro_info["titulo"], libro_info["especifico"], fecha_publicacion, libro_info["num_paginas"],  libro_info["autor"])
                    self.agregar_libro(libro)
                else:
                    print(f'Formato Fecha de Publicación no válido. El libro "{libro_info['titulo']}" no ha sido añadido a la biblioteca')
        print("Biblioteca inicializada con registros de libros.")