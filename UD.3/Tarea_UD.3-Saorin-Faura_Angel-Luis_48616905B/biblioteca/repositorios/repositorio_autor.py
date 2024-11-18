# biblioteca/repositorios/repositorio_autor.py

from biblioteca.modelos.autor import Autor

class RepositorioAutor:
        
        def __init__(self):
            
            self.autores = []
            self.diccionario_autores = {}
            
                
        def cargar_autores(self, lista_autores):
                """
                Carga la lista de autores en la biblioteca.
                """
                for autor in lista_autores:
                        nuevo_autor = Autor(autor["nombre"], autor["nacionalidad"])
                        self.autores.append(nuevo_autor)
                        self.diccionario_autores[nuevo_autor.nombre] = nuevo_autor


        def agregar_autor(self, autor):
                        """- Agrega un autor nuevo a la lista de autores de la biblioteca. """
                        self.autores.append(autor)
                        self.diccionario_autores[autor.get_pseudonimo().lower()] = autor

        def buscar_autor_nombre(self, pseudonimo):
                        """- Busca un autor específico, usando su atributo pseudonimo, dentro del diccionario de autores. Devuelve el objeto Autor buscado si existe."""
                        return self.diccionario_autores.get(pseudonimo.lower(), None)

        def mostrar_autores(self):
                """Devuelve una lista completa de todos los autores existentes en la Biblioteca."""
                return [autor.__str__() for autor in self.autores]

        def reestructurar_ids_autores(self):
                for index, autor in enumerate(self.autores):
                        autor.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.