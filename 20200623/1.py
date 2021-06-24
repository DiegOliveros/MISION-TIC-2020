# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:17:00 2021

@author: diego
"""

from tkinter import *
contador=0
base=Tk()
marco=Frame(base)

def suma():
    global contador
    contador+=1
    texto.configure(text="Resultado: "+str(contador))
def resta():
    global contador
    contador-=1
    texto.configure(text="Resultado: "+str(contador))
def reseteo():
    global contador
    contador=0
    texto.configure(text="Resultado: "+str(contador))
    

listadeautosDerecha=[]
for i in range (12):
    listadeautosDerecha.append(Button(marco, text=str(i), command=suma))
    listadeautosDerecha[i].pack()
    
listadeautosIzquierda=[]
for i in range (9):
    listadeautosDerecha.append(Button(marco, text=str(i), command=suma))
    listadeautosDerecha[i].pack()  
    
listadeautosArribaV=[]
for i in range (4):
    listadeautosDerecha.append(Button(marco, text=str(i), command=suma))
    listadeautosDerecha[i].pack()  
listadeautosArribaH=[]
for i in range (4):
    listadeautosDerecha.append(Button(marco, text=str(i), command=suma))
    listadeautosDerecha[i].pack()  
    
listadeautosAbajoV=[]
for i in range (4):
    listadeautosDerecha.append(Button(marco, text=str(i), command=suma))
    listadeautosDerecha[i].pack()  
    
listadeautoscentro=[]
for i in range (3):
    listadeautosDerecha.append(Button(marco, text=str(i), command=suma))
    listadeautosDerecha[i].pack()
    
texto=Label(marco, text="Resultado: "+str(contador))

marco.pack()

texto.pack()


base.mainloop()