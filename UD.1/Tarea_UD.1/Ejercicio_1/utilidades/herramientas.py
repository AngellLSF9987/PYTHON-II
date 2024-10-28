def comprobar_imc(cliente):
    """Calcula el índice de masa corporal (IMC)."""
    if cliente.get_altura() <= 0:  # Asegurar que la altura es válida
        return "Error: La altura debe ser mayor que 0."

    imc = cliente.get_peso() / (cliente.get_altura() ** 2)

    if imc < 18.5:
        return f"Su IMC es {imc:.2f}.Su peso está por debajo del ideal."  # IMC Bajo
    elif 18.5 <= imc <= 24.9:
        return f"Su IMC es {imc:.2f}.Su peso está dentro de los parámetros."  # IMC Ideal
    elif 25 <= imc <= 29.9:
        return f"Su IMC es {imc:.2f}. Está en una situación de sobrepeso leve."  # IMC sobrepeso leve
    else:
        return f"Su IMC es {imc:.2f}.Situación de sobrepeso."   # IMC Obesidad


def comprobar_edad(cliente):
    """Comprueba si el cliente es mayor de edad."""
    if cliente.get_edad() >= 18:
        return f"{cliente.get_nombre()} es mayor de edad."
    else:
        return f"{cliente.get_nombre()} es menor de edad."