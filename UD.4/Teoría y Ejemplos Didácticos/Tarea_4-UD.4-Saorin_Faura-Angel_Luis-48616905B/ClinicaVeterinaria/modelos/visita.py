class Visita:
    def __init__(self, id_visita, fecha, motivo, id_mascota):
        self.__id_visita = id_visita
        self.__fecha = fecha
        self.__motivo = motivo
        self.__id_mascota = id_mascota

    # Getters
    def get_id_visita(self):
        return self.__id_visita

    def get_fecha(self):
        return self.__fecha

    def get_motivo(self):
        return self.__motivo

    def get_id_mascota(self):
        return self.__id_mascota

    # Setters
    def set_id_visita(self, id_visita):
        self.__id_visita = id_visita

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_motivo(self, motivo):
        self.__motivo = motivo

    def set_id_mascota(self, id_mascota):
        self.__id_mascota = id_mascota

    # Representación legible
    def __str__(self):
        return (f"Visita[ID: {self.__id_visita}, Fecha: {self.__fecha}, Motivo: {self.__motivo}, "
                f"ID Mascota: {self.__id_mascota}]")
