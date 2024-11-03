class Cliente:

    __id_counter = 1

    def __init__(self, dni, nombre, edad, sexo, peso, altura):

        self.__id = Cliente.__id_counter # Asigna el ID actual, es decir, el ID = 1        
        Cliente.__id_counter += 1 # Contador autoincremental

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

    def get_id(self):
        return self.__id
    
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
    

    def mostrar_datos(self):
        """Muestra todos los datos del cliente. Actúa como método __str__"""
        return f"Id:Id: {self.get_id()}\nNombre: {self.get_nombre()}.\nNIF.: {self.get_dni()}.\nEdad: {self.get_edad()} años.\nSexo: {self.get_sexo()}.\nSu peso es: {self.get_peso()}Kg.\nSu estatura: {self.get_altura()} m." 