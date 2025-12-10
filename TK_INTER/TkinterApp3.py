from tkinter import *
root = Tk()
root.title("Calculator")

content = ""
txt_input = StringVar(value="0")

def btn(number):
    global content
    content = content+str(number)
    txt_input.set(content)

def btnd():
    global content
    char_list = list(content)
    popped_char = char_list.pop()
    new_string = "".join(char_list)
    content = new_string
    txt_input.set(content)

def btnc():
    global content
    content = ""
    txt_input.set(content)

def btrsum():
    global content
    cal = float(eval(content))
    txt_input.set(cal)
    content = ""

display = Entry(root,font=40,textvariable=txt_input,justify="right")
display.grid(row=0,columnspan=4)

#col1 
btn7=Button(root,font=40,text=7,padx=9,command=lambda:btn(7)).grid(row=1,column=0)
btn4=Button(root,font=40,text=4,padx=9,command=lambda:btn(4)).grid(row=2,column=0)
btn1=Button(root,font=40,text=1,padx=9,command=lambda:btn(1)).grid(row=3,column=0)
btnclear=Button(root,font=40,text="<-",padx=5,command=btnd).grid(row=4,column=0)
btnop=Button(root,font=40,text="(",padx=10.5,command=lambda:btn("(")).grid(row=5,column=0)

#col2
btn8=Button(root,font=40,text=8,padx=9,command=lambda:btn(8)).grid(row=1,column=1)
btn5=Button(root,font=40,text=5,padx=9,command=lambda:btn(5)).grid(row=2,column=1)
btn2=Button(root,font=40,text=2,padx=9,command=lambda:btn(2)).grid(row=3,column=1)
btn0=Button(root,font=40,text=0,padx=9,command=lambda:btn(0)).grid(row=4,column=1)
btncl=Button(root,font=40,text=")",padx=10.5,command=lambda:btn(")")).grid(row=5,column=1)

#col3 
btn9=Button(root,font=40,text=9,padx=9,command=lambda:btn(9)).grid(row=1,column=2)
btn6=Button(root,font=40,text=6,padx=9,command=lambda:btn(6)).grid(row=2,column=2)
btn3=Button(root,font=40,text=3,padx=9,command=lambda:btn(3)).grid(row=3,column=2)
btndot=Button(root,font=40,text=".",padx=12,command=lambda:btn(".")).grid(row=4,column=2)
btnC=Button(root,font=40,text="C",padx=8,command=btnc).grid(row=5,column=2)

#col4
btndy=btn9=Button(root,font=40,text="/",padx=11.1,command=lambda:btn("/")).grid(row=1,column=3)
btnti=btn9=Button(root,font=40,text="x",padx=10,command=lambda:btn("*")).grid(row=2,column=3)
btnmi=btn9=Button(root,font=40,text="-",padx=11.2,command=lambda:btn("-")).grid(row=3,column=3)
btnplus=btn9=Button(root,font=40,text="+",padx=8.4,command=lambda:btn("+")).grid(row=4,column=3)
btneq=Button(root,font=40,text="=",padx=8.4,command=btrsum).grid(row=5,column=3)

root.mainloop()
