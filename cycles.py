""" #Ejemplo5  ciclo if/else-----------------------------------
edad= int(input('Ingresa tu edad:'))
if 0<edad<120:
    print("Tienes ", edad, " años")
else:
    print("El valor ingresado no es válido.") """

# EJEMPLO2------------------------------------------------------
print("*************ASIGNATURAS 2021*************")
print("CALCULO - ","MATEMATICAS - ","DESARROLLO WEB")
print("******************************************")

asig_escogida = input("Escoge tu asignatura: ")
asig_escogida = asig_escogida.lower()  #transformo todo a minuscula
if asig_escogida in ("calculo","matematicas","desarrollo web"):
    print("Has seleccionado ", asig_escogida)
else:
    print("Esta asignatura no está en tu programa")
