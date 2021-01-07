def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No es posible dividir por cero!")
        return "Se continúa con la ejecución..."


while True:
    try:
        valor1 = int(input("Ingresa un valor: "))
        valor2 = int(input("Ingresa otro valor: "))
        break
    except ValueError:
        print("Datos ingresados erróneos!")
    finally:                                 #lo que vaya dentro de finally, siempre se ejecutará.
        print("Intente nuevamente...")

operacion = input("Escoge la operación a realizar: suma, resta, multiplica, divide: ")

if operacion == 'suma':
    print(suma(valor1, valor2))
elif operacion == 'resta':
    print(resta(valor1, valor2))
elif operacion == 'multiplica':
    print(multiplica(valor1, valor2))
elif operacion == 'divide':
    print(divide(valor1, valor2))
else:
    print("Operación no permitida")

print("-----------------------------------")
print("Fin de la operación!")
