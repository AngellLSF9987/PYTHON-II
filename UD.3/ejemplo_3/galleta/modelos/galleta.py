# ejemplo_3/galleta/modelos/galleta.py

class Galleta:
    
    def __init__(self, marca, sabor):
        
        self.__marca = marca
        self.__sabor = sabor
        
    def get_marca(self):
        return self.__marca
        
    def set_marca(self, value):
        self.__marca = value
        
    def get_sabor(self):
        return self.__sabor
    
    def set_sabor(self, value):
        self.__sabor = value   
    
    def __str__(self):
        return f"Galletas de marca {self.get_marca()}, rellenas de {self.get_sabor()}"
            