class Factura:
    def __init__(self, id_factura, fecha_emision, total, id_visita):
        self.__id_factura = id_factura
        self.__fecha_emision = fecha_emision
        self.__total = total
        self.__id_visita = id_visita

    # Getters
    def get_id_factura(self):
        return self.__id_factura

    def get_fecha_emision(self):
        return self.__fecha_emision

    def get_total(self):
        return self.__total

    def get_id_visita(self):
        return self.__id_visita

    # Setters
    def set_id_factura(self, id_factura):
        self.__id_factura = id_factura

    def set_fecha_emision(self, fecha_emision):
        self.__fecha_emision = fecha_emision

    def set_total(self, total):
        self.__total = total

    def set_id_visita(self, id_visita):
        self.__id_visita = id_visita

    # Representación legible
    def __str__(self):
        return (f"Factura[ID: {self.__id_factura}, Fecha Emisión: {self.__fecha_emision}, "
                f"Total: {self.__total}, ID Visita: {self.__id_visita}]")
