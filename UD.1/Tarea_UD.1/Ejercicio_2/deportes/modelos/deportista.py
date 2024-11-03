# deportes/modelos/deportista.py
# CLASE PADRE
class Deportista:
    
    def __init__(self, nombre, apellido, edad, nacionalidad):
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__nacionalidad = nacionalidad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, value):
        self.__nombre = value
        
    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, value):
        self.__apellido = value

    def get_edad(self):
        return self.__edad

    def set_edad(self, value):
        self.__edad = value

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, value):
        self.__nacionalidad = value
        
    def mostrar_datos(self):
        """Método que actúa como __str__"""        
        return f"Nombre: {self.get_nombre()}\nApellido: {self.get_apellido()}\nEdad: {self.get_edad()}\nNacionalidad: {self.get_nacionalidad()}"
