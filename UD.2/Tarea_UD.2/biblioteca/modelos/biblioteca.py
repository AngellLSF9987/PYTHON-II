# Biblioteca/modelos/biblioteca.py

class Biblioteca:
    def __init__(self):
        """Método constructor a partir de la instanciación de una lista vacía donde quedarán alojados los objetos libro existentes o creados."""
        self.libros = []

    def agregar_libro(self, libro):
        """Agrega un libro nuevo a la lista de libros de la biblioteca."""
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        """Busca un libro usando el método get_titulo(), que encapsula el atributo título, como referencia de la búsqueda. 
           Devuelve el objeto si se encuentra en la lista."""
        for libro in self.libros:
            if libro.get_titulo().lower() == titulo.lower(): # Uso del método get_titulo(), que encapsula el atributo título.
                return libro
        return None

    def eliminar_libro(self, titulo):
        """Eliminar un libro de la biblioteca por su título."""
        libro = self.buscar_libro(titulo)

        if libro:
            self.libros.remove(libro)
            print("El registro ha sido eliminado correctamente.")
            #return True # True si se elimina con éxito
        else:
            print("No se encontró ningún registro con ese título.\nCompruebe búsqueda e inténtelo de nuevo.")
        #return False    # False si no se encuentra el libro.

    def listar_libros(self):
        """Devuelve una lista completa de todos los libros existentes en la Biblioteca."""
        return [libro.mostrar_datos() for libro in self.libros]
    
    def mostrar_libros_por_autor(self, autor):
        """Muestra todos los libros existentes, publicados por un autor específico."""
        return [libro for libro in self.libros if libro.get_autor() == autor]
        
    def paginas_por_libro(self, titulo):
        """Devuelve el número de páginas que tiene un libro."""
        libro = self.buscar_libro(titulo)
        if libro:
            return libro.get_num_paginas()
        else:
            return "El libro no se encuentra en el listado de registros de la Biblioteca."