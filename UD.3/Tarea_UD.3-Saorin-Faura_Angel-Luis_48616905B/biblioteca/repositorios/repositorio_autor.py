# biblioteca/repositorios/repositorio_autor.py

from biblioteca.utilidades.lector_json import cargar_datos_json
from biblioteca.modelos.autor import Autor

# biblioteca/repositorios/repositorio_autor.py

class RepositorioAutor:
    def __init__(self):
        self.autores = []

    def cargar_autores(self, datos_autores):
        """Carga los autores desde el JSON en la memoria del repositorio."""
        self.autores = [
            {
                "id": autor_id,
                "nombre": autor.get("nombre", "Desconocido"),
                "apellido1": autor.get("apellido1", "Desconocido"),
                "apellido2": autor.get("apellido2", "Desconocido"),
                "pseudonimo": autor.get("pseudonimo", "Sin pseudónimo"),
                "nacido": autor.get("nacido", "No especificado"),
                "fallecido": autor.get("fallecido", "No especificado"),
                "nacionalidad": autor.get("nacionalidad", "Desconocido"),
            }
            for autor_id, autor in enumerate(datos_autores, start=1)
        ]

    def mostrar_autores(self):
        """Devuelve la lista de autores en el repositorio."""
        if not self.autores:
            return "No hay autores cargados en el repositorio."
        return "\n".join(f"{autor['id']}: {autor['nombre']} ({autor['pseudonimo']})" for autor in self.autores)


    # def agregar_autor(self, autor):
    #     """Agrega un autor nuevo a la lista de autores de la biblioteca."""
    #     self.autores.append(autor)
    #     self.diccionario_autores[autor.get_pseudonimo().lower()] = autor

    # def buscar_autor_nombre(self, pseudonimo):
    #     """Busca un autor usando su pseudónimo dentro del diccionario de autores."""
    #     return self.diccionario_autores.get(pseudonimo.lower(), None)

    # def reestructurar_ids_autores(self):
    #     """Reestructura los IDs de los autores, haciendo que sean consecutivos."""
    #     for index, autor in enumerate(self.autores):
    #         autor.set_id(index + 1)  # Actualiza los ids, haciendo que empiecen desde 1
