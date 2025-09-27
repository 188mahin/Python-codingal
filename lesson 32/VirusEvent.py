from tkinter import*
from tkinter import messagebox
window=Tk()
window.geometry("200x300")
def msg():
    messagebox.showwarning("Alert","Stop! Virus found")
button=Button(window,text="scan for Virus",command=msg)
button.place(x=100,y=150)
window.mainloop()

