from clientes.cliente import Cliente
from seguridad.validaciones import comprobar_dni



clientes = []

def añadir_cliente():
    """Permite crear un nuevo cliente."""
    dni = input("Introduce el DNI:\n")

    while not comprobar_dni(dni):
        print("DNI no válido.")
        dni = input("Introduce el DNI:\n")

    nombre = input("Introduce el nombre:\n")
    edad = int(input("Introduce la edad:\n"))
    sexo = input("Introduce el sexo (H/M):\n")
    peso = float(input("Introduce el peso (kg):\n"))
    altura = float(input("Introduce la altura (m):\n"))


    cliente = Cliente(dni, nombre, edad, sexo, peso, altura)
    clientes.append(cliente)

    print("Cliente creado correctamente.")

def buscar_cliente(dni):
    """Busca un cliente por DNI."""
    for cliente in clientes:
        if cliente.get_dni() == dni:
            return cliente
    return None

def modificar_cliente():
    """Modifica los datos de un cliente."""

    dni = input("Introduce el DNI del cliente que buscas:\n")
    cliente = buscar_cliente(dni)

    if cliente:
        print("Cliente  encontrado.")

        nombre = input(f"Introduce el nuevo nombre [{cliente.get_nombre()}]: ") or cliente.get_nombre()
        edad = input(f"Introduce la nueva edad [{cliente.get_edad()}]: ") or cliente.get_edad()
        sexo = input(f"Introduce el nuevo sexo [{cliente.get_sexo()}]: ") or cliente.get_sexo()
        peso = input(f"Introduce el nuevo peso [{cliente.get_peso()}]: ") or cliente.get_peso()
        altura = input(f"Introduce la nueva altura [{cliente.get_altura()}]: ") or cliente.get_altura()


        cliente.set_nombre(nombre)
        cliente.set_edad(int(edad))
        cliente.set_sexo(sexo)
        cliente.set_peso(float(peso))
        cliente.set_altura(float(altura))

        print("Cliente actualizado correctamente.")

    else:
        print("Cliente no encontrado.")

def borrar_cliente():
    """Borrar un cliente de la lista."""
    
    dni = input("Introduce el DNI del cliente que deseas borrar:\n")
    cliente = buscar_cliente(dni)

    if cliente:
        clientes.remove(cliente)
        print(f"Cliente con DNI {dni} ha sido borrado correctamente.")
    else:
        print(f"No se encontró ningún cliente con el DNI {dni}.")