#Clase principal
class Persona():
    def __init__(self, nombre, apellido, rut, ciudad_origen):
        self.pNombre = nombre
        self.pApellido = apellido
        self.pRut = rut
        self.pCiudad = ciudad_origen

    def descripcion(self):
        print("Nombre:", self.pNombre, "\nApellido:", self.pApellido, "\nRut:",
              self.pRut, "\nCiudad de Origen:", self.pCiudad)


#Clase que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombreE, apellidoE, rutE, ciudad_origenE, puesto, salario):
        super().__init__(nombreE, apellidoE, rutE, ciudad_origenE)
        self.puesto = puesto
        self.salario = salario

    def descripcion(self):
        super().descripcion()
        print("Puesto:", self.puesto, "\nSalario:", self.salario)


Carlos = Empleado('Carlos', 'Astorga', 128424873, 'Copiapo', 'Analista de Datos',  3000)
Carlos.descripcion()

print("---------------------------0---------------------------------")

Pedro = Empleado('Pedro', 'Rosselot', 128548874, 'Santiago','Científico de Datos', 3500)
Pedro.descripcion()