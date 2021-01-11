""" 
#Ejemplo de uso de upper, lower, capitalize
nombreUsuario = input("Introduce tu nombre de usuario: ")

# imprimimos todo tal cual el usuario lo ingresó:
print("Tu nombre es: ", nombreUsuario)

# upper deja todo en mayúscula
print("Tu nombre es: ", nombreUsuario.upper())

# lower deja todo en minúscula
print("Tu nombre es: ", nombreUsuario.lower())

# capitalize deja la primera letra en mayúscula
print("Tu nombre es: ", nombreUsuario.capitalize()) """

#Ejemplo de uso de isdigit() el cual nos ayuda a verificar que lo ingresado sea un número
""" edad = input("Introduce tu edad: ")

while (edad.isdigit()==False):
    print("Debes introducir un valor numérico!")
    edad = input("Introduce tu edad: ")

if (int(edad))<18:
    print("No puedes entrar")
else:
    print("Puedes ingresar") """

# Ejercicio ingreso de email válido:
""" Crea un programa que pida introducir una dirección de email por teclado. 
El programa debe imprimir en consola si la dirección de email es correcta o no en función de si esta tiene el símbolo ‘@’.
Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o ninguna ‘@’ la dirección será errónea.
Si la ‘@’ está al comienzo de la dirección de email o al final, la dirección también será errónea """

almacenaEmail = input("ingresa tu email: ")
email = almacenaEmail.lower()
arroba = email.count('@')

while (arroba != 1 or email.rfind('@')==(len(email)-1) or email.find('@')==0):
    print("Debe ingresar su email correctamente!")
    almacenaEmail = input("Ingrese su email: ")
    email = almacenaEmail.lower()
    arroba = email.count('@')

print("Su email ***", email, "*** se ha registrado correctamente!")