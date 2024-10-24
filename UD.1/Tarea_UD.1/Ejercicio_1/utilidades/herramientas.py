def comprobar_imc(cliente):
    """Calcula el índice de masa corporal (IMC)."""
    if cliente.get_altura() <= 0:  # Asegurar que la altura es válida
        return "Error: La altura debe ser mayor que 0."

    imc = cliente.get_peso() / (cliente.get_altura() ** 2)

    if imc < 18.5:
        return "Su peso está por debajo del ideal."  # IMC Bajo
    elif 18.5 <= imc <= 24.9:
        return "Su peso está dentro de los parámetros."  # IMC Ideal
    else:
        return "Situación de sobrepeso."


def comprobar_edad(cliente):
    """Comprueba si el cliente es mayor de edad."""
    return cliente.get_edad() >= 18