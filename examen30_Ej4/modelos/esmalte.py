# examen30_Ej47modelos7esmalte.py

class Esmalte:
    
    def __init__(self, color, marca):
        
        self.__color = color
        self.__marca = marca

    def get_color(self):
        return self.__color
   
    def set_color(self, value):
        self.__color = value

    def get_marca(self):
        return self.__marca

    def set_marca(self, value):
        self.__marca = value
       
    def __str__(self):
        
        return f"Esmalte de color: {self.get_color()} de la marca {self.get_marca()}"
        