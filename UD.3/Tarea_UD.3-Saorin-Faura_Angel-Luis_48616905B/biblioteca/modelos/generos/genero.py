class Genero:
    
    __id_counter = 1  # Contador para los registros existentes y los nuevos que se añadan
    
    def __init__(self, nombre_genero):
        """Inicializa el género literario con un nombre y un ID único."""
        if isinstance(nombre_genero, str):
            self.nombre_genero = nombre_genero.strip()
        else:
            raise ValueError(f"nombre_genero debe ser un string, pero se recibió {type(nombre_genero)}.")
        
        self.__id = Genero.__id_counter  # Asigna el ID actual
        Genero.__id_counter += 1         # Incrementa el contador autoincremental
        self.__nombre_genero = nombre_genero.strip()  # Asegurar que el nombre no tenga espacios extras
        
    def get_id(self):
        """Obtiene el ID del género."""
        return self.__id
    
    def set_id(self, nuevo_id):
        """Actualiza el ID del género."""
        self.__id = nuevo_id
    
    def get_nombre_genero(self):
        """Obtiene el nombre del género."""
        return self.__nombre_genero

    def set_nombre_genero(self, nuevo_nombre_genero):
        """Actualiza el nombre del género con una nueva validación."""
        if nuevo_nombre_genero:
            self.__nombre_genero = nuevo_nombre_genero.strip()  # Eliminar espacios extra al principio y al final
        else:
            raise ValueError("El nombre del género no puede estar vacío.")  # Validación adicional si es vacío

    def __str__(self):
        """Devuelve una representación en cadena de la clase Genero."""
        return f"Id: {self.get_id()}.\nNombre Género Literario: {self.get_nombre_genero()}."

    def mostrar_datos_genero(self):
        """Muestra los datos del género literario."""
        return f"Nombre Género Literario: {self.get_nombre_genero()}."
