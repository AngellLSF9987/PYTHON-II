# biblioteca/repositorios/repositorio_libro.py

from biblioteca.modelos.libro import Libro

class RepositorioLibro:
        
        def __init__(self, repositorio_autor, repositorio_genero):
        
                self.especificos = []
                self.diccionario_especifico = {}
                self.repositorio_autor = repositorio_autor
                self.repositorio_genero = repositorio_genero
                
        def cargar_libros(self, lista_libros):
                """Carga la lista de libros en la biblioteca."""
                for libro in lista_libros:
                        nuevo_libro = Libro(libro["titulo"], libro["autor"], libro["genero"], libro["especifico"])
                        self.libros.append(nuevo_libro)
                        self.diccionario_libros[nuevo_libro.titulo] = nuevo_libro

        def agregar_libro(self, libro):
                """- Agrega un libro nuevo al diccionario de libros de la biblioteca. """
                try:
                        titulo = libro.get_titulo().lower()
                        
                        if titulo not in self.diccionario_libros:
                                self.diccionario_libros[titulo] = libro
                except Exception as e:
                        print(f'El libro "{libro.get_titulo()}" ya está registrado. {e}')            

        def buscar_libro_titulo(self, titulo):
                """Busca un libro usando el método get_titulo(), que encapsula el atributo título, como referencia de la búsqueda. 
                Devuelve el objeto si se encuentra en la lista."""
                for libro in self.diccionario_libros.values():
                        if libro.get_titulo().lower() == titulo.lower(): # Uso del método get_titulo(), que encapsula el atributo título.
                                return libro
                return None

        def mostrar_libros(self):
                """Devuelve una lista completa de todos los libros existentes en la Biblioteca."""
                return [libro.mostrar_datos_libro() for libro in self.diccionario_libros.values()]
        
        def mostrar_libros_por_autor(self, autor):
                """Muestra todos los libros existentes, publicados por un autor específico."""
                autor_buscado = autor.lower() # El autor que buscas debe ser un pseudónimo en minúsculas
                libros_del_autor = [libro for libro in self.diccionario_libros.values() if libro.get_autor().lower() == autor_buscado]
                
                # Muestra los resultados
                for libro in libros_del_autor:
                        print(libro.mostrar_datos_libro())
        
        def mostrar_libros_por_genero(self, genero):
                """Muestra todos los libros existentes, publicados por un genero específico."""
                return [libro for libro in self.libros if libro.get_genero().lower() == genero.lower()]
        
        def mostrar_libros_especifico(self, especifico):
                """Muestra todos los libros existentes, publicados por un genero específico."""
                return [libro for libro in self.libros if libro.get_especifico().lower() == especifico.lower()]

        def reestructurar_ids_libros(self):
                for index, libro in enumerate(self.libros):
                        libro.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.

