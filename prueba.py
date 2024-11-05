class Figura:
    def __init__(self, nombre, color):
        self.__nombre = nombre
        self.color = color
        
        
    def get_nombre(self):
        return self.__nombre
    
    def calcular_area(self):
        pass
    
    def describir(self):
        return f"Soy una figura de nombre {self.get_nombre()} y color {self.color}"
    
    
class Cuadrado(Figura):
    
    def __init__(self, lado, nombre="Cuadrado", color="Azul"):
        
        super().__init__(nombre,color)
        self.__lado = lado
    
    def get_lado(self):
        return self.__lado
    
    def calcular_area(self):
        return self.get_lado() ** 2
    
    def describir(self):
        print(f"{super().describir()} y con lado {self.get_lado()}")
        
cuadrado = Cuadrado(5)

print(cuadrado.calcular_area())

cuadrado.describir()