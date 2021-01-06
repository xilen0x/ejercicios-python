#Ejemplo 1
""" def generaPares(limite):
    num = 1
    while num<limite:
        yield num*2
        num+=1

devuelvePares = generaPares(10)

for i in devuelvePares:
    print(i) """

#Ejemplo 2
""" def generaPares(limite):
    num = 1
    while num<limite:
        yield num*2
        num+=1

devuelvePares = generaPares(10)

print(next(devuelvePares))
print("Cualquier cosa")

print(next(devuelvePares))
print("Cualquier cosa")

print(next(devuelvePares)) """

#Ejemplo 3 - aki se aprecia q cada vez q llamo a la funcion (generador) me va entregando los valores de uno e uno.
""" def misLenguajes(*lenguajes): #el * indica en este caso, que se recibirán un n° indeterminado de parámetros.
    for leng in lenguajes:
        yield leng

lenguajesObtenidos = misLenguajes("Python","Javascript","C++","ActionScript","Java")

print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos)) """

#Ejemplo 4 - Para evitar realizar un for anidado, utlizamos un yield from para acceder a los subelementos(letras de cada elemento en este caso)
def misLenguajes(*lenguajes):
    for e in lenguajes:
        yield from e

lenguajesObtenidos = misLenguajes("Python","Javascript","C++","ActionScript","Java")

print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))