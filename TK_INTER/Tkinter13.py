from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("800x600+100+100")

def showchoice():
    print(language1.get(),language2.get(),language3.get(),language4.get())
language1 = IntVar()
Checkbutton(text="python",variable=language1).pack(anchor=W)
language2 = IntVar()
Checkbutton(text="java",variable=language2).pack(anchor=W)
language3 = IntVar()
Checkbutton(text="c",variable=language3).pack(anchor=W)
language4 = IntVar()
Checkbutton(text="c#",variable=language4).pack(anchor=W)

Button(text="showchoice",command=showchoice).pack(anchor=W)
root.mainloop()