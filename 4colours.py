from tkinter import *
app=Tk()
app.title("GUI_1")
bA=Label(app,text="A" ,width=12,bg='red').grid(column=0,row=0)

bB=Label(app,text="B",width=12,bg='blue').grid(column=0,row=1)

bC=Label(app,text="C",width=12,bg='white').grid(column=0,row=2)
bD=Label(app,text="D",width=12,bg='yellow').grid(column=0,row=3)





app.mainloop()
