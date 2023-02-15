from tkinter import *
import os
pen=Tk(className="Kuş")

def sahin():
    os.startfile("sahin.jpg")

def kartal():
    os.startfile("kartal.jpg")

def atmaca():
    os.startfile("atmaca.jpg")

label=Label(pen)
label.config(text="Hangi Kuş?",font=("Arial",17))
label.place(x=20,y=20)


sahin_=Button(pen)
sahin_.config(text="Şahin",command=sahin)
sahin_.place(x=150,y=75)


kartal_=Button(pen)
kartal_.config(text="kartal",command=kartal)
kartal_.place(x=150,y=100)

atmaca_=Button(pen)
atmaca_.config(text="Atmaca",command=atmaca)
atmaca_.place(x=150,y=125)






mainloop()
