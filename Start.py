from tkinter import *
from subprocess import call 


root=Tk()
root.title("GetContact")
root.geometry('700x200')
frame = Frame(root)
frame.pack(pady=20,padx=20)

def Open():
    call(["python", "application.py"])

btn=Button(frame,text='Open GetContact',command=Open)
btn.pack()

root.mainloop()
