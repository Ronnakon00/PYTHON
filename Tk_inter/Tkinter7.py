from tkinter import *
root = Tk()
root.title("My GUI")

myLable1 = Label(root,text="Hello wporld",fg="red",font=20,bg="yellow").pack()
myLable2 = Label(root,text="RF").pack()

def showMassage():
    Label(root,text=txt.get(),fg="red",font=20,bg="yellow").pack()

def openWindow() :
    mywindow = Tk()
    mywindow.title("My GUI")
    mywindow.geometry("400x200+900+100")

txt = StringVar()
Entry(root,textvariable=txt).pack()

btn1 = Button(root,text="select",fg="black",font=50,bg="white",command=showMassage).pack()
btn2 = Button(root,text="openwindows",command=openWindow).pack()
root.geometry("800x600+100+100")

root.mainloop()