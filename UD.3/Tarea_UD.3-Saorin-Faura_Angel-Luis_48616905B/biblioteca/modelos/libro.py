# biblioteca/modelos/libro.py

from biblioteca.modelos.generos.especifico import Especifico
from biblioteca.modelos.generos.genero import Genero
from biblioteca.modelos.autor import Autor

class Libro():

    __id_counter = 1 # Contador para los registros existentes y los nuevos que se añadan
#genero_id=None, subgenero_id=None, genero
    def __init__(self, titulo, genero, especifico, fecha_publicacion, num_paginas, autor):

        if not isinstance(genero, Genero):
            raise TypeError("El parámetro 'genero' debe ser una instancia de la clase 'Genero'")
        if not isinstance(especifico, Especifico):
            raise TypeError("El parámetro 'especifico' debe ser una instancia de la clase 'Especifico'")
        if not isinstance(autor, Autor):
            raise TypeError("El parámetro 'autor' debe ser una instancia de la clase 'Autor'")

        self.__libro_id = Libro.__id_counter  # Asigna el ID actual, es decir, el ID = 1
        Libro.__id_counter += 1         # Contador autoincremental

        self.__titulo = titulo
        self._genero = genero
        self.__especifico = especifico     
        self.__fecha_publicacion = fecha_publicacion
        self.__num_paginas = num_paginas
        self.__autor = autor

    def get_libro_id(self):
        return self.__libro_id

    def set_libro_id(self, nuevo_libro_id):
        self.__libro_id = nuevo_libro_id    # Método para actualizar el ID

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, value):
        self.__titulo = value      

    def get_genero(self):
        return self.__genero

    def set_genero(self, value):
        self.__genero = value 

    def get_especifico(self):
        return self.__especifico

    def set_especifico(self, value):
        self.__especifico = value 

    def get_fecha_publicacion(self):
        return self.__fecha_publicacion
    
    def set_fecha_publicacion(self, value):
        self.__fecha_publicacion = value

    def get_num_paginas(self):
        return self.__num_paginas

    def set_num_paginas(self, value):
        self.__num_paginas = value

    def get_autor(self):
        return self.__autor

    def set_autor(self, value):
        self.__autor = value  

    def mostrar_datos_libro(self):
        """ - Actúa como método __str__
            - Muestra todos los datos del libro.
            - Llama a las clases Autor, Género y Subgénero e incluye todos los datos de autor, género y subgénero, referidos, cada uno de ellos, en sus respectivos diccionarios y tratados a través de su ID correspondiente     
        """

        genero = self.get_genero()
        datos_genero = genero.mostrar_datos_genero()

        especifico = self.get_especifico()
        #print(f"Tipo de especifico: {type(especifico)}")
        datos_especifico = especifico.mostrar_datos_especifico()
        
        autor = self.get_autor()
        datos_autor = autor.mostrar_datos_autor()
        
        return f"Id: {self.get_libro_id()}.\nTítulo: {self.get_titulo()}.\n{datos_genero}.\n{datos_especifico}.\nFecha Publicación: {self.get_fecha_publicacion()}.\nNº Páginas: {self.get_num_paginas()}.\n- Autor -\n{datos_autor}.\n" 
    
    