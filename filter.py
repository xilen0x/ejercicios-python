#ejercicios con función filter que busca mostrar a los empleados que ganan sobre 5000

class Empleado():
    
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [
    Empleado("Juan", "Director", 7500),
    Empleado("Carlos", "Contador", 3000),
    Empleado("Claudia", "SysAdmin", 5500),
    Empleado("Juana", "Analista", 3000),
    Empleado("María", "Secretaria", 2500)
]

salariosAltos = filter(lambda elem:elem.salario>5000, listaEmpleados)

for e in salariosAltos:
    print(e)