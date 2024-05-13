def ejercicio11():
    #Una concesionaria de autos paga a su personal, un salario de 5500 pesos por mes, mas una comisión del 200pesos por cada auto vendido y un adicional del 5% del valor del auto vendido. Diseñar un algoritmo para calcularel salario total del vendedor. Conociendo solamente el número de autos vendidos y el valor de venta de launidad.
    autos = []
    inputUser = ""
    while inputUser != "SALIR":
        inputUser = input("ingrese el valor del auto vendido o SALIR")
        if inputUser != "SALIR":
            inputUser = float(inputUser)
            autos.append(inputUser)
            
    AUX = sum(autos)
    comision = AUX *0.05
    salario = len(autos) * 200
    cobrar = 5500 + salario + comision
    print ("el salario es: ", cobrar ,"pesos")
    
ejercicio11()