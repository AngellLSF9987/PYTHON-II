# biblioteca/repositorios/repositorio_autor.py

import json
class RepositorioAutor:
    def __init__(self):
        """Constructor del repositorio de géneros."""
        self.autores = []  # Lista para almacenar instancias de Autor

    def cargar_autores(self, datos_autores):
        """Carga los datos de los Autores desde el JSON en la memoria del repositorio."""
        try:
            self.autores = [
                {
                    "autor_id": autor.get("autor_id"),
                    "nombre": autor.get("nombre", "Desconocido"),
                    "apellido1": autor.get("apellido1", "Desconocido"),
                    "apellido2": autor.get("apellido2", "Desconocido"),
                    "pseudonimo": autor.get("pseudonimo", "Sin pseudónimo"),
                    "nacido": autor.get("nacido", "No especificado"),
                    "fallecido": autor.get("fallecido", "No especificado"),
                    "nacionalidad": autor.get("nacionalidad", "Desconocido")
                }
                for autor in datos_autores
            ]
            print("Carga de datos de Autores correcta.")
        
        except FileExistsError as DictAutorError:
            print(f"{DictAutorError}: La sección de datos pertenciente a Autores registrados no ha sido cargada correctamente.")

    def mostrar_autores(self):
        """Devuelve la lista de autores en el repositorio."""
        if not self.autores:
            return "No hay autores cargados en el repositorio."
        return "\n".join(f"ID: {autor['autor_id']}\nNombre del Autor/a: {autor['nombre']}\n2º Nombre o 1º Apellido del Autor/a: {autor['apellido1']}\n\
1º Apellido o 2º Apellido del Autor/a: {autor['apellido2']}\nConocido/a como: {autor['pseudonimo']}\n\
Fecha de Nacimiento: {autor['nacido']}\nFecha de Fallecimiento: {autor['fallecido']}\nNacionalidad: {autor['nacionalidad']}\n"\
        for autor in self.autores)

    def obtener_autor_por_id(self, autor_id):
        """Busca un autor por su ID."""
        print(f"Buscando autor con ID {autor_id}...")  # Depuración
        for autor in self.autores:
            print(f"Comparando con autor: {autor_id}")  # Depuración
            if autor["autor_id"] == autor_id:
                return autor
        print(f"No se encontró ningún Autor con ID {autor_id}.")  # Depuración
        return None

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
