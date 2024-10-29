# CLASE PADRE
class Deportista:
    
    def __init__(self, nombre, edad, nacionalidad):
        self._nombre = nombre
        self._edad = edad
        self._nacionalidad = nacionalidad
        
    def mostrar_datos(self):
        """Método que actúa como __str__"""
        
        return f"Nombre: {self._nombre}\nEdad: {self._edad}\nNacionalidad: {self._nacionalidad}"
        