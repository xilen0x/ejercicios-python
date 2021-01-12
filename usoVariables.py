nombre = input('Ingresa tu Nombre: ')
apellido = input('Ingresa tu Apellido: ')
edad = int(input('Ingresa tu Edad: '))
print("Bienvenido {} {}, entiendo q tienes {} años".format(nombre,apellido,edad))

if (edad<18):
    print('Eres un cabro chico')
else:
    print('Puedes pasar...')