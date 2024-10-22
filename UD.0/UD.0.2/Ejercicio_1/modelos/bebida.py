class Bebida:

    def __init__(self, nombre, precio):
        """MÉTODO CONSTRUCTOR:
        - Crearemos el objeto con los argumentos que pasamos a la hora de iniciar el objeto. """
        self.nombre = nombre
        self.precio = precio

    def mostrar_contenido(self):
        """Actúa como método __str__ y muestra las propiedades o atributos de cada bebida instanciada."""
        return (f"El nombre del producto es {self.nombre} y su precio es {self.precio}€")