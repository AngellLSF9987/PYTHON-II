class Mascota:
    def __init__(self, mascota_id, nombre, especie, raza, edad, id_propietario):
        self.__mascota_id = mascota_id
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__id_propietario = id_propietario

    # Getters
    def get_mascota_id(self):
        return self.__mascota_id

    def get_nombre(self):
        return self.__nombre

    def get_especie(self):
        return self.__especie

    def get_raza(self):
        return self.__raza

    def get_edad(self):
        return self.__edad

    def get_id_propietario(self):
        return self.__id_propietario

    # Setters
    def set_mascota_id(self, mascota_id):
        self.__mascota_id = mascota_id

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_especie(self, especie):
        self.__especie = especie

    def set_raza(self, raza):
        self.__raza = raza

    def set_edad(self, edad):
        self.__edad = edad

    def set_propietario_id(self, propietario_id):
        self.__propietario_id = propietario_id

    # Representación legible
    def __str__(self):
        return (f"Mascota[ID: {self.__mascota_id}, Nombre: {self.__nombre}, Especie: {self.__especie}, "
                f"Raza: {self.__raza}, Edad: {self.__edad}, ID Propietario: {self.__propietario_id}]")
