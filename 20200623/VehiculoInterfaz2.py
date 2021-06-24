# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:19:06 2021

@author: USUARIO
"""
from tkinter import *
from VehiculoPrincipal import *
from Vehiculo import *

p = []

def clicked():
    global p
    p = Parqueadero(int(txtPisos.get()),int(txtEspacios.get()), int(txtpCarros.get()), int(txtpMotos.get()))
    y = p.imprimirParqueadero()
    lblResult.configure(text= y)
    messagebox.showinfo("Parqueadero",'Parqueadero creado con éxito')

def parquear():
    global p 
    y = p.parquear(int(txtPisos1.get()),int(txtEspacios1.get()), txtPlaca.get(), int(selected.get()))
    z = p.imprimirParqueadero()
    lblResult.configure(text= z)
    messagebox.showinfo("Parqueadero",y)
    
def estadoParqueadero():
    global p 
    y = p.imprimirParqueadero()
    lblResult.configure(text= y)
    
def infoVehiculo():
    global p 
    y = p.matriz[int(txtPisos1.get())][int(txtEspacios1.get())].info()
    lblResult.configure(text= y)  
    
def pago():
    global p 
    y = p.matriz[int(txtPisos1.get())][int(txtEspacios1.get())].pago()
    lblResult.configure(text= y) 
    
def descargar():
    global p 
    p.decargarArchivo()
    messagebox.showinfo("Parqueadero",'Archivo generado')
    

window = Tk()

window.title("PARQUEADERO")
window.geometry('800x350')
window.grid_rowconfigure(1, weight=1)#?
window.grid_columnconfigure(0, weight=1)#?

#CONTENEDORES PRINCIPALES
########************************
inicio = Frame(window, bg='grey', width=800, height=100, pady=1)
pagina = Frame(window, bg='grey', width=800, height=100, pady=1)
#UBICACION CONTENEDORES
inicio.grid(row=0, sticky="ew")
pagina.grid(row=1, sticky="ew")

#SUBCONTENEDORES PRINCIPALES
########************************
menu = Frame(pagina, bg='lavender', width=400, height=200, pady=1)
info = Frame(pagina, bg='white', width=400, height=200, pady=1)
#matriz = Frame(pagina, bg='cyan', width=100, height=200, pady=3)
#UBICACION CONTENEDORES
menu.grid(row=0,column=0, sticky="ew")
info.grid(row=0,column=1, sticky="nsew")
#matriz.grid(row=0,column=2, sticky="ew")

#CONTENEDOR INICIO
########************************
lbl = Label(inicio, text="Ingrese info")
lbl.grid(columnspan=40, row=0)

lblPisos = Label(inicio, text="Pisos")
lblPisos.grid(column=0, row=1)
txtPisos = Entry(inicio,width=10)
txtPisos.grid(column=0, row=2)

lblEspacios = Label(inicio, text="Espacios")
lblEspacios.grid(column=5, row=1)
txtEspacios = Entry(inicio,width=10)
txtEspacios.grid(column=5, row=2)

lblpCarros = Label(inicio, text="Precio Carros")
lblpCarros.grid(column=10, row=1)
txtpCarros = Entry(inicio,width=10)
txtpCarros.grid(column=10, row=2)

lblpMotos = Label(inicio, text="Precio Motos")
lblpMotos.grid(column=15, row=1)
txtpMotos = Entry(inicio,width=10)
txtpMotos.grid(column=15, row=2)

btn = Button(inicio, text="Crear Parqueadero", command=clicked, bg ="hot pink")
btn.grid(column=40, row=2)

#CONTENEDOR MENU
########************************

#FRAMES
opciones = Frame(menu, bg='SteelBlue2', width=200, height=100, pady=3)
opciones.grid(row=1, sticky="ew")
crear = Frame(menu, bg='spring green', width=200, height=100, pady=3)
crear.grid(row=0, sticky="ew")

#CREAR
lbl1 = Label(crear, text="Para consultar o crear:")
lbl1.grid(columnspan=5, row=0)

lblPisos1 = Label(crear, text="Piso")
lblPisos1.grid(column=0, row=1)
txtPisos1 = Entry(crear,width=10)
txtPisos1.grid(column=0, row=2)

lblEspacios1 = Label(crear, text="Espacio")
lblEspacios1.grid(column=1, row=1)
txtEspacios1 = Entry(crear,width=10)
txtEspacios1.grid(column=1, row=2)

lblPlaca = Label(crear, text="PLACA")
lblPlaca.grid(column=2, row=1)
txtPlaca = Entry(crear,width=10)
txtPlaca.grid(column=2, row=2)

selected = IntVar()
rad1 = Radiobutton(crear, text='Carro',  value=1, variable=selected)
rad2 = Radiobutton(crear, text='Moto', value=2, variable=selected)
rad1.grid(column=1, row=4)
rad2.grid(column=1, row=5)


#BOTONES
btnCrear = Button(opciones, text="Parquear Vehiculo", command=parquear,bg="salmon")
btnCrear.grid(columnspan=4, row=0)

btn2 = Button(opciones, text="Estado Parqueadero", command=estadoParqueadero)
btn2.grid(column=0, row=1)

btnInfoVehiculo = Button(opciones, text="Info Vehiculo", command=infoVehiculo)
btnInfoVehiculo.grid(column=2, row=1)

btnDescargar= Button(opciones, text="Descargar info", command=descargar)
btnDescargar.grid(column=3, row=1)

btnPago = Button(opciones, text="Pago", command=pago,bg="gold2")
btnPago.grid(columnspan=4, row=2)



#CONTENEDOR INFO
########************************
lblResult = Label(info, text="info",font="Helvetica 16 bold italic",justify=LEFT)
lblResult.grid(column=0, row=1)

#CONTENEDOR MATRIZ
########************************

# display = Canvas(matriz,width=500, height=500, borderwidth=5, background='white')
# display.grid(column=0, row=0)

# def on_click(i,j,event):
#     global counter
#     color = "red" if counter%2 else "black"
#     event.widget.config(bg=color)
#     board[i][j] = color
#     counter += 1
    
# counter = 0
# board = p.copy()
# for x in range(len(board)):
#     for y in range(len(board[0])):
#           L = Label(matriz,text= board[x][y].info(),bg="blue")
#           L.grid(row= x,column=y)
#           event.widget.config(bg = "black")
#           board[x][y] = "blue"
#           #board[x][y] = Canvas(width=500, height=500, borderwidth=5, background='white')
#           #board[x][y].grid(row = x, column = y)
#           #board[x][y].bind('<Button-1>', clicked)
         



window.mainloop()