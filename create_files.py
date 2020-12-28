#funcion q al llamarla crea un archivo vacío llamado archivo.txt
""" def create_file():
    file = open('archivo.txt','w')
    file.close()

create_file() """

#funcion q guarda datos en el archivo.txt (si no existe el archivo se crea autom.%)
def write_file():
    file = open('archivo.txt','a')
    file.write('Nueva linea \n')
    file.write('_________-------__x___-------______\n')
    file.close()

write_file()
 
#función que permite leer un archivo línea por línea.
def read_file():
    archivo = open('archivo.txt', 'r')
    linea = archivo.readline()
    while linea!="":
        print(linea)
        linea = archivo.readline()

read_file()