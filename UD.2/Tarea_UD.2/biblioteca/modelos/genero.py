# biblioteca/modelos/genero.py

class Genero:
    
    __id_counter = 1 # Contador para los registros existentes y los nuevos que se añadan
    
    def __init__(self, nombre):
        
        self.__id = Genero.__id_counter  # Asigna el ID actual, es decir, el ID = 1
        Genero.__id_counter += 1         # Contador autoincremental
        
        self.__nombre = nombre
        
    def get_id(self):
        return self.__id
    
    def set_id(self, nuevo_id):
        self.__id = nuevo_id    # Método para actualizar el ID
        
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, value):
        self.__nombre = value
        
    def mostrar_datos(self):
        """Muestra todos los datos del libro. Actúa como método __str__"""
        return f"Id: {self.get_id()}.\nNombre: {self.get_nombre}."