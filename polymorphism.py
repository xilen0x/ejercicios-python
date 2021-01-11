# 3 clases de vehiculos con un metodo en común (desplazamiento)

class Coche():
    def desplazamiento(self):
        print ("Tengo cuatro ruedas")


class Moto():
    def desplazamiento(self):
        print ("Tengo dos ruedas")


class Camion():
    def desplazamiento(self):
        print ("Tengo seis ruedas")

#Función que recibe un objeto como parámetro y dependiento del objeto (vehículo) que reciba, invocará el método corresp.
def movimiento(vehiculo):
    vehiculo.desplazamiento()

#instancias de clases
khumo = Camion()
audi = Coche()
yamaha = Moto()

#llamadas a la función movimiento: 
movimiento(khumo)
movimiento(audi)
movimiento(yamaha)