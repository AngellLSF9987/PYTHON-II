class Pieza:

    def __init__(self, color, tamaño):
        """Constructor que inicializa los atributos de color y tamaño."""
        self.color = color
        self.tamaño = tamaño

    def __str__(self):
        """Método para mostrar la información de la pieza."""
        return f"Pieza de color {self.color} y tamaño {self.tamaño}"