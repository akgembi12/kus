from tkinter import *
from PIL.ImageTk import PhotoImage

pen=Tk(className=" Kuş")
pen.geometry("375x256")


rsahin=PhotoImage(file="sahin.jpg")
rkartal=PhotoImage(file="kartal.jpg")
ratmaca=PhotoImage(file="atmaca.jpg")

def sahin():
    esahin=Label(pen, image=rsahin)
    esahin.place(x=55,y=75)
def kartal():
    ekartal=Label(pen, image=rkartal)
    ekartal.place(x=55,y=75)
def atmaca():
    eatmaca=Label(pen, image=ratmaca)
    eatmaca.place(x=55,y=75)



sahin_=Button(pen)
sahin_.config(text="Şahin",command=sahin)
sahin_.place(x=6,y=100)


kartal_=Button(pen)
kartal_.config(text="Kartal",command=kartal)
kartal_.place(x=6,y=125)

atmaca_=Button(pen)
atmaca_.config(text="Atmaca",command=atmaca)
atmaca_.place(x=1,y=150)


label=Label(pen)
label.config(text="Hangi Kuş?",font=("Arial",25),fg="red")
label.place(x=125,y=25)
mainloop()




