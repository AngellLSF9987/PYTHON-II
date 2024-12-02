class Propietario:
    def __init__(self, id_propietario, nombre, apellido, dni, telefono, direccion):
        self.__id_propietario = id_propietario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__telefono = telefono
        self.__direccion = direccion

    # Getters
    def get_id_propietario(self):
        return self.__id_propietario

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_dni(self):
        return self.__dni

    def get_telefono(self):
        return self.__telefono

    def get_direccion(self):
        return self.__direccion

    # Setters
    def set_id_propietario(self, id_propietario):
        self.__id_propietario = id_propietario

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_dni(self, dni):
        self.__dni = dni

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_direccion(self, direccion):
        self.__direccion = direccion

    # Representación legible
    def __str__(self):
        return (f"Propietario[ID: {self.__id_propietario}, Nombre: {self.__nombre} {self.__apellido}, "
                f"DNI: {self.__dni}, Teléfono: {self.__telefono}, Dirección: {self.__direccion}]")
