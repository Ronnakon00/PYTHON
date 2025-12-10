from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("800x600+100+100")

Label(text="Frist name").grid(row=0)
Label(text="Last name").grid(row=1)
Label(text="Phone number").grid(row=2)

et1=Entry()
et1.grid(row=0,column=1)
et1.insert(0,"Ronnakon")

et2=Entry()
et2.grid(row=1,column=1)
et2.insert(0,"Thanetthamkhun")

et3=Entry()
et3.grid(row=2,column=1)
et3.insert(0,"096363123123")

def deletText():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)

button = Button(text="ล้างข้อมูล",command=deletText).grid(row=3,column=1)

root.mainloop()