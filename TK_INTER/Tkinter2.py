from tkinter import *
root = Tk()
root.title("My GUI")

myLable1 = Label(root,text="Hello wporld",fg="red",font=20,bg="yellow").place(x=0,y=0)
myLable2 = Label(root,text="RF").place(x=10,y=30)

root.geometry("800x600+100+100")
root.mainloop()