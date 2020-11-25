from tkinter import *
from tkinter import messagebox
top=Tk()
top.title("TPL assignmnet by Parth")
top.geometry("300x400")

def hello():

    #messagebox.askquestion(title="assignment", message="Destroy western civilization?")
    #messagebox.askokcancel(title="assignment", message="Would you like some mulch with that?")
    messagebox.askretrycancel(title="assignment", message="Ask for a date on more time?")
    #messagebox.askyesno(title="assignment", message=None, **options)
    #messagebox.askyesnocancel(title="assignment", message="can you cut dow a tree with herring?")
    #messagebox.showinfo(title="assignment", message="Brain not found!")
    #messagebox.showwarning(title="assignment", message="Your brain may not be the boss!")
    #messagebox.showerror(title="assignment", message="this is an ex-parrot")



B1=Button(top,text="Click Me!",width=25,command=hello)
B1.place(x=35,y=50)
top.mainloop()
