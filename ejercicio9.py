def ejercicio9():
    print(n)
    
    #Dada una fecha que se lee en formato numérico DDMMAAAA (dos números para el día, dos para el mes, cuatro para el año), se solicita obtener el día el mes y año por separado en tres variables. (usar descomposición matemática)
    
def fecha():
    fecha = int(input("ingrese la fecha:" ))
    año = fecha % 10000
    fecha = int (fecha / 10000)
    mes = fecha % 100
    fecha = int (fecha / 100)
    dia = fecha 
    
    print("el año es:", año)
    print("el mes es:", mes)
    print("el dia es:", dia)
    
fecha()
