class Persona:
    nombre=""
    apellido=""
    edad=0

    #aqui definimos el constructor  (aunque hay una disputa si init es realmente un constructor o no)
    def __init__(self,nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


    def saludar(self):
        print("Bienvenido", self.nombre)


estudiante = Persona("Carlos","Astorga",45)
print(estudiante.nombre, estudiante.apellido, estudiante.edad)

estudiante = Persona("Claudia","Baeza",46)
print(estudiante.nombre, estudiante.apellido, estudiante.edad)