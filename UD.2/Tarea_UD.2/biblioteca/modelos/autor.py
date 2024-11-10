# biblioteca/modelos/autor.py

# from datetime import date
class Autor:
    
    __id_counter = 1 # Contador para los registros existentes y los nuevos que se añadan
    
    def __init__(self, nombre, apellido1, apellido2, conocido, nacido, fallecido, nacionalidad):
        
        self.__id = Autor.__id_counter  # Asigna el ID actual, es decir, el ID = 1
        Autor.__id_counter += 1         # Contador autoincremental
        
        self.__nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__conocido = conocido
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

    def get_apellido1(self):
        return self.__apellido1

    def set_apellido1(self, value):
        self.__apellido1 = value

    def get_apellido2(self):
        return self.__apellido2

    def set_apellido2(self, value):
        self.__apellido2 = value

    def get_conocido(self):
        return self.__conocido

    def set_conocido(self, value):
        self.__conocido = value

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

    def __str__(self):
        """Método __str__. Muestra todos los datos de modelo Autor"""
        return f"Id: {self.get_id()}.\nNombre: {self.get_nombre()}.\nApellidos: {self.get_apellido1()} {self.get_apellido2()}.\nConocido/a como: {self.get_conocido()}\nNacido/a: {self.get_nacido()}.\nFallecido/a: {self.get_fallecido()}.\nNacionalidad: {self.get_nacionalidad()}.\n"
    
    def mostrar_datos_autor(self):
        """Muestra todos los datos específicos del libro."""
        return f"Nombre: {self.get_nombre()}.\nApellidos: {self.get_apellido1()} {self.get_apellido2()}.\nConocido/a como: {self.get_conocido()}\nNacido/a: {self.get_nacido()}.\nFallecido/a: {self.get_fallecido()}.\nNacionalidad: {self.get_nacionalidad()}.\n"