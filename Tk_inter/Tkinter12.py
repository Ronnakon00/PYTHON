from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("My GUI")
root.geometry("800x600+100+100")

def showChoice():
    choice=language.get()
    if choice == 0:
        messagebox.showinfo("notify","PYTHON")
    elif choice == 2:
        messagebox.showinfo("notify","C")
    elif choice == 1:
        messagebox.showinfo("notify","JAVA")
    elif choice == 3:
        messagebox.showinfo("notify","C#")

language = IntVar()
language.set(2)
Radiobutton(text="Python",variable=language,value=0,command=showChoice).grid(row=0,column=0)
Radiobutton(text="Java",variable=language,value=1,command=showChoice).grid(row=0,column=1)
Radiobutton(text="C",variable=language,value=2,command=showChoice).grid(row=0,column=2)
Radiobutton(text="C#",variable=language,value=3,command=showChoice).grid(row=0,column=3)
root.mainloop()