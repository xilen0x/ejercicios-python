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
""" #Ejemplo 2
class Automovil():
    modelo = "sedan"
    puertas = 4
    combustible="gasolina"
    cilindradada=2
    encendido = False

    def encender(self):
        self.encendido = True

audi_a4 = Automovil() #creo la instancia audi_a4

respuesta = input("Quieres encender el audi? SI, NO: ")
respuesta = respuesta.lower()
if respuesta=='si':
    audi_a4.encender() # llamamos a el método, el cual cambiará el encendido a True
    print("El vehículo es un", audi_a4.modelo, "de", audi_a4.puertas, "puertas y se encuentra Encendido")
else:
    print("El vehículo es un", audi_a4.modelo, "de", audi_a4.puertas, "puertas y se encuentra Apagado")

vw = Automovil()
print("El segundo coche es un VW tipo",vw.modelo) """


#Ejemplo 3 - agregamos el concepto de constructor el cual es el estado inicial de la clase
class Coche():
    def __init__(self):
        self.__modelo = "sedan" # El doble guion bajo __ antes del nombre de la variable, indica que estamos encapsulando
        self.__puertas = 4      # la variable para que no pueda ser modificable desde el exterior de la clase.
        self.__combustible = "gasolina"
        self.__cilindradada = 2
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if (self.__enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche es un", self.__modelo,". Tiene", self.__puertas, "puertas.", "Utiliza", self.__combustible)

audi = Coche()
print(audi.arrancar(True))
audi.estado()

print("----------------------------------------------------------------")

vw = Coche()
print(vw.arrancar(False))
vw.estado()