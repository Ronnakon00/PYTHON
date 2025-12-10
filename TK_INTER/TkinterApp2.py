from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Program")

money = IntVar()
label = Label(text="Amount money",font=30).grid(row=0,sticky=W)
et1 = Entry(font = 30,width=30,textvariable=money)
et1.grid(row=0, column=1)

choice = StringVar(value="select money type")
label = Label(text="Select your money type",font=30).grid(row=1,sticky=W)
combo = ttk.Combobox(width=30,font=30,textvariable=choice)
combo["values"]=("EUR","JPY","USD","GBP")
combo.grid(row=1,column=1)

label = Label(text="Amount money", padx=10,font=30).grid(row=2,sticky=W)
et2 = Entry(font = 30,width=30)
et2.grid(row=2, column=1)

def calculate():
    amount = money.get()
    currency = choice.get()
    if(currency == "EUR"):
        et2.delete(0,END)
        result = ((amount*0.026),"EUR")
        et2.insert(0,result)
    elif(currency == "JPY"):
        et2.delete(0,END)
        result = ((amount*3.486),"JPY")
        et2.insert(0,result)
    elif(currency == "USD"):
        et2.delete(0,END)
        result = ((amount*0.031),"USD")
        et2.insert(0,result)
    elif(currency == "GBP"):
        et2.delete(0,END)
        result = ((amount*0.023),"GBP")
        et2.insert(0,result)
    else :
        et2.delete(0,END)
        result = ("ข้อมูลยังไม่ครบ")
        et2.insert(0,result)
        
def clear():
    et2.delete(0,END)

Button(text="Claculate",font=30,width=15,command=calculate).grid(row=3,column=1,sticky=W)
Button(text="Clear",font=30,width=15,command=clear).grid(row=3,column=1,sticky=E)

root.mainloop()