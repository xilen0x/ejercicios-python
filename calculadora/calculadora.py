#************************************CALCULADORA SIMPLE*************************************#
from tkinter import *

root=Tk()
myFrame = Frame(root)
myFrame.pack()

operacion = ""
resultado = 0
memoria = 0
#------------------------------------PANTALLA--------------------------------#
numeros = StringVar()
pantalla=Entry(myFrame, textvariable=numeros)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #con columnspan le indicamos que esta fila debe ocupar las 4 columnas.
pantalla.config(background="black", fg="#03f943", justify="right", font=(28))

root.title("Simple Calculator")
root.geometry("250x200")
#------------------------------------Funciones Botones --------------------------------
def clickBoton(num):
    global operacion
    if operacion!="":
        memoria = numeros.set(num)
        operacion=""
    else:
        memoria = numeros.set(numeros.get() + num) #obtengo lo q hay en numeros, le concateno el parámetro y lo muestro en la pantalla
        
def clickBotonC():
    numeros.set("0")
    
#----------------------------función suma
def suma(num):
    global operacion, resultado
    resultado = int(num) + int(memoria)
    numeros.set(resultado)
    #resultado = 0

#----------------------------función resta
def resta(num):
    pass       

#función miResultado para el boton del =
def miResultado():
    global resultado
    numeros.set(resultado+int(pantalla.get()))    
    resultado= 0    


#------------------------------------FILA1 BOTONES 7,8,9,/ --------------------------------
boton7 = Button(myFrame, text="7", width=3, command=lambda:clickBoton("7"))
boton8 = Button(myFrame, text="8", width=3, command=lambda:clickBoton("8"))
boton9 = Button(myFrame, text="9", width=3, command=lambda:clickBoton("9"))
botonDiv = Button(myFrame, text="/", width=3)

boton7.grid(row=2, column=1)
boton8.grid(row=2, column=2)
boton9.grid(row=2, column=3)
botonDiv.grid(row=2, column=4)

#------------------------------------FILA2 BOTONES 4,5,6,X --------------------------------
boton4 = Button(myFrame, text="4", width=3, command=lambda:clickBoton("4"))
boton5 = Button(myFrame, text="5", width=3, command=lambda:clickBoton("5"))
boton6 = Button(myFrame, text="6", width=3, command=lambda:clickBoton("6"))
botonMult = Button(myFrame, text="X", width=3)

boton4.grid(row=3, column=1)
boton5.grid(row=3, column=2)
boton6.grid(row=3, column=3)
botonMult.grid(row=3, column=4)

#------------------------------------FILA3 BOTONES 1,2,3,- --------------------------------
boton1 = Button(myFrame, text="1", width=3, command=lambda:clickBoton("1"))
boton2 = Button(myFrame, text="2", width=3, command=lambda:clickBoton("2"))
boton3 = Button(myFrame, text="3", width=3, command=lambda:clickBoton("3"))
botonRest = Button(myFrame, text="-", width=3, command=lambda:resta(numeros.get()))

boton1.grid(row=4, column=1)
boton2.grid(row=4, column=2)
boton3.grid(row=4, column=3)
botonRest.grid(row=4, column=4)

#------------------------------------FILA4 BOTONES 0, ',' ,+,= --------------------------------
boton0 = Button(myFrame, text="0", width=3, command=lambda:clickBoton("0"))
botonComa = Button(myFrame, text=",", width=3, command=lambda:clickBoton(","))
botonIgual = Button(myFrame, text="=", width=3, command=lambda:miResultado())
botonSum = Button(myFrame, text="+", width=3, command=lambda:suma(numeros.get()))

boton0.grid(row=5, column=1)
botonComa.grid(row=5, column=2)
botonIgual.grid(row=5, column=3)
botonSum.grid(row=5, column=4)
#------------------------------------FILA5 BOTONES C --------------------------------
botonC = Button(myFrame, text="C", width=10, command=lambda:clickBotonC())
botonC.grid(row=6, column=1, columnspan=2)
#pantallaOpciones()
numeros.set("0")#Al iniciar que comience en 0




root.mainloop()