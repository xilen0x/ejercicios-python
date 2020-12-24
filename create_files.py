#funcion q al llamarla crea el archivo.txt
def create_file():
    file = open('archivo.txt','w')
    file.close()

create_file()