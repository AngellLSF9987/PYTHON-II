# examen30_Ej4/main.py

from modelos.uña import Uña
from modelos.esmalte import Esmalte
from simulacion.metodos import aplicar_manicura_basica

def main():
    
    esmalte_rojo = Esmalte("rojo", "Loreal")
    esmalte_azul = Esmalte("azul", "Marvimundo")
    esmaltes = [esmalte_rojo, esmalte_azul]
    
    uñas = [Uña(10, "redonda"), Uña(12, "alargada"), Uña(9, "cuadrada")]
    
    aplicar_manicura_basica(uñas, esmaltes)
    
    print("\n- Estado Final -\n")
    
    for uña in uñas:
        uña.estado_uña()
        
        
if __name__ == "__main__":
    main()