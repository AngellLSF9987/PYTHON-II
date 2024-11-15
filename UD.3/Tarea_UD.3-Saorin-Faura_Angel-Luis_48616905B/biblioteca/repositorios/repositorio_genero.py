# biblioteca/repositorios/repositorio_genero.py

def agregar_genero(self, genero):
        """- Agrega un género literario nuevo a la lista de generos de la biblioteca. """
        self.generos.append(genero)
        self.diccionario_generos[genero.get_nombre_genero().lower()] = genero

def buscar_genero_nombre(self, nombre_genero):
        """- Busca un género literario, usando su atributo nombre_genero, dentro del diccionario de generos. Devuelve el objeto Género buscado si existe."""
        return self.diccionario_generos.get(nombre_genero.lower(), None)

def reestructurar_ids_generos(self):
        for index, genero in enumerate(self.generos):
            genero.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.

def mostrar_generos(self):
        """Devuelve una lista completa de todos los géneros literarios existentes en la Biblioteca."""
        return [genero.__str__() for genero in self.generos]