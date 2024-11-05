# examen30_Ej4/modelos/uña.py

from .esmalte import Esmalte

class Uña:
    
    def __init__(self, longitud, forma):
        
        self.__longitud = longitud
        self.__forma = forma
        self.__esmalte = None
        
        
    def get_longitud(self):
        return self.__longitud
    
    def set_longitud(self, value):
        self.__longitud = value

    def get_forma(self):
        return self.__forma

    def set_forma(self, value):
        self.__forma = value
       
    def aplicar_esmalte(self, esmalte):
        
        self.__esmalte = esmalte
        
        print(f"Esmalte {esmalte} aplicado en uña de forma {self.get_forma()} y longitud {self.get_longitud()}")
        
        
    def estado_uña(self):
        
        if self.__esmalte:
            print(f"Uña {self.get_forma()} de longitud {self.get_longitud()}mm con esmalte {self.__esmalte}")
    
        else:
            print(f"Uña {self.get_forma()} de longitud {self.get_longitud()}mm sin esmalte.")