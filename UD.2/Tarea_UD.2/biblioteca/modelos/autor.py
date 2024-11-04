# biblioteca/modelos/autor.py

class Autor:
    
    __id_counter = 1 # Contador para los registros existentes y los nuevos que se añadan
    
    def __init__(self, nombre, apellido, nacido, fallecido, nacionalidad):
        
        self.__id = Autor.__id_counter  # Asigna el ID actual, es decir, el ID = 1
        Autor.__id_counter += 1         # Contador autoincremental
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nacido = nacido
        self.__fallecido = fallecido
        self.__nacionalidad = nacionalidad

    def get_id(self):
        return self.__id
    
    def set_id(self, nuevo_id):
        self.__id = nuevo_id    # Método para actualizar el ID
        
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, value):
        self.__nombre = value

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, value):
        self.__apellido = value

    def get_nacido(self):
        return self.__nacido

    def set_nacido(self, value):
        self.__nacido = value

    def get_fallecido(self):
        return self.__fallecido

    def set_fallecido(self, value):
        self.__fallecido = value

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, value):
        self.__nacionalidad = value
              
    def mostrar_datos(self):
        """Muestra todos los datos del libro. Actúa como método __str__"""
        return f"Id: {self.get_id()}.\nNombre: {self.get_nombre}.\nApellido: {self.get_apellido}.\nNacido: {self.get_nacido}.\nFallecido: {self.get_fallecido}.\nNacionalidad: {self.get_nacionalidad}."

        
        
        