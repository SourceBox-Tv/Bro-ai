from tkinter import *
import threading
m = Tk()
w = Canvas(m,width=450,height=450)
w.pack()
thread = threading.Thread(target="")
#make test_loop terminate when the user exits the window
thread.daemon = True 
thread.start()
b = Button(text="Hano")
b.pack()
m.title("Bro ai")
m.mainloop()