class Persona:
    nombre = ""
    apellido = ""
    edad = 0

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print("Bienvenido", self.nombre)


#creo la clase Estudiante q hereda de Persona sus propiadades
class Estudiante(Persona):
    curso = ""
    def __init__(self, curso):
        self.curso = curso


estudiante = Persona("Carlos", "Astorga", 45)
curso_estudiante = Estudiante("Primero")
print(estudiante.nombre, estudiante.apellido, estudiante.edad, curso_estudiante.curso)
estudiante.saludar()
