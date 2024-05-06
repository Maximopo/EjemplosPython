def ejercicio8():
    print(n)
    
    #Dados 2 números enteros, que representan una cantidad parcial y total se pide: Calcular e informar el porcentaje que representa la primera de la segunda. ¿Qué tipo de datos son los recomendados para este algoritmo?
def porcentaje():
    n1 = int(input("ingrese el primer numero:")) 
    n2 = int(input("ingrese el segundo numero:"))
    porcentaje = (n2 * n1) / 100

    print("el porcentaje de la primera de la segunda es:", porcentaje)
    print("el tipo de dato recomendado es el int (el entero)")
    
porcentaje()