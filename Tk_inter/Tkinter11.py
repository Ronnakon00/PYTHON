from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
root = Tk()
root.title("My GUI")
root.geometry("800x600+100+100")

def selectColor():
    color = askcolor()
    print(color)
    myLabel = Label(text="HELLO",bg=color[1],font=20).pack()

def selectFile():
    fileopen = askopenfilename()
    filecontnt = open(fileopen)
    myLabel = Label(text=filecontnt.read()).pack()


btn = Button(text="Select Color",command=selectFile).pack()
root.mainloop()