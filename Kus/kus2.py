from tkinter import *
from PIL.ImageTk import PhotoImage

pen=Tk(className="Kuş")
pen.geometry("305x325")

rsahin=PhotoImage(file="sahin.jpg")
rkartal=PhotoImage(file="kartal.jpg")
ratmaca=PhotoImage(file="atmaca.jpg")

def sahin():
    esahin=Label(pen, image=rsahin)
    esahin.place(x=0,y=150)
def kartal():
    ekartal=Label(pen, image=rkartal)
    ekartal.place(x=0,y=150)
def atmaca():
    eatmaca=Label(pen, image=ratmaca)
    eatmaca.place(x=0,y=150)



sahin_=Button(pen)
sahin_.config(text="Şahin",command=sahin)
sahin_.place(x=60,y=75)


kartal_=Button(pen)
kartal_.config(text="Kartal",command=kartal)
kartal_.place(x=60,y=100)

atmaca_=Button(pen)
atmaca_.config(text="Atmaca",command=atmaca)
atmaca_.place(x=52,y=125)

label=Label(pen)
label.config(text="Hangi Kuş?",font=("Arial",17))
label.place(x=20,y=20)

mainloop()




