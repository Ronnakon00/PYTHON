from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("My GUI")
root.geometry("800x600+100+100")

myMenu = Menu()
root.config(menu=myMenu)

def newwindow() : 
    Window = Tk()
    Window.title("NewWindow")
    Window.geometry("400x400+1200+100")

def abountProgram():
    messagebox.showinfo("Abount Progrram","Ronnakon")

def exitProgram():
    confirm = messagebox.askquestion("ยืนนัน","คุณต้องการปิดโปรแกรมหรือไม่")
    if confirm == "yes":
        root.destroy()

itemMenu = Menu()
itemMenu.add_command(label="Newfile",command=newwindow)
itemMenu.add_command(label="Openfile")
itemMenu.add_command(label="Save")
itemMenu.add_command(label="Abount",command=abountProgram)
itemMenu.add_command(label="Exit",command=exitProgram)

myMenu.add_cascade(label="File",menu=itemMenu)

root.mainloop()