import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.geometry("200x100")
ttk.Label(window,text="choose")
n=tk.StringVar()
mostchoosen=ttk.Combobox(window,width=27,textvariable=n)
mostchoosen['values']=("A","B","C","D")
mostchoosen.grid(column=1,row=12)
window.mainloop()
