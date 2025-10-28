from tkinter import *
root=Tk()
root.title("Using Widgets")
root.geometry("600x500")
label=Label(root,text="Enter your name",bg="blue")
entry=Entry()
label1=Label(root,text="Enter your age")
entry1=Entry()
def getEntry():
    name=entry.get()
    age=entry1.get()
    message="hello "+name+". Your age is "+ age
    text_box.insert(END,message)
text_box=Text(height=6)
button=Button(text="click here after filling the inputs",command=getEntry)
button.pack()
label.pack()
entry.pack()
label1.pack()
entry1.pack()
text_box.pack()
root.mainloop()


