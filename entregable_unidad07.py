"""
Dado el siguiente código fuente, agregar comentarios para explicar:

·         El significado de la constante PLAZO_MAXIMO.

·         El significado del bloque de control if-else.

·         La utilidad de la función calcular_periodo, sus parámetros y su retorno.
"""

# Esta constante representa el plazo mínimo de años que se puede introducir
PLAZO_MINIMO = 10 

 
# Esta función recibe un número entero que representa la cantidad de años y devuelve un número entero que representa el total de meses
def calcular_periodo(numero_anyos : int) -> int: 

    MESES_POR_ANYO = 12

    total_periodo = numero_anyos * MESES_POR_ANYO

    return total_periodo

 
# Este bloque if-else evalua el input del usuario, si es menor a la constante PLAZO_MINIMO imprime un mensaje de error,
#  en caso contrario llama a la función calcular_periodo la cual recibe la cantidad de años y devuelve la cantidad de meses
cantidad = int(input("Introduce cantidad de años:")) 

if cantidad < PLAZO_MINIMO:   

    print("La cantidad de años es insuficiente")

else:

    periodo = calcular_periodo(cantidad)

    print(periodo)