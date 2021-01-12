from tkinter import *

raiz = Tk()

#Titulo de la ventana
raiz.title("Soy el título de la ventana")

#Para fijar el tamaño, lo hacemos con el método resizable y las propiedades width y height
#raiz.resizable(0,0) #--> No es posible redimencionar
#raiz.resizable(1,0) #--> Es posible redimencionar solo el ancho
#raiz.resizable(0,1) #--> Es posible redimencionar solo el alto
#raiz.resizable(0,True) #--> También es posible utilizar True or False para el mismo efecto

#raiz.iconbitmap("favicon.ico") #esto para el ícono pero tiene algún error...

#Para el tamaño de la ventana:
raiz.geometry('800x500')

#Aplicar color de fondo a la venta con la siguiente línea, aunque podemos abviarlo agregandole color al frame:
raiz.config(bg="red")

#Crear un frame o marco para trabajar en él:
miFrame = Frame()
#Para poder asociar este frame a nuestra ventana hay que empaquetarlo:
miFrame.pack()
#Si queremos linear el frame abajo centrado, por ej.:
#miFrame.pack(side="bottom")
#Si queremos linear el frame abajo y a la derecha, por ej.:
#miFrame.pack(side="right", anchor="s") #s de SUR, n=NORTE(arriba)

#Color al frame (el cual no se verá a menos que le demos las dimensiones):
miFrame.config(bg="black")
miFrame.config(width="760", height="480")

#Si queremos expandir el frame en sentido horizontal:
#miFrame.pack(fill="x") 
#Si queremos expandir el frame en sentido vertical:
#miFrame.pack(fill="y", expand="True")
#Si queremos expandir el frame en ambos sentidos:
#miFrame.pack(fill="both", expand="True")

# Si queremos modificar el borde del frame:
miFrame.config(bd=30)
#miFrame.config(relief="groove")
miFrame.config(relief="sunken")

#Cambiar el cursor:
miFrame.config(cursor="hand2")


#Esta línea siempre debe ir al final
raiz.mainloop()