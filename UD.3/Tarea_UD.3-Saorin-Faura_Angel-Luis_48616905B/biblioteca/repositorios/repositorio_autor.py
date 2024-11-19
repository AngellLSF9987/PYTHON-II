# biblioteca/repositorios/repositorio_autor.py

from biblioteca.utilidades.lector_json import cargar_datos_json
from biblioteca.modelos.autor import Autor

class RepositorioAutor:
    
    def __init__(self):
        
        # Inicializa las listas y el diccionario donde se almacenarán los autores
        self.autores = []
        # self.diccionario_autores = {}

    def cargar_autores(self, datos_biblioteca):
        """
        Carga los autores desde un archivo JSON utilizando la función cargar_datos_json.
        """
        # Cargar los datos desde el archivo JSON
        datos = cargar_datos_json(datos_biblioteca)
        
        # Si los datos no son válidos (diccionario vacío), termina la función
        if not datos:
            return
        
        # Recorrer la lista de autores en el JSON
        for autor_data in datos.get("autores", []):
            # Crea un nuevo autor usando los datos del JSON
            autor = Autor(
                nombre = autor_data["nombre"],
                apellido1 = autor_data["apellido1"],
                apellido2 = autor_data["apellido2"],
                pseudonimo = autor_data["pseudonimo"],
                nacido = autor_data["nacido"],
                fallecido = autor_data["fallecido"],
                nacionalidad = autor_data["nacionalidad"]
            )
            return autor
        print(f"Autores cargados desde {datos_biblioteca}")
        
    def agregar_autor(self, autor):
        """Agrega un autor nuevo a la lista de autores de la biblioteca."""
        self.autores.append(autor)
        self.diccionario_autores[autor.get_pseudonimo().lower()] = autor

    def buscar_autor_nombre(self, pseudonimo):
        """Busca un autor usando su pseudónimo dentro del diccionario de autores."""
        return self.diccionario_autores.get(pseudonimo.lower(), None)

    def mostrar_autores(self):
        """Devuelve una lista completa de todos los autores existentes en la biblioteca."""
        return [autor.__str__() for autor in self.autores]

    def reestructurar_ids_autores(self):
        """Reestructura los IDs de los autores, haciendo que sean consecutivos."""
        for index, autor in enumerate(self.autores):
            autor.set_id(index + 1)  # Actualiza los ids, haciendo que empiecen desde 1
