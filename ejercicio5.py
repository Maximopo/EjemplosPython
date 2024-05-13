 #Se ingresa 3 números que representan horas, minutos y segundos. Se pide informar el resultado expresado en segundos. Determinar qué tipo de valor es el aconsejable para los datos solicitados
def multiplicacion():
    horas = int(input("ingrese las horas:")) 
    minutos = int(input("ingrese los minutos:"))
    segundos = int(input("ingrese los segundos:"))
    resultado = horas *3600 + minutos *360 + segundos
    print("la cantidad de segundos totales son:", resultado)

multiplicacion()