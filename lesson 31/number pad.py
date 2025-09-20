from tkinter import *
window=Tk()
window.title("Number pad")
window.geometry("250x300")
f1=Frame(master=window,height=200,width=360,bg="blue")
f1.pack(expand=True,fill="both")
nums=[[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]
for i in range(4):
    f1.columnconfigure(i,weight=1,minsize=75)      
    f1.rowconfigure(i,weight=1,minsize=50)
    for j in range(0,3):
        f2=Frame(master=f1,relief=RAISED,borderwidth=1)
        f2.grid(row=i,column=j,sticky="nsew")
        l1=Label(master=f2,text=nums[i][j],bg="green")
        l1.pack(expand=True,fill="both",padx=3,pady=3)

window.mainloop()


        

