class Cliente:

    def __init__(self, dni, nombre, edad, sexo, peso, altura):

        self.__dni = dni
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = self.comprobar_sexo(sexo)
        self.__peso = peso
        self.__altura = altura
            
    def comprobar_sexo(self, sexo):
        """Comprueba que el sexo sea correcto, si no, será 'NULL' por defecto."""
        if sexo.upper() not in ['H', 'M']:
            return 'NULL'
        return sexo.upper()
    
    def mostrar_datos(self):
        """Muestra todos los datos del cliente. Actúa como método __str__"""
        return f"Nombre: {self.__nombre}.\nNIF.: {self.__dni}.\nEdad: {self.__edad} años.\nSexo: {self.__sexo}.\nSu peso es: {self.__peso}Kg.\nSu estatura: {self.__altura} m." 
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def set_peso(self, peso):
        self.__peso = peso

    def set_altura(self, altura):
        self.__altura = altura

    def set_dni(self, dni):
        self.__dni = dni

    
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_sexo(self):
        return self.__sexo

    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura

    def get_dni(self):
        return self.__dni