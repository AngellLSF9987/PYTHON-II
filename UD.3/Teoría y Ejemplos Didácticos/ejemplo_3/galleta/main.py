# ejemplo_3/galleta/main.py

from metodos.metodos import leer_galletas, mas_galletas

def main():
    ruta_archivo = r"C:\Users\tarde\Desktop\PYTHON-II\UD.3\ejemplo_3\galleta\datos\datos_galletas.txt"   
    
    galletas = leer_galletas(ruta_archivo)

    print("Galletas leídas del archivo:")       
    for galleta in galletas:
        print(galleta)                                  # Imprime cada galleta usando el método __str__
    
    mas_galletas()

     
if __name__ == "__main__":
    main()