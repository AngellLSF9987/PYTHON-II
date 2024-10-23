class Persona:

    def __init__(self, nombre, edad, ciudad):
        """Constructor que inicializa los datos de la persona."""

        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def __str__(self):
        """Método para mostrar la información de la persona."""

        return f"{self.nombre}, {self.edad} años, vive en {self.ciudad}"