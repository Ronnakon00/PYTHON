from tkinter import *
root = Tk()
root.title("My GUI")

myLable1 = Label(root,text="Hello wporld",fg="red",font=20,bg="yellow").pack()
btn1 = Button(root,text="select",fg="black",font=50,bg="white").pack()

root.geometry("800x600+100+100")
root.mainloop()