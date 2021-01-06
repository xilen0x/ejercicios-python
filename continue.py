#La palabra resrvada continue, hace que no se tome en cuenta el siguiente línea de código
count = 0
titulo = "hola hola"

for e in titulo:
    if e == " ":
        continue
    count += 1


print("La cantidad de letras aquí es: ", count)