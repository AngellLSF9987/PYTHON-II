from modelos.gestor import Gestor

def main():

    gestor = Gestor()

    # Añadir personas

    gestor.agregar_persona("Ana", 28, "Murcia")
    gestor.agregar_persona("Luis", 33, "Madrid")
    gestor.agregar_persona("Vladimir", 45, "Sebastopol")
    gestor.agregar_persona("María", 56, "Murcia")
    gestor.agregar_persona("Carlos", 22, "Barcelona")

    # Mostrar lista inicial de personas
    gestor.mostrar_personas()

    # Buscar personas que viven en Murcia
    gestor.por_ciudad("Murcia")

    # Mostrar la lista después de la modificación
    gestor.modificar_nombre("Ana", "Encarna de Día")

    # Mostrar la lista después de la modificación de nombres
    gestor.mostrar_personas()

if __name__ == "__main__":
    main()
