Aquí te dejo un ejemplo de cómo estructurar el programa de la máquina expendedora utilizando POO y con la estructura que mencionas. El proyecto tendrá las siguientes partes:

**Estructura del proyecto:**
```
Expendedora/
│
├── main.py
└── expendedora/
    ├── __init__.py
    └── maquina.py
```

### Código de `maquina.py`:
```python
# maquina.py

class Bebida:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class MaquinaExpendedora:
    def __init__(self):
        # Se inicializan las bebidas disponibles
        self.bebidas = {
            "1": Bebida("Agua", 0.50),
            "2": Bebida("Coca-Cola", 1.20),
            "3": Bebida("Fanta", 1.00)
        }

    def mostrar_menu(self):
        # Mostrar las opciones de bebida disponibles
        print("\n--- Menú de Bebidas ---")
        for key, bebida in self.bebidas.items():
            print(f"{key}. {bebida.nombre} - {bebida.precio:.2f}€")
        print("0. Salir")

    def seleccionar_bebida(self):
        # Pedir al usuario que seleccione una bebida
        opcion = input("Selecciona una bebida (0 para salir): ")
        return opcion

    def procesar_pago(self, bebida):
        # Pedir el dinero al usuario y calcular la diferencia
        dinero_total = 0
        while dinero_total < bebida.precio:
            dinero = float(input(f"Introduce dinero (faltan {bebida.precio - dinero_total:.2f}€): "))
            dinero_total += dinero
            if dinero_total < bebida.precio:
                print(f"Falta dinero. Has introducido {dinero_total:.2f}€")
            elif dinero_total == bebida.precio:
                print(f"Dinero exacto. Dispensando {bebida.nombre}...")
                break
            else:
                print(f"Te sobran {dinero_total - bebida.precio:.2f}€. Dispensando {bebida.nombre}...")
                break

```

### Código de `main.py`:
```python
# main.py

from expendedora.maquina import MaquinaExpendedora

def iniciar_maquina():
    # Instanciar la máquina expendedora
    maquina = MaquinaExpendedora()

    while True:
        maquina.mostrar_menu()
        opcion = maquina.seleccionar_bebida()

        if opcion == "0":
            print("Saliendo...")
            break

        if opcion in maquina.bebidas:
            bebida = maquina.bebidas[opcion]
            maquina.procesar_pago(bebida)
        else:
            print("Opción no válida, por favor selecciona otra.")

if __name__ == "__main__":
    # Iniciar el programa
    iniciar_maquina()
```

### Explicación:
1. **Clase `Bebida`:** Representa cada bebida con su nombre y precio.
2. **Clase `MaquinaExpendedora`:** Contiene un diccionario con las bebidas disponibles y los métodos para mostrar el menú, seleccionar una bebida y procesar el pago.
3. **Método `mostrar_menu`:** Imprime el menú con las opciones de bebida.
4. **Método `seleccionar_bebida`:** Solicita la selección del usuario.
5. **Método `procesar_pago`:** Maneja el ingreso de dinero del usuario, calculando si falta o sobra dinero, y mostrando un mensaje al dispensar la bebida.
6. **Función `iniciar_maquina`:** Es la función principal que ejecuta la máquina, utilizando la estructura `if __name__ == "__main__":`.

Este diseño utiliza la orientación a objetos y está dividido en ficheros para una mejor organización.