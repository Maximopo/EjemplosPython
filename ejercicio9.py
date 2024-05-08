def ejercicio9():
    print(n)
    
    #Dada una fecha que se lee en formato numérico DDMMAAAA (dos números para el día, dos para el mes, cuatro para el año), se solicita obtener el día el mes y año por separado en tres variables. (usar descomposición matemática)
    
def fecha():
    fecha = int(input("ingrese la fecha:" ))
    año = fecha % 1000
    mes = fecha / 10000
    dia = fecha % 10000000
    
    print("el año es:", año)
    print("el mes es:", mes)
    print("el dia es:", dia)
    print("la fecha insertada es:", fecha)
    
fecha()
