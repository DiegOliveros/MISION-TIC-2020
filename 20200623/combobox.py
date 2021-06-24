# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 10:12:51 2021

@author: diego
"""

from tkinter import *
from tkinter import ttk

def obtener():
    if int(combo.get())>=18:
        texto.set("Edad: "+combo.get()+". Es mayor de edad")
    else:
         texto.set("Edad: "+combo.get()+". Es mayor de edad")
         
ventana=Tk()
texto= StringVar()
texto.set("Edad:")
combo =ttk.Combobox(ventana)
combo.place(x=50,y=100)
combo["values"]=("15","16","17","18", "19","20","21")
combo.current(1)
boton=Button(ventana, command=obtener, text="Calcular").place(x=80, y =150)
etiqueta=Label(ventana, textvariable=texto).place(x=40,y=200)
ventana.geometry("300x300")
ventana.mainloop()