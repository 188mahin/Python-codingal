from tkinter import *
from datetime import date
screen=Tk()
screen.title("Widget Application")
screen.geometry("600x500")
lbl=Label(text="hey there",fg="blue",bg="yellow",height=1,width=40)
name_lbl=Label(text="type your Name",fg="white",bg="black")
name_entry=Entry()
def Display():
    name=name_entry.get()
    global message
    message="welcome to the application\nTodays date is:"
    greet="hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
button=Button(text="Begin",font=("Arial",12,"bold"),command=Display)
lbl.pack()
name_lbl.pack()
name_entry.pack()
button.pack()
text_box.pack()
screen.mainloop()
