# biblioteca/modelos/generos/genero.py

class Genero:
    
    __id_counter = 1 # Contador para los registros existentes y los nuevos que se añadan
    
    def __init__(self, nombre_genero):
        
        self.__id = Genero.__id_counter  # Asigna el ID actual, es decir, el ID = 1
        Genero.__id_counter += 1         # Contador autoincremental
        
        self.__nombre_genero = nombre_genero
        
    def get_id(self):
        return self.__id
    
    def set_id(self, nuevo_id):
        self.__id = nuevo_id    # Método para actualizar el ID
        
    def get_nombre_genero(self):
        return self.__nombre_genero

    def set_nombre(self, value):
        self.__nombre_genero = value

    def __str__(self):
        """Método __str__. Muestra todos los datos de modelo Subgénero"""
        return f"Id: {self.get_id()}.\nNombre Género Literario: {self.get_nombre_genero()}."

    def mostrar_datos_genero(self):
        """Muestra los datos específicos del Género Literario."""
        return f"Nombre Género Literario: {self.get_nombre_genero()}."