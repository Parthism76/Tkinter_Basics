from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title("just Another texxt editor")
menubar=Menu(root)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label ='New File', command = None) 
file.add_command(label ='Open...', command = None) 
file.add_command(label ='Save', command = None) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy) 

help_=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help_)
help_.add_command(label ='Tk Help', command = None) 
help_.add_command(label ='Demo', command = None) 
help_.add_separator() 
help_.add_command(label ='About Tk', command = None)

root.config(menu=menubar)
root.mainloop()
