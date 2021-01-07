#Ejemplo 1
""" class Persona:
    nombre="Carlos"
    apellido="Astorga"
    edad=0
    altura=0
    peso=0

    def saludar(self):
        print("Bienvenido", self.nombre)

    def despedir(self):
        print("Hasta pronto", self.nombre, self.apellido)

saludo =  Persona()
saludo.saludar()
print("-----------------")
saludo.despedir() """

#Ejemplo 2
class Automovil():
    modelo = "sedan"
    puertas = 4
    combustible="gasolina"
    cilindradada=2
    encendido = False

    def encender(self):
        self.encendido = True

audi_a4 = Automovil() #creo la instancia audi_a4

audi_a4.encender() # llamamos a el método, el cual cambiará el encendido a True

print(audi_a4.encendido)

print("El vehículo es un", audi_a4.modelo, "de", audi_a4.puertas, "puertas")