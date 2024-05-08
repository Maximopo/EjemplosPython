def ejercicio6():
    print(n)
    
    #Se necesita calcular la superficie de un triángulo, y se dispone solamente de los valores de su base y altura.Definir también que tipo de valor es aconsejable para las variables con la información que se tiene.**No se podrá usar valores fijos en las fórmulas del algoritmo. Solo variables y/o constantes.**
def triangulo():
    base = float(input("ingrese la base:")) 
    altura = float(input("ingrese la altura:"))
    
    area = (base * altura) /2
    print("la superficie del triangulo es:", area)
    print("es recomendable el valor float para las variables")
    
triangulo()