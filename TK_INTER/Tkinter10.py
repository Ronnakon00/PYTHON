from tkinter import *
import tkinter.colorchooser

root = Tk()
root.title("My GUI")
root.geometry("800x600+100+100")

def selectColor():
    color = tkinter.colorchooser.askcolor()
    print(color)
    mylabel = Label(text="HELLO",bg=color[1],font=20).pack()

btn = Button(text="Select Color",command=selectColor).pack()
root.mainloop()