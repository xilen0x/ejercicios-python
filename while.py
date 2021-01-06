#Ejemplo while
""" x = 1
while x<10:
    print('{} soy un while menor a 10'.format(x))
    x=x+1

y = 50
while y>0:
    print('{} estoy decrementando desde 50'.format(y))
    y=y-1 """

#Ejemplo while 2:
""" myPass = '123456'
user = input("Nombre de usuario: ")
passw = input("Ingrese su contraseña: ")
while passw != myPass :
    print("Contraseña incorrecta!. Intente nuevamente... \n")
    passw = input("Ingrese su contraseña: ")
print("Bienvenido ", user) """

#Ejercicio1
""" Crea un programa que pida números infinitamente. Los números introducidos deben ser cada vez mayores. 
El programa finalizará cuando se introduce un número menor que el anterior. """
""" 
valor = 0
print("Ingrese un numero mayor que", valor)
nuevoValor = int(input())
while nuevoValor > valor:
    valor = nuevoValor
    print("Ingrese un numero mayor que", valor)
    nuevoValor = int(input())

print("El programa ha finalizado")
 """
#Ejercicio2
""" Crea un programa que pida números positivos indefinidamente. El programa termina cuando se introduce un número negativo. 
Finalmente el programa muestras la suma de todos los números introducidos """

valor = 0
print("Ingrese un numero positivo: ")
nuevoValor = int(input())
while nuevoValor > 0:
    valor = valor + nuevoValor
    print("Ingrese un numero positivo: ")
    nuevoValor = int(input())

print("El programa ha finalizado, y la suma de los valores ingresados es: ", valor)