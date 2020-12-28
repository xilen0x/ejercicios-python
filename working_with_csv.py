#creación de un archivo csv y guardado de datos en él

import csv

doc_csv = open('archivo.csv', 'w')
data = csv.writer(doc_csv)
lista = [
    ["carlos@hotmail.ocm",78451232],
    ["claudia@gmail.com",32215487],
    ["cristian@latinmail.com",65653298]
]

for e in lista:
    data.writerow(e)

doc_csv.close()

#lectura del archivo. 'a' y 'b' hacen ref.a los elementos guardados q en este caso son 2

doc = open('archivo.csv','r')
documento = csv.reader(doc)
for(a,b) in documento:
    print(a,b)

doc.close()