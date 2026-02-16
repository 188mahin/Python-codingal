from tkinter import *
root=Tk()
root.title("Password Strength Checker")
root.geometry("500x500")
l1=Label(root,text='Enter your password',bg='light blue')
e1=Entry()

def strengthChecker():
    password=e1.get()
    if len(password)<=5:
        message="password strength is WEAK"
        text=Text(height=4,bg="red")
    elif len(password)>=6 and len(password)<=8:
        message="password strength is MEDIUM"
        text=Text(height=4,bg="yellow")
    elif len(password)>8 and len(password)<=12:
        message="password strength is STRONG"
        text=Text(height=4,bg="light green",fg="black") 
    elif len(password)<12:
        message="password strength is VERY STRONG"
        text=Text(height=4,bg="dark green")
    
    text.insert(END,message)
    text.pack()   


button=Button(root,text="Check Strength",bg="red",command=strengthChecker)
l1.pack()
e1.pack()
button.pack()
root.mainloop()