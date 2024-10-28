from modelos.persona import Persona

class Gestor:

    def __init__(self):
        """Constructor que inicializa un lista vacía de personas."""

        self.personas = []

    def agregar_persona(self, nombre, edad, ciudad):
        """Agregar una persona a la lista."""

        nueva = Persona(nombre, edad, ciudad)
        self.personas.append(nueva)

    def por_ciudad(self, ciudad):
        """Método de búsqueda del nombre de personas usando como filtro la ciudad donde viven."""
        print(f"\nPersonas que viven en {ciudad}:\n")

        for persona in self.personas:
            if persona.ciudad == ciudad:
                print(persona.nombre)

    def modificar_nombre(self, nombre_anterior, nombre_actualizado):
        """Modificar el nombre de una persona si coincide."""

        for persona in self.personas:
            if persona.nombre == nombre_anterior:
                persona.nombre = nombre_actualizado
                print(f"Nombre modificado. {nombre_anterior} ahora es {nombre_actualizado}.")
                break

    def mostrar_personas(self):
        """Mostrar listado completo de personas."""

        print("\nListado completo de personas registradas:\n")

        for persona in self.personas:
            print(persona)
