from tkinter import *
root = Tk()
root.title("My GUI")

myLable1 = Label(root,text="Hello wporld",fg="red",font=20,bg="yellow").grid(row=0,column=0)
myLable2 = Label(root,text="RF").grid(row=1,column=1)

root.geometry("800x600+100+100")
root.mainloop()