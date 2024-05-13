#Dados 6 números reales, informar el promedio de los mismos.
def promedio():
    n1 = int(input("ingrese el primer numero:")) 
    n2 = int(input("ingrese el segundo numero:"))
    n3 = int(input("ingrese el tercer numero:")) 
    n4 = int(input("ingrese el cuarto numero:"))
    n5 = int(input("ingrese el quinto numero:")) 
    n6 = int(input("ingrese el sexto numero:"))
    promedio = (n1 + n2 + n3 + n4 + n5 + n6) / 6

    print("el promedio es:", promedio)
    
promedio()