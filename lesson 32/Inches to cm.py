from tkinter import *
root=Tk()
root.title("Inches to centimeter")
root.geometry("500x500")
l1=Label(root,text='Enter the length in inches',bg='blue',fg='red')
e1=Entry()
def inchesToCm():
    inches=e1.get()
    cm=int(inches)*2.54
    global text
    message=f"centimeter={cm} "
    text.insert(END,message)
text=Text(height=3)
button=Button(root,text="convert to cm",command=inchesToCm)
l1.pack()
e1.pack()
text.pack()
button.pack()
root.mainloop()