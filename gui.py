from tkinter import *
import ai
import time
m = Tk()
w = Canvas(m,width=450,height=450)
w.pack()
b = Button(text="Hano",command=ai.main)
b.pack()
m.title("Bro ai")
m.mainloop()