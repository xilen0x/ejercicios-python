""" nombre = "Carlos"
edades = '120'
x = 1

for loqsea in nombre:
    print(loqsea)

for edad in edades:
    print(edad)

for x in range (1,50):
    print(x) """

#Ejemplo2
""" frutas = ["manzana","platano","naranja","uva","durazno","piña"]
for e in frutas:
    print(frutas)

for e in frutas:
    print(e)

for e in frutas:
    print(frutas[3])

for e in frutas:
    print(e, end=" - ") """

#Ejemplo3
contador = 0
email = input("Ingrese su email: ")
for e in email:
    if (e == "@") or (e == "."):
        contador = contador + 1

if contador >=2:
    print("Tu email se ha ingresado correctamente!")
else:
    print("Verifica tu email!")
print(contador)