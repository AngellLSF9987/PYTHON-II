# examen30_Ej47modelos7herramienta.py


class Herramienta:
    
    def __init__(self, tipo):
        
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo

    
    def set_tipo(self, value):
        self.__tipo = value
        
        
    def usar(self):
        """Método __str__"""
        
        print(f"Usando la herramienta: {self.get_tipo()}")