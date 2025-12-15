from tkinter import *
root = Tk()
root.title("โปรแกรมคำนวนหาพื้นที่วงกลม")

Label(text="รัศมี",font=30).grid(row=0,sticky=W)
redius = IntVar()
et1 = Entry(width=30,textvariable=redius,font=30)
et1.grid(row=0,column=1)

Label(text="พื้นที่",font=30).grid(row=1,sticky=W)
et2 = Entry(width=30,font=30)
et2.grid(row=1,column=1)

def calculate():
    et2.delete(0,END)
    cal = 3.14*2*redius.get()
    et2.insert(0,cal)

def dell():
    et1.delete(0,END)
    et2.delete(0,END)


bt1 = Button(text="CAL",command=calculate).grid(row=2,column=1,sticky=W)
bt2 = Button(text="DELET",command=dell).grid(row=2,column=1,sticky=E)
root.mainloop()