import pyautogui
#import  tkinter as tk
import sys
import os
#root = tk.Tk()
#canvas = tk.Canvas(root, width=300, height=300)
#canvas.pack()
#it takes screenshots
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
jol = 1
def screens():
    global jol
    jol += 1
    screenshoters = pyautogui.screenshot()
    screenshoters.save('./screeners/'+str(jol) +".jpg")

"""mybutts = tk.Button(text='Take some clips', command=screens,bg ='red',fg='green',font=20)
canvas.create_window(150,150,window=mybutts)
root.mainloop()
"""
