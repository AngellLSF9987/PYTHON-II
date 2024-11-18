# biblioteca/repositorios/repositorio_genero.py

from biblioteca.modelos.generos.genero import Genero

class RepositorioGenero:
        
        def __init__(self):
                
                self.generos = []
                self.diccionario_generos = {}
        
        def cargar_generos(self, lista_generos):
                """
                Carga la lista de géneros en la biblioteca.
                """
                for genero in lista_generos:
                        nuevo_genero = Genero(genero["nombre"])
                        self.generos.append(nuevo_genero)
                        self.diccionario_generos[nuevo_genero.nombre] = nuevo_genero


        def agregar_genero(self, genero):
                """- Agrega un género literario nuevo a la lista de generos de la biblioteca. """
                self.generos.append(genero)
                self.diccionario_generos[genero.get_nombre_genero().lower()] = genero

        def buscar_genero_nombre(self, nombre_genero):
                """- Busca un género literario, usando su atributo nombre_genero, dentro del diccionario de generos. Devuelve el objeto Género buscado si existe."""
                return self.diccionario_generos.get(nombre_genero.lower(), None)

        def mostrar_generos(self):
                """Devuelve una lista completa de todos los géneros literarios existentes en la Biblioteca."""
                return [genero.__str__() for genero in self.generos]

        def reestructurar_ids_generos(self):
                for index, genero in enumerate(self.generos):
                        genero.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.