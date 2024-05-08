def ejercicio10():
    print(n)
    #En un curso de ciencias de la computación la calificación final del estudiante se determina a partir delrendimiento en tres aspectos del trabajo. A) Existe una calificación por los exámenes parciales que representa el30% del valor total de la nota final. B) la calificación por los trabajos prácticos corresponde al 20% del valor de lanota final. C) el examen integrador que corresponde al 50% restante. (los valores de las notas pueden ir de 0 a 10)
def nota():
    examPar = int (input("Inserte la nota parcial:",)[0:11])
    tp = int (input("Inserte la nota de los tps:")[0:11])
    examInt = int (input("Inserte la nota del exámen integral:")[0:11])
    primeranota = (examPar * 30) / 100
    segundanota = (tp * 20) / 100
    terceranota = (examInt * 50) / 100
    notafinal = primeranota + segundanota + terceranota
    print ("la nota final del estudiante es:", notafinal)
nota()
