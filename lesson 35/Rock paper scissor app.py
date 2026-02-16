import random
from tkinter import *
root=Tk()
root.title("Rock Paper Scissors App") 
root.geometry("500x500")
options=["rock","paper","scissors"]
label=Label(root,text="enter rock,paper or scissors:",bg="green")
user_choice=Entry()
text=Text(height=5,bg="blue")
text2=Text(height=3,bg="orange")
def RockPaperScissors():
    global message
    comp_choice=random.choice(options)
    if user_choice==comp_choice:
        message="It's a tie!"
    elif user_choice=='rock' and comp_choice=='scissors':
        message="you win! Rock crushes the scissors"
    elif user_choice=='paper' and comp_choice=='rock':
        message="You win! Paper covers the rock"
    elif user_choice=='scissors' and comp_choice=='paper':
        message="You win! scissors cuts through the paper"
    else:
        message="You lose"
        text.insert(END,message)
    message2=comp_choice
    text2.insert(END,message2)

button=Button(root,text="Press to Play!",command=RockPaperScissors)
label.pack()
text.pack()
text2.pack()
button.pack()
user_choice.pack()
button.pack()
root.mainloop()