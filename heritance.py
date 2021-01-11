class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

# creo la instancia moto y hereda de la clase padre Vehículos sus propiedades y métodos
class Motos(Vehiculos):
    def enDosRuedas(self, pirueta):
        self.pirueta = pirueta
        if self.pirueta:
            print("Voy en dos ruedas!!!")
        else:
            print("Voy tranquilo..todo ok!")


class Furgones(Vehiculos):
    def cargado(self, carga):
        self.carga = carga
        if carga>1000:
            print("Estas sobrecargado, no puedes seguir!")
        else:
            print("Todo ok, Puedes seguir!")

print("-------------------------- Vehículo 1 --------------------------")
moto1 = Motos("Kawasaki","KW2000")
moto1.arrancar() #al llamar al método arrancar, el booleano enmarcha cambia a True
moto1.estado()
moto1.enDosRuedas(False)

print("-------------------------- Vehículo 2 --------------------------")
furgon1 = Furgones('Kia', 4200)
furgon1.estado()
furgon1.cargado(1200)
