# biblioteca/modelos/generos/especifico.py

from biblioteca.modelos.generos.genero import Genero

class Especifico(Genero):

    __id_counter = 1 # Contador para los registros existentes y los nuevos que se añadan

    def __init__(self, nombre_genero, nombre_especifico, tipo=None):
        # Validar que nombre_genero y nombre_especifico no sean None o vacíos
        if not nombre_genero or not nombre_especifico:
            raise ValueError("El nombre del género y del subgénero son obligatorios.")
        
        super().__init__(nombre_genero)

        self.__especifico_id = Especifico.__id_counter  # Asigna el ID actual
        Especifico.__id_counter += 1         # Contador autoincremental

        # Asignar nombre_especifico y tipo, con validación si tipo es None
        self.__nombre_especifico = nombre_especifico.strip() if nombre_especifico else "Desconocido"
        self.__tipo = tipo.strip() if tipo else "Tipo no definido"

    def get_especifico_id(self):
        return self.__especifico_id
    
    def set_especifico_id(self, nuevo_especifico_id):
        self.__especifico_id = nuevo_especifico_id    # Método para actualizar el ID
    
    def get_nombre_especifico(self):
        return self.__nombre_especifico

    def set_nombre_especifico(self, value):
        if value:
            self.__nombre_especifico = value.strip()
        else:
            raise ValueError("El nombre del subgénero no puede estar vacío.")

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, value):
        if value:
            self.__tipo = value.strip()
        else:
            raise ValueError("El tipo del subgénero no puede estar vacío.")

    def __str__(self):
        """Método __str__. Muestra todos los datos de modelo Subgénero"""
        return f"Id: {self.get_especifico_id()}.\nSubgénero Literario: {self.get_nombre_especifico()} - Tipo Subgénero: {self.get_tipo()}."

    def mostrar_datos_especifico(self):
        """Muestra los datos específicos del Género Literario."""
        return f"Subgénero Literario: {self.get_nombre_especifico()} - Tipo Subgénero: {self.get_tipo()}"

    # def mostrar_datos_especifico_crud(self):
    #     """Muestra los datos específicos del Género Literario."""
    #     return f"Subgénero Literario: {self.get_nombre_especifico()} - Tipo Subgénero: {self.get_tipo()}."
