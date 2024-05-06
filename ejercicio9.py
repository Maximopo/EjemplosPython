def ejercicio9():
    print(n)
    
    #Dada una fecha que se lee en formato numérico DDMMAAAA (dos números para el día, dos para el mes, cuatro para el año), se solicita obtener el día el mes y año por separado en tres variables. (usar descomposición matemática)
    
def fecha():
    fecha = int(input("ingrese la fecha:" ))
    año = fecha % 10000
    mes_dia = año // 1000 
    mes = año % 100
    dia = mes // 100
    
    print("el año es:", año)
    print("el mes es:", mes)
    print("el dia es:", dia)
    print("la fecha insertada es:", fecha)
    
fecha()
