# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 13:20:22 2021

@author: diego
"""

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Bienvenido")
window.geometry('300x400')

#LABEL
lbl = Label(window, text="Label")
lbl.grid(column=0, row=0)
#LABEL
lbl = Label(window, text="Hola, soy un Label")
lbl.grid(column=1, row=0)
#LABEL
lbl = Label(window, text="Entry")
lbl.grid(column=0, row=1)
#ENTRY
txt = Entry(window,width=10)
txt.grid(column=1, row=1)
#LABEL
lbl = Label(window, text="Button")
lbl.grid(column=0, row=2)
#BOTON
btn = Button(window, text="Click Me")
btn.grid(column=1, row=2)
#LABEL
lbl = Label(window, text="Combobox")
lbl.grid(column=0, row=3)
#COMBOBOX
combo = ttk.Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=1, row=3)
#LABEL
lbl = Label(window, text="Checkbutton")
lbl.grid(column=0, row=5)
#CHECKBUTTON
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='casilla de verificación', var=chk_state)
chk.grid(column=1, row=5)
#LABEL
lbl = Label(window, text="Radiobutton")
lbl.grid(column=0, row=6)
#RADIOBUTTONS
frame_radios = Frame(window)
r_selected = IntVar()
rad1 = Radiobutton(frame_radios, text='First',  value=1, variable=r_selected)
rad2 = Radiobutton(frame_radios, text='Second', value=2, variable=r_selected)
rad3 = Radiobutton(frame_radios, text='Third',  value=3, variable=r_selected)
rad1.grid(column=1, row=6)
rad2.grid(column=1, row=7)
rad3.grid(column=1, row=8)
frame_radios.grid(column=1, row=6)
#LABEL
lbl = Label(window, text="Scala")
lbl.grid(column=0, row=7)
#SCALA
Scala = Scale(window, from_=0, to=10,orient=HORIZONTAL)
Scala.grid(column=1, row=7)
#LABEL
lbl = Label(window, text="Listbox")
lbl.grid(column=0, row=8)
#LISTBOX
listbox = Listbox(window)  
listbox.insert(1,"Bread")  
listbox.insert(2, "Milk")  
listbox.insert(3, "Meat")  
listbox.insert(4, "Cheese")
listbox.insert(5, "Vegetables")
listbox.grid(column=1, row=8)

window.mainloop()