class Persona:
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
saludo.despedir()