#ejemplo1-----------------------------------------------
""" nombre = input('Ingresa tu Nombre: ')

def saludar():
    print("Bienvenido", nombre) """

#saludar()

#ejemplo2-------------------------------------------------
""" def evaluacion(nota):
    res = "Aprovado"
    if (nota<4):
        res = "Reprovado"
    return res

print(evaluacion(6)) """

#ejemplo3 - uniendo los dos anteriores en uno--------------
""" nombre = input('Ingresa tu Nombre: ')
nota = int(input('Ingresa tu nota: '))


def saludar():
    print("Bienvenido", nombre)


def evaluacion(nota):
    res = "Aprovado"
    if (nota < 4):
        res = "Reprovado"
    return res

saludar()
print(evaluacion(nota)) """

#Ejemplo4  utilizando ciclo if/else
def evaluacion():
    nota= float(input('Ingresa tu nota:'))
    if nota<4:
        print("Has reprobado con un:", nota)
    elif (nota>100):
        print("El valor ingresado no es válido.")
    else:
        print("Has Aprobado con un:", nota)
    return nota

evaluacion()




