import pyautogui
#import  tkinter as tk

#root = tk.Tk()
#canvas = tk.Canvas(root, width=300, height=300)
#canvas.pack()
#it takes screenshots
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
