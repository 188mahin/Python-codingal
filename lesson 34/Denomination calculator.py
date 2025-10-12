from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window=Tk()
window.title("Denomination Calculator")
window.geometry("650x400")
window.configure(bg="light blue")
upload=Image.open("app_img.jpg")
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(window,image=image,bg="light blue")
label.place(x=180,y=20)
label1=Label(window,text="Hello,welcome to the denomination calculator",bg="light blue")
label1.place(relx=0.5,y=340,anchor=CENTER)
def message():
    msgbox=messagebox.showinfo("Alert,do you want to calculate the denomination amount")
    if msgbox=="ok":
        topwin()
btn=Button(window,text="lets get started",command=message)
btn.place(x=260,y=360)
def topwin():
    top=Toplevel()
    top.title("Denomination calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")
    label=Label(top,text="enter total amount",bg="light grey")
    entry=Entry(top)
    label2=Label(top,text="here are the number of notes for each denomination",bg="light grey")
    l1=Label(top,text="2000",bg="light grey")
    l2=Label(top,text="500",bg="light grey")
    l3=Label(top,text="100",bg="light grey")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    def calculator():
        try:
            global amount
            amount=int(entry.get())
            no2000=amount//2000
            amount%=2000
            no500=amount//500
            amount%=500
            no100=amount//100
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t1.insert(END,str(no2000))
            t2.insert(END,str(no500))
            t3.insert(END,str(no100))
        except ValueError:
            messagebox.showerror("error","please enter a valid number")
    btn=Button(top,text="calculate",command=calculator)
    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    label2.place(x=140,y=170)
    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)
    top.mainloop()
window.mainloop()
    



