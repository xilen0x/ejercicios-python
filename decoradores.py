#--------------------------------------- FUNCIÓN DECORADORA ----- (Q permite agregarle funcionalidades extra a nuestras funciones).

def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args): # El *args indica que se pueden recibir n elementos como parámetros(args es una convención).
        print("Resultado de la operación: ")

        funcion_parametro(*args)

        print("-----------Fin-----------")
    return funcion_interior

#Les aplicamos la función decoradora a estas dos funciones:
@funcion_decoradora
def suma(num1, num2):
    print(num1+num2)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

#Llamamos finalmente a las funciones:
suma(2,4)
resta(60,2)