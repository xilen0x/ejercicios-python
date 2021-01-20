#ejercicios con función map que busca mostrar a los empleados que ganan sobre 5000

class Empleado():
    
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [
    Empleado("Juan", "Director", 6700),
    Empleado("Carlos", "Contador", 7500),
    Empleado("Claudia", "SysAdmin", 2100),
    Empleado("Juana", "Analista", 2150),
    Empleado("María", "Secretaria", 1800)
]

def calculo_comision(empleado):
    empleado.salario = empleado.salario*1.03
    return empleado

listaEmpleadosComision = map(calculo_comision, listaEmpleados)

for e in listaEmpleadosComision:
    print(e)